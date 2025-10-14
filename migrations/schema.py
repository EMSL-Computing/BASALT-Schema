
from sqlalchemy import Column, Index, Table, ForeignKey, UniqueConstraint
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



    


class SamplingActivity(Base):
    """
    
    """
    __tablename__ = 'samplingActivity'

    id = Column(UUID(), primary_key=True, nullable=False )
    study_id = Column(UUID(), ForeignKey('study.id'), nullable=False )
    type = Column(Enum('soil', 'water', 'air', 'plant', 'none', name='samplingactivitytype'), nullable=False )
    sample_name = Column(Text(), nullable=False )
    lims_barcode = Column(Text())
    alt_id = Column(UUID(), ForeignKey('quantityValue.id'))
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

    id = Column(UUID(), ForeignKey('sample.id'), primary_key=True, nullable=False )
    soil_type = Column(Enum('soil_core', 'surface_layer', name='soiltype'), nullable=False )
    

    

    def __repr__(self):
        return f"soil_sample(id={self.id},soil_type={self.soil_type},)"



    


class AerosolSample(Base):
    """
    An aerosol sample with specific aerosol-related properties
    """
    __tablename__ = 'aerosol_sample'

    id = Column(UUID(), ForeignKey('sample.id'), primary_key=True, nullable=False )
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



    


class ProcessedData(Base):
    """
    
    """
    __tablename__ = 'processedData'

    id = Column(UUID(), primary_key=True, nullable=False )
    type = Column(Enum('processedData', 'FTICRProduct', 'TomographyProduct', 'MicrobialBiomassProduct', 'NitrogenAnalysisProduct', 'PhosphorusAnalysisProduct', 'pHProduct', 'ElementalAnalysisProduct', 'IonsAnalysisProduct', 'RespirationProduct', 'EnzymeProduct', 'TextureProduct', 'WEOMProduct', 'HydraulicPropertiesProduct', 'GWCMoistureProduct', 'MAOMProduct', 'BulkDensityProduct', 'MetaGenomicsProduct', name='product'), nullable=False )
    name = Column(Text(), nullable=False )
    proposal_id = Column(Numeric())
    sampling_set = Column(Numeric())
    core_section = Column(Text())
    sample_name = Column(Text())
    s3_base_url = Column(Text())
    s3_bucket = Column(Text())
    s3_key = Column(Text(), nullable=False )
    filesize = Column(Integer())
    md5checksum = Column(Text())
    workflow_id = Column(UUID(), ForeignKey('workflowExecutionActivity.id'))
    lims_barcode = Column(Text())
    version = Column(Text())
    

    

    def __repr__(self):
        return f"processedData(id={self.id},type={self.type},name={self.name},proposal_id={self.proposal_id},sampling_set={self.sampling_set},core_section={self.core_section},sample_name={self.sample_name},s3_base_url={self.s3_base_url},s3_bucket={self.s3_bucket},s3_key={self.s3_key},filesize={self.filesize},md5checksum={self.md5checksum},workflow_id={self.workflow_id},lims_barcode={self.lims_barcode},version={self.version},)"



    


class AnalysisActivity(Base):
    """
    
    """
    __tablename__ = 'analysisActivity'

    id = Column(UUID(), primary_key=True, nullable=False )
    type = Column(Enum('analysis_activity', 'lcms_metabolomics_method', 'fticr_acquisition_method', 'gravimetric_water_content_method', 'ph_method', 'hydraulic_properties_method', 'microbial_biomass_method', 'xray_computed_tomography_method', 'REGEN', 'KUO', 'respiration_method', 'texture_method', 'enzyme_activity_method', 'elemental_analysis_method', 'toc_tn_method', 'bulk_density_method', 'metagenomics_method', name='routemethod'))
    analyte_id = Column(UUID(), ForeignKey('processedSample.id'))
    name = Column(Text())
    acquisition_time = Column(DateTime(), nullable=False )
    instrument_id = Column(UUID(), ForeignKey('instrument.id'))
    protocol_url = Column(Text())
    instrument_operator_id = Column(UUID(), ForeignKey('personValue.id'))
    version = Column(Text())
    

    

    def __repr__(self):
        return f"analysisActivity(id={self.id},type={self.type},analyte_id={self.analyte_id},name={self.name},acquisition_time={self.acquisition_time},instrument_id={self.instrument_id},protocol_url={self.protocol_url},instrument_operator_id={self.instrument_operator_id},version={self.version},)"



    


class InstrumentData(Base):
    """
    
    """
    __tablename__ = 'instrumentData'

    id = Column(UUID(), primary_key=True, nullable=False )
    analysis_activity_id = Column(UUID(), ForeignKey('analysisActivity.id'))
    description = Column(Text(), nullable=False )
    alternative_identifiers = Column(Text())
    compression_type = Column(Text())
    file_size_bytes = Column(Integer())
    md5_checksum = Column(Text())
    name = Column(Text(), nullable=False )
    type = Column(Text())
    url = Column(Text())
    was_generated_by = Column(Text())
    file_type = Column(Enum('FT_ICR_MS_Analysis_Results', 'GC_MS_Metabolomics_Results', 'Metaproteomics_Workflow_Statistics', 'Protein_Report', 'Peptide_Report', 'Unfiltered_Metaproteomics_Results', 'Read_Count_and_RPKM', 'QC_non_rRNA_R2', 'QC_non_rRNA_R1', 'Metagenome_Bins', 'CheckM_Statistics', 'GOTTCHA2_Krona_Plot', 'Kraken2_Krona_Plot', 'Centrifuge_Krona_Plot', 'Kraken2_Classification_Report', 'Kraken2_Taxonomic_Classification', 'Centrifuge_Classification_Report', 'Centrifuge_Taxonomic_Classification', 'Structural_Annotation_GFF', 'Functional_Annotation_GFF', 'Annotation_Amino_Acid_FASTA', 'Annotation_Enzyme_Commission', 'Annotation_KEGG_Orthology', 'Assembly_Coverage_BAM', 'Assembly_AGP', 'Assembly_Scaffolds', 'Assembly_Contigs', 'Assembly_Coverage_Stats', 'Filtered_Sequencing_Reads', 'QC_Statistics', 'TIGRFam_Annotation_GFF', 'Clusters_of_Orthologous_Groups_COG_Annotation_GFF', 'CATH_FunFams_Functional_Families_Annotation_GFF', 'SUPERFam_Annotation_GFF', 'SMART_Annotation_GFF', 'Pfam_Annotation_GFF', 'Direct_Infusion_FT_ICR_MS_Raw_Data', name='filetype'))
    version = Column(Text())
    

    

    def __repr__(self):
        return f"instrumentData(id={self.id},analysis_activity_id={self.analysis_activity_id},description={self.description},alternative_identifiers={self.alternative_identifiers},compression_type={self.compression_type},file_size_bytes={self.file_size_bytes},md5_checksum={self.md5_checksum},name={self.name},type={self.type},url={self.url},was_generated_by={self.was_generated_by},file_type={self.file_type},version={self.version},)"



    


class WorkflowExecutionActivity(Base):
    """
    
    """
    __tablename__ = 'workflowExecutionActivity'

    id = Column(UUID(), primary_key=True, nullable=False )
    raw_data_id = Column(UUID(), ForeignKey('instrumentData.id'), nullable=False )
    description = Column(Text())
    ended_at_time = Column(DateTime())
    git_url = Column(Text(), nullable=False )
    name = Column(Text())
    started_at_time = Column(DateTime(), nullable=False )
    type = Column(Text(), nullable=False )
    used_id = Column(UUID(), ForeignKey('softwareControlledTermValue.id'))
    execution_resource = Column(Enum('RZR', 'Tahoma', 'local', 'other', name='executionresourcetype'))
    workflow_steps = Column(Text())
    version = Column(Text())
    

    

    def __repr__(self):
        return f"workflowExecutionActivity(id={self.id},raw_data_id={self.raw_data_id},description={self.description},ended_at_time={self.ended_at_time},git_url={self.git_url},name={self.name},started_at_time={self.started_at_time},type={self.type},used_id={self.used_id},execution_resource={self.execution_resource},workflow_steps={self.workflow_steps},version={self.version},)"



    


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
    vendor = Column(Enum('waters', 'agilent', 'bruker', 'thermo_fisher', 'perkin_elmer', 'scientific_industries', 'illumina', 'nikon', 'fia_lab', 'shimadzu', 'regen_ag_lab', 'kuo', name='vendorenum'))
    model = Column(Enum('exploris_240', 'exploris_480', 'ltq_orbitrap_velos', 'orbitrap_fusion_lumos', 'orbitrap_eclipse_tribid', 'orbitrap_q_exactive', 'solarix_7T', 'solarix_12T', 'solarix_15T', 'agilent_8890A', 'agilent_7980A', 'vortex_genie_2', 'novaseq', 'scimax', 'ed_400_with_rs_422', 'mettler_toledo_30029066', 'mettler_toledo_30266628', 'ums_hyprop2_020210', 'fialyzer_1000', 'fialyzer_1001', 'fialyzer_1002', 'orbitrap_q_exactive_plus', 'toc_5000A', 'toc_lcsh', 'sr_1', 'xth320', name='modelenum'))
    instrument_parameters = Column(Text())
    

    

    def __repr__(self):
        return f"instrument(id={self.id},name={self.name},alternative_names={self.alternative_names},vendor={self.vendor},model={self.model},instrument_parameters={self.instrument_parameters},)"



    


class MetaboliteQuantification(Base):
    """
    
    """
    __tablename__ = 'metaboliteQuantification'

    id = Column(UUID(), primary_key=True, nullable=False )
    description = Column(Text())
    alternative_identifiers = Column(Text())
    highest_similarity_score = Column(Integer())
    metabolite_quantified = Column(Text())
    

    

    def __repr__(self):
        return f"metaboliteQuantification(id={self.id},description={self.description},alternative_identifiers={self.alternative_identifiers},highest_similarity_score={self.highest_similarity_score},metabolite_quantified={self.metabolite_quantified},)"



    


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



    


class PeptideQuantification(Base):
    """
    
    """
    __tablename__ = 'peptideQuantification'

    id = Column(UUID(), primary_key=True, nullable=False )
    description = Column(Text())
    all_proteins = Column(Text())
    best_protein = Column(Text())
    min_q_value = Column(Numeric())
    peptide_sequence = Column(Text())
    peptide_spectral_count = Column(Integer())
    peptide_sum_masic_abundance = Column(Numeric())
    

    

    def __repr__(self):
        return f"peptideQuantification(id={self.id},description={self.description},all_proteins={self.all_proteins},best_protein={self.best_protein},min_q_value={self.min_q_value},peptide_sequence={self.peptide_sequence},peptide_spectral_count={self.peptide_spectral_count},peptide_sum_masic_abundance={self.peptide_sum_masic_abundance},)"



    


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



    


class InstrumentAltId(Base):
    """
    
    """
    __tablename__ = 'instrument_alt_id'

    id = Column(UUID(), ForeignKey('alternativeIdentifier.id'), primary_key=True, nullable=False )
    instrument_alt_id_provider = Column(Enum('nexus', 'dms', name='instrumentaltidprovider'))
    instrument_id = Column(UUID(), ForeignKey('instrument.id'), nullable=False )
    

    

    def __repr__(self):
        return f"instrument_alt_id(id={self.id},instrument_alt_id_provider={self.instrument_alt_id_provider},instrument_id={self.instrument_id},)"



    


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
    analysis_type = Column(Enum('analysis_activity', 'lcms_metabolomics_method', 'fticr_acquisition_method', 'gravimetric_water_content_method', 'ph_method', 'hydraulic_properties_method', 'microbial_biomass_method', 'xray_computed_tomography_method', 'REGEN', 'KUO', 'respiration_method', 'texture_method', 'enzyme_activity_method', 'elemental_analysis_method', 'toc_tn_method', 'bulk_density_method', 'metagenomics_method', name='routemethod'))
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
    sample_base_id = Column(UUID(), ForeignKey('sampleBase.id'), nullable=False )
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



    


class MagBin(Base):
    """
    
    """
    __tablename__ = 'magBin'

    id = Column(UUID(), primary_key=True, nullable=False )
    workflow_id = Column(UUID(), ForeignKey('workflowExecutionActivity.id'))
    bin_name = Column(Text(), nullable=False )
    bin_quality = Column(Enum('HQ', 'MQ', 'LQ', name='binquality'))
    completeness = Column(Numeric())
    contamination = Column(Numeric())
    gene_count = Column(Integer())
    gtdbtk_class = Column(Text())
    gtdbtk_domain = Column(Text())
    gtdbtk_family = Column(Text())
    gtdbtk_genus = Column(Text())
    gtdbtk_order = Column(Text())
    gtdbtk_phylum = Column(Text())
    gtdbtk_species = Column(Text())
    members_id = Column(Text())
    num_16s = Column(Integer())
    num_23s = Column(Integer())
    num_5s = Column(Integer())
    num_trna = Column(Integer())
    number_of_contig = Column(Integer())
    total_bases = Column(Integer())
    

    

    def __repr__(self):
        return f"magBin(id={self.id},workflow_id={self.workflow_id},bin_name={self.bin_name},bin_quality={self.bin_quality},completeness={self.completeness},contamination={self.contamination},gene_count={self.gene_count},gtdbtk_class={self.gtdbtk_class},gtdbtk_domain={self.gtdbtk_domain},gtdbtk_family={self.gtdbtk_family},gtdbtk_genus={self.gtdbtk_genus},gtdbtk_order={self.gtdbtk_order},gtdbtk_phylum={self.gtdbtk_phylum},gtdbtk_species={self.gtdbtk_species},members_id={self.members_id},num_16s={self.num_16s},num_23s={self.num_23s},num_5s={self.num_5s},num_trna={self.num_trna},number_of_contig={self.number_of_contig},total_bases={self.total_bases},)"



    


class Soil(Base):
    """
    
    """
    __tablename__ = 'soil'

    id = Column(UUID(), ForeignKey('samplingActivity.id'), primary_key=True, nullable=False )
    annual_precpt_id = Column(UUID(), ForeignKey('quantityValue.id'))
    annual_temp_id = Column(UUID(), ForeignKey('quantityValue.id'))
    bulk_elect_conductivity_id = Column(UUID(), ForeignKey('quantityValue.id'))
    density_id = Column(UUID(), ForeignKey('quantityValue.id'))
    depth_id = Column(UUID(), ForeignKey('quantityValue.id'))
    particle_class_id = Column(UUID(), ForeignKey('quantityValue.id'))
    porosity_id = Column(UUID(), ForeignKey('quantityValue.id'))
    pressure_id = Column(UUID(), ForeignKey('quantityValue.id'))
    season_precpt_id = Column(UUID(), ForeignKey('quantityValue.id'))
    season_temp_id = Column(UUID(), ForeignKey('quantityValue.id'))
    size_frac_low_id = Column(UUID(), ForeignKey('quantityValue.id'))
    size_frac_up_id = Column(UUID(), ForeignKey('quantityValue.id'))
    slope_aspect_id = Column(UUID(), ForeignKey('quantityValue.id'))
    slope_gradient_id = Column(UUID(), ForeignKey('quantityValue.id'))
    soil_temperature_id = Column(UUID(), ForeignKey('quantityValue.id'))
    soil_texture_id = Column(UUID(), ForeignKey('quantityValue.id'))
    temp_id = Column(UUID(), ForeignKey('quantityValue.id'))
    water_content_id = Column(UUID(), ForeignKey('quantityValue.id'))
    wind_speed_id = Column(UUID(), ForeignKey('quantityValue.id'))
    cur_land_use = Column(Enum('badlands', 'cities', 'conifers', 'crop_trees', 'farmstead', 'gravel', 'hardwoods', 'hayland', 'horticultural_plants', 'industrial_areas', 'intermixed', 'marshlands', 'meadows', 'mines_quarries', 'mudflats', 'oil_waste', 'pastureland', 'permanent_snow_or_ice', 'rainforest', 'rangeland', 'roads_railroads', 'rock', 'row_crops', 'saline_seeps', 'salt_flats', 'sand', 'shrub_crops', 'shrub_land', 'small_grains', 'successional_shrub_land', 'swamp', 'tropical', 'tundra', 'vegetable_crops', 'vine_crops', name='landuseenum'))
    drainage_class = Column(Enum('excessively_drained', 'moderately_well', 'poorly', 'somewhat_poorly', 'very_poorly', 'well', name='drainageclassenum'))
    fao_class = Column(Enum('acrisols', 'alisols', 'andosols', 'anthrosols', 'arenosols', 'calcisols', 'cambisols', 'chernozems', 'cryosols', 'durisols', 'ferralsols', 'fluvisols', 'gleysols', 'gypsisols', 'histosols', 'kastanozems', 'leptosols', 'lixisols', 'luvisols', 'nitisols', 'phaeozems', 'planosols', 'plinthosols', 'podzols', 'solonchaks', 'solonetz', 'stagnosols', 'technosols', 'umbrisols', 'vertisols', name='faoclassenum'))
    neon_domain = Column(Enum('northeast', 'mid_atlantic', 'southeast', 'atlantic_neotropical', 'great_lakes', 'prairie_peninsula', 'appalachians_and_cumberland_plateau', 'ozarks_complex', 'northern_plains', 'central_plains', 'southern_plains', 'desert_southwest', 'northern_rockies', 'southern_rockies_and_colorado_plateau', 'great_basin', 'sierra_nevada', 'pacific_northwest', 'pacific_southwest', 'tundra', 'taiga', 'pacific_tropical', name='neondomainenum'))
    profile_position = Column(Enum('backslope', 'footslope', 'shoulder', 'summit', 'toeslope', name='profilepositionenum'))
    sediment_type = Column(Enum('biogenous', 'cosmogenous', 'hydrogenous', 'lithogenous', name='sedimenttypeenum'))
    soil_horizon = Column(Enum('a_horizon', 'b_horizon', 'c_horizon', 'e_horizon', 'o_horizon', 'permafrost', 'r_layer', name='soilhorizonenum'))
    tillage = Column(Enum('chisel', 'cutting_disc', 'disc_plough', 'drill', 'mouldboard', 'ridge_till', 'strip_tillage', 'tined', 'zonal_tillage', name='tillageenum'))
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
    

    

    def __repr__(self):
        return f"soil(id={self.id},annual_precpt_id={self.annual_precpt_id},annual_temp_id={self.annual_temp_id},bulk_elect_conductivity_id={self.bulk_elect_conductivity_id},density_id={self.density_id},depth_id={self.depth_id},particle_class_id={self.particle_class_id},porosity_id={self.porosity_id},pressure_id={self.pressure_id},season_precpt_id={self.season_precpt_id},season_temp_id={self.season_temp_id},size_frac_low_id={self.size_frac_low_id},size_frac_up_id={self.size_frac_up_id},slope_aspect_id={self.slope_aspect_id},slope_gradient_id={self.slope_gradient_id},soil_temperature_id={self.soil_temperature_id},soil_texture_id={self.soil_texture_id},temp_id={self.temp_id},water_content_id={self.water_content_id},wind_speed_id={self.wind_speed_id},cur_land_use={self.cur_land_use},drainage_class={self.drainage_class},fao_class={self.fao_class},neon_domain={self.neon_domain},profile_position={self.profile_position},sediment_type={self.sediment_type},soil_horizon={self.soil_horizon},tillage={self.tillage},wind_direction={self.wind_direction},agrochem_addition={self.agrochem_addition},al_sat={self.al_sat},al_sat_meth={self.al_sat_meth},biotic_regm={self.biotic_regm},climate_environment={self.climate_environment},core_collector={self.core_collector},crop_rotation={self.crop_rotation},crop_rotation_schedule={self.crop_rotation_schedule},cur_vegetation={self.cur_vegetation},cur_vegetation_meth={self.cur_vegetation_meth},filter_method={self.filter_method},fire={self.fire},flooding={self.flooding},heavy_metals={self.heavy_metals},heavy_metals_meth={self.heavy_metals_meth},horizon_meth={self.horizon_meth},infiltration_1={self.infiltration_1},infiltration_2={self.infiltration_2},infiltration_notes={self.infiltration_notes},link_class_info={self.link_class_info},link_climate_info={self.link_climate_info},local_class={self.local_class},local_class_meth={self.local_class_meth},perturbation={self.perturbation},previous_land_use={self.previous_land_use},previous_land_use_meth={self.previous_land_use_meth},site_definition={self.site_definition},soil_type={self.soil_type},soil_type_meth={self.soil_type_meth},texture_meth={self.texture_meth},water_content_meth={self.water_content_meth},weather={self.weather},)"



    


class SiteMetadata(Base):
    """
    
    """
    __tablename__ = 'siteMetadata'

    id = Column(UUID(), primary_key=True, nullable=False )
    nasa_mean_annual_temp_c_id = Column(UUID(), ForeignKey('quantityValue.id'))
    nasa_mean_annual_precip_mm_id = Column(UUID(), ForeignKey('quantityValue.id'))
    nasa_max_annual_temp_c_id = Column(UUID(), ForeignKey('quantityValue.id'))
    nasa_min_annual_temp_c_id = Column(UUID(), ForeignKey('quantityValue.id'))
    nasa_mean_wind_speed_ms_id = Column(UUID(), ForeignKey('quantityValue.id'))
    nasa_mean_relative_humidity_pct_id = Column(UUID(), ForeignKey('quantityValue.id'))
    nasa_frost_days_per_year_id = Column(UUID(), ForeignKey('quantityValue.id'))
    nasa_mean_dew_point_c_id = Column(UUID(), ForeignKey('quantityValue.id'))
    nasa_mean_vapor_pressure_kpa_id = Column(UUID(), ForeignKey('quantityValue.id'))
    nasa_mean_surface_pressure_kpa_id = Column(UUID(), ForeignKey('quantityValue.id'))
    nasa_mean_shortwave_radiation_wm2_id = Column(UUID(), ForeignKey('quantityValue.id'))
    nasa_mean_longwave_radiation_wm2_id = Column(UUID(), ForeignKey('quantityValue.id'))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False )
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False )
    cache_key = Column(Text(), nullable=False )
    latitude = Column(Float(), nullable=False )
    longitude = Column(Float(), nullable=False )
    provider = Column(Text(), nullable=False )
    enriched_at = Column(TIMESTAMP(timezone=True), nullable=False )
    

    

    def __repr__(self):
        return f"siteMetadata(id={self.id},nasa_mean_annual_temp_c_id={self.nasa_mean_annual_temp_c_id},nasa_mean_annual_precip_mm_id={self.nasa_mean_annual_precip_mm_id},nasa_max_annual_temp_c_id={self.nasa_max_annual_temp_c_id},nasa_min_annual_temp_c_id={self.nasa_min_annual_temp_c_id},nasa_mean_wind_speed_ms_id={self.nasa_mean_wind_speed_ms_id},nasa_mean_relative_humidity_pct_id={self.nasa_mean_relative_humidity_pct_id},nasa_frost_days_per_year_id={self.nasa_frost_days_per_year_id},nasa_mean_dew_point_c_id={self.nasa_mean_dew_point_c_id},nasa_mean_vapor_pressure_kpa_id={self.nasa_mean_vapor_pressure_kpa_id},nasa_mean_surface_pressure_kpa_id={self.nasa_mean_surface_pressure_kpa_id},nasa_mean_shortwave_radiation_wm2_id={self.nasa_mean_shortwave_radiation_wm2_id},nasa_mean_longwave_radiation_wm2_id={self.nasa_mean_longwave_radiation_wm2_id},created_at={self.created_at},updated_at={self.updated_at},cache_key={self.cache_key},latitude={self.latitude},longitude={self.longitude},provider={self.provider},enriched_at={self.enriched_at},)"



    


class SamplingActivitySiteMetadataLink(Base):
    """
    
    """
    __tablename__ = 'sampling_activity_site_metadata_link'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    sampling_activity_id = Column(UUID(), ForeignKey('samplingActivity.id'), nullable=False )
    site_metadata_id = Column(UUID(), ForeignKey('siteMetadata.id'), nullable=False )
    

    

    def __repr__(self):
        return f"sampling_activity_site_metadata_link(id={self.id},sampling_activity_id={self.sampling_activity_id},site_metadata_id={self.site_metadata_id},)"



    


class BulkDensityMethod(Base):
    """
    
    """
    __tablename__ = 'BulkDensityMethod'

    analytic = Column(Text(), nullable=False )
    id = Column(UUID(), ForeignKey('analysisActivity.id'), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"BulkDensityMethod(analytic={self.analytic},id={self.id},)"



    


class ElementalAnalysisMethod(Base):
    """
    
    """
    __tablename__ = 'ElementalAnalysisMethod'

    id = Column(UUID(), ForeignKey('analysisActivity.id'), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"ElementalAnalysisMethod(id={self.id},)"



    


class EnzymeActivityMethod(Base):
    """
    
    """
    __tablename__ = 'EnzymeActivityMethod'

    analytic = Column(Text(), nullable=False )
    location = Column(Text(), nullable=False )
    id = Column(UUID(), ForeignKey('analysisActivity.id'), primary_key=True, nullable=False )
    incubation_temp_c = Column(Float())
    incubation_time = Column(Text())
    wavelength = Column(Float())
    method = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"EnzymeActivityMethod(analytic={self.analytic},location={self.location},id={self.id},incubation_temp_c={self.incubation_temp_c},incubation_time={self.incubation_time},wavelength={self.wavelength},method={self.method},)"



    


class FTICRAcquisitionMethod(Base):
    """
    
    """
    __tablename__ = 'FTICR_AcquisitionMethod'

    analytic = Column(Text(), nullable=False )
    location = Column(Text(), nullable=False )
    id = Column(UUID(), ForeignKey('analysisActivity.id'), primary_key=True, nullable=False )
    injection = Column(Text(), nullable=False )
    ionization = Column(Enum('ESI', 'EI', 'CI', 'MALDI', name='ionizationenum'), nullable=False )
    polarity = Column(Text(), nullable=False )
    iat = Column(Float())
    fid = Column(Float())
    mass_range = Column(Float())
    

    

    def __repr__(self):
        return f"FTICR_AcquisitionMethod(analytic={self.analytic},location={self.location},id={self.id},injection={self.injection},ionization={self.ionization},polarity={self.polarity},iat={self.iat},fid={self.fid},mass_range={self.mass_range},)"



    


class GravimetricWaterContentMethod(Base):
    """
    
    """
    __tablename__ = 'GravimetricWaterContentMethod'

    analytic = Column(Text(), nullable=False )
    location = Column(Text(), nullable=False )
    id = Column(UUID(), ForeignKey('analysisActivity.id'), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"GravimetricWaterContentMethod(analytic={self.analytic},location={self.location},id={self.id},)"



    


class HydraulicPropertiesMethod(Base):
    """
    
    """
    __tablename__ = 'HydraulicPropertiesMethod'

    analytic = Column(Text(), nullable=False )
    location = Column(Text(), nullable=False )
    id = Column(UUID(), ForeignKey('analysisActivity.id'), primary_key=True, nullable=False )
    fitting_model = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"HydraulicPropertiesMethod(analytic={self.analytic},location={self.location},id={self.id},fitting_model={self.fitting_model},)"



    


class KuoMethod(Base):
    """
    
    """
    __tablename__ = 'KuoMethod'

    analytic = Column(Text(), nullable=False )
    location = Column(Text(), nullable=False )
    method = Column(Text(), nullable=False )
    id = Column(UUID(), ForeignKey('analysisActivity.id'), primary_key=True, nullable=False )
    detection_limit = Column(Text(), nullable=False )
    wavelength = Column(Text())
    

    

    def __repr__(self):
        return f"KuoMethod(analytic={self.analytic},location={self.location},method={self.method},id={self.id},detection_limit={self.detection_limit},wavelength={self.wavelength},)"



    


class LCMSMetabolomicsMethod(Base):
    """
    
    """
    __tablename__ = 'LCMS_MetabolomicsMethod'

    analytic = Column(Text(), nullable=False )
    location = Column(Text(), nullable=False )
    id = Column(UUID(), ForeignKey('analysisActivity.id'), primary_key=True, nullable=False )
    injection = Column(Text(), nullable=False )
    polarity = Column(Text(), nullable=False )
    column = Column(Text(), nullable=False )
    mode = Column(Text(), nullable=False )
    method_duration = Column(Text(), nullable=False )
    runtime = Column(Text(), nullable=False )
    resolution = Column(Float(), nullable=False )
    scan_range = Column(Text(), nullable=False )
    dd_ms2_resolution = Column(Float(), nullable=False )
    loop_count = Column(Text(), nullable=False )
    isolation_window = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"LCMS_MetabolomicsMethod(analytic={self.analytic},location={self.location},id={self.id},injection={self.injection},polarity={self.polarity},column={self.column},mode={self.mode},method_duration={self.method_duration},runtime={self.runtime},resolution={self.resolution},scan_range={self.scan_range},dd_ms2_resolution={self.dd_ms2_resolution},loop_count={self.loop_count},isolation_window={self.isolation_window},)"



    


class MicrobialBiomassMethod(Base):
    """
    
    """
    __tablename__ = 'MicrobialBiomassMethod'

    analytic = Column(Text(), nullable=False )
    location = Column(Text(), nullable=False )
    id = Column(UUID(), ForeignKey('analysisActivity.id'), primary_key=True, nullable=False )
    detector = Column(Text(), nullable=False )
    mode = Column(Text())
    injection_volume = Column(Text(), nullable=False )
    sample_volume = Column(Text(), nullable=False )
    number_of_injections = Column(Float(), nullable=False )
    check_standard_spacing = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"MicrobialBiomassMethod(analytic={self.analytic},location={self.location},id={self.id},detector={self.detector},mode={self.mode},injection_volume={self.injection_volume},sample_volume={self.sample_volume},number_of_injections={self.number_of_injections},check_standard_spacing={self.check_standard_spacing},)"



    


class PHMethod(Base):
    """
    
    """
    __tablename__ = 'PH_Method'

    analytic = Column(Text(), nullable=False )
    location = Column(Text(), nullable=False )
    id = Column(UUID(), ForeignKey('analysisActivity.id'), primary_key=True, nullable=False )
    calibration = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"PH_Method(analytic={self.analytic},location={self.location},id={self.id},calibration={self.calibration},)"



    


class RespirationMethod(Base):
    """
    
    """
    __tablename__ = 'RespirationMethod'

    analytic = Column(Text(), nullable=False )
    id = Column(UUID(), ForeignKey('analysisActivity.id'), primary_key=True, nullable=False )
    respiration_analysis_type = Column(Text(), nullable=False )
    sample_volume_id = Column(UUID(), ForeignKey('quantityValue.id'))
    scale_id = Column(UUID(), ForeignKey('quantityValue.id'))
    duration_id = Column(UUID(), ForeignKey('quantityValue.id'))
    sampling_time_id = Column(UUID(), ForeignKey('quantityValue.id'))
    bottle_vol_id = Column(UUID(), ForeignKey('quantityValue.id'))
    

    

    def __repr__(self):
        return f"RespirationMethod(analytic={self.analytic},id={self.id},respiration_analysis_type={self.respiration_analysis_type},sample_volume_id={self.sample_volume_id},scale_id={self.scale_id},duration_id={self.duration_id},sampling_time_id={self.sampling_time_id},bottle_vol_id={self.bottle_vol_id},)"



    


class TOCTNMethod(Base):
    """
    
    """
    __tablename__ = 'TOC_TN_Method'

    analytic = Column(Text(), nullable=False )
    location = Column(Text(), nullable=False )
    id = Column(UUID(), ForeignKey('analysisActivity.id'), primary_key=True, nullable=False )
    column = Column(Text())
    mode = Column(Text())
    detector = Column(Text(), nullable=False )
    injection_volume = Column(Text(), nullable=False )
    sample_volume = Column(Text(), nullable=False )
    number_of_injections = Column(Float(), nullable=False )
    check_standard_spacing = Column(Text())
    

    

    def __repr__(self):
        return f"TOC_TN_Method(analytic={self.analytic},location={self.location},id={self.id},column={self.column},mode={self.mode},detector={self.detector},injection_volume={self.injection_volume},sample_volume={self.sample_volume},number_of_injections={self.number_of_injections},check_standard_spacing={self.check_standard_spacing},)"



    


class TextureMethod(Base):
    """
    
    """
    __tablename__ = 'TextureMethod'

    analytic = Column(Text(), nullable=False )
    location = Column(Text(), nullable=False )
    method = Column(Text(), nullable=False )
    id = Column(UUID(), ForeignKey('analysisActivity.id'), primary_key=True, nullable=False )
    

    

    def __repr__(self):
        return f"TextureMethod(analytic={self.analytic},location={self.location},method={self.method},id={self.id},)"



    


class XrayComputedTomographyMethod(Base):
    """
    
    """
    __tablename__ = 'XrayComputedTomographyMethod'

    analytic = Column(Text(), nullable=False )
    location = Column(Text(), nullable=False )
    id = Column(UUID(), ForeignKey('analysisActivity.id'), primary_key=True, nullable=False )
    x_ray_power = Column(Text(), nullable=False )
    cu_filter = Column(Text(), nullable=False )
    total_projections_collected = Column(Float(), nullable=False )
    rotation = Column(Text(), nullable=False )
    frames_recording_per_projection = Column(Float(), nullable=False )
    exposure_time_per_frame = Column(Text(), nullable=False )
    image_voxel_size_is = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"XrayComputedTomographyMethod(analytic={self.analytic},location={self.location},id={self.id},x_ray_power={self.x_ray_power},cu_filter={self.cu_filter},total_projections_collected={self.total_projections_collected},rotation={self.rotation},frames_recording_per_projection={self.frames_recording_per_projection},exposure_time_per_frame={self.exposure_time_per_frame},image_voxel_size_is={self.image_voxel_size_is},)"



    


class BulkDensityProduct(Base):
    """
    
    """
    __tablename__ = 'BulkDensityProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    id = Column(UUID(), ForeignKey('processedData.id'), primary_key=True, nullable=False )
    bulk_density_id = Column(UUID(), ForeignKey('quantityValue.id'))
    flag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    

    

    def __repr__(self):
        return f"BulkDensityProduct(measure_type={self.measure_type},id={self.id},bulk_density_id={self.bulk_density_id},flag={self.flag},)"



    


class ElementalAnalysisProduct(Base):
    """
    
    """
    __tablename__ = 'ElementalAnalysisProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    id = Column(UUID(), ForeignKey('processedData.id'), primary_key=True, nullable=False )
    total_carbon_id = Column(UUID(), ForeignKey('quantityValue.id'))
    total_nitrogen_id = Column(UUID(), ForeignKey('quantityValue.id'))
    total_kjeldahl_nitrogen_id = Column(UUID(), ForeignKey('quantityValue.id'))
    total_sulfur_id = Column(UUID(), ForeignKey('quantityValue.id'))
    flag_total_carbon = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_total_nitrogen = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_tkn = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_total_sulfur = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    

    

    def __repr__(self):
        return f"ElementalAnalysisProduct(measure_type={self.measure_type},id={self.id},total_carbon_id={self.total_carbon_id},total_nitrogen_id={self.total_nitrogen_id},total_kjeldahl_nitrogen_id={self.total_kjeldahl_nitrogen_id},total_sulfur_id={self.total_sulfur_id},flag_total_carbon={self.flag_total_carbon},flag_total_nitrogen={self.flag_total_nitrogen},flag_tkn={self.flag_tkn},flag_total_sulfur={self.flag_total_sulfur},)"



    


class EnzymeProduct(Base):
    """
    
    """
    __tablename__ = 'EnzymeProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    id = Column(UUID(), ForeignKey('processedData.id'), primary_key=True, nullable=False )
    beta_glucosidase_ug_pnp_per_g_per_h_id = Column(UUID(), ForeignKey('quantityValue.id'))
    flag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    

    

    def __repr__(self):
        return f"EnzymeProduct(measure_type={self.measure_type},id={self.id},beta_glucosidase_ug_pnp_per_g_per_h_id={self.beta_glucosidase_ug_pnp_per_g_per_h_id},flag={self.flag},)"



    


class FTICRProduct(Base):
    """
    
    """
    __tablename__ = 'FTICRProduct'

    id = Column(UUID(), ForeignKey('processedData.id'), primary_key=True, nullable=False )
    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    rep = Column(Numeric())
    aq = Column(Numeric())
    h_c_average = Column(Float())
    o_c_average = Column(Float())
    c_average = Column(Float())
    percent_mz_assigned_id = Column(UUID(), ForeignKey('quantityValue.id'))
    rms_id = Column(UUID(), ForeignKey('quantityValue.id'))
    dbe_average = Column(Float())
    low_mass_accuracy_flag = Column(Boolean())
    low_mz_assignment_flag = Column(Boolean())
    

    

    def __repr__(self):
        return f"FTICRProduct(id={self.id},measure_type={self.measure_type},rep={self.rep},aq={self.aq},h_c_average={self.h_c_average},o_c_average={self.o_c_average},c_average={self.c_average},percent_mz_assigned_id={self.percent_mz_assigned_id},rms_id={self.rms_id},dbe_average={self.dbe_average},low_mass_accuracy_flag={self.low_mass_accuracy_flag},low_mz_assignment_flag={self.low_mz_assignment_flag},)"



    


class GWCMoistureProduct(Base):
    """
    
    """
    __tablename__ = 'GWCMoistureProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    id = Column(UUID(), ForeignKey('processedData.id'), primary_key=True, nullable=False )
    gwc_percent_id = Column(UUID(), ForeignKey('quantityValue.id'))
    flag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    

    

    def __repr__(self):
        return f"GWCMoistureProduct(measure_type={self.measure_type},id={self.id},gwc_percent_id={self.gwc_percent_id},flag={self.flag},)"



    


class IonsAnalysisProduct(Base):
    """
    
    """
    __tablename__ = 'IonsAnalysisProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    id = Column(UUID(), ForeignKey('processedData.id'), primary_key=True, nullable=False )
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
    

    

    def __repr__(self):
        return f"IonsAnalysisProduct(measure_type={self.measure_type},id={self.id},sulfate_id={self.sulfate_id},boron_id={self.boron_id},zinc_id={self.zinc_id},manganate_id={self.manganate_id},copper_id={self.copper_id},iron_id={self.iron_id},calcium_id={self.calcium_id},magnesium_id={self.magnesium_id},sodium_id={self.sodium_id},potassium_id={self.potassium_id},total_bases_id={self.total_bases_id},cation_exchange_capacity_id={self.cation_exchange_capacity_id},flag_sulfate={self.flag_sulfate},flag_boron={self.flag_boron},flag_zinc={self.flag_zinc},flag_manganate={self.flag_manganate},flag_copper={self.flag_copper},flag_iron={self.flag_iron},flag_calcium={self.flag_calcium},flag_magnesium={self.flag_magnesium},flag_sodium={self.flag_sodium},flag_potassium={self.flag_potassium},flag_total_bases={self.flag_total_bases},flag_cec={self.flag_cec},)"



    


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



    


class MetaGenomicsProduct(Base):
    """
    
    """
    __tablename__ = 'MetaGenomicsProduct'

    id = Column(UUID(), ForeignKey('processedData.id'), primary_key=True, nullable=False )
    input_to_step = Column(Enum('ReadQcAnalysis', 'MetagenomeAssembly', 'ReadBasedTaxonomyAnalysis', 'MetagenomeAnnotation', 'MagsAnalys', name='metagenomicssteps'))
    output_to_step = Column(Enum('ReadQcAnalysis', 'MetagenomeAssembly', 'ReadBasedTaxonomyAnalysis', 'MetagenomeAnnotation', 'MagsAnalys', name='metagenomicssteps'), nullable=False )
    

    

    def __repr__(self):
        return f"MetaGenomicsProduct(id={self.id},input_to_step={self.input_to_step},output_to_step={self.output_to_step},)"



    


class MicrobialBiomassProduct(Base):
    """
    
    """
    __tablename__ = 'MicrobialBiomassProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    rep = Column(Numeric())
    id = Column(UUID(), ForeignKey('processedData.id'), primary_key=True, nullable=False )
    mbc_id = Column(UUID(), ForeignKey('quantityValue.id'))
    mbc_avg = Column(Float())
    mbn_id = Column(UUID(), ForeignKey('quantityValue.id'))
    mbn_avg = Column(Float())
    flag_mbc = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_mbn = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_mbc_avg = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_mbn_avg = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    

    

    def __repr__(self):
        return f"MicrobialBiomassProduct(measure_type={self.measure_type},rep={self.rep},id={self.id},mbc_id={self.mbc_id},mbc_avg={self.mbc_avg},mbn_id={self.mbn_id},mbn_avg={self.mbn_avg},flag_mbc={self.flag_mbc},flag_mbn={self.flag_mbn},flag_mbc_avg={self.flag_mbc_avg},flag_mbn_avg={self.flag_mbn_avg},)"



    


class NitrogenAnalysisProduct(Base):
    """
    
    """
    __tablename__ = 'NitrogenAnalysisProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    rep = Column(Numeric())
    id = Column(UUID(), ForeignKey('processedData.id'), primary_key=True, nullable=False )
    no3_n_id = Column(UUID(), ForeignKey('quantityValue.id'))
    no3_n_avg = Column(Float())
    nh4_n_id = Column(UUID(), ForeignKey('quantityValue.id'))
    nh4_n_avg = Column(Float())
    flag_no3n = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_nh4n = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_no3n_avg = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_nh4n_avg = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    

    

    def __repr__(self):
        return f"NitrogenAnalysisProduct(measure_type={self.measure_type},rep={self.rep},id={self.id},no3_n_id={self.no3_n_id},no3_n_avg={self.no3_n_avg},nh4_n_id={self.nh4_n_id},nh4_n_avg={self.nh4_n_avg},flag_no3n={self.flag_no3n},flag_nh4n={self.flag_nh4n},flag_no3n_avg={self.flag_no3n_avg},flag_nh4n_avg={self.flag_nh4n_avg},)"



    


class PhosphorusAnalysisProduct(Base):
    """
    
    """
    __tablename__ = 'PhosphorusAnalysisProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    rep = Column(Numeric())
    id = Column(UUID(), ForeignKey('processedData.id'), primary_key=True, nullable=False )
    extraction_method = Column(Text())
    phosphorus_id = Column(UUID(), ForeignKey('quantityValue.id'))
    phosphorus_avg = Column(Float())
    flag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    flag_avg = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    

    

    def __repr__(self):
        return f"PhosphorusAnalysisProduct(measure_type={self.measure_type},rep={self.rep},id={self.id},extraction_method={self.extraction_method},phosphorus_id={self.phosphorus_id},phosphorus_avg={self.phosphorus_avg},flag={self.flag},flag_avg={self.flag_avg},)"



    


class RespirationProduct(Base):
    """
    
    """
    __tablename__ = 'RespirationProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    id = Column(UUID(), ForeignKey('processedData.id'), primary_key=True, nullable=False )
    respiration_rate_per_day_id = Column(UUID(), ForeignKey('quantityValue.id'))
    flag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    

    

    def __repr__(self):
        return f"RespirationProduct(measure_type={self.measure_type},id={self.id},respiration_rate_per_day_id={self.respiration_rate_per_day_id},flag={self.flag},)"



    


class TextureProduct(Base):
    """
    
    """
    __tablename__ = 'TextureProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    id = Column(UUID(), ForeignKey('processedData.id'), primary_key=True, nullable=False )
    sand_pct_id = Column(UUID(), ForeignKey('quantityValue.id'))
    silt_pct_id = Column(UUID(), ForeignKey('quantityValue.id'))
    clay_pct_id = Column(UUID(), ForeignKey('quantityValue.id'))
    flag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    

    

    def __repr__(self):
        return f"TextureProduct(measure_type={self.measure_type},id={self.id},sand_pct_id={self.sand_pct_id},silt_pct_id={self.silt_pct_id},clay_pct_id={self.clay_pct_id},flag={self.flag},)"



    


class TomographyProduct(Base):
    """
    
    """
    __tablename__ = 'TomographyProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    id = Column(UUID(), ForeignKey('processedData.id'), primary_key=True, nullable=False )
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
    

    

    def __repr__(self):
        return f"TomographyProduct(measure_type={self.measure_type},id={self.id},roi_volume_voxel={self.roi_volume_voxel},voxel_size={self.voxel_size},connected_pores={self.connected_pores},pore_diameter_min={self.pore_diameter_min},pore_diameter_max={self.pore_diameter_max},pore_diameter_mean={self.pore_diameter_mean},pore_diameter_median={self.pore_diameter_median},pore_diameter_variance={self.pore_diameter_variance},pore_volume_mean={self.pore_volume_mean},total_pore_volume={self.total_pore_volume},permeability_x={self.permeability_x},flow_rate_x={self.flow_rate_x},tortuosity_x={self.tortuosity_x},permeability_y={self.permeability_y},flow_rate_y={self.flow_rate_y},tortuosity_y={self.tortuosity_y},permeability_z={self.permeability_z},flow_rate_z={self.flow_rate_z},tortuosity_z={self.tortuosity_z},flag_xct={self.flag_xct},)"



    


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



    


class PHProduct(Base):
    """
    
    """
    __tablename__ = 'pHProduct'

    measure_type = Column(Enum('Single', 'Replicate', 'Average', name='productmeasuretype'))
    id = Column(UUID(), ForeignKey('processedData.id'), primary_key=True, nullable=False )
    ph = Column(Float())
    flag = Column(Enum('Below_Detection', 'Below_Reporting_Limit', 'High_Background', 'Out_of_Range', 'Outlier', 'Data_not_available', 'Failed_QC', 'Insufficient_Material', name='processeddataflag'))
    

    

    def __repr__(self):
        return f"pHProduct(measure_type={self.measure_type},id={self.id},ph={self.ph},flag={self.flag},)"



    


class Changelog(Base):
    """
    
    """
    __tablename__ = 'changelog'

    version = Column(Text(), primary_key=True, nullable=False )
    changelog = Column(Text(), nullable=False )
    

    

    def __repr__(self):
        return f"changelog(version={self.version},changelog={self.changelog},)"



    


