#!/usr/bin/env python3
"""
Script to upload example SampleBase and SamplingActivity records to a localhost PostgreSQL instance.
Uses the schema defined in migrations/schema.py and database configuration from migrations/alembic.ini.
"""

import sys
import os
from datetime import datetime
from uuid import uuid4
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

# Add migrations directory to path to import schema
sys.path.append(os.path.join(os.path.dirname(__file__), 'migrations'))

from schema import (
    Base, Study, SamplingActivity, SampleBase, Sample, 
    QuantityValue, GeolocationValue, SoilSample
)

# Database configuration from alembic.ini
DATABASE_URL = "postgresql+psycopg2://developer:developer@localhost:5432/emsl1000soils"

def create_database_session():
    """Create database engine and session."""
    engine = create_engine(DATABASE_URL, echo=True)
    Session = sessionmaker(bind=engine)
    return Session(), engine

def create_example_study():
    """Create an example study record."""
    return Study(
        id=uuid4(),
        participant_name="Dr. Jane Smith",
        principal_investigator="Dr. John Doe",
        collaborating_institution="Pacific Northwest National Laboratory",
        project_status="active",
        project_start=datetime(2024, 1, 1),
        project_end=datetime(2024, 12, 31),
        proposal_title="Soil Microbiome Analysis in Agricultural Systems",
        proposal_abstract="A comprehensive study of soil microbial communities in various agricultural systems to understand their role in nutrient cycling and plant health.",
        project_id="PROJ_2024_001"
    )

def create_example_quantity_value():
    """Create an example elevation quantity value."""
    return QuantityValue(
        id=uuid4(),
        description="Site elevation above sea level",
        has_value_unit="meter",
        has_unit="m",
        has_numeric_value=150.5,
        has_raw_value="150.5 meters"
    )

def create_example_geolocation():
    """Create an example geolocation value."""
    return GeolocationValue(
        id=uuid4(),
        description="Agricultural field location in Pacific Northwest",
        latitude=47.6062,
        longitude=-122.3321,
        type="GPS coordinates",
        was_generated_by="Handheld GPS device"
    )

def create_example_sampling_activity(study_id, elev_id, lat_lon_id):
    """Create an example sampling activity record."""
    return SamplingActivity(
        id=uuid4(),
        study_id=study_id,
        type='soil',
        sample_name="PNW_AG_SOIL_001",
        lims_barcode="LIMS_001_2024",
        alt_id=uuid4(),
        elev_id=elev_id,
        lat_lon_id=lat_lon_id,
        growth_facil='field',
        oxygen_relationship='aerobic',
        sample_store_temp='frozen20',
        samp_biotic_relationship='free_living',
        storage_condt='frozen',
        collection_date=datetime(2024, 6, 15, 10, 30),
        collection_time=datetime(2024, 6, 15, 10, 30),
        geo_loc_name="Pacific Northwest Agricultural Field Site",
        ph=6.8,
        ph_meth="Standard pH meter measurement",
        salinity=0.2,
        salinity_method="Conductivity measurement",
        sample_collected="Surface soil (0-10cm depth)",
        sample_collection_dev="Soil auger",
        sample_collection_method="Standard soil sampling protocol",
        sample_start_time=datetime(2024, 6, 15, 10, 30),
        sample_end_time=datetime(2024, 6, 15, 11, 0),
        season_environment="Early summer growing season",
        shipped_sample_size="500g"
    )

def create_example_sample_base():
    """Create an example sample base record."""
    return SampleBase(
        id=uuid4(),
        sample_name="PNW_AG_SOIL_001",
        proposal_id=12345,
        sampling_set="Pacific_Northwest_Agricultural_Survey_2024",
        sample_base_type='sample'
    )

def create_example_sample(sample_base_id, sampling_activity_id):
    """Create an example sample record."""
    return Sample(
        id=sample_base_id,
        sampling_activity_id=sampling_activity_id,
        type='soil',
        guid_source="Laboratory generated",
        other_guid_source=None
    )

def create_example_soil_sample(sample_id):
    """Create an example soil sample record."""
    return SoilSample(
        id=sample_id,
        soil_type='surface_layer'
    )

def upload_sample_data():
    """Main function to upload example data to the database."""
    print("Starting upload of example SampleBase and SamplingActivity records...")
    
    try:
        # Create database session
        session, engine = create_database_session()
        
        print("Connected to database successfully.")
        
        # Create example records
        print("Creating example records...")
        
        # Create supporting records first
        study = create_example_study()
        elevation = create_example_quantity_value()
        geolocation = create_example_geolocation()
        
        # Add supporting records to session
        session.add(study)
        session.add(elevation)
        session.add(geolocation)
        session.flush()  # Get IDs without committing
        
        print(f"Created study with ID: {study.id}")
        print(f"Created elevation with ID: {elevation.id}")
        print(f"Created geolocation with ID: {geolocation.id}")
        
        # Create sampling activity
        sampling_activity = create_example_sampling_activity(
            study.id, elevation.id, geolocation.id
        )
        session.add(sampling_activity)
        session.flush()
        
        print(f"Created sampling activity with ID: {sampling_activity.id}")
        
        # Create sample base
        sample_base = create_example_sample_base()
        session.add(sample_base)
        session.flush()
        
        print(f"Created sample base with ID: {sample_base.id}")
        
        # Create sample
        sample = create_example_sample(sample_base.id, sampling_activity.id)
        session.add(sample)
        session.flush()
        
        print(f"Created sample with ID: {sample.id}")
        
        # Create soil sample
        soil_sample = create_example_soil_sample(sample.id)
        session.add(soil_sample)
        
        print(f"Created soil sample with ID: {soil_sample.id}")
        
        # Commit all changes
        session.commit()
        print("Successfully uploaded all example records to the database!")
        
        # Print summary
        print("\n=== Upload Summary ===")
        print(f"Study: {study.participant_name} - {study.proposal_title}")
        print(f"Sampling Activity: {sampling_activity.sample_name} at {sampling_activity.geo_loc_name}")
        print(f"Sample Base: {sample_base.sample_name} (Type: {sample_base.sample_base_type})")
        print(f"Sample: {sample.type} sample with GUID source: {sample.guid_source}")
        print(f"Soil Sample: {soil_sample.soil_type}")
        
    except IntegrityError as e:
        print(f"Database integrity error: {e}")
        session.rollback()
        return False
    except Exception as e:
        print(f"Error uploading data: {e}")
        session.rollback()
        return False
    finally:
        session.close()
    
    return True

def create_batch_data():
    """Create a batch of multiple sample records."""
    print("Starting upload of batch SampleBase and SamplingActivity records...")
    
    try:
        session, engine = create_database_session()
        print("Connected to database successfully.")
        
        # Create one study for all samples
        study = create_example_study()
        session.add(study)
        session.flush()
        
        batch_size = 5
        print(f"Creating batch of {batch_size} sample records...")
        
        for i in range(batch_size):
            # Create unique supporting records for each sample
            elevation = QuantityValue(
                id=uuid4(),
                description=f"Site elevation for sample {i+1}",
                has_value_unit="meter",
                has_unit="m",
                has_numeric_value=150.0 + (i * 10),
                has_raw_value=f"{150.0 + (i * 10)} meters"
            )
            
            geolocation = GeolocationValue(
                id=uuid4(),
                description=f"Location for sample {i+1}",
                latitude=47.6062 + (i * 0.001),
                longitude=-122.3321 + (i * 0.001),
                type="GPS coordinates",
                was_generated_by="Handheld GPS device"
            )
            
            session.add(elevation)
            session.add(geolocation)
            session.flush()
            
            # Create sampling activity
            sampling_activity = SamplingActivity(
                id=uuid4(),
                study_id=study.id,
                type='soil',
                sample_name=f"BATCH_SOIL_{i+1:03d}",
                lims_barcode=f"LIMS_{i+1:03d}_2024",
                elev_id=elevation.id,
                lat_lon_id=geolocation.id,
                growth_facil='field',
                oxygen_relationship='aerobic',
                sample_store_temp='frozen20',
                storage_condt='frozen',
                collection_date=datetime(2024, 6, 15 + i),
                geo_loc_name=f"Field Site {i+1}",
                ph=6.5 + (i * 0.1),
                sample_collected=f"Surface soil sample {i+1}"
            )
            
            # Create sample base
            sample_base = SampleBase(
                id=uuid4(),
                sample_name=f"BATCH_SOIL_{i+1:03d}",
                proposal_id=12345,
                sampling_set="Batch_Upload_Test_2024",
                sample_base_type='sample'
            )
            
            # Create sample
            sample = Sample(
                id=sample_base.id,
                sampling_activity_id=sampling_activity.id,
                type='soil',
                guid_source="Batch upload script"
            )
            
            # Create soil sample
            soil_sample = SoilSample(
                id=sample.id,
                soil_type='surface_layer'
            )
            
            session.add(sampling_activity)
            session.add(sample_base)
            session.add(sample)
            session.add(soil_sample)
            
            print(f"Created sample set {i+1}/{batch_size}")
        
        session.commit()
        print(f"Successfully uploaded batch of {batch_size} sample records!")
        
    except Exception as e:
        print(f"Error uploading batch data: {e}")
        session.rollback()
        return False
    finally:
        session.close()
    
    return True

if __name__ == "__main__":
    print("Sample Data Upload Script")
    print("=" * 40)
    
    if len(sys.argv) > 1 and sys.argv[1] == "--batch":
        success = create_batch_data()
    else:
        success = upload_sample_data()
    
    if success:
        print("\n✅ Upload completed successfully!")
    else:
        print("\n❌ Upload failed!")
        sys.exit(1)