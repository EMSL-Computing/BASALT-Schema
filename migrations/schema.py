
from sqlalchemy import Column, Index, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()
metadata = Base.metadata


class Database(Base):
    """
    Root container for all MONet analysis data including samples, processed samples, and site metadata
    """
    __tablename__ = 'Database'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    
    
    # One-To-Many: OneToAnyMapping(source_class='Database', source_slot='samples', mapping_type=None, target_class='Sample', target_slot='Database_id', join_class=None, uses_join_table=None, multivalued=False)
    samples = relationship( "Sample", foreign_keys="[Sample.Database_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Database', source_slot='processed_samples', mapping_type=None, target_class='ProcessedSample', target_slot='Database_id', join_class=None, uses_join_table=None, multivalued=False)
    processed_samples = relationship( "ProcessedSample", foreign_keys="[ProcessedSample.Database_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Database', source_slot='site_metadata_collection', mapping_type=None, target_class='SiteMetadata', target_slot='Database_id', join_class=None, uses_join_table=None, multivalued=False)
    site_metadata_collection = relationship( "SiteMetadata", foreign_keys="[SiteMetadata.Database_id]")
    

    def __repr__(self):
        return f"Database(id={self.id},)"



    


class NamedThing(Base):
    """
    A generic grouping for any identifiable entity
    """
    __tablename__ = 'NamedThing'

    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text())
    description = Column(Text())
    

    def __repr__(self):
        return f"NamedThing(id={self.id},name={self.name},description={self.description},)"



    


class DNAData(Base):
    """
    DNA-related data for molecular samples
    """
    __tablename__ = 'DNAData'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    single_cell_lysis_approach = Column(Enum('chemical', 'enzymatic', 'physical', 'combination', name='SingleCellLysisAppr'))
    dna_container_type = Column(Enum('plate', 'tube', name='DnaContTypeEnum'))
    dna_dnase_treatment = Column(Enum('False', 'True', name='DnaDnaseEnum'))
    dna_sample_format = Column(Enum('tris_hcl', 'dna_stable', 'ethanol', 'low_edta_te', 'mda_reaction_buffer', 'pbs', 'pellet', 'rna_stable', 'te', 'water', name='DnaSampleFormatEnum'))
    

    def __repr__(self):
        return f"DNAData(id={self.id},single_cell_lysis_approach={self.single_cell_lysis_approach},dna_container_type={self.dna_container_type},dna_dnase_treatment={self.dna_dnase_treatment},dna_sample_format={self.dna_sample_format},)"



    


class RNAData(Base):
    """
    RNA-related data for molecular samples
    """
    __tablename__ = 'RNAData'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    rna_container_type = Column(Enum('plate', 'tube', name='RnaContTypeEnum'))
    rna_sample_format = Column(Enum('tris_hcl', 'dna_stable', 'ethanol', 'low_edta_te', 'mda_reaction_buffer', 'pbs', 'pellet', 'rna_stable', 'te', 'water', name='RnaSampleFormatEnum'))
    dnase_rna_treatment = Column(Enum('True', 'False', name='DnaseRnaEnum'))
    

    def __repr__(self):
        return f"RNAData(id={self.id},rna_container_type={self.rna_container_type},rna_sample_format={self.rna_sample_format},dnase_rna_treatment={self.dnase_rna_treatment},)"



    


class LibraryData(Base):
    """
    Library preparation data for sequencing samples
    """
    __tablename__ = 'LibraryData'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    lib_layout = Column(Enum('natural_light', 'electric_light', 'desk_lamp', 'fluorescent_lights', 'none', name='LibLayoutEnum'))
    

    def __repr__(self):
        return f"LibraryData(id={self.id},lib_layout={self.lib_layout},)"



    


class QuantityValue(Base):
    """
    A quantity value with numeric value and optional unit
    """
    __tablename__ = 'QuantityValue'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    numeric_value = Column(Float(), nullable=False )
    unit_code = Column(Text())
    unit_name = Column(Text())
    

    def __repr__(self):
        return f"QuantityValue(id={self.id},numeric_value={self.numeric_value},unit_code={self.unit_code},unit_name={self.unit_name},)"



    


class NASAClimateData(Base):
    """
    Climate data from NASA POWER service
    """
    __tablename__ = 'NASAClimateData'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    nasa_mean_annual_temp_c_id = Column(Integer(), ForeignKey('QuantityValue.id'))
    nasa_mean_annual_temp_c = relationship("QuantityValue", uselist=False, foreign_keys=[nasa_mean_annual_temp_c_id])
    nasa_mean_annual_precip_mm_id = Column(Integer(), ForeignKey('QuantityValue.id'))
    nasa_mean_annual_precip_mm = relationship("QuantityValue", uselist=False, foreign_keys=[nasa_mean_annual_precip_mm_id])
    nasa_max_annual_temp_c_id = Column(Integer(), ForeignKey('QuantityValue.id'))
    nasa_max_annual_temp_c = relationship("QuantityValue", uselist=False, foreign_keys=[nasa_max_annual_temp_c_id])
    nasa_min_annual_temp_c_id = Column(Integer(), ForeignKey('QuantityValue.id'))
    nasa_min_annual_temp_c = relationship("QuantityValue", uselist=False, foreign_keys=[nasa_min_annual_temp_c_id])
    nasa_mean_wind_speed_ms_id = Column(Integer(), ForeignKey('QuantityValue.id'))
    nasa_mean_wind_speed_ms = relationship("QuantityValue", uselist=False, foreign_keys=[nasa_mean_wind_speed_ms_id])
    nasa_mean_relative_humidity_pct_id = Column(Integer(), ForeignKey('QuantityValue.id'))
    nasa_mean_relative_humidity_pct = relationship("QuantityValue", uselist=False, foreign_keys=[nasa_mean_relative_humidity_pct_id])
    nasa_frost_days_per_year_id = Column(Integer(), ForeignKey('QuantityValue.id'))
    nasa_frost_days_per_year = relationship("QuantityValue", uselist=False, foreign_keys=[nasa_frost_days_per_year_id])
    nasa_mean_dew_point_c_id = Column(Integer(), ForeignKey('QuantityValue.id'))
    nasa_mean_dew_point_c = relationship("QuantityValue", uselist=False, foreign_keys=[nasa_mean_dew_point_c_id])
    nasa_mean_vapor_pressure_kpa_id = Column(Integer(), ForeignKey('QuantityValue.id'))
    nasa_mean_vapor_pressure_kpa = relationship("QuantityValue", uselist=False, foreign_keys=[nasa_mean_vapor_pressure_kpa_id])
    nasa_mean_surface_pressure_kpa_id = Column(Integer(), ForeignKey('QuantityValue.id'))
    nasa_mean_surface_pressure_kpa = relationship("QuantityValue", uselist=False, foreign_keys=[nasa_mean_surface_pressure_kpa_id])
    nasa_mean_shortwave_radiation_wm2_id = Column(Integer(), ForeignKey('QuantityValue.id'))
    nasa_mean_shortwave_radiation_wm2 = relationship("QuantityValue", uselist=False, foreign_keys=[nasa_mean_shortwave_radiation_wm2_id])
    nasa_mean_longwave_radiation_wm2_id = Column(Integer(), ForeignKey('QuantityValue.id'))
    nasa_mean_longwave_radiation_wm2 = relationship("QuantityValue", uselist=False, foreign_keys=[nasa_mean_longwave_radiation_wm2_id])
    

    def __repr__(self):
        return f"NASAClimateData(id={self.id},nasa_mean_annual_temp_c_id={self.nasa_mean_annual_temp_c_id},nasa_mean_annual_precip_mm_id={self.nasa_mean_annual_precip_mm_id},nasa_max_annual_temp_c_id={self.nasa_max_annual_temp_c_id},nasa_min_annual_temp_c_id={self.nasa_min_annual_temp_c_id},nasa_mean_wind_speed_ms_id={self.nasa_mean_wind_speed_ms_id},nasa_mean_relative_humidity_pct_id={self.nasa_mean_relative_humidity_pct_id},nasa_frost_days_per_year_id={self.nasa_frost_days_per_year_id},nasa_mean_dew_point_c_id={self.nasa_mean_dew_point_c_id},nasa_mean_vapor_pressure_kpa_id={self.nasa_mean_vapor_pressure_kpa_id},nasa_mean_surface_pressure_kpa_id={self.nasa_mean_surface_pressure_kpa_id},nasa_mean_shortwave_radiation_wm2_id={self.nasa_mean_shortwave_radiation_wm2_id},nasa_mean_longwave_radiation_wm2_id={self.nasa_mean_longwave_radiation_wm2_id},)"



    


class WorldClimData(Base):
    """
    Climate data from WorldClim service (placeholder for future implementation)
    """
    __tablename__ = 'WorldClimData'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    worldclim_bio1_id = Column(Integer(), ForeignKey('QuantityValue.id'))
    worldclim_bio1 = relationship("QuantityValue", uselist=False, foreign_keys=[worldclim_bio1_id])
    worldclim_bio12_id = Column(Integer(), ForeignKey('QuantityValue.id'))
    worldclim_bio12 = relationship("QuantityValue", uselist=False, foreign_keys=[worldclim_bio12_id])
    

    def __repr__(self):
        return f"WorldClimData(id={self.id},worldclim_bio1_id={self.worldclim_bio1_id},worldclim_bio12_id={self.worldclim_bio12_id},)"



    


class ElevationData(Base):
    """
    Elevation data from various providers
    """
    __tablename__ = 'ElevationData'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    elevation_source = Column(Text())
    elevation_m_id = Column(Integer(), ForeignKey('QuantityValue.id'))
    elevation_m = relationship("QuantityValue", uselist=False, foreign_keys=[elevation_m_id])
    

    def __repr__(self):
        return f"ElevationData(id={self.id},elevation_source={self.elevation_source},elevation_m_id={self.elevation_m_id},)"



    


class SiteMetadataCollection(Base):
    """
    A collection of site metadata records
    """
    __tablename__ = 'SiteMetadataCollection'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    
    
    # One-To-Many: OneToAnyMapping(source_class='SiteMetadataCollection', source_slot='site_metadata_entries', mapping_type=None, target_class='SiteMetadata', target_slot='SiteMetadataCollection_id', join_class=None, uses_join_table=None, multivalued=False)
    site_metadata_entries = relationship( "SiteMetadata", foreign_keys="[SiteMetadata.SiteMetadataCollection_id]")
    

    def __repr__(self):
        return f"SiteMetadataCollection(id={self.id},)"



    


class SampleBase(NamedThing):
    """
    Base class for all sample entities in the MONet system
    """
    __tablename__ = 'SampleBase'

    sample_name = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Text())
    sample_base_type = Column(Enum('sample', 'processed_sample', name='SampleBaseType'), nullable=False )
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text())
    description = Column(Text())
    

    def __repr__(self):
        return f"SampleBase(sample_name={self.sample_name},proposal_id={self.proposal_id},sampling_set={self.sampling_set},sample_base_type={self.sample_base_type},id={self.id},name={self.name},description={self.description},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SiteMetadata(NamedThing):
    """
    Site-level metadata record for a given provider (e.g., NASA POWER)
    """
    __tablename__ = 'SiteMetadata'

    cache_key = Column(Text(), nullable=False )
    latitude = Column(Float(), nullable=False )
    longitude = Column(Float(), nullable=False )
    provider = Column(Text(), nullable=False )
    enriched_at = Column(DateTime(), nullable=False )
    created_at = Column(DateTime(), nullable=False )
    updated_at = Column(DateTime())
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text())
    description = Column(Text())
    Database_id = Column(Integer(), ForeignKey('Database.id'))
    SiteMetadataCollection_id = Column(Integer(), ForeignKey('SiteMetadataCollection.id'))
    nasa_climate_data_id = Column(Integer(), ForeignKey('NASAClimateData.id'))
    nasa_climate_data = relationship("NASAClimateData", uselist=False, foreign_keys=[nasa_climate_data_id])
    

    def __repr__(self):
        return f"SiteMetadata(cache_key={self.cache_key},latitude={self.latitude},longitude={self.longitude},provider={self.provider},enriched_at={self.enriched_at},created_at={self.created_at},updated_at={self.updated_at},id={self.id},name={self.name},description={self.description},Database_id={self.Database_id},SiteMetadataCollection_id={self.SiteMetadataCollection_id},nasa_climate_data_id={self.nasa_climate_data_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Sample(SampleBase):
    """
    A physical sample collected from the environment
    """
    __tablename__ = 'Sample'

    sampling_activity_id = Column(Text(), nullable=False )
    sample_type = Column(Enum('soil', 'aerosol', name='SampleType'))
    guid_source = Column(Text())
    other_guid_source = Column(Text())
    sample_name = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Text())
    sample_base_type = Column(Enum('sample', 'processed_sample', name='SampleBaseType'), nullable=False )
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text())
    description = Column(Text())
    Database_id = Column(Integer(), ForeignKey('Database.id'))
    

    def __repr__(self):
        return f"Sample(sampling_activity_id={self.sampling_activity_id},sample_type={self.sample_type},guid_source={self.guid_source},other_guid_source={self.other_guid_source},sample_name={self.sample_name},proposal_id={self.proposal_id},sampling_set={self.sampling_set},sample_base_type={self.sample_base_type},id={self.id},name={self.name},description={self.description},Database_id={self.Database_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ProcessedSample(SampleBase):
    """
    A sample that has undergone processing or analysis
    """
    __tablename__ = 'ProcessedSample'

    processed_sample_type = Column(Enum('analyte', 'coreSection', 'replicate', name='ProcessedSampleType'), nullable=False )
    sample_name = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Text())
    sample_base_type = Column(Enum('sample', 'processed_sample', name='SampleBaseType'), nullable=False )
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text())
    description = Column(Text())
    Database_id = Column(Integer(), ForeignKey('Database.id'))
    

    def __repr__(self):
        return f"ProcessedSample(processed_sample_type={self.processed_sample_type},sample_name={self.sample_name},proposal_id={self.proposal_id},sampling_set={self.sampling_set},sample_base_type={self.sample_base_type},id={self.id},name={self.name},description={self.description},Database_id={self.Database_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SoilSample(Sample):
    """
    A soil sample with specific soil-related properties
    """
    __tablename__ = 'SoilSample'

    soil_type = Column(Enum('soil_core', 'surface_layer', name='SoilType'), nullable=False )
    sampling_activity_id = Column(Text(), nullable=False )
    sample_type = Column(Enum('soil', 'aerosol', name='SampleType'))
    guid_source = Column(Text())
    other_guid_source = Column(Text())
    sample_name = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Text())
    sample_base_type = Column(Enum('sample', 'processed_sample', name='SampleBaseType'), nullable=False )
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text())
    description = Column(Text())
    

    def __repr__(self):
        return f"SoilSample(soil_type={self.soil_type},sampling_activity_id={self.sampling_activity_id},sample_type={self.sample_type},guid_source={self.guid_source},other_guid_source={self.other_guid_source},sample_name={self.sample_name},proposal_id={self.proposal_id},sampling_set={self.sampling_set},sample_base_type={self.sample_base_type},id={self.id},name={self.name},description={self.description},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class AerosolSample(Sample):
    """
    An aerosol sample with specific aerosol-related properties
    """
    __tablename__ = 'AerosolSample'

    aerosol_type = Column(Enum('sea_salt', 'dust', 'volcanic_ash', name='AerosolType'), nullable=False )
    sampling_activity_id = Column(Text(), nullable=False )
    sample_type = Column(Enum('soil', 'aerosol', name='SampleType'))
    guid_source = Column(Text())
    other_guid_source = Column(Text())
    sample_name = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Text())
    sample_base_type = Column(Enum('sample', 'processed_sample', name='SampleBaseType'), nullable=False )
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text())
    description = Column(Text())
    

    def __repr__(self):
        return f"AerosolSample(aerosol_type={self.aerosol_type},sampling_activity_id={self.sampling_activity_id},sample_type={self.sample_type},guid_source={self.guid_source},other_guid_source={self.other_guid_source},sample_name={self.sample_name},proposal_id={self.proposal_id},sampling_set={self.sampling_set},sample_base_type={self.sample_base_type},id={self.id},name={self.name},description={self.description},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class CoreSection(ProcessedSample):
    """
    A section of a core sample (TOP, MID, BTM)
    """
    __tablename__ = 'CoreSection'

    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'), nullable=False )
    processed_sample_type = Column(Enum('analyte', 'coreSection', 'replicate', name='ProcessedSampleType'), nullable=False )
    sample_name = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Text())
    sample_base_type = Column(Enum('sample', 'processed_sample', name='SampleBaseType'), nullable=False )
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text())
    description = Column(Text())
    

    def __repr__(self):
        return f"CoreSection(core_section={self.core_section},processed_sample_type={self.processed_sample_type},sample_name={self.sample_name},proposal_id={self.proposal_id},sampling_set={self.sampling_set},sample_base_type={self.sample_base_type},id={self.id},name={self.name},description={self.description},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Replicate(ProcessedSample):
    """
    A replicate or aliquot of a sample
    """
    __tablename__ = 'Replicate'

    rep = Column(Integer(), nullable=False )
    processed_sample_type = Column(Enum('analyte', 'coreSection', 'replicate', name='ProcessedSampleType'), nullable=False )
    sample_name = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Text())
    sample_base_type = Column(Enum('sample', 'processed_sample', name='SampleBaseType'), nullable=False )
    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text())
    description = Column(Text())
    

    def __repr__(self):
        return f"Replicate(rep={self.rep},processed_sample_type={self.processed_sample_type},sample_name={self.sample_name},proposal_id={self.proposal_id},sampling_set={self.sampling_set},sample_base_type={self.sample_base_type},id={self.id},name={self.name},description={self.description},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


