set shell := ["powershell", "-Command"]

# Lists `just` recipes
default:
    just --list

# set working-directory := "."

src_schema_path := "./src/analysis_api_schema/schema/analysis_api_schema.yaml"
dst_schema_path := "./project"

gen-schema:
    uv run python util/sqlalchemygen.py {{src_schema_path}} > {{dst_schema_path}}/schema.py
    uv run python util/fix_encoding.py {{dst_schema_path}}/schema.py

gen-models:
    uv run python util/pydanticgen.py  {{src_schema_path}} > {{dst_schema_path}}/models.py
    uv run python util/fix_encoding.py {{dst_schema_path}}/models.py

gen-project: gen-schema gen-models

gen-doc:
    uv run gen-doc -d ../docs/ {{src_schema_path}} 

serve-doc:
    uv run mkdocs serve

# deprecating
# gen-enums:
#     # gen-pydantic ../src/analysis_api_schema/schema/enums.yaml > enums.py
#     # python fix_encoding.py enums.py

# Generate DBML based SVG of the schema.
# [working-directory: '../src/analysis_api_schema/schema/']
# render:
#     @echo "Broken - expect failure"
#     linkml generate dbml -s analysis_api_schema.yaml -o pg.dbml
#     dbml-renderer -i pg.dbml -o pg.svg
