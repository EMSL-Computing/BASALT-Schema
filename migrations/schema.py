
from sqlalchemy import Column, Index, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()
metadata = Base.metadata


class Study(Base):
    """
    
    """
    __tablename__ = 'study'

    id = Column(UUID(), primary_key=True, nullable=False )
    participant_name = Column(Text())
    principal_investigator = Column(Text())
    collaborating_institution = Column(Text())
    project_status = Column(Text(), nullable=False )
    project_start = Column(DateTime())
    project_end = Column(DateTime())
    proposal_title = Column(Text())
    proposal_abstract = Column(Text())
    project_id = Column(Text(), nullable=False )
    

    def __repr__(self):
        return f"study(id={self.id},participant_name={self.participant_name},principal_investigator={self.principal_investigator},collaborating_institution={self.collaborating_institution},project_status={self.project_status},project_start={self.project_start},project_end={self.project_end},proposal_title={self.proposal_title},proposal_abstract={self.proposal_abstract},project_id={self.project_id},)"



    


class QuantityValue(Base):
    """
    A quantity value with numeric value and optional unit
    """
    __tablename__ = 'quantityValue'

    id = Column(UUID(), primary_key=True, nullable=False )
    description = Column(Text())
    has_value_unit = Column(Text())
    has_unit = Column(Text())
    has_numeric_value = Column(Float())
    has_minimum_numeric_value = Column(Numeric())
    has_maximum_numeric_value = Column(Numeric())
    has_raw_value = Column(Text())
    

    def __repr__(self):
        return f"quantityValue(id={self.id},description={self.description},has_value_unit={self.has_value_unit},has_unit={self.has_unit},has_numeric_value={self.has_numeric_value},has_minimum_numeric_value={self.has_minimum_numeric_value},has_maximum_numeric_value={self.has_maximum_numeric_value},has_raw_value={self.has_raw_value},)"



    


class GeolocationValue(Base):
    """
    
    """
    __tablename__ = 'geolocationValue'

    id = Column(UUID(), primary_key=True, nullable=False )
    description = Column(Text())
    has_raw_value = Column(Text())
    latitude = Column(Numeric())
    longitude = Column(Numeric())
    type = Column(Text())
    was_generated_by = Column(Text())
    

    def __repr__(self):
        return f"geolocationValue(id={self.id},description={self.description},has_raw_value={self.has_raw_value},latitude={self.latitude},longitude={self.longitude},type={self.type},was_generated_by={self.was_generated_by},)"



    


class SamplingActivity(Base):
    """
    
    """
    __tablename__ = 'samplingActivity'

    id = Column(UUID(), primary_key=True, nullable=False )
    study_id = Column(UUID(), ForeignKey('study.id'), nullable=False )
    type = Column(Enum('soil', 'water', 'air', 'plant', 'none', name='samplingactivitytype'))
    sample_name = Column(Text())
    lims_barcode = Column(Text())
    alt_id = Column(UUID())
    elev_id = Column(UUID(), ForeignKey('quantityValue.id'))
    lat_lon_id = Column(UUID(), ForeignKey('geolocationValue.id'))
    growth_facil = Column(Enum('field', 'commercially_purchased', 'experimental_garden', 'field_incubation', 'greenhouse', 'growth_chamber', 'lab_incubation', 'open_top_chamber', 'other', name='growthfacilityenum'))
    other_growth_facil = Column(Text())
    other_storage_condt = Column(Text())
    oxygen_relationship = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'oblifate_aerobe', 'obligate_anaerobe', name='oxygenstatusenum'))
    sample_store_temp = Column(Enum('fresh4', 'freshroom', 'frozen20', 'frozen80', 'other', name='samplestoretemp'))
    samp_biotic_relationship = Column(Enum('free_living', 'parasite', 'commensal', 'symbiont', name='sampbioticenum'))
    storage_condt = Column(Enum('fresh', 'frozen', 'lyophilized', 'other', name='storagecondtenum'))
    air_temp_regm = Column(Text())
    chem_administration = Column(Text())
    collection_date = Column(DateTime())
    collection_time = Column(DateTime())
    env_broad_scale_other = Column(Text())
    env_local_scale_other = Column(Text())
    env_medium_other = Column(Text())
    experimental_factor = Column(Text())
    experimental_factor_other = Column(Text())
    extraction_method = Column(Text())
    extreme_event = Column(DateTime())
    gaseous_environment = Column(Text())
    geo_loc_name = Column(Text())
    humidity_regm = Column(Text())
    isotope_exposure = Column(Text())
    light_regm = Column(Text())
    link_addit_analys = Column(Text())
    method_development = Column(Text())
    microbial_biomass_c_meth = Column(Text())
    microbial_biomass_meth = Column(Text())
    microbial_biomass_n_meth = Column(Text())
    misc_param = Column(Text())
    neon_plot_id = Column(Text())
    non_microb_biomass_method = Column(Text())
    other_sample_store_temp = Column(Text())
    other_treatment = Column(Text())
    ph = Column(Float())
    ph_meth = Column(Text())
    salinity = Column(Float())
    salinity_method = Column(Text())
    sample_collected = Column(Text())
    sample_collection_dev = Column(Text())
    sample_collection_method = Column(Text())
    sample_end_time = Column(DateTime())
    sample_processing = Column(Text())
    sample_start_time = Column(DateTime())
    season_environment = Column(Text())
    shipped_sample_size = Column(Text())
    sieving = Column(Text())
    start_date_inc = Column(DateTime())
    tot_nitro_cont_meth = Column(Text())
    tot_org_c_meth = Column(Text())
    watering_regm = Column(Text())
    

    def __repr__(self):
        return f"samplingActivity(id={self.id},study_id={self.study_id},type={self.type},sample_name={self.sample_name},lims_barcode={self.lims_barcode},alt_id={self.alt_id},elev_id={self.elev_id},lat_lon_id={self.lat_lon_id},growth_facil={self.growth_facil},other_growth_facil={self.other_growth_facil},other_storage_condt={self.other_storage_condt},oxygen_relationship={self.oxygen_relationship},sample_store_temp={self.sample_store_temp},samp_biotic_relationship={self.samp_biotic_relationship},storage_condt={self.storage_condt},air_temp_regm={self.air_temp_regm},chem_administration={self.chem_administration},collection_date={self.collection_date},collection_time={self.collection_time},env_broad_scale_other={self.env_broad_scale_other},env_local_scale_other={self.env_local_scale_other},env_medium_other={self.env_medium_other},experimental_factor={self.experimental_factor},experimental_factor_other={self.experimental_factor_other},extraction_method={self.extraction_method},extreme_event={self.extreme_event},gaseous_environment={self.gaseous_environment},geo_loc_name={self.geo_loc_name},humidity_regm={self.humidity_regm},isotope_exposure={self.isotope_exposure},light_regm={self.light_regm},link_addit_analys={self.link_addit_analys},method_development={self.method_development},microbial_biomass_c_meth={self.microbial_biomass_c_meth},microbial_biomass_meth={self.microbial_biomass_meth},microbial_biomass_n_meth={self.microbial_biomass_n_meth},misc_param={self.misc_param},neon_plot_id={self.neon_plot_id},non_microb_biomass_method={self.non_microb_biomass_method},other_sample_store_temp={self.other_sample_store_temp},other_treatment={self.other_treatment},ph={self.ph},ph_meth={self.ph_meth},salinity={self.salinity},salinity_method={self.salinity_method},sample_collected={self.sample_collected},sample_collection_dev={self.sample_collection_dev},sample_collection_method={self.sample_collection_method},sample_end_time={self.sample_end_time},sample_processing={self.sample_processing},sample_start_time={self.sample_start_time},season_environment={self.season_environment},shipped_sample_size={self.shipped_sample_size},sieving={self.sieving},start_date_inc={self.start_date_inc},tot_nitro_cont_meth={self.tot_nitro_cont_meth},tot_org_c_meth={self.tot_org_c_meth},watering_regm={self.watering_regm},)"



    


class SampleBase(Base):
    """
    
    """
    __tablename__ = 'sampleBase'

    id = Column(UUID(), primary_key=True, nullable=False )
    sample_name = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Text())
    sample_base_type = Column(Enum('sample', 'processed_sample', name='samplebasetype'), nullable=False )
    

    def __repr__(self):
        return f"sampleBase(id={self.id},sample_name={self.sample_name},proposal_id={self.proposal_id},sampling_set={self.sampling_set},sample_base_type={self.sample_base_type},)"



    


class Sample(Base):
    """
    A physical sample collected from the environment
    """
    __tablename__ = 'sample'

    id = Column(UUID(), ForeignKey('sampleBase.id'), primary_key=True, nullable=False )
    sampling_activity_id = Column(UUID(), ForeignKey('samplingActivity.id'), nullable=False )
    type = Column(Enum('soil', 'aerosol', name='sampletype'))
    guid_source = Column(Text())
    other_guid_source = Column(Text())
    

    def __repr__(self):
        return f"sample(id={self.id},sampling_activity_id={self.sampling_activity_id},type={self.type},guid_source={self.guid_source},other_guid_source={self.other_guid_source},)"



    


class SoilSample(Base):
    """
    A soil sample with specific soil-related properties
    """
    __tablename__ = 'soil_sample'

    id = Column(UUID(), primary_key=True, nullable=False )
    soil_type = Column(Enum('soil_core', 'surface_layer', name='soiltype'), nullable=False )
    

    def __repr__(self):
        return f"soil_sample(id={self.id},soil_type={self.soil_type},)"



    


class AerosolSample(Base):
    """
    An aerosol sample with specific aerosol-related properties
    """
    __tablename__ = 'aerosol_sample'

    id = Column(UUID(), primary_key=True, nullable=False )
    aerosol_type = Column(Enum('sea_salt', 'dust', 'volcanic_ash', name='aerosoltype'), nullable=False )
    

    def __repr__(self):
        return f"aerosol_sample(id={self.id},aerosol_type={self.aerosol_type},)"



    


class ProcessedSample(Base):
    """
    A sample that has undergone processing or analysis
    """
    __tablename__ = 'processedSample'

    id = Column(UUID(), ForeignKey('sampleBase.id'), primary_key=True, nullable=False )
    processed_sample_type = Column(Enum('analyte', 'coreSection', 'replicate', name='processedsampletype'), nullable=False )
    

    def __repr__(self):
        return f"processedSample(id={self.id},processed_sample_type={self.processed_sample_type},)"



    


class CoreSection(Base):
    """
    A section of a core sample (TOP, MID, BTM)
    """
    __tablename__ = 'coreSection'

    id = Column(UUID(), ForeignKey('processedSample.id'), primary_key=True, nullable=False )
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='coresectionenum'), nullable=False )
    

    def __repr__(self):
        return f"coreSection(id={self.id},core_section={self.core_section},)"



    


class Replicate(Base):
    """
    A replicate or aliquot of a sample
    """
    __tablename__ = 'replicate'

    id = Column(UUID(), ForeignKey('processedSample.id'), primary_key=True, nullable=False )
    rep = Column(Integer(), nullable=False )
    

    def __repr__(self):
        return f"replicate(id={self.id},rep={self.rep},)"



    


