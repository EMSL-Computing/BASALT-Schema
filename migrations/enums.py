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
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


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


linkml_meta = LinkMLMeta({'default_prefix': 'analysis_api_schema',
     'description': 'Enumerated values used throughout the MONet Analysis API '
                    'schema',
     'id': 'https://w3id.org/MONet/analysis-api-schema/enums',
     'imports': ['linkml:types'],
     'license': 'MIT',
     'name': 'analysis-api-schema-enums',
     'prefixes': {'analysis_api_schema': {'prefix_prefix': 'analysis_api_schema',
                                          'prefix_reference': 'https://w3id.org/MONet/analysis-api-schema/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'source_file': '../src/analysis_api_schema/schema/enums.yaml',
     'title': 'MONet Analysis API - Enumerations'} )

class Projectstatus(str, Enum):
    STARTED = "STARTED"
    COMPLETED = "COMPLETED"
    CLOSED = "CLOSED"
    EXTENDED = "EXTENDED"
    ACCEPTED = "ACCEPTED"
    WITHDRAWN = "WITHDRAWN"


class Samplebasetype(str, Enum):
    """
    Base types for sample entities
    """
    sample = "sample"
    """
    A physical sample
    """
    processed_sample = "processed_sample"
    """
    A sample that has undergone processing
    """


class Sampletype(str, Enum):
    """
    Types of samples that can be collected
    """
    soil = "soil"
    """
    Soil sample
    """
    aerosol = "aerosol"
    """
    Aerosol sample
    """


class Soiltype(str, Enum):
    """
    Specific types of soil samples
    """
    soil_core = "soil_core"
    """
    Soil core sample
    """
    surface_layer = "surface_layer"
    """
    Surface layer soil sample
    """


class Aerosoltype(str, Enum):
    """
    Types of aerosol samples
    """
    sea_salt = "sea_salt"
    """
    Sea salt aerosol
    """
    dust = "dust"
    """
    Dust aerosol
    """
    volcanic_ash = "volcanic_ash"
    """
    Volcanic ash aerosol
    """


class Processedsampletype(str, Enum):
    """
    Types of processed samples
    """
    analyte = "analyte"
    """
    Analyte sample
    """
    coreSection = "coreSection"
    """
    Core section sample
    """
    replicate = "replicate"
    """
    Replicate sample
    """


class Coresectionenum(str, Enum):
    """
    Sections of a core sample
    """
    TOP = "TOP"
    """
    Top section of core
    """
    BTM = "BTM"
    """
    Bottom section of core
    """
    MID = "MID"
    """
    Middle section of core
    """


class Samplingactivitytype(str, Enum):
    """
    Types of sampling activities
    """
    soil = "soil"
    """
    Soil sampling activity
    """
    water = "water"
    """
    Water sampling activity
    """
    air = "air"
    """
    Air sampling activity
    """
    plant = "plant"
    """
    Plant sampling activity
    """
    none = "none"
    """
    No specific activity type
    """


class Neondomainenum(str, Enum):
    """
    NEON ecological domains
    """
    northeast = "northeast"
    """
    Northeast domain
    """
    mid_atlantic = "mid_atlantic"
    """
    Mid-Atlantic domain
    """
    southeast = "southeast"
    """
    Southeast domain
    """
    atlantic_neotropical = "atlantic_neotropical"
    """
    Atlantic Neotropical domain
    """
    great_lakes = "great_lakes"
    """
    Great Lakes domain
    """
    prairie_peninsula = "prairie_peninsula"
    """
    Prairie Peninsula domain
    """
    appalachians_and_cumberland_plateau = "appalachians_and_cumberland_plateau"
    """
    Appalachians and Cumberland Plateau domain
    """
    ozarks_complex = "ozarks_complex"
    """
    Ozarks Complex domain
    """
    northern_plains = "northern_plains"
    """
    Northern Plains domain
    """
    central_plains = "central_plains"
    """
    Central Plains domain
    """
    southern_plains = "southern_plains"
    """
    Southern Plains domain
    """
    desert_southwest = "desert_southwest"
    """
    Desert Southwest domain
    """
    northern_rockies = "northern_rockies"
    """
    Northern Rockies domain
    """
    southern_rockies_and_colorado_plateau = "southern_rockies_and_colorado_plateau"
    """
    Southern Rockies and Colorado Plateau domain
    """
    great_basin = "great_basin"
    """
    Great Basin domain
    """
    sierra_nevada = "sierra_nevada"
    """
    Sierra Nevada domain
    """
    pacific_northwest = "pacific_northwest"
    """
    Pacific Northwest domain
    """
    pacific_southwest = "pacific_southwest"
    """
    Pacific Southwest domain
    """
    tundra = "tundra"
    """
    Tundra domain
    """
    taiga = "taiga"
    """
    Taiga domain
    """
    pacific_tropical = "pacific_tropical"
    """
    Pacific Tropical domain
    """


class Growthfacilityenum(str, Enum):
    """
    Types of growth facilities
    """
    field = "field"
    """
    Field conditions
    """
    commercially_purchased = "commercially_purchased"
    """
    Commercially purchased
    """
    experimental_garden = "experimental_garden"
    """
    Experimental garden
    """
    field_incubation = "field_incubation"
    """
    Field incubation
    """
    greenhouse = "greenhouse"
    """
    Greenhouse
    """
    growth_chamber = "growth_chamber"
    """
    Growth chamber
    """
    lab_incubation = "lab_incubation"
    """
    Laboratory incubation
    """
    open_top_chamber = "open_top_chamber"
    """
    Open top chamber
    """
    other = "other"
    """
    Other growth facility type
    """


class Landuseenum(str, Enum):
    """
    Land use classifications
    """
    badlands = "badlands"
    """
    Badlands
    """
    cities = "cities"
    """
    Urban/city areas
    """
    conifers = "conifers"
    """
    Coniferous forests (e.g. pine, spruce, fir, cypress)
    """
    crop_trees = "crop_trees"
    """
    Crop trees (nuts, fruit, christmas trees, nursery trees)
    """
    farmstead = "farmstead"
    """
    Farmstead
    """
    gravel = "gravel"
    """
    Gravel areas
    """
    hardwoods = "hardwoods"
    """
    Hardwood forests (e.g. oak, hickory, elm, aspen)
    """
    hayland = "hayland"
    """
    Hayland
    """
    horticultural_plants = "horticultural_plants"
    """
    Horticultural plants (e.g. tulips)
    """
    industrial_areas = "industrial_areas"
    """
    Industrial areas
    """
    intermixed = "intermixed"
    """
    Intermixed hardwood and conifers
    """
    marshlands = "marshlands"
    """
    Marshlands (grass, sedges, rushes)
    """
    meadows = "meadows"
    """
    Meadows (grasses, alfalfa, fescue, bromegrass, timothy)
    """
    mines_quarries = "mines_quarries"
    """
    Mines and quarries
    """
    mudflats = "mudflats"
    """
    Mudflats
    """
    oil_waste = "oil_waste"
    """
    Oil waste areas
    """
    pastureland = "pastureland"
    """
    Pastureland (grasslands used for livestock grazing)
    """
    permanent_snow_or_ice = "permanent_snow_or_ice"
    """
    Permanent snow or ice
    """
    rainforest = "rainforest"
    """
    Rainforest (evergreen forest receiving >406 cm annual rainfall)
    """
    rangeland = "rangeland"
    """
    Rangeland
    """
    roads_railroads = "roads_railroads"
    """
    Roads and railroads
    """
    rock = "rock"
    """
    Rock surfaces
    """
    row_crops = "row_crops"
    """
    Row crops
    """
    saline_seeps = "saline_seeps"
    """
    Saline seeps
    """
    salt_flats = "salt_flats"
    """
    Salt flats
    """
    sand = "sand"
    """
    Sand areas
    """
    shrub_crops = "shrub_crops"
    """
    Shrub crops (blueberries, nursery ornamentals, filberts)
    """
    shrub_land = "shrub_land"
    """
    Shrub land (e.g. mesquite, sage-brush, creosote bush, shrub oak, eucalyptus)
    """
    small_grains = "small_grains"
    """
    Small grains
    """
    successional_shrub_land = "successional_shrub_land"
    """
    Successional shrub land (tree saplings, hazels, sumacs, chokecherry, shrub dogwoods, blackberries)
    """
    swamp = "swamp"
    """
    Swamp (permanent or semi-permanent water body dominated by woody plants)
    """
    tropical = "tropical"
    """
    Tropical vegetation (e.g. mangrove, palms)
    """
    tundra = "tundra"
    """
    Tundra (mosses, lichens)
    """
    vegetable_crops = "vegetable_crops"
    """
    Vegetable crops
    """
    vine_crops = "vine_crops"
    """
    Vine crops (grapes)
    """


class Tillageenum(str, Enum):
    """
    Tillage methods
    """
    Chisel = "Chisel"
    """
    Chisel tillage
    """
    Cutting_Disc = "Cutting_Disc"
    """
    Cutting disc tillage
    """
    Disc_Plough = "Disc_Plough"
    """
    Disc plough tillage
    """
    Drill = "Drill"
    """
    Drill tillage
    """
    Mouldboard = "Mouldboard"
    """
    Mouldboard tillage
    """
    Ridge_Till = "Ridge_Till"
    """
    Ridge till
    """
    Streip_Tillage = "Streip_Tillage"
    """
    Strip tillage
    """
    Tined = "Tined"
    """
    Tined tillage
    """
    Zonal_Tillage = "Zonal_Tillage"
    """
    Zonal tillage
    """


class Profilepositionenum(str, Enum):
    """
    Soil profile positions
    """
    backslope = "backslope"
    """
    Backslope position
    """
    footslope = "footslope"
    """
    Footslope position
    """
    shoulder = "shoulder"
    """
    Shoulder position
    """
    summit = "summit"
    """
    Summit position
    """
    toeslope = "toeslope"
    """
    Toeslope position
    """


class Winddirectionenum(str, Enum):
    """
    Wind direction classifications
    """
    north = "north"
    """
    North wind direction
    """
    north_east = "north_east"
    """
    Northeast wind direction
    """
    east = "east"
    """
    East wind direction
    """
    south_east = "south_east"
    """
    Southeast wind direction
    """
    south = "south"
    """
    South wind direction
    """
    south_west = "south_west"
    """
    Southwest wind direction
    """
    west = "west"
    """
    West wind direction
    """
    north_west = "north_west"
    """
    Northwest wind direction
    """


class Drainageclassenum(str, Enum):
    """
    Soil drainage classifications
    """
    Excessively_Drained = "Excessively_Drained"
    """
    Excessively drained soil
    """
    Moderately_Well = "Moderately_Well"
    """
    Moderately well drained soil
    """
    Poorly = "Poorly"
    """
    Poorly drained soil
    """
    Somewhat_Poorly = "Somewhat_Poorly"
    """
    Somewhat poorly drained soil
    """
    Very_Poorly = "Very_Poorly"
    """
    Very poorly drained soil
    """
    Well = "Well"
    """
    Well drained soil
    """


class Soilhorizonenum(str, Enum):
    """
    Soil horizon classifications
    """
    a_horizon = "a_horizon"
    """
    A Horizon - topsoil
    """
    b_horizon = "b_horizon"
    """
    B Horizon - subsoil
    """
    c_horizon = "c_horizon"
    """
    C Horizon - parent material
    """
    e_horizon = "e_horizon"
    """
    E Horizon - eluviated layer
    """
    o_horizon = "o_horizon"
    """
    O Horizon - organic layer
    """
    permafrost = "permafrost"
    """
    Permafrost layer
    """
    r_layer = "r_layer"
    """
    R Layer - bedrock
    """


class Faoclassenum(str, Enum):
    """
    FAO soil classification system
    """
    Acrisols = "Acrisols"
    """
    Acrisols
    """
    Alisols = "Alisols"
    """
    Alisols
    """
    Andosols = "Andosols"
    """
    Andosols
    """
    Anthrosols = "Anthrosols"
    """
    Anthrosols
    """
    Arenosols = "Arenosols"
    """
    Arenosols
    """
    Calcisols = "Calcisols"
    """
    Calcisols
    """
    Cambisols = "Cambisols"
    """
    Cambisols
    """
    Chernozems = "Chernozems"
    """
    Chernozems
    """
    Cryosols = "Cryosols"
    """
    Cryosols
    """
    Durisols = "Durisols"
    """
    Durisols
    """
    Ferrasols = "Ferrasols"
    """
    Ferralsols
    """
    Fluvisols = "Fluvisols"
    """
    Fluvisols
    """
    Gleysols = "Gleysols"
    """
    Gleysols
    """
    Gypsisols = "Gypsisols"
    """
    Gypsisols
    """
    Histosols = "Histosols"
    """
    Histosols
    """
    Kastanozems = "Kastanozems"
    """
    Kastanozems
    """
    Leptosols = "Leptosols"
    """
    Leptosols
    """
    Lixisols = "Lixisols"
    """
    Lixisols
    """
    Luvisols = "Luvisols"
    """
    Luvisols
    """
    Nitosols = "Nitosols"
    """
    Nitisols
    """
    Phaeozems = "Phaeozems"
    """
    Phaeozems
    """
    Planosols = "Planosols"
    """
    Planosols
    """
    Plinthosols = "Plinthosols"
    """
    Plinthosols
    """
    Podzols = "Podzols"
    """
    Podzols
    """
    Solonchaks = "Solonchaks"
    """
    Solonchaks
    """
    Solonetz = "Solonetz"
    """
    Solonetz
    """
    Stagnosols = "Stagnosols"
    """
    Stagnosols
    """
    Technosols = "Technosols"
    """
    Technosols
    """
    Umbrisols = "Umbrisols"
    """
    Umbrisols
    """
    Vertisols = "Vertisols"
    """
    Vertisols
    """


class Sedimenttypeenum(str, Enum):
    """
    Types of sediment
    """
    biogenous = "biogenous"
    """
    Biogenous sediment
    """
    cosmogenous = "cosmogenous"
    """
    Cosmogenous sediment
    """
    hydrogenous = "hydrogenous"
    """
    Hydrogenous sediment
    """
    lithogenous = "lithogenous"
    """
    Lithogenous sediment
    """


class Samplestoretemp(str, Enum):
    """
    Sample storage temperature conditions
    """
    fresh4 = "fresh4"
    """
    Fresh storage at 4░C
    """
    freshroom = "freshroom"
    """
    Fresh storage at room temperature
    """
    frozen20 = "frozen20"
    """
    Frozen storage at -20░C
    """
    frozen80 = "frozen80"
    """
    Frozen storage at -80░C
    """
    other = "other"
    """
    Other storage temperature
    """


class Storagecondtenum(str, Enum):
    """
    Sample storage conditions
    """
    fresh = "fresh"
    """
    Fresh sample
    """
    frozen = "frozen"
    """
    Frozen sample
    """
    lyophilized = "lyophilized"
    """
    Lyophilized (freeze-dried) sample
    """
    other = "other"
    """
    Other storage condition
    """


class Oxygenstatusenum(str, Enum):
    """
    Oxygen status of samples
    """
    aerobic = "aerobic"
    """
    Aerobic conditions
    """
    anaerobic = "anaerobic"
    """
    Anaerobic conditions
    """
    anoxic = "anoxic"
    """
    Anoxic conditions
    """
    facultative = "facultative"
    """
    Facultative conditions
    """
    microaerophilic = "microaerophilic"
    """
    Microaerophilic conditions
    """
    microanaerobe = "microanaerobe"
    """
    Microanaerobe conditions
    """
    oblifate_aerobe = "oblifate_aerobe"
    """
    Obligate aerobe conditions
    """
    obligate_anaerobe = "obligate_anaerobe"
    """
    Obligate anaerobe conditions
    """


class Sampbioticenum(str, Enum):
    """
    Sample biotic relationships
    """
    free_living = "free_living"
    """
    Free-living organism
    """
    parasite = "parasite"
    """
    Parasitic organism
    """
    commensal = "commensal"
    """
    Commensal organism
    """
    symbiont = "symbiont"
    """
    Symbiotic organism
    """


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



# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model

