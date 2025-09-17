"""
analysis_api_schema: LinkML-based schema for MONet Analysis API

This package provides LinkML-generated data models, validation, and enrichment
providers for the MONet soil analysis system.
"""

from ._version import __version__

# Import LinkML-generated models (these will be available after schema compilation)
try:
    from .datamodel.analysis_api_schema import *
except ImportError:
    # Models not yet generated - run 'just gen-project' or 'make all' to generate
    pass

# Import providers
from .providers import (
    MetadataProvider,
    SiteCoordinate,
    MetadataResult,
    NASAPowerProvider,
)

__all__ = [
    "__version__",
    # Provider classes
    "MetadataProvider",
    "SiteCoordinate", 
    "MetadataResult",
    "NASAPowerProvider",
    # LinkML-generated models will be added here after generation
]