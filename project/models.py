from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    TypeVar,
    Union
)
from uuid import UUID 

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)

if sys.version_info.minor >= 12:
    from typing import TypeAliasType 
else:
    from typing_extensions import TypeAliasType 



metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root



_T = TypeVar("_T")

AnyShapeArray = TypeAliasType(
    "AnyShapeArray", list[Union[_T, "AnyShapeArray[_T]"]], type_params=(_T,)
)
linkml_meta = LinkMLMeta({'default_prefix': 'analysis_api_schema',
     'default_range': 'string',
     'description': 'LinkML-based schema for MONet soil analysis data management '
                    'and metadata enrichment.\n'
                    'This schema defines the data models for samples, processed '
                    'samples, site metadata,\n'
                    'and enrichment providers used in the MONet Analysis API.',
     'id': 'https://w3id.org/MONet/analysis-api-schema',
     'imports': ['linkml:types',
                 'enums',
                 'value_tables',
                 'metadata',
                 'methods',
                 'products',
                 'administration',
                 'campaign',
                 'study',
                 'zip_download'],
     'license': 'MIT',
     'name': 'analysis-api-schema',
     'prefixes': {'analysis_api_schema': {'prefix_prefix': 'analysis_api_schema',
                                          'prefix_reference': 'https://w3id.org/MONet/analysis-api-schema/'}},
     'see_also': ['https://MONet.github.io/analysis-api-schema',
                  'https://github.com/pnnl/analysis-api'],
     'source_file': './src/analysis_api_schema/schema/analysis_api_schema.yaml',
     'title': 'MONet Analysis API Schema'} )

class Samplebasetype(str, Enum):
    """
    Base types for sample entities
    """
    # A physical sample
    sample = "sample"
    # A sample that has undergone processing
    processed_sample = "processed_sample"


class Sampletype(str, Enum):
    """
    Types of samples that can be collected
    """
    # Soil sample
    soil_sample = "soil_sample"
    # Aerosol sample
    aerosol_sample = "aerosol_sample"


class Soiltype(str, Enum):
    """
    Specific types of soil samples
    """
    # Soil core sample
    soil_core = "soil_core"
    # Surface layer soil sample
    surface_layer = "surface_layer"


class Aerosoltype(str, Enum):
    """
    Types of aerosol samples
    """
    # Sea salt aerosol
    sea_salt = "sea_salt"
    # Dust aerosol
    dust = "dust"
    # Volcanic ash aerosol
    volcanic_ash = "volcanic_ash"


class Processedsampletype(str, Enum):
    """
    Types of processed samples
    """
    # Analyte sample
    analyte = "analyte"
    # Core section sample
    coreSection = "coreSection"
    # Replicate sample
    replicate = "replicate"


class Coresectionenum(str, Enum):
    """
    Sections of a core sample
    """
    # Top section of core
    TOP = "TOP"
    # Bottom section of core
    BTM = "BTM"
    # Middle section of core
    MID = "MID"


class Productmeasuretype(str, Enum):
    Single = "Single"
    Replicate = "Replicate"
    Average = "Average"


class Processeddataflag(str, Enum):
    Below_Detection = "Below_Detection"
    Below_Reporting_Limit = "Below_Reporting_Limit"
    High_Background = "High_Background"
    Out_of_Range = "Out_of_Range"
    Outlier = "Outlier"
    Data_not_available = "Data_not_available"
    Failed_QC = "Failed_QC"
    Insufficient_Material = "Insufficient_Material"


class Ionizationenum(str, Enum):
    ESI = "ESI"
    EI = "EI"
    CI = "CI"
    MALDI = "MALDI"


class Metagenomicssteps(str, Enum):
    ReadQcAnalysis = "ReadQcAnalysis"
    MetagenomeAssembly = "MetagenomeAssembly"
    ReadBasedTaxonomyAnalysis = "ReadBasedTaxonomyAnalysis"
    MetagenomeAnnotation = "MetagenomeAnnotation"
    MagsAnalysis = "MagsAnalysis"
    FunctionalAnnotation = "FunctionalAnnotation"
    GenePhylogeny = "GenePhylogeny"


class Alternateidentifiertype(str, Enum):
    instrument_alt_id = "instrument_alt_id"


class Routemethod(str, Enum):
    analysis_activity = "analysis_activity"
    lcms_metabolomics_method = "lcms_metabolomics_method"
    fticr_acquisition_method = "fticr_acquisition_method"
    gravimetric_water_content_method = "gravimetric_water_content_method"
    ph_method = "ph_method"
    hydraulic_properties_method = "hydraulic_properties_method"
    microbial_biomass_method = "microbial_biomass_method"
    xray_computed_tomography_method = "xray_computed_tomography_method"
    REGEN = "REGEN"
    KUO = "KUO"
    respiration_method = "respiration_method"
    texture_method = "texture_method"
    enzyme_activity_method = "enzyme_activity_method"
    elemental_analysis_method = "elemental_analysis_method"
    toc_tn_method = "toc_tn_method"
    bulk_density_method = "bulk_density_method"
    metagenomics_method = "metagenomics_method"


class Samplerole(str, Enum):
    input_sample = "input_sample"
    output_sample = "output_sample"


class Methodname(str, Enum):
    MAOM = "MAOM"
    WOEM = "WOEM"


class Executionresourcetype(str, Enum):
    RZR = "RZR"
    Tahoma = "Tahoma"
    local = "local"
    other = "other"


class Binquality(str, Enum):
    HQ = "HQ"
    MQ = "MQ"
    LQ = "LQ"


class Containertypeenum(str, Enum):
    screw_top_conical = "screw_top_conical"


class Annotationdatabasetype(str, Enum):
    PFAM = "PFAM"
    COG = "COG"
    KEGG = "KEGG"


class Vendorenum(str, Enum):
    waters = "waters"
    agilent = "agilent"
    bruker = "bruker"
    thermo_fisher = "thermo_fisher"
    perkin_elmer = "perkin_elmer"
    scientific_industries = "scientific_industries"
    illumina = "illumina"
    nikon = "nikon"
    fia_lab = "fia_lab"
    shimadzu = "shimadzu"
    regen_ag_lab = "regen_ag_lab"
    kuo = "kuo"


class Modelenum(str, Enum):
    exploris_240 = "exploris_240"
    exploris_480 = "exploris_480"
    ltq_orbitrap_velos = "ltq_orbitrap_velos"
    orbitrap_fusion_lumos = "orbitrap_fusion_lumos"
    orbitrap_eclipse_tribid = "orbitrap_eclipse_tribid"
    orbitrap_q_exactive = "orbitrap_q_exactive"
    solarix_7T = "solarix_7T"
    solarix_12T = "solarix_12T"
    solarix_15T = "solarix_15T"
    agilent_8890A = "agilent_8890A"
    agilent_7980A = "agilent_7980A"
    vortex_genie_2 = "vortex_genie_2"
    novaseq = "novaseq"
    scimax = "scimax"
    ed_400_with_rs_422 = "ed_400_with_rs_422"
    mettler_toledo_30029066 = "mettler_toledo_30029066"
    mettler_toledo_30266628 = "mettler_toledo_30266628"
    ums_hyprop2_020210 = "ums_hyprop2_020210"
    fialyzer_1000 = "fialyzer_1000"
    fialyzer_1001 = "fialyzer_1001"
    fialyzer_1002 = "fialyzer_1002"
    orbitrap_q_exactive_plus = "orbitrap_q_exactive_plus"
    toc_5000A = "toc_5000A"
    toc_lcsh = "toc_lcsh"
    sr_1 = "sr_1"
    xth320 = "xth320"


class Filetype(str, Enum):
    FT_ICR_MS_Analysis_Results = "FT_ICR_MS_Analysis_Results"
    GC_MS_Metabolomics_Results = "GC_MS_Metabolomics_Results"
    Metaproteomics_Workflow_Statistics = "Metaproteomics_Workflow_Statistics"
    Protein_Report = "Protein_Report"
    Peptide_Report = "Peptide_Report"
    Unfiltered_Metaproteomics_Results = "Unfiltered_Metaproteomics_Results"
    Read_Count_and_RPKM = "Read_Count_and_RPKM"
    QC_non_rRNA_R2 = "QC_non_rRNA_R2"
    QC_non_rRNA_R1 = "QC_non_rRNA_R1"
    Metagenome_Bins = "Metagenome_Bins"
    CheckM_Statistics = "CheckM_Statistics"
    GOTTCHA2_Krona_Plot = "GOTTCHA2_Krona_Plot"
    Kraken2_Krona_Plot = "Kraken2_Krona_Plot"
    Centrifuge_Krona_Plot = "Centrifuge_Krona_Plot"
    Kraken2_Classification_Report = "Kraken2_Classification_Report"
    Kraken2_Taxonomic_Classification = "Kraken2_Taxonomic_Classification"
    Centrifuge_Classification_Report = "Centrifuge_Classification_Report"
    Centrifuge_Taxonomic_Classification = "Centrifuge_Taxonomic_Classification"
    Structural_Annotation_GFF = "Structural_Annotation_GFF"
    Functional_Annotation_GFF = "Functional_Annotation_GFF"
    Annotation_Amino_Acid_FASTA = "Annotation_Amino_Acid_FASTA"
    Annotation_Enzyme_Commission = "Annotation_Enzyme_Commission"
    Annotation_KEGG_Orthology = "Annotation_KEGG_Orthology"
    Assembly_Coverage_BAM = "Assembly_Coverage_BAM"
    Assembly_AGP = "Assembly_AGP"
    Assembly_Scaffolds = "Assembly_Scaffolds"
    Assembly_Contigs = "Assembly_Contigs"
    Assembly_Coverage_Stats = "Assembly_Coverage_Stats"
    Filtered_Sequencing_Reads = "Filtered_Sequencing_Reads"
    QC_Statistics = "QC_Statistics"
    TIGRFam_Annotation_GFF = "TIGRFam_Annotation_GFF"
    Clusters_of_Orthologous_Groups_COG_Annotation_GFF = "Clusters_of_Orthologous_Groups_COG_Annotation_GFF"
    CATH_FunFams_Functional_Families_Annotation_GFF = "CATH_FunFams_Functional_Families_Annotation_GFF"
    SUPERFam_Annotation_GFF = "SUPERFam_Annotation_GFF"
    SMART_Annotation_GFF = "SMART_Annotation_GFF"
    Pfam_Annotation_GFF = "Pfam_Annotation_GFF"
    Direct_Infusion_FT_ICR_MS_Raw_Data = "Direct_Infusion_FT_ICR_MS_Raw_Data"


class Instrumentaltidprovider(str, Enum):
    nexus = "nexus"
    dms = "dms"


class Devicetypeenum(str, Enum):
    orbital_shaker = "orbital_shaker"
    thermomixer = "thermomixer"


class Product(str, Enum):
    processedData = "processedData"
    FTICRProduct = "FTICRProduct"
    TomographyProduct = "TomographyProduct"
    MicrobialBiomassProduct = "MicrobialBiomassProduct"
    NitrogenAnalysisProduct = "NitrogenAnalysisProduct"
    PhosphorusAnalysisProduct = "PhosphorusAnalysisProduct"
    pHProduct = "pHProduct"
    ElementalAnalysisProduct = "ElementalAnalysisProduct"
    IonsAnalysisProduct = "IonsAnalysisProduct"
    RespirationProduct = "RespirationProduct"
    EnzymeProduct = "EnzymeProduct"
    TextureProduct = "TextureProduct"
    WEOMProduct = "WEOMProduct"
    HydraulicPropertiesProduct = "HydraulicPropertiesProduct"
    GWCMoistureProduct = "GWCMoistureProduct"
    MAOMProduct = "MAOMProduct"
    BulkDensityProduct = "BulkDensityProduct"
    MetaGenomicsProduct = "MetaGenomicsProduct"


class Samplingactivitytype(str, Enum):
    """
    Types of sampling activities
    """
    # Soil sampling activity
    soil = "soil"
    # Water sampling activity
    water = "water"
    # Air sampling activity
    air = "air"
    # Plant sampling activity
    plant = "plant"
    # No specific activity type
    none = "none"


class Growthfacilityenum(str, Enum):
    """
    Types of growth facilities
    """
    # Field conditions
    field = "field"
    # Commercially purchased
    commercially_purchased = "commercially_purchased"
    # Experimental garden
    experimental_garden = "experimental_garden"
    # Field incubation
    field_incubation = "field_incubation"
    # Greenhouse
    greenhouse = "greenhouse"
    # Growth chamber
    growth_chamber = "growth_chamber"
    # Laboratory incubation
    lab_incubation = "lab_incubation"
    # Open top chamber
    open_top_chamber = "open_top_chamber"
    # Other growth facility type
    other = "other"


class Oxygenstatusenum(str, Enum):
    """
    Oxygen status of samples
    """
    # Aerobic conditions
    aerobic = "aerobic"
    # Anaerobic conditions
    anaerobic = "anaerobic"
    # Anoxic conditions
    anoxic = "anoxic"
    # Facultative conditions
    facultative = "facultative"
    # Microaerophilic conditions
    microaerophilic = "microaerophilic"
    # Microanaerobe conditions
    microanaerobe = "microanaerobe"
    # Obligate aerobe conditions
    oblifate_aerobe = "oblifate_aerobe"
    # Obligate anaerobe conditions
    obligate_anaerobe = "obligate_anaerobe"


class Samplestoretemp(str, Enum):
    """
    Sample storage temperature conditions
    """
    # Fresh storage at 4░C
    fresh4 = "fresh4"
    # Fresh storage at room temperature
    freshroom = "freshroom"
    # Frozen storage at -20░C
    frozen20 = "frozen20"
    # Frozen storage at -80░C
    frozen80 = "frozen80"
    # Other storage temperature
    other = "other"


class Sampbioticenum(str, Enum):
    """
    Sample biotic relationships
    """
    # Free-living organism
    free_living = "free_living"
    # Parasitic organism
    parasite = "parasite"
    # Commensal organism
    commensal = "commensal"
    # Symbiotic organism
    symbiont = "symbiont"


class Storagecondtenum(str, Enum):
    """
    Sample storage conditions
    """
    # Fresh sample
    fresh = "fresh"
    # Frozen sample
    frozen = "frozen"
    # Lyophilized (freeze-dried) sample
    lyophilized = "lyophilized"
    # Other storage condition
    other = "other"


class Landuseenum(str, Enum):
    """
    Land use classifications
    """
    # Badlands
    badlands = "badlands"
    # Urban/city areas
    cities = "cities"
    # Coniferous forests (e.g. pine, spruce, fir, cypress)
    conifers = "conifers"
    # Crop trees (nuts, fruit, christmas trees, nursery trees)
    crop_trees = "crop_trees"
    # Farmstead
    farmstead = "farmstead"
    # Gravel areas
    gravel = "gravel"
    # Hardwood forests (e.g. oak, hickory, elm, aspen)
    hardwoods = "hardwoods"
    # Hayland
    hayland = "hayland"
    # Horticultural plants (e.g. tulips)
    horticultural_plants = "horticultural_plants"
    # Industrial areas
    industrial_areas = "industrial_areas"
    # Intermixed hardwood and conifers
    intermixed = "intermixed"
    # Marshlands (grass, sedges, rushes)
    marshlands = "marshlands"
    # Meadows (grasses, alfalfa, fescue, bromegrass, timothy)
    meadows = "meadows"
    # Mines and quarries
    mines_quarries = "mines_quarries"
    # Mudflats
    mudflats = "mudflats"
    # Oil waste areas
    oil_waste = "oil_waste"
    # Pastureland (grasslands used for livestock grazing)
    pastureland = "pastureland"
    # Permanent snow or ice
    permanent_snow_or_ice = "permanent_snow_or_ice"
    # Rainforest (evergreen forest receiving >406 cm annual rainfall)
    rainforest = "rainforest"
    # Rangeland
    rangeland = "rangeland"
    # Roads and railroads
    roads_railroads = "roads_railroads"
    # Rock surfaces
    rock = "rock"
    # Row crops
    row_crops = "row_crops"
    # Saline seeps
    saline_seeps = "saline_seeps"
    # Salt flats
    salt_flats = "salt_flats"
    # Sand areas
    sand = "sand"
    # Shrub crops (blueberries, nursery ornamentals, filberts)
    shrub_crops = "shrub_crops"
    # Shrub land (e.g. mesquite, sage-brush, creosote bush, shrub oak, eucalyptus)
    shrub_land = "shrub_land"
    # Small grains
    small_grains = "small_grains"
    # Successional shrub land (tree saplings, hazels, sumacs, chokecherry, shrub dogwoods, blackberries)
    successional_shrub_land = "successional_shrub_land"
    # Swamp (permanent or semi-permanent water body dominated by woody plants)
    swamp = "swamp"
    # Tropical vegetation (e.g. mangrove, palms)
    tropical = "tropical"
    # Tundra (mosses, lichens)
    tundra = "tundra"
    # Vegetable crops
    vegetable_crops = "vegetable_crops"
    # Vine crops (grapes)
    vine_crops = "vine_crops"


class Drainageclassenum(str, Enum):
    """
    Soil drainage classifications
    """
    # Excessively drained soil
    Excessively_Drained = "Excessively_Drained"
    # Moderately well drained soil
    Moderately_Well = "Moderately_Well"
    # Poorly drained soil
    Poorly = "Poorly"
    # Somewhat poorly drained soil
    Somewhat_Poorly = "Somewhat_Poorly"
    # Very poorly drained soil
    Very_Poorly = "Very_Poorly"
    # Well drained soil
    Well = "Well"


class Faoclassenum(str, Enum):
    """
    FAO soil classification system
    """
    # Acrisols
    Acrisols = "Acrisols"
    # Alisols
    Alisols = "Alisols"
    # Andosols
    Andosols = "Andosols"
    # Anthrosols
    Anthrosols = "Anthrosols"
    # Arenosols
    Arenosols = "Arenosols"
    # Calcisols
    Calcisols = "Calcisols"
    # Cambisols
    Cambisols = "Cambisols"
    # Chernozems
    Chernozems = "Chernozems"
    # Cryosols
    Cryosols = "Cryosols"
    # Durisols
    Durisols = "Durisols"
    # Ferralsols
    Ferrasols = "Ferrasols"
    # Fluvisols
    Fluvisols = "Fluvisols"
    # Gleysols
    Gleysols = "Gleysols"
    # Gypsisols
    Gypsisols = "Gypsisols"
    # Histosols
    Histosols = "Histosols"
    # Kastanozems
    Kastanozems = "Kastanozems"
    # Leptosols
    Leptosols = "Leptosols"
    # Lixisols
    Lixisols = "Lixisols"
    # Luvisols
    Luvisols = "Luvisols"
    # Nitisols
    Nitosols = "Nitosols"
    # Phaeozems
    Phaeozems = "Phaeozems"
    # Planosols
    Planosols = "Planosols"
    # Plinthosols
    Plinthosols = "Plinthosols"
    # Podzols
    Podzols = "Podzols"
    # Solonchaks
    Solonchaks = "Solonchaks"
    # Solonetz
    Solonetz = "Solonetz"
    # Stagnosols
    Stagnosols = "Stagnosols"
    # Technosols
    Technosols = "Technosols"
    # Umbrisols
    Umbrisols = "Umbrisols"
    # Vertisols
    Vertisols = "Vertisols"


class Neondomainenum(str, Enum):
    """
    NEON ecological domains
    """
    # Northeast domain
    northeast = "northeast"
    # Mid-Atlantic domain
    mid_atlantic = "mid_atlantic"
    # Southeast domain
    southeast = "southeast"
    # Atlantic Neotropical domain
    atlantic_neotropical = "atlantic_neotropical"
    # Great Lakes domain
    great_lakes = "great_lakes"
    # Prairie Peninsula domain
    prairie_peninsula = "prairie_peninsula"
    # Appalachians and Cumberland Plateau domain
    appalachians_and_cumberland_plateau = "appalachians_and_cumberland_plateau"
    # Ozarks Complex domain
    ozarks_complex = "ozarks_complex"
    # Northern Plains domain
    northern_plains = "northern_plains"
    # Central Plains domain
    central_plains = "central_plains"
    # Southern Plains domain
    southern_plains = "southern_plains"
    # Desert Southwest domain
    desert_southwest = "desert_southwest"
    # Northern Rockies domain
    northern_rockies = "northern_rockies"
    # Southern Rockies and Colorado Plateau domain
    southern_rockies_and_colorado_plateau = "southern_rockies_and_colorado_plateau"
    # Great Basin domain
    great_basin = "great_basin"
    # Sierra Nevada domain
    sierra_nevada = "sierra_nevada"
    # Pacific Northwest domain
    pacific_northwest = "pacific_northwest"
    # Pacific Southwest domain
    pacific_southwest = "pacific_southwest"
    # Tundra domain
    tundra = "tundra"
    # Taiga domain
    taiga = "taiga"
    # Pacific Tropical domain
    pacific_tropical = "pacific_tropical"


class Profilepositionenum(str, Enum):
    """
    Soil profile positions
    """
    # Backslope position
    backslope = "backslope"
    # Footslope position
    footslope = "footslope"
    # Shoulder position
    shoulder = "shoulder"
    # Summit position
    summit = "summit"
    # Toeslope position
    toeslope = "toeslope"


class Sedimenttypeenum(str, Enum):
    """
    Types of sediment
    """
    # Biogenous sediment
    biogenous = "biogenous"
    # Cosmogenous sediment
    cosmogenous = "cosmogenous"
    # Hydrogenous sediment
    hydrogenous = "hydrogenous"
    # Lithogenous sediment
    lithogenous = "lithogenous"


class Soilhorizonenum(str, Enum):
    """
    Soil horizon classifications
    """
    # A Horizon - topsoil
    a_horizon = "a_horizon"
    # B Horizon - subsoil
    b_horizon = "b_horizon"
    # C Horizon - parent material
    c_horizon = "c_horizon"
    # E Horizon - eluviated layer
    e_horizon = "e_horizon"
    # O Horizon - organic layer
    o_horizon = "o_horizon"
    # Permafrost layer
    permafrost = "permafrost"
    # R Layer - bedrock
    r_layer = "r_layer"


class Tillageenum(str, Enum):
    """
    Tillage methods
    """
    # Chisel tillage
    Chisel = "Chisel"
    # Cutting disc tillage
    Cutting_Disc = "Cutting_Disc"
    # Disc plough tillage
    Disc_Plough = "Disc_Plough"
    # Drill tillage
    Drill = "Drill"
    # Mouldboard tillage
    Mouldboard = "Mouldboard"
    # Ridge till
    Ridge_Till = "Ridge_Till"
    # Strip tillage
    Streip_Tillage = "Streip_Tillage"
    # Tined tillage
    Tined = "Tined"
    # Zonal tillage
    Zonal_Tillage = "Zonal_Tillage"


class Winddirectionenum(str, Enum):
    """
    Wind direction classifications
    """
    # North wind direction
    north = "north"
    # Northeast wind direction
    north_east = "north_east"
    # East wind direction
    east = "east"
    # Southeast wind direction
    south_east = "south_east"
    # South wind direction
    south = "south"
    # Southwest wind direction
    south_west = "south_west"
    # West wind direction
    west = "west"
    # Northwest wind direction
    north_west = "north_west"


class Projectstatus(str, Enum):
    STARTED = "STARTED"
    COMPLETED = "COMPLETED"
    CLOSED = "CLOSED"
    EXTENDED = "EXTENDED"
    ACCEPTED = "ACCEPTED"
    WITHDRAWN = "WITHDRAWN"



class TimestampValue(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/value_tables.yaml'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'quantityValue',
                       'geolocationValue',
                       'latLongValue',
                       'campaign',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'labDevice']} })
    has_raw_value: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_raw_value',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue']} })
    type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'geolocationValue',
                       'conditioningValue',
                       'samplingActivity',
                       'sample',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity']} })
    was_generated_by: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'geolocationValue',
                       'instrumentData',
                       'containerType']} })


class TextValue(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/value_tables.yaml'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'quantityValue',
                       'geolocationValue',
                       'latLongValue',
                       'campaign',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'labDevice']} })
    language: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'language', 'domain_of': ['textValue']} })
    has_raw_value: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_raw_value',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue']} })
    type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'geolocationValue',
                       'conditioningValue',
                       'samplingActivity',
                       'sample',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity']} })
    was_generated_by: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'geolocationValue',
                       'instrumentData',
                       'containerType']} })


class SoftwareControlledTermValue(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/value_tables.yaml'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'quantityValue',
                       'geolocationValue',
                       'latLongValue',
                       'campaign',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'labDevice']} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['softwareControlledTermValue',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'instrument',
                       'ontologyClass']} })
    version: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['softwareControlledTermValue',
                       'changelog',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'sampleProcessing',
                       'processingSampleLink']} })
    has_raw_value: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_raw_value',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue']} })
    was_generated_by: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'geolocationValue',
                       'instrumentData',
                       'containerType']} })
    type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'geolocationValue',
                       'conditioningValue',
                       'samplingActivity',
                       'sample',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity']} })


class ControlledTermValue(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/value_tables.yaml'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'quantityValue',
                       'geolocationValue',
                       'latLongValue',
                       'campaign',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'labDevice']} })
    has_raw_value: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_raw_value',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue']} })
    was_generated_by: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'geolocationValue',
                       'instrumentData',
                       'containerType']} })
    type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'geolocationValue',
                       'conditioningValue',
                       'samplingActivity',
                       'sample',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity']} })


class PersonValue(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/value_tables.yaml',
         'unique_keys': {'personValue_email_key': {'unique_key_name': 'personValue_email_key',
                                                   'unique_key_slots': ['email']}}})

    email: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'email', 'domain_of': ['personValue']} })
    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    first_name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'first_name', 'domain_of': ['personValue']} })
    last_name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'last_name', 'domain_of': ['personValue']} })
    middle_initial: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'middle_initial', 'domain_of': ['personValue']} })
    orcid: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'orcid', 'domain_of': ['personValue']} })
    profile_image_url: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'profile_image_url', 'domain_of': ['personValue']} })
    websites: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'websites', 'domain_of': ['personValue']} })


class QuantityValue(ConfiguredBaseModel):
    """
    A quantity value with numeric value and optional unit
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/value_tables.yaml'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'quantityValue',
                       'geolocationValue',
                       'latLongValue',
                       'campaign',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'labDevice']} })
    has_value_unit: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_value_unit', 'domain_of': ['quantityValue']} })
    has_unit: Optional[str] = Field(default=None, description="""The human-readable unit name""", json_schema_extra = { "linkml_meta": {'alias': 'has_unit', 'domain_of': ['quantityValue']} })
    has_numeric_value: Optional[float] = Field(default=None, description="""The numeric value of the quantity""", json_schema_extra = { "linkml_meta": {'alias': 'has_numeric_value', 'domain_of': ['quantityValue']} })
    has_minimum_numeric_value: Optional[Decimal] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_minimum_numeric_value', 'domain_of': ['quantityValue']} })
    has_maximum_numeric_value: Optional[Decimal] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_maximum_numeric_value', 'domain_of': ['quantityValue']} })
    has_raw_value: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_raw_value',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue']} })


class GeolocationValue(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/value_tables.yaml'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'quantityValue',
                       'geolocationValue',
                       'latLongValue',
                       'campaign',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'labDevice']} })
    has_raw_value: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_raw_value',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue']} })
    latitude: Optional[Decimal] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'latitude',
         'domain_of': ['geolocationValue', 'latLongValue', 'siteMetadata']} })
    longitude: Optional[Decimal] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'longitude',
         'domain_of': ['geolocationValue', 'latLongValue', 'siteMetadata']} })
    type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'geolocationValue',
                       'conditioningValue',
                       'samplingActivity',
                       'sample',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity']} })
    was_generated_by: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'geolocationValue',
                       'instrumentData',
                       'containerType']} })


class ConditioningValue(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/value_tables.yaml'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    source_material: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'source_material', 'domain_of': ['conditioningValue']} })
    type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'geolocationValue',
                       'conditioningValue',
                       'samplingActivity',
                       'sample',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity']} })
    instrument: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'instrument', 'domain_of': ['conditioningValue']} })
    gas: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'gas', 'domain_of': ['conditioningValue']} })
    pressure: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'pressure', 'domain_of': ['conditioningValue']} })
    has_raw_value: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_raw_value',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue']} })


class LatLongValue(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/value_tables.yaml'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'quantityValue',
                       'geolocationValue',
                       'latLongValue',
                       'campaign',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'labDevice']} })
    has_raw_value: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_raw_value',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue']} })
    latitude: float = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'latitude',
         'domain_of': ['geolocationValue', 'latLongValue', 'siteMetadata']} })
    longitude: float = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'longitude',
         'domain_of': ['geolocationValue', 'latLongValue', 'siteMetadata']} })


class SamplingActivity(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    study_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'study_id', 'domain_of': ['samplingActivity']} })
    type: Samplingactivitytype = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'geolocationValue',
                       'conditioningValue',
                       'samplingActivity',
                       'sample',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity']} })
    sample_name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'sample_name',
         'domain_of': ['samplingActivity', 'sampleBase', 'processedData']} })
    lims_barcode: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'lims_barcode', 'domain_of': ['samplingActivity', 'processedData']} })
    alt_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'alt_id', 'domain_of': ['samplingActivity']} })
    elev_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'elev_id', 'domain_of': ['samplingActivity']} })
    lat_lon_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'lat_lon_id', 'domain_of': ['samplingActivity']} })
    growth_facil: Optional[Growthfacilityenum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'growth_facil', 'domain_of': ['samplingActivity']} })
    other_growth_facil: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'other_growth_facil', 'domain_of': ['samplingActivity']} })
    other_storage_condt: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'other_storage_condt', 'domain_of': ['samplingActivity']} })
    oxygen_relationship: Optional[Oxygenstatusenum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'oxygen_relationship', 'domain_of': ['samplingActivity']} })
    sample_store_temp: Optional[Samplestoretemp] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sample_store_temp', 'domain_of': ['samplingActivity']} })
    samp_biotic_relationship: Optional[Sampbioticenum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'samp_biotic_relationship', 'domain_of': ['samplingActivity']} })
    storage_condt: Optional[Storagecondtenum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'storage_condt', 'domain_of': ['samplingActivity']} })
    air_temp_regm: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'air_temp_regm', 'domain_of': ['samplingActivity']} })
    chem_administration: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'chem_administration', 'domain_of': ['samplingActivity']} })
    collection_date: Optional[datetime ] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'collection_date', 'domain_of': ['samplingActivity']} })
    collection_time: Optional[datetime ] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'collection_time', 'domain_of': ['samplingActivity']} })
    env_broad_scale_other: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'env_broad_scale_other', 'domain_of': ['samplingActivity']} })
    env_local_scale_other: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'env_local_scale_other', 'domain_of': ['samplingActivity']} })
    env_medium_other: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'env_medium_other', 'domain_of': ['samplingActivity']} })
    experimental_factor: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'experimental_factor', 'domain_of': ['samplingActivity']} })
    experimental_factor_other: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'experimental_factor_other', 'domain_of': ['samplingActivity']} })
    extraction_method: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'extraction_method',
         'domain_of': ['samplingActivity', 'PhosphorusAnalysisProduct']} })
    extreme_event: Optional[datetime ] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'extreme_event', 'domain_of': ['samplingActivity']} })
    gaseous_environment: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'gaseous_environment', 'domain_of': ['samplingActivity']} })
    geo_loc_name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'geo_loc_name', 'domain_of': ['samplingActivity']} })
    humidity_regm: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'humidity_regm', 'domain_of': ['samplingActivity']} })
    isotope_exposure: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'isotope_exposure', 'domain_of': ['samplingActivity']} })
    light_regm: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'light_regm', 'domain_of': ['samplingActivity']} })
    link_addit_analys: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'link_addit_analys', 'domain_of': ['samplingActivity']} })
    method_development: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'method_development', 'domain_of': ['samplingActivity']} })
    microbial_biomass_c_meth: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'microbial_biomass_c_meth', 'domain_of': ['samplingActivity']} })
    microbial_biomass_meth: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'microbial_biomass_meth', 'domain_of': ['samplingActivity']} })
    microbial_biomass_n_meth: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'microbial_biomass_n_meth', 'domain_of': ['samplingActivity']} })
    misc_param: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'misc_param', 'domain_of': ['samplingActivity']} })
    neon_plot_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'neon_plot_id', 'domain_of': ['samplingActivity']} })
    non_microb_biomass_method: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'non_microb_biomass_method', 'domain_of': ['samplingActivity']} })
    other_sample_store_temp: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'other_sample_store_temp', 'domain_of': ['samplingActivity']} })
    other_treatment: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'other_treatment', 'domain_of': ['samplingActivity']} })
    ph: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'ph', 'domain_of': ['samplingActivity', 'pHProduct']} })
    ph_meth: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'ph_meth', 'domain_of': ['samplingActivity']} })
    salinity: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'salinity', 'domain_of': ['samplingActivity']} })
    salinity_method: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'salinity_method', 'domain_of': ['samplingActivity']} })
    sample_collected: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sample_collected', 'domain_of': ['samplingActivity']} })
    sample_collection_dev: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sample_collection_dev', 'domain_of': ['samplingActivity']} })
    sample_collection_method: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sample_collection_method', 'domain_of': ['samplingActivity']} })
    sample_end_time: Optional[datetime ] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sample_end_time', 'domain_of': ['samplingActivity']} })
    sample_processing: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sample_processing', 'domain_of': ['samplingActivity']} })
    sample_start_time: Optional[datetime ] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sample_start_time', 'domain_of': ['samplingActivity']} })
    season_environment: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'season_environment', 'domain_of': ['samplingActivity']} })
    shipped_sample_size: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'shipped_sample_size', 'domain_of': ['samplingActivity']} })
    sieving: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sieving', 'domain_of': ['samplingActivity']} })
    start_date_inc: Optional[datetime ] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'start_date_inc', 'domain_of': ['samplingActivity']} })
    tot_nitro_cont_meth: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'tot_nitro_cont_meth', 'domain_of': ['samplingActivity']} })
    tot_org_c_meth: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'tot_org_c_meth', 'domain_of': ['samplingActivity']} })
    watering_regm: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'watering_regm', 'domain_of': ['samplingActivity']} })


class Soil(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    annual_precpt_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'annual_precpt_id', 'domain_of': ['soil']} })
    annual_temp_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'annual_temp_id', 'domain_of': ['soil']} })
    bulk_elect_conductivity_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'bulk_elect_conductivity_id', 'domain_of': ['soil']} })
    density_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'density_id', 'domain_of': ['soil']} })
    depth_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'depth_id', 'domain_of': ['soil']} })
    particle_class_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'particle_class_id', 'domain_of': ['soil']} })
    porosity_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'porosity_id', 'domain_of': ['soil']} })
    pressure_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'pressure_id', 'domain_of': ['soil']} })
    season_precpt_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'season_precpt_id', 'domain_of': ['soil']} })
    season_temp_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'season_temp_id', 'domain_of': ['soil']} })
    size_frac_low_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'size_frac_low_id', 'domain_of': ['soil']} })
    size_frac_up_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'size_frac_up_id', 'domain_of': ['soil']} })
    slope_aspect_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'slope_aspect_id', 'domain_of': ['soil']} })
    slope_gradient_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'slope_gradient_id', 'domain_of': ['soil']} })
    soil_temperature_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'soil_temperature_id', 'domain_of': ['soil']} })
    soil_texture_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'soil_texture_id', 'domain_of': ['soil']} })
    temp_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'temp_id', 'domain_of': ['soil']} })
    water_content_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'water_content_id', 'domain_of': ['soil']} })
    wind_speed_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'wind_speed_id', 'domain_of': ['soil']} })
    cur_land_use: Optional[Landuseenum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cur_land_use', 'domain_of': ['soil']} })
    drainage_class: Optional[Drainageclassenum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'drainage_class', 'domain_of': ['soil']} })
    fao_class: Optional[Faoclassenum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'fao_class', 'domain_of': ['soil']} })
    neon_domain: Optional[Neondomainenum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'neon_domain', 'domain_of': ['soil', 'siteMetadata']} })
    profile_position: Optional[Profilepositionenum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'profile_position', 'domain_of': ['soil']} })
    sediment_type: Optional[Sedimenttypeenum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sediment_type', 'domain_of': ['soil']} })
    soil_horizon: Optional[Soilhorizonenum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'soil_horizon', 'domain_of': ['soil']} })
    tillage: Optional[Tillageenum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'tillage', 'domain_of': ['soil']} })
    wind_direction: Optional[Winddirectionenum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'wind_direction', 'domain_of': ['soil']} })
    agrochem_addition: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'agrochem_addition', 'domain_of': ['soil']} })
    al_sat: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'al_sat', 'domain_of': ['soil']} })
    al_sat_meth: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'al_sat_meth', 'domain_of': ['soil']} })
    biotic_regm: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'biotic_regm', 'domain_of': ['soil']} })
    climate_environment: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'climate_environment', 'domain_of': ['soil']} })
    core_collector: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'core_collector', 'domain_of': ['soil']} })
    crop_rotation: Optional[bool] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'crop_rotation', 'domain_of': ['soil']} })
    crop_rotation_schedule: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'crop_rotation_schedule', 'domain_of': ['soil']} })
    cur_vegetation: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cur_vegetation', 'domain_of': ['soil']} })
    cur_vegetation_meth: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cur_vegetation_meth', 'domain_of': ['soil']} })
    filter_method: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'filter_method', 'domain_of': ['soil']} })
    fire: Optional[datetime ] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'fire', 'domain_of': ['soil']} })
    flooding: Optional[datetime ] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flooding', 'domain_of': ['soil']} })
    heavy_metals: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'heavy_metals', 'domain_of': ['soil']} })
    heavy_metals_meth: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'heavy_metals_meth', 'domain_of': ['soil']} })
    horizon_meth: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'horizon_meth', 'domain_of': ['soil']} })
    infiltration_1: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'infiltration_1', 'domain_of': ['soil']} })
    infiltration_2: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'infiltration_2', 'domain_of': ['soil']} })
    infiltration_notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'infiltration_notes', 'domain_of': ['soil']} })
    link_class_info: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'link_class_info', 'domain_of': ['soil']} })
    link_climate_info: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'link_climate_info', 'domain_of': ['soil']} })
    local_class: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'local_class', 'domain_of': ['soil']} })
    local_class_meth: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'local_class_meth', 'domain_of': ['soil']} })
    perturbation: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'perturbation', 'domain_of': ['soil']} })
    previous_land_use: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'previous_land_use', 'domain_of': ['soil']} })
    previous_land_use_meth: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'previous_land_use_meth', 'domain_of': ['soil']} })
    site_definition: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'site_definition', 'domain_of': ['soil']} })
    soil_type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'soil_type', 'domain_of': ['soil', 'soil_sample']} })
    soil_type_meth: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'soil_type_meth', 'domain_of': ['soil']} })
    texture_meth: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'texture_meth', 'domain_of': ['soil']} })
    water_content_meth: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'water_content_meth', 'domain_of': ['soil']} })
    weather: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'weather', 'domain_of': ['soil']} })


class SiteMetadata(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    nasa_mean_annual_temp_c_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'nasa_mean_annual_temp_c_id', 'domain_of': ['siteMetadata']} })
    nasa_mean_annual_precip_mm_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'nasa_mean_annual_precip_mm_id', 'domain_of': ['siteMetadata']} })
    nasa_max_annual_temp_c_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'nasa_max_annual_temp_c_id', 'domain_of': ['siteMetadata']} })
    nasa_min_annual_temp_c_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'nasa_min_annual_temp_c_id', 'domain_of': ['siteMetadata']} })
    nasa_mean_wind_speed_ms_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'nasa_mean_wind_speed_ms_id', 'domain_of': ['siteMetadata']} })
    nasa_mean_relative_humidity_pct_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'nasa_mean_relative_humidity_pct_id', 'domain_of': ['siteMetadata']} })
    nasa_frost_days_per_year_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'nasa_frost_days_per_year_id', 'domain_of': ['siteMetadata']} })
    nasa_mean_dew_point_c_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'nasa_mean_dew_point_c_id', 'domain_of': ['siteMetadata']} })
    nasa_mean_vapor_pressure_kpa_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'nasa_mean_vapor_pressure_kpa_id', 'domain_of': ['siteMetadata']} })
    nasa_mean_surface_pressure_kpa_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'nasa_mean_surface_pressure_kpa_id', 'domain_of': ['siteMetadata']} })
    nasa_mean_shortwave_radiation_wm2_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'nasa_mean_shortwave_radiation_wm2_id', 'domain_of': ['siteMetadata']} })
    nasa_mean_longwave_radiation_wm2_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'nasa_mean_longwave_radiation_wm2_id', 'domain_of': ['siteMetadata']} })
    epa_ecoregion_l1: Optional[str] = Field(default=None, description="""EPA Level 1 Ecoregion name""", json_schema_extra = { "linkml_meta": {'alias': 'epa_ecoregion_l1', 'domain_of': ['siteMetadata']} })
    epa_ecoregion_l2: Optional[str] = Field(default=None, description="""EPA Level 2 Ecoregion name""", json_schema_extra = { "linkml_meta": {'alias': 'epa_ecoregion_l2', 'domain_of': ['siteMetadata']} })
    epa_ecoregion_l3: Optional[str] = Field(default=None, description="""EPA Level 3 Ecoregion name""", json_schema_extra = { "linkml_meta": {'alias': 'epa_ecoregion_l3', 'domain_of': ['siteMetadata']} })
    epa_ecoregion_l4: Optional[str] = Field(default=None, description="""EPA Level 4 Ecoregion name""", json_schema_extra = { "linkml_meta": {'alias': 'epa_ecoregion_l4', 'domain_of': ['siteMetadata']} })
    neon_domain: Optional[str] = Field(default=None, description="""NEON Ecological Domain name""", json_schema_extra = { "linkml_meta": {'alias': 'neon_domain', 'domain_of': ['soil', 'siteMetadata']} })
    created_at: datetime = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'created_at', 'domain_of': ['siteMetadata']} })
    updated_at: datetime = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'updated_at', 'domain_of': ['siteMetadata']} })
    cache_key: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'cache_key', 'domain_of': ['siteMetadata']} })
    latitude: float = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'latitude',
         'domain_of': ['geolocationValue', 'latLongValue', 'siteMetadata']} })
    longitude: float = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'longitude',
         'domain_of': ['geolocationValue', 'latLongValue', 'siteMetadata']} })
    provider: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'provider', 'domain_of': ['siteMetadata']} })
    enriched_at: datetime = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'enriched_at', 'domain_of': ['siteMetadata']} })


class SamplingActivitySiteMetadataLink(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    sampling_activity_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'sampling_activity_id',
         'domain_of': ['sampling_activity_site_metadata_link', 'sample']} })
    site_metadata_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'site_metadata_id',
         'domain_of': ['sampling_activity_site_metadata_link']} })


class BulkDensityMethod(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    analytic: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'analytic',
         'domain_of': ['BulkDensityMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })


class ElementalAnalysisMethod(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })


class EnzymeActivityMethod(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    analytic: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'analytic',
         'domain_of': ['BulkDensityMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    location: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'location',
         'domain_of': ['EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    incubation_temp_c: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'incubation_temp_c', 'domain_of': ['EnzymeActivityMethod']} })
    incubation_time: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'incubation_time', 'domain_of': ['EnzymeActivityMethod']} })
    wavelength: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'wavelength', 'domain_of': ['EnzymeActivityMethod', 'KuoMethod']} })
    method: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'method',
         'domain_of': ['EnzymeActivityMethod', 'KuoMethod', 'TextureMethod']} })


class FTICRAcquisitionMethod(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    analytic: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'analytic',
         'domain_of': ['BulkDensityMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    location: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'location',
         'domain_of': ['EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    injection: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'injection',
         'domain_of': ['FTICR_AcquisitionMethod', 'LCMS_MetabolomicsMethod']} })
    ionization: Ionizationenum = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'ionization', 'domain_of': ['FTICR_AcquisitionMethod']} })
    polarity: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'polarity',
         'domain_of': ['FTICR_AcquisitionMethod', 'LCMS_MetabolomicsMethod']} })
    iat: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'iat', 'domain_of': ['FTICR_AcquisitionMethod']} })
    fid: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'fid', 'domain_of': ['FTICR_AcquisitionMethod']} })
    mass_range: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'mass_range', 'domain_of': ['FTICR_AcquisitionMethod']} })


class GravimetricWaterContentMethod(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    analytic: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'analytic',
         'domain_of': ['BulkDensityMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    location: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'location',
         'domain_of': ['EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })


class HydraulicPropertiesMethod(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    analytic: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'analytic',
         'domain_of': ['BulkDensityMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    location: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'location',
         'domain_of': ['EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    fitting_model: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'fitting_model', 'domain_of': ['HydraulicPropertiesMethod']} })


class KuoMethod(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    analytic: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'analytic',
         'domain_of': ['BulkDensityMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    location: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'location',
         'domain_of': ['EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    method: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'method',
         'domain_of': ['EnzymeActivityMethod', 'KuoMethod', 'TextureMethod']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    detection_limit: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'detection_limit', 'domain_of': ['KuoMethod']} })
    wavelength: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'wavelength', 'domain_of': ['EnzymeActivityMethod', 'KuoMethod']} })


class LCMSMetabolomicsMethod(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    analytic: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'analytic',
         'domain_of': ['BulkDensityMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    location: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'location',
         'domain_of': ['EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    injection: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'injection',
         'domain_of': ['FTICR_AcquisitionMethod', 'LCMS_MetabolomicsMethod']} })
    polarity: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'polarity',
         'domain_of': ['FTICR_AcquisitionMethod', 'LCMS_MetabolomicsMethod']} })
    column: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'column', 'domain_of': ['LCMS_MetabolomicsMethod', 'TOC_TN_Method']} })
    mode: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'mode',
         'domain_of': ['LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'TOC_TN_Method']} })
    method_duration: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'method_duration', 'domain_of': ['LCMS_MetabolomicsMethod']} })
    runtime: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'runtime', 'domain_of': ['LCMS_MetabolomicsMethod']} })
    resolution: float = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'resolution', 'domain_of': ['LCMS_MetabolomicsMethod']} })
    scan_range: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'scan_range', 'domain_of': ['LCMS_MetabolomicsMethod']} })
    dd_ms2_resolution: float = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'dd_ms2_resolution', 'domain_of': ['LCMS_MetabolomicsMethod']} })
    loop_count: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'loop_count', 'domain_of': ['LCMS_MetabolomicsMethod']} })
    isolation_window: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'isolation_window', 'domain_of': ['LCMS_MetabolomicsMethod']} })


class MicrobialBiomassMethod(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    analytic: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'analytic',
         'domain_of': ['BulkDensityMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    location: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'location',
         'domain_of': ['EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    detector: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'detector', 'domain_of': ['MicrobialBiomassMethod', 'TOC_TN_Method']} })
    mode: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'mode',
         'domain_of': ['LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'TOC_TN_Method']} })
    injection_volume: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'injection_volume',
         'domain_of': ['MicrobialBiomassMethod', 'TOC_TN_Method']} })
    sample_volume: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'sample_volume',
         'domain_of': ['MicrobialBiomassMethod', 'TOC_TN_Method']} })
    number_of_injections: float = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'number_of_injections',
         'domain_of': ['MicrobialBiomassMethod', 'TOC_TN_Method']} })
    check_standard_spacing: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'check_standard_spacing',
         'domain_of': ['MicrobialBiomassMethod', 'TOC_TN_Method']} })


class PHMethod(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    analytic: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'analytic',
         'domain_of': ['BulkDensityMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    location: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'location',
         'domain_of': ['EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    calibration: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'calibration', 'domain_of': ['PH_Method']} })


class RespirationMethod(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    analytic: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'analytic',
         'domain_of': ['BulkDensityMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    respiration_analysis_type: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'respiration_analysis_type', 'domain_of': ['RespirationMethod']} })
    sample_volume_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sample_volume_id', 'domain_of': ['RespirationMethod']} })
    scale_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'scale_id', 'domain_of': ['RespirationMethod']} })
    duration_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'duration_id', 'domain_of': ['RespirationMethod']} })
    sampling_time_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sampling_time_id', 'domain_of': ['RespirationMethod']} })
    bottle_vol_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'bottle_vol_id', 'domain_of': ['RespirationMethod']} })


class TOCTNMethod(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    analytic: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'analytic',
         'domain_of': ['BulkDensityMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    location: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'location',
         'domain_of': ['EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    column: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'column', 'domain_of': ['LCMS_MetabolomicsMethod', 'TOC_TN_Method']} })
    mode: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'mode',
         'domain_of': ['LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'TOC_TN_Method']} })
    detector: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'detector', 'domain_of': ['MicrobialBiomassMethod', 'TOC_TN_Method']} })
    injection_volume: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'injection_volume',
         'domain_of': ['MicrobialBiomassMethod', 'TOC_TN_Method']} })
    sample_volume: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'sample_volume',
         'domain_of': ['MicrobialBiomassMethod', 'TOC_TN_Method']} })
    number_of_injections: float = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'number_of_injections',
         'domain_of': ['MicrobialBiomassMethod', 'TOC_TN_Method']} })
    check_standard_spacing: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'check_standard_spacing',
         'domain_of': ['MicrobialBiomassMethod', 'TOC_TN_Method']} })


class TextureMethod(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    analytic: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'analytic',
         'domain_of': ['BulkDensityMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    location: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'location',
         'domain_of': ['EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    method: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'method',
         'domain_of': ['EnzymeActivityMethod', 'KuoMethod', 'TextureMethod']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })


class XrayComputedTomographyMethod(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    analytic: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'analytic',
         'domain_of': ['BulkDensityMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    location: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'location',
         'domain_of': ['EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    x_ray_power: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'x_ray_power', 'domain_of': ['XrayComputedTomographyMethod']} })
    cu_filter: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'cu_filter', 'domain_of': ['XrayComputedTomographyMethod']} })
    total_projections_collected: float = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'total_projections_collected',
         'domain_of': ['XrayComputedTomographyMethod']} })
    rotation: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'rotation', 'domain_of': ['XrayComputedTomographyMethod']} })
    frames_recording_per_projection: float = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'frames_recording_per_projection',
         'domain_of': ['XrayComputedTomographyMethod']} })
    exposure_time_per_frame: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'exposure_time_per_frame',
         'domain_of': ['XrayComputedTomographyMethod']} })
    image_voxel_size_is: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'image_voxel_size_is', 'domain_of': ['XrayComputedTomographyMethod']} })


class BulkDensityProduct(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    measure_type: Optional[Productmeasuretype] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'measure_type',
         'domain_of': ['BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    bulk_density_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'bulk_density_id', 'domain_of': ['BulkDensityProduct']} })
    flag: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag',
         'domain_of': ['BulkDensityProduct',
                       'EnzymeProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'pHProduct']} })


class ElementalAnalysisProduct(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    measure_type: Optional[Productmeasuretype] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'measure_type',
         'domain_of': ['BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    total_carbon_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'total_carbon_id', 'domain_of': ['ElementalAnalysisProduct']} })
    total_nitrogen_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'total_nitrogen_id',
         'domain_of': ['ElementalAnalysisProduct', 'MAOMProduct', 'WEOMProduct']} })
    total_kjeldahl_nitrogen_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'total_kjeldahl_nitrogen_id',
         'domain_of': ['ElementalAnalysisProduct']} })
    total_sulfur_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'total_sulfur_id', 'domain_of': ['ElementalAnalysisProduct']} })
    flag_total_carbon: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_total_carbon', 'domain_of': ['ElementalAnalysisProduct']} })
    flag_total_nitrogen: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_total_nitrogen', 'domain_of': ['ElementalAnalysisProduct']} })
    flag_tkn: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_tkn', 'domain_of': ['ElementalAnalysisProduct']} })
    flag_total_sulfur: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_total_sulfur', 'domain_of': ['ElementalAnalysisProduct']} })


class EnzymeProduct(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    measure_type: Optional[Productmeasuretype] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'measure_type',
         'domain_of': ['BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    beta_glucosidase_ug_pnp_per_g_per_h_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'beta_glucosidase_ug_pnp_per_g_per_h_id',
         'domain_of': ['EnzymeProduct']} })
    flag: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag',
         'domain_of': ['BulkDensityProduct',
                       'EnzymeProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'pHProduct']} })


class FTICRProduct(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    measure_type: Optional[Productmeasuretype] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'measure_type',
         'domain_of': ['BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct']} })
    rep: Optional[Decimal] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'rep',
         'domain_of': ['FTICRProduct',
                       'MAOMProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'WEOMProduct',
                       'replicate']} })
    aq: Optional[Decimal] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'aq', 'domain_of': ['FTICRProduct']} })
    h_c_average: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'h_c_average', 'domain_of': ['FTICRProduct']} })
    o_c_average: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'o_c_average', 'domain_of': ['FTICRProduct']} })
    c_average: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'c_average', 'domain_of': ['FTICRProduct']} })
    percent_mz_assigned_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'percent_mz_assigned_id', 'domain_of': ['FTICRProduct']} })
    rms_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'rms_id', 'domain_of': ['FTICRProduct']} })
    dbe_average: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'dbe_average', 'domain_of': ['FTICRProduct']} })
    low_mass_accuracy_flag: Optional[bool] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'low_mass_accuracy_flag', 'domain_of': ['FTICRProduct']} })
    low_mz_assignment_flag: Optional[bool] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'low_mz_assignment_flag', 'domain_of': ['FTICRProduct']} })


class GWCMoistureProduct(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    measure_type: Optional[Productmeasuretype] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'measure_type',
         'domain_of': ['BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    gwc_percent_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'gwc_percent_id', 'domain_of': ['GWCMoistureProduct']} })
    flag: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag',
         'domain_of': ['BulkDensityProduct',
                       'EnzymeProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'pHProduct']} })


class HydraulicPropertiesProduct(ConfiguredBaseModel):
    """
    Soil hydraulic parameters derived from HYPROP evaporation-experiment data. One row per core section; the four attributes are the four VGM model parameters.  Proposal_ID, sampling_set, and core_section are inherited from the parent processedData record.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    measure_type: Optional[Productmeasuretype] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'measure_type',
         'domain_of': ['BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    alpha: Optional[float] = Field(default=None, description="""Van Genuchten shape parameter alpha (1/cm). Controls the inverse of the air-entry suction; typically fitted by HYPROP-FIT or similar software.""", json_schema_extra = { "linkml_meta": {'alias': 'alpha', 'domain_of': ['HydraulicPropertiesProduct']} })
    n: Optional[float] = Field(default=None, description="""Van Genuchten pore-size distribution index n (dimensionless, n > 1). Controls the slope of the water-retention curve.""", json_schema_extra = { "linkml_meta": {'alias': 'n', 'domain_of': ['HydraulicPropertiesProduct']} })
    theta_r: Optional[float] = Field(default=None, description="""Residual volumetric water content theta_r (cm3 cm). The water content at which liquid conductivity approaches zero.""", json_schema_extra = { "linkml_meta": {'alias': 'theta_r', 'domain_of': ['HydraulicPropertiesProduct']} })
    theta_s: Optional[float] = Field(default=None, description="""Saturated volumetric water content theta_s (cm3 cm e-3). Approximates total porosity under saturated conditions.""", json_schema_extra = { "linkml_meta": {'alias': 'theta_s', 'domain_of': ['HydraulicPropertiesProduct']} })
    flag: Optional[Processeddataflag] = Field(default=None, description="""QC flag for the entire VGM fit (e.g. missing sample, failed QC).""", json_schema_extra = { "linkml_meta": {'alias': 'flag',
         'domain_of': ['BulkDensityProduct',
                       'EnzymeProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'pHProduct']} })


class IonsAnalysisProduct(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    measure_type: Optional[Productmeasuretype] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'measure_type',
         'domain_of': ['BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    sulfate_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sulfate_id', 'domain_of': ['IonsAnalysisProduct']} })
    boron_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'boron_id', 'domain_of': ['IonsAnalysisProduct']} })
    zinc_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'zinc_id', 'domain_of': ['IonsAnalysisProduct']} })
    manganate_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'manganate_id', 'domain_of': ['IonsAnalysisProduct']} })
    copper_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'copper_id', 'domain_of': ['IonsAnalysisProduct']} })
    iron_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'iron_id', 'domain_of': ['IonsAnalysisProduct']} })
    calcium_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'calcium_id', 'domain_of': ['IonsAnalysisProduct']} })
    magnesium_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'magnesium_id', 'domain_of': ['IonsAnalysisProduct']} })
    sodium_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sodium_id', 'domain_of': ['IonsAnalysisProduct']} })
    potassium_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'potassium_id', 'domain_of': ['IonsAnalysisProduct']} })
    total_bases_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'total_bases_id', 'domain_of': ['IonsAnalysisProduct']} })
    cation_exchange_capacity_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'cation_exchange_capacity_id', 'domain_of': ['IonsAnalysisProduct']} })
    flag_sulfate: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_sulfate', 'domain_of': ['IonsAnalysisProduct']} })
    flag_boron: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_boron', 'domain_of': ['IonsAnalysisProduct']} })
    flag_zinc: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_zinc', 'domain_of': ['IonsAnalysisProduct']} })
    flag_manganate: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_manganate', 'domain_of': ['IonsAnalysisProduct']} })
    flag_copper: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_copper', 'domain_of': ['IonsAnalysisProduct']} })
    flag_iron: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_iron', 'domain_of': ['IonsAnalysisProduct']} })
    flag_calcium: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_calcium', 'domain_of': ['IonsAnalysisProduct']} })
    flag_magnesium: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_magnesium', 'domain_of': ['IonsAnalysisProduct']} })
    flag_sodium: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_sodium', 'domain_of': ['IonsAnalysisProduct']} })
    flag_potassium: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_potassium', 'domain_of': ['IonsAnalysisProduct']} })
    flag_total_bases: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_total_bases', 'domain_of': ['IonsAnalysisProduct']} })
    flag_cec: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_cec', 'domain_of': ['IonsAnalysisProduct']} })


class MAOMProduct(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    measure_type: Optional[Productmeasuretype] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'measure_type',
         'domain_of': ['BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct']} })
    rep: Optional[Decimal] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'rep',
         'domain_of': ['FTICRProduct',
                       'MAOMProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'WEOMProduct',
                       'replicate']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    total_organic_carbon_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'total_organic_carbon_id',
         'domain_of': ['MAOMProduct', 'WEOMProduct']} })
    total_organic_carbon_avg: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'total_organic_carbon_avg',
         'domain_of': ['MAOMProduct', 'WEOMProduct']} })
    total_nitrogen_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'total_nitrogen_id',
         'domain_of': ['ElementalAnalysisProduct', 'MAOMProduct', 'WEOMProduct']} })
    total_nitrogen_avg: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'total_nitrogen_avg', 'domain_of': ['MAOMProduct', 'WEOMProduct']} })
    flag_toc: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_toc', 'domain_of': ['MAOMProduct', 'WEOMProduct']} })
    flag_tn: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_tn', 'domain_of': ['MAOMProduct', 'WEOMProduct']} })
    flag_toc_avg: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_toc_avg', 'domain_of': ['MAOMProduct', 'WEOMProduct']} })
    flag_tn_avg: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_tn_avg', 'domain_of': ['MAOMProduct', 'WEOMProduct']} })


class MetaGenomicsProduct(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    input_to_step: Optional[Metagenomicssteps] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'input_to_step', 'domain_of': ['MetaGenomicsProduct']} })
    output_to_step: Metagenomicssteps = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'output_to_step', 'domain_of': ['MetaGenomicsProduct']} })


class MicrobialBiomassProduct(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    measure_type: Optional[Productmeasuretype] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'measure_type',
         'domain_of': ['BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct']} })
    rep: Optional[Decimal] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'rep',
         'domain_of': ['FTICRProduct',
                       'MAOMProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'WEOMProduct',
                       'replicate']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    mbc_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'mbc_id', 'domain_of': ['MicrobialBiomassProduct']} })
    mbc_avg: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'mbc_avg', 'domain_of': ['MicrobialBiomassProduct']} })
    mbn_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'mbn_id', 'domain_of': ['MicrobialBiomassProduct']} })
    mbn_avg: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'mbn_avg', 'domain_of': ['MicrobialBiomassProduct']} })
    flag_mbc: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_mbc', 'domain_of': ['MicrobialBiomassProduct']} })
    flag_mbn: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_mbn', 'domain_of': ['MicrobialBiomassProduct']} })
    flag_mbc_avg: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_mbc_avg', 'domain_of': ['MicrobialBiomassProduct']} })
    flag_mbn_avg: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_mbn_avg', 'domain_of': ['MicrobialBiomassProduct']} })


class NitrogenAnalysisProduct(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    measure_type: Optional[Productmeasuretype] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'measure_type',
         'domain_of': ['BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct']} })
    rep: Optional[Decimal] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'rep',
         'domain_of': ['FTICRProduct',
                       'MAOMProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'WEOMProduct',
                       'replicate']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    no3_n_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'no3_n_id', 'domain_of': ['NitrogenAnalysisProduct']} })
    no3_n_avg: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'no3_n_avg', 'domain_of': ['NitrogenAnalysisProduct']} })
    nh4_n_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'nh4_n_id', 'domain_of': ['NitrogenAnalysisProduct']} })
    nh4_n_avg: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'nh4_n_avg', 'domain_of': ['NitrogenAnalysisProduct']} })
    flag_no3n: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_no3n', 'domain_of': ['NitrogenAnalysisProduct']} })
    flag_nh4n: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_nh4n', 'domain_of': ['NitrogenAnalysisProduct']} })
    flag_no3n_avg: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_no3n_avg', 'domain_of': ['NitrogenAnalysisProduct']} })
    flag_nh4n_avg: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_nh4n_avg', 'domain_of': ['NitrogenAnalysisProduct']} })


class PhosphorusAnalysisProduct(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    measure_type: Optional[Productmeasuretype] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'measure_type',
         'domain_of': ['BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct']} })
    rep: Optional[Decimal] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'rep',
         'domain_of': ['FTICRProduct',
                       'MAOMProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'WEOMProduct',
                       'replicate']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    extraction_method: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'extraction_method',
         'domain_of': ['samplingActivity', 'PhosphorusAnalysisProduct']} })
    phosphorus_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'phosphorus_id', 'domain_of': ['PhosphorusAnalysisProduct']} })
    phosphorus_avg: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'phosphorus_avg', 'domain_of': ['PhosphorusAnalysisProduct']} })
    flag: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag',
         'domain_of': ['BulkDensityProduct',
                       'EnzymeProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'pHProduct']} })
    flag_avg: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_avg', 'domain_of': ['PhosphorusAnalysisProduct']} })


class RespirationProduct(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    measure_type: Optional[Productmeasuretype] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'measure_type',
         'domain_of': ['BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    respiration_rate_per_day_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'respiration_rate_per_day_id', 'domain_of': ['RespirationProduct']} })
    flag: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag',
         'domain_of': ['BulkDensityProduct',
                       'EnzymeProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'pHProduct']} })


class TextureProduct(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    measure_type: Optional[Productmeasuretype] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'measure_type',
         'domain_of': ['BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    sand_pct_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sand_pct_id', 'domain_of': ['TextureProduct']} })
    silt_pct_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'silt_pct_id', 'domain_of': ['TextureProduct']} })
    clay_pct_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'clay_pct_id', 'domain_of': ['TextureProduct']} })
    flag: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag',
         'domain_of': ['BulkDensityProduct',
                       'EnzymeProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'pHProduct']} })


class TomographyProduct(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    measure_type: Optional[Productmeasuretype] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'measure_type',
         'domain_of': ['BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    roi_volume_voxel: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'roi_volume_voxel', 'domain_of': ['TomographyProduct']} })
    voxel_size: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'voxel_size', 'domain_of': ['TomographyProduct']} })
    connected_pores: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'connected_pores', 'domain_of': ['TomographyProduct']} })
    pore_diameter_min: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'pore_diameter_min', 'domain_of': ['TomographyProduct']} })
    pore_diameter_max: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'pore_diameter_max', 'domain_of': ['TomographyProduct']} })
    pore_diameter_mean: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'pore_diameter_mean', 'domain_of': ['TomographyProduct']} })
    pore_diameter_median: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'pore_diameter_median', 'domain_of': ['TomographyProduct']} })
    pore_diameter_variance: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'pore_diameter_variance', 'domain_of': ['TomographyProduct']} })
    pore_volume_mean: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'pore_volume_mean', 'domain_of': ['TomographyProduct']} })
    total_pore_volume: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'total_pore_volume', 'domain_of': ['TomographyProduct']} })
    permeability_x: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'permeability_x', 'domain_of': ['TomographyProduct']} })
    flow_rate_x: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flow_rate_x', 'domain_of': ['TomographyProduct']} })
    tortuosity_x: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'tortuosity_x', 'domain_of': ['TomographyProduct']} })
    permeability_y: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'permeability_y', 'domain_of': ['TomographyProduct']} })
    flow_rate_y: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flow_rate_y', 'domain_of': ['TomographyProduct']} })
    tortuosity_y: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'tortuosity_y', 'domain_of': ['TomographyProduct']} })
    permeability_z: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'permeability_z', 'domain_of': ['TomographyProduct']} })
    flow_rate_z: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flow_rate_z', 'domain_of': ['TomographyProduct']} })
    tortuosity_z: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'tortuosity_z', 'domain_of': ['TomographyProduct']} })
    flag_xct: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_xct', 'domain_of': ['TomographyProduct']} })


class WEOMProduct(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    measure_type: Optional[Productmeasuretype] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'measure_type',
         'domain_of': ['BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct']} })
    rep: Optional[Decimal] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'rep',
         'domain_of': ['FTICRProduct',
                       'MAOMProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'WEOMProduct',
                       'replicate']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    total_organic_carbon_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'total_organic_carbon_id',
         'domain_of': ['MAOMProduct', 'WEOMProduct']} })
    total_organic_carbon_avg: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'total_organic_carbon_avg',
         'domain_of': ['MAOMProduct', 'WEOMProduct']} })
    total_nitrogen_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'total_nitrogen_id',
         'domain_of': ['ElementalAnalysisProduct', 'MAOMProduct', 'WEOMProduct']} })
    total_nitrogen_avg: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'total_nitrogen_avg', 'domain_of': ['MAOMProduct', 'WEOMProduct']} })
    flag_toc: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_toc', 'domain_of': ['MAOMProduct', 'WEOMProduct']} })
    flag_tn: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_tn', 'domain_of': ['MAOMProduct', 'WEOMProduct']} })
    flag_toc_avg: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_toc_avg', 'domain_of': ['MAOMProduct', 'WEOMProduct']} })
    flag_tn_avg: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag_tn_avg', 'domain_of': ['MAOMProduct', 'WEOMProduct']} })


class PHProduct(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/enums'})

    measure_type: Optional[Productmeasuretype] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'measure_type',
         'domain_of': ['BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    ph: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'ph', 'domain_of': ['samplingActivity', 'pHProduct']} })
    flag: Optional[Processeddataflag] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'flag',
         'domain_of': ['BulkDensityProduct',
                       'EnzymeProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'pHProduct']} })


class Changelog(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    version: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['softwareControlledTermValue',
                       'changelog',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'sampleProcessing',
                       'processingSampleLink']} })
    changelog: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'changelog', 'domain_of': ['changelog']} })


class Campaign(ConfiguredBaseModel):
    """
    A research campaign that encompasses one or more studies.
    Campaigns are organizational units, typically lasting a single fiscal year beginning in FY26, that group related studies together.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema/campaign'})

    id: UUID = Field(default=..., description="""Unique identifier for the campaign""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    campaign_name: str = Field(default=..., description="""Short name or code for the campaign""", json_schema_extra = { "linkml_meta": {'alias': 'campaign_name', 'domain_of': ['campaign']} })
    campaign_year: Optional[int] = Field(default=None, description="""Primary year associated with the campaign""", json_schema_extra = { "linkml_meta": {'alias': 'campaign_year', 'domain_of': ['campaign']} })
    display_name: Optional[str] = Field(default=None, description="""Human-readable display name for the campaign""", json_schema_extra = { "linkml_meta": {'alias': 'display_name', 'domain_of': ['campaign']} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the campaign objectives and scope""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'quantityValue',
                       'geolocationValue',
                       'latLongValue',
                       'campaign',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'labDevice']} })


class Study(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    campaign_id: Optional[str] = Field(default=None, description="""Reference to the campaign this study belongs to""", json_schema_extra = { "linkml_meta": {'alias': 'campaign_id', 'domain_of': ['study']} })
    participant_name: AnyShapeArray[str] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'participant_name', 'domain_of': ['study']} })
    principal_investigator: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'principal_investigator', 'domain_of': ['study']} })
    collaborating_institution: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'collaborating_institution', 'domain_of': ['study']} })
    project_status: Optional[Projectstatus] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'project_status', 'domain_of': ['study']} })
    project_start: Optional[datetime ] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'project_start', 'domain_of': ['study']} })
    project_end: Optional[datetime ] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'project_end', 'domain_of': ['study']} })
    proposal_title: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'proposal_title', 'domain_of': ['study']} })
    proposal_abstract: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'proposal_abstract', 'domain_of': ['study']} })
    project_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['study']} })


class ZipDownload(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    time: datetime  = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'time', 'domain_of': ['zipDownload']} })
    user: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'user', 'domain_of': ['zipDownload']} })
    files: int = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'files', 'domain_of': ['zipDownload']} })
    packages: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'packages', 'domain_of': ['zipDownload']} })


class SampleBase(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    sample_name: Optional[str] = Field(default=None, description="""The human readable name for the sample""", json_schema_extra = { "linkml_meta": {'alias': 'sample_name',
         'domain_of': ['samplingActivity', 'sampleBase', 'processedData']} })
    proposal_id: Optional[int] = Field(default=None, description="""The 5 digit project ID assigned to an EMSL user proposal/project""", json_schema_extra = { "linkml_meta": {'alias': 'proposal_id', 'domain_of': ['sampleBase', 'processedData']} })
    sampling_set: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sampling_set', 'domain_of': ['sampleBase', 'processedData']} })
    sample_base_type: Samplebasetype = Field(default=..., description="""The name of the sample set if the sample is a part of a set of samples processed together""", json_schema_extra = { "linkml_meta": {'alias': 'sample_base_type', 'domain_of': ['sampleBase']} })


class Sample(ConfiguredBaseModel):
    """
    A physical sample collected from the environment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    sampling_activity_id: str = Field(default=..., description="""Reference to the sampling activity that collected this sample""", json_schema_extra = { "linkml_meta": {'alias': 'sampling_activity_id',
         'domain_of': ['sampling_activity_site_metadata_link', 'sample']} })
    type: Optional[Sampletype] = Field(default=None, description="""The type of sample (soil, aerosol, etc.)""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'geolocationValue',
                       'conditioningValue',
                       'samplingActivity',
                       'sample',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity']} })
    guid_source: Optional[str] = Field(default=None, description="""Indicate the source of the GUID that you have provided for your samples""", json_schema_extra = { "linkml_meta": {'alias': 'guid_source', 'domain_of': ['sample']} })
    other_guid_source: Optional[str] = Field(default=None, description="""Please specify if other GUID source""", json_schema_extra = { "linkml_meta": {'alias': 'other_guid_source', 'domain_of': ['sample']} })


class SoilSample(ConfiguredBaseModel):
    """
    A soil sample with specific soil-related properties
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    soil_type: Soiltype = Field(default=..., description="""The specific type of soil sample""", json_schema_extra = { "linkml_meta": {'alias': 'soil_type', 'domain_of': ['soil', 'soil_sample']} })


class AerosolSample(ConfiguredBaseModel):
    """
    An aerosol sample with specific aerosol-related properties
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    aerosol_type: Aerosoltype = Field(default=..., description="""The type or method of aerosol collection""", json_schema_extra = { "linkml_meta": {'alias': 'aerosol_type', 'domain_of': ['aerosol_sample']} })


class ProcessedSample(ConfiguredBaseModel):
    """
    A sample that has undergone processing or analysis
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    processed_sample_type: Processedsampletype = Field(default=..., description="""The type of processed sample""", json_schema_extra = { "linkml_meta": {'alias': 'processed_sample_type', 'domain_of': ['processedSample']} })


class CoreSection(ConfiguredBaseModel):
    """
    A section of a core sample (TOP, MID, BTM)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    core_section: Coresectionenum = Field(default=..., description="""The section of the core (e.g. TOP, MID, BTM)""", json_schema_extra = { "linkml_meta": {'alias': 'core_section', 'domain_of': ['coreSection', 'processedData']} })


class Replicate(ConfiguredBaseModel):
    """
    A replicate or aliquot of a sample
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    rep: int = Field(default=..., description="""The replicate (or aliquot) number""", json_schema_extra = { "linkml_meta": {'alias': 'rep',
         'domain_of': ['FTICRProduct',
                       'MAOMProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'WEOMProduct',
                       'replicate']} })


class ProcessedData(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    type: Product = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'geolocationValue',
                       'conditioningValue',
                       'samplingActivity',
                       'sample',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity']} })
    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['softwareControlledTermValue',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'instrument',
                       'ontologyClass']} })
    proposal_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'proposal_id', 'domain_of': ['sampleBase', 'processedData']} })
    sampling_set: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sampling_set', 'domain_of': ['sampleBase', 'processedData']} })
    core_section: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'core_section', 'domain_of': ['coreSection', 'processedData']} })
    sample_name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'sample_name',
         'domain_of': ['samplingActivity', 'sampleBase', 'processedData']} })
    s3_base_url: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 's3_base_url', 'domain_of': ['processedData']} })
    s3_bucket: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 's3_bucket', 'domain_of': ['processedData']} })
    s3_key: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 's3_key', 'domain_of': ['processedData']} })
    filesize: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'filesize', 'domain_of': ['processedData']} })
    md5checksum: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'md5checksum', 'domain_of': ['processedData']} })
    workflow_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'workflow_id',
         'domain_of': ['processedData', 'workflowExecutionFunctionalAnnotation']} })
    lims_barcode: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'lims_barcode', 'domain_of': ['samplingActivity', 'processedData']} })
    version: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['softwareControlledTermValue',
                       'changelog',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'sampleProcessing',
                       'processingSampleLink']} })


class AnalysisActivity(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    type: Optional[Routemethod] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'geolocationValue',
                       'conditioningValue',
                       'samplingActivity',
                       'sample',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity']} })
    analyte_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'analyte_id', 'domain_of': ['analysisActivity']} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['softwareControlledTermValue',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'instrument',
                       'ontologyClass']} })
    acquisition_time: datetime  = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'acquisition_time', 'domain_of': ['analysisActivity']} })
    instrument_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'instrument_id',
         'domain_of': ['analysisActivity', 'instrument_alt_id', 'instrumentCustodian']} })
    protocol_url: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'protocol_url', 'domain_of': ['analysisActivity']} })
    instrument_operator_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'instrument_operator_id', 'domain_of': ['analysisActivity']} })
    version: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['softwareControlledTermValue',
                       'changelog',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'sampleProcessing',
                       'processingSampleLink']} })


class InstrumentData(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    analysis_activity_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'analysis_activity_id', 'domain_of': ['instrumentData']} })
    description: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'quantityValue',
                       'geolocationValue',
                       'latLongValue',
                       'campaign',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'labDevice']} })
    alternative_identifiers: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'alternative_identifiers',
         'domain_of': ['instrumentData', 'metaboliteQuantification', 'ontologyClass']} })
    compression_type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'compression_type', 'domain_of': ['instrumentData']} })
    file_size_bytes: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'file_size_bytes', 'domain_of': ['instrumentData']} })
    md5_checksum: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'md5_checksum', 'domain_of': ['instrumentData']} })
    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['softwareControlledTermValue',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'instrument',
                       'ontologyClass']} })
    type: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'geolocationValue',
                       'conditioningValue',
                       'samplingActivity',
                       'sample',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity']} })
    url: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['instrumentData', 'sampleProcessing']} })
    was_generated_by: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'geolocationValue',
                       'instrumentData',
                       'containerType']} })
    file_type: Optional[Filetype] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'file_type', 'domain_of': ['instrumentData']} })
    version: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['softwareControlledTermValue',
                       'changelog',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'sampleProcessing',
                       'processingSampleLink']} })


class WorkflowExecutionActivity(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    raw_data_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'raw_data_id', 'domain_of': ['workflowExecutionActivity']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'quantityValue',
                       'geolocationValue',
                       'latLongValue',
                       'campaign',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'labDevice']} })
    ended_at_time: Optional[datetime ] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'ended_at_time', 'domain_of': ['workflowExecutionActivity']} })
    git_url: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'git_url', 'domain_of': ['workflowExecutionActivity']} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['softwareControlledTermValue',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'instrument',
                       'ontologyClass']} })
    started_at_time: datetime  = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'started_at_time', 'domain_of': ['workflowExecutionActivity']} })
    type: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'geolocationValue',
                       'conditioningValue',
                       'samplingActivity',
                       'sample',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity']} })
    used_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'used_id', 'domain_of': ['workflowExecutionActivity']} })
    execution_resource: Optional[Executionresourcetype] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'execution_resource', 'domain_of': ['workflowExecutionActivity']} })
    workflow_steps: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'workflow_steps', 'domain_of': ['workflowExecutionActivity']} })
    version: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['softwareControlledTermValue',
                       'changelog',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'sampleProcessing',
                       'processingSampleLink']} })


class AlternativeIdentifier(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    alternate_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'alternate_id', 'domain_of': ['alternativeIdentifier']} })
    alternate_identifier_type: Alternateidentifiertype = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'alternate_identifier_type', 'domain_of': ['alternativeIdentifier']} })


class Ecoregion(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    domain_id: int = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'domain_id', 'domain_of': ['ecoregion']} })
    domain_name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'domain_name', 'domain_of': ['ecoregion']} })


class FunctionalAnnotationIdentifier(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    functional_identifier: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'functional_identifier',
         'domain_of': ['functionalAnnotationIdentifier']} })
    database: Annotationdatabasetype = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'database', 'domain_of': ['functionalAnnotationIdentifier']} })


class Instrument(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['softwareControlledTermValue',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'instrument',
                       'ontologyClass']} })
    alternative_names: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'alternative_names', 'domain_of': ['instrument']} })
    vendor: Optional[Vendorenum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'vendor', 'domain_of': ['instrument']} })
    model: Optional[Modelenum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'model', 'domain_of': ['instrument']} })
    instrument_parameters: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'instrument_parameters', 'domain_of': ['instrument']} })


class MetaboliteQuantification(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'quantityValue',
                       'geolocationValue',
                       'latLongValue',
                       'campaign',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'labDevice']} })
    alternative_identifiers: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'alternative_identifiers',
         'domain_of': ['instrumentData', 'metaboliteQuantification', 'ontologyClass']} })
    highest_similarity_score: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'highest_similarity_score', 'domain_of': ['metaboliteQuantification']} })
    metabolite_quantified: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'metabolite_quantified', 'domain_of': ['metaboliteQuantification']} })


class OntologyClass(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'quantityValue',
                       'geolocationValue',
                       'latLongValue',
                       'campaign',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'labDevice']} })
    alternative_identifiers: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'alternative_identifiers',
         'domain_of': ['instrumentData', 'metaboliteQuantification', 'ontologyClass']} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['softwareControlledTermValue',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'instrument',
                       'ontologyClass']} })


class PeptideQuantification(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'quantityValue',
                       'geolocationValue',
                       'latLongValue',
                       'campaign',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'labDevice']} })
    all_proteins: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'all_proteins', 'domain_of': ['peptideQuantification']} })
    best_protein: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'best_protein', 'domain_of': ['peptideQuantification']} })
    min_q_value: Optional[Decimal] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'min_q_value', 'domain_of': ['peptideQuantification']} })
    peptide_sequence: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'peptide_sequence', 'domain_of': ['peptideQuantification']} })
    peptide_spectral_count: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'peptide_spectral_count', 'domain_of': ['peptideQuantification']} })
    peptide_sum_masic_abundance: Optional[Decimal] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'peptide_sum_masic_abundance', 'domain_of': ['peptideQuantification']} })


class ContainerType(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'quantityValue',
                       'geolocationValue',
                       'latLongValue',
                       'campaign',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'labDevice']} })
    was_generated_by: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'geolocationValue',
                       'instrumentData',
                       'containerType']} })
    container_type: Optional[Containertypeenum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'container_type', 'domain_of': ['containerType']} })
    container_size_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'container_size_id', 'domain_of': ['containerType']} })


class Custodian(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    person_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'person_id', 'domain_of': ['custodian']} })


class InstrumentAltId(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    instrument_alt_id_provider: Optional[Instrumentaltidprovider] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'instrument_alt_id_provider', 'domain_of': ['instrument_alt_id']} })
    instrument_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'instrument_id',
         'domain_of': ['analysisActivity', 'instrument_alt_id', 'instrumentCustodian']} })


class LabDevice(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'quantityValue',
                       'geolocationValue',
                       'latLongValue',
                       'campaign',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'labDevice']} })
    device_type: Optional[Devicetypeenum] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'device_type', 'domain_of': ['labDevice']} })
    activity_time_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'activity_time_id', 'domain_of': ['labDevice']} })
    activity_speed_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'activity_speed_id', 'domain_of': ['labDevice']} })


class SampleProcessing(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    analysis_type: Optional[Routemethod] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'analysis_type', 'domain_of': ['sampleProcessing']} })
    method_name: Optional[Methodname] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'method_name', 'domain_of': ['sampleProcessing']} })
    processing_steps: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'processing_steps', 'domain_of': ['sampleProcessing']} })
    url: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['instrumentData', 'sampleProcessing']} })
    version: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['softwareControlledTermValue',
                       'changelog',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'sampleProcessing',
                       'processingSampleLink']} })


class ProcessingSampleLink(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema',
         'unique_keys': {'unique_sample_process_step': {'unique_key_name': 'unique_sample_process_step',
                                                        'unique_key_slots': ['sample_base_id',
                                                                             'processing_id',
                                                                             'step_number',
                                                                             'role']}}})

    id: UUID = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['timestampValue',
                       'textValue',
                       'softwareControlledTermValue',
                       'controlledTermValue',
                       'personValue',
                       'quantityValue',
                       'geolocationValue',
                       'conditioningValue',
                       'latLongValue',
                       'samplingActivity',
                       'soil',
                       'siteMetadata',
                       'BulkDensityMethod',
                       'ElementalAnalysisMethod',
                       'EnzymeActivityMethod',
                       'FTICR_AcquisitionMethod',
                       'GravimetricWaterContentMethod',
                       'HydraulicPropertiesMethod',
                       'KuoMethod',
                       'LCMS_MetabolomicsMethod',
                       'MicrobialBiomassMethod',
                       'PH_Method',
                       'RespirationMethod',
                       'TOC_TN_Method',
                       'TextureMethod',
                       'XrayComputedTomographyMethod',
                       'BulkDensityProduct',
                       'ElementalAnalysisProduct',
                       'EnzymeProduct',
                       'FTICRProduct',
                       'GWCMoistureProduct',
                       'HydraulicPropertiesProduct',
                       'IonsAnalysisProduct',
                       'MAOMProduct',
                       'MetaGenomicsProduct',
                       'MicrobialBiomassProduct',
                       'NitrogenAnalysisProduct',
                       'PhosphorusAnalysisProduct',
                       'RespirationProduct',
                       'TextureProduct',
                       'TomographyProduct',
                       'WEOMProduct',
                       'pHProduct',
                       'campaign',
                       'study',
                       'zipDownload',
                       'sampleBase',
                       'sample',
                       'soil_sample',
                       'aerosol_sample',
                       'processedSample',
                       'coreSection',
                       'replicate',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'alternativeIdentifier',
                       'functionalAnnotationIdentifier',
                       'instrument',
                       'metaboliteQuantification',
                       'ontologyClass',
                       'peptideQuantification',
                       'containerType',
                       'custodian',
                       'instrument_alt_id',
                       'labDevice',
                       'sampleProcessing',
                       'processingSampleLink']} })
    sample_base_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'sample_base_id', 'domain_of': ['processingSampleLink']} })
    processing_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'processing_id', 'domain_of': ['processingSampleLink']} })
    step_number: int = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'step_number', 'domain_of': ['processingSampleLink']} })
    role: Samplerole = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'role', 'domain_of': ['processingSampleLink']} })
    version: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['softwareControlledTermValue',
                       'changelog',
                       'processedData',
                       'analysisActivity',
                       'instrumentData',
                       'workflowExecutionActivity',
                       'sampleProcessing',
                       'processingSampleLink']} })


class InstrumentCustodian(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    instrument_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'instrument_id',
         'domain_of': ['analysisActivity', 'instrument_alt_id', 'instrumentCustodian']} })
    custodian_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'custodian_id', 'domain_of': ['instrumentCustodian']} })


class WorkflowExecutionFunctionalAnnotation(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/MONet/analysis-api-schema'})

    workflow_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'workflow_id',
         'domain_of': ['processedData', 'workflowExecutionFunctionalAnnotation']} })
    functional_annotation_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'functional_annotation_id',
         'domain_of': ['workflowExecutionFunctionalAnnotation']} })
    count: Optional[Decimal] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'count', 'domain_of': ['workflowExecutionFunctionalAnnotation']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
TimestampValue.model_rebuild()
TextValue.model_rebuild()
SoftwareControlledTermValue.model_rebuild()
ControlledTermValue.model_rebuild()
PersonValue.model_rebuild()
QuantityValue.model_rebuild()
GeolocationValue.model_rebuild()
ConditioningValue.model_rebuild()
LatLongValue.model_rebuild()
SamplingActivity.model_rebuild()
Soil.model_rebuild()
SiteMetadata.model_rebuild()
SamplingActivitySiteMetadataLink.model_rebuild()
BulkDensityMethod.model_rebuild()
ElementalAnalysisMethod.model_rebuild()
EnzymeActivityMethod.model_rebuild()
FTICRAcquisitionMethod.model_rebuild()
GravimetricWaterContentMethod.model_rebuild()
HydraulicPropertiesMethod.model_rebuild()
KuoMethod.model_rebuild()
LCMSMetabolomicsMethod.model_rebuild()
MicrobialBiomassMethod.model_rebuild()
PHMethod.model_rebuild()
RespirationMethod.model_rebuild()
TOCTNMethod.model_rebuild()
TextureMethod.model_rebuild()
XrayComputedTomographyMethod.model_rebuild()
BulkDensityProduct.model_rebuild()
ElementalAnalysisProduct.model_rebuild()
EnzymeProduct.model_rebuild()
FTICRProduct.model_rebuild()
GWCMoistureProduct.model_rebuild()
HydraulicPropertiesProduct.model_rebuild()
IonsAnalysisProduct.model_rebuild()
MAOMProduct.model_rebuild()
MetaGenomicsProduct.model_rebuild()
MicrobialBiomassProduct.model_rebuild()
NitrogenAnalysisProduct.model_rebuild()
PhosphorusAnalysisProduct.model_rebuild()
RespirationProduct.model_rebuild()
TextureProduct.model_rebuild()
TomographyProduct.model_rebuild()
WEOMProduct.model_rebuild()
PHProduct.model_rebuild()
Changelog.model_rebuild()
Campaign.model_rebuild()
Study.model_rebuild()
ZipDownload.model_rebuild()
SampleBase.model_rebuild()
Sample.model_rebuild()
SoilSample.model_rebuild()
AerosolSample.model_rebuild()
ProcessedSample.model_rebuild()
CoreSection.model_rebuild()
Replicate.model_rebuild()
ProcessedData.model_rebuild()
AnalysisActivity.model_rebuild()
InstrumentData.model_rebuild()
WorkflowExecutionActivity.model_rebuild()
AlternativeIdentifier.model_rebuild()
Ecoregion.model_rebuild()
FunctionalAnnotationIdentifier.model_rebuild()
Instrument.model_rebuild()
MetaboliteQuantification.model_rebuild()
OntologyClass.model_rebuild()
PeptideQuantification.model_rebuild()
ContainerType.model_rebuild()
Custodian.model_rebuild()
InstrumentAltId.model_rebuild()
LabDevice.model_rebuild()
SampleProcessing.model_rebuild()
ProcessingSampleLink.model_rebuild()
InstrumentCustodian.model_rebuild()
WorkflowExecutionFunctionalAnnotation.model_rebuild()

