import yaml
import json
import re
from pathlib import Path
from linkml.generators import JsonSchemaGenerator
from linkml_runtime.utils import schemaview
from linkml_runtime.dumpers import YAMLDumper

# Running from analysis-api-schema repo base directory

# Hardcode list of sample classes that we consider completed
# kebab-case to match existing manually curated jsons
SAMPLE_TYPES: list = [
    'aerosol',
    'aerosol-arm',
    'commercially-purchased',
    'culture-environmental',
    'engineered-strain',
    'field-deployed-terraform',
    'mixed-culture',
    'monet-soil',
    'other-undescribed',
    'plant',
    'pure-culture',
    'sediment',
    'soil',
    'synthesized-material',
    'terraform',
    'water'
]

# Read in all of the sample classes from ./src/analysis_api_schema/schema/sample_classes.yaml
with open("./src/analysis_api_schema/schema/sample_classes.yaml", "r") as f:
    sample_classes = yaml.safe_load(f)

# Pair up Sample classes and SamplingActivity classes from the yaml using the sample type list
lookup: dict = {}
for s in SAMPLE_TYPES:
    sample_subclass_name = s.replace("-", " ").title().replace(" ", "") + "Sample"
    activity_subclass_name = s.replace("-", " ").title().replace(" ", "") + "SamplingActivity"
    lookup[s] = (sample_subclass_name, activity_subclass_name)

# Create compiled sample classes in a temporary YAML file using (xxSample, xxSamplingActivity, and Site) for each sample type
compiled_sample_classes = {
    "id": "https://w3id.org/MONet/analysis-api-schema/submission-classes",
    "name": "analysis-api-schema-submission-classes",
    "title": "MONet Analysis API Submission Sample Type Schema",
    "description": "Temporary LinkML schema files for building submission portal JSON schemas for each sample type",
    "license": sample_classes["license"],
    "see_also": sample_classes["see_also"],
    "prefixes": sample_classes["prefixes"],
    "default_prefix": sample_classes["default_prefix"],
    "default_range": sample_classes["default_range"],
    "imports": sample_classes["imports"] + ["sample_classes", "enums"],
    "classes": {}
}

# Create a SiteMixin class
site_class = sample_classes['classes']['Site']
site_mixin_class = site_class.copy()
site_mixin_class["mixin"]= True

compiled_sample_classes['classes']['SiteMixin'] = site_mixin_class

# For each sample type, create an xxSampleSubmission class that inherits from 
# Site, Sample subclass, and SamplingActivity subclass.
for s in SAMPLE_TYPES:
    # Can't do multiple inheritance in LinkML. Use Site and SamplingActivity as mixins
    sample_subclass_name, activity_subclass_name = lookup[s]
    sample_class = sample_classes['classes'][sample_subclass_name]
    activity_class = sample_classes['classes'][activity_subclass_name]

    activity_mixin_class = activity_class.copy()
    activity_mixin_class["mixin"] = True

    compiled_sample_classes["classes"][activity_subclass_name + "Mixin"] = activity_mixin_class
        
    # Then create each xxSampleSubmission class that inherits from xxSample class using is_a
    # and uses the SiteMixin and xxSamplingActivityMixin
    compiled_sample_classes['classes'][sample_subclass_name + "Submission"] = {
        "is_a": sample_subclass_name,
        "mixins": ["SiteMixin", activity_subclass_name + "Mixin"],
        "description": f"Submission class for {s} samples, combining Site and SamplingActivity information."
    }

# Temporary dump to file so schemaview works better
with open("./src/analysis_api_schema/schema/temp_compiled_sample_classes.yaml", "w") as f:
    yaml.dump(compiled_sample_classes, f)

# Use linkml_runtime SchemaView to convert these all to induced classes
schema_view = schemaview.SchemaView("./src/analysis_api_schema/schema/temp_compiled_sample_classes.yaml")
schema_view.schema.source_file = str("./src/analysis_api_schema/schema/temp_compiled_sample_classes.yaml")  # ensure string path

# Replace all the classes in schema_view.schema.classes with induced classes
for c in schema_view.all_classes().keys():
    schema_view.schema.classes[c] = schema_view.induced_class(c)

materialized = schema_view.materialize_derived_schema()

# Convert every slot annotation with prefix submission_ to that property
# e.g. annotation "submission_pattern" becomes a "pattern" on that slot
# (technically attribute now that the schema is materialized)
for c in materialized.classes:
    for s in materialized.classes[c].attributes:
        if materialized.classes[c].attributes[s].annotations:
            for a in materialized.classes[c].attributes[s].annotations:
                if re.search("^submission_", a):
                    prop = re.sub("^submission_", "", a)
                    val = materialized.classes[c].attributes[s].annotations[a].value
                    materialized.classes[c].attributes[s][f'{prop}'] = val

# Dump to file so JSONschema generator works better
materialized_schema_path = Path("./src/analysis_api_schema/schema/temp_compiled_sample_classes.materialized.yaml")
YAMLDumper().dump(materialized, materialized_schema_path)

generator = JsonSchemaGenerator(materialized, include_null=False)
json_schema = generator.serialize()
json_schema = json.loads(json_schema)

# Look in each $defs - class - properties - (slot name) - $ref for a reference to an enum.
# Replace "$ref": "#/$defs/xx" with "enum": [contents of xx enum]
json_schema_cleaned = json_schema.copy()
for d in json_schema_cleaned["$defs"]:
    if "Submission" in d:
        for p in json_schema_cleaned["$defs"][d]["properties"]:
            if "$ref" in json_schema_cleaned["$defs"][d]["properties"][p]:
                ref = json_schema_cleaned["$defs"][d]["properties"][p]["$ref"]
                if re.search("^#/\$defs/.*", ref):
                    enum_name = re.sub("^#/\$defs/", "", ref)
                    enum_values = json_schema_cleaned["$defs"][enum_name]["enum"]
                    json_schema_cleaned["$defs"][d]["properties"][p].pop("$ref")
                    json_schema_cleaned["$defs"][d]["properties"][p]["enum"] = enum_values

# # Write out temp json schema dump for debugging
# with open("./src/submission_schema/temp_json_schema.json", "w") as f:
#     json.dump(json_schema_cleaned, f, indent=2)

# Break out each submission class from $defs into its own json schema file
for sample_type in SAMPLE_TYPES:
    sample_subclass_name, _ = lookup[sample_type]
    submission_class_name = sample_subclass_name + "Submission"
    submission_schema = {
        "$schema": json_schema_cleaned["$schema"],
        "header": {
            "title": f"{sample_type.replace('-', ' ').title()} Sample Schema",
            "description": f"JSON schema for {sample_type} sample submissions.",
            "version": "1.0.0" # TODO figure out versioning
        },
        "items": {
            "additionalProperties": False,
            "properties": json_schema_cleaned["$defs"][submission_class_name]["properties"],
            "required": json_schema_cleaned["$defs"][submission_class_name]["required"],
            "type": "object"
        },
        "type": "array"
    }

    # Write the JSON schema to file
    output_dir = "./src/submission_schema"
    output_file = f"{output_dir}/{sample_type}.json"
    with open(output_file, "w") as f:
        json.dump(submission_schema, f, indent=2)

# Delete temp files created above
temp_files = [
    "./src/analysis_api_schema/schema/temp_compiled_sample_classes.yaml",
    "./src/analysis_api_schema/schema/temp_compiled_sample_classes.materialized.yaml",
    "./src/submission_schema/temp_json_schema.json"
]
for temp_file in temp_files:
    if Path(temp_file).exists():
        Path(temp_file).unlink()