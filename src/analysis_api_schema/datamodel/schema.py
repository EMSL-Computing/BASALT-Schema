
from sqlalchemy import Column, Index, Table, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()
metadata = Base.metadata


class Activity(Base):
    """
    Something that happens over time and can use equipment.
    """
    __tablename__ = 'Activity'

    name = Column(Text(), nullable=False )
    description = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    ended_at_time = Column(DateTime())
    processing_institution = Column(Enum('nmdc', 'ucsd', 'jgi', 'emsl', 'battelle', 'anl', 'ucd_genome_center', 'azenta', name='InstitutionEnum'))
    protocol_link = Column(Text())
    started_at_time = Column(DateTime())
    

    

    def __repr__(self):
        return f"Activity(name={self.name},description={self.description},id={self.id},ended_at_time={self.ended_at_time},processing_institution={self.processing_institution},protocol_link={self.protocol_link},started_at_time={self.started_at_time},)"



    


class Entity(Base):
    """
    Base identifiable thing.
    """
    __tablename__ = 'Entity'

    name = Column(Text(), nullable=False )
    description = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"Entity(name={self.name},description={self.description},id={self.id},)"



    


class DataProduct(Base):
    """
    Abstract base class for raw or processed data accessible in S3 storage.
Carries S3-pointer and sample-linkage slots shared across product types.
processedData and future sitePhoto extend this via is_a.
No direct database table, subclasses map to tables.
    """
    __tablename__ = 'DataProduct'

    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"DataProduct(name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    


class DataGenerationActivity(Base):
    """
    Abstract base for any data generation activity (physical to digital). Input data should 
be specified on workflow subclasses.
    """
    __tablename__ = 'DataGenerationActivity'

    sequence_order = Column(Integer())
    name = Column(Text(), nullable=False )
    description = Column(Text())
    protocol_url = Column(Text())
    protocol_version = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analyte_id = Column(UUID(), ForeignKey('ProcessedSample.id'))
    acquisition_start_time = Column(DateTime(), nullable=False )
    acquisition_end_time = Column(DateTime(), nullable=False )
    instrument_used = Column(UUID(), ForeignKey('Instrument.id'))
    instrument_operator_id = Column(UUID(), ForeignKey('PersonValue.id'))
    

    

    def __repr__(self):
        return f"DataGenerationActivity(sequence_order={self.sequence_order},name={self.name},description={self.description},protocol_url={self.protocol_url},protocol_version={self.protocol_version},id={self.id},analyte_id={self.analyte_id},acquisition_start_time={self.acquisition_start_time},acquisition_end_time={self.acquisition_end_time},instrument_used={self.instrument_used},instrument_operator_id={self.instrument_operator_id},)"



    


class DataProcessingActivity(Base):
    """
    Abstract base for any data processing activity (digital to digital). Input data should 
be specified on workflow subclasses.
    """
    __tablename__ = 'DataProcessingActivity'

    parent_workflow_id = Column(UUID(), ForeignKey('DataProcessingActivity.id'))
    workflow_steps = Column(Text())
    description = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    started_at_time = Column(DateTime(), nullable=False )
    ended_at_time = Column(DateTime())
    software_url = Column(Text())
    software_version = Column(Text())
    software_poc = Column(Text())
    execution_resource = Column(Enum('nersc_cori', 'nersc_perlmutter', 'emsl_rzr', 'emsl_tahoma', name='ExecutionResourceEnum'))
    

    

    def __repr__(self):
        return f"DataProcessingActivity(parent_workflow_id={self.parent_workflow_id},workflow_steps={self.workflow_steps},description={self.description},id={self.id},started_at_time={self.started_at_time},ended_at_time={self.ended_at_time},software_url={self.software_url},software_version={self.software_version},software_poc={self.software_poc},execution_resource={self.execution_resource},)"



    


class AlternativeIdentifier(Base):
    """
    
    """
    __tablename__ = 'AlternativeIdentifier'

    id = Column(UUID(), primary_key=True, nullable=False )
    alternate_id = Column(Text(), nullable=False )
    alternate_identifier_type = Column(Enum('instrument_alt_id', name='AlternateIdentifierType'), nullable=False )
    

    

    def __repr__(self):
        return f"AlternativeIdentifier(id={self.id},alternate_id={self.alternate_id},alternate_identifier_type={self.alternate_identifier_type},)"



    


class FunctionalAnnotationIdentifier(Base):
    """
    
    """
    __tablename__ = 'FunctionalAnnotationIdentifier'

    id = Column(UUID(), primary_key=True, nullable=False )
    functional_identifier = Column(Text(), nullable=False )
    database = Column(Enum('PFAM', 'COG', 'KEGG', name='AnnotationDatabaseEnum'), nullable=False )
    

    

    def __repr__(self):
        return f"FunctionalAnnotationIdentifier(id={self.id},functional_identifier={self.functional_identifier},database={self.database},)"



    


class Instrument(Base):
    """
    A material entity that is designed to perform a function in a scientific 
investigation, but is not a reagent. This class models a specific
instance of an instrument IF identifying information is filled out, 
otherwise, it is a generic standin for an instrument model.
    """
    __tablename__ = 'Instrument'

    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    vendor = Column(Enum('waters', 'agilent', 'bruker', 'thermo_fisher', 'perkin_elmer', 'scientific_industries', 'illumina', 'nikon', 'fia_lab', 'shimadzu', 'regen_ag_lab', 'kuo', 'rigaku', 'panalytical', name='VendorEnum'))
    model = Column(Enum('exploris_21T', 'exploris_240', 'exploris_480', 'ltq_orbitrap_velos', 'orbitrap_fusion_lumos', 'orbitrap_eclipse_tribid', 'orbitrap_q_exactive', 'orbitrap_iqx_tribrid', 'orbitrap_exploris_120', 'solarix_7T', 'solarix_12T', 'solarix_15T', 'agilent_8890A', 'agilent_7980A', 'vortex_genie_2', 'novaseq', 'novaseq_6000', 'novaseq_x', 'hiseq', 'hiseq_1000', 'hiseq_1500', 'hiseq_2000', 'hiseq_2500', 'hiseq_3000', 'hiseq_4000', 'hiseq_x_ten', 'miniseq', 'miseq', 'nextseq_1000', 'nextseq', 'nextseq_500', 'nextseq_550', 'gridion', 'minion', 'promethion', 'rs_II', 'sequel', 'sequel_II', 'revio', 'scimax', 'ed_400_with_rs_422', 'mettler_toledo_30029066', 'mettler_toledo_30266628', 'ums_hyprop2_020210', 'fialyzer_1000', 'fialyzer_1001', 'fialyzer_1002', 'orbitrap_q_exactive_plus', 'toc_5000A', 'toc_lcsh', 'sr_1', 'xth320', name='ModelEnum'))
    serial_number = Column(Text())
    lims_resource_id = Column(Integer())
    location = Column(Text())
    maintenance = Column(Text())
    alternative_names = Column(Text())
    instrument_parameters = Column(Text())
    mass_analyzer_type = Column(Enum('quadrupole', 'time_of_flight', 'orbitrap', 'ion_trap', 'ion_cyclotron_resonance', 'fourier_transform_ion_cyclotron_resonance', name='MassAnalyzerEnum'))
    other_properties = Column(Text())
    

    

    def __repr__(self):
        return f"Instrument(id={self.id},name={self.name},vendor={self.vendor},model={self.model},serial_number={self.serial_number},lims_resource_id={self.lims_resource_id},location={self.location},maintenance={self.maintenance},alternative_names={self.alternative_names},instrument_parameters={self.instrument_parameters},mass_analyzer_type={self.mass_analyzer_type},other_properties={self.other_properties},)"



    


class OntologyClass(Base):
    """
    
    """
    __tablename__ = 'OntologyClass'

    id = Column(UUID(), primary_key=True, nullable=False )
    description = Column(Text())
    alternative_identifiers = Column(Text())
    name = Column(Text())
    

    

    def __repr__(self):
        return f"OntologyClass(id={self.id},description={self.description},alternative_identifiers={self.alternative_identifiers},name={self.name},)"



    


class ContainerType(Base):
    """
    
    """
    __tablename__ = 'ContainerType'

    id = Column(UUID(), primary_key=True, nullable=False )
    description = Column(Text())
    container_type = Column(Enum('screw_top_conical', name='ContainerTypeEnum'))
    container_size_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    label_format = Column(Text())
    renderer = Column(Text())
    slot_capacity = Column(Text())
    
    
    # ManyToMany
    axes = relationship( "ContainerAxis", secondary="ContainerType_axes")
    
    
    contains_rel = relationship( "ContainerType_contains" )
    contains = association_proxy("contains_rel", "contains",
                                  creator=lambda x_: ContainerType_contains(contains=x_))
    

    

    def __repr__(self):
        return f"ContainerType(id={self.id},description={self.description},container_type={self.container_type},container_size_id={self.container_size_id},label_format={self.label_format},renderer={self.renderer},slot_capacity={self.slot_capacity},)"



    


class ContainerAxis(Base):
    """
    
    """
    __tablename__ = 'ContainerAxis'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    name = Column(Text())
    
    
    values_rel = relationship( "ContainerAxis_values" )
    values = association_proxy("values_rel", "values",
                                  creator=lambda x_: ContainerAxis_values(values=x_))
    

    

    def __repr__(self):
        return f"ContainerAxis(id={self.id},name={self.name},)"



    


class Custodian(Base):
    """
    
    """
    __tablename__ = 'Custodian'

    id = Column(UUID(), primary_key=True, nullable=False )
    person_id = Column(UUID(), ForeignKey('PersonValue.id'))
    

    

    def __repr__(self):
        return f"Custodian(id={self.id},person_id={self.person_id},)"



    


class InstrumentAlternativeIdentifier(Base):
    """
    
    """
    __tablename__ = 'InstrumentAlternativeIdentifier'

    id = Column(UUID(), primary_key=True, nullable=False )
    alt_id = Column(UUID(), ForeignKey('AlternativeIdentifier.id'))
    instrument_alt_id_provider = Column(Enum('nexus', 'dms', name='InstrumentAltIdProviderEnum'))
    instrument_id = Column(UUID(), ForeignKey('Instrument.id'), nullable=False )
    

    

    def __repr__(self):
        return f"InstrumentAlternativeIdentifier(id={self.id},alt_id={self.alt_id},instrument_alt_id_provider={self.instrument_alt_id_provider},instrument_id={self.instrument_id},)"



    


class LabDevice(Base):
    """
    A lab device is a physical instrument or equipment used in a laboratory setting for conducting experiments, measurements, or analyses. It can include various types of instruments such as microscopes, spectrometers, centrifuges, and other specialized equipment. Lab devices are essential for performing scientific research and obtaining accurate data.
    """
    __tablename__ = 'LabDevice'

    id = Column(UUID(), primary_key=True, nullable=False )
    description = Column(Text())
    device_type = Column(Enum('orbital_shaker', 'thermomixer', name='DeviceTypeEnum'))
    activity_time_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    activity_speed_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    

    

    def __repr__(self):
        return f"LabDevice(id={self.id},description={self.description},device_type={self.device_type},activity_time_id={self.activity_time_id},activity_speed_id={self.activity_speed_id},)"



    


class SampleProcessing(Base):
    """
    Abstract base for any sample processing activity (physical to physical). Input data should 
be specified on workflow subclasses.
    """
    __tablename__ = 'SampleProcessing'

    protocol_url = Column(Text())
    protocol_version = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analysis_type = Column(Enum('analysis_activity', 'lcms_metabolomics_method', 'fticr_acquisition_method', 'gravimetric_water_content_method', 'ph_method', 'hydraulic_properties_method', 'microbial_biomass_method', 'xray_computed_tomography_method', 'REGEN', 'KUO', 'respiration_method', 'texture_method', 'enzyme_activity_method', 'elemental_analysis_method', 'toc_tn_method', 'bulk_density_method', 'metagenomics_method', 'xrf_analysis', 'xrd_analysis', name='RouteMethodEnum'))
    method_name = Column(Enum('MAOM', 'WOEM', name='MethodNameEnum'))
    processing_steps = Column(Text(), nullable=False )
    uses_sample = Column(UUID(), ForeignKey('Sample.id'))
    

    

    def __repr__(self):
        return f"SampleProcessing(protocol_url={self.protocol_url},protocol_version={self.protocol_version},id={self.id},analysis_type={self.analysis_type},method_name={self.method_name},processing_steps={self.processing_steps},uses_sample={self.uses_sample},)"



    


class ProcessingSampleLink(Base):
    """
    A link between a processed sample and the sample processing activity that produced it.
This class captures the relationship between a processed sample and the sample processing
activity that generated it, including the step number and role of the sample in the process.
    """
    __tablename__ = 'ProcessingSampleLink'

    id = Column(UUID(), primary_key=True, nullable=False )
    sample_base_id = Column(UUID(), ForeignKey('Sample.id'), nullable=False )
    processing_id = Column(UUID(), ForeignKey('SampleProcessing.id'), nullable=False )
    step_number = Column(Integer(), nullable=False )
    role = Column(Enum('input_sample', 'output_sample', name='SampleRole'), nullable=False )
    

    
    # Unique constraints
    __table_args__ = (
        UniqueConstraint('sample_base_id', 'processing_id', 'step_number', 'role'),
    )
    

    def __repr__(self):
        return f"ProcessingSampleLink(id={self.id},sample_base_id={self.sample_base_id},processing_id={self.processing_id},step_number={self.step_number},role={self.role},)"



    


class InstrumentCustodian(Base):
    """
    A link between an instrument and a custodian (person) responsible for it.
This class captures the relationship between an instrument and the person
who is responsible for its maintenance, calibration, and proper use.
    """
    __tablename__ = 'InstrumentCustodian'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    instrument_id = Column(UUID(), ForeignKey('Instrument.id'), nullable=False )
    custodian_id = Column(UUID(), ForeignKey('Custodian.id'), nullable=False )
    

    

    def __repr__(self):
        return f"InstrumentCustodian(id={self.id},instrument_id={self.instrument_id},custodian_id={self.custodian_id},)"



    


class WorkflowExecutionFunctionalAnnotation(Base):
    """
    A link between a workflow execution and a functional annotation identifier.
This class captures the relationship between a workflow execution and the
functional annotation identifier that was used in the analysis.
    """
    __tablename__ = 'WorkflowExecutionFunctionalAnnotation'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    workflow_id = Column(UUID(), ForeignKey('DataProcessingActivity.id'), nullable=False )
    functional_annotation_id = Column(UUID(), ForeignKey('FunctionalAnnotationIdentifier.id'), nullable=False )
    count = Column(Float())
    

    

    def __repr__(self):
        return f"WorkflowExecutionFunctionalAnnotation(id={self.id},workflow_id={self.workflow_id},functional_annotation_id={self.functional_annotation_id},count={self.count},)"



    


class Changelog(Base):
    """
    
    """
    __tablename__ = 'Changelog'

    version = Column(Text(), primary_key=True, nullable=False )
    changelog = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"Changelog(version={self.version},changelog={self.changelog},)"



    


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



    


class MobilePhaseSegment(Base):
    """
    A segment of the mobile phase used in chromatography during mass spectrometry.
    """
    __tablename__ = 'MobilePhaseSegment'

    name = Column(Text(), nullable=False )
    duration_min = Column(Float())
    id = Column(UUID(), primary_key=True, nullable=False )
    segment_order = Column(Integer())
    substance = Column(Text())
    

    

    def __repr__(self):
        return f"MobilePhaseSegment(name={self.name},duration_min={self.duration_min},id={self.id},segment_order={self.segment_order},substance={self.substance},)"



    


class MassSpectrometryStandardRun(Base):
    """
    A record of a mass spectrometry standard run with a batch of samples, which is used for calibration and quality control.
    """
    __tablename__ = 'MassSpectrometryStandardRun'

    name = Column(Text(), nullable=False )
    description = Column(Text())
    internal_calibration = Column(Boolean())
    calibration_target = Column(Enum('mass_charge_ratio', 'retention_time', 'retention_index', name='CalibrationTargetEnum'))
    calibration_standard = Column(UUID(), ForeignKey('PurchasedMaterial.id'))
    calibration_data = Column(UUID(), ForeignKey('MassSpectrometryInstrumentData.id'))
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"MassSpectrometryStandardRun(name={self.name},description={self.description},internal_calibration={self.internal_calibration},calibration_target={self.calibration_target},calibration_standard={self.calibration_standard},calibration_data={self.calibration_data},id={self.id},)"



    


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
    oxygen_status = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'obligate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    

    

    def __repr__(self):
        return f"HasIncubationConditions(id={self.id},temperature_celsius={self.temperature_celsius},agitation_speed_rpm={self.agitation_speed_rpm},oxygen_status={self.oxygen_status},)"



    


class PurchasedMaterial(Base):
    """
    [NEW ABSTRACT CLASS] Lightweight base for non-sample physical lab materials
that are not instruments.  Currently Strain is the only concrete subtype.
Activities reference Strain via the strain_ref FK slot.
    """
    __tablename__ = 'PurchasedMaterial'

    purchased_material_type = Column(Text(), nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"PurchasedMaterial(purchased_material_type={self.purchased_material_type},name={self.name},description={self.description},id={self.id},)"



    


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
    __tablename__ = 'LabProcessingActivity'

    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text())
    description = Column(Text())
    

    

    def __repr__(self):
        return f"LabProcessingActivity(id={self.id},name={self.name},description={self.description},)"



    


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
NOT a standalone database table; embedded structured entries under
PlateSetupActivity.well_metadata.
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
    Per-well measurement data. NOT a standalone database table; embedded structured entries under
PlateProduct.well_readings.
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
    Mineral-Associated Organic Matter (MAOM) analysis product, typically derived via HCl extraction and TOC/TN measurement.
One row per sample with columns for total organic carbon and total nitrogen.
Individual QC flags for each measurement using ProcessedDataFlag enum. TO BE RENAMED TO HClExtOMProduct
    """
    __tablename__ = 'MAOMProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='ProductMeasureType'))
    replicate = Column(Integer())
    id = Column(UUID(), ForeignKey('ProcessedData.id'), primary_key=True, nullable=False )
    total_organic_carbon_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    total_organic_carbon_avg = Column(Float())
    total_nitrogen_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    total_nitrogen_avg = Column(Float())
    flag_toc = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_tn = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_toc_avg = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_tn_avg = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    

    

    def __repr__(self):
        return f"MAOMProduct(measure_type={self.measure_type},replicate={self.replicate},id={self.id},total_organic_carbon_id={self.total_organic_carbon_id},total_organic_carbon_avg={self.total_organic_carbon_avg},total_nitrogen_id={self.total_nitrogen_id},total_nitrogen_avg={self.total_nitrogen_avg},flag_toc={self.flag_toc},flag_tn={self.flag_tn},flag_toc_avg={self.flag_toc_avg},flag_tn_avg={self.flag_tn_avg},)"



    


class WEOMProduct(Base):
    """
    Water Extractable Organic Matter (WEOM) analysis product, typically derived via Shimadzu TOC-L or similar instrument.
One row per sample with columns for total organic carbon and total nitrogen.
Individual QC flags for each measurement using ProcessedDataFlag enum.
    """
    __tablename__ = 'WEOMProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='ProductMeasureType'))
    replicate = Column(Integer())
    id = Column(UUID(), ForeignKey('ProcessedData.id'), primary_key=True, nullable=False )
    total_organic_carbon_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    total_organic_carbon_avg = Column(Float())
    total_nitrogen_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    total_nitrogen_avg = Column(Float())
    flag_toc = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_tn = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_toc_avg = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_tn_avg = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    

    

    def __repr__(self):
        return f"WEOMProduct(measure_type={self.measure_type},replicate={self.replicate},id={self.id},total_organic_carbon_id={self.total_organic_carbon_id},total_organic_carbon_avg={self.total_organic_carbon_avg},total_nitrogen_id={self.total_nitrogen_id},total_nitrogen_avg={self.total_nitrogen_avg},flag_toc={self.flag_toc},flag_tn={self.flag_tn},flag_toc_avg={self.flag_toc_avg},flag_tn_avg={self.flag_tn_avg},)"



    


class Site(Base):
    """
    Site-level metadata for a specific location from which a set of samples are collected.
    """
    __tablename__ = 'Site'

    name = Column(Text(), nullable=False )
    description = Column(Text())
    alt = Column(Text())
    annual_precpt = Column(Text())
    annual_temp = Column(Text())
    atmospheric_data = Column(Text())
    crop_rotation = Column(Text())
    cur_land_use = Column(Enum('badlands', 'cities', 'conifers', 'crop_trees', 'farmstead', 'gravel', 'hardwoods', 'hayland', 'horticultural_plants', 'industrial_areas', 'intermixed', 'marshlands', 'meadows', 'mines_quarries', 'mudflats', 'oil_waste', 'pastureland', 'permanent_snow_or_ice', 'rainforest', 'rangeland', 'roads_railroads', 'rock', 'row_crops', 'saline_seeps', 'salt_flats', 'sand', 'shrub_crops', 'shrub_land', 'small_grains', 'successional_shrub_land', 'swamp', 'tropical', 'tundra', 'vegetable_crops', 'vine_crops', name='LandUseEnum'))
    cur_vegetation = Column(Text())
    cur_vegetation_meth = Column(Text())
    drainage_class = Column(Enum('excessively_drained', 'moderately_well', 'poorly', 'somewhat_poorly', 'very_poorly', 'well', name='DrainageClassEnum'))
    elev = Column(Text(), nullable=False )
    extreme_event = Column(Text())
    fao_class = Column(Enum('Acrisols', 'Alisols', 'Andosols', 'Anthrosols', 'Arenosols', 'Calcisols', 'Cambisols', 'Chernozems', 'Cryosols', 'Durisols', 'Ferrasols', 'Fluvisols', 'Gleysols', 'Gypsisols', 'Histosols', 'Kastanozems', 'Leptosols', 'Lixisols', 'Luvisols', 'Nitosols', 'Phaeozems', 'Planosols', 'Plinthosols', 'Podzols', 'Solonchaks', 'Solonetz', 'Stagnosols', 'Technosols', 'Umbrisols', 'Vertisols', name='FAOClassEnum'))
    fire = Column(Text())
    flooding = Column(Text())
    geo_loc_name = Column(Text(), nullable=False )
    growth_facil = Column(Enum('field', 'commercially_purchased', 'experimental_garden', 'field_incubation', 'greenhouse', 'growth_chamber', 'lab_incubation', 'open_top_chamber', 'other', name='GrowthFacilityEnum'), nullable=False )
    latitude = Column(Float(), nullable=False )
    link_climate_info = Column(Text())
    link_class_info = Column(Text())
    local_class = Column(Text())
    local_class_meth = Column(Text())
    longitude = Column(Float(), nullable=False )
    neon_site_code = Column(Text())
    neon_plot_id = Column(Text())
    other_growth_facil = Column(Text())
    previous_land_use = Column(Text())
    previous_land_use_meth = Column(Text())
    profile_position = Column(Enum('backslope', 'footslope', 'shoulder', 'summit', 'toeslope', name='ProfilePositionEnum'))
    season_precpt = Column(Text())
    season_temp = Column(Text())
    slope_aspect = Column(Text())
    slope_gradient = Column(Text())
    tillage = Column(Enum('chisel', 'cutting_disc', 'disc_plough', 'drill', 'mouldboard', 'ridge_till', 'strip_tillage', 'tined', 'zonal_tillage', name='TillageEnum'))
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"Site(name={self.name},description={self.description},alt={self.alt},annual_precpt={self.annual_precpt},annual_temp={self.annual_temp},atmospheric_data={self.atmospheric_data},crop_rotation={self.crop_rotation},cur_land_use={self.cur_land_use},cur_vegetation={self.cur_vegetation},cur_vegetation_meth={self.cur_vegetation_meth},drainage_class={self.drainage_class},elev={self.elev},extreme_event={self.extreme_event},fao_class={self.fao_class},fire={self.fire},flooding={self.flooding},geo_loc_name={self.geo_loc_name},growth_facil={self.growth_facil},latitude={self.latitude},link_climate_info={self.link_climate_info},link_class_info={self.link_class_info},local_class={self.local_class},local_class_meth={self.local_class_meth},longitude={self.longitude},neon_site_code={self.neon_site_code},neon_plot_id={self.neon_plot_id},other_growth_facil={self.other_growth_facil},previous_land_use={self.previous_land_use},previous_land_use_meth={self.previous_land_use_meth},profile_position={self.profile_position},season_precpt={self.season_precpt},season_temp={self.season_temp},slope_aspect={self.slope_aspect},slope_gradient={self.slope_gradient},tillage={self.tillage},id={self.id},)"



    


class Sample(Base):
    """
    A physical sample collected from an environment. The environment can be ecological, laboratory, or any other context where samples are collected. This class serves as an abstract class to relate subclasses of samples.
    """
    __tablename__ = 'Sample'

    name = Column(Text(), nullable=False )
    description = Column(Text())
    emsl_activity = Column(Text())
    lims_barcode = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"Sample(name={self.name},description={self.description},emsl_activity={self.emsl_activity},lims_barcode={self.lims_barcode},id={self.id},)"



    


class SamplingActivity(Base):
    """
    An activity that involves the collection of a sample. This class serves as an abstract class to relate subclasses of sampling activities. Samples reference their parent sampling activity via the 'sampled_during' slot.
    """
    __tablename__ = 'SamplingActivity'

    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    emsl_activity = Column(Text())
    collection_date = Column(Date())
    shipped_sample_size = Column(Text())
    sampled_at_site = Column(UUID(), ForeignKey('Site.id'))
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"SamplingActivity(name={self.name},description={self.description},project={self.project},emsl_activity={self.emsl_activity},collection_date={self.collection_date},shipped_sample_size={self.shipped_sample_size},sampled_at_site={self.sampled_at_site},id={self.id},)"



    


class Biological_entity(Base):
    """
    Reference data representing a biological identity (strain, isolate,
engineered construct, etc.) that can be instantiated by multiple
physical samples.

REPLACES: This class replaces the former Strain class, which was modeled
as a PurchasedMaterial subclass. That approach did not accommodate strains
engineered in-house or received from collaborators, nor did it cleanly
separate biological identity from physical samples. Additionally, the term
"strain" implies purity that cannot always be guaranteed; this class
represents the *intended* or *characterized* biological identity.

Relationship to samples:
  - One biological_entity can have many AMP2UserSample instances
  - AMP2UserSample.biological_entity_ref points here
  - CultureGrowth activities reference via biological_entity_ref (aliased as strain_ref)
    """
    __tablename__ = 'biological_entity'

    name = Column(Text(), nullable=False )
    description = Column(Text())
    strain_identifier = Column(Text(), nullable=False )
    organism_name = Column(Text())
    taxonomy_id = Column(Text())
    host_common_name = Column(Text())
    host_taxid = Column(Text())
    strain_source = Column(Text())
    strain_type = Column(Enum('bacterial', 'fungal', 'archaeal', 'viral', 'algal', 'protist', 'other', name='StrainTypeEnum'))
    modification_method = Column(Enum('electroporation', 'conjugation', 'transformation', 'transduction', 'crispr', 'homologous_recombination', 'transposon', 'other', 'p_element', 'phage_transformation', 'piggybac', 'polyethylene_glycol_mediated', 'replicon', 'whisker_mediated_transformation', name='ModificationMethodEnum'))
    strain_description = Column(Text())
    strain_mutation = Column(Text())
    phenotype = Column(Text())
    trait = Column(Enum('other', 'product_quality', 'agronomic_properties', 'bacterial_resistance', 'herbicide_resistance', 'insect_resistance', 'marker_gene', 'nematode_resistance', 'virus_resistance', name='IntendedTraitEnum'))
    encoded_traits = Column(Text())
    genotype_segment_category = Column(Enum('Empty Transformation Vector', 'Gene Knock-Out', 'Gene Silencer', 'Gene(s) of Interest', 'RNA Interface (RNAi)', 'Screenable Marker', 'Selectable Marker', 'Virus Genome', 'Wild Type', 'Recombination Site', 'Other', name='GenotypeSegmentEnum'))
    genotype_segment_name = Column(Text())
    component_name = Column(Text())
    construct_component = Column(Enum('None', "3'UTR", "5'UTR", 'Enhancer', 'Epitope Tag', 'Exon', 'Flanking Element', 'Gene', 'Intron', 'Leader Sequence', 'Promoter', 'Recognition Sequence', 'Signal Sequence', 'Spacer', 'Targeting Sequence', 'Terminator', 'Transit Peptide', 'Vector Sequence', name='ConstructComponentEnum'))
    donor_organism = Column(Text())
    component_description = Column(Text())
    trophic_level = Column(Enum('autotroph', 'carboxydotroph', 'chemoautolithotroph', 'chemoautotroph', 'chemoheterotroph', 'chemolithoautotroph', 'chemolithotroph', 'chemoorganoheterotroph', 'chemoorganotroph', 'chemosynthetic', 'chemotroph', 'copiotroph', 'diazotroph', 'facultative', 'heterotroph', 'lithoautotroph', 'lithoheterotroph', 'lithotroph', 'methanotroph', 'methylotroph', 'mixotroph', 'obligate', 'oligotroph', 'organoheterotroph', 'organotroph', 'osmotroph', 'photoheterotroph', 'photoautotroph', 'photolithoautotroph', 'photolithotroph', 'phototroph', name='TrophicLevelEnum'))
    pathogenicity = Column(Text())
    host_spec_range = Column(Text())
    propagation = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"biological_entity(name={self.name},description={self.description},strain_identifier={self.strain_identifier},organism_name={self.organism_name},taxonomy_id={self.taxonomy_id},host_common_name={self.host_common_name},host_taxid={self.host_taxid},strain_source={self.strain_source},strain_type={self.strain_type},modification_method={self.modification_method},strain_description={self.strain_description},strain_mutation={self.strain_mutation},phenotype={self.phenotype},trait={self.trait},encoded_traits={self.encoded_traits},genotype_segment_category={self.genotype_segment_category},genotype_segment_name={self.genotype_segment_name},component_name={self.component_name},construct_component={self.construct_component},donor_organism={self.donor_organism},component_description={self.component_description},trophic_level={self.trophic_level},pathogenicity={self.pathogenicity},host_spec_range={self.host_spec_range},propagation={self.propagation},id={self.id},)"



    


class Study(Base):
    """
    A study or research project, typically associated with a proposal and a set of experiments.
A study may have multiple participants, each with different roles, and may be associated with
one or more campaigns. The study may also have associated DOIs and funding sources.
    """
    __tablename__ = 'Study'

    id = Column(UUID(), primary_key=True, nullable=False )
    project_id = Column(Integer(), nullable=False )
    title = Column(Text())
    name = Column(Text(), nullable=False )
    proposal_abstract = Column(Text())
    description = Column(Text())
    principal_investigator = Column(UUID(), ForeignKey('PersonValue.id'), nullable=False )
    collaborating_institution = Column(Text())
    project_status = Column(Enum('STARTED', 'COMPLETED', 'CLOSED', 'EXTENDED', 'ACCEPTED', 'WITHDRAWN', name='ProjectStatusEnum'))
    project_start = Column(DateTime())
    project_end = Column(DateTime())
    
    
    external_identifiers_rel = relationship( "Study_external_identifiers" )
    external_identifiers = association_proxy("external_identifiers_rel", "external_identifiers",
                                  creator=lambda x_: Study_external_identifiers(external_identifiers=x_))
    
    
    # ManyToMany
    has_participants = relationship( "ProjectParticipant", secondary="Study_has_participants")
    
    
    # ManyToMany
    associated_dois = relationship( "DOI", secondary="Study_associated_dois")
    
    
    # ManyToMany
    funding_sources = relationship( "DOI", secondary="Study_funding_sources")
    

    

    def __repr__(self):
        return f"Study(id={self.id},project_id={self.project_id},title={self.title},name={self.name},proposal_abstract={self.proposal_abstract},description={self.description},principal_investigator={self.principal_investigator},collaborating_institution={self.collaborating_institution},project_status={self.project_status},project_start={self.project_start},project_end={self.project_end},)"



    


class ProjectParticipant(Base):
    """
    A record of a person and their role on an EMSL project.
    """
    __tablename__ = 'ProjectParticipant'

    id = Column(UUID(), primary_key=True, nullable=False )
    role = Column(Enum('Principal Investigator', 'Co-Investigator', 'Team Member', 'Integrated Research Platform Lead', 'Administrative Coordinator', 'Project Manager', 'Metadata POC', 'Science Lead', 'Science POC', name='NexusRoleEnum'), nullable=False )
    person = Column(UUID(), ForeignKey('PersonValue.id'), nullable=False )
    

    

    def __repr__(self):
        return f"ProjectParticipant(id={self.id},role={self.role},person={self.person},)"



    


class DOI(Base):
    """
    A digital object identifier (DOI) representing a persistent link to a digital resource.
    """
    __tablename__ = 'DOI'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    doi_value = Column(Text(), nullable=False )
    doi_category = Column(Enum('award_doi', 'dataset_doi', 'publication_doi', 'data_management_plan_doi', name='DoiCategoryEnum'))
    doi_provider = Column(Enum('emsl', 'jgi', 'kbase', 'osti', 'ess_dive', 'massive', 'gsc', 'zenodo', 'edi', 'figshare', name='DoiProviderEnum'))
    

    

    def __repr__(self):
        return f"DOI(id={self.id},doi_value={self.doi_value},doi_category={self.doi_category},doi_provider={self.doi_provider},)"



    


class TimestampValue(Base):
    """
    A timestamp value with optional description. No pattern at present,
    """
    __tablename__ = 'TimestampValue'

    description = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    has_raw_value = Column(Text())
    

    

    def __repr__(self):
        return f"TimestampValue(description={self.description},id={self.id},has_raw_value={self.has_raw_value},)"



    


class TextValue(Base):
    """
    A text value with optional description and language.
    """
    __tablename__ = 'TextValue'

    description = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    language = Column(Text())
    has_raw_value = Column(Text())
    

    

    def __repr__(self):
        return f"TextValue(description={self.description},id={self.id},language={self.language},has_raw_value={self.has_raw_value},)"



    


class SoftwareControlledTermValue(Base):
    """
    
    """
    __tablename__ = 'SoftwareControlledTermValue'

    name = Column(Text(), nullable=False )
    description = Column(Text())
    version = Column(Text(), nullable=False )
    id = Column(Text(), primary_key=True, nullable=False )
    has_raw_value = Column(Text())
    

    

    def __repr__(self):
        return f"SoftwareControlledTermValue(name={self.name},description={self.description},version={self.version},id={self.id},has_raw_value={self.has_raw_value},)"



    


class ControlledTermValue(Base):
    """
    
    """
    __tablename__ = 'ControlledTermValue'

    description = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    has_raw_value = Column(Text())
    term = Column(Text())
    term_id = Column(Text())
    controlled_term_provider = Column(Text())
    

    

    def __repr__(self):
        return f"ControlledTermValue(description={self.description},id={self.id},has_raw_value={self.has_raw_value},term={self.term},term_id={self.term_id},controlled_term_provider={self.controlled_term_provider},)"



    


class PersonValue(Base):
    """
    
    """
    __tablename__ = 'PersonValue'

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
        return f"PersonValue(email={self.email},id={self.id},first_name={self.first_name},last_name={self.last_name},middle_initial={self.middle_initial},orcid={self.orcid},profile_image_url={self.profile_image_url},websites={self.websites},)"



    


class QuantityValue(Base):
    """
    A quantity value with numeric value and optional unit
    """
    __tablename__ = 'QuantityValue'

    description = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    has_value_unit = Column(Text())
    has_unit = Column(Text())
    has_numeric_value = Column(Float())
    has_minimum_numeric_value = Column(Float())
    has_maximum_numeric_value = Column(Float())
    has_raw_value = Column(Text())
    

    

    def __repr__(self):
        return f"QuantityValue(description={self.description},id={self.id},has_value_unit={self.has_value_unit},has_unit={self.has_unit},has_numeric_value={self.has_numeric_value},has_minimum_numeric_value={self.has_minimum_numeric_value},has_maximum_numeric_value={self.has_maximum_numeric_value},has_raw_value={self.has_raw_value},)"



    


class ConditioningValue(Base):
    """
    
    """
    __tablename__ = 'ConditioningValue'

    id = Column(Text(), primary_key=True, nullable=False )
    source_material = Column(Text())
    instrument = Column(Text())
    gas = Column(Text())
    pressure = Column(Text())
    has_raw_value = Column(Text())
    

    

    def __repr__(self):
        return f"ConditioningValue(id={self.id},source_material={self.source_material},instrument={self.instrument},gas={self.gas},pressure={self.pressure},has_raw_value={self.has_raw_value},)"



    


class ZipDownload(Base):
    """
    A zip download record, capturing the details of a zip file download event.
    """
    __tablename__ = 'zipDownload'

    id = Column(UUID(), primary_key=True, nullable=False )
    time = Column(DateTime(), nullable=False )
    user = Column(Text(), nullable=False )
    files = Column(Integer(), nullable=False )
    packages = Column(Text())
    

    

    def __repr__(self):
        return f"zipDownload(id={self.id},time={self.time},user={self.user},files={self.files},packages={self.packages},)"



    


class ContainerType_axes(Base):
    """
    
    """
    __tablename__ = 'ContainerType_axes'

    ContainerType_id = Column(UUID(), ForeignKey('ContainerType.id'), primary_key=True)
    axes_id = Column(Integer(), ForeignKey('ContainerAxis.id'), primary_key=True)
    

    

    def __repr__(self):
        return f"ContainerType_axes(ContainerType_id={self.ContainerType_id},axes_id={self.axes_id},)"



    


class ContainerType_contains(Base):
    """
    
    """
    __tablename__ = 'ContainerType_contains'

    ContainerType_id = Column(UUID(), ForeignKey('ContainerType.id'), primary_key=True)
    contains = Column(Text(), primary_key=True)
    

    

    def __repr__(self):
        return f"ContainerType_contains(ContainerType_id={self.ContainerType_id},contains={self.contains},)"



    


class ContainerAxis_values(Base):
    """
    
    """
    __tablename__ = 'ContainerAxis_values'

    ContainerAxis_id = Column(Integer(), ForeignKey('ContainerAxis.id'), primary_key=True)
    values = Column(Text(), primary_key=True)
    

    

    def __repr__(self):
        return f"ContainerAxis_values(ContainerAxis_id={self.ContainerAxis_id},values={self.values},)"



    


class ChromatographyConfiguration_mobile_phases(Base):
    """
    
    """
    __tablename__ = 'ChromatographyConfiguration_mobile_phases'

    ChromatographyConfiguration_uid = Column(Integer(), ForeignKey('ChromatographyConfiguration.uid'), primary_key=True)
    mobile_phases_id = Column(UUID(), ForeignKey('MobilePhaseSegment.id'), primary_key=True)
    

    

    def __repr__(self):
        return f"ChromatographyConfiguration_mobile_phases(ChromatographyConfiguration_uid={self.ChromatographyConfiguration_uid},mobile_phases_id={self.mobile_phases_id},)"



    


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



    


class NucleotideSequencing_external_identifiers(Base):
    """
    
    """
    __tablename__ = 'NucleotideSequencing_external_identifiers'

    NucleotideSequencing_id = Column(UUID(), ForeignKey('NucleotideSequencing.id'), primary_key=True)
    external_identifiers = Column(Text(), primary_key=True)
    

    

    def __repr__(self):
        return f"NucleotideSequencing_external_identifiers(NucleotideSequencing_id={self.NucleotideSequencing_id},external_identifiers={self.external_identifiers},)"



    


class AerosolArmSample_external_identifiers(Base):
    """
    
    """
    __tablename__ = 'AerosolArmSample_external_identifiers'

    AerosolArmSample_id = Column(UUID(), ForeignKey('AerosolArmSample.id'), primary_key=True)
    external_identifiers = Column(Text(), primary_key=True)
    

    

    def __repr__(self):
        return f"AerosolArmSample_external_identifiers(AerosolArmSample_id={self.AerosolArmSample_id},external_identifiers={self.external_identifiers},)"



    


class AerosolSample_external_identifiers(Base):
    """
    
    """
    __tablename__ = 'AerosolSample_external_identifiers'

    AerosolSample_id = Column(UUID(), ForeignKey('AerosolSample.id'), primary_key=True)
    external_identifiers = Column(Text(), primary_key=True)
    

    

    def __repr__(self):
        return f"AerosolSample_external_identifiers(AerosolSample_id={self.AerosolSample_id},external_identifiers={self.external_identifiers},)"



    


class CommerciallyPurchasedSample_external_identifiers(Base):
    """
    
    """
    __tablename__ = 'CommerciallyPurchasedSample_external_identifiers'

    CommerciallyPurchasedSample_id = Column(UUID(), ForeignKey('CommerciallyPurchasedSample.id'), primary_key=True)
    external_identifiers = Column(Text(), primary_key=True)
    

    

    def __repr__(self):
        return f"CommerciallyPurchasedSample_external_identifiers(CommerciallyPurchasedSample_id={self.CommerciallyPurchasedSample_id},external_identifiers={self.external_identifiers},)"



    


class CultureEnvironmentalSample_external_identifiers(Base):
    """
    
    """
    __tablename__ = 'CultureEnvironmentalSample_external_identifiers'

    CultureEnvironmentalSample_id = Column(UUID(), ForeignKey('CultureEnvironmentalSample.id'), primary_key=True)
    external_identifiers = Column(Text(), primary_key=True)
    

    

    def __repr__(self):
        return f"CultureEnvironmentalSample_external_identifiers(CultureEnvironmentalSample_id={self.CultureEnvironmentalSample_id},external_identifiers={self.external_identifiers},)"



    


class EngineeredStrainSample_external_identifiers(Base):
    """
    
    """
    __tablename__ = 'EngineeredStrainSample_external_identifiers'

    EngineeredStrainSample_id = Column(UUID(), ForeignKey('EngineeredStrainSample.id'), primary_key=True)
    external_identifiers = Column(Text(), primary_key=True)
    

    

    def __repr__(self):
        return f"EngineeredStrainSample_external_identifiers(EngineeredStrainSample_id={self.EngineeredStrainSample_id},external_identifiers={self.external_identifiers},)"



    


class FieldDeployedTerraformSample_external_identifiers(Base):
    """
    
    """
    __tablename__ = 'FieldDeployedTerraformSample_external_identifiers'

    FieldDeployedTerraformSample_id = Column(UUID(), ForeignKey('FieldDeployedTerraformSample.id'), primary_key=True)
    external_identifiers = Column(Text(), primary_key=True)
    

    

    def __repr__(self):
        return f"FieldDeployedTerraformSample_external_identifiers(FieldDeployedTerraformSample_id={self.FieldDeployedTerraformSample_id},external_identifiers={self.external_identifiers},)"



    


class MixedCultureSample_external_identifiers(Base):
    """
    
    """
    __tablename__ = 'MixedCultureSample_external_identifiers'

    MixedCultureSample_id = Column(UUID(), ForeignKey('MixedCultureSample.id'), primary_key=True)
    external_identifiers = Column(Text(), primary_key=True)
    

    

    def __repr__(self):
        return f"MixedCultureSample_external_identifiers(MixedCultureSample_id={self.MixedCultureSample_id},external_identifiers={self.external_identifiers},)"



    


class MonetSoilSample_external_identifiers(Base):
    """
    
    """
    __tablename__ = 'MonetSoilSample_external_identifiers'

    MonetSoilSample_id = Column(UUID(), ForeignKey('MonetSoilSample.id'), primary_key=True)
    external_identifiers = Column(Text(), primary_key=True)
    

    

    def __repr__(self):
        return f"MonetSoilSample_external_identifiers(MonetSoilSample_id={self.MonetSoilSample_id},external_identifiers={self.external_identifiers},)"



    


class OtherUndescribedSample_external_identifiers(Base):
    """
    
    """
    __tablename__ = 'OtherUndescribedSample_external_identifiers'

    OtherUndescribedSample_id = Column(UUID(), ForeignKey('OtherUndescribedSample.id'), primary_key=True)
    external_identifiers = Column(Text(), primary_key=True)
    

    

    def __repr__(self):
        return f"OtherUndescribedSample_external_identifiers(OtherUndescribedSample_id={self.OtherUndescribedSample_id},external_identifiers={self.external_identifiers},)"



    


class PlantSample_external_identifiers(Base):
    """
    
    """
    __tablename__ = 'PlantSample_external_identifiers'

    PlantSample_id = Column(UUID(), ForeignKey('PlantSample.id'), primary_key=True)
    external_identifiers = Column(Text(), primary_key=True)
    

    

    def __repr__(self):
        return f"PlantSample_external_identifiers(PlantSample_id={self.PlantSample_id},external_identifiers={self.external_identifiers},)"



    


class PureCultureSample_external_identifiers(Base):
    """
    
    """
    __tablename__ = 'PureCultureSample_external_identifiers'

    PureCultureSample_id = Column(UUID(), ForeignKey('PureCultureSample.id'), primary_key=True)
    external_identifiers = Column(Text(), primary_key=True)
    

    

    def __repr__(self):
        return f"PureCultureSample_external_identifiers(PureCultureSample_id={self.PureCultureSample_id},external_identifiers={self.external_identifiers},)"



    


class SedimentSample_external_identifiers(Base):
    """
    
    """
    __tablename__ = 'SedimentSample_external_identifiers'

    SedimentSample_id = Column(UUID(), ForeignKey('SedimentSample.id'), primary_key=True)
    external_identifiers = Column(Text(), primary_key=True)
    

    

    def __repr__(self):
        return f"SedimentSample_external_identifiers(SedimentSample_id={self.SedimentSample_id},external_identifiers={self.external_identifiers},)"



    


class SoilSample_external_identifiers(Base):
    """
    
    """
    __tablename__ = 'SoilSample_external_identifiers'

    SoilSample_id = Column(UUID(), ForeignKey('SoilSample.id'), primary_key=True)
    external_identifiers = Column(Text(), primary_key=True)
    

    

    def __repr__(self):
        return f"SoilSample_external_identifiers(SoilSample_id={self.SoilSample_id},external_identifiers={self.external_identifiers},)"



    


class SynthesizedMaterialSample_external_identifiers(Base):
    """
    
    """
    __tablename__ = 'SynthesizedMaterialSample_external_identifiers'

    SynthesizedMaterialSample_id = Column(UUID(), ForeignKey('SynthesizedMaterialSample.id'), primary_key=True)
    external_identifiers = Column(Text(), primary_key=True)
    

    

    def __repr__(self):
        return f"SynthesizedMaterialSample_external_identifiers(SynthesizedMaterialSample_id={self.SynthesizedMaterialSample_id},external_identifiers={self.external_identifiers},)"



    


class TerraformSample_external_identifiers(Base):
    """
    
    """
    __tablename__ = 'TerraformSample_external_identifiers'

    TerraformSample_id = Column(UUID(), ForeignKey('TerraformSample.id'), primary_key=True)
    external_identifiers = Column(Text(), primary_key=True)
    

    

    def __repr__(self):
        return f"TerraformSample_external_identifiers(TerraformSample_id={self.TerraformSample_id},external_identifiers={self.external_identifiers},)"



    


class WaterSample_external_identifiers(Base):
    """
    
    """
    __tablename__ = 'WaterSample_external_identifiers'

    WaterSample_id = Column(UUID(), ForeignKey('WaterSample.id'), primary_key=True)
    external_identifiers = Column(Text(), primary_key=True)
    

    

    def __repr__(self):
        return f"WaterSample_external_identifiers(WaterSample_id={self.WaterSample_id},external_identifiers={self.external_identifiers},)"



    


class Study_external_identifiers(Base):
    """
    
    """
    __tablename__ = 'Study_external_identifiers'

    Study_id = Column(UUID(), ForeignKey('Study.id'), primary_key=True)
    external_identifiers = Column(Text(), primary_key=True)
    

    

    def __repr__(self):
        return f"Study_external_identifiers(Study_id={self.Study_id},external_identifiers={self.external_identifiers},)"



    


class Study_has_participants(Base):
    """
    
    """
    __tablename__ = 'Study_has_participants'

    Study_id = Column(UUID(), ForeignKey('Study.id'), primary_key=True)
    has_participants_id = Column(UUID(), ForeignKey('ProjectParticipant.id'), primary_key=True)
    

    

    def __repr__(self):
        return f"Study_has_participants(Study_id={self.Study_id},has_participants_id={self.has_participants_id},)"



    


class Study_associated_dois(Base):
    """
    
    """
    __tablename__ = 'Study_associated_dois'

    Study_id = Column(UUID(), ForeignKey('Study.id'), primary_key=True)
    associated_dois_id = Column(Integer(), ForeignKey('DOI.id'), primary_key=True)
    

    

    def __repr__(self):
        return f"Study_associated_dois(Study_id={self.Study_id},associated_dois_id={self.associated_dois_id},)"



    


class Study_funding_sources(Base):
    """
    
    """
    __tablename__ = 'Study_funding_sources'

    Study_id = Column(UUID(), ForeignKey('Study.id'), primary_key=True)
    funding_sources_id = Column(Integer(), ForeignKey('DOI.id'), primary_key=True)
    

    

    def __repr__(self):
        return f"Study_funding_sources(Study_id={self.Study_id},funding_sources_id={self.funding_sources_id},)"



    


class ProcessedData(DataProduct):
    """
    A data product generated by a workflow execution.
    """
    __tablename__ = 'ProcessedData'

    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"ProcessedData(summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},sample_id={self.sample_id},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class InstrumentData(DataProduct):
    """
    An abstract parent class for raw data files generated by different kinds  of instruments. All subclasses must have a slot pointing upstream that  specifies the analysisActivity subclass which created them.
    """
    __tablename__ = 'InstrumentData'

    file_curie = Column(Text())
    alternative_identifiers = Column(Text())
    compression_type = Column(Text())
    file_type = Column(Enum('FT_ICR_MS_Analysis_Results', 'GC_MS_Metabolomics_Results', 'Metaproteomics_Workflow_Statistics', 'Protein_Report', 'Peptide_Report', 'Unfiltered_Metaproteomics_Results', 'Read_Count_and_RPKM', 'QC_non_rRNA_R2', 'QC_non_rRNA_R1', 'Metagenome_Bins', 'CheckM_Statistics', 'GOTTCHA2_Krona_Plot', 'Kraken2_Krona_Plot', 'Centrifuge_Krona_Plot', 'Kraken2_Classification_Report', 'Kraken2_Taxonomic_Classification', 'Centrifuge_Classification_Report', 'Centrifuge_Taxonomic_Classification', 'Structural_Annotation_GFF', 'Functional_Annotation_GFF', 'Annotation_Amino_Acid_FASTA', 'Annotation_Enzyme_Commission', 'Annotation_KEGG_Orthology', 'Assembly_Coverage_BAM', 'Assembly_AGP', 'Assembly_Scaffolds', 'Assembly_Contigs', 'Assembly_Coverage_Stats', 'Filtered_Sequencing_Reads', 'QC_Statistics', 'TIGRFam_Annotation_GFF', 'Clusters_of_Orthologous_Groups_COG_Annotation_GFF', 'CATH_FunFams_Functional_Families_Annotation_GFF', 'SUPERFam_Annotation_GFF', 'SMART_Annotation_GFF', 'Pfam_Annotation_GFF', 'Direct_Infusion_FT_ICR_MS_Raw_Data', name='FileTypeEnum'))
    software_version = Column(Text())
    name = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"InstrumentData(file_curie={self.file_curie},alternative_identifiers={self.alternative_identifiers},compression_type={self.compression_type},file_type={self.file_type},software_version={self.software_version},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SitePhoto(DataProduct):
    """
    A data product representing a photo of a site, typically taken during sampling.
One row per photo with metadata about the photo type and when it was taken.
    """
    __tablename__ = 'SitePhoto'

    site_photo_type = Column(Enum('landscape', 'measure', name='SitePhotoCategoryEnum'))
    photo_taken_during = Column(UUID(), ForeignKey('SamplingActivity.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"SitePhoto(site_photo_type={self.site_photo_type},photo_taken_during={self.photo_taken_during},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class RespirationDataGenerationActivity(DataGenerationActivity):
    """
    Data generation activity for soil respiration analysis.
Captures CO2-C efflux measured per gram of soil.
    """
    __tablename__ = 'RespirationDataGenerationActivity'

    sequence_order = Column(Integer())
    name = Column(Text(), nullable=False )
    description = Column(Text())
    protocol_url = Column(Text())
    protocol_version = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analyte_id = Column(UUID(), ForeignKey('ProcessedSample.id'))
    acquisition_start_time = Column(DateTime(), nullable=False )
    acquisition_end_time = Column(DateTime(), nullable=False )
    instrument_used = Column(UUID(), ForeignKey('Instrument.id'))
    instrument_operator_id = Column(UUID(), ForeignKey('PersonValue.id'))
    method_id_id = Column(Integer(), ForeignKey('RespirationMethod.id'))
    method_id = relationship("RespirationMethod", uselist=False, foreign_keys=[method_id_id])
    

    

    def __repr__(self):
        return f"RespirationDataGenerationActivity(sequence_order={self.sequence_order},name={self.name},description={self.description},protocol_url={self.protocol_url},protocol_version={self.protocol_version},id={self.id},analyte_id={self.analyte_id},acquisition_start_time={self.acquisition_start_time},acquisition_end_time={self.acquisition_end_time},instrument_used={self.instrument_used},instrument_operator_id={self.instrument_operator_id},method_id_id={self.method_id_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class XRayDataGenerationActivity(DataGenerationActivity):
    """
    Abstract base class for X-ray analytical methods including XRF (elemental)
and XRD (mineralogical) analysis. Inherits acquisition_time, instrument_id,
protocol_url, analyte_id, and other core metadata from DataGenerationActivity.

Concrete subclasses define method-specific measurement parameters.
Future X-ray methods (e.g., XCT) can extend this class.

Shared patterns:
  - Direct instrument output (no computational workflow) is typical for XRF
  - XRD may optionally link to DataProcessingActivity for Rietveld refinement
  - protocol_url should link to vendor SOP or EMSL internal protocol documentation
    """
    __tablename__ = 'XRayDataGenerationActivity'

    sequence_order = Column(Integer())
    name = Column(Text(), nullable=False )
    description = Column(Text())
    protocol_url = Column(Text())
    protocol_version = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analyte_id = Column(UUID(), ForeignKey('ProcessedSample.id'))
    acquisition_start_time = Column(DateTime(), nullable=False )
    acquisition_end_time = Column(DateTime(), nullable=False )
    instrument_used = Column(UUID(), ForeignKey('Instrument.id'))
    instrument_operator_id = Column(UUID(), ForeignKey('PersonValue.id'))
    

    

    def __repr__(self):
        return f"XRayDataGenerationActivity(sequence_order={self.sequence_order},name={self.name},description={self.description},protocol_url={self.protocol_url},protocol_version={self.protocol_version},id={self.id},analyte_id={self.analyte_id},acquisition_start_time={self.acquisition_start_time},acquisition_end_time={self.acquisition_end_time},instrument_used={self.instrument_used},instrument_operator_id={self.instrument_operator_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MassSpectrometryDataGenerationActivity(DataGenerationActivity):
    """
    A record of the mass spectrometry run that generates a raw data product.
    """
    __tablename__ = 'MassSpectrometryDataGenerationActivity'

    analyte_category = Column(Enum('dna', 'rna', 'protein', 'metabolite', 'lipid', 'natural_organic_matter', 'unknown', name='AnalyteCategoryEnum'))
    sequence_order = Column(Integer())
    name = Column(Text(), nullable=False )
    description = Column(Text())
    protocol_url = Column(Text())
    protocol_version = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analyte_id = Column(UUID(), ForeignKey('ProcessedSample.id'))
    acquisition_start_time = Column(DateTime(), nullable=False )
    acquisition_end_time = Column(DateTime(), nullable=False )
    instrument_used = Column(UUID(), ForeignKey('Instrument.id'))
    instrument_operator_id = Column(UUID(), ForeignKey('PersonValue.id'))
    uses_ms_configuration_uid = Column(Integer(), ForeignKey('MassSpectrometryConfiguration.uid'), nullable=False )
    uses_ms_configuration = relationship("MassSpectrometryConfiguration", uselist=False, foreign_keys=[uses_ms_configuration_uid])
    uses_chromatography_uid = Column(Integer(), ForeignKey('ChromatographyConfiguration.uid'))
    uses_chromatography = relationship("ChromatographyConfiguration", uselist=False, foreign_keys=[uses_chromatography_uid])
    

    

    def __repr__(self):
        return f"MassSpectrometryDataGenerationActivity(analyte_category={self.analyte_category},sequence_order={self.sequence_order},name={self.name},description={self.description},protocol_url={self.protocol_url},protocol_version={self.protocol_version},id={self.id},analyte_id={self.analyte_id},acquisition_start_time={self.acquisition_start_time},acquisition_end_time={self.acquisition_end_time},instrument_used={self.instrument_used},instrument_operator_id={self.instrument_operator_id},uses_ms_configuration_uid={self.uses_ms_configuration_uid},uses_chromatography_uid={self.uses_chromatography_uid},)"



    
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
    injection = Column(Text(), nullable=False )
    ionization = Column(Enum('electrospray_ionization', 'matrix_assisted_laser_desorption_ionization', 'atmospheric_pressure_photo_ionization', 'atmospheric_pressure_chemical_ionization', 'electron_ionization', name='IonizationSourceEnum'), nullable=False )
    fragmentation = Column(Enum('HCD', 'CID', 'ETD', name='FragmentationEnum'))
    polarity = Column(Enum('positive', 'negative', name='PolarityEnum'), nullable=False )
    resolution = Column(Enum('high', 'low', name='MassSpecResolutionEnum'), nullable=False )
    dd_ms2_resolution = Column(Float(), nullable=False )
    loop_count = Column(Text(), nullable=False )
    iat = Column(Float())
    fid = Column(Float())
    mass_range_max = Column(Float())
    mass_range_min = Column(Float())
    acquisition_strategy = Column(Enum('data_independent_acquisition', 'data_dependent_acquisition', 'full_scan_only', name='MassSpectrometryAcquisitionStrategyEnum'))
    lims_protocol_instance_id = Column(Integer())
    name = Column(Text(), nullable=False )
    description = Column(Text())
    id = Column(UUID(), nullable=False )
    

    

    def __repr__(self):
        return f"MassSpectrometryConfiguration(uid={self.uid},injection={self.injection},ionization={self.ionization},fragmentation={self.fragmentation},polarity={self.polarity},resolution={self.resolution},dd_ms2_resolution={self.dd_ms2_resolution},loop_count={self.loop_count},iat={self.iat},fid={self.fid},mass_range_max={self.mass_range_max},mass_range_min={self.mass_range_min},acquisition_strategy={self.acquisition_strategy},lims_protocol_instance_id={self.lims_protocol_instance_id},name={self.name},description={self.description},id={self.id},)"



    
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
    column = Column(Text())
    column_dimensions = Column(Text())
    column_manufacturer = Column(Text())
    chromatography_type = Column(Enum('liquid_chromatography', 'gas_chromatography', 'solid_phase_extraction', name='ChromatographyCategoryEnum'), nullable=False )
    stationary_phase = Column(Text())
    temperature_celsius = Column(Float())
    duration_min = Column(Float())
    flow_rate_ul_min = Column(Float())
    injection_volume_ul = Column(Float())
    name = Column(Text(), nullable=False )
    description = Column(Text())
    id = Column(UUID(), nullable=False )
    
    
    # ManyToMany
    mobile_phases = relationship( "MobilePhaseSegment", secondary="ChromatographyConfiguration_mobile_phases")
    

    

    def __repr__(self):
        return f"ChromatographyConfiguration(uid={self.uid},column={self.column},column_dimensions={self.column_dimensions},column_manufacturer={self.column_manufacturer},chromatography_type={self.chromatography_type},stationary_phase={self.stationary_phase},temperature_celsius={self.temperature_celsius},duration_min={self.duration_min},flow_rate_ul_min={self.flow_rate_ul_min},injection_volume_ul={self.injection_volume_ul},name={self.name},description={self.description},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MassSpectrometryDataProcessingActivity(DataProcessingActivity):
    """
    Concrete mass spectrometry workflow run. Inherits all DataProcessingActivity
slots including used_software and version.
    """
    __tablename__ = 'MassSpectrometryDataProcessingActivity'

    uses_calibration = Column(UUID(), ForeignKey('MassSpectrometryStandardRun.id'))
    uses_raw_ms_data = Column(UUID(), ForeignKey('MassSpectrometryInstrumentData.id'))
    lims_task_instance_id = Column(Integer())
    metaproteomics_analysis_category = Column(Enum('matched_metagenome', 'in_silico_metagenome', 'WITHDRAWN', name='MetaproteomicsAnalysisCategoryEnum'))
    parent_workflow_id = Column(UUID(), ForeignKey('DataProcessingActivity.id'))
    workflow_steps = Column(Text())
    description = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    started_at_time = Column(DateTime(), nullable=False )
    ended_at_time = Column(DateTime())
    software_url = Column(Text())
    software_version = Column(Text())
    software_poc = Column(Text())
    execution_resource = Column(Enum('nersc_cori', 'nersc_perlmutter', 'emsl_rzr', 'emsl_tahoma', name='ExecutionResourceEnum'))
    

    

    def __repr__(self):
        return f"MassSpectrometryDataProcessingActivity(uses_calibration={self.uses_calibration},uses_raw_ms_data={self.uses_raw_ms_data},lims_task_instance_id={self.lims_task_instance_id},metaproteomics_analysis_category={self.metaproteomics_analysis_category},parent_workflow_id={self.parent_workflow_id},workflow_steps={self.workflow_steps},description={self.description},id={self.id},started_at_time={self.started_at_time},ended_at_time={self.ended_at_time},software_url={self.software_url},software_version={self.software_version},software_poc={self.software_poc},execution_resource={self.execution_resource},)"



    
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
    protocol_url = Column(Text())
    protocol_version = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analysis_type = Column(Enum('analysis_activity', 'lcms_metabolomics_method', 'fticr_acquisition_method', 'gravimetric_water_content_method', 'ph_method', 'hydraulic_properties_method', 'microbial_biomass_method', 'xray_computed_tomography_method', 'REGEN', 'KUO', 'respiration_method', 'texture_method', 'enzyme_activity_method', 'elemental_analysis_method', 'toc_tn_method', 'bulk_density_method', 'metagenomics_method', 'xrf_analysis', 'xrd_analysis', name='RouteMethodEnum'))
    method_name = Column(Enum('MAOM', 'WOEM', name='MethodNameEnum'))
    processing_steps = Column(Text(), nullable=False )
    uses_sample = Column(UUID(), ForeignKey('Sample.id'))
    
    
    exposure_sensitivity_rel = relationship( "MediaPreparation_exposure_sensitivity" )
    exposure_sensitivity = association_proxy("exposure_sensitivity_rel", "exposure_sensitivity",
                                  creator=lambda x_: MediaPreparation_exposure_sensitivity(exposure_sensitivity=x_))
    
    
    media_additions_rel = relationship( "MediaPreparation_media_additions" )
    media_additions = association_proxy("media_additions_rel", "media_additions",
                                  creator=lambda x_: MediaPreparation_media_additions(media_additions=x_))
    

    

    def __repr__(self):
        return f"MediaPreparation(media_type={self.media_type},volume_ml={self.volume_ml},media_recipe={self.media_recipe},media_formulation={self.media_formulation},commercial_media_catalog={self.commercial_media_catalog},sterilization_method={self.sterilization_method},ph_adjustment={self.ph_adjustment},ph_target={self.ph_target},storage_temperature={self.storage_temperature},creation_date={self.creation_date},protocol_url={self.protocol_url},protocol_version={self.protocol_version},id={self.id},analysis_type={self.analysis_type},method_name={self.method_name},processing_steps={self.processing_steps},uses_sample={self.uses_sample},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class CultureGrowth(SampleProcessing):
    """
    Abstract activity for growing cultures from samples or other cultures.

Concrete subclasses: StrainPurity, StockCulturePreparation, 
PreCultureGrowth, ExperimentalCulture.
    """
    __tablename__ = 'CultureGrowth'

    biological_entity_ref = Column(UUID(), ForeignKey('biological_entity.id'))
    growth_medium = Column(Text())
    incubation_time_hours = Column(Float())
    container_type = Column(Text())
    temperature_celsius = Column(Float())
    agitation_speed_rpm = Column(Integer())
    oxygen_status = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'obligate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    protocol_url = Column(Text())
    protocol_version = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analysis_type = Column(Enum('analysis_activity', 'lcms_metabolomics_method', 'fticr_acquisition_method', 'gravimetric_water_content_method', 'ph_method', 'hydraulic_properties_method', 'microbial_biomass_method', 'xray_computed_tomography_method', 'REGEN', 'KUO', 'respiration_method', 'texture_method', 'enzyme_activity_method', 'elemental_analysis_method', 'toc_tn_method', 'bulk_density_method', 'metagenomics_method', 'xrf_analysis', 'xrd_analysis', name='RouteMethodEnum'))
    method_name = Column(Enum('MAOM', 'WOEM', name='MethodNameEnum'))
    processing_steps = Column(Text(), nullable=False )
    uses_sample = Column(UUID(), ForeignKey('Sample.id'))
    

    

    def __repr__(self):
        return f"CultureGrowth(biological_entity_ref={self.biological_entity_ref},growth_medium={self.growth_medium},incubation_time_hours={self.incubation_time_hours},container_type={self.container_type},temperature_celsius={self.temperature_celsius},agitation_speed_rpm={self.agitation_speed_rpm},oxygen_status={self.oxygen_status},protocol_url={self.protocol_url},protocol_version={self.protocol_version},id={self.id},analysis_type={self.analysis_type},method_name={self.method_name},processing_steps={self.processing_steps},uses_sample={self.uses_sample},)"



    
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
    setup_operator_id = Column(UUID(), ForeignKey('PersonValue.id'))
    setup_instrument = Column(Text())
    sealing_method = Column(Text())
    temperature_celsius = Column(Float())
    agitation_speed_rpm = Column(Integer())
    oxygen_status = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'obligate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    protocol_url = Column(Text())
    protocol_version = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analysis_type = Column(Enum('analysis_activity', 'lcms_metabolomics_method', 'fticr_acquisition_method', 'gravimetric_water_content_method', 'ph_method', 'hydraulic_properties_method', 'microbial_biomass_method', 'xray_computed_tomography_method', 'REGEN', 'KUO', 'respiration_method', 'texture_method', 'enzyme_activity_method', 'elemental_analysis_method', 'toc_tn_method', 'bulk_density_method', 'metagenomics_method', 'xrf_analysis', 'xrd_analysis', name='RouteMethodEnum'))
    method_name = Column(Enum('MAOM', 'WOEM', name='MethodNameEnum'))
    processing_steps = Column(Text(), nullable=False )
    uses_sample = Column(UUID(), ForeignKey('Sample.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='PlateSetupActivity', source_slot='well_metadata', mapping_type=None, target_class='WellMetadata', target_slot='PlateSetupActivity_id', join_class=None, uses_join_table=None, multivalued=False)
    well_metadata = relationship( "WellMetadata", foreign_keys="[WellMetadata.PlateSetupActivity_id]")
    

    

    def __repr__(self):
        return f"PlateSetupActivity(plate_type={self.plate_type},plate_barcode={self.plate_barcode},setup_date={self.setup_date},setup_operator_id={self.setup_operator_id},setup_instrument={self.setup_instrument},sealing_method={self.sealing_method},temperature_celsius={self.temperature_celsius},agitation_speed_rpm={self.agitation_speed_rpm},oxygen_status={self.oxygen_status},protocol_url={self.protocol_url},protocol_version={self.protocol_version},id={self.id},analysis_type={self.analysis_type},method_name={self.method_name},processing_steps={self.processing_steps},uses_sample={self.uses_sample},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class PlateDataGenerationActivity(DataGenerationActivity):
    """
    Abstract base for plate measurement activities.
Adds timepoint_label for repeated-measurement series 
    """
    __tablename__ = 'PlateDataGenerationActivity'

    timepoint_label = Column(Text(), nullable=False )
    sequence_order = Column(Integer())
    name = Column(Text(), nullable=False )
    description = Column(Text())
    protocol_url = Column(Text())
    protocol_version = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analyte_id = Column(UUID(), ForeignKey('ProcessedSample.id'))
    acquisition_start_time = Column(DateTime(), nullable=False )
    acquisition_end_time = Column(DateTime(), nullable=False )
    instrument_used = Column(UUID(), ForeignKey('Instrument.id'))
    instrument_operator_id = Column(UUID(), ForeignKey('PersonValue.id'))
    

    

    def __repr__(self):
        return f"PlateDataGenerationActivity(timepoint_label={self.timepoint_label},sequence_order={self.sequence_order},name={self.name},description={self.description},protocol_url={self.protocol_url},protocol_version={self.protocol_version},id={self.id},analyte_id={self.analyte_id},acquisition_start_time={self.acquisition_start_time},acquisition_end_time={self.acquisition_end_time},instrument_used={self.instrument_used},instrument_operator_id={self.instrument_operator_id},)"



    
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
    


class NucleotideSequencing(DataGenerationActivity):
    """
    A lab activity in which DNA or RNA that was extracted from a sample is sequenced.
    """
    __tablename__ = 'NucleotideSequencing'

    nucleotide_sequencing_category = Column(Enum('metagenome', 'metatranscriptome', 'amplicon_sequencing_assay', name='NucleotideSequencingEnum'))
    sequence_order = Column(Integer())
    name = Column(Text(), nullable=False )
    description = Column(Text())
    protocol_url = Column(Text())
    protocol_version = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analyte_id = Column(UUID(), ForeignKey('ProcessedSample.id'))
    acquisition_start_time = Column(DateTime(), nullable=False )
    acquisition_end_time = Column(DateTime(), nullable=False )
    instrument_used = Column(UUID(), ForeignKey('Instrument.id'))
    instrument_operator_id = Column(UUID(), ForeignKey('PersonValue.id'))
    
    
    external_identifiers_rel = relationship( "NucleotideSequencing_external_identifiers" )
    external_identifiers = association_proxy("external_identifiers_rel", "external_identifiers",
                                  creator=lambda x_: NucleotideSequencing_external_identifiers(external_identifiers=x_))
    

    

    def __repr__(self):
        return f"NucleotideSequencing(nucleotide_sequencing_category={self.nucleotide_sequencing_category},sequence_order={self.sequence_order},name={self.name},description={self.description},protocol_url={self.protocol_url},protocol_version={self.protocol_version},id={self.id},analyte_id={self.analyte_id},acquisition_start_time={self.acquisition_start_time},acquisition_end_time={self.acquisition_end_time},instrument_used={self.instrument_used},instrument_operator_id={self.instrument_operator_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MetagenomicsDataProcessingActivity(DataProcessingActivity):
    """
    Concrete metagenomics workflow run. Inherits all DataProcessingActivity
slots including parent_workflow_id (chain link) and workflow_steps
(key-value, schema TBD). Specific workflow step type is captured via the
inherited type attribute (string); expected values: 
'metagenomics_annotation', 'metagenomics_binning', 'metagenomics_phylogeny'.
    """
    __tablename__ = 'MetagenomicsDataProcessingActivity'

    parent_workflow_id = Column(UUID(), ForeignKey('DataProcessingActivity.id'))
    workflow_steps = Column(Text())
    description = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    started_at_time = Column(DateTime(), nullable=False )
    ended_at_time = Column(DateTime())
    software_url = Column(Text())
    software_version = Column(Text())
    software_poc = Column(Text())
    execution_resource = Column(Enum('nersc_cori', 'nersc_perlmutter', 'emsl_rzr', 'emsl_tahoma', name='ExecutionResourceEnum'))
    

    

    def __repr__(self):
        return f"MetagenomicsDataProcessingActivity(parent_workflow_id={self.parent_workflow_id},workflow_steps={self.workflow_steps},description={self.description},id={self.id},started_at_time={self.started_at_time},ended_at_time={self.ended_at_time},software_url={self.software_url},software_version={self.software_version},software_poc={self.software_poc},execution_resource={self.execution_resource},)"



    
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
    analytic = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"RespirationMethod(id={self.id},analytic={self.analytic},)"



    
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
    


class AerosolArmSample(Sample):
    """
    An aerosol sample collected by the ARM facility.
    """
    __tablename__ = 'AerosolArmSample'

    aerosol_type = Column(Enum('sea_salt', 'dust', 'volcanic_ash', name='AerosolTypeEnum'), nullable=False )
    air_temp_regm = Column(Text())
    analysis_type = Column(Text(), nullable=False )
    carb_dioxide = Column(Text())
    carb_monoxide = Column(Text())
    chem_administration = Column(Text())
    color_code = Column(Enum('Red- 0-250m Profiling', 'Red Hashed- 0-250m Loitering', 'Yellow- 251-500m Profiling', 'Yellow Hashed- 251-500m Loitering', 'Green- 501-750m Profiling', 'Green Hashed- 501-750m Loitering', 'Blue- 751-1000m Profiling', 'Blue Hashed- 751-1000m Loitering', 'Purple- >=1001m Profiling', 'Purple Hashed- >=1001m Loitering', name='ColorCodeEnum'))
    env_broad_scale = Column(Text())
    env_local_scale = Column(Text())
    env_medium = Column(Text())
    experimental_factor = Column(Text())
    experimental_factor_other = Column(Text())
    extraction_method = Column(Text())
    first_blh = Column(Float())
    first_blh_quality_index = Column(Text())
    first_cbh = Column(Float())
    humidity_regm = Column(Text())
    isotope_exposure = Column(Text())
    latitude = Column(Float())
    longitude = Column(Float())
    mean_total_cpc_concentration = Column(Float())
    mean_total_pops_concentration = Column(Float())
    methane = Column(Text())
    method_development = Column(Text())
    misc_param = Column(Text())
    other = Column(Text())
    other_treatment = Column(Text())
    other_samp_store_temp = Column(Text())
    photochemical_exposure = Column(Enum('ultraviolet', 'visible light', 'infrared', name='PhotochemicalExposureEnum'))
    pressure_control = Column(Text())
    priority_order = Column(Float())
    project = Column(Integer())
    replicate_number = Column(Integer())
    samp_store_temp = Column(Enum('fresh4', 'freshroom', 'frozen20', 'frozen80', 'other', name='SampleStoreTempEnum'))
    sample_link = Column(Text())
    sample_name = Column(Text())
    sample_processing = Column(Text())
    sampled_during = Column(UUID(), ForeignKey('SamplingActivity.id'))
    second_blh = Column(Float())
    second_blh_quality = Column(Text())
    second_cbh = Column(Float())
    size_frac_low = Column(Text())
    size_frac_up = Column(Text())
    solar_irradiance = Column(Text())
    source_mat_id = Column(Text())
    storage_condition = Column(Enum('fresh', 'frozen', 'lyophilized', 'other', name='StorageConditionEnum'))
    storage_condition_other = Column(Text())
    technical_reps = Column(Integer())
    third_blh = Column(Float())
    third_blh_quality = Column(Text())
    volatile_org_comp = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    emsl_activity = Column(Text())
    lims_barcode = Column(Text())
    
    
    external_identifiers_rel = relationship( "AerosolArmSample_external_identifiers" )
    external_identifiers = association_proxy("external_identifiers_rel", "external_identifiers",
                                  creator=lambda x_: AerosolArmSample_external_identifiers(external_identifiers=x_))
    

    

    def __repr__(self):
        return f"AerosolArmSample(aerosol_type={self.aerosol_type},air_temp_regm={self.air_temp_regm},analysis_type={self.analysis_type},carb_dioxide={self.carb_dioxide},carb_monoxide={self.carb_monoxide},chem_administration={self.chem_administration},color_code={self.color_code},env_broad_scale={self.env_broad_scale},env_local_scale={self.env_local_scale},env_medium={self.env_medium},experimental_factor={self.experimental_factor},experimental_factor_other={self.experimental_factor_other},extraction_method={self.extraction_method},first_blh={self.first_blh},first_blh_quality_index={self.first_blh_quality_index},first_cbh={self.first_cbh},humidity_regm={self.humidity_regm},isotope_exposure={self.isotope_exposure},latitude={self.latitude},longitude={self.longitude},mean_total_cpc_concentration={self.mean_total_cpc_concentration},mean_total_pops_concentration={self.mean_total_pops_concentration},methane={self.methane},method_development={self.method_development},misc_param={self.misc_param},other={self.other},other_treatment={self.other_treatment},other_samp_store_temp={self.other_samp_store_temp},photochemical_exposure={self.photochemical_exposure},pressure_control={self.pressure_control},priority_order={self.priority_order},project={self.project},replicate_number={self.replicate_number},samp_store_temp={self.samp_store_temp},sample_link={self.sample_link},sample_name={self.sample_name},sample_processing={self.sample_processing},sampled_during={self.sampled_during},second_blh={self.second_blh},second_blh_quality={self.second_blh_quality},second_cbh={self.second_cbh},size_frac_low={self.size_frac_low},size_frac_up={self.size_frac_up},solar_irradiance={self.solar_irradiance},source_mat_id={self.source_mat_id},storage_condition={self.storage_condition},storage_condition_other={self.storage_condition_other},technical_reps={self.technical_reps},third_blh={self.third_blh},third_blh_quality={self.third_blh_quality},volatile_org_comp={self.volatile_org_comp},id={self.id},name={self.name},description={self.description},emsl_activity={self.emsl_activity},lims_barcode={self.lims_barcode},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class AerosolSample(Sample):
    """
    An aerosol sample collected from the environment.
    """
    __tablename__ = 'AerosolSample'

    aerosol_type = Column(Enum('sea_salt', 'dust', 'volcanic_ash', name='AerosolTypeEnum'), nullable=False )
    air_temp_regm = Column(Text())
    analysis_type = Column(Text(), nullable=False )
    carb_dioxide = Column(Text())
    carb_monoxide = Column(Text())
    chem_administration = Column(Text())
    env_broad_scale = Column(Text())
    env_local_scale = Column(Text())
    env_medium = Column(Text())
    experimental_factor = Column(Text())
    experimental_factor_other = Column(Text())
    extraction_method = Column(Text())
    humidity_regm = Column(Text())
    isotope_exposure = Column(Text())
    latitude = Column(Float())
    longitude = Column(Float())
    methane = Column(Text())
    method_development = Column(Text())
    misc_param = Column(Text())
    other = Column(Text())
    other_samp_store_temp = Column(Text())
    other_storage_condt = Column(Text())
    other_treatment = Column(Text())
    oxygen = Column(Text())
    photochemical_exposure = Column(Enum('ultraviolet', 'visible light', 'infrared', name='PhotochemicalExposureEnum'))
    pressure_control = Column(Text())
    priority_order = Column(Float())
    project = Column(Integer())
    replicate_number = Column(Integer())
    sample_link = Column(Text())
    sample_name = Column(Text())
    sample_processing = Column(Text())
    sampled_during = Column(UUID(), ForeignKey('SamplingActivity.id'))
    samp_store_temp = Column(Enum('fresh4', 'freshroom', 'frozen20', 'frozen80', 'other', name='SampleStoreTempEnum'))
    size_frac_low = Column(Text())
    size_frac_up = Column(Text())
    solar_irradiance = Column(Text())
    source_mat_id = Column(Text())
    storage_condition = Column(Enum('fresh', 'frozen', 'lyophilized', 'other', name='StorageConditionEnum'))
    storage_condition_other = Column(Text())
    technical_reps = Column(Integer())
    temperature_exposure = Column(Text())
    volatile_org_comp = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    emsl_activity = Column(Text())
    lims_barcode = Column(Text())
    
    
    external_identifiers_rel = relationship( "AerosolSample_external_identifiers" )
    external_identifiers = association_proxy("external_identifiers_rel", "external_identifiers",
                                  creator=lambda x_: AerosolSample_external_identifiers(external_identifiers=x_))
    

    

    def __repr__(self):
        return f"AerosolSample(aerosol_type={self.aerosol_type},air_temp_regm={self.air_temp_regm},analysis_type={self.analysis_type},carb_dioxide={self.carb_dioxide},carb_monoxide={self.carb_monoxide},chem_administration={self.chem_administration},env_broad_scale={self.env_broad_scale},env_local_scale={self.env_local_scale},env_medium={self.env_medium},experimental_factor={self.experimental_factor},experimental_factor_other={self.experimental_factor_other},extraction_method={self.extraction_method},humidity_regm={self.humidity_regm},isotope_exposure={self.isotope_exposure},latitude={self.latitude},longitude={self.longitude},methane={self.methane},method_development={self.method_development},misc_param={self.misc_param},other={self.other},other_samp_store_temp={self.other_samp_store_temp},other_storage_condt={self.other_storage_condt},other_treatment={self.other_treatment},oxygen={self.oxygen},photochemical_exposure={self.photochemical_exposure},pressure_control={self.pressure_control},priority_order={self.priority_order},project={self.project},replicate_number={self.replicate_number},sample_link={self.sample_link},sample_name={self.sample_name},sample_processing={self.sample_processing},sampled_during={self.sampled_during},samp_store_temp={self.samp_store_temp},size_frac_low={self.size_frac_low},size_frac_up={self.size_frac_up},solar_irradiance={self.solar_irradiance},source_mat_id={self.source_mat_id},storage_condition={self.storage_condition},storage_condition_other={self.storage_condition_other},technical_reps={self.technical_reps},temperature_exposure={self.temperature_exposure},volatile_org_comp={self.volatile_org_comp},id={self.id},name={self.name},description={self.description},emsl_activity={self.emsl_activity},lims_barcode={self.lims_barcode},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class AMP2UserSample(Sample):
    """
    A user-submitted microbial sample for AMP2 workflows.

References a biological_entity for identity (the "what") and carries
physical/logistical metadata for the specific sample instance (the "this tube").

Relationship to biological_entity:
  - Many AMP2UserSample instances can reference one biological_entity
  - biological_entity_ref is the FK (required)
  - Example: 1000 samples of strain KT2440_pTE314

Workflow integration:
  - Enters workflow via SampleReceiving activity
  - Processed through StrainPurity → StockCulturePreparation → PreCultureGrowth → ExperimentalCulture
  - Outputs ProcessedSample instances at each stage
    """
    __tablename__ = 'AMP2UserSample'

    biological_entity_ref = Column(UUID(), ForeignKey('biological_entity.id'), nullable=False )
    collection_date = Column(Date())
    growth_facil = Column(Enum('field', 'commercially_purchased', 'experimental_garden', 'field_incubation', 'greenhouse', 'growth_chamber', 'lab_incubation', 'open_top_chamber', 'other', name='GrowthFacilityEnum'))
    isol_growth_condt = Column(Text())
    start_date_inc = Column(Text())
    storage_condition = Column(Enum('fresh', 'frozen', 'lyophilized', 'other', name='StorageConditionEnum'), nullable=False )
    storage_temperature = Column(Text())
    shipped_sample_size = Column(Text())
    guid_source = Column(Text())
    other_guid_source = Column(Text())
    analysis_type = Column(Text())
    cbi = Column(Boolean())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    emsl_activity = Column(Text())
    lims_barcode = Column(Text())
    

    

    def __repr__(self):
        return f"AMP2UserSample(biological_entity_ref={self.biological_entity_ref},collection_date={self.collection_date},growth_facil={self.growth_facil},isol_growth_condt={self.isol_growth_condt},start_date_inc={self.start_date_inc},storage_condition={self.storage_condition},storage_temperature={self.storage_temperature},shipped_sample_size={self.shipped_sample_size},guid_source={self.guid_source},other_guid_source={self.other_guid_source},analysis_type={self.analysis_type},cbi={self.cbi},id={self.id},name={self.name},description={self.description},emsl_activity={self.emsl_activity},lims_barcode={self.lims_barcode},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class CommerciallyPurchasedSample(Sample):
    """
    A sample containing commercially purchased material.
    """
    __tablename__ = 'CommerciallyPurchasedSample'

    analysis_type = Column(Text(), nullable=False )
    cas = Column(Text())
    compound_name = Column(Text(), nullable=False )
    experimental_factor = Column(Text())
    experimental_factor_other = Column(Text())
    item_number = Column(Text())
    method_development = Column(Text())
    other = Column(Text())
    other_samp_store_temp = Column(Text())
    other_storage_condt = Column(Text())
    other_treatment = Column(Text())
    oxygen_status = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'obligate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    production_method = Column(Text())
    project = Column(Integer())
    replicate_number = Column(Integer())
    sample_link = Column(Text())
    sample_name = Column(Text())
    sample_processing = Column(Text())
    samp_store_temp = Column(Enum('fresh4', 'freshroom', 'frozen20', 'frozen80', 'other', name='SampleStoreTempEnum'))
    sampled_during = Column(UUID(), ForeignKey('SamplingActivity.id'))
    source_mat_id = Column(Text())
    storage_condition = Column(Enum('fresh', 'frozen', 'lyophilized', 'other', name='StorageConditionEnum'))
    storage_condition_other = Column(Text())
    technical_reps = Column(Integer())
    temp = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    emsl_activity = Column(Text())
    lims_barcode = Column(Text())
    
    
    external_identifiers_rel = relationship( "CommerciallyPurchasedSample_external_identifiers" )
    external_identifiers = association_proxy("external_identifiers_rel", "external_identifiers",
                                  creator=lambda x_: CommerciallyPurchasedSample_external_identifiers(external_identifiers=x_))
    

    

    def __repr__(self):
        return f"CommerciallyPurchasedSample(analysis_type={self.analysis_type},cas={self.cas},compound_name={self.compound_name},experimental_factor={self.experimental_factor},experimental_factor_other={self.experimental_factor_other},item_number={self.item_number},method_development={self.method_development},other={self.other},other_samp_store_temp={self.other_samp_store_temp},other_storage_condt={self.other_storage_condt},other_treatment={self.other_treatment},oxygen_status={self.oxygen_status},production_method={self.production_method},project={self.project},replicate_number={self.replicate_number},sample_link={self.sample_link},sample_name={self.sample_name},sample_processing={self.sample_processing},samp_store_temp={self.samp_store_temp},sampled_during={self.sampled_during},source_mat_id={self.source_mat_id},storage_condition={self.storage_condition},storage_condition_other={self.storage_condition_other},technical_reps={self.technical_reps},temp={self.temp},id={self.id},name={self.name},description={self.description},emsl_activity={self.emsl_activity},lims_barcode={self.lims_barcode},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class CultureEnvironmentalSample(Sample):
    """
    A sample containing organisms cultured from an environmental sample.
    """
    __tablename__ = 'CultureEnvironmentalSample'

    air_temp_regm = Column(Text())
    analysis_type = Column(Text(), nullable=False )
    biotic_regm = Column(Text())
    chem_administration = Column(Text())
    encoded_traits = Column(Text())
    env_broad_scale = Column(Text())
    env_local_scale = Column(Text())
    env_medium = Column(Text())
    experimental_factor = Column(Text())
    experimental_factor_other = Column(Text())
    extraction_method = Column(Text())
    filter_method = Column(Text())
    gaseous_environment = Column(Text())
    genetic_mod = Column(Text())
    growth_medium = Column(Text(), nullable=False )
    host_common_name = Column(Text(), nullable=False )
    host_spec_range = Column(Text())
    host_taxid = Column(Text(), nullable=False )
    humidity_regm = Column(Text())
    isol_growth_condt = Column(Text(), nullable=False )
    isotope_exposure = Column(Text())
    latitude = Column(Float())
    longitude = Column(Float())
    light_regm = Column(Text())
    method_development = Column(Text())
    non_microb_biomass = Column(Text())
    non_microb_biomass_method = Column(Text())
    other = Column(Text())
    other_samp_store_temp = Column(Text())
    other_storage_condt = Column(Text())
    other_treatment = Column(Text())
    oxygen_status = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'obligate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    pathogenicity = Column(Text())
    project = Column(Integer())
    propagation = Column(Text())
    ref_biomaterial = Column(Text())
    replicate_number = Column(Integer())
    biotic_relationship = Column(Enum('free_living', 'parasite', 'commensal', 'symbiont', name='BioticRelationshipEnum'))
    samp_store_temp = Column(Enum('fresh4', 'freshroom', 'frozen20', 'frozen80', 'other', name='SampleStoreTempEnum'))
    sample_link = Column(Text())
    sample_name = Column(Text())
    sample_processing = Column(Text())
    sampled_during = Column(UUID(), ForeignKey('SamplingActivity.id'))
    source_mat_id = Column(Text())
    start_date_inc = Column(Text(), nullable=False )
    storage_condition = Column(Enum('fresh', 'frozen', 'lyophilized', 'other', name='StorageConditionEnum'))
    storage_condition_other = Column(Text())
    subspecf_gen_lin = Column(Text())
    technical_reps = Column(Integer())
    trophic_level = Column(Enum('autotroph', 'carboxydotroph', 'chemoautolithotroph', 'chemoautotroph', 'chemoheterotroph', 'chemolithoautotroph', 'chemolithotroph', 'chemoorganoheterotroph', 'chemoorganotroph', 'chemosynthetic', 'chemotroph', 'copiotroph', 'diazotroph', 'facultative', 'heterotroph', 'lithoautotroph', 'lithoheterotroph', 'lithotroph', 'methanotroph', 'methylotroph', 'mixotroph', 'obligate', 'oligotroph', 'organoheterotroph', 'organotroph', 'osmotroph', 'photoheterotroph', 'photoautotroph', 'photolithoautotroph', 'photolithotroph', 'phototroph', name='TrophicLevelEnum'))
    watering_regm = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    emsl_activity = Column(Text())
    lims_barcode = Column(Text())
    
    
    external_identifiers_rel = relationship( "CultureEnvironmentalSample_external_identifiers" )
    external_identifiers = association_proxy("external_identifiers_rel", "external_identifiers",
                                  creator=lambda x_: CultureEnvironmentalSample_external_identifiers(external_identifiers=x_))
    

    

    def __repr__(self):
        return f"CultureEnvironmentalSample(air_temp_regm={self.air_temp_regm},analysis_type={self.analysis_type},biotic_regm={self.biotic_regm},chem_administration={self.chem_administration},encoded_traits={self.encoded_traits},env_broad_scale={self.env_broad_scale},env_local_scale={self.env_local_scale},env_medium={self.env_medium},experimental_factor={self.experimental_factor},experimental_factor_other={self.experimental_factor_other},extraction_method={self.extraction_method},filter_method={self.filter_method},gaseous_environment={self.gaseous_environment},genetic_mod={self.genetic_mod},growth_medium={self.growth_medium},host_common_name={self.host_common_name},host_spec_range={self.host_spec_range},host_taxid={self.host_taxid},humidity_regm={self.humidity_regm},isol_growth_condt={self.isol_growth_condt},isotope_exposure={self.isotope_exposure},latitude={self.latitude},longitude={self.longitude},light_regm={self.light_regm},method_development={self.method_development},non_microb_biomass={self.non_microb_biomass},non_microb_biomass_method={self.non_microb_biomass_method},other={self.other},other_samp_store_temp={self.other_samp_store_temp},other_storage_condt={self.other_storage_condt},other_treatment={self.other_treatment},oxygen_status={self.oxygen_status},pathogenicity={self.pathogenicity},project={self.project},propagation={self.propagation},ref_biomaterial={self.ref_biomaterial},replicate_number={self.replicate_number},biotic_relationship={self.biotic_relationship},samp_store_temp={self.samp_store_temp},sample_link={self.sample_link},sample_name={self.sample_name},sample_processing={self.sample_processing},sampled_during={self.sampled_during},source_mat_id={self.source_mat_id},start_date_inc={self.start_date_inc},storage_condition={self.storage_condition},storage_condition_other={self.storage_condition_other},subspecf_gen_lin={self.subspecf_gen_lin},technical_reps={self.technical_reps},trophic_level={self.trophic_level},watering_regm={self.watering_regm},id={self.id},name={self.name},description={self.description},emsl_activity={self.emsl_activity},lims_barcode={self.lims_barcode},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class EngineeredStrainSample(Sample):
    """
    A sample containing a strain of an organism that has been subjected to genetic engineering.

This class references a biological_entity for strain identity information (organism_name,
strain_source, modification_method, genotype_segment_*, component_*, phenotype, trait, etc.)
and carries only sample-instance-specific slots.
  
    """
    __tablename__ = 'EngineeredStrainSample'

    biological_entity_ref = Column(UUID(), ForeignKey('biological_entity.id'))
    cbi = Column(Text(), nullable=False )
    storage_condition = Column(Text(), nullable=False )
    storage_temperature = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    emsl_activity = Column(Text())
    lims_barcode = Column(Text())
    
    
    external_identifiers_rel = relationship( "EngineeredStrainSample_external_identifiers" )
    external_identifiers = association_proxy("external_identifiers_rel", "external_identifiers",
                                  creator=lambda x_: EngineeredStrainSample_external_identifiers(external_identifiers=x_))
    

    

    def __repr__(self):
        return f"EngineeredStrainSample(biological_entity_ref={self.biological_entity_ref},cbi={self.cbi},storage_condition={self.storage_condition},storage_temperature={self.storage_temperature},id={self.id},name={self.name},description={self.description},emsl_activity={self.emsl_activity},lims_barcode={self.lims_barcode},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class FieldDeployedTerraformSample(Sample):
    """
    A sample collected from a field-deployed Terraform experiment.
    """
    __tablename__ = 'FieldDeployedTerraformSample'

    air_temp_regm = Column(Text())
    analysis_type = Column(Text(), nullable=False )
    biotic_regm = Column(Text())
    chem_administration = Column(Text())
    cult_root_med = Column(Text())
    depth = Column(Text())
    encoded_traits = Column(Text())
    env_broad_scale = Column(Text())
    env_local_scale = Column(Text())
    env_medium = Column(Text())
    gaseous_environment = Column(Text())
    genetic_mod = Column(Text())
    growth_medium = Column(Text())
    host_age = Column(Text())
    host_common_name = Column(Text())
    host_dry_mass = Column(Text())
    host_genotype = Column(Text())
    host_height = Column(Text())
    host_life_stage = Column(Text())
    host_spec_range = Column(Text())
    host_taxid = Column(Text())
    host_tot_mass = Column(Text())
    host_wet_mass = Column(Text())
    humidity_regm = Column(Text())
    initiation_date_inoculation = Column(Text(), nullable=False )
    initiation_date_plant = Column(Text(), nullable=False )
    isol_growth_condt = Column(Text())
    isotope_exposure = Column(Text())
    latitude = Column(Float(), nullable=False )
    longitude = Column(Float(), nullable=False )
    light_regm = Column(Text())
    method_development = Column(Text())
    mineral_nutr_regm = Column(Text())
    misc_param = Column(Text())
    non_min_nutr_regm = Column(Text())
    other = Column(Text())
    other_samp_store_temp = Column(Text())
    other_storage_condt = Column(Text())
    other_treatment = Column(Text())
    oxygen_status = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'obligate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    plant_growth_med = Column(Text())
    plant_product = Column(Text())
    plant_sex = Column(Enum('androdioecious', 'androecious', 'androgynomonoecious', 'androgynous', 'andromonoecious', 'bisexual', 'dichogamous', 'diclinous', 'dioecious', 'gynodioecious', 'gynoecious', 'gynomonoecious', 'hermaphroditic', 'imperfect', 'monoclinous', 'monoecious', 'perfect', 'polygamodioecious', 'polygamomonoecious', 'polygamous', 'protandrous', 'protogynous', 'subandroecious', 'subdioecious', 'subgynoecious', 'synoecious', 'trimonoecious', 'trioecious', 'unisexual', name='PlantSexEnum'))
    plant_struc = Column(Enum('stem', 'leaf', 'root', 'fine_root', 'whole_plant', 'stamen', 'carpel', 'seed', 'rhizodeposits', name='PlantStructureEnum'))
    pressure = Column(Text())
    project = Column(Integer())
    propagation = Column(Text())
    redox_potential = Column(Text())
    ref_biomaterial = Column(Text())
    replicate_number = Column(Integer())
    root_cond = Column(Text())
    root_med_carbon = Column(Text())
    root_med_macronutr = Column(Text())
    root_med_micronutr = Column(Text())
    salt_regm = Column(Text())
    sample_link = Column(Text())
    sample_name = Column(Text())
    sample_processing = Column(Text())
    biotic_relationship = Column(Enum('free_living', 'parasite', 'commensal', 'symbiont', name='BioticRelationshipEnum'))
    samp_store_temp = Column(Enum('fresh4', 'freshroom', 'frozen20', 'frozen80', 'other', name='SampleStoreTempEnum'))
    sampled_during = Column(UUID(), ForeignKey('SamplingActivity.id'))
    source_mat_id = Column(Text())
    start_date_inc = Column(Text())
    storage_condition = Column(Enum('fresh', 'frozen', 'lyophilized', 'other', name='StorageConditionEnum'))
    storage_condition_other = Column(Text())
    synth_env_assembly = Column(Text(), nullable=False )
    synth_env_design = Column(Enum('pore_scale_micromodels', 'rhizochip', 'subtap', 'three_d_bioprinted_synthetic_soil_aggregates', 'pore2chip', name='SyntheticEnvironmentEnum'), nullable=False )
    synth_env_design_method = Column(Text(), nullable=False )
    synth_env_material = Column(Text(), nullable=False )
    synth_env_treatment = Column(Text(), nullable=False )
    synth_start_date = Column(Text(), nullable=False )
    technical_reps = Column(Integer())
    temp = Column(Text())
    tiss_cult_growth_med = Column(Text())
    water_content = Column(Text())
    water_content_meth = Column(Text())
    watering_regm = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    emsl_activity = Column(Text())
    lims_barcode = Column(Text())
    
    
    external_identifiers_rel = relationship( "FieldDeployedTerraformSample_external_identifiers" )
    external_identifiers = association_proxy("external_identifiers_rel", "external_identifiers",
                                  creator=lambda x_: FieldDeployedTerraformSample_external_identifiers(external_identifiers=x_))
    

    

    def __repr__(self):
        return f"FieldDeployedTerraformSample(air_temp_regm={self.air_temp_regm},analysis_type={self.analysis_type},biotic_regm={self.biotic_regm},chem_administration={self.chem_administration},cult_root_med={self.cult_root_med},depth={self.depth},encoded_traits={self.encoded_traits},env_broad_scale={self.env_broad_scale},env_local_scale={self.env_local_scale},env_medium={self.env_medium},gaseous_environment={self.gaseous_environment},genetic_mod={self.genetic_mod},growth_medium={self.growth_medium},host_age={self.host_age},host_common_name={self.host_common_name},host_dry_mass={self.host_dry_mass},host_genotype={self.host_genotype},host_height={self.host_height},host_life_stage={self.host_life_stage},host_spec_range={self.host_spec_range},host_taxid={self.host_taxid},host_tot_mass={self.host_tot_mass},host_wet_mass={self.host_wet_mass},humidity_regm={self.humidity_regm},initiation_date_inoculation={self.initiation_date_inoculation},initiation_date_plant={self.initiation_date_plant},isol_growth_condt={self.isol_growth_condt},isotope_exposure={self.isotope_exposure},latitude={self.latitude},longitude={self.longitude},light_regm={self.light_regm},method_development={self.method_development},mineral_nutr_regm={self.mineral_nutr_regm},misc_param={self.misc_param},non_min_nutr_regm={self.non_min_nutr_regm},other={self.other},other_samp_store_temp={self.other_samp_store_temp},other_storage_condt={self.other_storage_condt},other_treatment={self.other_treatment},oxygen_status={self.oxygen_status},plant_growth_med={self.plant_growth_med},plant_product={self.plant_product},plant_sex={self.plant_sex},plant_struc={self.plant_struc},pressure={self.pressure},project={self.project},propagation={self.propagation},redox_potential={self.redox_potential},ref_biomaterial={self.ref_biomaterial},replicate_number={self.replicate_number},root_cond={self.root_cond},root_med_carbon={self.root_med_carbon},root_med_macronutr={self.root_med_macronutr},root_med_micronutr={self.root_med_micronutr},salt_regm={self.salt_regm},sample_link={self.sample_link},sample_name={self.sample_name},sample_processing={self.sample_processing},biotic_relationship={self.biotic_relationship},samp_store_temp={self.samp_store_temp},sampled_during={self.sampled_during},source_mat_id={self.source_mat_id},start_date_inc={self.start_date_inc},storage_condition={self.storage_condition},storage_condition_other={self.storage_condition_other},synth_env_assembly={self.synth_env_assembly},synth_env_design={self.synth_env_design},synth_env_design_method={self.synth_env_design_method},synth_env_material={self.synth_env_material},synth_env_treatment={self.synth_env_treatment},synth_start_date={self.synth_start_date},technical_reps={self.technical_reps},temp={self.temp},tiss_cult_growth_med={self.tiss_cult_growth_med},water_content={self.water_content},water_content_meth={self.water_content_meth},watering_regm={self.watering_regm},id={self.id},name={self.name},description={self.description},emsl_activity={self.emsl_activity},lims_barcode={self.lims_barcode},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MixedCultureSample(Sample):
    """
    A sample containing multiple cultured organisms.
    """
    __tablename__ = 'MixedCultureSample'

    air_temp_regm = Column(Text())
    analysis_type = Column(Text(), nullable=False )
    biotic_regm = Column(Text())
    chem_administration = Column(Text())
    encoded_traits = Column(Text())
    experimental_factor = Column(Text())
    experimental_factor_other = Column(Text())
    extraction_method = Column(Text())
    gaseous_environment = Column(Text())
    genetic_mod = Column(Text())
    growth_medium = Column(Text(), nullable=False )
    host_common_name = Column(Text(), nullable=False )
    host_spec_range = Column(Text())
    host_taxid = Column(Text(), nullable=False )
    humidity_regm = Column(Text())
    isol_growth_condt = Column(Text(), nullable=False )
    isotope_exposure = Column(Text())
    light_regm = Column(Text())
    method_development = Column(Text())
    non_microb_biomass = Column(Text())
    other = Column(Text())
    other_samp_store_temp = Column(Text())
    other_storage_condt = Column(Text())
    other_treatment = Column(Text())
    oxygen_status = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'obligate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    pathogenicity = Column(Text())
    project = Column(Integer())
    propagation = Column(Text())
    ref_biomaterial = Column(Text())
    replicate_number = Column(Integer())
    biotic_relationship = Column(Enum('free_living', 'parasite', 'commensal', 'symbiont', name='BioticRelationshipEnum'))
    sample_link = Column(Text())
    sample_name = Column(Text())
    sample_processing = Column(Text())
    sampled_during = Column(UUID(), ForeignKey('SamplingActivity.id'))
    samp_store_temp = Column(Enum('fresh4', 'freshroom', 'frozen20', 'frozen80', 'other', name='SampleStoreTempEnum'))
    source_mat_id = Column(Text())
    specific_host = Column(Text())
    start_date_inc = Column(Text(), nullable=False )
    storage_condition = Column(Enum('fresh', 'frozen', 'lyophilized', 'other', name='StorageConditionEnum'))
    storage_condition_other = Column(Text())
    subspecf_gen_lin = Column(Text())
    technical_reps = Column(Integer())
    trophic_level = Column(Enum('autotroph', 'carboxydotroph', 'chemoautolithotroph', 'chemoautotroph', 'chemoheterotroph', 'chemolithoautotroph', 'chemolithotroph', 'chemoorganoheterotroph', 'chemoorganotroph', 'chemosynthetic', 'chemotroph', 'copiotroph', 'diazotroph', 'facultative', 'heterotroph', 'lithoautotroph', 'lithoheterotroph', 'lithotroph', 'methanotroph', 'methylotroph', 'mixotroph', 'obligate', 'oligotroph', 'organoheterotroph', 'organotroph', 'osmotroph', 'photoheterotroph', 'photoautotroph', 'photolithoautotroph', 'photolithotroph', 'phototroph', name='TrophicLevelEnum'))
    watering_regm = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    emsl_activity = Column(Text())
    lims_barcode = Column(Text())
    
    
    external_identifiers_rel = relationship( "MixedCultureSample_external_identifiers" )
    external_identifiers = association_proxy("external_identifiers_rel", "external_identifiers",
                                  creator=lambda x_: MixedCultureSample_external_identifiers(external_identifiers=x_))
    

    

    def __repr__(self):
        return f"MixedCultureSample(air_temp_regm={self.air_temp_regm},analysis_type={self.analysis_type},biotic_regm={self.biotic_regm},chem_administration={self.chem_administration},encoded_traits={self.encoded_traits},experimental_factor={self.experimental_factor},experimental_factor_other={self.experimental_factor_other},extraction_method={self.extraction_method},gaseous_environment={self.gaseous_environment},genetic_mod={self.genetic_mod},growth_medium={self.growth_medium},host_common_name={self.host_common_name},host_spec_range={self.host_spec_range},host_taxid={self.host_taxid},humidity_regm={self.humidity_regm},isol_growth_condt={self.isol_growth_condt},isotope_exposure={self.isotope_exposure},light_regm={self.light_regm},method_development={self.method_development},non_microb_biomass={self.non_microb_biomass},other={self.other},other_samp_store_temp={self.other_samp_store_temp},other_storage_condt={self.other_storage_condt},other_treatment={self.other_treatment},oxygen_status={self.oxygen_status},pathogenicity={self.pathogenicity},project={self.project},propagation={self.propagation},ref_biomaterial={self.ref_biomaterial},replicate_number={self.replicate_number},biotic_relationship={self.biotic_relationship},sample_link={self.sample_link},sample_name={self.sample_name},sample_processing={self.sample_processing},sampled_during={self.sampled_during},samp_store_temp={self.samp_store_temp},source_mat_id={self.source_mat_id},specific_host={self.specific_host},start_date_inc={self.start_date_inc},storage_condition={self.storage_condition},storage_condition_other={self.storage_condition_other},subspecf_gen_lin={self.subspecf_gen_lin},technical_reps={self.technical_reps},trophic_level={self.trophic_level},watering_regm={self.watering_regm},id={self.id},name={self.name},description={self.description},emsl_activity={self.emsl_activity},lims_barcode={self.lims_barcode},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MonetSoilSample(Sample):
    """
    A soil sample that has been collected according to the MONet soil sampling protocol. This sample type has specific slot requirements related to the MONet soil sampling method, such as infiltration rates.
    """
    __tablename__ = 'MonetSoilSample'

    agrochem_addition = Column(Text())
    bulk_elect_conductivity = Column(Text(), nullable=False )
    chem_administration = Column(Text())
    core_group = Column(Enum('A', 'B', 'C1', 'C2', 'C3', 'C4', name='MONetCoreGroupEnum'))
    depth = Column(Text(), nullable=False )
    env_broad_scale = Column(Text())
    env_local_scale = Column(Text())
    env_medium = Column(Text())
    latitude = Column(Float(), nullable=False )
    longitude = Column(Float(), nullable=False )
    lims_id = Column(Text())
    misc_param = Column(Text())
    other = Column(Text())
    other_samp_store_temp = Column(Text())
    other_storage_condt = Column(Text())
    other_treatment = Column(Text())
    project = Column(Integer())
    sample_name = Column(Text())
    samp_store_temp = Column(Enum('fresh4', 'freshroom', 'frozen20', 'frozen80', 'other', name='SampleStoreTempEnum'))
    sampled_during = Column(UUID(), ForeignKey('SamplingActivity.id'))
    sampling_set = Column(Integer(), nullable=False )
    soil_sample_type = Column(Enum('soil_core', 'surface_layer', name='SoilSampleTypeEnum'), nullable=False )
    soil_type = Column(Enum('alfisol', 'andisol', 'aridisol', 'entisol', 'gelisol', 'histosol', 'inceptisol', 'mollisol', 'oxisol', 'spodosol', 'ultisol', 'vertisol', name='SoilTypeEnum'), nullable=False )
    soil_type_meth = Column(Text(), nullable=False )
    storage_condition = Column(Enum('fresh', 'frozen', 'lyophilized', 'other', name='StorageConditionEnum'))
    storage_condition_other = Column(Text())
    temp = Column(Text(), nullable=False )
    water_content = Column(Text(), nullable=False )
    water_content_meth = Column(Text())
    watering_regm = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    emsl_activity = Column(Text())
    lims_barcode = Column(Text())
    
    
    external_identifiers_rel = relationship( "MonetSoilSample_external_identifiers" )
    external_identifiers = association_proxy("external_identifiers_rel", "external_identifiers",
                                  creator=lambda x_: MonetSoilSample_external_identifiers(external_identifiers=x_))
    

    

    def __repr__(self):
        return f"MonetSoilSample(agrochem_addition={self.agrochem_addition},bulk_elect_conductivity={self.bulk_elect_conductivity},chem_administration={self.chem_administration},core_group={self.core_group},depth={self.depth},env_broad_scale={self.env_broad_scale},env_local_scale={self.env_local_scale},env_medium={self.env_medium},latitude={self.latitude},longitude={self.longitude},lims_id={self.lims_id},misc_param={self.misc_param},other={self.other},other_samp_store_temp={self.other_samp_store_temp},other_storage_condt={self.other_storage_condt},other_treatment={self.other_treatment},project={self.project},sample_name={self.sample_name},samp_store_temp={self.samp_store_temp},sampled_during={self.sampled_during},sampling_set={self.sampling_set},soil_sample_type={self.soil_sample_type},soil_type={self.soil_type},soil_type_meth={self.soil_type_meth},storage_condition={self.storage_condition},storage_condition_other={self.storage_condition_other},temp={self.temp},water_content={self.water_content},water_content_meth={self.water_content_meth},watering_regm={self.watering_regm},id={self.id},name={self.name},description={self.description},emsl_activity={self.emsl_activity},lims_barcode={self.lims_barcode},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class OtherUndescribedSample(Sample):
    """
    A sample that does not fit into any of the other described sample types.
    """
    __tablename__ = 'OtherUndescribedSample'

    agrochem_addition = Column(Text())
    air_temp_regm = Column(Text())
    al_sat = Column(Text())
    al_sat_meth = Column(Text())
    alkalinity = Column(Text())
    alkalinity_method = Column(Text())
    alkyl_diethers = Column(Text())
    aminopept_act = Column(Text())
    ammonium = Column(Text())
    analysis_type = Column(Text(), nullable=False )
    ances_data = Column(Text())
    antibiotic_regm = Column(Text())
    bac_prod = Column(Text())
    bac_resp = Column(Text())
    bacteria_carb_prod = Column(Text())
    biochem_oxygen_dem = Column(Text())
    biol_stat = Column(Enum('wild', 'natural', 'semi-natural', 'inbred line', "breeder's line", 'hybrid', 'clonal selection', 'mutant', name='BiolStatEnum'))
    biotic_regm = Column(Text())
    bishomohopanol = Column(Text())
    bromide = Column(Text())
    bulk_elect_conductivity = Column(Text())
    calcium = Column(Text())
    carb_dioxide = Column(Text())
    carb_monoxide = Column(Text())
    carb_nitro_ratio = Column(Text())
    cas = Column(Text())
    chem_administration = Column(Text())
    chem_mutagen = Column(Text())
    chem_oxygen_dem = Column(Text())
    chloride = Column(Text())
    chlorophyll = Column(Text())
    compound_name = Column(Text())
    conduc = Column(Text())
    density = Column(Text())
    depth = Column(Text())
    diether_lipids = Column(Text())
    diss_carb_dioxide = Column(Text())
    diss_hydrogen = Column(Text())
    diss_inorg_carb = Column(Text())
    diss_inorg_nitro = Column(Text())
    diss_inorg_phosp = Column(Text())
    diss_org_carb = Column(Text())
    diss_org_nitro = Column(Text())
    diss_oxygen = Column(Text())
    down_par = Column(Text())
    efficiency_percent = Column(Text())
    emulsions = Column(Text())
    encoded_traits = Column(Text())
    env_broad_scale = Column(Text())
    env_local_scale = Column(Text())
    env_medium = Column(Text())
    experimental_factor = Column(Text())
    experimental_factor_other = Column(Text())
    extraction_method = Column(Text())
    fertilizer_regm = Column(Text())
    filter_method = Column(Text())
    fluor = Column(Text())
    fungicide_regm = Column(Text())
    gaseous_environment = Column(Text())
    gaseous_substances = Column(Text())
    genetic_mod = Column(Text())
    glucosidase_act = Column(Text())
    gravity = Column(Text())
    growth_habit = Column(Enum('erect', 'semi-erect', 'spreading', 'prostrate', name='GrowthHabitEnum'))
    growth_hormone_regm = Column(Text())
    growth_medium = Column(Text())
    heavy_metals = Column(Text())
    heavy_metals_meth = Column(Text())
    herbicide_regm = Column(Text())
    host_age = Column(Text())
    host_common_name = Column(Text())
    host_disease_stat = Column(Text())
    host_dry_mass = Column(Text())
    host_height = Column(Text())
    host_infra_spec_name = Column(Text())
    host_infra_spec_rank = Column(Text())
    host_length = Column(Text())
    host_life_stage = Column(Text())
    host_phenotype = Column(Text())
    host_spec_range = Column(Text())
    host_symbiont = Column(Text())
    host_taxid = Column(Text())
    host_tot_mass = Column(Text())
    host_wet_mass = Column(Text())
    humidity_regm = Column(Text())
    indust_eff_percent = Column(Text())
    inorg_particles = Column(Text())
    isol_growth_condt = Column(Text())
    isotope_exposure = Column(Text())
    item_number = Column(Text())
    latitude = Column(Float(), nullable=False )
    longitude = Column(Float(), nullable=False )
    light_intensity = Column(Text())
    light_regm = Column(Text())
    link_addit_analys = Column(Text())
    magnesium = Column(Text())
    mean_frict_vel = Column(Text())
    mean_peak_frict_vel = Column(Text())
    mechanical_damage = Column(Text())
    method_development = Column(Text())
    methane = Column(Text())
    micro_biomass_C_meth = Column(Text())
    micro_biomass_N_meth = Column(Text())
    microbial_biomass = Column(Text())
    microbial_biomass_c = Column(Text())
    microbial_biomass_n = Column(Text())
    microbial_biomass_meth = Column(Text())
    mineral_nutr_regm = Column(Text())
    misc_param = Column(Text())
    n_alkanes = Column(Text())
    nitrate = Column(Text())
    nitrite = Column(Text())
    nitro = Column(Text())
    non_microb_biomass = Column(Text())
    non_microb_biomass_method = Column(Text())
    non_min_nutr_regm = Column(Text())
    org_carb = Column(Text())
    org_matter = Column(Text())
    org_nitro = Column(Text())
    org_nitro_method = Column(Text())
    org_particles = Column(Text())
    organism_count = Column(Text())
    other = Column(Text())
    other_samp_store_temp = Column(Text())
    other_treatment = Column(Text())
    oxygen = Column(Text())
    oxygen_status = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'obligate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    part_org_carb = Column(Text())
    part_org_nitro = Column(Text())
    particle_class = Column(Text())
    pathogenicity = Column(Text())
    perturbation = Column(Text())
    pesticide_regm = Column(Text())
    petroleum_hydrocarb = Column(Text())
    ph = Column(Float())
    ph_meth = Column(Text())
    ph_regm = Column(Text())
    phaeopigments = Column(Text())
    phosphate = Column(Text())
    phosplipid_fatt_acid = Column(Text())
    photochemical_exposure = Column(Enum('ultraviolet', 'visible light', 'infrared', name='PhotochemicalExposureEnum'))
    photon_flux = Column(Text())
    porosity = Column(Text())
    potassium = Column(Text())
    pre_treatment = Column(Text())
    pressure = Column(Text())
    pressure_control = Column(Text())
    primary_prod = Column(Text())
    primary_treatment = Column(Text())
    priority_order = Column(Float())
    production_method = Column(Text())
    project = Column(Integer())
    propagation = Column(Text())
    radiation_regm = Column(Text())
    rainfall_regm = Column(Text())
    reactor_type = Column(Text())
    redox_potential = Column(Text())
    ref_biomaterial = Column(Text())
    replicate_number = Column(Integer())
    salinity = Column(Text())
    salinity_method = Column(Text())
    salt_regm = Column(Text())
    biotic_relationship = Column(Enum('free_living', 'parasite', 'commensal', 'symbiont', name='BioticRelationshipEnum'))
    samp_capt_status = Column(Text())
    samp_dis_stage = Column(Text())
    samp_store_temp = Column(Enum('fresh4', 'freshroom', 'frozen20', 'frozen80', 'other', name='SampleStoreTempEnum'))
    sample_link = Column(Text())
    sample_name = Column(Text())
    sample_processing = Column(Text())
    sample_type = Column(Text(), nullable=False )
    sampled_during = Column(UUID(), ForeignKey('SamplingActivity.id'))
    season_environment = Column(Text())
    secondary_treatment = Column(Text())
    sewage_type = Column(Text())
    sieving = Column(Text())
    silicate = Column(Text())
    size_frac_low = Column(Text())
    size_frac_up = Column(Text())
    sludge_retent_time = Column(Text())
    sodium = Column(Text())
    solar_irradiance = Column(Text())
    soluble_inorg_mat = Column(Text())
    soluble_org_mat = Column(Text())
    soluble_react_phosp = Column(Text())
    source_mat_id = Column(Text())
    standing_water_regm = Column(Text())
    start_date_inc = Column(Text())
    storage_condition = Column(Enum('fresh', 'frozen', 'lyophilized', 'other', name='StorageConditionEnum'))
    storage_condition_other = Column(Text())
    subspecf_gen_lin = Column(Text())
    sulfate = Column(Text())
    sulfide = Column(Text())
    suspend_part_matter = Column(Text())
    suspend_solids = Column(Text())
    synth_instrument = Column(Text())
    synth_process = Column(Text())
    synth_reagents = Column(Text())
    technical_reps = Column(Integer())
    temp = Column(Text())
    temperature_exposure = Column(Text())
    tertiary_treatment = Column(Text())
    tidal_stage = Column(Enum('low_tide', 'high_tide', 'ebb_tide', 'flood_tide', name='TidalStageEnum'))
    tiss_cult_growth_med = Column(Text())
    tot_carb = Column(Text())
    tot_depth_water_col = Column(Text())
    tot_diss_nitro = Column(Text())
    tot_inorg_nitro = Column(Text())
    tot_nitro = Column(Text())
    tot_nitro_cont_meth = Column(Text())
    tot_nitro_content = Column(Text())
    tot_org_c_meth = Column(Text())
    tot_org_carb = Column(Text())
    tot_part_carb = Column(Text())
    tot_phosp = Column(Text())
    tot_phosphate = Column(Text())
    trophic_level = Column(Enum('autotroph', 'carboxydotroph', 'chemoautolithotroph', 'chemoautotroph', 'chemoheterotroph', 'chemolithoautotroph', 'chemolithotroph', 'chemoorganoheterotroph', 'chemoorganotroph', 'chemosynthetic', 'chemotroph', 'copiotroph', 'diazotroph', 'facultative', 'heterotroph', 'lithoautotroph', 'lithoheterotroph', 'lithotroph', 'methanotroph', 'methylotroph', 'mixotroph', 'obligate', 'oligotroph', 'organoheterotroph', 'organotroph', 'osmotroph', 'photoheterotroph', 'photoautotroph', 'photolithoautotroph', 'photolithotroph', 'phototroph', name='TrophicLevelEnum'))
    turbidity = Column(Text())
    volatile_org_comp = Column(Text())
    wastewater_type = Column(Text())
    water_content = Column(Text())
    water_current = Column(Text())
    water_temp_regm = Column(Text())
    watering_regm = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    emsl_activity = Column(Text())
    lims_barcode = Column(Text())
    
    
    external_identifiers_rel = relationship( "OtherUndescribedSample_external_identifiers" )
    external_identifiers = association_proxy("external_identifiers_rel", "external_identifiers",
                                  creator=lambda x_: OtherUndescribedSample_external_identifiers(external_identifiers=x_))
    

    

    def __repr__(self):
        return f"OtherUndescribedSample(agrochem_addition={self.agrochem_addition},air_temp_regm={self.air_temp_regm},al_sat={self.al_sat},al_sat_meth={self.al_sat_meth},alkalinity={self.alkalinity},alkalinity_method={self.alkalinity_method},alkyl_diethers={self.alkyl_diethers},aminopept_act={self.aminopept_act},ammonium={self.ammonium},analysis_type={self.analysis_type},ances_data={self.ances_data},antibiotic_regm={self.antibiotic_regm},bac_prod={self.bac_prod},bac_resp={self.bac_resp},bacteria_carb_prod={self.bacteria_carb_prod},biochem_oxygen_dem={self.biochem_oxygen_dem},biol_stat={self.biol_stat},biotic_regm={self.biotic_regm},bishomohopanol={self.bishomohopanol},bromide={self.bromide},bulk_elect_conductivity={self.bulk_elect_conductivity},calcium={self.calcium},carb_dioxide={self.carb_dioxide},carb_monoxide={self.carb_monoxide},carb_nitro_ratio={self.carb_nitro_ratio},cas={self.cas},chem_administration={self.chem_administration},chem_mutagen={self.chem_mutagen},chem_oxygen_dem={self.chem_oxygen_dem},chloride={self.chloride},chlorophyll={self.chlorophyll},compound_name={self.compound_name},conduc={self.conduc},density={self.density},depth={self.depth},diether_lipids={self.diether_lipids},diss_carb_dioxide={self.diss_carb_dioxide},diss_hydrogen={self.diss_hydrogen},diss_inorg_carb={self.diss_inorg_carb},diss_inorg_nitro={self.diss_inorg_nitro},diss_inorg_phosp={self.diss_inorg_phosp},diss_org_carb={self.diss_org_carb},diss_org_nitro={self.diss_org_nitro},diss_oxygen={self.diss_oxygen},down_par={self.down_par},efficiency_percent={self.efficiency_percent},emulsions={self.emulsions},encoded_traits={self.encoded_traits},env_broad_scale={self.env_broad_scale},env_local_scale={self.env_local_scale},env_medium={self.env_medium},experimental_factor={self.experimental_factor},experimental_factor_other={self.experimental_factor_other},extraction_method={self.extraction_method},fertilizer_regm={self.fertilizer_regm},filter_method={self.filter_method},fluor={self.fluor},fungicide_regm={self.fungicide_regm},gaseous_environment={self.gaseous_environment},gaseous_substances={self.gaseous_substances},genetic_mod={self.genetic_mod},glucosidase_act={self.glucosidase_act},gravity={self.gravity},growth_habit={self.growth_habit},growth_hormone_regm={self.growth_hormone_regm},growth_medium={self.growth_medium},heavy_metals={self.heavy_metals},heavy_metals_meth={self.heavy_metals_meth},herbicide_regm={self.herbicide_regm},host_age={self.host_age},host_common_name={self.host_common_name},host_disease_stat={self.host_disease_stat},host_dry_mass={self.host_dry_mass},host_height={self.host_height},host_infra_spec_name={self.host_infra_spec_name},host_infra_spec_rank={self.host_infra_spec_rank},host_length={self.host_length},host_life_stage={self.host_life_stage},host_phenotype={self.host_phenotype},host_spec_range={self.host_spec_range},host_symbiont={self.host_symbiont},host_taxid={self.host_taxid},host_tot_mass={self.host_tot_mass},host_wet_mass={self.host_wet_mass},humidity_regm={self.humidity_regm},indust_eff_percent={self.indust_eff_percent},inorg_particles={self.inorg_particles},isol_growth_condt={self.isol_growth_condt},isotope_exposure={self.isotope_exposure},item_number={self.item_number},latitude={self.latitude},longitude={self.longitude},light_intensity={self.light_intensity},light_regm={self.light_regm},link_addit_analys={self.link_addit_analys},magnesium={self.magnesium},mean_frict_vel={self.mean_frict_vel},mean_peak_frict_vel={self.mean_peak_frict_vel},mechanical_damage={self.mechanical_damage},method_development={self.method_development},methane={self.methane},micro_biomass_C_meth={self.micro_biomass_C_meth},micro_biomass_N_meth={self.micro_biomass_N_meth},microbial_biomass={self.microbial_biomass},microbial_biomass_c={self.microbial_biomass_c},microbial_biomass_n={self.microbial_biomass_n},microbial_biomass_meth={self.microbial_biomass_meth},mineral_nutr_regm={self.mineral_nutr_regm},misc_param={self.misc_param},n_alkanes={self.n_alkanes},nitrate={self.nitrate},nitrite={self.nitrite},nitro={self.nitro},non_microb_biomass={self.non_microb_biomass},non_microb_biomass_method={self.non_microb_biomass_method},non_min_nutr_regm={self.non_min_nutr_regm},org_carb={self.org_carb},org_matter={self.org_matter},org_nitro={self.org_nitro},org_nitro_method={self.org_nitro_method},org_particles={self.org_particles},organism_count={self.organism_count},other={self.other},other_samp_store_temp={self.other_samp_store_temp},other_treatment={self.other_treatment},oxygen={self.oxygen},oxygen_status={self.oxygen_status},part_org_carb={self.part_org_carb},part_org_nitro={self.part_org_nitro},particle_class={self.particle_class},pathogenicity={self.pathogenicity},perturbation={self.perturbation},pesticide_regm={self.pesticide_regm},petroleum_hydrocarb={self.petroleum_hydrocarb},ph={self.ph},ph_meth={self.ph_meth},ph_regm={self.ph_regm},phaeopigments={self.phaeopigments},phosphate={self.phosphate},phosplipid_fatt_acid={self.phosplipid_fatt_acid},photochemical_exposure={self.photochemical_exposure},photon_flux={self.photon_flux},porosity={self.porosity},potassium={self.potassium},pre_treatment={self.pre_treatment},pressure={self.pressure},pressure_control={self.pressure_control},primary_prod={self.primary_prod},primary_treatment={self.primary_treatment},priority_order={self.priority_order},production_method={self.production_method},project={self.project},propagation={self.propagation},radiation_regm={self.radiation_regm},rainfall_regm={self.rainfall_regm},reactor_type={self.reactor_type},redox_potential={self.redox_potential},ref_biomaterial={self.ref_biomaterial},replicate_number={self.replicate_number},salinity={self.salinity},salinity_method={self.salinity_method},salt_regm={self.salt_regm},biotic_relationship={self.biotic_relationship},samp_capt_status={self.samp_capt_status},samp_dis_stage={self.samp_dis_stage},samp_store_temp={self.samp_store_temp},sample_link={self.sample_link},sample_name={self.sample_name},sample_processing={self.sample_processing},sample_type={self.sample_type},sampled_during={self.sampled_during},season_environment={self.season_environment},secondary_treatment={self.secondary_treatment},sewage_type={self.sewage_type},sieving={self.sieving},silicate={self.silicate},size_frac_low={self.size_frac_low},size_frac_up={self.size_frac_up},sludge_retent_time={self.sludge_retent_time},sodium={self.sodium},solar_irradiance={self.solar_irradiance},soluble_inorg_mat={self.soluble_inorg_mat},soluble_org_mat={self.soluble_org_mat},soluble_react_phosp={self.soluble_react_phosp},source_mat_id={self.source_mat_id},standing_water_regm={self.standing_water_regm},start_date_inc={self.start_date_inc},storage_condition={self.storage_condition},storage_condition_other={self.storage_condition_other},subspecf_gen_lin={self.subspecf_gen_lin},sulfate={self.sulfate},sulfide={self.sulfide},suspend_part_matter={self.suspend_part_matter},suspend_solids={self.suspend_solids},synth_instrument={self.synth_instrument},synth_process={self.synth_process},synth_reagents={self.synth_reagents},technical_reps={self.technical_reps},temp={self.temp},temperature_exposure={self.temperature_exposure},tertiary_treatment={self.tertiary_treatment},tidal_stage={self.tidal_stage},tiss_cult_growth_med={self.tiss_cult_growth_med},tot_carb={self.tot_carb},tot_depth_water_col={self.tot_depth_water_col},tot_diss_nitro={self.tot_diss_nitro},tot_inorg_nitro={self.tot_inorg_nitro},tot_nitro={self.tot_nitro},tot_nitro_cont_meth={self.tot_nitro_cont_meth},tot_nitro_content={self.tot_nitro_content},tot_org_c_meth={self.tot_org_c_meth},tot_org_carb={self.tot_org_carb},tot_part_carb={self.tot_part_carb},tot_phosp={self.tot_phosp},tot_phosphate={self.tot_phosphate},trophic_level={self.trophic_level},turbidity={self.turbidity},volatile_org_comp={self.volatile_org_comp},wastewater_type={self.wastewater_type},water_content={self.water_content},water_current={self.water_current},water_temp_regm={self.water_temp_regm},watering_regm={self.watering_regm},id={self.id},name={self.name},description={self.description},emsl_activity={self.emsl_activity},lims_barcode={self.lims_barcode},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class PlantSample(Sample):
    """
    A sample containing plant material.
    """
    __tablename__ = 'PlantSample'

    air_temp_regm = Column(Text())
    ances_data = Column(Text())
    analysis_type = Column(Text(), nullable=False )
    biol_stat = Column(Enum('wild', 'natural', 'semi-natural', 'inbred line', "breeder's line", 'hybrid', 'clonal selection', 'mutant', name='BiolStatEnum'))
    biotic_regm = Column(Text())
    chem_administration = Column(Text())
    chem_mutagen = Column(Text())
    env_broad_scale = Column(Text())
    env_local_scale = Column(Text())
    env_medium = Column(Text())
    experimental_factor = Column(Text())
    experimental_factor_other = Column(Text())
    extraction_method = Column(Text())
    fertilizer_regm = Column(Text())
    fungicide_regm = Column(Text())
    gaseous_environment = Column(Text())
    genetic_mod = Column(Text())
    gravity = Column(Text())
    growth_habit = Column(Enum('erect', 'semi-erect', 'spreading', 'prostrate', name='GrowthHabitEnum'))
    growth_hormone_regm = Column(Text())
    herbicide_regm = Column(Text())
    host_height = Column(Text())
    host_length = Column(Text())
    host_life_stage = Column(Text())
    humidity_regm = Column(Text())
    isotope_exposure = Column(Text())
    latitude = Column(Float(), nullable=False )
    longitude = Column(Float(), nullable=False )
    light_regm = Column(Text())
    mechanical_damage = Column(Text())
    method_development = Column(Text())
    mineral_nutr_regm = Column(Text())
    misc_param = Column(Text())
    non_microb_biomass = Column(Text())
    non_microb_biomass_method = Column(Text())
    non_min_nutr_regm = Column(Text())
    other = Column(Text())
    other_samp_store_temp = Column(Text())
    other_storage_condt = Column(Text())
    other_treatment = Column(Text())
    pesticide_regm = Column(Text())
    ph_regm = Column(Text())
    plant_age = Column(Text())
    plant_common_name = Column(Text(), nullable=False )
    plant_disease_stat = Column(Text())
    plant_dry_mass = Column(Text())
    plant_genotype = Column(Text())
    plant_growth_med = Column(Text())
    plant_sex = Column(Enum('androdioecious', 'androecious', 'androgynomonoecious', 'androgynous', 'andromonoecious', 'bisexual', 'dichogamous', 'diclinous', 'dioecious', 'gynodioecious', 'gynoecious', 'gynomonoecious', 'hermaphroditic', 'imperfect', 'monoclinous', 'monoecious', 'perfect', 'polygamodioecious', 'polygamomonoecious', 'polygamous', 'protandrous', 'protogynous', 'subandroecious', 'subdioecious', 'subgynoecious', 'synoecious', 'trimonoecious', 'trioecious', 'unisexual', name='PlantSexEnum'))
    plant_struc = Column(Enum('stem', 'leaf', 'root', 'fine_root', 'whole_plant', 'stamen', 'carpel', 'seed', 'rhizodeposits', name='PlantStructureEnum'), nullable=False )
    plant_taxid = Column(Text(), nullable=False )
    plant_wet_mass = Column(Text())
    project = Column(Integer())
    rainfall_regm = Column(Text())
    replicate_number = Column(Integer())
    root_cond = Column(Text())
    root_med_carbon = Column(Text())
    root_med_macronutr = Column(Text())
    root_med_micronutr = Column(Text())
    root_med_ph = Column(Float())
    root_med_regl = Column(Text())
    root_med_solid = Column(Text())
    root_med_suppl = Column(Text())
    salinity = Column(Text())
    salinity_method = Column(Text())
    salt_regm = Column(Text())
    sample_link = Column(Text())
    sample_name = Column(Text())
    sample_processing = Column(Text())
    samp_store_temp = Column(Enum('fresh4', 'freshroom', 'frozen20', 'frozen80', 'other', name='SampleStoreTempEnum'))
    sampled_during = Column(UUID(), ForeignKey('SamplingActivity.id'))
    source_mat_id = Column(Text())
    standing_water_regm = Column(Text())
    start_date_inc = Column(Text())
    storage_condition = Column(Enum('fresh', 'frozen', 'lyophilized', 'other', name='StorageConditionEnum'))
    storage_condition_other = Column(Text())
    technical_reps = Column(Integer())
    temp = Column(Text())
    water_temp_regm = Column(Text())
    watering_regm = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    emsl_activity = Column(Text())
    lims_barcode = Column(Text())
    
    
    external_identifiers_rel = relationship( "PlantSample_external_identifiers" )
    external_identifiers = association_proxy("external_identifiers_rel", "external_identifiers",
                                  creator=lambda x_: PlantSample_external_identifiers(external_identifiers=x_))
    

    

    def __repr__(self):
        return f"PlantSample(air_temp_regm={self.air_temp_regm},ances_data={self.ances_data},analysis_type={self.analysis_type},biol_stat={self.biol_stat},biotic_regm={self.biotic_regm},chem_administration={self.chem_administration},chem_mutagen={self.chem_mutagen},env_broad_scale={self.env_broad_scale},env_local_scale={self.env_local_scale},env_medium={self.env_medium},experimental_factor={self.experimental_factor},experimental_factor_other={self.experimental_factor_other},extraction_method={self.extraction_method},fertilizer_regm={self.fertilizer_regm},fungicide_regm={self.fungicide_regm},gaseous_environment={self.gaseous_environment},genetic_mod={self.genetic_mod},gravity={self.gravity},growth_habit={self.growth_habit},growth_hormone_regm={self.growth_hormone_regm},herbicide_regm={self.herbicide_regm},host_height={self.host_height},host_length={self.host_length},host_life_stage={self.host_life_stage},humidity_regm={self.humidity_regm},isotope_exposure={self.isotope_exposure},latitude={self.latitude},longitude={self.longitude},light_regm={self.light_regm},mechanical_damage={self.mechanical_damage},method_development={self.method_development},mineral_nutr_regm={self.mineral_nutr_regm},misc_param={self.misc_param},non_microb_biomass={self.non_microb_biomass},non_microb_biomass_method={self.non_microb_biomass_method},non_min_nutr_regm={self.non_min_nutr_regm},other={self.other},other_samp_store_temp={self.other_samp_store_temp},other_storage_condt={self.other_storage_condt},other_treatment={self.other_treatment},pesticide_regm={self.pesticide_regm},ph_regm={self.ph_regm},plant_age={self.plant_age},plant_common_name={self.plant_common_name},plant_disease_stat={self.plant_disease_stat},plant_dry_mass={self.plant_dry_mass},plant_genotype={self.plant_genotype},plant_growth_med={self.plant_growth_med},plant_sex={self.plant_sex},plant_struc={self.plant_struc},plant_taxid={self.plant_taxid},plant_wet_mass={self.plant_wet_mass},project={self.project},rainfall_regm={self.rainfall_regm},replicate_number={self.replicate_number},root_cond={self.root_cond},root_med_carbon={self.root_med_carbon},root_med_macronutr={self.root_med_macronutr},root_med_micronutr={self.root_med_micronutr},root_med_ph={self.root_med_ph},root_med_regl={self.root_med_regl},root_med_solid={self.root_med_solid},root_med_suppl={self.root_med_suppl},salinity={self.salinity},salinity_method={self.salinity_method},salt_regm={self.salt_regm},sample_link={self.sample_link},sample_name={self.sample_name},sample_processing={self.sample_processing},samp_store_temp={self.samp_store_temp},sampled_during={self.sampled_during},source_mat_id={self.source_mat_id},standing_water_regm={self.standing_water_regm},start_date_inc={self.start_date_inc},storage_condition={self.storage_condition},storage_condition_other={self.storage_condition_other},technical_reps={self.technical_reps},temp={self.temp},water_temp_regm={self.water_temp_regm},watering_regm={self.watering_regm},id={self.id},name={self.name},description={self.description},emsl_activity={self.emsl_activity},lims_barcode={self.lims_barcode},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class PureCultureSample(Sample):
    """
    A sample of a culture containing a single organism.
    """
    __tablename__ = 'PureCultureSample'

    air_temp_regm = Column(Text())
    analysis_type = Column(Text(), nullable=False )
    biotic_regm = Column(Text())
    chem_administration = Column(Text())
    encoded_traits = Column(Text())
    env_broad_scale = Column(Text())
    env_local_scale = Column(Text())
    env_medium = Column(Text())
    experimental_factor = Column(Text())
    experimental_factor_other = Column(Text())
    extraction_method = Column(Text())
    filter_method = Column(Text())
    gaseous_environment = Column(Text())
    genetic_mod = Column(Text())
    growth_medium = Column(Text(), nullable=False )
    host_common_name = Column(Text(), nullable=False )
    host_spec_range = Column(Text())
    host_taxid = Column(Text(), nullable=False )
    humidity_regm = Column(Text())
    isol_growth_condt = Column(Text(), nullable=False )
    isotope_exposure = Column(Text())
    light_regm = Column(Text())
    method_development = Column(Text())
    non_microb_biomass = Column(Text())
    non_microb_biomass_method = Column(Text())
    other = Column(Text())
    other_samp_store_temp = Column(Text())
    other_storage_condt = Column(Text())
    other_treatment = Column(Text())
    oxygen_status = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'obligate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    pathogenicity = Column(Text())
    project = Column(Integer())
    propagation = Column(Text())
    ref_biomaterial = Column(Text())
    replicate_number = Column(Integer())
    biotic_relationship = Column(Enum('free_living', 'parasite', 'commensal', 'symbiont', name='BioticRelationshipEnum'))
    samp_store_temp = Column(Enum('fresh4', 'freshroom', 'frozen20', 'frozen80', 'other', name='SampleStoreTempEnum'))
    sample_link = Column(Text())
    sample_name = Column(Text())
    sample_processing = Column(Text())
    sampled_during = Column(UUID(), ForeignKey('SamplingActivity.id'))
    source_mat_id = Column(Text())
    start_date_inc = Column(Text(), nullable=False )
    storage_condition = Column(Enum('fresh', 'frozen', 'lyophilized', 'other', name='StorageConditionEnum'))
    storage_condition_other = Column(Text())
    subspecf_gen_lin = Column(Text())
    technical_reps = Column(Integer())
    trophic_level = Column(Enum('autotroph', 'carboxydotroph', 'chemoautolithotroph', 'chemoautotroph', 'chemoheterotroph', 'chemolithoautotroph', 'chemolithotroph', 'chemoorganoheterotroph', 'chemoorganotroph', 'chemosynthetic', 'chemotroph', 'copiotroph', 'diazotroph', 'facultative', 'heterotroph', 'lithoautotroph', 'lithoheterotroph', 'lithotroph', 'methanotroph', 'methylotroph', 'mixotroph', 'obligate', 'oligotroph', 'organoheterotroph', 'organotroph', 'osmotroph', 'photoheterotroph', 'photoautotroph', 'photolithoautotroph', 'photolithotroph', 'phototroph', name='TrophicLevelEnum'))
    watering_regm = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    emsl_activity = Column(Text())
    lims_barcode = Column(Text())
    
    
    external_identifiers_rel = relationship( "PureCultureSample_external_identifiers" )
    external_identifiers = association_proxy("external_identifiers_rel", "external_identifiers",
                                  creator=lambda x_: PureCultureSample_external_identifiers(external_identifiers=x_))
    

    

    def __repr__(self):
        return f"PureCultureSample(air_temp_regm={self.air_temp_regm},analysis_type={self.analysis_type},biotic_regm={self.biotic_regm},chem_administration={self.chem_administration},encoded_traits={self.encoded_traits},env_broad_scale={self.env_broad_scale},env_local_scale={self.env_local_scale},env_medium={self.env_medium},experimental_factor={self.experimental_factor},experimental_factor_other={self.experimental_factor_other},extraction_method={self.extraction_method},filter_method={self.filter_method},gaseous_environment={self.gaseous_environment},genetic_mod={self.genetic_mod},growth_medium={self.growth_medium},host_common_name={self.host_common_name},host_spec_range={self.host_spec_range},host_taxid={self.host_taxid},humidity_regm={self.humidity_regm},isol_growth_condt={self.isol_growth_condt},isotope_exposure={self.isotope_exposure},light_regm={self.light_regm},method_development={self.method_development},non_microb_biomass={self.non_microb_biomass},non_microb_biomass_method={self.non_microb_biomass_method},other={self.other},other_samp_store_temp={self.other_samp_store_temp},other_storage_condt={self.other_storage_condt},other_treatment={self.other_treatment},oxygen_status={self.oxygen_status},pathogenicity={self.pathogenicity},project={self.project},propagation={self.propagation},ref_biomaterial={self.ref_biomaterial},replicate_number={self.replicate_number},biotic_relationship={self.biotic_relationship},samp_store_temp={self.samp_store_temp},sample_link={self.sample_link},sample_name={self.sample_name},sample_processing={self.sample_processing},sampled_during={self.sampled_during},source_mat_id={self.source_mat_id},start_date_inc={self.start_date_inc},storage_condition={self.storage_condition},storage_condition_other={self.storage_condition_other},subspecf_gen_lin={self.subspecf_gen_lin},technical_reps={self.technical_reps},trophic_level={self.trophic_level},watering_regm={self.watering_regm},id={self.id},name={self.name},description={self.description},emsl_activity={self.emsl_activity},lims_barcode={self.lims_barcode},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SedimentSample(Sample):
    """
    A sample of sediment collected from the environment.
    """
    __tablename__ = 'SedimentSample'

    air_temp_regm = Column(Text())
    alkalinity = Column(Text())
    alkalinity_method = Column(Text())
    alkyl_diethers = Column(Text())
    aminopept_act = Column(Text())
    ammonium = Column(Text())
    analysis_type = Column(Text(), nullable=False )
    bacteria_carb_prod = Column(Text())
    biotic_regm = Column(Text())
    bishomohopanol = Column(Text())
    bromide = Column(Text())
    calcium = Column(Text())
    carb_nitro_ratio = Column(Text())
    chem_administration = Column(Text())
    chloride = Column(Text())
    chlorophyll = Column(Text())
    density = Column(Text())
    depth = Column(Text(), nullable=False )
    diether_lipids = Column(Text())
    diss_carb_dioxide = Column(Text())
    diss_hydrogen = Column(Text())
    diss_inorg_carb = Column(Text())
    diss_org_carb = Column(Text())
    diss_org_nitro = Column(Text())
    diss_oxygen = Column(Text())
    env_broad_scale = Column(Text())
    env_local_scale = Column(Text())
    env_medium = Column(Text())
    experimental_factor = Column(Text())
    experimental_factor_other = Column(Text())
    extraction_method = Column(Text())
    gaseous_environment = Column(Text())
    glucosidase_act = Column(Text())
    humidity_regm = Column(Text())
    isotope_exposure = Column(Text())
    latitude = Column(Float(), nullable=False )
    longitude = Column(Float(), nullable=False )
    light_regm = Column(Text())
    magnesium = Column(Text())
    mean_frict_vel = Column(Text())
    mean_peak_frict_vel = Column(Text())
    methane = Column(Text())
    method_development = Column(Text())
    micro_biomass_c_meth = Column(Text())
    micro_biomass_n_meth = Column(Text())
    microbial_biomass = Column(Text())
    microbial_biomass_c = Column(Text())
    microbial_biomass_meth = Column(Text())
    microbial_biomass_n = Column(Text())
    misc_param = Column(Text())
    n_alkanes = Column(Text())
    nitrate = Column(Text())
    nitrite = Column(Text())
    nitro = Column(Text())
    non_microb_biomass = Column(Text())
    non_microb_biomass_method = Column(Text())
    org_carb = Column(Text())
    org_matter = Column(Text())
    org_nitro = Column(Text())
    org_nitro_method = Column(Text())
    other = Column(Text())
    other_samp_store_temp = Column(Text())
    other_storage_condt = Column(Text())
    other_treatment = Column(Text())
    oxygen_status = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'obligate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    part_org_carb = Column(Text())
    particle_class = Column(Text())
    perturbation = Column(Text())
    petroleum_hydrocarb = Column(Text())
    ph = Column(Float())
    ph_meth = Column(Text())
    phaeopigments = Column(Text())
    phosphate = Column(Text())
    phosplipid_fatt_acid = Column(Text())
    porosity = Column(Text())
    potassium = Column(Text())
    pressure = Column(Text())
    project = Column(Integer())
    redox_potential = Column(Text())
    replicate_number = Column(Integer())
    salinity = Column(Text())
    salinity_method = Column(Text())
    sample_link = Column(Text())
    sample_name = Column(Text())
    sample_processing = Column(Text())
    biotic_relationship = Column(Enum('free_living', 'parasite', 'commensal', 'symbiont', name='BioticRelationshipEnum'))
    samp_store_temp = Column(Enum('fresh4', 'freshroom', 'frozen20', 'frozen80', 'other', name='SampleStoreTempEnum'))
    sampled_during = Column(UUID(), ForeignKey('SamplingActivity.id'))
    sediment_type = Column(Enum('biogenous', 'cosmogenous', 'hydrogenous', 'lithogenous', name='SedimentTypeEnum'))
    sieving = Column(Text())
    silicate = Column(Text())
    sodium = Column(Text())
    source_mat_id = Column(Text())
    start_date_inc = Column(Text())
    storage_condition = Column(Enum('fresh', 'frozen', 'lyophilized', 'other', name='StorageConditionEnum'))
    storage_condition_other = Column(Text())
    sulfate = Column(Text())
    sulfide = Column(Text())
    technical_reps = Column(Integer())
    temp = Column(Text())
    tidal_stage = Column(Enum('low_tide', 'high_tide', 'ebb_tide', 'flood_tide', name='TidalStageEnum'))
    tot_carb = Column(Text())
    tot_depth_water_col = Column(Text())
    tot_nitro_cont_meth = Column(Text())
    tot_nitro_content = Column(Text())
    tot_org_c_meth = Column(Text())
    tot_org_carb = Column(Text())
    turbidity = Column(Text())
    water_content = Column(Text())
    water_content_meth = Column(Text())
    watering_regm = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    emsl_activity = Column(Text())
    lims_barcode = Column(Text())
    
    
    external_identifiers_rel = relationship( "SedimentSample_external_identifiers" )
    external_identifiers = association_proxy("external_identifiers_rel", "external_identifiers",
                                  creator=lambda x_: SedimentSample_external_identifiers(external_identifiers=x_))
    

    

    def __repr__(self):
        return f"SedimentSample(air_temp_regm={self.air_temp_regm},alkalinity={self.alkalinity},alkalinity_method={self.alkalinity_method},alkyl_diethers={self.alkyl_diethers},aminopept_act={self.aminopept_act},ammonium={self.ammonium},analysis_type={self.analysis_type},bacteria_carb_prod={self.bacteria_carb_prod},biotic_regm={self.biotic_regm},bishomohopanol={self.bishomohopanol},bromide={self.bromide},calcium={self.calcium},carb_nitro_ratio={self.carb_nitro_ratio},chem_administration={self.chem_administration},chloride={self.chloride},chlorophyll={self.chlorophyll},density={self.density},depth={self.depth},diether_lipids={self.diether_lipids},diss_carb_dioxide={self.diss_carb_dioxide},diss_hydrogen={self.diss_hydrogen},diss_inorg_carb={self.diss_inorg_carb},diss_org_carb={self.diss_org_carb},diss_org_nitro={self.diss_org_nitro},diss_oxygen={self.diss_oxygen},env_broad_scale={self.env_broad_scale},env_local_scale={self.env_local_scale},env_medium={self.env_medium},experimental_factor={self.experimental_factor},experimental_factor_other={self.experimental_factor_other},extraction_method={self.extraction_method},gaseous_environment={self.gaseous_environment},glucosidase_act={self.glucosidase_act},humidity_regm={self.humidity_regm},isotope_exposure={self.isotope_exposure},latitude={self.latitude},longitude={self.longitude},light_regm={self.light_regm},magnesium={self.magnesium},mean_frict_vel={self.mean_frict_vel},mean_peak_frict_vel={self.mean_peak_frict_vel},methane={self.methane},method_development={self.method_development},micro_biomass_c_meth={self.micro_biomass_c_meth},micro_biomass_n_meth={self.micro_biomass_n_meth},microbial_biomass={self.microbial_biomass},microbial_biomass_c={self.microbial_biomass_c},microbial_biomass_meth={self.microbial_biomass_meth},microbial_biomass_n={self.microbial_biomass_n},misc_param={self.misc_param},n_alkanes={self.n_alkanes},nitrate={self.nitrate},nitrite={self.nitrite},nitro={self.nitro},non_microb_biomass={self.non_microb_biomass},non_microb_biomass_method={self.non_microb_biomass_method},org_carb={self.org_carb},org_matter={self.org_matter},org_nitro={self.org_nitro},org_nitro_method={self.org_nitro_method},other={self.other},other_samp_store_temp={self.other_samp_store_temp},other_storage_condt={self.other_storage_condt},other_treatment={self.other_treatment},oxygen_status={self.oxygen_status},part_org_carb={self.part_org_carb},particle_class={self.particle_class},perturbation={self.perturbation},petroleum_hydrocarb={self.petroleum_hydrocarb},ph={self.ph},ph_meth={self.ph_meth},phaeopigments={self.phaeopigments},phosphate={self.phosphate},phosplipid_fatt_acid={self.phosplipid_fatt_acid},porosity={self.porosity},potassium={self.potassium},pressure={self.pressure},project={self.project},redox_potential={self.redox_potential},replicate_number={self.replicate_number},salinity={self.salinity},salinity_method={self.salinity_method},sample_link={self.sample_link},sample_name={self.sample_name},sample_processing={self.sample_processing},biotic_relationship={self.biotic_relationship},samp_store_temp={self.samp_store_temp},sampled_during={self.sampled_during},sediment_type={self.sediment_type},sieving={self.sieving},silicate={self.silicate},sodium={self.sodium},source_mat_id={self.source_mat_id},start_date_inc={self.start_date_inc},storage_condition={self.storage_condition},storage_condition_other={self.storage_condition_other},sulfate={self.sulfate},sulfide={self.sulfide},technical_reps={self.technical_reps},temp={self.temp},tidal_stage={self.tidal_stage},tot_carb={self.tot_carb},tot_depth_water_col={self.tot_depth_water_col},tot_nitro_cont_meth={self.tot_nitro_cont_meth},tot_nitro_content={self.tot_nitro_content},tot_org_c_meth={self.tot_org_c_meth},tot_org_carb={self.tot_org_carb},turbidity={self.turbidity},water_content={self.water_content},water_content_meth={self.water_content_meth},watering_regm={self.watering_regm},id={self.id},name={self.name},description={self.description},emsl_activity={self.emsl_activity},lims_barcode={self.lims_barcode},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SoilSample(Sample):
    """
    A sample of soil collected from the environment.
    """
    __tablename__ = 'SoilSample'

    agrochem_addition = Column(Text())
    air_temp_regm = Column(Text())
    al_sat = Column(Text())
    al_sat_meth = Column(Text())
    analysis_type = Column(Text(), nullable=False )
    biotic_regm = Column(Text())
    bulk_elect_conductivity = Column(Text())
    chem_administration = Column(Text())
    depth = Column(Text(), nullable=False )
    env_broad_scale = Column(Text())
    env_local_scale = Column(Text())
    env_medium = Column(Text())
    experimental_factor = Column(Text())
    experimental_factor_other = Column(Text())
    extraction_method = Column(Text())
    filter_method = Column(Text())
    gaseous_environment = Column(Text())
    heavy_metals = Column(Text())
    heavy_metals_meth = Column(Text())
    horizon_meth = Column(Text())
    humidity_regm = Column(Text())
    isotope_exposure = Column(Text())
    latitude = Column(Float(), nullable=False )
    longitude = Column(Float(), nullable=False )
    light_regm = Column(Text())
    link_addit_analys = Column(Text())
    method_development = Column(Text())
    micro_biomass_c_meth = Column(Text())
    micro_biomass_n_meth = Column(Text())
    microbial_biomass = Column(Text())
    microbial_biomass_c = Column(Text())
    microbial_biomass_meth = Column(Text())
    microbial_biomass_n = Column(Text())
    misc_param = Column(Text())
    non_microb_biomass = Column(Text())
    non_microb_biomass_method = Column(Text())
    other = Column(Text())
    other_samp_store_temp = Column(Text())
    other_storage_condt = Column(Text())
    other_treatment = Column(Text())
    oxygen_status = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'obligate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    perturbation = Column(Text())
    ph = Column(Float())
    ph_meth = Column(Text())
    project = Column(Integer())
    replicate_number = Column(Integer())
    salinity = Column(Text())
    salinity_method = Column(Text())
    biotic_relationship = Column(Enum('free_living', 'parasite', 'commensal', 'symbiont', name='BioticRelationshipEnum'))
    samp_store_temp = Column(Enum('fresh4', 'freshroom', 'frozen20', 'frozen80', 'other', name='SampleStoreTempEnum'))
    sample_link = Column(Text())
    sample_name = Column(Text())
    sample_processing = Column(Text())
    sampled_during = Column(UUID(), ForeignKey('SamplingActivity.id'))
    sieving = Column(Text())
    size_frac_low = Column(Text())
    size_frac_up = Column(Text())
    soil_horizon = Column(Enum('a_horizon', 'b_horizon', 'c_horizon', 'e_horizon', 'o_horizon', 'permafrost', 'r_layer', 'm_horizon', name='SoilHorizonEnum'))
    soil_sample_type = Column(Enum('soil_core', 'surface_layer', name='SoilSampleTypeEnum'))
    soil_texture = Column(Text())
    soil_type = Column(Enum('alfisol', 'andisol', 'aridisol', 'entisol', 'gelisol', 'histosol', 'inceptisol', 'mollisol', 'oxisol', 'spodosol', 'ultisol', 'vertisol', name='SoilTypeEnum'))
    soil_type_meth = Column(Text())
    source_mat_id = Column(Text())
    start_date_inc = Column(Text())
    storage_condition = Column(Enum('fresh', 'frozen', 'lyophilized', 'other', name='StorageConditionEnum'))
    storage_condition_other = Column(Text())
    technical_reps = Column(Integer())
    temp = Column(Text())
    texture_meth = Column(Text())
    tot_nitro_cont_meth = Column(Text())
    tot_nitro_content = Column(Text())
    tot_org_c_meth = Column(Text())
    tot_org_carb = Column(Text())
    water_content = Column(Text())
    water_content_meth = Column(Text())
    watering_regm = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    emsl_activity = Column(Text())
    lims_barcode = Column(Text())
    
    
    external_identifiers_rel = relationship( "SoilSample_external_identifiers" )
    external_identifiers = association_proxy("external_identifiers_rel", "external_identifiers",
                                  creator=lambda x_: SoilSample_external_identifiers(external_identifiers=x_))
    

    

    def __repr__(self):
        return f"SoilSample(agrochem_addition={self.agrochem_addition},air_temp_regm={self.air_temp_regm},al_sat={self.al_sat},al_sat_meth={self.al_sat_meth},analysis_type={self.analysis_type},biotic_regm={self.biotic_regm},bulk_elect_conductivity={self.bulk_elect_conductivity},chem_administration={self.chem_administration},depth={self.depth},env_broad_scale={self.env_broad_scale},env_local_scale={self.env_local_scale},env_medium={self.env_medium},experimental_factor={self.experimental_factor},experimental_factor_other={self.experimental_factor_other},extraction_method={self.extraction_method},filter_method={self.filter_method},gaseous_environment={self.gaseous_environment},heavy_metals={self.heavy_metals},heavy_metals_meth={self.heavy_metals_meth},horizon_meth={self.horizon_meth},humidity_regm={self.humidity_regm},isotope_exposure={self.isotope_exposure},latitude={self.latitude},longitude={self.longitude},light_regm={self.light_regm},link_addit_analys={self.link_addit_analys},method_development={self.method_development},micro_biomass_c_meth={self.micro_biomass_c_meth},micro_biomass_n_meth={self.micro_biomass_n_meth},microbial_biomass={self.microbial_biomass},microbial_biomass_c={self.microbial_biomass_c},microbial_biomass_meth={self.microbial_biomass_meth},microbial_biomass_n={self.microbial_biomass_n},misc_param={self.misc_param},non_microb_biomass={self.non_microb_biomass},non_microb_biomass_method={self.non_microb_biomass_method},other={self.other},other_samp_store_temp={self.other_samp_store_temp},other_storage_condt={self.other_storage_condt},other_treatment={self.other_treatment},oxygen_status={self.oxygen_status},perturbation={self.perturbation},ph={self.ph},ph_meth={self.ph_meth},project={self.project},replicate_number={self.replicate_number},salinity={self.salinity},salinity_method={self.salinity_method},biotic_relationship={self.biotic_relationship},samp_store_temp={self.samp_store_temp},sample_link={self.sample_link},sample_name={self.sample_name},sample_processing={self.sample_processing},sampled_during={self.sampled_during},sieving={self.sieving},size_frac_low={self.size_frac_low},size_frac_up={self.size_frac_up},soil_horizon={self.soil_horizon},soil_sample_type={self.soil_sample_type},soil_texture={self.soil_texture},soil_type={self.soil_type},soil_type_meth={self.soil_type_meth},source_mat_id={self.source_mat_id},start_date_inc={self.start_date_inc},storage_condition={self.storage_condition},storage_condition_other={self.storage_condition_other},technical_reps={self.technical_reps},temp={self.temp},texture_meth={self.texture_meth},tot_nitro_cont_meth={self.tot_nitro_cont_meth},tot_nitro_content={self.tot_nitro_content},tot_org_c_meth={self.tot_org_c_meth},tot_org_carb={self.tot_org_carb},water_content={self.water_content},water_content_meth={self.water_content_meth},watering_regm={self.watering_regm},id={self.id},name={self.name},description={self.description},emsl_activity={self.emsl_activity},lims_barcode={self.lims_barcode},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SynthesizedMaterialSample(Sample):
    """
    A sample containing synthetically generated material.
    """
    __tablename__ = 'SynthesizedMaterialSample'

    analysis_type = Column(Text(), nullable=False )
    cas = Column(Text())
    compound_name = Column(Text())
    experimental_factor = Column(Text())
    experimental_factor_other = Column(Text())
    genetic_mod = Column(Text())
    item_number = Column(Text())
    other = Column(Text())
    other_samp_store_temp = Column(Text())
    other_storage_condt = Column(Text())
    oxygen_status = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'obligate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    product_name = Column(Text())
    production_method = Column(Text())
    project = Column(Integer())
    replicate_number = Column(Integer())
    sample_link = Column(Text())
    sample_name = Column(Text())
    sample_processing = Column(Text())
    samp_store_temp = Column(Enum('fresh4', 'freshroom', 'frozen20', 'frozen80', 'other', name='SampleStoreTempEnum'))
    sampled_during = Column(UUID(), ForeignKey('SamplingActivity.id'))
    source_mat_id = Column(Text())
    storage_condition = Column(Enum('fresh', 'frozen', 'lyophilized', 'other', name='StorageConditionEnum'))
    storage_condition_other = Column(Text())
    synth_instrument = Column(Text(), nullable=False )
    synth_process = Column(Text())
    synth_reagents = Column(Text(), nullable=False )
    technical_reps = Column(Integer())
    temp = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    emsl_activity = Column(Text())
    lims_barcode = Column(Text())
    
    
    external_identifiers_rel = relationship( "SynthesizedMaterialSample_external_identifiers" )
    external_identifiers = association_proxy("external_identifiers_rel", "external_identifiers",
                                  creator=lambda x_: SynthesizedMaterialSample_external_identifiers(external_identifiers=x_))
    

    

    def __repr__(self):
        return f"SynthesizedMaterialSample(analysis_type={self.analysis_type},cas={self.cas},compound_name={self.compound_name},experimental_factor={self.experimental_factor},experimental_factor_other={self.experimental_factor_other},genetic_mod={self.genetic_mod},item_number={self.item_number},other={self.other},other_samp_store_temp={self.other_samp_store_temp},other_storage_condt={self.other_storage_condt},oxygen_status={self.oxygen_status},product_name={self.product_name},production_method={self.production_method},project={self.project},replicate_number={self.replicate_number},sample_link={self.sample_link},sample_name={self.sample_name},sample_processing={self.sample_processing},samp_store_temp={self.samp_store_temp},sampled_during={self.sampled_during},source_mat_id={self.source_mat_id},storage_condition={self.storage_condition},storage_condition_other={self.storage_condition_other},synth_instrument={self.synth_instrument},synth_process={self.synth_process},synth_reagents={self.synth_reagents},technical_reps={self.technical_reps},temp={self.temp},id={self.id},name={self.name},description={self.description},emsl_activity={self.emsl_activity},lims_barcode={self.lims_barcode},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class TerraformSample(Sample):
    """
    A sample collected from a Terraform experiment.
    """
    __tablename__ = 'TerraformSample'

    air_temp_regm = Column(Text())
    analysis_type = Column(Text(), nullable=False )
    biotic_regm = Column(Text())
    chem_administration = Column(Text())
    cult_root_med = Column(Text())
    encoded_traits = Column(Text())
    env_broad_scale = Column(Text())
    env_local_scale = Column(Text())
    env_medium = Column(Text())
    gaseous_environment = Column(Text())
    genetic_mod = Column(Text())
    growth_medium = Column(Text())
    host_age = Column(Text())
    host_common_name = Column(Text())
    host_dry_mass = Column(Text())
    host_genotype = Column(Text())
    host_height = Column(Text())
    host_life_stage = Column(Text())
    host_spec_range = Column(Text())
    host_taxid = Column(Text())
    host_tot_mass = Column(Text())
    host_wet_mass = Column(Text())
    humidity_regm = Column(Text())
    initiation_date_inoculation = Column(Text(), nullable=False )
    initiation_date_plant = Column(Text(), nullable=False )
    isol_growth_condt = Column(Text())
    isotope_exposure = Column(Text())
    light_regm = Column(Text())
    method_development = Column(Text())
    mineral_nutr_regm = Column(Text())
    misc_param = Column(Text())
    non_min_nutr_regm = Column(Text())
    other = Column(Text())
    other_samp_store_temp = Column(Text())
    other_storage_condt = Column(Text())
    other_treatment = Column(Text())
    oxygen_status = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'obligate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    plant_growth_med = Column(Text())
    plant_product = Column(Text())
    plant_sex = Column(Enum('androdioecious', 'androecious', 'androgynomonoecious', 'androgynous', 'andromonoecious', 'bisexual', 'dichogamous', 'diclinous', 'dioecious', 'gynodioecious', 'gynoecious', 'gynomonoecious', 'hermaphroditic', 'imperfect', 'monoclinous', 'monoecious', 'perfect', 'polygamodioecious', 'polygamomonoecious', 'polygamous', 'protandrous', 'protogynous', 'subandroecious', 'subdioecious', 'subgynoecious', 'synoecious', 'trimonoecious', 'trioecious', 'unisexual', name='PlantSexEnum'))
    plant_struc = Column(Enum('stem', 'leaf', 'root', 'fine_root', 'whole_plant', 'stamen', 'carpel', 'seed', 'rhizodeposits', name='PlantStructureEnum'))
    pressure = Column(Text())
    project = Column(Integer())
    propagation = Column(Text())
    redox_potential = Column(Text())
    ref_biomaterial = Column(Text())
    replicate_number = Column(Integer())
    root_cond = Column(Text())
    root_med_carbon = Column(Text())
    root_med_macronutr = Column(Text())
    root_med_micronutr = Column(Text())
    salt_regm = Column(Text())
    sample_link = Column(Text())
    sample_name = Column(Text())
    sample_processing = Column(Text())
    biotic_relationship = Column(Enum('free_living', 'parasite', 'commensal', 'symbiont', name='BioticRelationshipEnum'))
    samp_store_temp = Column(Enum('fresh4', 'freshroom', 'frozen20', 'frozen80', 'other', name='SampleStoreTempEnum'))
    sampled_during = Column(UUID(), ForeignKey('SamplingActivity.id'))
    source_mat_id = Column(Text())
    storage_condition = Column(Enum('fresh', 'frozen', 'lyophilized', 'other', name='StorageConditionEnum'))
    storage_condition_other = Column(Text())
    synth_env_assembly = Column(Text(), nullable=False )
    synth_env_design = Column(Enum('pore_scale_micromodels', 'rhizochip', 'subtap', 'three_d_bioprinted_synthetic_soil_aggregates', 'pore2chip', name='SyntheticEnvironmentEnum'), nullable=False )
    synth_env_design_method = Column(Text(), nullable=False )
    synth_env_material = Column(Text(), nullable=False )
    synth_env_treatment = Column(Text(), nullable=False )
    synth_start_date = Column(Text(), nullable=False )
    technical_reps = Column(Integer())
    temp = Column(Text())
    tiss_cult_growth_med = Column(Text())
    water_content = Column(Text())
    water_content_meth = Column(Text())
    watering_regm = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    emsl_activity = Column(Text())
    lims_barcode = Column(Text())
    
    
    external_identifiers_rel = relationship( "TerraformSample_external_identifiers" )
    external_identifiers = association_proxy("external_identifiers_rel", "external_identifiers",
                                  creator=lambda x_: TerraformSample_external_identifiers(external_identifiers=x_))
    

    

    def __repr__(self):
        return f"TerraformSample(air_temp_regm={self.air_temp_regm},analysis_type={self.analysis_type},biotic_regm={self.biotic_regm},chem_administration={self.chem_administration},cult_root_med={self.cult_root_med},encoded_traits={self.encoded_traits},env_broad_scale={self.env_broad_scale},env_local_scale={self.env_local_scale},env_medium={self.env_medium},gaseous_environment={self.gaseous_environment},genetic_mod={self.genetic_mod},growth_medium={self.growth_medium},host_age={self.host_age},host_common_name={self.host_common_name},host_dry_mass={self.host_dry_mass},host_genotype={self.host_genotype},host_height={self.host_height},host_life_stage={self.host_life_stage},host_spec_range={self.host_spec_range},host_taxid={self.host_taxid},host_tot_mass={self.host_tot_mass},host_wet_mass={self.host_wet_mass},humidity_regm={self.humidity_regm},initiation_date_inoculation={self.initiation_date_inoculation},initiation_date_plant={self.initiation_date_plant},isol_growth_condt={self.isol_growth_condt},isotope_exposure={self.isotope_exposure},light_regm={self.light_regm},method_development={self.method_development},mineral_nutr_regm={self.mineral_nutr_regm},misc_param={self.misc_param},non_min_nutr_regm={self.non_min_nutr_regm},other={self.other},other_samp_store_temp={self.other_samp_store_temp},other_storage_condt={self.other_storage_condt},other_treatment={self.other_treatment},oxygen_status={self.oxygen_status},plant_growth_med={self.plant_growth_med},plant_product={self.plant_product},plant_sex={self.plant_sex},plant_struc={self.plant_struc},pressure={self.pressure},project={self.project},propagation={self.propagation},redox_potential={self.redox_potential},ref_biomaterial={self.ref_biomaterial},replicate_number={self.replicate_number},root_cond={self.root_cond},root_med_carbon={self.root_med_carbon},root_med_macronutr={self.root_med_macronutr},root_med_micronutr={self.root_med_micronutr},salt_regm={self.salt_regm},sample_link={self.sample_link},sample_name={self.sample_name},sample_processing={self.sample_processing},biotic_relationship={self.biotic_relationship},samp_store_temp={self.samp_store_temp},sampled_during={self.sampled_during},source_mat_id={self.source_mat_id},storage_condition={self.storage_condition},storage_condition_other={self.storage_condition_other},synth_env_assembly={self.synth_env_assembly},synth_env_design={self.synth_env_design},synth_env_design_method={self.synth_env_design_method},synth_env_material={self.synth_env_material},synth_env_treatment={self.synth_env_treatment},synth_start_date={self.synth_start_date},technical_reps={self.technical_reps},temp={self.temp},tiss_cult_growth_med={self.tiss_cult_growth_med},water_content={self.water_content},water_content_meth={self.water_content_meth},watering_regm={self.watering_regm},id={self.id},name={self.name},description={self.description},emsl_activity={self.emsl_activity},lims_barcode={self.lims_barcode},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class WaterSample(Sample):
    """
    A sample of water collected from the environment.
    """
    __tablename__ = 'WaterSample'

    air_temp_regm = Column(Text())
    alkalinity = Column(Text())
    alkalinity_method = Column(Text())
    alkyl_diethers = Column(Text())
    aminopept_act = Column(Text())
    ammonium = Column(Text())
    analysis_type = Column(Text(), nullable=False )
    bac_prod = Column(Text())
    bac_resp = Column(Text())
    bacteria_carb_prod = Column(Text())
    biotic_regm = Column(Text())
    bishomohopanol = Column(Text())
    bromide = Column(Text())
    calcium = Column(Text())
    carb_nitro_ratio = Column(Text())
    chem_administration = Column(Text())
    chloride = Column(Text())
    chlorophyll = Column(Text())
    conduc = Column(Text())
    density = Column(Text())
    depth = Column(Text(), nullable=False )
    diether_lipids = Column(Text())
    diss_carb_dioxide = Column(Text())
    diss_hydrogen = Column(Text())
    diss_inorg_carb = Column(Text())
    diss_inorg_nitro = Column(Text())
    diss_inorg_phosp = Column(Text())
    diss_org_carb = Column(Text())
    diss_org_nitro = Column(Text())
    diss_oxygen = Column(Text())
    down_par = Column(Text())
    env_broad_scale = Column(Text())
    env_local_scale = Column(Text())
    env_medium = Column(Text())
    experimental_factor = Column(Text())
    experimental_factor_other = Column(Text())
    extraction_method = Column(Text())
    filter_method = Column(Text(), nullable=False )
    fluor = Column(Text())
    gaseous_environment = Column(Text())
    glucosidase_act = Column(Text())
    isotope_exposure = Column(Text())
    latitude = Column(Float(), nullable=False )
    longitude = Column(Float(), nullable=False )
    light_intensity = Column(Text())
    magnesium = Column(Text())
    mean_frict_vel = Column(Text())
    mean_peak_frict_vel = Column(Text())
    method_development = Column(Text())
    misc_param = Column(Text())
    n_alkanes = Column(Text())
    nitrate = Column(Text())
    nitrite = Column(Text())
    nitro = Column(Text())
    non_microb_biomass = Column(Text())
    non_microb_biomass_method = Column(Text())
    org_carb = Column(Text())
    org_matter = Column(Text())
    org_nitro = Column(Text())
    org_nitro_method = Column(Text())
    other = Column(Text())
    other_samp_store_temp = Column(Text())
    other_storage_condt = Column(Text())
    other_treatment = Column(Text())
    oxygen_status = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'obligate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    part_org_carb = Column(Text())
    part_org_nitro = Column(Text())
    perturbation = Column(Text())
    petroleum_hydrocarb = Column(Text())
    ph = Column(Float())
    ph_meth = Column(Text())
    phaeopigments = Column(Text())
    phosphate = Column(Text())
    phosplipid_fatt_acid = Column(Text())
    photon_flux = Column(Text())
    potassium = Column(Text())
    pressure = Column(Text())
    primary_prod = Column(Text())
    project = Column(Integer())
    redox_potential = Column(Text())
    replicate_number = Column(Integer())
    salinity = Column(Text())
    salinity_method = Column(Text())
    sample_link = Column(Text())
    sample_name = Column(Text())
    sampled_during = Column(UUID(), ForeignKey('SamplingActivity.id'))
    silicate = Column(Text())
    size_frac_low = Column(Text(), nullable=False )
    size_frac_up = Column(Text(), nullable=False )
    sodium = Column(Text())
    soluble_react_phosp = Column(Text())
    source_mat_id = Column(Text())
    start_date_inc = Column(Text())
    storage_condition = Column(Enum('fresh', 'frozen', 'lyophilized', 'other', name='StorageConditionEnum'))
    storage_condition_other = Column(Text())
    sulfate = Column(Text())
    sulfide = Column(Text())
    samp_store_temp = Column(Enum('fresh4', 'freshroom', 'frozen20', 'frozen80', 'other', name='SampleStoreTempEnum'))
    suspend_part_matter = Column(Text())
    technical_reps = Column(Integer())
    temp = Column(Text())
    tidal_stage = Column(Enum('low_tide', 'high_tide', 'ebb_tide', 'flood_tide', name='TidalStageEnum'))
    tot_depth_water_col = Column(Text())
    tot_diss_nitro = Column(Text())
    tot_inorg_nitro = Column(Text())
    tot_nitro = Column(Text())
    tot_part_carb = Column(Text())
    tot_phosp = Column(Text())
    turbidity = Column(Text())
    water_current = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    emsl_activity = Column(Text())
    lims_barcode = Column(Text())
    
    
    external_identifiers_rel = relationship( "WaterSample_external_identifiers" )
    external_identifiers = association_proxy("external_identifiers_rel", "external_identifiers",
                                  creator=lambda x_: WaterSample_external_identifiers(external_identifiers=x_))
    

    

    def __repr__(self):
        return f"WaterSample(air_temp_regm={self.air_temp_regm},alkalinity={self.alkalinity},alkalinity_method={self.alkalinity_method},alkyl_diethers={self.alkyl_diethers},aminopept_act={self.aminopept_act},ammonium={self.ammonium},analysis_type={self.analysis_type},bac_prod={self.bac_prod},bac_resp={self.bac_resp},bacteria_carb_prod={self.bacteria_carb_prod},biotic_regm={self.biotic_regm},bishomohopanol={self.bishomohopanol},bromide={self.bromide},calcium={self.calcium},carb_nitro_ratio={self.carb_nitro_ratio},chem_administration={self.chem_administration},chloride={self.chloride},chlorophyll={self.chlorophyll},conduc={self.conduc},density={self.density},depth={self.depth},diether_lipids={self.diether_lipids},diss_carb_dioxide={self.diss_carb_dioxide},diss_hydrogen={self.diss_hydrogen},diss_inorg_carb={self.diss_inorg_carb},diss_inorg_nitro={self.diss_inorg_nitro},diss_inorg_phosp={self.diss_inorg_phosp},diss_org_carb={self.diss_org_carb},diss_org_nitro={self.diss_org_nitro},diss_oxygen={self.diss_oxygen},down_par={self.down_par},env_broad_scale={self.env_broad_scale},env_local_scale={self.env_local_scale},env_medium={self.env_medium},experimental_factor={self.experimental_factor},experimental_factor_other={self.experimental_factor_other},extraction_method={self.extraction_method},filter_method={self.filter_method},fluor={self.fluor},gaseous_environment={self.gaseous_environment},glucosidase_act={self.glucosidase_act},isotope_exposure={self.isotope_exposure},latitude={self.latitude},longitude={self.longitude},light_intensity={self.light_intensity},magnesium={self.magnesium},mean_frict_vel={self.mean_frict_vel},mean_peak_frict_vel={self.mean_peak_frict_vel},method_development={self.method_development},misc_param={self.misc_param},n_alkanes={self.n_alkanes},nitrate={self.nitrate},nitrite={self.nitrite},nitro={self.nitro},non_microb_biomass={self.non_microb_biomass},non_microb_biomass_method={self.non_microb_biomass_method},org_carb={self.org_carb},org_matter={self.org_matter},org_nitro={self.org_nitro},org_nitro_method={self.org_nitro_method},other={self.other},other_samp_store_temp={self.other_samp_store_temp},other_storage_condt={self.other_storage_condt},other_treatment={self.other_treatment},oxygen_status={self.oxygen_status},part_org_carb={self.part_org_carb},part_org_nitro={self.part_org_nitro},perturbation={self.perturbation},petroleum_hydrocarb={self.petroleum_hydrocarb},ph={self.ph},ph_meth={self.ph_meth},phaeopigments={self.phaeopigments},phosphate={self.phosphate},phosplipid_fatt_acid={self.phosplipid_fatt_acid},photon_flux={self.photon_flux},potassium={self.potassium},pressure={self.pressure},primary_prod={self.primary_prod},project={self.project},redox_potential={self.redox_potential},replicate_number={self.replicate_number},salinity={self.salinity},salinity_method={self.salinity_method},sample_link={self.sample_link},sample_name={self.sample_name},sampled_during={self.sampled_during},silicate={self.silicate},size_frac_low={self.size_frac_low},size_frac_up={self.size_frac_up},sodium={self.sodium},soluble_react_phosp={self.soluble_react_phosp},source_mat_id={self.source_mat_id},start_date_inc={self.start_date_inc},storage_condition={self.storage_condition},storage_condition_other={self.storage_condition_other},sulfate={self.sulfate},sulfide={self.sulfide},samp_store_temp={self.samp_store_temp},suspend_part_matter={self.suspend_part_matter},technical_reps={self.technical_reps},temp={self.temp},tidal_stage={self.tidal_stage},tot_depth_water_col={self.tot_depth_water_col},tot_diss_nitro={self.tot_diss_nitro},tot_inorg_nitro={self.tot_inorg_nitro},tot_nitro={self.tot_nitro},tot_part_carb={self.tot_part_carb},tot_phosp={self.tot_phosp},turbidity={self.turbidity},water_current={self.water_current},id={self.id},name={self.name},description={self.description},emsl_activity={self.emsl_activity},lims_barcode={self.lims_barcode},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ProcessedSample(Sample):
    """
    A sample that has undergone processing or analysis. Processed Sample entities are derived from Activities. The upstream SampleProcessing that produced this ProcessedSample is referenced via sampled_during.
    """
    __tablename__ = 'ProcessedSample'

    storage_location = Column(Text())
    label_text = Column(Text())
    concentration_ug_per_uL = Column(Float())
    total_amount_ug = Column(Float())
    volume_uL = Column(Float())
    sampled_portion = Column(Enum('supernatant', 'pellet', 'organic_layer', 'aqueous_layer', 'interlayer', 'chloroform_layer', 'methanol_layer', name='SamplePortionEnum'))
    sampled_during = Column(UUID(), ForeignKey('SampleProcessing.id'))
    replicate = Column(Integer())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    emsl_activity = Column(Text())
    lims_barcode = Column(Text())
    

    

    def __repr__(self):
        return f"ProcessedSample(storage_location={self.storage_location},label_text={self.label_text},concentration_ug_per_uL={self.concentration_ug_per_uL},total_amount_ug={self.total_amount_ug},volume_uL={self.volume_uL},sampled_portion={self.sampled_portion},sampled_during={self.sampled_during},replicate={self.replicate},id={self.id},name={self.name},description={self.description},emsl_activity={self.emsl_activity},lims_barcode={self.lims_barcode},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class AerosolArmSamplingActivity(SamplingActivity):
    """
    A sampling activity where aerosol samples were collected by ARM.
    """
    __tablename__ = 'AerosolArmSamplingActivity'

    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    emsl_activity = Column(Text())
    collection_date = Column(Date())
    shipped_sample_size = Column(Text())
    sampled_at_site = Column(UUID(), ForeignKey('Site.id'))
    

    

    def __repr__(self):
        return f"AerosolArmSamplingActivity(id={self.id},name={self.name},description={self.description},project={self.project},emsl_activity={self.emsl_activity},collection_date={self.collection_date},shipped_sample_size={self.shipped_sample_size},sampled_at_site={self.sampled_at_site},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class AerosolSamplingActivity(SamplingActivity):
    """
    A sampling activity where aerosol samples were collected.
    """
    __tablename__ = 'AerosolSamplingActivity'

    collection_time = Column(Text())
    humidity = Column(Text())
    sample_collected = Column(Text())
    sample_collection_dev = Column(Text())
    sampling_duration = Column(Text())
    wind_direction = Column(Enum('north', 'north_east', 'east', 'south_east', 'south', 'south_west', 'west', 'north_west', name='CardinalDirectionEnum'))
    wind_speed = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    emsl_activity = Column(Text())
    collection_date = Column(Date())
    shipped_sample_size = Column(Text())
    sampled_at_site = Column(UUID(), ForeignKey('Site.id'))
    

    

    def __repr__(self):
        return f"AerosolSamplingActivity(collection_time={self.collection_time},humidity={self.humidity},sample_collected={self.sample_collected},sample_collection_dev={self.sample_collection_dev},sampling_duration={self.sampling_duration},wind_direction={self.wind_direction},wind_speed={self.wind_speed},id={self.id},name={self.name},description={self.description},project={self.project},emsl_activity={self.emsl_activity},collection_date={self.collection_date},shipped_sample_size={self.shipped_sample_size},sampled_at_site={self.sampled_at_site},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class CommerciallyPurchasedSamplingActivity(SamplingActivity):
    """
    Collection of samples that were purchased by the user.
    """
    __tablename__ = 'CommerciallyPurchasedSamplingActivity'

    sample_collected = Column(Text())
    sample_collection_dev = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    emsl_activity = Column(Text())
    collection_date = Column(Date())
    shipped_sample_size = Column(Text())
    sampled_at_site = Column(UUID(), ForeignKey('Site.id'))
    

    

    def __repr__(self):
        return f"CommerciallyPurchasedSamplingActivity(sample_collected={self.sample_collected},sample_collection_dev={self.sample_collection_dev},id={self.id},name={self.name},description={self.description},project={self.project},emsl_activity={self.emsl_activity},collection_date={self.collection_date},shipped_sample_size={self.shipped_sample_size},sampled_at_site={self.sampled_at_site},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class CultureEnvironmentalSamplingActivity(SamplingActivity):
    """
    Collection of samples from a culture of organisms taken from the environment.
    """
    __tablename__ = 'CultureEnvironmentalSamplingActivity'

    collection_time = Column(Text())
    sample_collected = Column(Text())
    sample_collection_dev = Column(Text())
    sample_collection_method = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    emsl_activity = Column(Text())
    collection_date = Column(Date())
    shipped_sample_size = Column(Text())
    sampled_at_site = Column(UUID(), ForeignKey('Site.id'))
    

    

    def __repr__(self):
        return f"CultureEnvironmentalSamplingActivity(collection_time={self.collection_time},sample_collected={self.sample_collected},sample_collection_dev={self.sample_collection_dev},sample_collection_method={self.sample_collection_method},id={self.id},name={self.name},description={self.description},project={self.project},emsl_activity={self.emsl_activity},collection_date={self.collection_date},shipped_sample_size={self.shipped_sample_size},sampled_at_site={self.sampled_at_site},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class EngineeredStrainSamplingActivity(SamplingActivity):
    """
    Collection of samples from a culture of an engineered organism.
    """
    __tablename__ = 'EngineeredStrainSamplingActivity'

    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    emsl_activity = Column(Text())
    collection_date = Column(Date())
    shipped_sample_size = Column(Text())
    sampled_at_site = Column(UUID(), ForeignKey('Site.id'))
    

    

    def __repr__(self):
        return f"EngineeredStrainSamplingActivity(id={self.id},name={self.name},description={self.description},project={self.project},emsl_activity={self.emsl_activity},collection_date={self.collection_date},shipped_sample_size={self.shipped_sample_size},sampled_at_site={self.sampled_at_site},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class FieldDeployedTerraformSamplingActivity(SamplingActivity):
    """
    Collection of samples from a field-deployed Terraform device.
    """
    __tablename__ = 'FieldDeployedTerraformSamplingActivity'

    collection_time = Column(Text())
    sample_collected = Column(Text())
    sample_collection_method = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    emsl_activity = Column(Text())
    collection_date = Column(Date())
    shipped_sample_size = Column(Text())
    sampled_at_site = Column(UUID(), ForeignKey('Site.id'))
    

    

    def __repr__(self):
        return f"FieldDeployedTerraformSamplingActivity(collection_time={self.collection_time},sample_collected={self.sample_collected},sample_collection_method={self.sample_collection_method},id={self.id},name={self.name},description={self.description},project={self.project},emsl_activity={self.emsl_activity},collection_date={self.collection_date},shipped_sample_size={self.shipped_sample_size},sampled_at_site={self.sampled_at_site},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MixedCultureSamplingActivity(SamplingActivity):
    """
    Collection of samples from a mixed culture.
    """
    __tablename__ = 'MixedCultureSamplingActivity'

    collection_time = Column(Text())
    sample_collected = Column(Text())
    sample_collection_dev = Column(Text())
    sample_collection_method = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    emsl_activity = Column(Text())
    collection_date = Column(Date())
    shipped_sample_size = Column(Text())
    sampled_at_site = Column(UUID(), ForeignKey('Site.id'))
    

    

    def __repr__(self):
        return f"MixedCultureSamplingActivity(collection_time={self.collection_time},sample_collected={self.sample_collected},sample_collection_dev={self.sample_collection_dev},sample_collection_method={self.sample_collection_method},id={self.id},name={self.name},description={self.description},project={self.project},emsl_activity={self.emsl_activity},collection_date={self.collection_date},shipped_sample_size={self.shipped_sample_size},sampled_at_site={self.sampled_at_site},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MonetSoilSamplingActivity(SamplingActivity):
    """
    Collection of soil cores according to the MONet soil sampling protocol.
    """
    __tablename__ = 'MonetSoilSamplingActivity'

    collection_time = Column(Text(), nullable=False )
    infiltration_1 = Column(Text(), nullable=False )
    infiltration_2 = Column(Text(), nullable=False )
    infiltration_notes = Column(Text())
    sample_collection_dev = Column(Text(), nullable=False )
    weather = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    emsl_activity = Column(Text())
    collection_date = Column(Date())
    shipped_sample_size = Column(Text())
    sampled_at_site = Column(UUID(), ForeignKey('Site.id'))
    

    

    def __repr__(self):
        return f"MonetSoilSamplingActivity(collection_time={self.collection_time},infiltration_1={self.infiltration_1},infiltration_2={self.infiltration_2},infiltration_notes={self.infiltration_notes},sample_collection_dev={self.sample_collection_dev},weather={self.weather},id={self.id},name={self.name},description={self.description},project={self.project},emsl_activity={self.emsl_activity},collection_date={self.collection_date},shipped_sample_size={self.shipped_sample_size},sampled_at_site={self.sampled_at_site},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class OtherUndescribedSamplingActivity(SamplingActivity):
    """
    Collection of samples from source that does not fit into any of the other categories.
    """
    __tablename__ = 'OtherUndescribedSamplingActivity'

    collection_time = Column(Text())
    humidity = Column(Text())
    sample_collected = Column(Text())
    sample_collection_dev = Column(Text())
    sample_collection_method = Column(Text())
    sampling_duration = Column(Text())
    wind_direction = Column(Enum('north', 'north_east', 'east', 'south_east', 'south', 'south_west', 'west', 'north_west', name='CardinalDirectionEnum'))
    wind_speed = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    emsl_activity = Column(Text())
    collection_date = Column(Date())
    shipped_sample_size = Column(Text())
    sampled_at_site = Column(UUID(), ForeignKey('Site.id'))
    

    

    def __repr__(self):
        return f"OtherUndescribedSamplingActivity(collection_time={self.collection_time},humidity={self.humidity},sample_collected={self.sample_collected},sample_collection_dev={self.sample_collection_dev},sample_collection_method={self.sample_collection_method},sampling_duration={self.sampling_duration},wind_direction={self.wind_direction},wind_speed={self.wind_speed},id={self.id},name={self.name},description={self.description},project={self.project},emsl_activity={self.emsl_activity},collection_date={self.collection_date},shipped_sample_size={self.shipped_sample_size},sampled_at_site={self.sampled_at_site},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class PlantSamplingActivity(SamplingActivity):
    """
    Collection of samples associated with plants.
    """
    __tablename__ = 'PlantSamplingActivity'

    collection_time = Column(Text())
    sample_collected = Column(Text())
    sample_collection_dev = Column(Text())
    sample_collection_method = Column(Text())
    weather = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    emsl_activity = Column(Text())
    collection_date = Column(Date())
    shipped_sample_size = Column(Text())
    sampled_at_site = Column(UUID(), ForeignKey('Site.id'))
    

    

    def __repr__(self):
        return f"PlantSamplingActivity(collection_time={self.collection_time},sample_collected={self.sample_collected},sample_collection_dev={self.sample_collection_dev},sample_collection_method={self.sample_collection_method},weather={self.weather},id={self.id},name={self.name},description={self.description},project={self.project},emsl_activity={self.emsl_activity},collection_date={self.collection_date},shipped_sample_size={self.shipped_sample_size},sampled_at_site={self.sampled_at_site},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class PureCultureSamplingActivity(SamplingActivity):
    """
    Collection of samples from a culture containing a single organism.
    """
    __tablename__ = 'PureCultureSamplingActivity'

    collection_time = Column(Text())
    sample_collected = Column(Text())
    sample_collection_dev = Column(Text())
    sample_collection_method = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    emsl_activity = Column(Text())
    collection_date = Column(Date())
    shipped_sample_size = Column(Text())
    sampled_at_site = Column(UUID(), ForeignKey('Site.id'))
    

    

    def __repr__(self):
        return f"PureCultureSamplingActivity(collection_time={self.collection_time},sample_collected={self.sample_collected},sample_collection_dev={self.sample_collection_dev},sample_collection_method={self.sample_collection_method},id={self.id},name={self.name},description={self.description},project={self.project},emsl_activity={self.emsl_activity},collection_date={self.collection_date},shipped_sample_size={self.shipped_sample_size},sampled_at_site={self.sampled_at_site},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SedimentSamplingActivity(SamplingActivity):
    """
    Collection of sediment samples from the environment.
    """
    __tablename__ = 'SedimentSamplingActivity'

    collection_time = Column(Text())
    sample_collected = Column(Text())
    sample_collection_dev = Column(Text())
    sample_collection_method = Column(Text())
    weather = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    emsl_activity = Column(Text())
    collection_date = Column(Date())
    shipped_sample_size = Column(Text())
    sampled_at_site = Column(UUID(), ForeignKey('Site.id'))
    

    

    def __repr__(self):
        return f"SedimentSamplingActivity(collection_time={self.collection_time},sample_collected={self.sample_collected},sample_collection_dev={self.sample_collection_dev},sample_collection_method={self.sample_collection_method},weather={self.weather},id={self.id},name={self.name},description={self.description},project={self.project},emsl_activity={self.emsl_activity},collection_date={self.collection_date},shipped_sample_size={self.shipped_sample_size},sampled_at_site={self.sampled_at_site},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SoilSamplingActivity(SamplingActivity):
    """
    Collection of soil samples from the environment.
    """
    __tablename__ = 'SoilSamplingActivity'

    name = Column(Text(), nullable=False )
    description = Column(Text())
    collection_time = Column(Text())
    infiltration_1 = Column(Text())
    infiltration_2 = Column(Text())
    infiltration_notes = Column(Text())
    sample_collected = Column(Text())
    sample_collection_dev = Column(Text())
    sample_collection_method = Column(Text())
    wind_direction = Column(Enum('north', 'north_east', 'east', 'south_east', 'south', 'south_west', 'west', 'north_west', name='CardinalDirectionEnum'))
    weather = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    project = Column(Integer())
    emsl_activity = Column(Text())
    collection_date = Column(Date())
    shipped_sample_size = Column(Text())
    sampled_at_site = Column(UUID(), ForeignKey('Site.id'))
    

    

    def __repr__(self):
        return f"SoilSamplingActivity(name={self.name},description={self.description},collection_time={self.collection_time},infiltration_1={self.infiltration_1},infiltration_2={self.infiltration_2},infiltration_notes={self.infiltration_notes},sample_collected={self.sample_collected},sample_collection_dev={self.sample_collection_dev},sample_collection_method={self.sample_collection_method},wind_direction={self.wind_direction},weather={self.weather},id={self.id},project={self.project},emsl_activity={self.emsl_activity},collection_date={self.collection_date},shipped_sample_size={self.shipped_sample_size},sampled_at_site={self.sampled_at_site},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SynthesizedMaterialSamplingActivity(SamplingActivity):
    """
    Collection of samples of a synthesized material.
    """
    __tablename__ = 'SynthesizedMaterialSamplingActivity'

    sample_collected = Column(Text())
    sample_collection_dev = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    emsl_activity = Column(Text())
    collection_date = Column(Date())
    shipped_sample_size = Column(Text())
    sampled_at_site = Column(UUID(), ForeignKey('Site.id'))
    

    

    def __repr__(self):
        return f"SynthesizedMaterialSamplingActivity(sample_collected={self.sample_collected},sample_collection_dev={self.sample_collection_dev},id={self.id},name={self.name},description={self.description},project={self.project},emsl_activity={self.emsl_activity},collection_date={self.collection_date},shipped_sample_size={self.shipped_sample_size},sampled_at_site={self.sampled_at_site},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class TerraformSamplingActivity(SamplingActivity):
    """
    Collection of samples from a Terraform device.
    """
    __tablename__ = 'TerraformSamplingActivity'

    collection_time = Column(Text())
    sample_collected = Column(Text())
    sample_collection_method = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    emsl_activity = Column(Text())
    collection_date = Column(Date())
    shipped_sample_size = Column(Text())
    sampled_at_site = Column(UUID(), ForeignKey('Site.id'))
    

    

    def __repr__(self):
        return f"TerraformSamplingActivity(collection_time={self.collection_time},sample_collected={self.sample_collected},sample_collection_method={self.sample_collection_method},id={self.id},name={self.name},description={self.description},project={self.project},emsl_activity={self.emsl_activity},collection_date={self.collection_date},shipped_sample_size={self.shipped_sample_size},sampled_at_site={self.sampled_at_site},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class WaterSamplingActivity(SamplingActivity):
    """
    Collection of water samples.
    """
    __tablename__ = 'WaterSamplingActivity'

    collection_time = Column(Text())
    sample_collected = Column(Text())
    sample_collection_dev = Column(Text(), nullable=False )
    sample_collection_method = Column(Text(), nullable=False )
    id = Column(UUID(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    emsl_activity = Column(Text())
    collection_date = Column(Date())
    shipped_sample_size = Column(Text())
    sampled_at_site = Column(UUID(), ForeignKey('Site.id'))
    

    

    def __repr__(self):
        return f"WaterSamplingActivity(collection_time={self.collection_time},sample_collected={self.sample_collected},sample_collection_dev={self.sample_collection_dev},sample_collection_method={self.sample_collection_method},id={self.id},name={self.name},description={self.description},project={self.project},emsl_activity={self.emsl_activity},collection_date={self.collection_date},shipped_sample_size={self.shipped_sample_size},sampled_at_site={self.sampled_at_site},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class XRFDataGenerationActivity(XRayDataGenerationActivity):
    """
    X-ray Fluorescence (XRF) elemental analysis activity.

XRF measures elemental composition by detecting characteristic X-ray emissions
from a sample bombarded with high-energy X-rays. Typical output: concentrations
of 10-30 elements per sample (Ni, Pb, As, Cr, Fe, Ca, K, etc.).

Data product: XRFElementalProduct (one row per element per sample)

Workflow pattern: Direct instrument output (no computational processing step)
  processedSample -> XRFDataGenerationActivity -> XRFElementalProduct (workflow_id = NULL)

Protocol information: Stored externally; link via protocol_url attribute.
Example protocol parameters (stored in external SOP or DataProcessingActivity
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
    __tablename__ = 'XRFDataGenerationActivity'

    sequence_order = Column(Integer())
    name = Column(Text(), nullable=False )
    description = Column(Text())
    protocol_url = Column(Text())
    protocol_version = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analyte_id = Column(UUID(), ForeignKey('ProcessedSample.id'))
    acquisition_start_time = Column(DateTime(), nullable=False )
    acquisition_end_time = Column(DateTime(), nullable=False )
    instrument_used = Column(UUID(), ForeignKey('Instrument.id'))
    instrument_operator_id = Column(UUID(), ForeignKey('PersonValue.id'))
    

    

    def __repr__(self):
        return f"XRFDataGenerationActivity(sequence_order={self.sequence_order},name={self.name},description={self.description},protocol_url={self.protocol_url},protocol_version={self.protocol_version},id={self.id},analyte_id={self.analyte_id},acquisition_start_time={self.acquisition_start_time},acquisition_end_time={self.acquisition_end_time},instrument_used={self.instrument_used},instrument_operator_id={self.instrument_operator_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class XRDDataGenerationActivity(XRayDataGenerationActivity):
    """
    X-ray Diffraction (XRD) mineralogical analysis activity.

XRD identifies crystalline mineral phases by measuring diffraction patterns.
Output: mineral phase names and quantitative abundances (weight %).

Data product: XRDPhaseProduct (one row per mineral phase per sample)

Workflow patterns:
  1. Direct/semi-quantitative: 
       processedSample -> XRDDataGenerationActivity -> XRDPhaseProduct (workflow_id = NULL)
  2. With Rietveld refinement (computational):
       processedSample -> XRDDataGenerationActivity -> 
       DataProcessingActivity(type='xrd_rietveld_refinement') -> 
       XRDPhaseProduct (workflow_id = refinement WEA)

Protocol information: Stored externally; link via protocol_url attribute.
Example protocol parameters (stored in external SOP or DataProcessingActivity):
  - Diffractometer geometry (Bragg-Brentano, Debye-Scherrer)
  - X-ray tube type (Cu, Co, Mo)
  - Scan range (2-theta degrees), step size
  - Refinement software (HighScore Plus, GSAS-II, FullProf)
  - R-factor, GOF (goodness of fit)

Required enum additions to enums.yaml:
  routemethod:
    xrd_analysis:  # Add to routemethod permissible_values
    """
    __tablename__ = 'XRDDataGenerationActivity'

    sequence_order = Column(Integer())
    name = Column(Text(), nullable=False )
    description = Column(Text())
    protocol_url = Column(Text())
    protocol_version = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analyte_id = Column(UUID(), ForeignKey('ProcessedSample.id'))
    acquisition_start_time = Column(DateTime(), nullable=False )
    acquisition_end_time = Column(DateTime(), nullable=False )
    instrument_used = Column(UUID(), ForeignKey('Instrument.id'))
    instrument_operator_id = Column(UUID(), ForeignKey('PersonValue.id'))
    

    

    def __repr__(self):
        return f"XRDDataGenerationActivity(sequence_order={self.sequence_order},name={self.name},description={self.description},protocol_url={self.protocol_url},protocol_version={self.protocol_version},id={self.id},analyte_id={self.analyte_id},acquisition_start_time={self.acquisition_start_time},acquisition_end_time={self.acquisition_end_time},instrument_used={self.instrument_used},instrument_operator_id={self.instrument_operator_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MassSpectrometryInstrumentData(InstrumentData):
    """
    Raw data files output from a mass spectrometry instrument.
    """
    __tablename__ = 'MassSpectrometryInstrumentData'

    produced_by_ms_run = Column(UUID(), ForeignKey('MassSpectrometryDataGenerationActivity.id'))
    ms_raw_file_type = Column(Enum('.d', '.raw', 'other', name='MassSpecRawFileTypeEnum'))
    collection_mode = Column(Enum('full_profile', 'reduced_profile', 'centroid', name='MassSpectrumCollectionModeEnum'))
    file_curie = Column(Text())
    alternative_identifiers = Column(Text())
    compression_type = Column(Text())
    file_type = Column(Enum('FT_ICR_MS_Analysis_Results', 'GC_MS_Metabolomics_Results', 'Metaproteomics_Workflow_Statistics', 'Protein_Report', 'Peptide_Report', 'Unfiltered_Metaproteomics_Results', 'Read_Count_and_RPKM', 'QC_non_rRNA_R2', 'QC_non_rRNA_R1', 'Metagenome_Bins', 'CheckM_Statistics', 'GOTTCHA2_Krona_Plot', 'Kraken2_Krona_Plot', 'Centrifuge_Krona_Plot', 'Kraken2_Classification_Report', 'Kraken2_Taxonomic_Classification', 'Centrifuge_Classification_Report', 'Centrifuge_Taxonomic_Classification', 'Structural_Annotation_GFF', 'Functional_Annotation_GFF', 'Annotation_Amino_Acid_FASTA', 'Annotation_Enzyme_Commission', 'Annotation_KEGG_Orthology', 'Assembly_Coverage_BAM', 'Assembly_AGP', 'Assembly_Scaffolds', 'Assembly_Contigs', 'Assembly_Coverage_Stats', 'Filtered_Sequencing_Reads', 'QC_Statistics', 'TIGRFam_Annotation_GFF', 'Clusters_of_Orthologous_Groups_COG_Annotation_GFF', 'CATH_FunFams_Functional_Families_Annotation_GFF', 'SUPERFam_Annotation_GFF', 'SMART_Annotation_GFF', 'Pfam_Annotation_GFF', 'Direct_Infusion_FT_ICR_MS_Raw_Data', name='FileTypeEnum'))
    software_version = Column(Text())
    name = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"MassSpectrometryInstrumentData(produced_by_ms_run={self.produced_by_ms_run},ms_raw_file_type={self.ms_raw_file_type},collection_mode={self.collection_mode},file_curie={self.file_curie},alternative_identifiers={self.alternative_identifiers},compression_type={self.compression_type},file_type={self.file_type},software_version={self.software_version},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
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

    results_from_ms_processing = Column(UUID(), ForeignKey('MassSpectrometryDataProcessingActivity.id'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"MassSpectrometryDataProduct(results_from_ms_processing={self.results_from_ms_processing},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},sample_id={self.sample_id},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
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
    """
    __tablename__ = 'StrainPurity'

    inspection_method = Column(Text())
    target_strain = Column(Text())
    contaminant_strains = Column(Text())
    biological_entity_ref = Column(UUID(), ForeignKey('biological_entity.id'))
    growth_medium = Column(Text())
    incubation_time_hours = Column(Float())
    container_type = Column(Text())
    temperature_celsius = Column(Float())
    agitation_speed_rpm = Column(Integer())
    oxygen_status = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'obligate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    protocol_url = Column(Text())
    protocol_version = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analysis_type = Column(Enum('analysis_activity', 'lcms_metabolomics_method', 'fticr_acquisition_method', 'gravimetric_water_content_method', 'ph_method', 'hydraulic_properties_method', 'microbial_biomass_method', 'xray_computed_tomography_method', 'REGEN', 'KUO', 'respiration_method', 'texture_method', 'enzyme_activity_method', 'elemental_analysis_method', 'toc_tn_method', 'bulk_density_method', 'metagenomics_method', 'xrf_analysis', 'xrd_analysis', name='RouteMethodEnum'))
    method_name = Column(Enum('MAOM', 'WOEM', name='MethodNameEnum'))
    processing_steps = Column(Text(), nullable=False )
    uses_sample = Column(UUID(), ForeignKey('Sample.id'))
    

    

    def __repr__(self):
        return f"StrainPurity(inspection_method={self.inspection_method},target_strain={self.target_strain},contaminant_strains={self.contaminant_strains},biological_entity_ref={self.biological_entity_ref},growth_medium={self.growth_medium},incubation_time_hours={self.incubation_time_hours},container_type={self.container_type},temperature_celsius={self.temperature_celsius},agitation_speed_rpm={self.agitation_speed_rpm},oxygen_status={self.oxygen_status},protocol_url={self.protocol_url},protocol_version={self.protocol_version},id={self.id},analysis_type={self.analysis_type},method_name={self.method_name},processing_steps={self.processing_steps},uses_sample={self.uses_sample},)"



    
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
    """
    __tablename__ = 'StockCulturePreparation'

    preparation_date = Column(Date())
    biological_entity_ref = Column(UUID(), ForeignKey('biological_entity.id'))
    growth_medium = Column(Text())
    incubation_time_hours = Column(Float())
    container_type = Column(Text())
    temperature_celsius = Column(Float())
    agitation_speed_rpm = Column(Integer())
    oxygen_status = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'obligate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    protocol_url = Column(Text())
    protocol_version = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analysis_type = Column(Enum('analysis_activity', 'lcms_metabolomics_method', 'fticr_acquisition_method', 'gravimetric_water_content_method', 'ph_method', 'hydraulic_properties_method', 'microbial_biomass_method', 'xray_computed_tomography_method', 'REGEN', 'KUO', 'respiration_method', 'texture_method', 'enzyme_activity_method', 'elemental_analysis_method', 'toc_tn_method', 'bulk_density_method', 'metagenomics_method', 'xrf_analysis', 'xrd_analysis', name='RouteMethodEnum'))
    method_name = Column(Enum('MAOM', 'WOEM', name='MethodNameEnum'))
    processing_steps = Column(Text(), nullable=False )
    uses_sample = Column(UUID(), ForeignKey('Sample.id'))
    

    

    def __repr__(self):
        return f"StockCulturePreparation(preparation_date={self.preparation_date},biological_entity_ref={self.biological_entity_ref},growth_medium={self.growth_medium},incubation_time_hours={self.incubation_time_hours},container_type={self.container_type},temperature_celsius={self.temperature_celsius},agitation_speed_rpm={self.agitation_speed_rpm},oxygen_status={self.oxygen_status},protocol_url={self.protocol_url},protocol_version={self.protocol_version},id={self.id},analysis_type={self.analysis_type},method_name={self.method_name},processing_steps={self.processing_steps},uses_sample={self.uses_sample},)"



    
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
    """
    __tablename__ = 'PreCultureGrowth'

    biological_entity_ref = Column(UUID(), ForeignKey('biological_entity.id'))
    growth_medium = Column(Text())
    incubation_time_hours = Column(Float())
    container_type = Column(Text())
    temperature_celsius = Column(Float())
    agitation_speed_rpm = Column(Integer())
    oxygen_status = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'obligate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    protocol_url = Column(Text())
    protocol_version = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analysis_type = Column(Enum('analysis_activity', 'lcms_metabolomics_method', 'fticr_acquisition_method', 'gravimetric_water_content_method', 'ph_method', 'hydraulic_properties_method', 'microbial_biomass_method', 'xray_computed_tomography_method', 'REGEN', 'KUO', 'respiration_method', 'texture_method', 'enzyme_activity_method', 'elemental_analysis_method', 'toc_tn_method', 'bulk_density_method', 'metagenomics_method', 'xrf_analysis', 'xrd_analysis', name='RouteMethodEnum'))
    method_name = Column(Enum('MAOM', 'WOEM', name='MethodNameEnum'))
    processing_steps = Column(Text(), nullable=False )
    uses_sample = Column(UUID(), ForeignKey('Sample.id'))
    

    

    def __repr__(self):
        return f"PreCultureGrowth(biological_entity_ref={self.biological_entity_ref},growth_medium={self.growth_medium},incubation_time_hours={self.incubation_time_hours},container_type={self.container_type},temperature_celsius={self.temperature_celsius},agitation_speed_rpm={self.agitation_speed_rpm},oxygen_status={self.oxygen_status},protocol_url={self.protocol_url},protocol_version={self.protocol_version},id={self.id},analysis_type={self.analysis_type},method_name={self.method_name},processing_steps={self.processing_steps},uses_sample={self.uses_sample},)"



    
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
    """
    __tablename__ = 'ExperimentalCulture'

    treatment_type = Column(Text())
    growth_time = Column(Text())
    biological_entity_ref = Column(UUID(), ForeignKey('biological_entity.id'))
    growth_medium = Column(Text())
    incubation_time_hours = Column(Float())
    container_type = Column(Text())
    temperature_celsius = Column(Float())
    agitation_speed_rpm = Column(Integer())
    oxygen_status = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'obligate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    protocol_url = Column(Text())
    protocol_version = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analysis_type = Column(Enum('analysis_activity', 'lcms_metabolomics_method', 'fticr_acquisition_method', 'gravimetric_water_content_method', 'ph_method', 'hydraulic_properties_method', 'microbial_biomass_method', 'xray_computed_tomography_method', 'REGEN', 'KUO', 'respiration_method', 'texture_method', 'enzyme_activity_method', 'elemental_analysis_method', 'toc_tn_method', 'bulk_density_method', 'metagenomics_method', 'xrf_analysis', 'xrd_analysis', name='RouteMethodEnum'))
    method_name = Column(Enum('MAOM', 'WOEM', name='MethodNameEnum'))
    processing_steps = Column(Text(), nullable=False )
    uses_sample = Column(UUID(), ForeignKey('Sample.id'))
    

    

    def __repr__(self):
        return f"ExperimentalCulture(treatment_type={self.treatment_type},growth_time={self.growth_time},biological_entity_ref={self.biological_entity_ref},growth_medium={self.growth_medium},incubation_time_hours={self.incubation_time_hours},container_type={self.container_type},temperature_celsius={self.temperature_celsius},agitation_speed_rpm={self.agitation_speed_rpm},oxygen_status={self.oxygen_status},protocol_url={self.protocol_url},protocol_version={self.protocol_version},id={self.id},analysis_type={self.analysis_type},method_name={self.method_name},processing_steps={self.processing_steps},uses_sample={self.uses_sample},)"



    
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
    setup_operator_id = Column(UUID(), ForeignKey('PersonValue.id'))
    setup_instrument = Column(Text())
    sealing_method = Column(Text())
    temperature_celsius = Column(Float())
    agitation_speed_rpm = Column(Integer())
    oxygen_status = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'obligate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    protocol_url = Column(Text())
    protocol_version = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analysis_type = Column(Enum('analysis_activity', 'lcms_metabolomics_method', 'fticr_acquisition_method', 'gravimetric_water_content_method', 'ph_method', 'hydraulic_properties_method', 'microbial_biomass_method', 'xray_computed_tomography_method', 'REGEN', 'KUO', 'respiration_method', 'texture_method', 'enzyme_activity_method', 'elemental_analysis_method', 'toc_tn_method', 'bulk_density_method', 'metagenomics_method', 'xrf_analysis', 'xrd_analysis', name='RouteMethodEnum'))
    method_name = Column(Enum('MAOM', 'WOEM', name='MethodNameEnum'))
    processing_steps = Column(Text(), nullable=False )
    uses_sample = Column(UUID(), ForeignKey('Sample.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='AMP2PlateSetupActivity', source_slot='well_metadata', mapping_type=None, target_class='WellMetadata', target_slot='AMP2PlateSetupActivity_id', join_class=None, uses_join_table=None, multivalued=False)
    well_metadata = relationship( "WellMetadata", foreign_keys="[WellMetadata.AMP2PlateSetupActivity_id]")
    

    

    def __repr__(self):
        return f"AMP2PlateSetupActivity(media_ref={self.media_ref},plate_type={self.plate_type},plate_barcode={self.plate_barcode},setup_date={self.setup_date},setup_operator_id={self.setup_operator_id},setup_instrument={self.setup_instrument},sealing_method={self.sealing_method},temperature_celsius={self.temperature_celsius},agitation_speed_rpm={self.agitation_speed_rpm},oxygen_status={self.oxygen_status},protocol_url={self.protocol_url},protocol_version={self.protocol_version},id={self.id},analysis_type={self.analysis_type},method_name={self.method_name},processing_steps={self.processing_steps},uses_sample={self.uses_sample},)"



    
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
    setup_operator_id = Column(UUID(), ForeignKey('PersonValue.id'))
    setup_instrument = Column(Text())
    sealing_method = Column(Text())
    temperature_celsius = Column(Float())
    agitation_speed_rpm = Column(Integer())
    oxygen_status = Column(Enum('aerobic', 'anaerobic', 'anoxic', 'facultative', 'microaerophilic', 'microanaerobe', 'obligate_aerobe', 'obligate_anaerobe', name='OxygenStatusEnum'))
    protocol_url = Column(Text())
    protocol_version = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analysis_type = Column(Enum('analysis_activity', 'lcms_metabolomics_method', 'fticr_acquisition_method', 'gravimetric_water_content_method', 'ph_method', 'hydraulic_properties_method', 'microbial_biomass_method', 'xray_computed_tomography_method', 'REGEN', 'KUO', 'respiration_method', 'texture_method', 'enzyme_activity_method', 'elemental_analysis_method', 'toc_tn_method', 'bulk_density_method', 'metagenomics_method', 'xrf_analysis', 'xrd_analysis', name='RouteMethodEnum'))
    method_name = Column(Enum('MAOM', 'WOEM', name='MethodNameEnum'))
    processing_steps = Column(Text(), nullable=False )
    uses_sample = Column(UUID(), ForeignKey('Sample.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='EcoplatePlateSetupActivity', source_slot='well_metadata', mapping_type=None, target_class='WellMetadata', target_slot='EcoplatePlateSetupActivity_id', join_class=None, uses_join_table=None, multivalued=False)
    well_metadata = relationship( "WellMetadata", foreign_keys="[WellMetadata.EcoplatePlateSetupActivity_id]")
    

    

    def __repr__(self):
        return f"EcoplatePlateSetupActivity(plate_type={self.plate_type},plate_barcode={self.plate_barcode},setup_date={self.setup_date},setup_operator_id={self.setup_operator_id},setup_instrument={self.setup_instrument},sealing_method={self.sealing_method},temperature_celsius={self.temperature_celsius},agitation_speed_rpm={self.agitation_speed_rpm},oxygen_status={self.oxygen_status},protocol_url={self.protocol_url},protocol_version={self.protocol_version},id={self.id},analysis_type={self.analysis_type},method_name={self.method_name},processing_steps={self.processing_steps},uses_sample={self.uses_sample},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class AMP2DataGenerationActivity(PlateDataGenerationActivity):
    """
    AMP2 plate measurement (OD, fluorescence, flow cytometry).
analyte_id -> processedSample(type='amp2_96well_plate')

Chained via DataProcessingActivity.parent_workflow_id to track
multi-timepoint series on the same plate.

v1 origin: plate-general.yaml AMP2DataGenerationActivity
    """
    __tablename__ = 'AMP2DataGenerationActivity'

    measurement_type = Column(Text())
    wavelength_nm = Column(Integer(), nullable=False )
    timepoint_label = Column(Text(), nullable=False )
    sequence_order = Column(Integer())
    name = Column(Text(), nullable=False )
    description = Column(Text())
    protocol_url = Column(Text())
    protocol_version = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analyte_id = Column(UUID(), ForeignKey('ProcessedSample.id'))
    acquisition_start_time = Column(DateTime(), nullable=False )
    acquisition_end_time = Column(DateTime(), nullable=False )
    instrument_used = Column(UUID(), ForeignKey('Instrument.id'))
    instrument_operator_id = Column(UUID(), ForeignKey('PersonValue.id'))
    

    

    def __repr__(self):
        return f"AMP2DataGenerationActivity(measurement_type={self.measurement_type},wavelength_nm={self.wavelength_nm},timepoint_label={self.timepoint_label},sequence_order={self.sequence_order},name={self.name},description={self.description},protocol_url={self.protocol_url},protocol_version={self.protocol_version},id={self.id},analyte_id={self.analyte_id},acquisition_start_time={self.acquisition_start_time},acquisition_end_time={self.acquisition_end_time},instrument_used={self.instrument_used},instrument_operator_id={self.instrument_operator_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class EcoplateDataGenerationActivity(PlateDataGenerationActivity):
    """
    Ecoplate absorbance measurement at a single timepoint.
analyte_id -> processedSample(type='ecoplate_plate')
wavelength_nm typically 590 for Biolog EcoPlates.

v1 origin: plate-general.yaml EcoplateDataGenerationActivity
    """
    __tablename__ = 'EcoplateDataGenerationActivity'

    wavelength_nm = Column(Integer(), nullable=False )
    timepoint_label = Column(Text(), nullable=False )
    sequence_order = Column(Integer())
    name = Column(Text(), nullable=False )
    description = Column(Text())
    protocol_url = Column(Text())
    protocol_version = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    analyte_id = Column(UUID(), ForeignKey('ProcessedSample.id'))
    acquisition_start_time = Column(DateTime(), nullable=False )
    acquisition_end_time = Column(DateTime(), nullable=False )
    instrument_used = Column(UUID(), ForeignKey('Instrument.id'))
    instrument_operator_id = Column(UUID(), ForeignKey('PersonValue.id'))
    

    

    def __repr__(self):
        return f"EcoplateDataGenerationActivity(wavelength_nm={self.wavelength_nm},timepoint_label={self.timepoint_label},sequence_order={self.sequence_order},name={self.name},description={self.description},protocol_url={self.protocol_url},protocol_version={self.protocol_version},id={self.id},analyte_id={self.analyte_id},acquisition_start_time={self.acquisition_start_time},acquisition_end_time={self.acquisition_end_time},instrument_used={self.instrument_used},instrument_operator_id={self.instrument_operator_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class NucleotideSequencingInstrumentData(InstrumentData):
    """
    Data generated by a nucleotide sequencing instrument (e.g., raw FASTQ files).
    """
    __tablename__ = 'NucleotideSequencingInstrumentData'

    produced_by_sequencing_activity = Column(UUID(), ForeignKey('NucleotideSequencing.id'))
    file_curie = Column(Text())
    alternative_identifiers = Column(Text())
    compression_type = Column(Text())
    file_type = Column(Enum('FT_ICR_MS_Analysis_Results', 'GC_MS_Metabolomics_Results', 'Metaproteomics_Workflow_Statistics', 'Protein_Report', 'Peptide_Report', 'Unfiltered_Metaproteomics_Results', 'Read_Count_and_RPKM', 'QC_non_rRNA_R2', 'QC_non_rRNA_R1', 'Metagenome_Bins', 'CheckM_Statistics', 'GOTTCHA2_Krona_Plot', 'Kraken2_Krona_Plot', 'Centrifuge_Krona_Plot', 'Kraken2_Classification_Report', 'Kraken2_Taxonomic_Classification', 'Centrifuge_Classification_Report', 'Centrifuge_Taxonomic_Classification', 'Structural_Annotation_GFF', 'Functional_Annotation_GFF', 'Annotation_Amino_Acid_FASTA', 'Annotation_Enzyme_Commission', 'Annotation_KEGG_Orthology', 'Assembly_Coverage_BAM', 'Assembly_AGP', 'Assembly_Scaffolds', 'Assembly_Contigs', 'Assembly_Coverage_Stats', 'Filtered_Sequencing_Reads', 'QC_Statistics', 'TIGRFam_Annotation_GFF', 'Clusters_of_Orthologous_Groups_COG_Annotation_GFF', 'CATH_FunFams_Functional_Families_Annotation_GFF', 'SUPERFam_Annotation_GFF', 'SMART_Annotation_GFF', 'Pfam_Annotation_GFF', 'Direct_Infusion_FT_ICR_MS_Raw_Data', name='FileTypeEnum'))
    software_version = Column(Text())
    name = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"NucleotideSequencingInstrumentData(produced_by_sequencing_activity={self.produced_by_sequencing_activity},file_curie={self.file_curie},alternative_identifiers={self.alternative_identifiers},compression_type={self.compression_type},file_type={self.file_type},software_version={self.software_version},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
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

    mg_workflow_step = Column(Enum('ReadQcAnalysis', 'MetagenomeAssembly', 'ReadBasedTaxonomyAnalysis', 'MetagenomeAnnotation', 'MagsAnalysis', 'FunctionalAnnotation', 'GenePhylogeny', name='MetagenomicsSteps'))
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    provider_name = Column(Text(), ForeignKey('ControlledTermValue.id'))
    raw_fasta_url = Column(Text())
    additional_information = Column(Text())
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"MetagenomicsProduct(mg_workflow_step={self.mg_workflow_step},sample_id={self.sample_id},provider_name={self.provider_name},raw_fasta_url={self.raw_fasta_url},additional_information={self.additional_information},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class BulkDensityProduct(ProcessedData):
    """
    Bulk density analysis product, typically derived via oven-drying and weighing of a known volume of soil.
One row per sample with columns for bulk density and QC flag.
    """
    __tablename__ = 'BulkDensityProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='ProductMeasureType'))
    bulk_density_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    flag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"BulkDensityProduct(measure_type={self.measure_type},bulk_density_id={self.bulk_density_id},flag={self.flag},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},sample_id={self.sample_id},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ElementalAnalysisProduct(ProcessedData):
    """
    Elemental analysis product, typically derived via combustion or similar instrument.
One row per sample with columns for total carbon, total nitrogen, total Kjeldahl nitrogen, and total sulfur.
Individual QC flags for each measurement using ProcessedDataFlag enum.
    """
    __tablename__ = 'ElementalAnalysisProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='ProductMeasureType'))
    total_carbon_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    total_nitrogen_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    total_kjeldahl_nitrogen_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    total_sulfur_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    flag_total_carbon = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_total_nitrogen = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_tkn = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_total_sulfur = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"ElementalAnalysisProduct(measure_type={self.measure_type},total_carbon_id={self.total_carbon_id},total_nitrogen_id={self.total_nitrogen_id},total_kjeldahl_nitrogen_id={self.total_kjeldahl_nitrogen_id},total_sulfur_id={self.total_sulfur_id},flag_total_carbon={self.flag_total_carbon},flag_total_nitrogen={self.flag_total_nitrogen},flag_tkn={self.flag_tkn},flag_total_sulfur={self.flag_total_sulfur},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},sample_id={self.sample_id},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class EnzymeProduct(ProcessedData):
    """
    Enzyme activity analysis product, typically derived via colorimetric assay of soil extracts.
One row per sample with columns for beta-glucosidase activity and QC flag.
    """
    __tablename__ = 'EnzymeProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='ProductMeasureType'))
    beta_glucosidase_ug_pnp_per_g_per_h_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    flag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"EnzymeProduct(measure_type={self.measure_type},beta_glucosidase_ug_pnp_per_g_per_h_id={self.beta_glucosidase_ug_pnp_per_g_per_h_id},flag={self.flag},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},sample_id={self.sample_id},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class GWCMoistureProduct(ProcessedData):
    """
    Gravimetric water content (GWC) analysis product, typically derived via oven-drying and weighing of a known mass of soil.
One row per sample with columns for GWC and QC flag.
    """
    __tablename__ = 'GWCMoistureProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='ProductMeasureType'))
    gwc_percent_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    flag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"GWCMoistureProduct(measure_type={self.measure_type},gwc_percent_id={self.gwc_percent_id},flag={self.flag},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},sample_id={self.sample_id},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class HydraulicPropertiesProduct(ProcessedData):
    """
    Soil hydraulic parameters derived from HYPROP evaporation-experiment data. One row per core section; the four attributes are the four VGM model parameters.  Proposal_ID, sampling_set, and core_section are inherited from the parent processedData record.
    """
    __tablename__ = 'HydraulicPropertiesProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='ProductMeasureType'))
    alpha = Column(Float())
    n = Column(Float())
    theta_r = Column(Float())
    theta_s = Column(Float())
    flag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"HydraulicPropertiesProduct(measure_type={self.measure_type},alpha={self.alpha},n={self.n},theta_r={self.theta_r},theta_s={self.theta_s},flag={self.flag},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},sample_id={self.sample_id},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class IonsAnalysisProduct(ProcessedData):
    """
    Ions analysis product, typically derived via ICP-OES or similar instrument.
One row per sample with columns for each ion measured.
Individual QC flags for each ion using ProcessedDataFlag enum.
    """
    __tablename__ = 'IonsAnalysisProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='ProductMeasureType'))
    sulfate_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    boron_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    zinc_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    manganate_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    copper_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    iron_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    calcium_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    magnesium_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    sodium_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    potassium_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    total_bases_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    cation_exchange_capacity_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    flag_sulfate = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_boron = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_zinc = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_manganate = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_copper = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_iron = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_calcium = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_magnesium = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_sodium = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_potassium = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_total_bases = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_cec = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"IonsAnalysisProduct(measure_type={self.measure_type},sulfate_id={self.sulfate_id},boron_id={self.boron_id},zinc_id={self.zinc_id},manganate_id={self.manganate_id},copper_id={self.copper_id},iron_id={self.iron_id},calcium_id={self.calcium_id},magnesium_id={self.magnesium_id},sodium_id={self.sodium_id},potassium_id={self.potassium_id},total_bases_id={self.total_bases_id},cation_exchange_capacity_id={self.cation_exchange_capacity_id},flag_sulfate={self.flag_sulfate},flag_boron={self.flag_boron},flag_zinc={self.flag_zinc},flag_manganate={self.flag_manganate},flag_copper={self.flag_copper},flag_iron={self.flag_iron},flag_calcium={self.flag_calcium},flag_magnesium={self.flag_magnesium},flag_sodium={self.flag_sodium},flag_potassium={self.flag_potassium},flag_total_bases={self.flag_total_bases},flag_cec={self.flag_cec},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},sample_id={self.sample_id},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MicrobialBiomassProduct(ProcessedData):
    """
    Microbial biomass analysis product, typically derived via chloroform fumigation-extraction (CFE) or similar instrument.
One row per sample with columns for microbial biomass carbon and nitrogen.
Individual QC flags for each measurement using ProcessedDataFlag enum.
    """
    __tablename__ = 'MicrobialBiomassProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='ProductMeasureType'))
    replicate = Column(Integer())
    mbc_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    mbc_avg = Column(Float())
    mbn_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    mbn_avg = Column(Float())
    flag_mbc = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_mbn = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_mbc_avg = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_mbn_avg = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"MicrobialBiomassProduct(measure_type={self.measure_type},replicate={self.replicate},mbc_id={self.mbc_id},mbc_avg={self.mbc_avg},mbn_id={self.mbn_id},mbn_avg={self.mbn_avg},flag_mbc={self.flag_mbc},flag_mbn={self.flag_mbn},flag_mbc_avg={self.flag_mbc_avg},flag_mbn_avg={self.flag_mbn_avg},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},sample_id={self.sample_id},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class NitrogenAnalysisProduct(ProcessedData):
    """
    Nitrogen analysis product, typically derived via colorimetric assay of soil extracts.
One row per sample with columns for nitrate and ammonium concentrations.
Individual QC flags for each measurement using ProcessedDataFlag enum.
    """
    __tablename__ = 'NitrogenAnalysisProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='ProductMeasureType'))
    replicate = Column(Integer())
    no3_n_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    no3_n_avg = Column(Float())
    nh4_n_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    nh4_n_avg = Column(Float())
    flag_no3n = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_nh4n = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_no3n_avg = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_nh4n_avg = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"NitrogenAnalysisProduct(measure_type={self.measure_type},replicate={self.replicate},no3_n_id={self.no3_n_id},no3_n_avg={self.no3_n_avg},nh4_n_id={self.nh4_n_id},nh4_n_avg={self.nh4_n_avg},flag_no3n={self.flag_no3n},flag_nh4n={self.flag_nh4n},flag_no3n_avg={self.flag_no3n_avg},flag_nh4n_avg={self.flag_nh4n_avg},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},sample_id={self.sample_id},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class PhosphorusAnalysisProduct(ProcessedData):
    """
    Phosphorus analysis product, typically derived via colorimetric assay of soil extracts.
One row per sample with columns for phosphorus concentration.
Individual QC flags for each measurement using ProcessedDataFlag enum.
    """
    __tablename__ = 'PhosphorusAnalysisProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='ProductMeasureType'))
    replicate = Column(Integer())
    extraction_method = Column(Text())
    phosphorus_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    phosphorus_avg = Column(Float())
    flag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_avg = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"PhosphorusAnalysisProduct(measure_type={self.measure_type},replicate={self.replicate},extraction_method={self.extraction_method},phosphorus_id={self.phosphorus_id},phosphorus_avg={self.phosphorus_avg},flag={self.flag},flag_avg={self.flag_avg},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},sample_id={self.sample_id},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class RespirationProduct(ProcessedData):
    """
    Soil respiration analysis product.
One row per sample with columns for soil respiration and QC flag.
    """
    __tablename__ = 'RespirationProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='ProductMeasureType'))
    respiration_co2_c_ug_per_g = Column(Float())
    flag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"RespirationProduct(measure_type={self.measure_type},respiration_co2_c_ug_per_g={self.respiration_co2_c_ug_per_g},flag={self.flag},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},sample_id={self.sample_id},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class TextureProduct(ProcessedData):
    """
    Soil texture analysis product, typically derived via hydrometer or similar instrument.
One row per sample with columns for sand, silt, and clay percentages.
Individual QC flags for each measurement using ProcessedDataFlag enum.
    """
    __tablename__ = 'TextureProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='ProductMeasureType'))
    sand_pct_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    silt_pct_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    clay_pct_id = Column(UUID(), ForeignKey('QuantityValue.id'))
    flag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"TextureProduct(measure_type={self.measure_type},sand_pct_id={self.sand_pct_id},silt_pct_id={self.silt_pct_id},clay_pct_id={self.clay_pct_id},flag={self.flag},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},sample_id={self.sample_id},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class TomographyProduct(ProcessedData):
    """
    Soil tomography analysis product, typically derived via X-ray computed tomography (XCT) or similar instrument.
One row per sample with columns for pore structure metrics and QC flag.
    """
    __tablename__ = 'TomographyProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='ProductMeasureType'))
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
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"TomographyProduct(measure_type={self.measure_type},roi_volume_voxel={self.roi_volume_voxel},voxel_size={self.voxel_size},connected_pores={self.connected_pores},pore_diameter_min={self.pore_diameter_min},pore_diameter_max={self.pore_diameter_max},pore_diameter_mean={self.pore_diameter_mean},pore_diameter_median={self.pore_diameter_median},pore_diameter_variance={self.pore_diameter_variance},pore_volume_mean={self.pore_volume_mean},total_pore_volume={self.total_pore_volume},permeability_x={self.permeability_x},flow_rate_x={self.flow_rate_x},tortuosity_x={self.tortuosity_x},permeability_y={self.permeability_y},flow_rate_y={self.flow_rate_y},tortuosity_y={self.tortuosity_y},permeability_z={self.permeability_z},flow_rate_z={self.flow_rate_z},tortuosity_z={self.tortuosity_z},flag_xct={self.flag_xct},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},sample_id={self.sample_id},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class PHProduct(ProcessedData):
    """
    Soil pH analysis product, typically derived via pH meter or similar instrument.
One row per sample with columns for pH and QC flag.
    """
    __tablename__ = 'pHProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='ProductMeasureType'))
    ph = Column(Float())
    flag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"pHProduct(measure_type={self.measure_type},ph={self.ph},flag={self.flag},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},sample_id={self.sample_id},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class XRayDataProduct(ProcessedData):
    """
    Abstract base class for X-ray analytical data products.
Inherits S3 storage metadata and sample linkage from dataProduct via ProcessedData.

Concrete subclasses:
  - XRFElementalProduct: elemental concentrations (one row per sample)
  - XRDPhaseProduct: mineral phases (one row per sample)

Common patterns:
  - s3_key points to raw spectrum/diffractogram file in MinIO
  - summary_metrics provides lightweight queryable summaries:
      XRF: {"Ni_mg_kg":45.3, "Pb_mg_kg":8.2, "As_mg_kg":12.1}
      XRD: {"quartz_percent":42, "albite_percent":18, "kaolinite_percent":31}
  - workflow_id is NULL for direct instrument output (XRF typical)
  - workflow_id links to DataProcessingActivity for computational processing (XRD Rietveld) 
    """
    __tablename__ = 'XRayDataProduct'

    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"XRayDataProduct(summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},sample_id={self.sample_id},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class CoreSection(ProcessedSample):
    """
    A section of a core sample (TOP, MID, BTM).
    """
    __tablename__ = 'CoreSection'

    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'), nullable=False )
    id = Column(UUID(), primary_key=True, nullable=False )
    storage_location = Column(Text())
    label_text = Column(Text())
    concentration_ug_per_uL = Column(Float())
    total_amount_ug = Column(Float())
    volume_uL = Column(Float())
    sampled_portion = Column(Enum('supernatant', 'pellet', 'organic_layer', 'aqueous_layer', 'interlayer', 'chloroform_layer', 'methanol_layer', name='SamplePortionEnum'))
    sampled_during = Column(UUID(), ForeignKey('SampleProcessing.id'))
    replicate = Column(Integer())
    name = Column(Text(), nullable=False )
    description = Column(Text())
    emsl_activity = Column(Text())
    lims_barcode = Column(Text())
    

    

    def __repr__(self):
        return f"CoreSection(core_section={self.core_section},id={self.id},storage_location={self.storage_location},label_text={self.label_text},concentration_ug_per_uL={self.concentration_ug_per_uL},total_amount_ug={self.total_amount_ug},volume_uL={self.volume_uL},sampled_portion={self.sampled_portion},sampled_during={self.sampled_during},replicate={self.replicate},name={self.name},description={self.description},emsl_activity={self.emsl_activity},lims_barcode={self.lims_barcode},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MSImageProduct(MassSpectrometryDataProduct):
    """
    one or more image(s) output from a mass spec data processing workflow (eg. LESA, CoreMS QC plots). Should be a zip file containing all similar image outputs from one data processing workflow.
    """
    __tablename__ = 'MSImageProduct'

    results_from_ms_processing = Column(UUID(), ForeignKey('MassSpectrometryDataProcessingActivity.id'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"MSImageProduct(results_from_ms_processing={self.results_from_ms_processing},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},sample_id={self.sample_id},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MolecularIdentificationProduct(MassSpectrometryDataProduct):
    """
    a file containing molecular formula identifications that was output from a mass spec data processing workflow (eg. .csv of m/z and molecular formulae, .hdf5 file).
    """
    __tablename__ = 'MolecularIdentificationProduct'

    results_from_ms_processing = Column(UUID(), ForeignKey('MassSpectrometryDataProcessingActivity.id'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"MolecularIdentificationProduct(results_from_ms_processing={self.results_from_ms_processing},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},sample_id={self.sample_id},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MetaproteomicsProduct(MassSpectrometryDataProduct):
    """
    Abstract parent class for processed metaproteomics data. Details and subclasses TBD.
    """
    __tablename__ = 'MetaproteomicsProduct'

    results_from_ms_processing = Column(UUID(), ForeignKey('MassSpectrometryDataProcessingActivity.id'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"MetaproteomicsProduct(results_from_ms_processing={self.results_from_ms_processing},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},sample_id={self.sample_id},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
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

    annotation_database = Column(Enum('PFAM', 'COG', 'KEGG', name='AnnotationDatabaseEnum'))
    mg_workflow_step = Column(Enum('ReadQcAnalysis', 'MetagenomeAssembly', 'ReadBasedTaxonomyAnalysis', 'MetagenomeAnnotation', 'MagsAnalysis', 'FunctionalAnnotation', 'GenePhylogeny', name='MetagenomicsSteps'))
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    provider_name = Column(Text(), ForeignKey('ControlledTermValue.id'))
    raw_fasta_url = Column(Text())
    additional_information = Column(Text())
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"Metagenomics_AnnotationProduct(annotation_database={self.annotation_database},mg_workflow_step={self.mg_workflow_step},sample_id={self.sample_id},provider_name={self.provider_name},raw_fasta_url={self.raw_fasta_url},additional_information={self.additional_information},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
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

    mg_workflow_step = Column(Enum('ReadQcAnalysis', 'MetagenomeAssembly', 'ReadBasedTaxonomyAnalysis', 'MetagenomeAnnotation', 'MagsAnalysis', 'FunctionalAnnotation', 'GenePhylogeny', name='MetagenomicsSteps'))
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    provider_name = Column(Text(), ForeignKey('ControlledTermValue.id'))
    raw_fasta_url = Column(Text())
    additional_information = Column(Text())
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"Metagenomics_BinningProduct(mg_workflow_step={self.mg_workflow_step},sample_id={self.sample_id},provider_name={self.provider_name},raw_fasta_url={self.raw_fasta_url},additional_information={self.additional_information},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
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
    mg_workflow_step = Column(Enum('ReadQcAnalysis', 'MetagenomeAssembly', 'ReadBasedTaxonomyAnalysis', 'MetagenomeAnnotation', 'MagsAnalysis', 'FunctionalAnnotation', 'GenePhylogeny', name='MetagenomicsSteps'))
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    provider_name = Column(Text(), ForeignKey('ControlledTermValue.id'))
    raw_fasta_url = Column(Text())
    additional_information = Column(Text())
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"Metagenomics_GenePhylogenyProduct(gene_family={self.gene_family},mg_workflow_step={self.mg_workflow_step},sample_id={self.sample_id},provider_name={self.provider_name},raw_fasta_url={self.raw_fasta_url},additional_information={self.additional_information},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
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
Individual QC flags for each element using ProcessedDataFlag enum.

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

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='ProductMeasureType'))
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
    flag_cl = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_v = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_cr = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_ni = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_cu = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_zn = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_ga = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_as = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_se = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_br = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_rb = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_sr = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_y = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_nb = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_mo = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_ag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_cd = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_in = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_sn = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_sb = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_cs = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_ba = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_la = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_ce = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_pb = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_th = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_u = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"XRFElementalProduct(measure_type={self.measure_type},cl_mg_per_kg={self.cl_mg_per_kg},v_mg_per_kg={self.v_mg_per_kg},cr_mg_per_kg={self.cr_mg_per_kg},ni_mg_per_kg={self.ni_mg_per_kg},cu_mg_per_kg={self.cu_mg_per_kg},zn_mg_per_kg={self.zn_mg_per_kg},ga_mg_per_kg={self.ga_mg_per_kg},as_mg_per_kg={self.as_mg_per_kg},se_mg_per_kg={self.se_mg_per_kg},br_mg_per_kg={self.br_mg_per_kg},rb_mg_per_kg={self.rb_mg_per_kg},sr_mg_per_kg={self.sr_mg_per_kg},y_mg_per_kg={self.y_mg_per_kg},nb_mg_per_kg={self.nb_mg_per_kg},mo_mg_per_kg={self.mo_mg_per_kg},ag_mg_per_kg={self.ag_mg_per_kg},cd_mg_per_kg={self.cd_mg_per_kg},in_mg_per_kg={self.in_mg_per_kg},sn_mg_per_kg={self.sn_mg_per_kg},sb_mg_per_kg={self.sb_mg_per_kg},cs_mg_per_kg={self.cs_mg_per_kg},ba_mg_per_kg={self.ba_mg_per_kg},la_mg_per_kg={self.la_mg_per_kg},ce_mg_per_kg={self.ce_mg_per_kg},pb_mg_per_kg={self.pb_mg_per_kg},th_mg_per_kg={self.th_mg_per_kg},u_mg_per_kg={self.u_mg_per_kg},flag_cl={self.flag_cl},flag_v={self.flag_v},flag_cr={self.flag_cr},flag_ni={self.flag_ni},flag_cu={self.flag_cu},flag_zn={self.flag_zn},flag_ga={self.flag_ga},flag_as={self.flag_as},flag_se={self.flag_se},flag_br={self.flag_br},flag_rb={self.flag_rb},flag_sr={self.flag_sr},flag_y={self.flag_y},flag_nb={self.flag_nb},flag_mo={self.flag_mo},flag_ag={self.flag_ag},flag_cd={self.flag_cd},flag_in={self.flag_in},flag_sn={self.flag_sn},flag_sb={self.flag_sb},flag_cs={self.flag_cs},flag_ba={self.flag_ba},flag_la={self.flag_la},flag_ce={self.flag_ce},flag_pb={self.flag_pb},flag_th={self.flag_th},flag_u={self.flag_u},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},sample_id={self.sample_id},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class XRDPhaseProduct(XRayDataProduct):
    """
    X-ray Diffraction (XRD) mineral phase identification and quantification data.
One row per sample with columns for each mineral phase identified.

Follows the wide-format pattern with individual weight percent columns.
Individual QC flags for each mineral using ProcessedDataFlag enum.

Relationship to core tables:
  - id: FK -> processedData.id (1:1 linkage)
  - processedData.type = 'XRDPhaseProduct'
  - processedData.workflow_id -> DataProcessingActivity if Rietveld refinement
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
  XRDDataGenerationActivity acquires raw diffractogram ->
  DataProcessingActivity (type='xrd_rietveld_refinement') processes with
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

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='ProductMeasureType'))
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
    flag_quartz = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_albite = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_microcline = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_muscovite = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_kaolinite = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_chlorite = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_hornblende = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_pyrite = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_halite = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    flag_gypsum = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='ProcessedDataFlag'))
    summary_metrics = Column(Text())
    lims_barcode = Column(Text())
    sample_id = Column(UUID(), ForeignKey('Sample.id'))
    name = Column(Text(), nullable=False )
    description = Column(Text())
    project = Column(Integer())
    sampling_set = Column(Integer())
    core_section = Column(Enum('TOP', 'BTM', 'MID', name='CoreSectionEnum'))
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    id = Column(UUID(), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"XRDPhaseProduct(measure_type={self.measure_type},quartz_percent={self.quartz_percent},albite_percent={self.albite_percent},microcline_percent={self.microcline_percent},muscovite_percent={self.muscovite_percent},kaolinite_percent={self.kaolinite_percent},chlorite_percent={self.chlorite_percent},hornblende_percent={self.hornblende_percent},pyrite_percent={self.pyrite_percent},halite_percent={self.halite_percent},gypsum_percent={self.gypsum_percent},flag_quartz={self.flag_quartz},flag_albite={self.flag_albite},flag_microcline={self.flag_microcline},flag_muscovite={self.flag_muscovite},flag_kaolinite={self.flag_kaolinite},flag_chlorite={self.flag_chlorite},flag_hornblende={self.flag_hornblende},flag_pyrite={self.flag_pyrite},flag_halite={self.flag_halite},flag_gypsum={self.flag_gypsum},summary_metrics={self.summary_metrics},lims_barcode={self.lims_barcode},sample_id={self.sample_id},name={self.name},description={self.description},project={self.project},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


