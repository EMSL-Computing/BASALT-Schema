set shell := ["powershell", "-Command"]

# Define a justfile with the specified commands
default := "create-revision"

set working-directory := "migrations"

gen:
    python sqlalchemygen.py ../src/analysis_api_schema/schema/analysis_api_schema.yaml > schema.py
    python fix_encoding.py schema.py
 
    # gen-python ../src/analysis_api_schema/schema/enums.yaml > enums.py
    gen-pydantic ../src/analysis_api_schema/schema/enums.yaml > enums.py
    python fix_encoding.py enums.py


# Recipe: create-revision
create-revision:
    if (Test-Path versions/revision_test.py) { Remove-Item versions/revision_test.py -Force }
    python sqlalchemygen.py ../src/analysis_api_schema/schema/analysis_api_schema.yaml > schema.py
    python fix_encoding.py schema.py
    alembic revision --autogenerate --rev-id="revision" -m "test"

gen-tables:
    python sqltablegen.py ../src/analysis_api_schema/schema/analysis_api_schema.yaml > schema.sql
    python fix_encoding.py schema.sql

gen-pydantic:
    gen-pydantic ../src/analysis_api_schema/schema/analysis_api_schema.yaml > pyd_model.py

test:
    python sqltablegen.py ../src/analysis_api_schema/schema/test.yml > test.sql
    python fix_encoding.py test.sql
    gen-pydantic ../src/analysis_api_schema/schema/test.yml > test.py
    python fix_encoding.py test.py
