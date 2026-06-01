import json
import os
import yaml
from pathlib import Path
import pandas as pd

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
# print(sc_schema_dict['soil']['items']['properties']['geo_loc_name']) # slots are here, with key, title, type, description, enum
# print(sc_schema_dict['soil']['items']['required'])
# print(sc_schema_dict['soil']['type']) # not important

# Extract all the slots and the required list for each 
slots_per_sample_type: dict = {}
required_slots_per_sample_type: dict = {}
slot_holder: list = []

for sample_type in sc_schema_dict.keys(): 
    slots_per_sample_type[sample_type] = list(sc_schema_dict[sample_type]['items']['properties'].keys())
    required_slots_per_sample_type = list(sc_schema_dict[sample_type]['items']['required'])
    slot_holder = slot_holder + slots_per_sample_type[sample_type]

# Then, compare slot usages
# this might be a dumb way to uniq a list but whatever
all_sample_slots = list(set(slot_holder))
all_sample_slots.sort()
print(all_sample_slots)

# initialize log file
fp: str = "./sc-sample-types/slot_attribute_check.csv"
with open(fp, "w") as f:
    f.write("slot,property,sample_type,value\n")

def check_slot_attribute_uniqueness(slot_name: str, property_name: str, slot_details_holder: dict, log_file_path: str = "./sc-sample-types/slot_attribute_check.csv") -> None:
    with open(log_file_path, "a") as f:
        # get unique set of property values (eg. all descriptions for this slot from all sample types)
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
                property_value = ''.join(property_value)
            # Clean commas
            property_value = property_value.replace(',', '')
            property_values.add(property_value)
            # record all combinations
            f.write(f"{slot_name},{property_name},{sample_type},{property_value}\n")
        # if len(property_values) > 1:
        #     print(f"Slot '{slot_name}' has different '{property_name}' values across sample types")


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
    for property_name in ['title', 'description', 'type', 'enum']:
        check_slot_attribute_uniqueness(slot, property_name, slot_details_holder, log_file_path=fp)

# read in csv as a pandas dataframe. there's probably a better way to do this

slot_usage_df: pd.DataFrame = pd.read_csv(fp)
print(slot_usage_df.head())

# group by slot name and property name. add a column counting unique values

# actually just rewrite this all in pandas

# add a column to denote primary slot value, modification, or manual_review
# if there is one majority value, mark those rows as primary and the rest of the values for that slot/property combo as modifications
# if there is more than one majority value, mark them as manual_review

# then decide what to do next

# eventually we want all of the slot definitions in one dictionary

# we want all the sample types to be sample classes, with their slot lists

# some of the slots will go on sampling activity
sampling_activity_slots: list = [
    sample_store_temp,
    other_samp_store_temp,
    other_storage_condt,
    collection_date,
    collection_time,
    sample_collected,
    sample_collection_dev,
    sample_collection_method,
    sample_end_time,
    sample_start_time,
    sampling_duration,
    shipped_sample_size,
    bulk_elect_conductivity,
    depth,
    humidity,
    infiltration_1,
    infiltration_2,
    infiltration_notes,
    season_temp,
    season_precpt,
    storage_condt,
    temp,
    weather,
    wind_direction,
    wind_speed,
    within_17_oz



]

# some of the slots will go on site metadata
site_metadata_slots: list = [
    'alt',
    'latitude', # lat_lon in analysis-api schema
    'longitude',
    cur_land_use,
    drainage_class,
    fao_class,
    neon_domain,
    annual_precpt,
    annual_temp,
    atmospheric_data,
    crop_rotation,
    cur_vegetation,
    cur_vegetation_meth,
    ecoregion,
    elev,
    env_broad_scale,
    env_local_scale,
    env_medium,
    extreme_event,
    fire,
    flooding,
    geo_loc_name,
    growth_facil,
    other_growth_facil,
    link_climate_info,
    local_class,
    local_class_meth,
    neon_plot_id,
    previous_land_use,
    previous_land_use_meth,
    slope_aspect,
    slope_gradient,
    profile_position,
    tillage
]



# and we want all modifications as slot_usage on the appropriate classes

# CHECK are all slots listed on either a Sample, SamplingActivity, or SiteMetadata class? ONE AND ONLY ONE OF THOSE

# write out a generated linkml yaml file with slot definitions and sample classes

# then copy paste as you please into main schema files

