# BASALT Schema Examples

This directory contains example YAML files demonstrating the usage of the LinkML-based BASALT Schema.

## Valid Examples

### Individual Entity Examples

- **`sample-001.yaml`** - Basic soil sample with standard metadata fields
- **`processed-sample-001.yaml`** - Processed sample showing core section data
- **`site-metadata-001.yaml`** - Site metadata enriched with NASA POWER climate data

### Complete Database Example

- **`complete-database-001.yaml`** - Full database structure showing samples, processed samples, and site metadata working together

## Key Features Demonstrated

### Sample Management
- Sample identification with UUIDs and human-readable names
- Sample type classification (soil, aerosol)
- Soil type specialization (surface_layer, soil_core)
- Proposal ID tracking for EMSL integration
- Sampling set organization

### Processed Samples
- Core section processing (TOP, MID, BTM)
- Replicate sample tracking
- Processing type classification

### Site Metadata & Enrichment
- Geographic coordinate storage
- NASA POWER climate data integration
- Quantity values with units (following QUDT patterns)
- Cache key management for efficient lookups
- Provider tracking and timestamps

### Data Quality
- Required vs optional field patterns
- Enum value validation
- Unit consistency with QUDT vocabulary
- Coordinate validation ranges

## Usage

These examples can be used to:

1. **Validate Schema** - Test LinkML schema compilation
2. **Generate Code** - Create Python dataclasses from schema
3. **API Development** - Understand expected data structures
4. **Data Migration** - Template for converting existing MONet data

## Validation

After generating the LinkML models, validate examples with:

```bash
poetry run linkml-validate --schema src/basalt_schema/schema/basalt_schema.yaml src/data/examples/valid/sample-001.yaml
```

## Schema Generation

Generate Python models from schema:

```bash
just gen-project
# or
make all
```