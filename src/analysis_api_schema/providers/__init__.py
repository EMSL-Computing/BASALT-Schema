"""
Metadata providers for MONet Analysis API schema.

This package contains providers for external metadata enrichment services
that integrate with LinkML-generated data models.
"""

from .metadata_provider import MetadataProvider, SiteCoordinate, MetadataResult
from .nasa_climate_provider import NASAPowerProvider

__all__ = [
    "MetadataProvider",
    "SiteCoordinate", 
    "MetadataResult",
    "NASAPowerProvider",
]