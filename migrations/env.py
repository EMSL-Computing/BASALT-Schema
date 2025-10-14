from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from sqlalchemy import VARCHAR, Text
from sqlalchemy.dialects import postgresql

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
from schema import metadata
target_metadata = metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def should_ignore_column_migration(table_name, column_name, inspected_type, metadata_type):
    """
    Function to determine if a column migration should be ignored based on
    table name, column name, and PostgreSQL types (JSON, ARRAY, JSONB).
    
    Args:
        table_name (str): Name of the table
        column_name (str): Name of the column
        inspected_type: The type found in the database
        metadata_type: The type defined in the metadata
    
    Returns:
        bool: True if migration should be ignored, False otherwise
    """
    # Check if either type is a PostgreSQL JSON, ARRAY, or JSONB type
    postgresql_types_to_ignore = (
        postgresql.JSON,
        postgresql.JSONB,
        postgresql.ARRAY
    )
    
    # Check if inspected_type or metadata_type is one of the types we want to ignore
    if (isinstance(inspected_type, postgresql_types_to_ignore) or
        isinstance(metadata_type, postgresql_types_to_ignore)):
        print(f"Ignoring migration for {table_name}.{column_name} - PostgreSQL type detected: "
              f"inspected={type(inspected_type).__name__}, metadata={type(metadata_type).__name__}")
        return True
    
    return False


def include_object(object, name, type_, reflected, compare_to):
    """
    Function to determine whether to include an object in the migration.
    Return False to exclude the object from migrations.
    
    This function prevents accidental index drops and specific column additions.
    """
    # Prevent index drops
    if type_ == "index" and reflected and not compare_to:
        print(f"Preventing drop of index: {name}")
        return False
    
    # Prevent specific column additions by table.column name
    if type_ == "column" and not reflected:
        # This is a column addition - get table name from object
        table_name = object.table.name if hasattr(object, 'table') else 'unknown'
        column_name = name
        
        # List of specific columns to ignore (table.column format)
        columns_to_ignore = [
            'instrumentCustodian.id',
            'sampling_activity_site_metadata_link.id',
            'workflowExecutionFunctionalAnnotation.id'
        ]
        
        full_column_name = f"{table_name}.{column_name}"
        if full_column_name in columns_to_ignore:
            print(f"Preventing addition of column: {full_column_name}")
            return False
    
    # Allow all other operations
    return True


def compare_type(context, inspected_column, metadata_column, inspected_type, metadata_type):
    """
    Custom type comparison function to ignore certain type changes.
    Return False to ignore the difference, True to include it in migrations.
    
    Right now triggers for:
    - VARCHAR->Text
    - study.participant_name which is `ARRAY(VARCHAR)`
    - All columns with JSON, ARRAY, or JSONB PostgreSQL types
    
    """
    table_name = inspected_column.table.name
    column_name = inspected_column.name
    
    # Check if we should ignore this column migration based on PostgreSQL types
    if should_ignore_column_migration(table_name, column_name, inspected_type, metadata_type):
        return False
    
    # Ignore specific migration for study.participant_name column
    if (table_name == 'study' and column_name == 'participant_name'):
        print('working...')
        return False
    
    # Ignore VARCHAR <-> Text conversions
    if (isinstance(inspected_type, VARCHAR) and isinstance(metadata_type, Text)) or \
       (isinstance(inspected_type, Text) and isinstance(metadata_type, VARCHAR)):
        return False
    
    return None


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=compare_type,
        include_object=include_object,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    
    
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=compare_type,
            include_object=include_object,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
