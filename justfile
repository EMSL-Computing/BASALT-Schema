set shell := ["powershell", "-Command"]

# Lists `just` recipes
default:
    just --list

# TODO move out of migration folder
set working-directory := "migrations"

# Generate SQL Alchemy `schema.py` and `enums.py`
gen:
    python sqlalchemygen.py ../src/analysis_api_schema/schema/analysis_api_schema.yaml > schema.py
    python fix_encoding.py schema.py
    gen-pydantic ../src/analysis_api_schema/schema/enums.yaml > enums.py
    python fix_encoding.py enums.py

# Generate DBML based SVG of the schema.
[working-directory: '../src/analysis_api_schema/schema/']
render:
    @echo "Broken - expect failure"
    linkml generate dbml -s analysis_api_schema.yaml -o pg.dbml
    dbml-renderer -i pg.dbml -o pg.svg

# TODO: more work to be done with pydantic - especially for building data verification and constraints
# Will need to adapt UUID's as well - oof
gen-pydantic:
    # @echo "Broken - expect failure"
    # gen-pydantic ../src/analysis_api_schema/schema/analysis_api_schema.yaml > pyd_model.py
    python pydanticgen.py  ../src/analysis_api_schema/schema/analysis_api_schema.yaml > pyd_model.py
    python fix_encoding.py pyd_model.py
