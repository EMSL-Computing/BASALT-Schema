#!/usr/bin/env python3
"""
Generate formatted SQL DDL from LinkML schema
"""

from linkml.generators.sqltablegen import SQLTableGenerator
import re

def format_sql_ddl(sql_content):
    """Format the SQL DDL for better readability"""
    
    # Split into individual statements
    statements = sql_content.split(';')
    formatted_statements = []
    
    for stmt in statements:
        stmt = stmt.strip()
        if not stmt:
            continue
            
        # Add proper spacing and formatting
        if stmt.startswith('CREATE TABLE'):
            formatted_statements.append('\n-- ' + '='*80)
            formatted_statements.append(stmt + ';')
        elif stmt.startswith('CREATE INDEX'):
            formatted_statements.append(stmt + ';')
        else:
            formatted_statements.append(stmt + ';')
    
    return '\n'.join(formatted_statements)

def generate_formatted_sql_ddl(schema_path, output_path):
    """Generate formatted SQL DDL from LinkML schema"""
    try:
        generator = SQLTableGenerator(schema_path)
        sql_ddl = generator.serialize()
        
        # Add header information
        header = """-- ============================================================================
-- MONet Analysis API Schema - SQL DDL
-- Generated from LinkML schema: samples.yaml
-- ============================================================================

"""
        
        formatted_sql = header + format_sql_ddl(sql_ddl)
        
        with open(output_path, 'w') as f:
            f.write(formatted_sql)
        
        print(f"Successfully generated formatted SQL DDL: {output_path}")
        return True
        
    except Exception as e:
        print(f"Error generating SQL DDL: {e}")
        return False

if __name__ == "__main__":
    schema_file = "src/analysis_api_schema/schema/samples.yaml"
    output_file = "project/sqlschema/samples_formatted.sql"
    
    generate_formatted_sql_ddl(schema_file, output_file)