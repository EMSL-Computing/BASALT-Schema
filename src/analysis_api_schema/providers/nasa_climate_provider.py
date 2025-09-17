"""
NASA Climate Provider for MONet site metadata enrichment.

This provider wraps NASA POWER climatology data to work with LinkML-generated
data models, enabling integration with the site enrichment system.
"""

import hashlib
import requests
import time
import json
import logging
import math
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from io import BytesIO
from dataclasses import dataclass

try:
    from minio import Minio
    from minio.error import S3Error
    MINIO_AVAILABLE = True
except ImportError:
    MINIO_AVAILABLE = False

from .metadata_provider import MetadataProvider, SiteCoordinate, MetadataResult

# Import LinkML models - these will be generated from the schema
try:
    from ..datamodel.analysis_api_schema import NASAClimateData, QuantityValue, SiteMetadata
    LINKML_MODELS_AVAILABLE = True
except ImportError:
    LINKML_MODELS_AVAILABLE = False


class NASAPowerClient:
    """Client for fetching NASA POWER climatology data with caching support"""
    
    def __init__(self, cache_days=30, minio_client: Optional[Any] = None):
        self.base_url = "https://power.larc.nasa.gov/api/temporal/climatology/point"
        self.session = requests.Session()
        self.cache_days = cache_days
        self.logger = logging.getLogger(__name__)
        self.minio_client = minio_client if MINIO_AVAILABLE else None
        
        # Set reasonable timeout and headers
        self.session.headers.update({
            'User-Agent': 'MONet-Research/1.0 (Climate data for soil research)'
        })
    
    def get_climate_data(self, latitude: float, longitude: float, cache_key: str) -> dict:
        """
        Get climatology data for a single coordinate with optional caching
        
        Args:
            latitude: Latitude coordinate
            longitude: Longitude coordinate
            cache_key: Cache key provided by the parent provider
            
        Returns:
            Dict with NASA POWER climate parameters
        """
        
        # Check cache if available
        if self.minio_client:
            cached_data = self._load_from_cache(cache_key)
            if cached_data is not None:
                self.logger.debug(f"Cache hit for {cache_key}")
                return cached_data
        
        # Cache miss - fetch from API
        self.logger.info(f"Cache miss for {cache_key}, fetching from NASA POWER API")
        return self._fetch_and_cache_from_api(latitude, longitude, cache_key)
    
    def _fetch_and_cache_from_api(self, latitude: float, longitude: float, cache_key: str) -> dict:
        """
        Fetch data from NASA POWER API and store in cache if available.
        
        Args:
            latitude: Latitude coordinate
            longitude: Longitude coordinate
            cache_key: Cache key for storage
            
        Returns:
            Dict with NASA POWER climate parameters
        """
        params = {
            'parameters': 'T2M,T2M_MAX,T2M_MIN,PRECTOTCORR,WS2M,RH2M,FROST_DAYS,PS,T2MDEW,ALLSKY_SFC_SW_DWN,ALLSKY_SFC_LW_DWN',
            'community': 'AG',
            'longitude': longitude,
            'latitude': latitude,
            'format': 'JSON'
        }
        
        try:
            response = self.session.get(self.base_url, params=params, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                climate_data = self._parse_response(data)
                
                # Save to cache if we got valid data and caching is available
                if climate_data['nasa_mean_annual_temp_c'] is not None and self.minio_client:
                    try:
                        self._save_to_cache(cache_key, climate_data, data)
                        self.logger.info(f"Stored climate data in cache for {cache_key}")
                    except Exception as e:
                        self.logger.warning(f"Failed to store in cache: {e}")
                
                return climate_data
            else:
                self.logger.warning(f"NASA POWER API returned status {response.status_code}")
                return self._get_empty_climate_data()
                
        except Exception as e:
            self.logger.error(f"Error fetching from NASA POWER API: {e}")
            return self._get_empty_climate_data()
    
    def _parse_response(self, data: dict) -> dict:
        """Parse NASA POWER API response into climate data dictionary"""
        
        try:
            if 'properties' in data and 'parameter' in data['properties']:
                params_data = data['properties']['parameter']
                
                # Get monthly climatology data for all parameters
                temp_data = params_data.get('T2M', {})
                temp_max_data = params_data.get('T2M_MAX', {})
                temp_min_data = params_data.get('T2M_MIN', {})
                precip_data = params_data.get('PRECTOTCORR', {})
                wind_data = params_data.get('WS2M', {})
                humidity_data = params_data.get('RH2M', {})
                frost_data = params_data.get('FROST_DAYS', {})
                surface_pressure_data = params_data.get('PS', {})
                dew_point_data = params_data.get('T2MDEW', {})
                shortwave_radiation_data = params_data.get('ALLSKY_SFC_SW_DWN', {})
                longwave_radiation_data = params_data.get('ALLSKY_SFC_LW_DWN', {})
                
                # Calculate annual means from monthly data
                temp_values = list(temp_data.values()) if temp_data else []
                temp_max_values = list(temp_max_data.values()) if temp_max_data else []
                temp_min_values = list(temp_min_data.values()) if temp_min_data else []
                precip_values = list(precip_data.values()) if precip_data else []
                wind_values = list(wind_data.values()) if wind_data else []
                humidity_values = list(humidity_data.values()) if humidity_data else []
                frost_values = list(frost_data.values()) if frost_data else []
                surface_pressure_values = list(surface_pressure_data.values()) if surface_pressure_data else []
                dew_point_values = list(dew_point_data.values()) if dew_point_data else []
                shortwave_radiation_values = list(shortwave_radiation_data.values()) if shortwave_radiation_data else []
                longwave_radiation_values = list(longwave_radiation_data.values()) if longwave_radiation_data else []
                
                # Calculate derived values
                mean_temp = sum(temp_values) / len(temp_values) if temp_values else None
                max_temp = sum(temp_max_values) / len(temp_max_values) if temp_max_values else None
                min_temp = sum(temp_min_values) / len(temp_min_values) if temp_min_values else None
                mean_precip = sum(precip_values) * 365.25 / 12 if precip_values else None  # Convert to annual
                mean_wind = sum(wind_values) / len(wind_values) if wind_values else None
                mean_humidity = sum(humidity_values) / len(humidity_values) if humidity_values else None
                total_frost_days = sum(frost_values) if frost_values else None
                mean_surface_pressure = sum(surface_pressure_values) / len(surface_pressure_values) if surface_pressure_values else None
                mean_dew_point = sum(dew_point_values) / len(dew_point_values) if dew_point_values else None
                mean_shortwave_radiation = sum(shortwave_radiation_values) / len(shortwave_radiation_values) if shortwave_radiation_values else None
                mean_longwave_radiation = sum(longwave_radiation_values) / len(longwave_radiation_values) if longwave_radiation_values else None
                
                # Calculate vapor pressure from dew point using Tetens formula
                mean_vapor_pressure = None
                if mean_dew_point is not None:
                    mean_vapor_pressure = 0.611 * math.exp(17.27 * mean_dew_point / (mean_dew_point + 237.3))
                
                return {
                    'nasa_mean_annual_temp_c': round(mean_temp, 2) if mean_temp else None,
                    'nasa_mean_annual_precip_mm': round(mean_precip, 1) if mean_precip else None,
                    'nasa_max_annual_temp_c': round(max_temp, 2) if max_temp else None,
                    'nasa_min_annual_temp_c': round(min_temp, 2) if min_temp else None,
                    'nasa_mean_wind_speed_ms': round(mean_wind, 2) if mean_wind else None,
                    'nasa_mean_relative_humidity_pct': round(mean_humidity, 1) if mean_humidity else None,
                    'nasa_frost_days_per_year': round(total_frost_days, 0) if total_frost_days else None,
                    'nasa_mean_dew_point_c': round(mean_dew_point, 2) if mean_dew_point else None,
                    'nasa_mean_vapor_pressure_kpa': round(mean_vapor_pressure, 2) if mean_vapor_pressure else None,
                    'nasa_mean_surface_pressure_kpa': round(mean_surface_pressure, 2) if mean_surface_pressure else None,
                    'nasa_mean_shortwave_radiation_wm2': round(mean_shortwave_radiation, 2) if mean_shortwave_radiation else None,
                    'nasa_mean_longwave_radiation_wm2': round(mean_longwave_radiation, 2) if mean_longwave_radiation else None
                }
            else:
                return self._get_empty_climate_data()
                
        except Exception as e:
            self.logger.error(f"Error parsing NASA POWER response: {e}")
            return self._get_empty_climate_data()
    
    def _get_empty_climate_data(self) -> dict:
        """Return empty climate data structure with all None values"""
        return {
            'nasa_mean_annual_temp_c': None,
            'nasa_mean_annual_precip_mm': None,
            'nasa_max_annual_temp_c': None,
            'nasa_min_annual_temp_c': None,
            'nasa_mean_wind_speed_ms': None,
            'nasa_mean_relative_humidity_pct': None,
            'nasa_frost_days_per_year': None,
            'nasa_mean_dew_point_c': None,
            'nasa_mean_vapor_pressure_kpa': None,
            'nasa_mean_surface_pressure_kpa': None,
            'nasa_mean_shortwave_radiation_wm2': None,
            'nasa_mean_longwave_radiation_wm2': None
        }
    
    def _save_to_cache(self, cache_key: str, climate_data: dict, raw_response: dict):
        """Save climate data to cache (MinIO if available)"""
        if not self.minio_client:
            return
            
        try:
            # Create storage object
            storage_data = {
                "cache_key": cache_key,
                "cached_at": datetime.utcnow().isoformat(),
                "climate_data": climate_data,
                "raw_response": raw_response
            }
            
            # Generate object key
            object_key = f"climate-cache/nasa-power/{cache_key}.json"
            
            # Convert to JSON bytes
            json_data = json.dumps(storage_data, indent=2)
            data_bytes = BytesIO(json_data.encode('utf-8'))
            
            # Store in MinIO (bucket name would come from config)
            bucket_name = "monet-storage"  # This should be configurable
            self.minio_client.put_object(
                bucket_name=bucket_name,
                object_name=object_key,
                data=data_bytes,
                length=len(json_data.encode('utf-8')),
                metadata={
                    'Content-Type': 'application/json',
                    'cache-key': cache_key,
                    'provider': 'NASA_POWER',
                    'cached-at': datetime.utcnow().isoformat()
                }
            )
            
        except Exception as e:
            self.logger.error(f"Failed to store in cache: {e}")

    def _load_from_cache(self, cache_key: str) -> Optional[dict]:
        """Load climate data from cache (MinIO if available)"""
        if not self.minio_client:
            return None
            
        try:
            object_key = f"climate-cache/nasa-power/{cache_key}.json"
            bucket_name = "monet-storage"  # This should be configurable
            
            # Get object from MinIO
            response = self.minio_client.get_object(bucket_name, object_key)
            
            # Parse JSON data
            json_data = response.read().decode('utf-8')
            response.close()
            
            storage_data = json.loads(json_data)
            
            # Check if cache is still valid
            cached_at = datetime.fromisoformat(storage_data['cached_at'])
            expiry_time = datetime.utcnow() - timedelta(days=self.cache_days)
            
            if cached_at < expiry_time:
                self.logger.debug(f"Cache expired for key {cache_key}")
                return None
            
            return storage_data['climate_data']
            
        except Exception as e:
            self.logger.debug(f"No cached data found for key {cache_key}: {e}")
            return None


class NASAPowerProvider(MetadataProvider):
    """
    NASA POWER climate data provider for LinkML integration.
    
    Provides climate metadata following the standard MetadataProvider interface
    and returns data compatible with LinkML-generated models.
    """
    
    def __init__(self, cache_days: int = 30, enabled: bool = True, 
                 minio_client: Optional[Any] = None):
        super().__init__(name="NASA_POWER", enabled=enabled, spatial_precision=4)
        self.cache_days = cache_days
        self.minio_client = minio_client if MINIO_AVAILABLE else None
        self._nasa_client = None
    
    @property
    def nasa_client(self):
        """Lazy-load the NASA client"""
        if self._nasa_client is None:
            self._nasa_client = NASAPowerClient(
                cache_days=self.cache_days,
                minio_client=self.minio_client
            )
        return self._nasa_client
    
    def get_metadata(self, site_coordinate: SiteCoordinate) -> MetadataResult:
        """
        Get NASA climate metadata for a single site coordinate.
        
        Args:
            site_coordinate: The geographic location to enrich
            
        Returns:
            MetadataResult with NASA climate data compatible with LinkML models
        """
        if not self.validate_coordinate(site_coordinate):
            return MetadataResult(
                site_coordinate=site_coordinate,
                metadata={},
                source=self.name,
                success=False,
                error_message="Invalid coordinates for NASA provider"
            )
        
        try:
            # Get cache key
            cache_key = self.get_cache_key(site_coordinate)
            
            # Get raw climate data
            climate_data = self.nasa_client.get_climate_data(
                site_coordinate.latitude, 
                site_coordinate.longitude,
                cache_key=cache_key
            )
            
            # Transform to LinkML-compatible structure
            linkml_metadata = self._transform_to_linkml(climate_data, site_coordinate, cache_key)
            
            return MetadataResult(
                site_coordinate=site_coordinate,
                metadata=linkml_metadata,
                source=self.name,
                cache_key=cache_key,
                success=True
            )
            
        except Exception as e:
            return MetadataResult(
                site_coordinate=site_coordinate,
                metadata={},
                source=self.name,
                success=False,
                error_message=f"NASA API error: {str(e)}"
            )
    
    def _transform_to_linkml(self, climate_data: dict, site_coordinate: SiteCoordinate, cache_key: str) -> dict:
        """
        Transform NASA climate data to LinkML-compatible format.
        
        Args:
            climate_data: Raw NASA climate data dictionary
            site_coordinate: Site coordinate information
            cache_key: Cache key for this data
            
        Returns:
            Dictionary compatible with LinkML SiteMetadata and NASAClimateData models
        """
        # Create QuantityValue objects for each climate parameter
        nasa_climate = {}
        
        # Temperature parameters
        if climate_data.get('nasa_mean_annual_temp_c') is not None:
            nasa_climate['nasa_mean_annual_temp_c'] = {
                'numeric_value': climate_data['nasa_mean_annual_temp_c'],
                'unit_code': 'Cel',
                'unit_name': 'degree Celsius'
            }
        
        if climate_data.get('nasa_max_annual_temp_c') is not None:
            nasa_climate['nasa_max_annual_temp_c'] = {
                'numeric_value': climate_data['nasa_max_annual_temp_c'],
                'unit_code': 'Cel',
                'unit_name': 'degree Celsius'
            }
        
        if climate_data.get('nasa_min_annual_temp_c') is not None:
            nasa_climate['nasa_min_annual_temp_c'] = {
                'numeric_value': climate_data['nasa_min_annual_temp_c'],
                'unit_code': 'Cel',
                'unit_name': 'degree Celsius'
            }
        
        # Precipitation
        if climate_data.get('nasa_mean_annual_precip_mm') is not None:
            nasa_climate['nasa_mean_annual_precip_mm'] = {
                'numeric_value': climate_data['nasa_mean_annual_precip_mm'],
                'unit_code': 'mm',
                'unit_name': 'millimeter'
            }
        
        # Wind speed
        if climate_data.get('nasa_mean_wind_speed_ms') is not None:
            nasa_climate['nasa_mean_wind_speed_ms'] = {
                'numeric_value': climate_data['nasa_mean_wind_speed_ms'],
                'unit_code': 'm/s',
                'unit_name': 'meter per second'
            }
        
        # Humidity
        if climate_data.get('nasa_mean_relative_humidity_pct') is not None:
            nasa_climate['nasa_mean_relative_humidity_pct'] = {
                'numeric_value': climate_data['nasa_mean_relative_humidity_pct'],
                'unit_code': '%',
                'unit_name': 'percent'
            }
        
        # Frost days
        if climate_data.get('nasa_frost_days_per_year') is not None:
            nasa_climate['nasa_frost_days_per_year'] = {
                'numeric_value': climate_data['nasa_frost_days_per_year'],
                'unit_code': 'd',
                'unit_name': 'day'
            }
        
        # Additional parameters...
        for param_key, unit_info in [
            ('nasa_mean_dew_point_c', ('Cel', 'degree Celsius')),
            ('nasa_mean_vapor_pressure_kpa', ('kPa', 'kilopascal')),
            ('nasa_mean_surface_pressure_kpa', ('kPa', 'kilopascal')),
            ('nasa_mean_shortwave_radiation_wm2', ('W/m2', 'watt per square meter')),
            ('nasa_mean_longwave_radiation_wm2', ('W/m2', 'watt per square meter'))
        ]:
            if climate_data.get(param_key) is not None:
                nasa_climate[param_key] = {
                    'numeric_value': climate_data[param_key],
                    'unit_code': unit_info[0],
                    'unit_name': unit_info[1]
                }
        
        # Return SiteMetadata-compatible structure
        return {
            'cache_key': cache_key,
            'latitude': site_coordinate.latitude,
            'longitude': site_coordinate.longitude,
            'provider': self.name,
            'enriched_at': datetime.utcnow().isoformat(),
            'created_at': datetime.utcnow().isoformat(),
            'nasa_climate_data': nasa_climate
        }
    
    def get_bulk_metadata(self, site_coordinates: List[SiteCoordinate]) -> List[MetadataResult]:
        """
        Get NASA climate metadata for multiple site coordinates.
        
        Args:
            site_coordinates: List of geographic locations to enrich
            
        Returns:
            List of MetadataResult objects with NASA climate data
        """
        results = []
        for coordinate in site_coordinates:
            result = self.get_metadata(coordinate)
            results.append(result)
        return results
    
    def get_cache_key(self, site_coordinate: SiteCoordinate) -> str:
        """
        Generate a NASA-specific cache key for spatial clustering/deduplication.
        
        Uses spatial rounding (4 decimal places ~11m precision) to create
        MD5 hash for NASA climate data caching.
        
        Args:
            site_coordinate: The geographic location
            
        Returns:
            MD5 hash string for cache key
        """
        return self.generate_spatial_cache_key(
            site_coordinate.latitude, 
            site_coordinate.longitude
        )
    
    def validate_coordinate(self, site_coordinate: SiteCoordinate) -> bool:
        """
        Check if the coordinate is valid for NASA POWER data.
        
        Args:
            site_coordinate: The geographic location to validate
            
        Returns:
            True if coordinate is valid (basic lat/lon bounds check)
        """
        lat = site_coordinate.latitude
        lon = site_coordinate.longitude
        
        # Basic validation - NASA POWER has global coverage
        return -90 <= lat <= 90 and -180 <= lon <= 180