import json
import os
import yaml
from pathlib import Path
import pandas as pd

# A script to gather current slot usage information from all the different sample type schemas
# currently used by the ScienceCentral submission portal, so that we can build out the 
# different sample type modelling in monet/analysis-api-schema with all the slot 
# definitions condensed. This is not intended to be reused since the goal is 
# to build the sc submission schemas from analysis-api-schema, this is just to
# get it all in one place first. BJM 01 June 2026

# Set working directory
os.chdir("/home/bmeluch/monet/analysis-api-schema")

# Read in each json schema file in sc-sample-types folder
json_file_list: list = list((Path(os.getcwd()) / "sc-sample-types").glob("*.json"))

sc_schema_dict: dict = {}

for j in json_file_list:
    with open(j, "r") as json_text: 
        sc_schema_dict[j.stem] = json.load(json_text)

print(sc_schema_dict.keys())
# print(sc_schema_dict['soil'].keys())
# print(sc_schema_dict['soil']['header']) # only version important
# print(sc_schema_dict['soil']['items']['properties']['geo_loc_name']) # slots are here, with key, title, type, description, enum, pattern
# print(sc_schema_dict['soil']['items']['required'])
# print(sc_schema_dict['soil']['type']) # not important

# Extract all the slots and the required list for each 
slots_per_sample_type: dict = {}
required_slots_per_sample_type: dict = {}
slot_holder: list = []

for sample_type in sc_schema_dict.keys(): 
    slots_per_sample_type[sample_type] = list(sc_schema_dict[sample_type]['items']['properties'].keys())
    required_slots_per_sample_type[sample_type] = list(sc_schema_dict[sample_type]['items']['required'])
    slot_holder = slot_holder + slots_per_sample_type[sample_type]

# Then, compare slot usages
# this might be a dumb way to uniq a list but whatever
all_sample_slots = list(set(slot_holder))
all_sample_slots.sort()
#print(all_sample_slots)

data_records: list = []

def check_slot_attribute_uniqueness(slot_name: str, property_name: str, slot_details_holder: dict, data_list: list) -> None:
    # Get unique set of property values (eg. all descriptions for this slot from all sample types)
    property_values = set()
    for sample_type in sc_schema_dict.keys():
        # check that property name exists in slot details for this sample type
        if sample_type not in slot_details_holder:
            continue
        if property_name not in slot_details_holder[sample_type]:
            continue
        property_value = slot_details_holder[sample_type][property_name]
        # if property name is enum, we can't add the list to the set, so we convert it to a string first
        if property_name == "enum":
            property_value = '|'.join(property_value)
        # Clean commas
        property_value = property_value.replace(',', '')
        property_values.add(property_value)
        # record all combinations
        data_list.append({
            "slot": slot_name,
            "property": property_name,
            "sample_type": sample_type,
            "value": property_value
        })


# For each slot, check its properties in all the sample schemas
for slot in all_sample_slots:
    slot_details_holder: dict = {}
    for sample_type in sc_schema_dict.keys():
        # If the slot is used in this schema
        if slot in slots_per_sample_type[sample_type]:
            # save its details
            slot_details_holder[sample_type] = (
                sc_schema_dict[sample_type]['items']['properties'][slot]
            )
    # Check if all title, descriptions, type, enum in slot_details_holder match
    for property_name in ['title', 'description', 'type', 'enum', 'pattern']:
        check_slot_attribute_uniqueness(slot, property_name, slot_details_holder, data_records)

# Create pandas dataframe from collected data
slot_usage_df: pd.DataFrame = pd.DataFrame(data_records)
#print(slot_usage_df.head())

# Group by slot name and property name. add a column counting unique values.
# Add a column listing the sample types that use that slot/property combination.
# Retain the value column.
slot_usage_df: pd.DataFrame = slot_usage_df.groupby(['slot', 'property', 'value']).agg(
    sample_type_count=('sample_type', lambda x: len(set(x))),
    sample_types=('sample_type', lambda x: ', '.join(x.unique())),
).reset_index()
#print(slot_usage_df.head())

# Add a column to denote primary slot value, modification, or manual_review.
# If there is ONE value used in the most sample types, mark those rows as primary and the rest of the values for that slot/property combo as modifications.
# If there is more than one majority value, mark them as manual_review.
def determine_primary_value(group: pd.DataFrame) -> pd.DataFrame:
    max_count = group['sample_type_count'].max()
    majority_values = group[group['sample_type_count'] == max_count]
    if len(majority_values) == 1:
        group['primary_or_modification'] = group.apply(
            lambda row: 'primary' if row['value'] == majority_values['value'].iloc[0] else 'modification', axis=1
        )
    else:
        group['primary_or_modification'] = 'manual_review'
    return group

slot_usage_df = slot_usage_df.groupby(['slot', 'property']).apply(determine_primary_value).reset_index(drop=True)
#print(slot_usage_df.head())

# Write the summary to a csv for review
# slot_usage_df.to_csv("./sc-sample-types/slot_attribute_check.csv", index=False)

################ MANUAL REVIEW: READ BACK IN FROM MODIFIED CSV ################
# By hand, review the "manual_review" rows and change them to primary or mod.
slot_usage_df_manual: pd.DataFrame = pd.read_csv(
    "./sc-sample-types/slot_attribute_check_manual.csv"
    )
###############################################################################

# Add rows for required slots from required_slots_per_sample_type
for sample_type, required_slots in required_slots_per_sample_type.items():
    for slot in required_slots:
        slot_usage_df_manual = pd.concat([slot_usage_df_manual, pd.DataFrame([{
            'slot': slot,
            'property': "required",
            'value': True,
            'sample_type_count': 1,
            'sample_types': sample_type,
            'primary_or_modification': 'modification'
        }])], ignore_index=True)

# Filter to "primary" rows
primary_slots_df: pd.DataFrame = slot_usage_df_manual[slot_usage_df_manual['primary_or_modification'] == 'primary']
# Confirm that there is only one primary value per slot/property combination
primary_value_counts: pd.DataFrame = primary_slots_df.groupby(['slot', 'property']).size().reset_index(name='primary_value_count')

if (primary_value_counts['primary_value_count'] > 1).any():
    raise ValueError(f"Error: There should be only one primary value per slot/property combination. Found:\n{primary_value_counts[primary_value_counts['primary_value_count'] > 1]}")

# Create a dictionary of slots where they keys are slot names and the values are dictionaries containing (property name, primary value) pairs
primary_slot_definitions: dict = {}
for _, row in primary_slots_df.iterrows():
    slot_name = row['slot']
    property_name = row['property']
    primary_value = row['value']
    # Convert any "type" properties to "range"
    if property_name == "type":
        property_name = "range"
    if slot_name not in primary_slot_definitions:
        primary_slot_definitions[slot_name] = {}
    primary_slot_definitions[slot_name][property_name] = primary_value
# print(primary_slot_definitions)

# Filter to "modification" rows
# Now create a dictionary of slot_usage modifications where the keys are sample types and the values are dictionaries of (slot: (property_name, modification_value)) pairs
modification_rows_df: pd.DataFrame = slot_usage_df_manual[slot_usage_df_manual['primary_or_modification'] == 'modification']
slot_usages: dict = {}
for _, row in modification_rows_df.iterrows():
    slot_name = row['slot']
    property_name = row['property']
    modification_value = row['value']
    sample_types = row['sample_types'].split(', ')
    # Convert any "type" properties to "range"
    if property_name == "type":
        property_name = "range"
    for sample_type in sample_types:
        if sample_type not in slot_usages:
            slot_usages[sample_type] = {}
        if slot_name not in slot_usages[sample_type]:
            slot_usages[sample_type][slot_name] = {}
        slot_usages[sample_type][slot_name][property_name] = modification_value
#print(slot_usages)

# Write out the primary slot definitions to a yaml file
with open("./sc-sample-types/primary_slot_definitions_generated.yaml", "w") as yaml_file:
    yaml.dump(primary_slot_definitions, yaml_file)


# Break up slots by superclass
# some of the slots will go on sampling activity
sampling_activity_slots: list = [
    'collection_date',
    'collection_time',
    'sample_collected',
    'sample_collection_dev',
    'sample_collection_method',
    'sample_end_time',
    'sample_start_time',
    'sampling_duration',
    'shipped_sample_size',
    'bulk_elect_conductivity',
    'humidity',
    'infiltration_1',
    'infiltration_2',
    'infiltration_notes',
    'storage_condt',
    'weather',
    'wind_direction',
    'wind_speed',
    'within_17_oz'
]

# some of the slots will go on site metadata
site_metadata_slots: list = [
    'alt',
    'latitude', # lat_lon in analysis-api schema
    'longitude',
    'cur_land_use',
    'drainage_class',
    'fao_class',
    'neon_domain',
    'annual_precpt',
    'annual_temp',
    'season_temp',
    'season_precpt',
    'atmospheric_data',
    'crop_rotation',
    'cur_vegetation',
    'cur_vegetation_meth',
    'ecoregion',
    'elev',
    'env_broad_scale',
    'env_local_scale',
    'env_medium',
    'extreme_event',
    'fire',
    'flooding',
    'geo_loc_name',
    'growth_facil',
    'other_growth_facil',
    'link_climate_info',
    'local_class',
    'local_class_meth',
    'neon_plot_id',
    'previous_land_use',
    'previous_land_use_meth',
    'slope_aspect',
    'slope_gradient',
    'profile_position',
    'tillage'
]

sample_class_slots: list = [s for s in all_sample_slots if s not in sampling_activity_slots and s not in site_metadata_slots]

# Create a dictionary where the keys are the sample type keys and the values are SampleClassNames
sc_sample_to_class_name: dict = {
    'field-deployed-terraform': 'FieldDeployedTerraformSample',
    'other-undescribed': 'OtherUndescribedSample',
    'soil': 'SoilSample',
    'water': 'WaterSample',
    'aerosol': 'AerosolSample',
    'aerosol-arm': 'AerosolArmSample',
    'pure-culture': 'PureCultureSample',
    'culture-environmental': 'CultureEnvironmentalSample',
    'commercially-purchased': 'CommerciallyPurchasedSample',
    'mixed-culture': 'MixedCultureSample',
    'sediment': 'SedimentSample',
    'terraform': 'TerraformSample',
    'synthesized-material': 'SynthesizedMaterialSample',
    'monet-soil': 'MonetSoilSample',
    'engineered-strain': 'EngineeredStrainSample',
    'plant': 'PlantSample'
}

# Create a dictionary where the keys are the sample type keys and the values are ___SamplingActivity class names
sc_type_to_activity_name: dict = {
    'field-deployed-terraform': 'FieldDeployedTerraformSamplingActivity',
    'other-undescribed': 'OtherUndescribedSamplingActivity',
    'soil': 'SoilSamplingActivity',
    'water': 'WaterSamplingActivity',
    'aerosol': 'AerosolSamplingActivity',
    'aerosol-arm': 'AerosolArmSamplingActivity',
    'pure-culture': 'PureCultureSamplingActivity',
    'culture-environmental': 'CultureEnvironmentalSamplingActivity',
    'commercially-purchased': 'CommerciallyPurchasedSamplingActivity',
    'mixed-culture': 'MixedCultureSamplingActivity',
    'sediment': 'SedimentSamplingActivity',
    'terraform': 'TerraformSamplingActivity',
    'synthesized-material': 'SynthesizedMaterialSamplingActivity',
    'monet-soil': 'MonetSoilSamplingActivity',
    'engineered-strain': 'EngineeredStrainSamplingActivity',
    'plant': 'PlantSamplingActivity'
}



# Create dictionaries for sample classes and sampling activity classes
sample_classes_with_slots: dict = {}
for sample_type, class_name in sc_sample_to_class_name.items():
    sample_classes_with_slots[class_name] = [s for s in slots_per_sample_type[sample_type] if s in sample_class_slots]
# Create a Sample superclass containing all slots that are shared by all sample types. Remove the shared slots from the sample classes.
shared_slots = set.intersection(*[set(slots) for slots in sample_classes_with_slots.values()])
for class_name in sample_classes_with_slots:
    sample_classes_with_slots[class_name] = [s for s in sample_classes_with_slots[class_name] if s not in shared_slots]
# Add a Sample class to the sample_classes_with_slots dict with the shared slots
sample_classes_with_slots['Sample'] = sorted(shared_slots)

activity_classes_with_slots: dict = {}
for sample_type, activity_name in sc_type_to_activity_name.items():
    activity_classes_with_slots[activity_name] = [s for s in slots_per_sample_type[sample_type] if s in sampling_activity_slots]
# Create a SamplingActivity superclass containing all slots that are shared by all sampling activity types. Remove the shared slots from the sampling activity classes.
shared_activity_slots = set.intersection(*[set(slots) for slots in activity_classes_with_slots.values()])
for class_name in activity_classes_with_slots:
    activity_classes_with_slots[class_name] = [s for s in activity_classes_with_slots[class_name] if s not in shared_activity_slots]
# Add a SamplingActivity class to the activity_classes_with_slots dict with the shared slots
activity_classes_with_slots['SamplingActivity'] = sorted(shared_activity_slots)

# Write out a yaml file of sample classes. The class names are sample_classes_with_slots.keys(),
# the descriptions are blank, there is one attribute which is an identifier,
# the slots are the list of slots in sample_classes_with_slots in alphabetical order    
sample_classes_yaml: dict = {}
slot_usage_holder: dict = {}
for class_name, slots in sample_classes_with_slots.items():
    # Get slot_usages from slot_usages dict for this class/sample type, if they exist
    sample_type = None
    for key, value in sc_sample_to_class_name.items():
        if value == class_name:
            sample_type = key
            break
    try:
        s = {slot: modifications for slot, modifications in slot_usages[sample_type].items() if slot in slots}
    except:
        s = ''

    sample_classes_yaml[class_name] = {
        'description': '',
        'is_a': 'Sample',
        'slots': sorted(slots),
        'attributes': {
            'id': {
                'range': 'uuid',
                'identifier': True
            }
        },
        'slot_usage': s
    }

with open("./sc-sample-types/sample_classes_generated.yaml", "w") as yaml_file:
    yaml.dump(sample_classes_yaml, yaml_file, default_flow_style=False)

# Do the same for SamplingActivity classes
activity_classes_yaml: dict = {}
for class_name, slots in activity_classes_with_slots.items():
    # Get slot_usages from slot_usages dict for this class/sample type, if they exist
    sample_type = None
    for key, value in sc_type_to_activity_name.items():
        if value == class_name:
            sample_type = key
            break
    try:
        s = {slot: modifications for slot, modifications in slot_usages[sample_type].items() if slot in slots}
    except:
        s = ''

    activity_classes_yaml[class_name] = {
        'description': '',
        'is_a': 'SamplingActivity',
        'slots': sorted(slots),
        'attributes': {
            'id': {
                'range': 'uuid',
                'identifier': True
            }
        },
        'slot_usage': s
    }

with open("./sc-sample-types/sampling_activity_classes_generated.yaml", "w") as yaml_file:
    yaml.dump(activity_classes_yaml, yaml_file, default_flow_style=False)

# And write out a SiteMetadata class including all slot usages from any sample type
site_metadata_class_yaml: dict = {
    'SiteMetadata': {
        'description': '',
        'slots': sorted(site_metadata_slots),
        'attributes': {
            'id': {
                'range': 'uuid',
                'identifier': True
            }
        },
        'slot_usage': {slot: slot_usages.get(sample_type, {}).get(slot, '') for slot in site_metadata_slots for sample_type in sc_schema_dict.keys()}
    }
}
with open("./sc-sample-types/site_metadata_class_generated.yaml", "w") as yaml_file:
    yaml.dump(site_metadata_class_yaml, yaml_file, default_flow_style=False)

# CHECK are all slots listed on either a Sample, SamplingActivity, or SiteMetadata class? ONE AND ONLY ONE OF THOSE
all_class_slots = set()
for class_yaml in [sample_classes_yaml, activity_classes_yaml, site_metadata_class_yaml]:
    for class_name, class_details in class_yaml.items():
        all_class_slots.update(class_details['slots'])
missing_slots = set(all_sample_slots) - all_class_slots
if missing_slots:
    print(f"Warning: The following slots are missing from all classes: {missing_slots}")
else:
    print("All slots are accounted for in the classes.")

# Then copy paste as you please into main schema files.

