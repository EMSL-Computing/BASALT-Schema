## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Generate the SQLAlchemy declarative models (schema.py)
[group('model development')]
gen-sqlalchemy:
  uv run python util/sqlalchemygen.py {{ source_schema_path }} > {{ pymodel }}/schema.py
  uv run python util/fix_encoding.py {{ pymodel }}/schema.py

# Generate the custom Pydantic models (models.py)
[group('model development')]
gen-models:
  uv run python util/pydanticgen.py {{ source_schema_path }} > {{ pymodel }}/models.py
  uv run python util/fix_encoding.py {{ pymodel }}/models.py

# Generate both hand-rolled ORM/model artifacts (schema.py + models.py)
[group('model development')]
gen-orm: gen-sqlalchemy gen-models

# Excluded from gen-project because it accounts for ~97% of that recipe's
# runtime; expect this to take roughly 8 minutes.

# Generate the xlsx data-entry template on demand (slow, ~8 min)
[group('model development')]
gen-excel:
  uv run gen-project {{ config_yaml }} -I excel -d {{ dest }} {{ source_schema_path }}
