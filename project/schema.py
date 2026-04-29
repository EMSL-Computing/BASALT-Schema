
from sqlalchemy import Column, Index, Table, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()
metadata = Base.metadata


class DataProduct(Base):
    """
    Abstract base class for raw or processed data accessible in S3 storage.
Carries S3-pointer and sample-linkage slots shared across product types.
processedData and future sitePhoto extend this via is_a.
No direct database table   subclasses map to tables.
    """
    __tablename__ = 'dataProduct'

    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"dataProduct(name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    


class Replicate(Base):
    """
    A replicate or aliquot of a sample
    """
    __tablename__ = 'replicate'

    id = Column(UUID(), ForeignKey('ProcessedSample.id'), primary_key=True, nullable=False )
    rep = Column(Integer(), nullable=False )
    

    

    def __repr__(self):
        return f"replicate(id={self.id},rep={self.rep},)"



    


class AnalysisActivity(Base):
    """
    
    """
    __tablename__ = 'analysisActivity'

    sequence_order = Column(Integer())
    version = Column(Text(), nullable=False )
    id = Column(UUID(), primary_key=True, nullable=False )
    analyte_id = Column(UUID(), ForeignKey('ProcessedSample.id'))
    name = Column(Text())
    acquisition_start_time = Column(DateTime(), nullable=False )
    acquisition_end_time = Column(DateTime(), nullable=False )
    instrument_id = Column(UUID(), ForeignKey('instrument.id'))
    protocol_url = Column(Text())
    instrument_operator_id = Column(UUID(), ForeignKey('personValue.id'))
    

    

    def __repr__(self):
        return f"analysisActivity(sequence_order={self.sequence_order},version={self.version},id={self.id},analyte_id={self.analyte_id},name={self.name},acquisition_start_time={self.acquisition_start_time},acquisition_end_time={self.acquisition_end_time},instrument_id={self.instrument_id},protocol_url={self.protocol_url},instrument_operator_id={self.instrument_operator_id},)"



    


class WorkflowExecutionActivity(Base):
    """
    Abstract base for any workflow execution activity. Input data should 
be specified on workflow subclasses.
    """
    __tablename__ = 'workflowExecutionActivity'

    parent_workflow_id = Column(UUID())
    workflow_steps = Column(Text())
    version = Column(Text(), nullable=False )
    description = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    type = Column(Text(), nullable=False )
    started_at_time = Column(DateTime(), nullable=False )
    ended_at_time = Column(DateTime())
    software_url = Column(Text())
    software_version = Column(Text())
    software_poc = Column(Text())
    execution_resource = Column(Enum('RZR', 'Tahoma', 'local', 'other', name='executionresourcetype'))
    

    

    def __repr__(self):
        return f"workflowExecutionActivity(parent_workflow_id={self.parent_workflow_id},workflow_steps={self.workflow_steps},version={self.version},description={self.description},id={self.id},type={self.type},started_at_time={self.started_at_time},ended_at_time={self.ended_at_time},software_url={self.software_url},software_version={self.software_version},software_poc={self.software_poc},execution_resource={self.execution_resource},)"



    


class AlternativeIdentifier(Base):
    """
    
    """
    __tablename__ = 'alternativeIdentifier'

    id = Column(UUID(), primary_key=True, nullable=False )
    alternate_id = Column(Text(), nullable=False )
    alternate_identifier_type = Column(Enum('instrument_alt_id', name='alternateidentifiertype'), nullable=False )
    

    

    def __repr__(self):
        return f"alternativeIdentifier(id={self.id},alternate_id={self.alternate_id},alternate_identifier_type={self.alternate_identifier_type},)"



    


class Ecoregion(Base):
    """
    
    """
    __tablename__ = 'ecoregion'

    domain_id = Column(Integer(), primary_key=True, nullable=False )
    domain_name = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"ecoregion(domain_id={self.domain_id},domain_name={self.domain_name},)"



    


class FunctionalAnnotationIdentifier(Base):
    """
    
    """
    __tablename__ = 'functionalAnnotationIdentifier'

    id = Column(UUID(), primary_key=True, nullable=False )
    functional_identifier = Column(Text(), nullable=False )
    database = Column(Enum('PFAM', 'COG', 'KEGG', name='annotationdatabasetype'), nullable=False )
    

    

    def __repr__(self):
        return f"functionalAnnotationIdentifier(id={self.id},functional_identifier={self.functional_identifier},database={self.database},)"



    


class Instrument(Base):
    """
    
    """
    __tablename__ = 'instrument'

    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    alternative_names = Column(Text())
    vendor = Column(Enum('waters', 'agilent', 'bruker', 'thermo_fisher', 'perkin_elmer', 'scientific_industries', 'illumina', 'nikon', 'fia_lab', 'shimadzu', 'regen_ag_lab', 'kuo', 'rigaku', 'panalytical', name='vendorenum'))
    model = Column(Enum('exploris_240', 'exploris_480', 'ltq_orbitrap_velos', 'orbitrap_fusion_lumos', 'orbitrap_eclipse_tribid', 'orbitrap_q_exactive', 'solarix_7T', 'solarix_12T', 'solarix_15T', 'agilent_8890A', 'agilent_7980A', 'vortex_genie_2', 'novaseq', 'scimax', 'ed_400_with_rs_422', 'mettler_toledo_30029066', 'mettler_toledo_30266628', 'ums_hyprop2_020210', 'fialyzer_1000', 'fialyzer_1001', 'fialyzer_1002', 'orbitrap_q_exactive_plus', 'toc_5000A', 'toc_lcsh', 'sr_1', 'xth320', name='modelenum'))
    instrument_parameters = Column(Text())
    

    

    def __repr__(self):
        return f"instrument(id={self.id},name={self.name},alternative_names={self.alternative_names},vendor={self.vendor},model={self.model},instrument_parameters={self.instrument_parameters},)"



    


class OntologyClass(Base):
    """
    
    """
    __tablename__ = 'ontologyClass'

    id = Column(UUID(), primary_key=True, nullable=False )
    description = Column(Text())
    alternative_identifiers = Column(Text())
    name = Column(Text())
    

    

    def __repr__(self):
        return f"ontologyClass(id={self.id},description={self.description},alternative_identifiers={self.alternative_identifiers},name={self.name},)"



    


class ContainerType(Base):
    """
    
    """
    __tablename__ = 'containerType'

    id = Column(UUID(), primary_key=True, nullable=False )
    description = Column(Text())
    was_generated_by = Column(Text())
    container_type = Column(Enum('screw_top_conical', name='containertypeenum'))
    container_size_id = Column(UUID(), ForeignKey('quantityValue.id'))
    

    

    def __repr__(self):
        return f"containerType(id={self.id},description={self.description},was_generated_by={self.was_generated_by},container_type={self.container_type},container_size_id={self.container_size_id},)"



    


class Custodian(Base):
    """
    
    """
    __tablename__ = 'custodian'

    id = Column(UUID(), primary_key=True, nullable=False )
    person_id = Column(UUID(), ForeignKey('personValue.id'))
    

    

    def __repr__(self):
        return f"custodian(id={self.id},person_id={self.person_id},)"



    


class Instrument_alt_id(Base):
    """
    
    """
    __tablename__ = 'instrument_alt_id'

    id = Column(UUID(), primary_key=True, nullable=False )
    alt_id = Column(UUID(), ForeignKey('alternativeIdentifier.id'))
    instrument_alt_id_provider = Column(Enum('nexus', 'dms', name='instrumentaltidprovider'))
    instrument_id = Column(UUID(), ForeignKey('instrument.id'), nullable=False )
    

    

    def __repr__(self):
        return f"instrument_alt_id(id={self.id},alt_id={self.alt_id},instrument_alt_id_provider={self.instrument_alt_id_provider},instrument_id={self.instrument_id},)"



    


class LabDevice(Base):
    """
    
    """
    __tablename__ = 'labDevice'

    id = Column(UUID(), primary_key=True, nullable=False )
    description = Column(Text())
    device_type = Column(Enum('orbital_shaker', 'thermomixer', name='devicetypeenum'))
    activity_time_id = Column(UUID(), ForeignKey('quantityValue.id'))
    activity_speed_id = Column(UUID(), ForeignKey('quantityValue.id'))
    

    

    def __repr__(self):
        return f"labDevice(id={self.id},description={self.description},device_type={self.device_type},activity_time_id={self.activity_time_id},activity_speed_id={self.activity_speed_id},)"



    


class SampleProcessing(Base):
    """
    
    """
    __tablename__ = 'sampleProcessing'

    id = Column(UUID(), primary_key=True, nullable=False )
    analysis_type = Column(Enum('analysis_activity', 'lcms_metabolomics_method', 'fticr_acquisition_method', 'gravimetric_water_content_method', 'ph_method', 'hydraulic_properties_method', 'microbial_biomass_method', 'xray_computed_tomography_method', 'REGEN', 'KUO', 'respiration_method', 'texture_method', 'enzyme_activity_method', 'elemental_analysis_method', 'toc_tn_method', 'bulk_density_method', 'metagenomics_method', 'xrf_analysis', 'xrd_analysis', name='routemethod'))
    method_name = Column(Enum('MAOM', 'WOEM', name='methodname'))
    processing_steps = Column(Text(), nullable=False )
    url = Column(Text())
    version = Column(Text())
    

    

    def __repr__(self):
        return f"sampleProcessing(id={self.id},analysis_type={self.analysis_type},method_name={self.method_name},processing_steps={self.processing_steps},url={self.url},version={self.version},)"



    


class ProcessingSampleLink(Base):
    """
    
    """
    __tablename__ = 'processingSampleLink'

    id = Column(UUID(), primary_key=True, nullable=False )
    sample_base_id = Column(UUID(), ForeignKey('Sample.id'), nullable=False )
    processing_id = Column(UUID(), ForeignKey('sampleProcessing.id'), nullable=False )
    step_number = Column(Integer(), nullable=False )
    role = Column(Enum('input_sample', 'output_sample', name='samplerole'), nullable=False )
    version = Column(Text())
    

    
    # Unique constraints
    __table_args__ = (
        UniqueConstraint('sample_base_id', 'processing_id', 'step_number', 'role'),
    )
    

    def __repr__(self):
        return f"processingSampleLink(id={self.id},sample_base_id={self.sample_base_id},processing_id={self.processing_id},step_number={self.step_number},role={self.role},version={self.version},)"



    


class InstrumentCustodian(Base):
    """
    
    """
    __tablename__ = 'instrumentCustodian'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    instrument_id = Column(UUID(), ForeignKey('instrument.id'), nullable=False )
    custodian_id = Column(UUID(), ForeignKey('custodian.id'), nullable=False )
    

    

    def __repr__(self):
        return f"instrumentCustodian(id={self.id},instrument_id={self.instrument_id},custodian_id={self.custodian_id},)"



    


class WorkflowExecutionFunctionalAnnotation(Base):
    """
    
    """
    __tablename__ = 'workflowExecutionFunctionalAnnotation'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    workflow_id = Column(UUID(), ForeignKey('workflowExecutionActivity.id'), nullable=False )
    functional_annotation_id = Column(UUID(), ForeignKey('functionalAnnotationIdentifier.id'), nullable=False )
    count = Column(Numeric())
    

    

    def __repr__(self):
        return f"workflowExecutionFunctionalAnnotation(id={self.id},workflow_id={self.workflow_id},functional_annotation_id={self.functional_annotation_id},count={self.count},)"



    


class TimestampValue(Base):
    """
    
    """
    __tablename__ = 'timestampValue'

    id = Column(UUID(), primary_key=True, nullable=False )
    description = Column(Text())
    has_raw_value = Column(Text())
    type = Column(Text())
    was_generated_by = Column(Text())
    

    

    def __repr__(self):
        return f"timestampValue(id={self.id},description={self.description},has_raw_value={self.has_raw_value},type={self.type},was_generated_by={self.was_generated_by},)"



    


class TextValue(Base):
    """
    
    """
    __tablename__ = 'textValue'

    id = Column(UUID(), primary_key=True, nullable=False )
    description = Column(Text())
    language = Column(Text())
    has_raw_value = Column(Text())
    type = Column(Text())
    was_generated_by = Column(Text())
    

    

    def __repr__(self):
        return f"textValue(id={self.id},description={self.description},language={self.language},has_raw_value={self.has_raw_value},type={self.type},was_generated_by={self.was_generated_by},)"



    


class SoftwareControlledTermValue(Base):
    """
    
    """
    __tablename__ = 'softwareControlledTermValue'

    id = Column(UUID(), primary_key=True, nullable=False )
    description = Column(Text())
    name = Column(Text())
    version = Column(Text())
    has_raw_value = Column(Text())
    was_generated_by = Column(Text())
    type = Column(Text())
    

    

    def __repr__(self):
        return f"softwareControlledTermValue(id={self.id},description={self.description},name={self.name},version={self.version},has_raw_value={self.has_raw_value},was_generated_by={self.was_generated_by},type={self.type},)"



    


class ControlledTermValue(Base):
    """
    
    """
    __tablename__ = 'controlledTermValue'

    id = Column(UUID(), primary_key=True, nullable=False )
    description = Column(Text())
    has_raw_value = Column(Text())
    was_generated_by = Column(Text())
    type = Column(Text())
    

    

    def __repr__(self):
        return f"controlledTermValue(id={self.id},description={self.description},has_raw_value={self.has_raw_value},was_generated_by={self.was_generated_by},type={self.type},)"



    


class PersonValue(Base):
    """
    
    """
    __tablename__ = 'personValue'

    email = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    first_name = Column(Text(), nullable=False )
    last_name = Column(Text(), nullable=False )
    middle_initial = Column(Text())
    orcid = Column(Text())
    profile_image_url = Column(Text())
    websites = Column(Text())
    

    
    # Unique constraints
    __table_args__ = (
        UniqueConstraint('email'),
    )
    

    def __repr__(self):
        return f"personValue(email={self.email},id={self.id},first_name={self.first_name},last_name={self.last_name},middle_initial={self.middle_initial},orcid={self.orcid},profile_image_url={self.profile_image_url},websites={self.websites},)"



    


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



    


class ConditioningValue(Base):
    """
    
    """
    __tablename__ = 'conditioningValue'

    id = Column(UUID(), primary_key=True, nullable=False )
    source_material = Column(Text())
    type = Column(Text())
    instrument = Column(Text())
    gas = Column(Text())
    pressure = Column(Text())
    has_raw_value = Column(Text())
    

    

    def __repr__(self):
        return f"conditioningValue(id={self.id},source_material={self.source_material},type={self.type},instrument={self.instrument},gas={self.gas},pressure={self.pressure},has_raw_value={self.has_raw_value},)"



    


class LatLongValue(Base):
    """
    
    """
    __tablename__ = 'latLongValue'

    id = Column(UUID(), primary_key=True, nullable=False )
    description = Column(Text())
    has_raw_value = Column(Text())
    latitude = Column(Float(), nullable=False )
    longitude = Column(Float(), nullable=False )
    

    

    def __repr__(self):
        return f"latLongValue(id={self.id},description={self.description},has_raw_value={self.has_raw_value},latitude={self.latitude},longitude={self.longitude},)"



    


class SiteMetadata(Base):
    """
    Site-level metadata for specific locations from which a set of samples are collected.
    """
    __tablename__ = 'SiteMetadata'

    name = Column(Text(), nullable=False )
    description = Column(Text())
    type = Column(Text())
    latitude = Column(Float())
    longitude = Column(Float())
    id = Column(UUID(), primary_key=True, nullable=False )
    cur_land_use = Column(Enum('badlands', 'cities', 'conifers', 'crop_trees', 'farmstead', 'gravel', 'hardwoods', 'hayland', 'horticultural_plants', 'industrial_areas', 'intermixed', 'marshlands', 'meadows', 'mines_quarries', 'mudflats', 'oil_waste', 'pastureland', 'permanent_snow_or_ice', 'rainforest', 'rangeland', 'roads_railroads', 'rock', 'row_crops', 'saline_seeps', 'salt_flats', 'sand', 'shrub_crops', 'shrub_land', 'small_grains', 'successional_shrub_land', 'swamp', 'tropical', 'tundra', 'vegetable_crops', 'vine_crops', name='LandUseEnum'))
    drainage_class = Column(Enum('excessively_drained', 'moderately_well', 'poorly', 'somewhat_poorly', 'very_poorly', 'well', name='DrainageClassEnum'))
    fao_class = Column(Enum('Acrisols', 'Alisols', 'Andosols', 'Anthrosols', 'Arenosols', 'Calcisols', 'Cambisols', 'Chernozems', 'Cryosols', 'Durisols', 'Ferrasols', 'Fluvisols', 'Gleysols', 'Gypsisols', 'Histosols', 'Kastanozems', 'Leptosols', 'Lixisols', 'Luvisols', 'Nitosols', 'Phaeozems', 'Planosols', 'Plinthosols', 'Podzols', 'Solonchaks', 'Solonetz', 'Stagnosols', 'Technosols', 'Umbrisols', 'Vertisols', name='FAOClassEnum'))
    neon_domain = Column(Enum('northeast', 'mid_atlantic', 'southeast', 'atlantic_neotropical', 'great_lakes', 'prairie_peninsula', 'appalachians_and_cumberland_plateau', 'ozarks_complex', 'northern_plains', 'central_plains', 'southern_plains', 'desert_southwest', 'northern_rockies', 'southern_rockies_and_colorado_plateau', 'great_basin', 'sierra_nevada', 'pacific_northwest', 'pacific_southwest', 'tundra', 'taiga', 'pacific_tropical', name='NEONDomainEnum'))
    from_sampling_activity = Column(UUID(), ForeignKey('SamplingActivity.id'))
    

    

    def __repr__(self):
        return f"SiteMetadata(name={self.name},description={self.description},type={self.type},latitude={self.latitude},longitude={self.longitude},id={self.id},cur_land_use={self.cur_land_use},drainage_class={self.drainage_class},fao_class={self.fao_class},neon_domain={self.neon_domain},from_sampling_activity={self.from_sampling_activity},)"



    


class Sample(Base):
    """
    A physical sample collected from an environment. The environment can be ecological, laboratory, or any other context where samples are collected. This class serves as an abstract class to relate subclasses of samples.
    """
    __tablename__ = 'Sample'

    name = Column(Text(), nullable=False )
    description = Column(Text())
    type = Column(Text())
    ['study'_'study_id'_'project_id'_'proposal'_'proposal_id'] = Column(Integer())
    emsl_activity = Column(Text())
    storage_condition = Column(Enum('fresh', 'frozen', 'lyophilized', 'other', name='StorageConditionEnum'))
    oxygen_relationship = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'oblifate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    biotic_relationship = Column(Enum('free_living', 'parasite', 'commensal', 'symbiont', name='BioticRelationshipEnum'))
    air_temp_regm = Column(Text())
    chem_administration = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    proposal_id = Column(Integer())
    other_storage_condt = Column(Text())
    

    

    def __repr__(self):
        return f"Sample(name={self.name},description={self.description},type={self.type},['study'_'study_id'_'project_id'_'proposal'_'proposal_id']={self.['study'_'study_id'_'project_id'_'proposal'_'proposal_id']},emsl_activity={self.emsl_activity},storage_condition={self.storage_condition},oxygen_relationship={self.oxygen_relationship},biotic_relationship={self.biotic_relationship},air_temp_regm={self.air_temp_regm},chem_administration={self.chem_administration},id={self.id},proposal_id={self.proposal_id},other_storage_condt={self.other_storage_condt},)"



    


class SamplingActivity(Base):
    """
    An activity that involves the collection of a sample. This class serves as an abstract class to relate subclasses of sampling activities. Note that the sampling activity is related to the sample via the has_output relationship on the activity, not via a direct relationship on the sample.
    """
    __tablename__ = 'SamplingActivity'

    name = Column(Text(), nullable=False )
    description = Column(Text())
    type = Column(Text())
    ['study'_'study_id'_'project_id'_'proposal'_'proposal_id'] = Column(Integer())
    emsl_activity = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    sample_name = Column(Text(), nullable=False )
    lims_barcode = Column(Text())
    growth_facil = Column(Enum('field', 'commercially_purchased', 'experimental_garden', 'field_incubation', 'greenhouse', 'growth_chamber', 'lab_incubation', 'open_top_chamber', 'other', name='growthfacilityenum'))
    other_growth_facil = Column(Text())
    sample_store_temp = Column(Enum('fresh4', 'freshroom', 'frozen20', 'frozen80', 'other', name='samplestoretemp'))
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
    
    
    # ManyToMany
    has_output = relationship( "Sample", secondary="SamplingActivity_has_output")
    

    

    def __repr__(self):
        return f"SamplingActivity(name={self.name},description={self.description},type={self.type},['study'_'study_id'_'project_id'_'proposal'_'proposal_id']={self.['study'_'study_id'_'project_id'_'proposal'_'proposal_id']},emsl_activity={self.emsl_activity},id={self.id},sample_name={self.sample_name},lims_barcode={self.lims_barcode},growth_facil={self.growth_facil},other_growth_facil={self.other_growth_facil},sample_store_temp={self.sample_store_temp},collection_date={self.collection_date},collection_time={self.collection_time},env_broad_scale_other={self.env_broad_scale_other},env_local_scale_other={self.env_local_scale_other},env_medium_other={self.env_medium_other},experimental_factor={self.experimental_factor},experimental_factor_other={self.experimental_factor_other},extraction_method={self.extraction_method},extreme_event={self.extreme_event},gaseous_environment={self.gaseous_environment},geo_loc_name={self.geo_loc_name},humidity_regm={self.humidity_regm},isotope_exposure={self.isotope_exposure},light_regm={self.light_regm},link_addit_analys={self.link_addit_analys},method_development={self.method_development},misc_param={self.misc_param},neon_plot_id={self.neon_plot_id},non_microb_biomass_method={self.non_microb_biomass_method},other_sample_store_temp={self.other_sample_store_temp},other_treatment={self.other_treatment},ph={self.ph},ph_meth={self.ph_meth},salinity={self.salinity},salinity_method={self.salinity_method},sample_collected={self.sample_collected},sample_collection_dev={self.sample_collection_dev},sample_collection_method={self.sample_collection_method},sample_end_time={self.sample_end_time},sample_processing={self.sample_processing},sample_start_time={self.sample_start_time},season_environment={self.season_environment},shipped_sample_size={self.shipped_sample_size},sieving={self.sieving},start_date_inc={self.start_date_inc},tot_nitro_cont_meth={self.tot_nitro_cont_meth},tot_org_c_meth={self.tot_org_c_meth},watering_regm={self.watering_regm},)"



    


class Method(Base):
    """
    
    """
    __tablename__ = 'Method'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    analytic = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"Method(id={self.id},analytic={self.analytic},)"



    


class MAOMProduct(Base):
    """
    
    """
    __tablename__ = 'MAOMProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    rep = Column(Numeric())
    id = Column(UUID(), ForeignKey('processedData.id'), primary_key=True, nullable=False )
    total_organic_carbon_id = Column(UUID(), ForeignKey('quantityValue.id'))
    total_organic_carbon_avg = Column(Float())
    total_nitrogen_id = Column(UUID(), ForeignKey('quantityValue.id'))
    total_nitrogen_avg = Column(Float())
    flag_toc = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_tn = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_toc_avg = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_tn_avg = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    

    

    def __repr__(self):
        return f"MAOMProduct(measure_type={self.measure_type},rep={self.rep},id={self.id},total_organic_carbon_id={self.total_organic_carbon_id},total_organic_carbon_avg={self.total_organic_carbon_avg},total_nitrogen_id={self.total_nitrogen_id},total_nitrogen_avg={self.total_nitrogen_avg},flag_toc={self.flag_toc},flag_tn={self.flag_tn},flag_toc_avg={self.flag_toc_avg},flag_tn_avg={self.flag_tn_avg},)"



    


class WEOMProduct(Base):
    """
    
    """
    __tablename__ = 'WEOMProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    rep = Column(Numeric())
    id = Column(UUID(), ForeignKey('processedData.id'), primary_key=True, nullable=False )
    total_organic_carbon_id = Column(UUID(), ForeignKey('quantityValue.id'))
    total_organic_carbon_avg = Column(Float())
    total_nitrogen_id = Column(UUID(), ForeignKey('quantityValue.id'))
    total_nitrogen_avg = Column(Float())
    flag_toc = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_tn = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_toc_avg = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_tn_avg = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    

    

    def __repr__(self):
        return f"WEOMProduct(measure_type={self.measure_type},rep={self.rep},id={self.id},total_organic_carbon_id={self.total_organic_carbon_id},total_organic_carbon_avg={self.total_organic_carbon_avg},total_nitrogen_id={self.total_nitrogen_id},total_nitrogen_avg={self.total_nitrogen_avg},flag_toc={self.flag_toc},flag_tn={self.flag_tn},flag_toc_avg={self.flag_toc_avg},flag_tn_avg={self.flag_tn_avg},)"



    


class Changelog(Base):
    """
    
    """
    __tablename__ = 'changelog'

    version = Column(Text(), primary_key=True, nullable=False )
    changelog = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"changelog(version={self.version},changelog={self.changelog},)"



    


class Study(Base):
    """
    
    """
    __tablename__ = 'study'

    id = Column(UUID(), primary_key=True, nullable=False )
    participant_name = Column(Text(), nullable=False )
    principal_investigator = Column(Text())
    collaborating_institution = Column(Text())
    project_status = Column(Enum('STARTED', 'COMPLETED', 'CLOSED', 'EXTENDED', 'ACCEPTED', 'WITHDRAWN', name='projectstatus'))
    project_start = Column(DateTime())
    project_end = Column(DateTime())
    proposal_title = Column(Text())
    proposal_abstract = Column(Text())
    project_id = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"study(id={self.id},participant_name={self.participant_name},principal_investigator={self.principal_investigator},collaborating_institution={self.collaborating_institution},project_status={self.project_status},project_start={self.project_start},project_end={self.project_end},proposal_title={self.proposal_title},proposal_abstract={self.proposal_abstract},project_id={self.project_id},)"



    


class ZipDownload(Base):
    """
    
    """
    __tablename__ = 'zipDownload'

    id = Column(UUID(), primary_key=True, nullable=False )
    time = Column(DateTime(), nullable=False )
    user = Column(Text(), nullable=False )
    files = Column(Integer(), nullable=False )
    packages = Column(Text())
    

    

    def __repr__(self):
        return f"zipDownload(id={self.id},time={self.time},user={self.user},files={self.files},packages={self.packages},)"



    


class HasIncubationConditions(Base):
    """
    Mixin for activities/setups that involve controlled incubation.
Used by CultureGrowth activities AND PlateSetupActivity, which share
temperature and agitation parameters but live in different branches
of the sampleProcessing is_a tree.
    """
    __tablename__ = 'HasIncubationConditions'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    temperature_celsius = Column(Float())
    agitation_speed_rpm = Column(Integer())
    oxygen_status = Column(Text())
    

    

    def __repr__(self):
        return f"HasIncubationConditions(id={self.id},temperature_celsius={self.temperature_celsius},agitation_speed_rpm={self.agitation_speed_rpm},oxygen_status={self.oxygen_status},)"



    


class PurchasedMaterial(Base):
    """
    [NEW ABSTRACT CLASS] Lightweight base for non-sample physical lab materials
that are not instruments.  Currently Strain is the only concrete subtype.
Activities reference Strain via the strain_ref FK slot.
    """
    __tablename__ = 'purchasedMaterial'

    entity_type = Column(Text(), nullable=False )
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    

    

    def __repr__(self):
        return f"purchasedMaterial(entity_type={self.entity_type},id={self.id},name={self.name},description={self.description},)"



    


class LabProcessingActivity(Base):
    """
    [NEW ABSTRACT CLASS] Higher-level abstract base for any activity that
transforms or creates physical lab materials.

sampleProcessing inherits from this via is_a.  This class provides the
common identity layer, allowing future extensions (e.g. non-sample
consuming activities) without forcing them into the sampleProcessing branch.

NOTE: In the live schema, sampleProcessing should gain
  is_a: labProcessingActivity
and its existing id attribute can be retained or removed (inherited).
    """
    __tablename__ = 'labProcessingActivity'

    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text())
    description = Column(Text())
    

    

    def __repr__(self):
        return f"labProcessingActivity(id={self.id},name={self.name},description={self.description},)"



    


class PlateProduct(Base):
    """
    Abstract base for plate measurement data products.
Common summary slots shared across AMP2 and Ecoplate products.

v1 origin: plate-general.yaml PlateProduct
v2 change: follows existing satellite-table pattern (id: range: processedData)
           instead of v1's is_a: dataProduct.
    """
    __tablename__ = 'PlateProduct'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    wavelength_nm = Column(Integer(), nullable=False )
    timepoint_label = Column(Text(), nullable=False )
    plate_average = Column(Float())
    blank_mean = Column(Float())
    cv_percent = Column(Float())
    
    
    # One-To-Many: OneToAnyMapping(source_class='PlateProduct', source_slot='well_readings', mapping_type=None, target_class='WellReading', target_slot='PlateProduct_id', join_class=None, uses_join_table=None, multivalued=False)
    well_readings = relationship( "WellReading", foreign_keys="[WellReading.PlateProduct_id]")
    

    

    def __repr__(self):
        return f"PlateProduct(id={self.id},wavelength_nm={self.wavelength_nm},timepoint_label={self.timepoint_label},plate_average={self.plate_average},blank_mean={self.blank_mean},cv_percent={self.cv_percent},)"



    


class WellMetadata(Base):
    """
    Base structure for per-well metadata in plate setup.
NOT a database table embedded as JSONB in PlateSetupActivity.
Subclasses add type-specific fields.
    """
    __tablename__ = 'WellMetadata'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    position = Column(Text(), nullable=False )
    well_type = Column(Text())
    replicate_group = Column(Text())
    PlateSetupActivity_id = Column(UUID(), ForeignKey('PlateSetupActivity.id'))
    AMP2PlateSetupActivity_id = Column(UUID(), ForeignKey('AMP2PlateSetupActivity.id'))
    EcoplatePlateSetupActivity_id = Column(UUID(), ForeignKey('EcoplatePlateSetupActivity.id'))
    

    

    def __repr__(self):
        return f"WellMetadata(id={self.id},position={self.position},well_type={self.well_type},replicate_group={self.replicate_group},PlateSetupActivity_id={self.PlateSetupActivity_id},AMP2PlateSetupActivity_id={self.AMP2PlateSetupActivity_id},EcoplatePlateSetupActivity_id={self.EcoplatePlateSetupActivity_id},)"



    


class WellReading(Base):
    """
    Per-well measurement data.
NOT a database table   embedded as JSONB in PlateProduct records.
Lightweight summary for queries; raw data in MinIO.

v1 origin: plate-general.yaml WellReading
    """
    __tablename__ = 'WellReading'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    position = Column(Text(), nullable=False )
    value = Column(Float(), nullable=False )
    flag = Column(Text())
    PlateProduct_id = Column(Integer(), ForeignKey('PlateProduct.id'))
    AMP2ODProduct_id = Column(Integer(), ForeignKey('AMP2ODProduct.id'))
    EcoplateAbsorbanceProduct_id = Column(Integer(), ForeignKey('EcoplateAbsorbanceProduct.id'))
    

    

    def __repr__(self):
        return f"WellReading(id={self.id},position={self.position},value={self.value},flag={self.flag},PlateProduct_id={self.PlateProduct_id},AMP2ODProduct_id={self.AMP2ODProduct_id},EcoplateAbsorbanceProduct_id={self.EcoplateAbsorbanceProduct_id},)"



    


class Configuration(Base):
    """
    Record of configuration and/or settings for an activity.
    """
    __tablename__ = 'Configuration'

    uid = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    id = Column(UUID(), nullable=False )
    

    

    def __repr__(self):
        return f"Configuration(uid={self.uid},name={self.name},description={self.description},id={self.id},)"



    


class MassSpectrometryStandardRun(Base):
    """
    
    """
    __tablename__ = 'MassSpectrometryStandardRun'

    name = Column(Text(), nullable=False )
    description = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    internal_calibration = Column(Boolean())
    calibration_target = Column(Enum('mass_charge_ratio', 'retention_time', 'retention_index', name='calibrationtargetenum'))
    calibration_standard = Column(UUID(), ForeignKey('purchasedMaterial.id'))
    calibration_data = Column(UUID(), ForeignKey('MassSpectrometryInstrumentData.id'))
    

    

    def __repr__(self):
        return f"MassSpectrometryStandardRun(name={self.name},description={self.description},id={self.id},internal_calibration={self.internal_calibration},calibration_target={self.calibration_target},calibration_standard={self.calibration_standard},calibration_data={self.calibration_data},)"



    


class SamplingActivity_has_output(Base):
    """
    
    """
    __tablename__ = 'SamplingActivity_has_output'

    SamplingActivity_id = Column(UUID(), ForeignKey('SamplingActivity.id'), primary_key=True)
    has_output_id = Column(UUID(), ForeignKey('Sample.id'), primary_key=True)
    

    

    def __repr__(self):
        return f"SamplingActivity_has_output(SamplingActivity_id={self.SamplingActivity_id},has_output_id={self.has_output_id},)"



    


class SoilSamplingActivity_has_output(Base):
    """
    
    """
    __tablename__ = 'SoilSamplingActivity_has_output'

    SoilSamplingActivity_id = Column(UUID(), ForeignKey('SoilSamplingActivity.id'), primary_key=True)
    has_output_id = Column(UUID(), ForeignKey('SoilSample.id'), primary_key=True)
    

    

    def __repr__(self):
        return f"SoilSamplingActivity_has_output(SoilSamplingActivity_id={self.SoilSamplingActivity_id},has_output_id={self.has_output_id},)"



    


class MediaPreparation_exposure_sensitivity(Base):
    """
    
    """
    __tablename__ = 'MediaPreparation_exposure_sensitivity'

    MediaPreparation_id = Column(UUID(), ForeignKey('MediaPreparation.id'), primary_key=True)
    exposure_sensitivity = Column(Text(), primary_key=True)
    

    

    def __repr__(self):
        return f"MediaPreparation_exposure_sensitivity(MediaPreparation_id={self.MediaPreparation_id},exposure_sensitivity={self.exposure_sensitivity},)"



    


class MediaPreparation_media_additions(Base):
    """
    
    """
    __tablename__ = 'MediaPreparation_media_additions'

    MediaPreparation_id = Column(UUID(), ForeignKey('MediaPreparation.id'), primary_key=True)
    media_additions = Column(Text(), primary_key=True)
    

    

    def __repr__(self):
        return f"MediaPreparation_media_additions(MediaPreparation_id={self.MediaPreparation_id},media_additions={self.media_additions},)"



    


class AMP2WellMetadata_treatments(Base):
    """
    
    """
    __tablename__ = 'AMP2WellMetadata_treatments'

    AMP2WellMetadata_id = Column(Integer(), ForeignKey('AMP2WellMetadata.id'), primary_key=True)
    treatments = Column(Text(), primary_key=True)
    

    

    def __repr__(self):
        return f"AMP2WellMetadata_treatments(AMP2WellMetadata_id={self.AMP2WellMetadata_id},treatments={self.treatments},)"



    


class ProcessedData(DataProduct):
    """
    A data product generated by a workflow execution.
    """
    __tablename__ = 'processedData'

    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"processedData(summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},sample_id={self.sample_id},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class InstrumentData(DataProduct):
    """
    
    """
    __tablename__ = 'instrumentData'

    file_curie = Column(Text())
    alternative_identifiers = Column(Text())
    compression_type = Column(Text())
    type = Column(Text())
    file_type = Column(Enum('FT_ICR_MS_Analysis_Results', 'GC_MS_Metabolomics_Results', 'Metaproteomics_Workflow_Statistics', 'Protein_Report', 'Peptide_Report', 'Unfiltered_Metaproteomics_Results', 'Read_Count_and_RPKM', 'QC_non_rRNA_R2', 'QC_non_rRNA_R1', 'Metagenome_Bins', 'CheckM_Statistics', 'GOTTCHA2_Krona_Plot', 'Kraken2_Krona_Plot', 'Centrifuge_Krona_Plot', 'Kraken2_Classification_Report', 'Kraken2_Taxonomic_Classification', 'Centrifuge_Classification_Report', 'Centrifuge_Taxonomic_Classification', 'Structural_Annotation_GFF', 'Functional_Annotation_GFF', 'Annotation_Amino_Acid_FASTA', 'Annotation_Enzyme_Commission', 'Annotation_KEGG_Orthology', 'Assembly_Coverage_BAM', 'Assembly_AGP', 'Assembly_Scaffolds', 'Assembly_Contigs', 'Assembly_Coverage_Stats', 'Filtered_Sequencing_Reads', 'QC_Statistics', 'TIGRFam_Annotation_GFF', 'Clusters_of_Orthologous_Groups_COG_Annotation_GFF', 'CATH_FunFams_Functional_Families_Annotation_GFF', 'SUPERFam_Annotation_GFF', 'SMART_Annotation_GFF', 'Pfam_Annotation_GFF', 'Direct_Infusion_FT_ICR_MS_Raw_Data', name='filetype'))
    version = Column(Text())
    name = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"instrumentData(file_curie={self.file_curie},alternative_identifiers={self.alternative_identifiers},compression_type={self.compression_type},type={self.type},file_type={self.file_type},version={self.version},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SitePhoto(DataProduct):
    """
    
    """
    __tablename__ = 'sitePhoto'

    site_photo_type = Column(Enum('landscape', 'measure', name='sitephototype'))
    photo_taken_during = Column(UUID(), ForeignKey('SamplingActivity.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"sitePhoto(site_photo_type={self.site_photo_type},photo_taken_during={self.photo_taken_during},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SoilSample(Sample):
    """
    A soil sample with specific soil-related properties.
    """
    __tablename__ = 'SoilSample'

    soil_type = Column(Enum('soil_core', 'surface_layer', name='SoilTypeEnum'))
    soil_horizon = Column(Enum('A horizon', 'B horizon', 'C horizon', 'E horizon', 'O horizon', 'Permafrost', 'R layer', 'M horizon', name='SoilHorizonEnum'))
    id = Column(UUID(), ForeignKey('Sample.id'), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    type = Column(Text())
    ['study'_'study_id'_'project_id'_'proposal'_'proposal_id'] = Column(Integer())
    emsl_activity = Column(Text())
    storage_condition = Column(Enum('fresh', 'frozen', 'lyophilized', 'other', name='StorageConditionEnum'))
    oxygen_relationship = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'oblifate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    biotic_relationship = Column(Enum('free_living', 'parasite', 'commensal', 'symbiont', name='BioticRelationshipEnum'))
    air_temp_regm = Column(Text())
    chem_administration = Column(Text())
    proposal_id = Column(Integer())
    other_storage_condt = Column(Text())
    

    

    def __repr__(self):
        return f"SoilSample(soil_type={self.soil_type},soil_horizon={self.soil_horizon},id={self.id},name={self.name},description={self.description},type={self.type},['study'_'study_id'_'project_id'_'proposal'_'proposal_id']={self.['study'_'study_id'_'project_id'_'proposal'_'proposal_id']},emsl_activity={self.emsl_activity},storage_condition={self.storage_condition},oxygen_relationship={self.oxygen_relationship},biotic_relationship={self.biotic_relationship},air_temp_regm={self.air_temp_regm},chem_administration={self.chem_administration},proposal_id={self.proposal_id},other_storage_condt={self.other_storage_condt},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class AerosolSample(Sample):
    """
    An aerosol sample with specific aerosol-related properties
    """
    __tablename__ = 'AerosolSample'

    aerosol_type = Column(Enum('sea_salt', 'dust', 'volcanic_ash', name='AerosolTypeEnum'), nullable=False )
    id = Column(UUID(), ForeignKey('Sample.id'), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    type = Column(Text())
    ['study'_'study_id'_'project_id'_'proposal'_'proposal_id'] = Column(Integer())
    emsl_activity = Column(Text())
    storage_condition = Column(Enum('fresh', 'frozen', 'lyophilized', 'other', name='StorageConditionEnum'))
    oxygen_relationship = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'oblifate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    biotic_relationship = Column(Enum('free_living', 'parasite', 'commensal', 'symbiont', name='BioticRelationshipEnum'))
    air_temp_regm = Column(Text())
    chem_administration = Column(Text())
    proposal_id = Column(Integer())
    other_storage_condt = Column(Text())
    

    

    def __repr__(self):
        return f"AerosolSample(aerosol_type={self.aerosol_type},id={self.id},name={self.name},description={self.description},type={self.type},['study'_'study_id'_'project_id'_'proposal'_'proposal_id']={self.['study'_'study_id'_'project_id'_'proposal'_'proposal_id']},emsl_activity={self.emsl_activity},storage_condition={self.storage_condition},oxygen_relationship={self.oxygen_relationship},biotic_relationship={self.biotic_relationship},air_temp_regm={self.air_temp_regm},chem_administration={self.chem_administration},proposal_id={self.proposal_id},other_storage_condt={self.other_storage_condt},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ProcessedSample(Sample):
    """
    A sample that has undergone processing or analysis. Processed Sample entities are derived from Activitites. Relationships to original sample, other processed samples, and projects is avaialble via following Activity to Entity relationships: has_input, has_output.
    """
    __tablename__ = 'ProcessedSample'

    id = Column(UUID(), ForeignKey('Sample.id'), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    type = Column(Text())
    ['study'_'study_id'_'project_id'_'proposal'_'proposal_id'] = Column(Integer())
    emsl_activity = Column(Text())
    storage_condition = Column(Enum('fresh', 'frozen', 'lyophilized', 'other', name='StorageConditionEnum'))
    oxygen_relationship = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'oblifate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    biotic_relationship = Column(Enum('free_living', 'parasite', 'commensal', 'symbiont', name='BioticRelationshipEnum'))
    air_temp_regm = Column(Text())
    chem_administration = Column(Text())
    proposal_id = Column(Integer())
    other_storage_condt = Column(Text())
    

    

    def __repr__(self):
        return f"ProcessedSample(id={self.id},name={self.name},description={self.description},type={self.type},['study'_'study_id'_'project_id'_'proposal'_'proposal_id']={self.['study'_'study_id'_'project_id'_'proposal'_'proposal_id']},emsl_activity={self.emsl_activity},storage_condition={self.storage_condition},oxygen_relationship={self.oxygen_relationship},biotic_relationship={self.biotic_relationship},air_temp_regm={self.air_temp_regm},chem_administration={self.chem_administration},proposal_id={self.proposal_id},other_storage_condt={self.other_storage_condt},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SoilSamplingActivity(SamplingActivity):
    """
    A sampling activity specific to soil samples.
    """
    __tablename__ = 'SoilSamplingActivity'

    name = Column(Text(), nullable=False )
    description = Column(Text())
    type = Column(Text())
    id = Column(UUID(), ForeignKey('SamplingActivity.id'), primary_key=True, nullable=False )
    profile_position = Column(Enum('backslope', 'footslope', 'shoulder', 'summit', 'toeslope', name='profilepositionenum'))
    sediment_type = Column(Enum('biogenous', 'cosmogenous', 'hydrogenous', 'lithogenous', name='sedimenttypeenum'))
    soil_horizon = Column(Enum('a_horizon', 'b_horizon', 'c_horizon', 'e_horizon', 'o_horizon', 'permafrost', 'r_layer', name='soilhorizonenum'))
    tillage = Column(Enum('Chisel', 'Cutting_Disc', 'Disc_Plough', 'Drill', 'Mouldboard', 'Ridge_Till', 'Streip_Tillage', 'Tined', 'Zonal_Tillage', name='tillageenum'))
    wind_direction = Column(Enum('north', 'north_east', 'east', 'south_east', 'south', 'south_west', 'west', 'north_west', name='winddirectionenum'))
    agrochem_addition = Column(Text())
    al_sat = Column(Float())
    al_sat_meth = Column(Text())
    biotic_regm = Column(Text())
    climate_environment = Column(Text())
    core_collector = Column(Text())
    crop_rotation = Column(Boolean())
    crop_rotation_schedule = Column(Text())
    cur_vegetation = Column(Text())
    cur_vegetation_meth = Column(Text())
    filter_method = Column(Text())
    fire = Column(DateTime())
    flooding = Column(DateTime())
    heavy_metals = Column(Text())
    heavy_metals_meth = Column(Text())
    horizon_meth = Column(Text())
    infiltration_1 = Column(Time())
    infiltration_2 = Column(Time())
    infiltration_notes = Column(Text())
    link_class_info = Column(Text())
    link_climate_info = Column(Text())
    local_class = Column(Text())
    local_class_meth = Column(Text())
    perturbation = Column(Text())
    previous_land_use = Column(Text())
    previous_land_use_meth = Column(Text())
    site_definition = Column(Text())
    soil_type = Column(Text())
    soil_type_meth = Column(Text())
    texture_meth = Column(Text())
    water_content_meth = Column(Text())
    weather = Column(Text())
    ['study'_'study_id'_'project_id'_'proposal'_'proposal_id'] = Column(Integer())
    emsl_activity = Column(Text())
    sample_name = Column(Text(), nullable=False )
    lims_barcode = Column(Text())
    growth_facil = Column(Enum('field', 'commercially_purchased', 'experimental_garden', 'field_incubation', 'greenhouse', 'growth_chamber', 'lab_incubation', 'open_top_chamber', 'other', name='growthfacilityenum'))
    other_growth_facil = Column(Text())
    sample_store_temp = Column(Enum('fresh4', 'freshroom', 'frozen20', 'frozen80', 'other', name='samplestoretemp'))
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
    
    
    # ManyToMany
    has_output = relationship( "SoilSample", secondary="SoilSamplingActivity_has_output")
    

    

    def __repr__(self):
        return f"SoilSamplingActivity(name={self.name},description={self.description},type={self.type},id={self.id},profile_position={self.profile_position},sediment_type={self.sediment_type},soil_horizon={self.soil_horizon},tillage={self.tillage},wind_direction={self.wind_direction},agrochem_addition={self.agrochem_addition},al_sat={self.al_sat},al_sat_meth={self.al_sat_meth},biotic_regm={self.biotic_regm},climate_environment={self.climate_environment},core_collector={self.core_collector},crop_rotation={self.crop_rotation},crop_rotation_schedule={self.crop_rotation_schedule},cur_vegetation={self.cur_vegetation},cur_vegetation_meth={self.cur_vegetation_meth},filter_method={self.filter_method},fire={self.fire},flooding={self.flooding},heavy_metals={self.heavy_metals},heavy_metals_meth={self.heavy_metals_meth},horizon_meth={self.horizon_meth},infiltration_1={self.infiltration_1},infiltration_2={self.infiltration_2},infiltration_notes={self.infiltration_notes},link_class_info={self.link_class_info},link_climate_info={self.link_climate_info},local_class={self.local_class},local_class_meth={self.local_class_meth},perturbation={self.perturbation},previous_land_use={self.previous_land_use},previous_land_use_meth={self.previous_land_use_meth},site_definition={self.site_definition},soil_type={self.soil_type},soil_type_meth={self.soil_type_meth},texture_meth={self.texture_meth},water_content_meth={self.water_content_meth},weather={self.weather},['study'_'study_id'_'project_id'_'proposal'_'proposal_id']={self.['study'_'study_id'_'project_id'_'proposal'_'proposal_id']},emsl_activity={self.emsl_activity},sample_name={self.sample_name},lims_barcode={self.lims_barcode},growth_facil={self.growth_facil},other_growth_facil={self.other_growth_facil},sample_store_temp={self.sample_store_temp},collection_date={self.collection_date},collection_time={self.collection_time},env_broad_scale_other={self.env_broad_scale_other},env_local_scale_other={self.env_local_scale_other},env_medium_other={self.env_medium_other},experimental_factor={self.experimental_factor},experimental_factor_other={self.experimental_factor_other},extraction_method={self.extraction_method},extreme_event={self.extreme_event},gaseous_environment={self.gaseous_environment},geo_loc_name={self.geo_loc_name},humidity_regm={self.humidity_regm},isotope_exposure={self.isotope_exposure},light_regm={self.light_regm},link_addit_analys={self.link_addit_analys},method_development={self.method_development},misc_param={self.misc_param},neon_plot_id={self.neon_plot_id},non_microb_biomass_method={self.non_microb_biomass_method},other_sample_store_temp={self.other_sample_store_temp},other_treatment={self.other_treatment},ph={self.ph},ph_meth={self.ph_meth},salinity={self.salinity},salinity_method={self.salinity_method},sample_collected={self.sample_collected},sample_collection_dev={self.sample_collection_dev},sample_collection_method={self.sample_collection_method},sample_end_time={self.sample_end_time},sample_processing={self.sample_processing},sample_start_time={self.sample_start_time},season_environment={self.season_environment},shipped_sample_size={self.shipped_sample_size},sieving={self.sieving},start_date_inc={self.start_date_inc},tot_nitro_cont_meth={self.tot_nitro_cont_meth},tot_org_c_meth={self.tot_org_c_meth},watering_regm={self.watering_regm},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class BulkDensityMethod(Method):
    """
    
    """
    __tablename__ = 'BulkDensityMethod'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    analytic = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"BulkDensityMethod(id={self.id},analytic={self.analytic},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ElementalAnalysisMethod(Method):
    """
    
    """
    __tablename__ = 'ElementalAnalysisMethod'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    analytic = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"ElementalAnalysisMethod(id={self.id},analytic={self.analytic},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class EnzymeActivityMethod(Method):
    """
    
    """
    __tablename__ = 'EnzymeActivityMethod'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    location = Column(Text(), nullable=False )
    incubation_temp_c = Column(Float())
    incubation_time = Column(Text())
    wavelength = Column(Float())
    analytic = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"EnzymeActivityMethod(id={self.id},location={self.location},incubation_temp_c={self.incubation_temp_c},incubation_time={self.incubation_time},wavelength={self.wavelength},analytic={self.analytic},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class GravimetricWaterContentMethod(Method):
    """
    
    """
    __tablename__ = 'GravimetricWaterContentMethod'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    location = Column(Text(), nullable=False )
    analytic = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"GravimetricWaterContentMethod(id={self.id},location={self.location},analytic={self.analytic},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class HydraulicPropertiesMethod(Method):
    """
    
    """
    __tablename__ = 'HydraulicPropertiesMethod'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    location = Column(Text(), nullable=False )
    fitting_model = Column(Text(), nullable=False )
    analytic = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"HydraulicPropertiesMethod(id={self.id},location={self.location},fitting_model={self.fitting_model},analytic={self.analytic},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class KuoMethod(Method):
    """
    
    """
    __tablename__ = 'KuoMethod'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    location = Column(Text(), nullable=False )
    method = Column(Text())
    detection_limit = Column(Text(), nullable=False )
    wavelength = Column(Text())
    analytic = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"KuoMethod(id={self.id},location={self.location},method={self.method},detection_limit={self.detection_limit},wavelength={self.wavelength},analytic={self.analytic},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MicrobialBiomassMethod(Method):
    """
    
    """
    __tablename__ = 'MicrobialBiomassMethod'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    location = Column(Text(), nullable=False )
    detector = Column(Text(), nullable=False )
    mode = Column(Text())
    injection_volume = Column(Text(), nullable=False )
    sample_volume = Column(Text(), nullable=False )
    number_of_injections = Column(Float(), nullable=False )
    check_standard_spacing = Column(Text(), nullable=False )
    analytic = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"MicrobialBiomassMethod(id={self.id},location={self.location},detector={self.detector},mode={self.mode},injection_volume={self.injection_volume},sample_volume={self.sample_volume},number_of_injections={self.number_of_injections},check_standard_spacing={self.check_standard_spacing},analytic={self.analytic},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class PH_Method(Method):
    """
    
    """
    __tablename__ = 'PH_Method'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    location = Column(Text(), nullable=False )
    calibration = Column(Text(), nullable=False )
    analytic = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"PH_Method(id={self.id},location={self.location},calibration={self.calibration},analytic={self.analytic},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class RespirationMethod(Method):
    """
    
    """
    __tablename__ = 'RespirationMethod'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    respiration_analysis_type = Column(Text(), nullable=False )
    sample_volume_id = Column(UUID(), ForeignKey('quantityValue.id'))
    scale_id = Column(UUID(), ForeignKey('quantityValue.id'))
    duration_id = Column(UUID(), ForeignKey('quantityValue.id'))
    sampling_time_id = Column(UUID(), ForeignKey('quantityValue.id'))
    bottle_vol_id = Column(UUID(), ForeignKey('quantityValue.id'))
    analytic = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"RespirationMethod(id={self.id},respiration_analysis_type={self.respiration_analysis_type},sample_volume_id={self.sample_volume_id},scale_id={self.scale_id},duration_id={self.duration_id},sampling_time_id={self.sampling_time_id},bottle_vol_id={self.bottle_vol_id},analytic={self.analytic},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class TOC_TN_Method(Method):
    """
    
    """
    __tablename__ = 'TOC_TN_Method'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    location = Column(Text(), nullable=False )
    column = Column(Text())
    mode = Column(Text())
    detector = Column(Text(), nullable=False )
    injection_volume = Column(Text(), nullable=False )
    sample_volume = Column(Text(), nullable=False )
    number_of_injections = Column(Float(), nullable=False )
    check_standard_spacing = Column(Text())
    analytic = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"TOC_TN_Method(id={self.id},location={self.location},column={self.column},mode={self.mode},detector={self.detector},injection_volume={self.injection_volume},sample_volume={self.sample_volume},number_of_injections={self.number_of_injections},check_standard_spacing={self.check_standard_spacing},analytic={self.analytic},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class TextureMethod(Method):
    """
    
    """
    __tablename__ = 'TextureMethod'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    location = Column(Text(), nullable=False )
    method = Column(Text())
    analytic = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"TextureMethod(id={self.id},location={self.location},method={self.method},analytic={self.analytic},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class XrayComputedTomographyMethod(Method):
    """
    
    """
    __tablename__ = 'XrayComputedTomographyMethod'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    location = Column(Text(), nullable=False )
    x_ray_power = Column(Text(), nullable=False )
    cu_filter = Column(Text(), nullable=False )
    total_projections_collected = Column(Float(), nullable=False )
    rotation = Column(Text(), nullable=False )
    frames_recording_per_projection = Column(Float(), nullable=False )
    exposure_time_per_frame = Column(Text(), nullable=False )
    image_voxel_size_is = Column(Text(), nullable=False )
    analytic = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"XrayComputedTomographyMethod(id={self.id},location={self.location},x_ray_power={self.x_ray_power},cu_filter={self.cu_filter},total_projections_collected={self.total_projections_collected},rotation={self.rotation},frames_recording_per_projection={self.frames_recording_per_projection},exposure_time_per_frame={self.exposure_time_per_frame},image_voxel_size_is={self.image_voxel_size_is},analytic={self.analytic},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Strain(PurchasedMaterial):
    """
    A microbial strain entity.  Strains are reference data   they are stable
identities that get referenced by culture growth activities.

entity_type discriminator value: 'strain'

Montana source: amp2-metadata.yaml Strain class, amp2-complete-001.yaml strain_set
    """
    __tablename__ = 'Strain'

    strain_identifier = Column(Text(), nullable=False )
    strain_type = Column(Text())
    strain_source = Column(Text())
    strain_mutation = Column(Text())
    entity_type = Column(Text(), nullable=False )
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    

    

    def __repr__(self):
        return f"Strain(strain_identifier={self.strain_identifier},strain_type={self.strain_type},strain_source={self.strain_source},strain_mutation={self.strain_mutation},entity_type={self.entity_type},id={self.id},name={self.name},description={self.description},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MediaPreparation(SampleProcessing):
    """
    Activity that prepares a batch of growth media.
Replaces the former labPreparationActivity + MediaCreation pattern.

Media details (recipe, formulation, sterilisation, etc.) are carried as
slots on this activity.  The physical media batch is represented as a
processedSample(type='prepared_media') linked via processingSampleLink
(role: output_sample).  Downstream CultureGrowth and AMP2PlateSetupActivity
activities reference that processedSample via the media_ref FK slot.

Lifecycle:
  MediaPreparation activity
    -> processingSampleLink(role=output_sample)
    -> processedSample(type='prepared_media'); media_ref points here
    -> CultureGrowth / AMP2PlateSetupActivity.media_ref

Montana source: amp2-metadata.yaml MediaCreation class,
                amp2-complete-001.yaml media_creation_activity_set
    """
    __tablename__ = 'MediaPreparation'

    media_type = Column(Enum('strain_purity', 'stock_culture', 'pre_culture', 'rich_media', 'minimal_media', name='MediaTypeEnum'))
    volume_ml = Column(Float())
    media_recipe = Column(Text())
    media_formulation = Column(Enum('manual_mix', 'commercial', 'premixed', name='FormulationEnum'))
    commercial_media_catalog = Column(Text())
    sterilization_method = Column(Enum('autoclave', 'filter', 'uv', 'none', name='SterilizationMethodEnum'))
    ph_adjustment = Column(Boolean())
    ph_target = Column(Float())
    storage_temperature = Column(Text())
    creation_date = Column(Date())
    id = Column(UUID(), primary_key=True, nullable=False )
    analysis_type = Column(Enum('analysis_activity', 'lcms_metabolomics_method', 'fticr_acquisition_method', 'gravimetric_water_content_method', 'ph_method', 'hydraulic_properties_method', 'microbial_biomass_method', 'xray_computed_tomography_method', 'REGEN', 'KUO', 'respiration_method', 'texture_method', 'enzyme_activity_method', 'elemental_analysis_method', 'toc_tn_method', 'bulk_density_method', 'metagenomics_method', 'xrf_analysis', 'xrd_analysis', name='routemethod'))
    method_name = Column(Enum('MAOM', 'WOEM', name='methodname'))
    processing_steps = Column(Text(), nullable=False )
    url = Column(Text())
    version = Column(Text())
    
    
    exposure_sensitivity_rel = relationship( "MediaPreparation_exposure_sensitivity" )
    exposure_sensitivity = association_proxy("exposure_sensitivity_rel", "exposure_sensitivity",
                                  creator=lambda x_: MediaPreparation_exposure_sensitivity(exposure_sensitivity=x_))
    
    
    media_additions_rel = relationship( "MediaPreparation_media_additions" )
    media_additions = association_proxy("media_additions_rel", "media_additions",
                                  creator=lambda x_: MediaPreparation_media_additions(media_additions=x_))
    

    

    def __repr__(self):
        return f"MediaPreparation(media_type={self.media_type},volume_ml={self.volume_ml},media_recipe={self.media_recipe},media_formulation={self.media_formulation},commercial_media_catalog={self.commercial_media_catalog},sterilization_method={self.sterilization_method},ph_adjustment={self.ph_adjustment},ph_target={self.ph_target},storage_temperature={self.storage_temperature},creation_date={self.creation_date},id={self.id},analysis_type={self.analysis_type},method_name={self.method_name},processing_steps={self.processing_steps},url={self.url},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class CultureGrowth(SampleProcessing):
    """
    Abstract base for culture growth activities.  Inherits processing
infrastructure from sampleProcessing and gains incubation conditions
via mixin.  media_ref and strain_ref are declared directly (no mixins).

Input/output sample linkage: via processingSampleLink (existing mechanism).
Media reference: media_ref -> processedSample(type='prepared_media')
Strain reference: strain_ref -> Strain (purchasedMaterial)

Montana source: amp2-metadata.yaml CultureGrowth class
    """
    __tablename__ = 'CultureGrowth'

    media_ref = Column(UUID(), ForeignKey('ProcessedSample.id'))
    strain_ref = Column(UUID(), ForeignKey('Strain.id'))
    incubation_time_hours = Column(Float())
    container_type = Column(Text())
    temperature_celsius = Column(Float())
    agitation_speed_rpm = Column(Integer())
    oxygen_status = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analysis_type = Column(Enum('analysis_activity', 'lcms_metabolomics_method', 'fticr_acquisition_method', 'gravimetric_water_content_method', 'ph_method', 'hydraulic_properties_method', 'microbial_biomass_method', 'xray_computed_tomography_method', 'REGEN', 'KUO', 'respiration_method', 'texture_method', 'enzyme_activity_method', 'elemental_analysis_method', 'toc_tn_method', 'bulk_density_method', 'metagenomics_method', 'xrf_analysis', 'xrd_analysis', name='routemethod'))
    method_name = Column(Enum('MAOM', 'WOEM', name='methodname'))
    processing_steps = Column(Text(), nullable=False )
    url = Column(Text())
    version = Column(Text())
    

    

    def __repr__(self):
        return f"CultureGrowth(media_ref={self.media_ref},strain_ref={self.strain_ref},incubation_time_hours={self.incubation_time_hours},container_type={self.container_type},temperature_celsius={self.temperature_celsius},agitation_speed_rpm={self.agitation_speed_rpm},oxygen_status={self.oxygen_status},id={self.id},analysis_type={self.analysis_type},method_name={self.method_name},processing_steps={self.processing_steps},url={self.url},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class PlateSetupActivity(SampleProcessing):
    """
    Abstract base for 96-well plate setup activities.
Common plate-level metadata shared across AMP2 and Ecoplate workflows.
Subclasses differ in how they handle well-level metadata and media references.

Input:  processedSample (experimental culture, soil extract, etc.)
        via processingSampleLink (role: input_sample)
Output: processedSample(type='*_plate') via processingSampleLink

v1 origin: plate-general.yaml PlateSetupActivity
    """
    __tablename__ = 'PlateSetupActivity'

    plate_type = Column(Text(), nullable=False )
    plate_barcode = Column(Text())
    setup_date = Column(DateTime(), nullable=False )
    setup_operator_id = Column(UUID(), ForeignKey('personValue.id'))
    setup_instrument = Column(Text())
    sealing_method = Column(Text())
    temperature_celsius = Column(Float())
    agitation_speed_rpm = Column(Integer())
    oxygen_status = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analysis_type = Column(Enum('analysis_activity', 'lcms_metabolomics_method', 'fticr_acquisition_method', 'gravimetric_water_content_method', 'ph_method', 'hydraulic_properties_method', 'microbial_biomass_method', 'xray_computed_tomography_method', 'REGEN', 'KUO', 'respiration_method', 'texture_method', 'enzyme_activity_method', 'elemental_analysis_method', 'toc_tn_method', 'bulk_density_method', 'metagenomics_method', 'xrf_analysis', 'xrd_analysis', name='routemethod'))
    method_name = Column(Enum('MAOM', 'WOEM', name='methodname'))
    processing_steps = Column(Text(), nullable=False )
    url = Column(Text())
    version = Column(Text())
    
    
    # One-To-Many: OneToAnyMapping(source_class='PlateSetupActivity', source_slot='well_metadata', mapping_type=None, target_class='WellMetadata', target_slot='PlateSetupActivity_id', join_class=None, uses_join_table=None, multivalued=False)
    well_metadata = relationship( "WellMetadata", foreign_keys="[WellMetadata.PlateSetupActivity_id]")
    

    

    def __repr__(self):
        return f"PlateSetupActivity(plate_type={self.plate_type},plate_barcode={self.plate_barcode},setup_date={self.setup_date},setup_operator_id={self.setup_operator_id},setup_instrument={self.setup_instrument},sealing_method={self.sealing_method},temperature_celsius={self.temperature_celsius},agitation_speed_rpm={self.agitation_speed_rpm},oxygen_status={self.oxygen_status},id={self.id},analysis_type={self.analysis_type},method_name={self.method_name},processing_steps={self.processing_steps},url={self.url},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class PlateAnalysisActivity(AnalysisActivity):
    """
    Abstract base for plate measurement activities.
Adds timepoint_label for repeated-measurement series (per core-planB
decision to put timepoint_label on concrete subclasses, not on base
analysisActivity).

v1 origin: plate-general.yaml PlateAnalysisActivity
    """
    __tablename__ = 'PlateAnalysisActivity'

    timepoint_label = Column(Text(), nullable=False )
    sequence_order = Column(Integer())
    version = Column(Text(), nullable=False )
    id = Column(UUID(), primary_key=True, nullable=False )
    analyte_id = Column(UUID(), ForeignKey('ProcessedSample.id'))
    name = Column(Text())
    acquisition_start_time = Column(DateTime(), nullable=False )
    acquisition_end_time = Column(DateTime(), nullable=False )
    instrument_id = Column(UUID(), ForeignKey('instrument.id'))
    protocol_url = Column(Text())
    instrument_operator_id = Column(UUID(), ForeignKey('personValue.id'))
    

    

    def __repr__(self):
        return f"PlateAnalysisActivity(timepoint_label={self.timepoint_label},sequence_order={self.sequence_order},version={self.version},id={self.id},analyte_id={self.analyte_id},name={self.name},acquisition_start_time={self.acquisition_start_time},acquisition_end_time={self.acquisition_end_time},instrument_id={self.instrument_id},protocol_url={self.protocol_url},instrument_operator_id={self.instrument_operator_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class AMP2ODProduct(PlateProduct):
    """
    AMP2 optical density measurement product.
One row per plate × timepoint.
processedData.type = 'amp2_od'

v1 origin: plate-general.yaml AMP2ODProduct
    """
    __tablename__ = 'AMP2ODProduct'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    plate_reader_model = Column(Text())
    wavelength_nm = Column(Integer(), nullable=False )
    timepoint_label = Column(Text(), nullable=False )
    plate_average = Column(Float())
    blank_mean = Column(Float())
    cv_percent = Column(Float())
    
    
    # One-To-Many: OneToAnyMapping(source_class='AMP2ODProduct', source_slot='well_readings', mapping_type=None, target_class='WellReading', target_slot='AMP2ODProduct_id', join_class=None, uses_join_table=None, multivalued=False)
    well_readings = relationship( "WellReading", foreign_keys="[WellReading.AMP2ODProduct_id]")
    

    

    def __repr__(self):
        return f"AMP2ODProduct(id={self.id},plate_reader_model={self.plate_reader_model},wavelength_nm={self.wavelength_nm},timepoint_label={self.timepoint_label},plate_average={self.plate_average},blank_mean={self.blank_mean},cv_percent={self.cv_percent},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class EcoplateAbsorbanceProduct(PlateProduct):
    """
    Ecoplate absorbance measurement product.
One row per plate × timepoint.
processedData.type = 'ecoplate_absorbance'

v1 origin: plate-general.yaml EcoplateAbsorbanceProduct
    """
    __tablename__ = 'EcoplateAbsorbanceProduct'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    plate_lot = Column(Text())
    uninoculated_mean = Column(Float())
    average_well_color_development = Column(Float())
    wavelength_nm = Column(Integer(), nullable=False )
    timepoint_label = Column(Text(), nullable=False )
    plate_average = Column(Float())
    blank_mean = Column(Float())
    cv_percent = Column(Float())
    
    
    # One-To-Many: OneToAnyMapping(source_class='EcoplateAbsorbanceProduct', source_slot='well_readings', mapping_type=None, target_class='WellReading', target_slot='EcoplateAbsorbanceProduct_id', join_class=None, uses_join_table=None, multivalued=False)
    well_readings = relationship( "WellReading", foreign_keys="[WellReading.EcoplateAbsorbanceProduct_id]")
    

    

    def __repr__(self):
        return f"EcoplateAbsorbanceProduct(id={self.id},plate_lot={self.plate_lot},uninoculated_mean={self.uninoculated_mean},average_well_color_development={self.average_well_color_development},wavelength_nm={self.wavelength_nm},timepoint_label={self.timepoint_label},plate_average={self.plate_average},blank_mean={self.blank_mean},cv_percent={self.cv_percent},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class AMP2WellMetadata(WellMetadata):
    """
    AMP2-specific per-well metadata.
Minimal   media composition comes from the Media entity referenced via
the activity's media_ref slot.  Per-well data is volumes and replicate info.

Montana source: amp2-metadata.yaml WellDetails class,
                amp2-complete-001.yaml well layout patterns
    """
    __tablename__ = 'AMP2WellMetadata'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    media_ref = Column(UUID(), ForeignKey('ProcessedSample.id'))
    media_volume_ul = Column(Float(), nullable=False )
    inoculum_volume_ul = Column(Float(), nullable=False )
    sample_id = Column(Text())
    position = Column(Text(), nullable=False )
    well_type = Column(Text())
    replicate_group = Column(Text())
    
    
    treatments_rel = relationship( "AMP2WellMetadata_treatments" )
    treatments = association_proxy("treatments_rel", "treatments",
                                  creator=lambda x_: AMP2WellMetadata_treatments(treatments=x_))
    

    

    def __repr__(self):
        return f"AMP2WellMetadata(id={self.id},media_ref={self.media_ref},media_volume_ul={self.media_volume_ul},inoculum_volume_ul={self.inoculum_volume_ul},sample_id={self.sample_id},position={self.position},well_type={self.well_type},replicate_group={self.replicate_group},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class EcoplateWellMetadata(WellMetadata):
    """
    Ecoplate-specific per-well metadata.
Rich   no media entity; carbon source and treatment are per-well
experimental design variables.

v1 origin: plate-general.yaml EcoplateWellMetadata
    """
    __tablename__ = 'EcoplateWellMetadata'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    media_volume_ul = Column(Float(), nullable=False )
    carbon_source = Column(Text(), nullable=False )
    treatment = Column(Text())
    treatment_concentration = Column(Text())
    position = Column(Text(), nullable=False )
    well_type = Column(Text())
    replicate_group = Column(Text())
    

    

    def __repr__(self):
        return f"EcoplateWellMetadata(id={self.id},media_volume_ul={self.media_volume_ul},carbon_source={self.carbon_source},treatment={self.treatment},treatment_concentration={self.treatment_concentration},position={self.position},well_type={self.well_type},replicate_group={self.replicate_group},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MetagenomicsWorkflowExecutionActivity(WorkflowExecutionActivity):
    """
    Concrete metagenomics workflow run. Inherits all workflowExecutionActivity
slots including parent_workflow_id (chain link) and workflow_steps
(key-value, schema TBD). Specific workflow step type is captured via the
inherited type attribute (string); expected values: 
'metagenomics_annotation', 'metagenomics_binning', 'metagenomics_phylogeny'.
    """
    __tablename__ = 'MetagenomicsWorkflowExecutionActivity'

    parent_workflow_id = Column(UUID())
    workflow_steps = Column(Text())
    version = Column(Text(), nullable=False )
    description = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    type = Column(Text(), nullable=False )
    started_at_time = Column(DateTime(), nullable=False )
    ended_at_time = Column(DateTime())
    software_url = Column(Text())
    software_version = Column(Text())
    software_poc = Column(Text())
    execution_resource = Column(Enum('RZR', 'Tahoma', 'local', 'other', name='executionresourcetype'))
    

    

    def __repr__(self):
        return f"MetagenomicsWorkflowExecutionActivity(parent_workflow_id={self.parent_workflow_id},workflow_steps={self.workflow_steps},version={self.version},description={self.description},id={self.id},type={self.type},started_at_time={self.started_at_time},ended_at_time={self.ended_at_time},software_url={self.software_url},software_version={self.software_version},software_poc={self.software_poc},execution_resource={self.execution_resource},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MassSpectrometryAnalysisActivity(AnalysisActivity):
    """
    A record of the mass spectrometry run that generates a raw data product.
    """
    __tablename__ = 'MassSpectrometryAnalysisActivity'

    analyte_category = Column(Enum('dna', 'rna', 'protein', 'metabolite', 'lipid', 'natural_organic_matter', 'unknown', name='analytecategoryenum'))
    sequence_order = Column(Integer())
    version = Column(Text(), nullable=False )
    id = Column(UUID(), primary_key=True, nullable=False )
    analyte_id = Column(UUID(), ForeignKey('ProcessedSample.id'))
    name = Column(Text())
    acquisition_start_time = Column(DateTime(), nullable=False )
    acquisition_end_time = Column(DateTime(), nullable=False )
    instrument_id = Column(UUID(), ForeignKey('instrument.id'))
    protocol_url = Column(Text())
    instrument_operator_id = Column(UUID(), ForeignKey('personValue.id'))
    uses_ms_configuration_uid = Column(Integer(), ForeignKey('MassSpectrometryConfiguration.uid'), nullable=False )
    uses_ms_configuration = relationship("MassSpectrometryConfiguration", uselist=False, foreign_keys=[uses_ms_configuration_uid])
    uses_chromatography_uid = Column(Integer(), ForeignKey('ChromatographyConfiguration.uid'))
    uses_chromatography = relationship("ChromatographyConfiguration", uselist=False, foreign_keys=[uses_chromatography_uid])
    

    

    def __repr__(self):
        return f"MassSpectrometryAnalysisActivity(analyte_category={self.analyte_category},sequence_order={self.sequence_order},version={self.version},id={self.id},analyte_id={self.analyte_id},name={self.name},acquisition_start_time={self.acquisition_start_time},acquisition_end_time={self.acquisition_end_time},instrument_id={self.instrument_id},protocol_url={self.protocol_url},instrument_operator_id={self.instrument_operator_id},uses_ms_configuration_uid={self.uses_ms_configuration_uid},uses_chromatography_uid={self.uses_chromatography_uid},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MassSpectrometryConfiguration(Configuration):
    """
    Instrument configuration and setup for a mass spectrometry run.
    """
    __tablename__ = 'MassSpectrometryConfiguration'

    uid = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    location = Column(Text(), nullable=False )
    injection = Column(Text(), nullable=False )
    ionization = Column(Enum('ESI', 'EI', 'CI', 'MALDI', name='ionizationenum'), nullable=False )
    polarity = Column(Enum('positive', 'negative', name='polarityenum'), nullable=False )
    resolution = Column(Float(), nullable=False )
    scan_range = Column(Text(), nullable=False )
    dd_ms2_resolution = Column(Float(), nullable=False )
    loop_count = Column(Text(), nullable=False )
    iat = Column(Float())
    fid = Column(Float())
    mass_range = Column(Float())
    name = Column(Text(), nullable=False )
    description = Column(Text())
    id = Column(UUID(), nullable=False )
    

    

    def __repr__(self):
        return f"MassSpectrometryConfiguration(uid={self.uid},location={self.location},injection={self.injection},ionization={self.ionization},polarity={self.polarity},resolution={self.resolution},scan_range={self.scan_range},dd_ms2_resolution={self.dd_ms2_resolution},loop_count={self.loop_count},iat={self.iat},fid={self.fid},mass_range={self.mass_range},name={self.name},description={self.description},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ChromatographyConfiguration(Configuration):
    """
    Configuration and settings for a chromatography run.
    """
    __tablename__ = 'ChromatographyConfiguration'

    uid = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    column = Column(Text(), nullable=False )
    chromatography_type = Column(Enum('liquid_chromatography', 'gas_chromatography', 'solid_phase_extraction', name='chromatographytypeenum'), nullable=False )
    mobile_phases = Column(Text())
    stationary_phase = Column(Text())
    temperature_celsius = Column(Float())
    duration_min = Column(Float())
    name = Column(Text(), nullable=False )
    description = Column(Text())
    id = Column(UUID(), nullable=False )
    

    

    def __repr__(self):
        return f"ChromatographyConfiguration(uid={self.uid},column={self.column},chromatography_type={self.chromatography_type},mobile_phases={self.mobile_phases},stationary_phase={self.stationary_phase},temperature_celsius={self.temperature_celsius},duration_min={self.duration_min},name={self.name},description={self.description},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MassSpectrometryWorkflowExecutionActivity(WorkflowExecutionActivity):
    """
    Concrete mass spectrometry workflow run. Inherits all workflowExecutionActivity
slots including used_software and version.
    """
    __tablename__ = 'MassSpectrometryWorkflowExecutionActivity'

    uses_calibration = Column(UUID(), ForeignKey('MassSpectrometryStandardRun.id'))
    parent_workflow_id = Column(UUID())
    workflow_steps = Column(Text())
    version = Column(Text(), nullable=False )
    description = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    type = Column(Text(), nullable=False )
    started_at_time = Column(DateTime(), nullable=False )
    ended_at_time = Column(DateTime())
    software_url = Column(Text())
    software_version = Column(Text())
    software_poc = Column(Text())
    execution_resource = Column(Enum('RZR', 'Tahoma', 'local', 'other', name='executionresourcetype'))
    

    

    def __repr__(self):
        return f"MassSpectrometryWorkflowExecutionActivity(uses_calibration={self.uses_calibration},parent_workflow_id={self.parent_workflow_id},workflow_steps={self.workflow_steps},version={self.version},description={self.description},id={self.id},type={self.type},started_at_time={self.started_at_time},ended_at_time={self.ended_at_time},software_url={self.software_url},software_version={self.software_version},software_poc={self.software_poc},execution_resource={self.execution_resource},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class XRayAnalysisActivity(AnalysisActivity):
    """
    Abstract base class for X-ray analytical methods including XRF (elemental)
and XRD (mineralogical) analysis. Inherits acquisition_time, instrument_id,
protocol_url, analyte_id, and other core metadata from analysisActivity.

Concrete subclasses define method-specific measurement parameters.
Future X-ray methods (e.g., XCT) can extend this class.

Shared patterns:
  - Direct instrument output (no computational workflow) is typical for XRF
  - XRD may optionally link to workflowExecutionActivity for Rietveld refinement
  - protocol_url should link to vendor SOP or EMSL internal protocol documentation
    """
    __tablename__ = 'XRayAnalysisActivity'

    sequence_order = Column(Integer())
    version = Column(Text(), nullable=False )
    id = Column(UUID(), primary_key=True, nullable=False )
    analyte_id = Column(UUID(), ForeignKey('ProcessedSample.id'))
    name = Column(Text())
    acquisition_start_time = Column(DateTime(), nullable=False )
    acquisition_end_time = Column(DateTime(), nullable=False )
    instrument_id = Column(UUID(), ForeignKey('instrument.id'))
    protocol_url = Column(Text())
    instrument_operator_id = Column(UUID(), ForeignKey('personValue.id'))
    

    

    def __repr__(self):
        return f"XRayAnalysisActivity(sequence_order={self.sequence_order},version={self.version},id={self.id},analyte_id={self.analyte_id},name={self.name},acquisition_start_time={self.acquisition_start_time},acquisition_end_time={self.acquisition_end_time},instrument_id={self.instrument_id},protocol_url={self.protocol_url},instrument_operator_id={self.instrument_operator_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MonetSoilSample(SoilSample):
    """
    A soil sample with specific soil-related properties that align with the MONet Soil Sample template.
    """
    __tablename__ = 'MonetSoilSample'

    sampling_set = Column(Integer(), nullable=False )
    id = Column(UUID(), ForeignKey('Sample.id'), primary_key=True, nullable=False )
    soil_type = Column(Enum('soil_core', 'surface_layer', name='SoilTypeEnum'), nullable=False )
    soil_horizon = Column(Enum('A horizon', 'B horizon', 'C horizon', 'E horizon', 'O horizon', 'Permafrost', 'R layer', 'M horizon', name='SoilHorizonEnum'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    type = Column(Text())
    ['study'_'study_id'_'project_id'_'proposal'_'proposal_id'] = Column(Integer())
    emsl_activity = Column(Text())
    storage_condition = Column(Enum('fresh', 'frozen', 'lyophilized', 'other', name='StorageConditionEnum'))
    oxygen_relationship = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'oblifate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    biotic_relationship = Column(Enum('free_living', 'parasite', 'commensal', 'symbiont', name='BioticRelationshipEnum'))
    air_temp_regm = Column(Text())
    chem_administration = Column(Text())
    proposal_id = Column(Integer())
    other_storage_condt = Column(Text())
    

    

    def __repr__(self):
        return f"MonetSoilSample(sampling_set={self.sampling_set},id={self.id},soil_type={self.soil_type},soil_horizon={self.soil_horizon},name={self.name},description={self.description},type={self.type},['study'_'study_id'_'project_id'_'proposal'_'proposal_id']={self.['study'_'study_id'_'project_id'_'proposal'_'proposal_id']},emsl_activity={self.emsl_activity},storage_condition={self.storage_condition},oxygen_relationship={self.oxygen_relationship},biotic_relationship={self.biotic_relationship},air_temp_regm={self.air_temp_regm},chem_administration={self.chem_administration},proposal_id={self.proposal_id},other_storage_condt={self.other_storage_condt},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class CoreSection(ProcessedSample):
    """
    A section of a core sample (TOP, MID, BTM).
    """
    __tablename__ = 'CoreSection'

    core_section = Column(Text(), nullable=False )
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    type = Column(Text())
    ['study'_'study_id'_'project_id'_'proposal'_'proposal_id'] = Column(Integer())
    emsl_activity = Column(Text())
    storage_condition = Column(Enum('fresh', 'frozen', 'lyophilized', 'other', name='StorageConditionEnum'))
    oxygen_relationship = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'oblifate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    biotic_relationship = Column(Enum('free_living', 'parasite', 'commensal', 'symbiont', name='BioticRelationshipEnum'))
    air_temp_regm = Column(Text())
    chem_administration = Column(Text())
    proposal_id = Column(Integer())
    other_storage_condt = Column(Text())
    

    

    def __repr__(self):
        return f"CoreSection(core_section={self.core_section},id={self.id},name={self.name},description={self.description},type={self.type},['study'_'study_id'_'project_id'_'proposal'_'proposal_id']={self.['study'_'study_id'_'project_id'_'proposal'_'proposal_id']},emsl_activity={self.emsl_activity},storage_condition={self.storage_condition},oxygen_relationship={self.oxygen_relationship},biotic_relationship={self.biotic_relationship},air_temp_regm={self.air_temp_regm},chem_administration={self.chem_administration},proposal_id={self.proposal_id},other_storage_condt={self.other_storage_condt},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class BulkDensityProduct(ProcessedData):
    """
    
    """
    __tablename__ = 'BulkDensityProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    bulk_density_id = Column(UUID(), ForeignKey('quantityValue.id'))
    flag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"BulkDensityProduct(measure_type={self.measure_type},bulk_density_id={self.bulk_density_id},flag={self.flag},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},sample_id={self.sample_id},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ElementalAnalysisProduct(ProcessedData):
    """
    
    """
    __tablename__ = 'ElementalAnalysisProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    total_carbon_id = Column(UUID(), ForeignKey('quantityValue.id'))
    total_nitrogen_id = Column(UUID(), ForeignKey('quantityValue.id'))
    total_kjeldahl_nitrogen_id = Column(UUID(), ForeignKey('quantityValue.id'))
    total_sulfur_id = Column(UUID(), ForeignKey('quantityValue.id'))
    flag_total_carbon = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_total_nitrogen = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_tkn = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_total_sulfur = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"ElementalAnalysisProduct(measure_type={self.measure_type},total_carbon_id={self.total_carbon_id},total_nitrogen_id={self.total_nitrogen_id},total_kjeldahl_nitrogen_id={self.total_kjeldahl_nitrogen_id},total_sulfur_id={self.total_sulfur_id},flag_total_carbon={self.flag_total_carbon},flag_total_nitrogen={self.flag_total_nitrogen},flag_tkn={self.flag_tkn},flag_total_sulfur={self.flag_total_sulfur},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},sample_id={self.sample_id},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class EnzymeProduct(ProcessedData):
    """
    
    """
    __tablename__ = 'EnzymeProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    beta_glucosidase_ug_pnp_per_g_per_h_id = Column(UUID(), ForeignKey('quantityValue.id'))
    flag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"EnzymeProduct(measure_type={self.measure_type},beta_glucosidase_ug_pnp_per_g_per_h_id={self.beta_glucosidase_ug_pnp_per_g_per_h_id},flag={self.flag},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},sample_id={self.sample_id},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class GWCMoistureProduct(ProcessedData):
    """
    
    """
    __tablename__ = 'GWCMoistureProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    gwc_percent_id = Column(UUID(), ForeignKey('quantityValue.id'))
    flag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"GWCMoistureProduct(measure_type={self.measure_type},gwc_percent_id={self.gwc_percent_id},flag={self.flag},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},sample_id={self.sample_id},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class HydraulicPropertiesProduct(ProcessedData):
    """
    Soil hydraulic parameters derived from HYPROP evaporation-experiment data. One row per core section; the four attributes are the four VGM model parameters.  Proposal_ID, sampling_set, and core_section are inherited from the parent processedData record.
    """
    __tablename__ = 'HydraulicPropertiesProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    alpha = Column(Float())
    n = Column(Float())
    theta_r = Column(Float())
    theta_s = Column(Float())
    flag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"HydraulicPropertiesProduct(measure_type={self.measure_type},alpha={self.alpha},n={self.n},theta_r={self.theta_r},theta_s={self.theta_s},flag={self.flag},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},sample_id={self.sample_id},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class IonsAnalysisProduct(ProcessedData):
    """
    
    """
    __tablename__ = 'IonsAnalysisProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    sulfate_id = Column(UUID(), ForeignKey('quantityValue.id'))
    boron_id = Column(UUID(), ForeignKey('quantityValue.id'))
    zinc_id = Column(UUID(), ForeignKey('quantityValue.id'))
    manganate_id = Column(UUID(), ForeignKey('quantityValue.id'))
    copper_id = Column(UUID(), ForeignKey('quantityValue.id'))
    iron_id = Column(UUID(), ForeignKey('quantityValue.id'))
    calcium_id = Column(UUID(), ForeignKey('quantityValue.id'))
    magnesium_id = Column(UUID(), ForeignKey('quantityValue.id'))
    sodium_id = Column(UUID(), ForeignKey('quantityValue.id'))
    potassium_id = Column(UUID(), ForeignKey('quantityValue.id'))
    total_bases_id = Column(UUID(), ForeignKey('quantityValue.id'))
    cation_exchange_capacity_id = Column(UUID(), ForeignKey('quantityValue.id'))
    flag_sulfate = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_boron = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_zinc = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_manganate = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_copper = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_iron = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_calcium = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_magnesium = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_sodium = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_potassium = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_total_bases = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_cec = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"IonsAnalysisProduct(measure_type={self.measure_type},sulfate_id={self.sulfate_id},boron_id={self.boron_id},zinc_id={self.zinc_id},manganate_id={self.manganate_id},copper_id={self.copper_id},iron_id={self.iron_id},calcium_id={self.calcium_id},magnesium_id={self.magnesium_id},sodium_id={self.sodium_id},potassium_id={self.potassium_id},total_bases_id={self.total_bases_id},cation_exchange_capacity_id={self.cation_exchange_capacity_id},flag_sulfate={self.flag_sulfate},flag_boron={self.flag_boron},flag_zinc={self.flag_zinc},flag_manganate={self.flag_manganate},flag_copper={self.flag_copper},flag_iron={self.flag_iron},flag_calcium={self.flag_calcium},flag_magnesium={self.flag_magnesium},flag_sodium={self.flag_sodium},flag_potassium={self.flag_potassium},flag_total_bases={self.flag_total_bases},flag_cec={self.flag_cec},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},sample_id={self.sample_id},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MetaGenomicsProduct(ProcessedData):
    """
    
    """
    __tablename__ = 'MetaGenomicsProduct'

    input_to_step = Column(Enum('ReadQcAnalysis', 'MetagenomeAssembly', 'ReadBasedTaxonomyAnalysis', 'MetagenomeAnnotation', 'MagsAnalysis', 'FunctionalAnnotation', 'GenePhylogeny', name='metagenomicssteps'))
    output_to_step = Column(Enum('ReadQcAnalysis', 'MetagenomeAssembly', 'ReadBasedTaxonomyAnalysis', 'MetagenomeAnnotation', 'MagsAnalysis', 'FunctionalAnnotation', 'GenePhylogeny', name='metagenomicssteps'), nullable=False )
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"MetaGenomicsProduct(input_to_step={self.input_to_step},output_to_step={self.output_to_step},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},sample_id={self.sample_id},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MicrobialBiomassProduct(ProcessedData):
    """
    
    """
    __tablename__ = 'MicrobialBiomassProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    rep = Column(Numeric())
    mbc_id = Column(UUID(), ForeignKey('quantityValue.id'))
    mbc_avg = Column(Float())
    mbn_id = Column(UUID(), ForeignKey('quantityValue.id'))
    mbn_avg = Column(Float())
    flag_mbc = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_mbn = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_mbc_avg = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_mbn_avg = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"MicrobialBiomassProduct(measure_type={self.measure_type},rep={self.rep},mbc_id={self.mbc_id},mbc_avg={self.mbc_avg},mbn_id={self.mbn_id},mbn_avg={self.mbn_avg},flag_mbc={self.flag_mbc},flag_mbn={self.flag_mbn},flag_mbc_avg={self.flag_mbc_avg},flag_mbn_avg={self.flag_mbn_avg},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},sample_id={self.sample_id},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class NitrogenAnalysisProduct(ProcessedData):
    """
    
    """
    __tablename__ = 'NitrogenAnalysisProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    rep = Column(Numeric())
    no3_n_id = Column(UUID(), ForeignKey('quantityValue.id'))
    no3_n_avg = Column(Float())
    nh4_n_id = Column(UUID(), ForeignKey('quantityValue.id'))
    nh4_n_avg = Column(Float())
    flag_no3n = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_nh4n = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_no3n_avg = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_nh4n_avg = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"NitrogenAnalysisProduct(measure_type={self.measure_type},rep={self.rep},no3_n_id={self.no3_n_id},no3_n_avg={self.no3_n_avg},nh4_n_id={self.nh4_n_id},nh4_n_avg={self.nh4_n_avg},flag_no3n={self.flag_no3n},flag_nh4n={self.flag_nh4n},flag_no3n_avg={self.flag_no3n_avg},flag_nh4n_avg={self.flag_nh4n_avg},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},sample_id={self.sample_id},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class PhosphorusAnalysisProduct(ProcessedData):
    """
    
    """
    __tablename__ = 'PhosphorusAnalysisProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    rep = Column(Numeric())
    extraction_method = Column(Text())
    phosphorus_id = Column(UUID(), ForeignKey('quantityValue.id'))
    phosphorus_avg = Column(Float())
    flag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_avg = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"PhosphorusAnalysisProduct(measure_type={self.measure_type},rep={self.rep},extraction_method={self.extraction_method},phosphorus_id={self.phosphorus_id},phosphorus_avg={self.phosphorus_avg},flag={self.flag},flag_avg={self.flag_avg},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},sample_id={self.sample_id},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class RespirationProduct(ProcessedData):
    """
    
    """
    __tablename__ = 'RespirationProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    respiration_rate_per_day_id = Column(UUID(), ForeignKey('quantityValue.id'))
    flag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"RespirationProduct(measure_type={self.measure_type},respiration_rate_per_day_id={self.respiration_rate_per_day_id},flag={self.flag},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},sample_id={self.sample_id},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class TextureProduct(ProcessedData):
    """
    
    """
    __tablename__ = 'TextureProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    sand_pct_id = Column(UUID(), ForeignKey('quantityValue.id'))
    silt_pct_id = Column(UUID(), ForeignKey('quantityValue.id'))
    clay_pct_id = Column(UUID(), ForeignKey('quantityValue.id'))
    flag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"TextureProduct(measure_type={self.measure_type},sand_pct_id={self.sand_pct_id},silt_pct_id={self.silt_pct_id},clay_pct_id={self.clay_pct_id},flag={self.flag},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},sample_id={self.sample_id},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class TomographyProduct(ProcessedData):
    """
    
    """
    __tablename__ = 'TomographyProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    roi_volume_voxel = Column(Float())
    voxel_size = Column(Float())
    connected_pores = Column(Float())
    pore_diameter_min = Column(Float())
    pore_diameter_max = Column(Float())
    pore_diameter_mean = Column(Float())
    pore_diameter_median = Column(Float())
    pore_diameter_variance = Column(Float())
    pore_volume_mean = Column(Float())
    total_pore_volume = Column(Float())
    permeability_x = Column(Float())
    flow_rate_x = Column(Float())
    tortuosity_x = Column(Float())
    permeability_y = Column(Float())
    flow_rate_y = Column(Float())
    tortuosity_y = Column(Float())
    permeability_z = Column(Float())
    flow_rate_z = Column(Float())
    tortuosity_z = Column(Float())
    flag_xct = Column(Text())
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"TomographyProduct(measure_type={self.measure_type},roi_volume_voxel={self.roi_volume_voxel},voxel_size={self.voxel_size},connected_pores={self.connected_pores},pore_diameter_min={self.pore_diameter_min},pore_diameter_max={self.pore_diameter_max},pore_diameter_mean={self.pore_diameter_mean},pore_diameter_median={self.pore_diameter_median},pore_diameter_variance={self.pore_diameter_variance},pore_volume_mean={self.pore_volume_mean},total_pore_volume={self.total_pore_volume},permeability_x={self.permeability_x},flow_rate_x={self.flow_rate_x},tortuosity_x={self.tortuosity_x},permeability_y={self.permeability_y},flow_rate_y={self.flow_rate_y},tortuosity_y={self.tortuosity_y},permeability_z={self.permeability_z},flow_rate_z={self.flow_rate_z},tortuosity_z={self.tortuosity_z},flag_xct={self.flag_xct},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},sample_id={self.sample_id},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class PHProduct(ProcessedData):
    """
    
    """
    __tablename__ = 'pHProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    ph = Column(Float())
    flag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"pHProduct(measure_type={self.measure_type},ph={self.ph},flag={self.flag},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},sample_id={self.sample_id},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class XRayDataProduct(ProcessedData):
    """
    Abstract base class for X-ray analytical data products.
Inherits S3 storage metadata and sample linkage from dataProduct via processedData.

Concrete subclasses:
  - XRFElementalProduct: elemental concentrations (one row per sample)
  - XRDPhaseProduct: mineral phases (one row per sample)

Common patterns:
  - s3_key points to raw spectrum/diffractogram file in MinIO
  - summary_metrics (JSONB) provides lightweight queryable summaries:
      XRF: {"Ni_mg_kg":45.3, "Pb_mg_kg":8.2, "As_mg_kg":12.1}
      XRD: {"quartz_percent":42, "albite_percent":18, "kaolinite_percent":31}
  - workflow_id is NULL for direct instrument output (XRF typical)
  - workflow_id links to workflowExecutionActivity for computational processing (XRD Rietveld) 
    """
    __tablename__ = 'XRayDataProduct'

    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"XRayDataProduct(summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},sample_id={self.sample_id},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class StrainPurity(CultureGrowth):
    """
    Purity check of a strain culture.  Verifies that a sample contains the
expected strain without contamination.

Input:  sample(s) via processingSampleLink (role: input_sample)
Output: typically no new processedSample   pass/fail QC gate.
Refs:   Media (growth medium), Strain (target organism)

Montana source: amp2-metadata.yaml StrainPurity class,
                amp2-complete-001.yaml activity uuid:17
    """
    __tablename__ = 'StrainPurity'

    inspection_method = Column(Text())
    target_strain = Column(Text())
    contaminant_strains = Column(Text())
    media_ref = Column(UUID(), ForeignKey('ProcessedSample.id'))
    strain_ref = Column(UUID(), ForeignKey('Strain.id'))
    incubation_time_hours = Column(Float())
    container_type = Column(Text())
    temperature_celsius = Column(Float())
    agitation_speed_rpm = Column(Integer())
    oxygen_status = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analysis_type = Column(Enum('analysis_activity', 'lcms_metabolomics_method', 'fticr_acquisition_method', 'gravimetric_water_content_method', 'ph_method', 'hydraulic_properties_method', 'microbial_biomass_method', 'xray_computed_tomography_method', 'REGEN', 'KUO', 'respiration_method', 'texture_method', 'enzyme_activity_method', 'elemental_analysis_method', 'toc_tn_method', 'bulk_density_method', 'metagenomics_method', 'xrf_analysis', 'xrd_analysis', name='routemethod'))
    method_name = Column(Enum('MAOM', 'WOEM', name='methodname'))
    processing_steps = Column(Text(), nullable=False )
    url = Column(Text())
    version = Column(Text())
    

    

    def __repr__(self):
        return f"StrainPurity(inspection_method={self.inspection_method},target_strain={self.target_strain},contaminant_strains={self.contaminant_strains},media_ref={self.media_ref},strain_ref={self.strain_ref},incubation_time_hours={self.incubation_time_hours},container_type={self.container_type},temperature_celsius={self.temperature_celsius},agitation_speed_rpm={self.agitation_speed_rpm},oxygen_status={self.oxygen_status},id={self.id},analysis_type={self.analysis_type},method_name={self.method_name},processing_steps={self.processing_steps},url={self.url},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class StockCulturePreparation(CultureGrowth):
    """
    Preparation of a stock culture from user samples for long-term storage.

Input:  sample(s) via processingSampleLink (role: input_sample)
Output: processedSample(type='stock_culture') via processingSampleLink
Refs:   Media (growth medium), Strain

Montana source: amp2-metadata.yaml StockCulturePreparation class,
                amp2-complete-001.yaml activity uuid:18
    """
    __tablename__ = 'StockCulturePreparation'

    preparation_date = Column(Date())
    media_ref = Column(UUID(), ForeignKey('ProcessedSample.id'))
    strain_ref = Column(UUID(), ForeignKey('Strain.id'))
    incubation_time_hours = Column(Float())
    container_type = Column(Text())
    temperature_celsius = Column(Float())
    agitation_speed_rpm = Column(Integer())
    oxygen_status = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analysis_type = Column(Enum('analysis_activity', 'lcms_metabolomics_method', 'fticr_acquisition_method', 'gravimetric_water_content_method', 'ph_method', 'hydraulic_properties_method', 'microbial_biomass_method', 'xray_computed_tomography_method', 'REGEN', 'KUO', 'respiration_method', 'texture_method', 'enzyme_activity_method', 'elemental_analysis_method', 'toc_tn_method', 'bulk_density_method', 'metagenomics_method', 'xrf_analysis', 'xrd_analysis', name='routemethod'))
    method_name = Column(Enum('MAOM', 'WOEM', name='methodname'))
    processing_steps = Column(Text(), nullable=False )
    url = Column(Text())
    version = Column(Text())
    

    

    def __repr__(self):
        return f"StockCulturePreparation(preparation_date={self.preparation_date},media_ref={self.media_ref},strain_ref={self.strain_ref},incubation_time_hours={self.incubation_time_hours},container_type={self.container_type},temperature_celsius={self.temperature_celsius},agitation_speed_rpm={self.agitation_speed_rpm},oxygen_status={self.oxygen_status},id={self.id},analysis_type={self.analysis_type},method_name={self.method_name},processing_steps={self.processing_steps},url={self.url},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class PreCultureGrowth(CultureGrowth):
    """
    Growth of a pre-culture to establish viable inoculum before
experimental culture growth.

Input:  processedSample(type='stock_culture') via processingSampleLink
Output: processedSample(type='pre_culture') via processingSampleLink
Refs:   Media (growth medium), Strain

Montana source: amp2-metadata.yaml PreCultureGrowth class,
                amp2-complete-001.yaml activity uuid:19
    """
    __tablename__ = 'PreCultureGrowth'

    media_ref = Column(UUID(), ForeignKey('ProcessedSample.id'))
    strain_ref = Column(UUID(), ForeignKey('Strain.id'))
    incubation_time_hours = Column(Float())
    container_type = Column(Text())
    temperature_celsius = Column(Float())
    agitation_speed_rpm = Column(Integer())
    oxygen_status = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analysis_type = Column(Enum('analysis_activity', 'lcms_metabolomics_method', 'fticr_acquisition_method', 'gravimetric_water_content_method', 'ph_method', 'hydraulic_properties_method', 'microbial_biomass_method', 'xray_computed_tomography_method', 'REGEN', 'KUO', 'respiration_method', 'texture_method', 'enzyme_activity_method', 'elemental_analysis_method', 'toc_tn_method', 'bulk_density_method', 'metagenomics_method', 'xrf_analysis', 'xrd_analysis', name='routemethod'))
    method_name = Column(Enum('MAOM', 'WOEM', name='methodname'))
    processing_steps = Column(Text(), nullable=False )
    url = Column(Text())
    version = Column(Text())
    

    

    def __repr__(self):
        return f"PreCultureGrowth(media_ref={self.media_ref},strain_ref={self.strain_ref},incubation_time_hours={self.incubation_time_hours},container_type={self.container_type},temperature_celsius={self.temperature_celsius},agitation_speed_rpm={self.agitation_speed_rpm},oxygen_status={self.oxygen_status},id={self.id},analysis_type={self.analysis_type},method_name={self.method_name},processing_steps={self.processing_steps},url={self.url},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ExperimentalCulture(CultureGrowth):
    """
    Growth of an experimental culture for downstream analysis.
This is the terminal culture step before plate setup or direct measurement.

Input:  processedSample(type='pre_culture') via processingSampleLink
Output: processedSample(type='experimental_culture') via processingSampleLink
Refs:   Media (growth medium), Strain

Montana source: amp2-metadata.yaml ExperimentalCulture class,
                amp2-complete-001.yaml activity uuid:22
    """
    __tablename__ = 'ExperimentalCulture'

    treatment_type = Column(Text())
    growth_time = Column(Text())
    media_ref = Column(UUID(), ForeignKey('ProcessedSample.id'))
    strain_ref = Column(UUID(), ForeignKey('Strain.id'))
    incubation_time_hours = Column(Float())
    container_type = Column(Text())
    temperature_celsius = Column(Float())
    agitation_speed_rpm = Column(Integer())
    oxygen_status = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analysis_type = Column(Enum('analysis_activity', 'lcms_metabolomics_method', 'fticr_acquisition_method', 'gravimetric_water_content_method', 'ph_method', 'hydraulic_properties_method', 'microbial_biomass_method', 'xray_computed_tomography_method', 'REGEN', 'KUO', 'respiration_method', 'texture_method', 'enzyme_activity_method', 'elemental_analysis_method', 'toc_tn_method', 'bulk_density_method', 'metagenomics_method', 'xrf_analysis', 'xrd_analysis', name='routemethod'))
    method_name = Column(Enum('MAOM', 'WOEM', name='methodname'))
    processing_steps = Column(Text(), nullable=False )
    url = Column(Text())
    version = Column(Text())
    

    

    def __repr__(self):
        return f"ExperimentalCulture(treatment_type={self.treatment_type},growth_time={self.growth_time},media_ref={self.media_ref},strain_ref={self.strain_ref},incubation_time_hours={self.incubation_time_hours},container_type={self.container_type},temperature_celsius={self.temperature_celsius},agitation_speed_rpm={self.agitation_speed_rpm},oxygen_status={self.oxygen_status},id={self.id},analysis_type={self.analysis_type},method_name={self.method_name},processing_steps={self.processing_steps},url={self.url},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class AMP2PlateSetupActivity(PlateSetupActivity):
    """
    AMP2-specific plate setup.
media_ref points to the plate-level prepared media processedSample.
well_metadata stores minimal per-well data as AMP2WellMetadata instances
(position, volumes, replicate_group).  AMP2WellMetadata also carries a
per-well media_ref for plates that use different media per well.

Input:  processedSample(type='experimental_culture') via processingSampleLink
Output: processedSample(type='amp2_96well_plate') via processingSampleLink
Refs:   processedSample(type='prepared_media') via media_ref

v1 origin: plate-general.yaml AMP2PlateSetupActivity
v2 change: media_ref directly on class (no UsesMedia mixin);
           range is processedSample (not purchasedMaterial)
    """
    __tablename__ = 'AMP2PlateSetupActivity'

    media_ref = Column(UUID(), ForeignKey('ProcessedSample.id'))
    plate_type = Column(Text(), nullable=False )
    plate_barcode = Column(Text())
    setup_date = Column(DateTime(), nullable=False )
    setup_operator_id = Column(UUID(), ForeignKey('personValue.id'))
    setup_instrument = Column(Text())
    sealing_method = Column(Text())
    temperature_celsius = Column(Float())
    agitation_speed_rpm = Column(Integer())
    oxygen_status = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analysis_type = Column(Enum('analysis_activity', 'lcms_metabolomics_method', 'fticr_acquisition_method', 'gravimetric_water_content_method', 'ph_method', 'hydraulic_properties_method', 'microbial_biomass_method', 'xray_computed_tomography_method', 'REGEN', 'KUO', 'respiration_method', 'texture_method', 'enzyme_activity_method', 'elemental_analysis_method', 'toc_tn_method', 'bulk_density_method', 'metagenomics_method', 'xrf_analysis', 'xrd_analysis', name='routemethod'))
    method_name = Column(Enum('MAOM', 'WOEM', name='methodname'))
    processing_steps = Column(Text(), nullable=False )
    url = Column(Text())
    version = Column(Text())
    
    
    # One-To-Many: OneToAnyMapping(source_class='AMP2PlateSetupActivity', source_slot='well_metadata', mapping_type=None, target_class='WellMetadata', target_slot='AMP2PlateSetupActivity_id', join_class=None, uses_join_table=None, multivalued=False)
    well_metadata = relationship( "WellMetadata", foreign_keys="[WellMetadata.AMP2PlateSetupActivity_id]")
    

    

    def __repr__(self):
        return f"AMP2PlateSetupActivity(media_ref={self.media_ref},plate_type={self.plate_type},plate_barcode={self.plate_barcode},setup_date={self.setup_date},setup_operator_id={self.setup_operator_id},setup_instrument={self.setup_instrument},sealing_method={self.sealing_method},temperature_celsius={self.temperature_celsius},agitation_speed_rpm={self.agitation_speed_rpm},oxygen_status={self.oxygen_status},id={self.id},analysis_type={self.analysis_type},method_name={self.method_name},processing_steps={self.processing_steps},url={self.url},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class EcoplatePlateSetupActivity(PlateSetupActivity):
    """
    Ecoplate-specific plate setup.
NO media reference   carbon source and treatment are per-well experimental
design captured in EcoplateWellMetadata instances.

Input:  processedSample(type='soil_extract') via processingSampleLink
Output: processedSample(type='ecoplate_plate') via processingSampleLink

v1 origin: plate-general.yaml EcoplatePlateSetupActivity
    """
    __tablename__ = 'EcoplatePlateSetupActivity'

    plate_type = Column(Text(), nullable=False )
    plate_barcode = Column(Text())
    setup_date = Column(DateTime(), nullable=False )
    setup_operator_id = Column(UUID(), ForeignKey('personValue.id'))
    setup_instrument = Column(Text())
    sealing_method = Column(Text())
    temperature_celsius = Column(Float())
    agitation_speed_rpm = Column(Integer())
    oxygen_status = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analysis_type = Column(Enum('analysis_activity', 'lcms_metabolomics_method', 'fticr_acquisition_method', 'gravimetric_water_content_method', 'ph_method', 'hydraulic_properties_method', 'microbial_biomass_method', 'xray_computed_tomography_method', 'REGEN', 'KUO', 'respiration_method', 'texture_method', 'enzyme_activity_method', 'elemental_analysis_method', 'toc_tn_method', 'bulk_density_method', 'metagenomics_method', 'xrf_analysis', 'xrd_analysis', name='routemethod'))
    method_name = Column(Enum('MAOM', 'WOEM', name='methodname'))
    processing_steps = Column(Text(), nullable=False )
    url = Column(Text())
    version = Column(Text())
    
    
    # One-To-Many: OneToAnyMapping(source_class='EcoplatePlateSetupActivity', source_slot='well_metadata', mapping_type=None, target_class='WellMetadata', target_slot='EcoplatePlateSetupActivity_id', join_class=None, uses_join_table=None, multivalued=False)
    well_metadata = relationship( "WellMetadata", foreign_keys="[WellMetadata.EcoplatePlateSetupActivity_id]")
    

    

    def __repr__(self):
        return f"EcoplatePlateSetupActivity(plate_type={self.plate_type},plate_barcode={self.plate_barcode},setup_date={self.setup_date},setup_operator_id={self.setup_operator_id},setup_instrument={self.setup_instrument},sealing_method={self.sealing_method},temperature_celsius={self.temperature_celsius},agitation_speed_rpm={self.agitation_speed_rpm},oxygen_status={self.oxygen_status},id={self.id},analysis_type={self.analysis_type},method_name={self.method_name},processing_steps={self.processing_steps},url={self.url},version={self.version},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class AMP2AnalysisActivity(PlateAnalysisActivity):
    """
    AMP2 plate measurement (OD, fluorescence, flow cytometry).
analyte_id -> processedSample(type='amp2_96well_plate')

Chained via workflowExecutionActivity.parent_workflow_id to track
multi-timepoint series on the same plate.

v1 origin: plate-general.yaml AMP2AnalysisActivity
    """
    __tablename__ = 'AMP2AnalysisActivity'

    measurement_type = Column(Text())
    wavelength_nm = Column(Integer(), nullable=False )
    timepoint_label = Column(Text(), nullable=False )
    sequence_order = Column(Integer())
    version = Column(Text(), nullable=False )
    id = Column(UUID(), primary_key=True, nullable=False )
    analyte_id = Column(UUID(), ForeignKey('ProcessedSample.id'))
    name = Column(Text())
    acquisition_start_time = Column(DateTime(), nullable=False )
    acquisition_end_time = Column(DateTime(), nullable=False )
    instrument_id = Column(UUID(), ForeignKey('instrument.id'))
    protocol_url = Column(Text())
    instrument_operator_id = Column(UUID(), ForeignKey('personValue.id'))
    

    

    def __repr__(self):
        return f"AMP2AnalysisActivity(measurement_type={self.measurement_type},wavelength_nm={self.wavelength_nm},timepoint_label={self.timepoint_label},sequence_order={self.sequence_order},version={self.version},id={self.id},analyte_id={self.analyte_id},name={self.name},acquisition_start_time={self.acquisition_start_time},acquisition_end_time={self.acquisition_end_time},instrument_id={self.instrument_id},protocol_url={self.protocol_url},instrument_operator_id={self.instrument_operator_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class EcoplateAnalysisActivity(PlateAnalysisActivity):
    """
    Ecoplate absorbance measurement at a single timepoint.
analyte_id -> processedSample(type='ecoplate_plate')
wavelength_nm typically 590 for Biolog EcoPlates.

v1 origin: plate-general.yaml EcoplateAnalysisActivity
    """
    __tablename__ = 'EcoplateAnalysisActivity'

    wavelength_nm = Column(Integer(), nullable=False )
    timepoint_label = Column(Text(), nullable=False )
    sequence_order = Column(Integer())
    version = Column(Text(), nullable=False )
    id = Column(UUID(), primary_key=True, nullable=False )
    analyte_id = Column(UUID(), ForeignKey('ProcessedSample.id'))
    name = Column(Text())
    acquisition_start_time = Column(DateTime(), nullable=False )
    acquisition_end_time = Column(DateTime(), nullable=False )
    instrument_id = Column(UUID(), ForeignKey('instrument.id'))
    protocol_url = Column(Text())
    instrument_operator_id = Column(UUID(), ForeignKey('personValue.id'))
    

    

    def __repr__(self):
        return f"EcoplateAnalysisActivity(wavelength_nm={self.wavelength_nm},timepoint_label={self.timepoint_label},sequence_order={self.sequence_order},version={self.version},id={self.id},analyte_id={self.analyte_id},name={self.name},acquisition_start_time={self.acquisition_start_time},acquisition_end_time={self.acquisition_end_time},instrument_id={self.instrument_id},protocol_url={self.protocol_url},instrument_operator_id={self.instrument_operator_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MetagenomicsProduct(ProcessedData):
    """
    Abstract base for all metagenomics data products.
Inherits S3/file slots from dataProduct (via processedData is_a chain).
Concrete sub-types (Annotation, Binning, GenePhylogeny) use is_a to inherit
and add only their type-specific slots.
    """
    __tablename__ = 'MetagenomicsProduct'

    workflow_step = Column(Enum('ReadQcAnalysis', 'MetagenomeAssembly', 'ReadBasedTaxonomyAnalysis', 'MetagenomeAnnotation', 'MagsAnalysis', 'FunctionalAnnotation', 'GenePhylogeny', name='metagenomicssteps'))
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    provider_name = Column(UUID(), ForeignKey('controlledTermValue.id'))
    raw_fasta_url = Column(Text())
    additional_information = Column(Text())
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"MetagenomicsProduct(workflow_step={self.workflow_step},sample_id={self.sample_id},provider_name={self.provider_name},raw_fasta_url={self.raw_fasta_url},additional_information={self.additional_information},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MassSpectrometryInstrumentData(InstrumentData):
    """
    Raw data files output from a mass spectrometry instrument.
    """
    __tablename__ = 'MassSpectrometryInstrumentData'

    produced_by_ms_run = Column(UUID(), ForeignKey('MassSpectrometryAnalysisActivity.id'))
    ms_raw_file_type = Column(Enum('.d', '.raw', 'other', name='msrawfiletypeenum'))
    collection_mode = Column(Enum('profile', 'centroid', name='msmodeenum'))
    file_curie = Column(Text())
    alternative_identifiers = Column(Text())
    compression_type = Column(Text())
    type = Column(Text())
    file_type = Column(Enum('FT_ICR_MS_Analysis_Results', 'GC_MS_Metabolomics_Results', 'Metaproteomics_Workflow_Statistics', 'Protein_Report', 'Peptide_Report', 'Unfiltered_Metaproteomics_Results', 'Read_Count_and_RPKM', 'QC_non_rRNA_R2', 'QC_non_rRNA_R1', 'Metagenome_Bins', 'CheckM_Statistics', 'GOTTCHA2_Krona_Plot', 'Kraken2_Krona_Plot', 'Centrifuge_Krona_Plot', 'Kraken2_Classification_Report', 'Kraken2_Taxonomic_Classification', 'Centrifuge_Classification_Report', 'Centrifuge_Taxonomic_Classification', 'Structural_Annotation_GFF', 'Functional_Annotation_GFF', 'Annotation_Amino_Acid_FASTA', 'Annotation_Enzyme_Commission', 'Annotation_KEGG_Orthology', 'Assembly_Coverage_BAM', 'Assembly_AGP', 'Assembly_Scaffolds', 'Assembly_Contigs', 'Assembly_Coverage_Stats', 'Filtered_Sequencing_Reads', 'QC_Statistics', 'TIGRFam_Annotation_GFF', 'Clusters_of_Orthologous_Groups_COG_Annotation_GFF', 'CATH_FunFams_Functional_Families_Annotation_GFF', 'SUPERFam_Annotation_GFF', 'SMART_Annotation_GFF', 'Pfam_Annotation_GFF', 'Direct_Infusion_FT_ICR_MS_Raw_Data', name='filetype'))
    version = Column(Text())
    name = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"MassSpectrometryInstrumentData(produced_by_ms_run={self.produced_by_ms_run},ms_raw_file_type={self.ms_raw_file_type},collection_mode={self.collection_mode},file_curie={self.file_curie},alternative_identifiers={self.alternative_identifiers},compression_type={self.compression_type},type={self.type},file_type={self.file_type},version={self.version},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MassSpectrometryDataProduct(ProcessedData):
    """
    Abstract base for all mass spectrometry data products.
Inherits S3/file slots from dataProduct (via processedData is_a chain).
    """
    __tablename__ = 'MassSpectrometryDataProduct'

    results_from_ms_processing = Column(UUID(), ForeignKey('MassSpectrometryWorkflowExecutionActivity.id'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"MassSpectrometryDataProduct(results_from_ms_processing={self.results_from_ms_processing},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},sample_id={self.sample_id},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class XRFAnalysisActivity(XRayAnalysisActivity):
    """
    X-ray Fluorescence (XRF) elemental analysis activity.

XRF measures elemental composition by detecting characteristic X-ray emissions
from a sample bombarded with high-energy X-rays. Typical output: concentrations
of 10-30 elements per sample (Ni, Pb, As, Cr, Fe, Ca, K, etc.).

Data product: XRFElementalProduct (one row per element per sample)

Workflow pattern: Direct instrument output (no computational processing step)
  processedSample -> XRFAnalysisActivity -> XRFElementalProduct (workflow_id = NULL)

Protocol information: Stored externally; link via protocol_url attribute.
Example protocol parameters (stored in external SOP or workflowExecutionActivity
if computational correction is needed):
  - Beam voltage (kV), beam current (mA)
  - Measurement duration (seconds)
  - Matrix correction method (fundamental parameters, empirical)
  - Calibration date
  - Operator ID

Required enum additions to enums.yaml:
  routemethod:
    xrf_analysis:  # Add to routemethod permissible_values
    """
    __tablename__ = 'XRFAnalysisActivity'

    sequence_order = Column(Integer())
    version = Column(Text(), nullable=False )
    id = Column(UUID(), primary_key=True, nullable=False )
    analyte_id = Column(UUID(), ForeignKey('ProcessedSample.id'))
    name = Column(Text())
    acquisition_start_time = Column(DateTime(), nullable=False )
    acquisition_end_time = Column(DateTime(), nullable=False )
    instrument_id = Column(UUID(), ForeignKey('instrument.id'))
    protocol_url = Column(Text())
    instrument_operator_id = Column(UUID(), ForeignKey('personValue.id'))
    

    

    def __repr__(self):
        return f"XRFAnalysisActivity(sequence_order={self.sequence_order},version={self.version},id={self.id},analyte_id={self.analyte_id},name={self.name},acquisition_start_time={self.acquisition_start_time},acquisition_end_time={self.acquisition_end_time},instrument_id={self.instrument_id},protocol_url={self.protocol_url},instrument_operator_id={self.instrument_operator_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class XRDAnalysisActivity(XRayAnalysisActivity):
    """
    X-ray Diffraction (XRD) mineralogical analysis activity.

XRD identifies crystalline mineral phases by measuring diffraction patterns.
Output: mineral phase names and quantitative abundances (weight %).

Data product: XRDPhaseProduct (one row per mineral phase per sample)

Workflow patterns:
  1. Direct/semi-quantitative: 
       processedSample -> XRDAnalysisActivity -> XRDPhaseProduct (workflow_id = NULL)
  2. With Rietveld refinement (computational):
       processedSample -> XRDAnalysisActivity -> 
       workflowExecutionActivity(type='xrd_rietveld_refinement') -> 
       XRDPhaseProduct (workflow_id = refinement WEA)

Protocol information: Stored externally; link via protocol_url attribute.
Example protocol parameters (stored in external SOP or workflowExecutionActivity):
  - Diffractometer geometry (Bragg-Brentano, Debye-Scherrer)
  - X-ray tube type (Cu, Co, Mo)
  - Scan range (2-theta degrees), step size
  - Refinement software (HighScore Plus, GSAS-II, FullProf)
  - R-factor, GOF (goodness of fit)

Required enum additions to enums.yaml:
  routemethod:
    xrd_analysis:  # Add to routemethod permissible_values
    """
    __tablename__ = 'XRDAnalysisActivity'

    sequence_order = Column(Integer())
    version = Column(Text(), nullable=False )
    id = Column(UUID(), primary_key=True, nullable=False )
    analyte_id = Column(UUID(), ForeignKey('ProcessedSample.id'))
    name = Column(Text())
    acquisition_start_time = Column(DateTime(), nullable=False )
    acquisition_end_time = Column(DateTime(), nullable=False )
    instrument_id = Column(UUID(), ForeignKey('instrument.id'))
    protocol_url = Column(Text())
    instrument_operator_id = Column(UUID(), ForeignKey('personValue.id'))
    

    

    def __repr__(self):
        return f"XRDAnalysisActivity(sequence_order={self.sequence_order},version={self.version},id={self.id},analyte_id={self.analyte_id},name={self.name},acquisition_start_time={self.acquisition_start_time},acquisition_end_time={self.acquisition_end_time},instrument_id={self.instrument_id},protocol_url={self.protocol_url},instrument_operator_id={self.instrument_operator_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class XRFElementalProduct(XRayDataProduct):
    """
    X-ray Fluorescence (XRF) elemental concentration data.
One row per sample with columns for each element measured.

Follows the wide-format pattern established by IonsAnalysisProduct.
Element concentrations in mg/kg (parts per million dry weight basis) as float values.
Individual QC flags for each element using processeddataflag enum.

Relationship to core tables:
  - id: FK -> processedData.id (1:1 linkage)
  - processedData.type = 'XRFElementalProduct'
  - processedData.workflow_id = NULL (direct acquisition; no computational WEA)
  - processedData.summary_metrics = {"Ni_mg_kg":45.3, "Pb_mg_kg":8.2, ...}
  - processedData.s3_key = path to raw spectrum or calibrated CSV in MinIO

Standard XRF element panel (27 elements):
  Trace metals: Cl, V, Cr, Ni, Cu, Zn, Ga, As, Se, Br, Rb, Sr, Y, Nb, Mo,
                Ag, Cd, In, Sn, Sb, Cs, Ba, La, Ce, Pb, Th, U

Required enum additions to enums.yaml:
  product:
    XRFElementalProduct:  # Add to product permissible_values
    """
    __tablename__ = 'XRFElementalProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    cl_mg_per_kg = Column(Float())
    v_mg_per_kg = Column(Float())
    cr_mg_per_kg = Column(Float())
    ni_mg_per_kg = Column(Float())
    cu_mg_per_kg = Column(Float())
    zn_mg_per_kg = Column(Float())
    ga_mg_per_kg = Column(Float())
    as_mg_per_kg = Column(Float())
    se_mg_per_kg = Column(Float())
    br_mg_per_kg = Column(Float())
    rb_mg_per_kg = Column(Float())
    sr_mg_per_kg = Column(Float())
    y_mg_per_kg = Column(Float())
    nb_mg_per_kg = Column(Float())
    mo_mg_per_kg = Column(Float())
    ag_mg_per_kg = Column(Float())
    cd_mg_per_kg = Column(Float())
    in_mg_per_kg = Column(Float())
    sn_mg_per_kg = Column(Float())
    sb_mg_per_kg = Column(Float())
    cs_mg_per_kg = Column(Float())
    ba_mg_per_kg = Column(Float())
    la_mg_per_kg = Column(Float())
    ce_mg_per_kg = Column(Float())
    pb_mg_per_kg = Column(Float())
    th_mg_per_kg = Column(Float())
    u_mg_per_kg = Column(Float())
    flag_cl = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_v = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_cr = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_ni = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_cu = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_zn = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_ga = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_as = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_se = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_br = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_rb = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_sr = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_y = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_nb = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_mo = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_ag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_cd = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_in = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_sn = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_sb = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_cs = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_ba = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_la = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_ce = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_pb = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_th = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_u = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"XRFElementalProduct(measure_type={self.measure_type},cl_mg_per_kg={self.cl_mg_per_kg},v_mg_per_kg={self.v_mg_per_kg},cr_mg_per_kg={self.cr_mg_per_kg},ni_mg_per_kg={self.ni_mg_per_kg},cu_mg_per_kg={self.cu_mg_per_kg},zn_mg_per_kg={self.zn_mg_per_kg},ga_mg_per_kg={self.ga_mg_per_kg},as_mg_per_kg={self.as_mg_per_kg},se_mg_per_kg={self.se_mg_per_kg},br_mg_per_kg={self.br_mg_per_kg},rb_mg_per_kg={self.rb_mg_per_kg},sr_mg_per_kg={self.sr_mg_per_kg},y_mg_per_kg={self.y_mg_per_kg},nb_mg_per_kg={self.nb_mg_per_kg},mo_mg_per_kg={self.mo_mg_per_kg},ag_mg_per_kg={self.ag_mg_per_kg},cd_mg_per_kg={self.cd_mg_per_kg},in_mg_per_kg={self.in_mg_per_kg},sn_mg_per_kg={self.sn_mg_per_kg},sb_mg_per_kg={self.sb_mg_per_kg},cs_mg_per_kg={self.cs_mg_per_kg},ba_mg_per_kg={self.ba_mg_per_kg},la_mg_per_kg={self.la_mg_per_kg},ce_mg_per_kg={self.ce_mg_per_kg},pb_mg_per_kg={self.pb_mg_per_kg},th_mg_per_kg={self.th_mg_per_kg},u_mg_per_kg={self.u_mg_per_kg},flag_cl={self.flag_cl},flag_v={self.flag_v},flag_cr={self.flag_cr},flag_ni={self.flag_ni},flag_cu={self.flag_cu},flag_zn={self.flag_zn},flag_ga={self.flag_ga},flag_as={self.flag_as},flag_se={self.flag_se},flag_br={self.flag_br},flag_rb={self.flag_rb},flag_sr={self.flag_sr},flag_y={self.flag_y},flag_nb={self.flag_nb},flag_mo={self.flag_mo},flag_ag={self.flag_ag},flag_cd={self.flag_cd},flag_in={self.flag_in},flag_sn={self.flag_sn},flag_sb={self.flag_sb},flag_cs={self.flag_cs},flag_ba={self.flag_ba},flag_la={self.flag_la},flag_ce={self.flag_ce},flag_pb={self.flag_pb},flag_th={self.flag_th},flag_u={self.flag_u},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},sample_id={self.sample_id},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class XRDPhaseProduct(XRayDataProduct):
    """
    X-ray Diffraction (XRD) mineral phase identification and quantification data.
One row per sample with columns for each mineral phase identified.

Follows the wide-format pattern with individual weight percent columns.
Individual QC flags for each mineral using processeddataflag enum.

Relationship to core tables:
  - id: FK -> processedData.id (1:1 linkage)
  - processedData.type = 'XRDPhaseProduct'
  - processedData.workflow_id -> workflowExecutionActivity if Rietveld refinement
    is computational; NULL if manual/semi-quantitative
  - processedData.summary_metrics = {"quartz_percent":42, "albite_percent":18, ...}
  - processedData.s3_key = diffractogram .xy, .xrdml, or .raw file in MinIO

Standard soil mineral panel (10 major phases):
  Primary minerals: quartz, albite, microcline
  Phyllosilicates: muscovite, kaolinite, chlorite
  Amphiboles: hornblende
  Sulfides and evaporites: pyrite, halite, gypsum

Quantification methods:
  - Rietveld refinement (computational, most accurate)
  - Reference intensity ratio (RIR) method
  - Semi-quantitative (manual, less precise)

Computational processing workflow (if applicable):
  XRDAnalysisActivity acquires raw diffractogram ->
  workflowExecutionActivity (type='xrd_rietveld_refinement') processes with
  HighScore Plus, GSAS-II, or FullProf ->
  XRDPhaseProduct (workflow_id points to refinement WEA)
  
  workflow_steps JSONB example:
    {"software": "HighScore_Plus", "version": "5.1", "method": "Rietveld",
     "r_factor": 0.042, "gof": 1.8, "amorphous_content_pct": 12}

Required enum additions to enums.yaml:
  product:
    XRDPhaseProduct:  # Add to product permissible_values
    """
    __tablename__ = 'XRDPhaseProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    quartz_percent = Column(Float())
    albite_percent = Column(Float())
    microcline_percent = Column(Float())
    muscovite_percent = Column(Float())
    kaolinite_percent = Column(Float())
    chlorite_percent = Column(Float())
    hornblende_percent = Column(Float())
    pyrite_percent = Column(Float())
    halite_percent = Column(Float())
    gypsum_percent = Column(Float())
    flag_quartz = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_albite = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_microcline = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_muscovite = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_kaolinite = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_chlorite = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_hornblende = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_pyrite = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_halite = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_gypsum = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"XRDPhaseProduct(measure_type={self.measure_type},quartz_percent={self.quartz_percent},albite_percent={self.albite_percent},microcline_percent={self.microcline_percent},muscovite_percent={self.muscovite_percent},kaolinite_percent={self.kaolinite_percent},chlorite_percent={self.chlorite_percent},hornblende_percent={self.hornblende_percent},pyrite_percent={self.pyrite_percent},halite_percent={self.halite_percent},gypsum_percent={self.gypsum_percent},flag_quartz={self.flag_quartz},flag_albite={self.flag_albite},flag_microcline={self.flag_microcline},flag_muscovite={self.flag_muscovite},flag_kaolinite={self.flag_kaolinite},flag_chlorite={self.flag_chlorite},flag_hornblende={self.flag_hornblende},flag_pyrite={self.flag_pyrite},flag_halite={self.flag_halite},flag_gypsum={self.flag_gypsum},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},sample_id={self.sample_id},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Metagenomics_AnnotationProduct(MetagenomicsProduct):
    """
    Top-level archive for functional annotation outputs (zip/tar stored in MinIO).
Inherits all MetagenomicsProduct and dataProduct slots.
    """
    __tablename__ = 'Metagenomics_AnnotationProduct'

    annotation_database = Column(Enum('PFAM', 'COG', 'KEGG', name='annotationdatabasetype'))
    workflow_step = Column(Enum('ReadQcAnalysis', 'MetagenomeAssembly', 'ReadBasedTaxonomyAnalysis', 'MetagenomeAnnotation', 'MagsAnalysis', 'FunctionalAnnotation', 'GenePhylogeny', name='metagenomicssteps'))
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    provider_name = Column(UUID(), ForeignKey('controlledTermValue.id'))
    raw_fasta_url = Column(Text())
    additional_information = Column(Text())
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"Metagenomics_AnnotationProduct(annotation_database={self.annotation_database},workflow_step={self.workflow_step},sample_id={self.sample_id},provider_name={self.provider_name},raw_fasta_url={self.raw_fasta_url},additional_information={self.additional_information},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Metagenomics_BinningProduct(MetagenomicsProduct):
    """
    Top-level archive (zip/tar) for binning results stored in MinIO.
Inherits all MetagenomicsProduct and dataProduct slots.
    """
    __tablename__ = 'Metagenomics_BinningProduct'

    workflow_step = Column(Enum('ReadQcAnalysis', 'MetagenomeAssembly', 'ReadBasedTaxonomyAnalysis', 'MetagenomeAnnotation', 'MagsAnalysis', 'FunctionalAnnotation', 'GenePhylogeny', name='metagenomicssteps'))
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    provider_name = Column(UUID(), ForeignKey('controlledTermValue.id'))
    raw_fasta_url = Column(Text())
    additional_information = Column(Text())
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"Metagenomics_BinningProduct(workflow_step={self.workflow_step},sample_id={self.sample_id},provider_name={self.provider_name},raw_fasta_url={self.raw_fasta_url},additional_information={self.additional_information},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Metagenomics_GenePhylogenyProduct(MetagenomicsProduct):
    """
    Top-level archive for gene-based phylogeny outputs (zip/tar stored in MinIO).
Inherits all MetagenomicsProduct and dataProduct slots.
    """
    __tablename__ = 'Metagenomics_GenePhylogenyProduct'

    gene_family = Column(Text())
    workflow_step = Column(Enum('ReadQcAnalysis', 'MetagenomeAssembly', 'ReadBasedTaxonomyAnalysis', 'MetagenomeAnnotation', 'MagsAnalysis', 'FunctionalAnnotation', 'GenePhylogeny', name='metagenomicssteps'))
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    provider_name = Column(UUID(), ForeignKey('controlledTermValue.id'))
    raw_fasta_url = Column(Text())
    additional_information = Column(Text())
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"Metagenomics_GenePhylogenyProduct(gene_family={self.gene_family},workflow_step={self.workflow_step},sample_id={self.sample_id},provider_name={self.provider_name},raw_fasta_url={self.raw_fasta_url},additional_information={self.additional_information},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MSImageProduct(MassSpectrometryDataProduct):
    """
    one or more image(s) output from a mass spec data processing workflow (eg. LESA, CoreMS QC plots). Should be a zip file containing all similar image outputs from one data processing workflow.
    """
    __tablename__ = 'MSImageProduct'

    results_from_ms_processing = Column(UUID(), ForeignKey('MassSpectrometryWorkflowExecutionActivity.id'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"MSImageProduct(results_from_ms_processing={self.results_from_ms_processing},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},sample_id={self.sample_id},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MolecularIdentificationProduct(MassSpectrometryDataProduct):
    """
    a file containing molecular formula identifications that was output from a mass spec data processing workflow (eg. .csv of m/z and molecular formulae, .hdf5 file).
    """
    __tablename__ = 'MolecularIdentificationProduct'

    results_from_ms_processing = Column(UUID(), ForeignKey('MassSpectrometryWorkflowExecutionActivity.id'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"MolecularIdentificationProduct(results_from_ms_processing={self.results_from_ms_processing},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},sample_id={self.sample_id},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MetaproteomicsProduct(MassSpectrometryDataProduct):
    """
    Abstract parent class for processed metaproteomics data. Details and subclasses TBD.
    """
    __tablename__ = 'MetaproteomicsProduct'

    results_from_ms_processing = Column(UUID(), ForeignKey('MassSpectrometryWorkflowExecutionActivity.id'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    version = Column(Text(), nullable=False )
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    proposal_id = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"MetaproteomicsProduct(results_from_ms_processing={self.results_from_ms_processing},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},version={self.version},sample_id={self.sample_id},name={self.name},description={self.description},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


