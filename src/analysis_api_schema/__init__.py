"""analysis-api-schema.

Data schema for analysis database at EMSL (PNNL).
"""

try:
    from analysis_api_schema._version import __version__, __version_tuple__
except ImportError:  # pragma: no cover
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)
