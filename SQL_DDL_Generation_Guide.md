# SQL DDL/SQLAlchemy Generation Workflow

This document describes how to generate SQL Data Definition Language (DDL) and/or the SQLAlchemy Python ORM classes from the LinkML YAML schema for database testing.

## Quick Start (PowerShell)

Since the `just` command is not available in your PowerShell environment, use Poetry directly:

```powershell
# Navigate to project directory
cd "c:\Users\kapu336\Documents\MONet\analysis-api-schema"

# Generate SQL DDL using our custom script
poetry run python generate_sql.py
```

This will generate `project/sqlschema/samples_ddl.sql` with complete CREATE TABLE statements.

## Alternative Methods

### Method 1a: Direct LinkML Generator (Python API)
```powershell
poetry run python -c "from linkml.generators.sqltablegen import SQLTableGenerator; gen = SQLTableGenerator('src/analysis_api_schema/schema/samples.yaml'); print(gen.serialize())" > project/sqlschema/samples_ddl.sql
```

### Method 1b: SQLA LinkML generator (python API)
```powershell
poetry run python -c "from linkml.generators.sqlalchemygen import SQLAlchemyGenerator; gen = SQLAlchemyGenerator('src/analysis_api_schema/schema/samples.yaml'); print(gen.serialize())" > project/sqlschema/samples_sqla.py
```

### Method 2: Using Just (when available)
If you install `just` command runner:
```bash
just gen-sql
```

## Generated Files

The SQL DDL generation creates:
- `project/sqlschema/samples_ddl.sql` - Main SQL DDL file with CREATE TABLE statements

## Schema Structure

The generated SQL includes tables for:

1. **NamedThing** - Base class for identifiable entities
2. **SampleBase** - Base class for all sample entities
3. **Sample** - Physical samples collected from environment
4. **SoilSample** - Soil-specific samples (inherits from Sample)
5. **AerosolSample** - Aerosol-specific samples (inherits from Sample)
6. **ProcessedSample** - Samples that have undergone processing
7. **CoreSection** - Core sample sections (TOP, MID, BTM)
8. **Replicate** - Sample replicates/aliquots
9. **DNAData** - DNA-related molecular data
10. **RNAData** - RNA-related molecular data
11. **LibraryData** - Library preparation data

## Key Features

- All tables include proper primary keys and indexes
- Enumerated values are constrained with VARCHAR lengths
- Foreign key relationships are preserved
- Field descriptions are included as comments

## Troubleshooting

### Missing Enum Error
If you see "Unknown range: [EnumName]", the enum is not defined in `src/analysis_api_schema/schema/enums.yaml`. Add the missing enum definition.

### PowerShell Command Issues
- Use semicolons (`;`) instead of `&&` for command chaining
- Wrap paths in quotes if they contain spaces
- Use `poetry run` prefix for all LinkML commands

## Next Steps

1. Review the generated SQL DDL in `project/sqlschema/samples_ddl.sql`
2. Share with your colleague for database testing
3. Modify schema as needed and regenerate DDL
4. Consider adding constraints, triggers, or views as required

