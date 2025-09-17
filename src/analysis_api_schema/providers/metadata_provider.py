"""
Abstract base class for metadata providers in MONet site enrichment system.

This module defines the contract that all metadata providers must implement,
enabling a pluggable architecture for different data sources (NASA, USGS, etc.)
that integrates with LinkML-generated data models.
"""

import hashlib
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
from dataclasses import dataclass


@dataclass
class SiteCoordinate:
    """Represents a site's geographic coordinates"""
    latitude: float
    longitude: float
    site_id: Optional[str] = None


@dataclass
class MetadataResult:
    """Standard result format for metadata retrieval with LinkML model integration"""
    site_coordinate: SiteCoordinate
    metadata: Dict[str, Any]
    source: str
    cache_key: Optional[str] = None
    success: bool = True
    error_message: Optional[str] = None


class MetadataProvider(ABC):
    """
    Abstract base class for all metadata providers.
    
    Each provider (NASA, USGS, etc.) must implement these methods
    to participate in the site metadata enrichment system with LinkML models.
    """
    
    SPATIAL_PRECISION_METERS = 11  # ~11m precision at 4 decimal places
    DEFAULT_SPATIAL_PRECISION = 4  # 0.0001 degrees
    
    def __init__(self, name: str, enabled: bool = True, spatial_precision: int = 4):
        self.name = name
        self.enabled = enabled
        self.spatial_precision = spatial_precision  # Decimal places for coordinate rounding
    
    @abstractmethod
    def get_cache_key(self, site_coordinate: SiteCoordinate) -> str:
        """
        Generate a provider-specific cache key for spatial clustering/deduplication.
        
        Each provider should implement their own cache key generation strategy.
        Most providers will use spatial rounding for coordinate-based caching.
        
        Args:
            site_coordinate: The geographic location
            
        Returns:
            Cache key string (typically MD5 hash)
        """
        pass
    
    @abstractmethod
    def get_metadata(self, site_coordinate: SiteCoordinate) -> MetadataResult:
        """
        Get metadata for a single site coordinate.
        
        Args:
            site_coordinate: The geographic location to enrich
            
        Returns:
            MetadataResult with enriched data or error information
        """
        pass
    
    @abstractmethod
    def get_bulk_metadata(self, site_coordinates: List[SiteCoordinate]) -> List[MetadataResult]:
        """
        Get metadata for multiple site coordinates.
        
        Args:
            site_coordinates: List of geographic locations to enrich
            
        Returns:
            List of MetadataResult objects
        """
        pass
    
    @abstractmethod
    def validate_coordinate(self, site_coordinate: SiteCoordinate) -> bool:
        """
        Check if the coordinate is valid for this provider.
        
        Args:
            site_coordinate: The geographic location to validate
            
        Returns:
            True if coordinate is valid for this provider
        """
        pass
    
    def is_enabled(self) -> bool:
        """Check if this provider is currently enabled"""
        return self.enabled
    
    def enable(self):
        """Enable this provider"""
        self.enabled = True
    
    def disable(self):
        """Disable this provider"""
        self.enabled = False
    
    def generate_spatial_cache_key(self, latitude: float, longitude: float) -> str:
        """
        Generate a standard spatial cache key using coordinate rounding.
        
        Args:
            latitude: Latitude coordinate
            longitude: Longitude coordinate
            
        Returns:
            MD5 hash of rounded coordinates
        """
        # Round coordinates to specified precision
        rounded_lat = round(latitude, self.spatial_precision)
        rounded_lon = round(longitude, self.spatial_precision)
        
        # Create cache key string
        cache_string = f"{self.name}_{rounded_lat}_{rounded_lon}"
        
        # Return MD5 hash
        return hashlib.md5(cache_string.encode()).hexdigest()