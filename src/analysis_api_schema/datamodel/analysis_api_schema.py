# Auto generated from analysis_api_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-07-28T15:41:41
# Schema: analysis-api-schema
#
# id: https://w3id.org/MONet/analysis-api-schema
# description: LinkML-based schema for MONet soil analysis data management and metadata enrichment.
#   This schema defines the data models for samples, processed samples, site metadata,
#   and enrichment providers used in the MONet Analysis API.
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Date, Datetime, Double, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Namespaces
BTO = CurieNamespace('BTO', 'http://purl.obolibrary.org/obo/BTO_')
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
EC = CurieNamespace('EC', 'https://enzyme.expasy.org/EC/')
MIXS = CurieNamespace('MIXS', 'https://w3id.org/mixs/')
MS = CurieNamespace('MS', 'http://purl.obolibrary.org/obo/MS_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PO = CurieNamespace('PO', 'http://purl.obolibrary.org/obo/PO_')
ANALYSIS_API_SCHEMA = CurieNamespace('analysis_api_schema', 'https://w3id.org/MONet/analysis-api-schema/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
ROR = CurieNamespace('ror', 'https://ror.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ANALYSIS_API_SCHEMA


# Types
class Uuid(String):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "uuid"
    type_model_uri = ANALYSIS_API_SCHEMA.Uuid


class TimestampTz(Datetime):
    type_class_uri = XSD["dateTime"]
    type_class_curie = "xsd:dateTime"
    type_name = "timestamp_tz"
    type_model_uri = ANALYSIS_API_SCHEMA.TimestampTz


# Class references
class ActivityId(Uuid):
    pass


class EntityId(Uuid):
    pass


class DataProductId(Uuid):
    pass


class ProcessedDataId(DataProductId):
    pass


class InstrumentDataId(DataProductId):
    pass


class SitePhotoId(DataProductId):
    pass


class DataGenerationActivityId(Uuid):
    pass


class RespirationDataGenerationActivityId(DataGenerationActivityId):
    pass


class DataProcessingActivityId(Uuid):
    pass


class AlternativeIdentifierId(Uuid):
    pass


class FunctionalAnnotationIdentifierId(Uuid):
    pass


class InstrumentId(Uuid):
    pass


class OntologyClassId(Uuid):
    pass


class ContainerTypeId(Uuid):
    pass


class CustodianId(Uuid):
    pass


class InstrumentAlternativeIdentifierId(Uuid):
    pass


class LabDeviceId(Uuid):
    pass


class SampleProcessingId(Uuid):
    pass


class ProcessingSampleLinkId(Uuid):
    pass


class XRayDataGenerationActivityId(DataGenerationActivityId):
    pass


class XRFDataGenerationActivityId(XRayDataGenerationActivityId):
    pass


class XRDDataGenerationActivityId(XRayDataGenerationActivityId):
    pass


class ChangelogVersion(extended_str):
    pass


class MassSpectrometryInstrumentDataId(InstrumentDataId):
    pass


class MassSpectrometryDataProductId(ProcessedDataId):
    pass


class MSImageProductId(MassSpectrometryDataProductId):
    pass


class MolecularIdentificationProductId(MassSpectrometryDataProductId):
    pass


class MetaproteomicsProductId(MassSpectrometryDataProductId):
    pass


class MassSpectrometryDataGenerationActivityId(DataGenerationActivityId):
    pass


class MobilePhaseSegmentId(Uuid):
    pass


class MassSpectrometryDataProcessingActivityId(DataProcessingActivityId):
    pass


class MassSpectrometryStandardRunId(Uuid):
    pass


class PurchasedMaterialId(Uuid):
    pass


class LabProcessingActivityId(Uuid):
    pass


class MediaPreparationId(SampleProcessingId):
    pass


class CultureGrowthId(SampleProcessingId):
    pass


class StrainPurityId(CultureGrowthId):
    pass


class StockCulturePreparationId(CultureGrowthId):
    pass


class PreCultureGrowthId(CultureGrowthId):
    pass


class ExperimentalCultureId(CultureGrowthId):
    pass


class PlateSetupActivityId(SampleProcessingId):
    pass


class AMP2PlateSetupActivityId(PlateSetupActivityId):
    pass


class EcoplatePlateSetupActivityId(PlateSetupActivityId):
    pass


class PlateDataGenerationActivityId(DataGenerationActivityId):
    pass


class AMP2DataGenerationActivityId(PlateDataGenerationActivityId):
    pass


class EcoplateDataGenerationActivityId(PlateDataGenerationActivityId):
    pass


class NucleotideSequencingId(DataGenerationActivityId):
    pass


class NucleotideSequencingInstrumentDataId(InstrumentDataId):
    pass


class MetagenomicsProductId(ProcessedDataId):
    pass


class MetagenomicsAnnotationProductId(MetagenomicsProductId):
    pass


class MetagenomicsBinningProductId(MetagenomicsProductId):
    pass


class MetagenomicsGenePhylogenyProductId(MetagenomicsProductId):
    pass


class MetagenomicsDataProcessingActivityId(DataProcessingActivityId):
    pass


class BulkDensityProductId(ProcessedDataId):
    pass


class ElementalAnalysisProductId(ProcessedDataId):
    pass


class EnzymeProductId(ProcessedDataId):
    pass


class GWCMoistureProductId(ProcessedDataId):
    pass


class HydraulicPropertiesProductId(ProcessedDataId):
    pass


class IonsAnalysisProductId(ProcessedDataId):
    pass


class MAOMProductId(ProcessedDataId):
    pass


class MicrobialBiomassProductId(ProcessedDataId):
    pass


class NitrogenAnalysisProductId(ProcessedDataId):
    pass


class PhosphorusAnalysisProductId(ProcessedDataId):
    pass


class RespirationProductId(ProcessedDataId):
    pass


class TextureProductId(ProcessedDataId):
    pass


class TomographyProductId(ProcessedDataId):
    pass


class WEOMProductId(ProcessedDataId):
    pass


class PHProductId(ProcessedDataId):
    pass


class XRayDataProductId(ProcessedDataId):
    pass


class XRFElementalProductId(XRayDataProductId):
    pass


class XRDPhaseProductId(XRayDataProductId):
    pass


class SiteId(Uuid):
    pass


class SampleId(Uuid):
    pass


class AerosolArmSampleId(SampleId):
    pass


class AerosolSampleId(SampleId):
    pass


class AMP2UserSampleId(SampleId):
    pass


class CommerciallyPurchasedSampleId(SampleId):
    pass


class CultureEnvironmentalSampleId(SampleId):
    pass


class EngineeredStrainSampleId(SampleId):
    pass


class FieldDeployedTerraformSampleId(SampleId):
    pass


class MixedCultureSampleId(SampleId):
    pass


class MonetSoilSampleId(SampleId):
    pass


class OtherUndescribedSampleId(SampleId):
    pass


class PlantSampleId(SampleId):
    pass


class PureCultureSampleId(SampleId):
    pass


class SedimentSampleId(SampleId):
    pass


class SoilSampleId(SampleId):
    pass


class SynthesizedMaterialSampleId(SampleId):
    pass


class TerraformSampleId(SampleId):
    pass


class WaterSampleId(SampleId):
    pass


class ProcessedSampleId(SampleId):
    pass


class CoreSectionId(ProcessedSampleId):
    pass


class SamplingActivityId(Uuid):
    pass


class AerosolArmSamplingActivityId(SamplingActivityId):
    pass


class AerosolSamplingActivityId(SamplingActivityId):
    pass


class CommerciallyPurchasedSamplingActivityId(SamplingActivityId):
    pass


class CultureEnvironmentalSamplingActivityId(SamplingActivityId):
    pass


class EngineeredStrainSamplingActivityId(SamplingActivityId):
    pass


class FieldDeployedTerraformSamplingActivityId(SamplingActivityId):
    pass


class MixedCultureSamplingActivityId(SamplingActivityId):
    pass


class MonetSoilSamplingActivityId(SamplingActivityId):
    pass


class OtherUndescribedSamplingActivityId(SamplingActivityId):
    pass


class PlantSamplingActivityId(SamplingActivityId):
    pass


class PureCultureSamplingActivityId(SamplingActivityId):
    pass


class SedimentSamplingActivityId(SamplingActivityId):
    pass


class SoilSamplingActivityId(SamplingActivityId):
    pass


class SynthesizedMaterialSamplingActivityId(SamplingActivityId):
    pass


class TerraformSamplingActivityId(SamplingActivityId):
    pass


class WaterSamplingActivityId(SamplingActivityId):
    pass


class BiologicalEntityId(Uuid):
    pass


class StudyId(Uuid):
    pass


class ProjectParticipantId(Uuid):
    pass


class TimestampValueId(extended_str):
    pass


class TextValueId(extended_str):
    pass


class SoftwareControlledTermValueId(extended_str):
    pass


class ControlledTermValueId(extended_str):
    pass


class PersonValueId(Uuid):
    pass


class QuantityValueId(Uuid):
    pass


class ConditioningValueId(extended_str):
    pass


class ZipDownloadId(Uuid):
    pass


@dataclass(repr=False)
class Activity(YAMLRoot):
    """
    Something that happens over time and can use equipment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["Activity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:Activity"
    class_name: ClassVar[str] = "Activity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.Activity

    id: Union[str, ActivityId] = None
    name: str = None
    description: Optional[str] = None
    ended_at_time: Optional[Union[str, XSDDateTime]] = None
    processing_institution: Optional[Union[str, "InstitutionEnum"]] = None
    protocol_link: Optional[str] = None
    started_at_time: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivityId):
            self.id = ActivityId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.ended_at_time is not None and not isinstance(self.ended_at_time, XSDDateTime):
            self.ended_at_time = XSDDateTime(self.ended_at_time)

        if self.processing_institution is not None and not isinstance(self.processing_institution, InstitutionEnum):
            self.processing_institution = InstitutionEnum(self.processing_institution)

        if self.protocol_link is not None and not isinstance(self.protocol_link, str):
            self.protocol_link = str(self.protocol_link)

        if self.started_at_time is not None and not isinstance(self.started_at_time, XSDDateTime):
            self.started_at_time = XSDDateTime(self.started_at_time)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Entity(YAMLRoot):
    """
    Base identifiable thing.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["Entity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.Entity

    id: Union[str, EntityId] = None
    name: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataProduct(YAMLRoot):
    """
    Abstract base class for raw or processed data accessible in S3 storage.
    Carries S3-pointer and sample-linkage slots shared across product types.
    processedData and future sitePhoto extend this via is_a.
    No direct database table, subclasses map to tables.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["DataProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:DataProduct"
    class_name: ClassVar[str] = "DataProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.DataProduct

    id: Union[str, DataProductId] = None
    name: str = None
    s3_key: str = None
    description: Optional[str] = None
    project: Optional[int] = None
    sampling_set: Optional[int] = None
    core_section: Optional[Union[str, "CoreSectionEnum"]] = None
    sample_name: Optional[str] = None
    s3_base_url: Optional[str] = None
    s3_bucket: Optional[str] = None
    filesize: Optional[int] = None
    md5checksum: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.s3_key):
            self.MissingRequiredField("s3_key")
        if not isinstance(self.s3_key, str):
            self.s3_key = str(self.s3_key)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataProductId):
            self.id = DataProductId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.project is not None and not isinstance(self.project, int):
            self.project = int(self.project)

        if self.sampling_set is not None and not isinstance(self.sampling_set, int):
            self.sampling_set = int(self.sampling_set)

        if self.core_section is not None and not isinstance(self.core_section, CoreSectionEnum):
            self.core_section = CoreSectionEnum(self.core_section)

        if self.sample_name is not None and not isinstance(self.sample_name, str):
            self.sample_name = str(self.sample_name)

        if self.s3_base_url is not None and not isinstance(self.s3_base_url, str):
            self.s3_base_url = str(self.s3_base_url)

        if self.s3_bucket is not None and not isinstance(self.s3_bucket, str):
            self.s3_bucket = str(self.s3_bucket)

        if self.filesize is not None and not isinstance(self.filesize, int):
            self.filesize = int(self.filesize)

        if self.md5checksum is not None and not isinstance(self.md5checksum, str):
            self.md5checksum = str(self.md5checksum)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProcessedData(DataProduct):
    """
    A data product generated by a workflow execution.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["ProcessedData"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:ProcessedData"
    class_name: ClassVar[str] = "ProcessedData"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.ProcessedData

    id: Union[str, ProcessedDataId] = None
    name: str = None
    s3_key: str = None
    summary_metrics: Optional[str] = None
    lims_barcode: Optional[str] = None
    sample_id: Optional[Union[str, SampleId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.summary_metrics is not None and not isinstance(self.summary_metrics, str):
            self.summary_metrics = str(self.summary_metrics)

        if self.lims_barcode is not None and not isinstance(self.lims_barcode, str):
            self.lims_barcode = str(self.lims_barcode)

        if self.sample_id is not None and not isinstance(self.sample_id, SampleId):
            self.sample_id = SampleId(self.sample_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InstrumentData(DataProduct):
    """
    An abstract parent class for raw data files generated by different kinds of instruments. All subclasses must have
    a slot pointing upstream that specifies the analysisActivity subclass which created them.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["InstrumentData"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:InstrumentData"
    class_name: ClassVar[str] = "InstrumentData"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.InstrumentData

    id: Union[str, InstrumentDataId] = None
    name: str = None
    s3_key: str = None
    description: str = None
    file_curie: Optional[str] = None
    alternative_identifiers: Optional[str] = None
    compression_type: Optional[str] = None
    file_type: Optional[Union[str, "FileTypeEnum"]] = None
    software_version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.file_curie is not None and not isinstance(self.file_curie, str):
            self.file_curie = str(self.file_curie)

        if self.alternative_identifiers is not None and not isinstance(self.alternative_identifiers, str):
            self.alternative_identifiers = str(self.alternative_identifiers)

        if self.compression_type is not None and not isinstance(self.compression_type, str):
            self.compression_type = str(self.compression_type)

        if self.file_type is not None and not isinstance(self.file_type, FileTypeEnum):
            self.file_type = FileTypeEnum(self.file_type)

        if self.software_version is not None and not isinstance(self.software_version, str):
            self.software_version = str(self.software_version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SitePhoto(DataProduct):
    """
    A data product representing a photo of a site, typically taken during sampling.
    One row per photo with metadata about the photo type and when it was taken.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["SitePhoto"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:SitePhoto"
    class_name: ClassVar[str] = "SitePhoto"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.SitePhoto

    id: Union[str, SitePhotoId] = None
    name: str = None
    s3_key: str = None
    site_photo_type: Optional[Union[str, "SitePhotoCategoryEnum"]] = None
    photo_taken_during: Optional[Union[str, SamplingActivityId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SitePhotoId):
            self.id = SitePhotoId(self.id)

        if self.site_photo_type is not None and not isinstance(self.site_photo_type, SitePhotoCategoryEnum):
            self.site_photo_type = SitePhotoCategoryEnum(self.site_photo_type)

        if self.photo_taken_during is not None and not isinstance(self.photo_taken_during, SamplingActivityId):
            self.photo_taken_during = SamplingActivityId(self.photo_taken_during)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataGenerationActivity(YAMLRoot):
    """
    Abstract base for any data generation activity (physical to digital). Input data should
    be specified on workflow subclasses.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["DataGenerationActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:DataGenerationActivity"
    class_name: ClassVar[str] = "DataGenerationActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.DataGenerationActivity

    id: Union[str, DataGenerationActivityId] = None
    name: str = None
    acquisition_start_time: Union[str, XSDDateTime] = None
    acquisition_end_time: Union[str, XSDDateTime] = None
    sequence_order: Optional[int] = None
    description: Optional[str] = None
    protocol_url: Optional[str] = None
    protocol_version: Optional[str] = None
    analyte_id: Optional[Union[str, ProcessedSampleId]] = None
    instrument_used: Optional[Union[str, InstrumentId]] = None
    instrument_operator_id: Optional[Union[str, PersonValueId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataGenerationActivityId):
            self.id = DataGenerationActivityId(self.id)

        if self._is_empty(self.acquisition_start_time):
            self.MissingRequiredField("acquisition_start_time")
        if not isinstance(self.acquisition_start_time, XSDDateTime):
            self.acquisition_start_time = XSDDateTime(self.acquisition_start_time)

        if self._is_empty(self.acquisition_end_time):
            self.MissingRequiredField("acquisition_end_time")
        if not isinstance(self.acquisition_end_time, XSDDateTime):
            self.acquisition_end_time = XSDDateTime(self.acquisition_end_time)

        if self.sequence_order is not None and not isinstance(self.sequence_order, int):
            self.sequence_order = int(self.sequence_order)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.protocol_url is not None and not isinstance(self.protocol_url, str):
            self.protocol_url = str(self.protocol_url)

        if self.protocol_version is not None and not isinstance(self.protocol_version, str):
            self.protocol_version = str(self.protocol_version)

        if self.analyte_id is not None and not isinstance(self.analyte_id, ProcessedSampleId):
            self.analyte_id = ProcessedSampleId(self.analyte_id)

        if self.instrument_used is not None and not isinstance(self.instrument_used, InstrumentId):
            self.instrument_used = InstrumentId(self.instrument_used)

        if self.instrument_operator_id is not None and not isinstance(self.instrument_operator_id, PersonValueId):
            self.instrument_operator_id = PersonValueId(self.instrument_operator_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RespirationDataGenerationActivity(DataGenerationActivity):
    """
    Data generation activity for soil respiration analysis.
    Captures CO2-C efflux measured per gram of soil.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["RespirationDataGenerationActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:RespirationDataGenerationActivity"
    class_name: ClassVar[str] = "RespirationDataGenerationActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.RespirationDataGenerationActivity

    id: Union[str, RespirationDataGenerationActivityId] = None
    name: str = None
    acquisition_start_time: Union[str, XSDDateTime] = None
    acquisition_end_time: Union[str, XSDDateTime] = None
    method_id: Optional[Union[dict, "RespirationMethod"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RespirationDataGenerationActivityId):
            self.id = RespirationDataGenerationActivityId(self.id)

        if self.method_id is not None and not isinstance(self.method_id, RespirationMethod):
            self.method_id = RespirationMethod(**as_dict(self.method_id))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataProcessingActivity(YAMLRoot):
    """
    Abstract base for any data processing activity (digital to digital). Input data should
    be specified on workflow subclasses.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["DataProcessingActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:DataProcessingActivity"
    class_name: ClassVar[str] = "DataProcessingActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.DataProcessingActivity

    id: Union[str, DataProcessingActivityId] = None
    started_at_time: Union[str, XSDDateTime] = None
    parent_workflow_id: Optional[Union[str, DataProcessingActivityId]] = None
    workflow_steps: Optional[str] = None
    description: Optional[str] = None
    ended_at_time: Optional[Union[str, XSDDateTime]] = None
    software_url: Optional[str] = None
    software_version: Optional[str] = None
    software_poc: Optional[str] = None
    execution_resource: Optional[Union[str, "ExecutionResourceEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataProcessingActivityId):
            self.id = DataProcessingActivityId(self.id)

        if self._is_empty(self.started_at_time):
            self.MissingRequiredField("started_at_time")
        if not isinstance(self.started_at_time, XSDDateTime):
            self.started_at_time = XSDDateTime(self.started_at_time)

        if self.parent_workflow_id is not None and not isinstance(self.parent_workflow_id, DataProcessingActivityId):
            self.parent_workflow_id = DataProcessingActivityId(self.parent_workflow_id)

        if self.workflow_steps is not None and not isinstance(self.workflow_steps, str):
            self.workflow_steps = str(self.workflow_steps)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.ended_at_time is not None and not isinstance(self.ended_at_time, XSDDateTime):
            self.ended_at_time = XSDDateTime(self.ended_at_time)

        if self.software_url is not None and not isinstance(self.software_url, str):
            self.software_url = str(self.software_url)

        if self.software_version is not None and not isinstance(self.software_version, str):
            self.software_version = str(self.software_version)

        if self.software_poc is not None and not isinstance(self.software_poc, str):
            self.software_poc = str(self.software_poc)

        if self.execution_resource is not None and not isinstance(self.execution_resource, ExecutionResourceEnum):
            self.execution_resource = ExecutionResourceEnum(self.execution_resource)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AlternativeIdentifier(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["AlternativeIdentifier"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:AlternativeIdentifier"
    class_name: ClassVar[str] = "AlternativeIdentifier"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.AlternativeIdentifier

    id: Union[str, AlternativeIdentifierId] = None
    alternate_id: str = None
    alternate_identifier_type: Union[str, "AlternateIdentifierType"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AlternativeIdentifierId):
            self.id = AlternativeIdentifierId(self.id)

        if self._is_empty(self.alternate_id):
            self.MissingRequiredField("alternate_id")
        if not isinstance(self.alternate_id, str):
            self.alternate_id = str(self.alternate_id)

        if self._is_empty(self.alternate_identifier_type):
            self.MissingRequiredField("alternate_identifier_type")
        if not isinstance(self.alternate_identifier_type, AlternateIdentifierType):
            self.alternate_identifier_type = AlternateIdentifierType(self.alternate_identifier_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FunctionalAnnotationIdentifier(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["FunctionalAnnotationIdentifier"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:FunctionalAnnotationIdentifier"
    class_name: ClassVar[str] = "FunctionalAnnotationIdentifier"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.FunctionalAnnotationIdentifier

    id: Union[str, FunctionalAnnotationIdentifierId] = None
    functional_identifier: str = None
    database: Union[str, "AnnotationDatabaseEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FunctionalAnnotationIdentifierId):
            self.id = FunctionalAnnotationIdentifierId(self.id)

        if self._is_empty(self.functional_identifier):
            self.MissingRequiredField("functional_identifier")
        if not isinstance(self.functional_identifier, str):
            self.functional_identifier = str(self.functional_identifier)

        if self._is_empty(self.database):
            self.MissingRequiredField("database")
        if not isinstance(self.database, AnnotationDatabaseEnum):
            self.database = AnnotationDatabaseEnum(self.database)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Instrument(YAMLRoot):
    """
    A material entity that is designed to perform a function in a scientific
    investigation, but is not a reagent. This class models a specific
    instance of an instrument IF identifying information is filled out,
    otherwise, it is a generic standin for an instrument model.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["Instrument"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:Instrument"
    class_name: ClassVar[str] = "Instrument"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.Instrument

    id: Union[str, InstrumentId] = None
    name: str = None
    vendor: Optional[Union[str, "VendorEnum"]] = None
    model: Optional[Union[str, "ModelEnum"]] = None
    serial_number: Optional[str] = None
    lims_resource_id: Optional[int] = None
    location: Optional[str] = None
    maintenance: Optional[str] = None
    alternative_names: Optional[str] = None
    instrument_parameters: Optional[str] = None
    mass_analyzer_type: Optional[Union[str, "MassAnalyzerEnum"]] = None
    other_properties: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InstrumentId):
            self.id = InstrumentId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.vendor is not None and not isinstance(self.vendor, VendorEnum):
            self.vendor = VendorEnum(self.vendor)

        if self.model is not None and not isinstance(self.model, ModelEnum):
            self.model = ModelEnum(self.model)

        if self.serial_number is not None and not isinstance(self.serial_number, str):
            self.serial_number = str(self.serial_number)

        if self.lims_resource_id is not None and not isinstance(self.lims_resource_id, int):
            self.lims_resource_id = int(self.lims_resource_id)

        if self.location is not None and not isinstance(self.location, str):
            self.location = str(self.location)

        if self.maintenance is not None and not isinstance(self.maintenance, str):
            self.maintenance = str(self.maintenance)

        if self.alternative_names is not None and not isinstance(self.alternative_names, str):
            self.alternative_names = str(self.alternative_names)

        if self.instrument_parameters is not None and not isinstance(self.instrument_parameters, str):
            self.instrument_parameters = str(self.instrument_parameters)

        if self.mass_analyzer_type is not None and not isinstance(self.mass_analyzer_type, MassAnalyzerEnum):
            self.mass_analyzer_type = MassAnalyzerEnum(self.mass_analyzer_type)

        if self.other_properties is not None and not isinstance(self.other_properties, str):
            self.other_properties = str(self.other_properties)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OntologyClass(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["OntologyClass"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:OntologyClass"
    class_name: ClassVar[str] = "OntologyClass"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.OntologyClass

    id: Union[str, OntologyClassId] = None
    description: Optional[str] = None
    alternative_identifiers: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.alternative_identifiers is not None and not isinstance(self.alternative_identifiers, str):
            self.alternative_identifiers = str(self.alternative_identifiers)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContainerType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["ContainerType"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:ContainerType"
    class_name: ClassVar[str] = "ContainerType"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.ContainerType

    id: Union[str, ContainerTypeId] = None
    description: Optional[str] = None
    container_type: Optional[Union[str, "ContainerTypeEnum"]] = None
    container_size_id: Optional[Union[str, QuantityValueId]] = None
    axes: Optional[Union[Union[dict, "ContainerAxis"], list[Union[dict, "ContainerAxis"]]]] = empty_list()
    contains: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    label_format: Optional[str] = None
    renderer: Optional[str] = None
    slot_capacity: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContainerTypeId):
            self.id = ContainerTypeId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.container_type is not None and not isinstance(self.container_type, ContainerTypeEnum):
            self.container_type = ContainerTypeEnum(self.container_type)

        if self.container_size_id is not None and not isinstance(self.container_size_id, QuantityValueId):
            self.container_size_id = QuantityValueId(self.container_size_id)

        if not isinstance(self.axes, list):
            self.axes = [self.axes] if self.axes is not None else []
        self.axes = [v if isinstance(v, ContainerAxis) else ContainerAxis(**as_dict(v)) for v in self.axes]

        if not isinstance(self.contains, list):
            self.contains = [self.contains] if self.contains is not None else []
        self.contains = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.contains]

        if self.label_format is not None and not isinstance(self.label_format, str):
            self.label_format = str(self.label_format)

        if self.renderer is not None and not isinstance(self.renderer, str):
            self.renderer = str(self.renderer)

        if self.slot_capacity is not None and not isinstance(self.slot_capacity, str):
            self.slot_capacity = str(self.slot_capacity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContainerAxis(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["ContainerAxis"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:ContainerAxis"
    class_name: ClassVar[str] = "ContainerAxis"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.ContainerAxis

    name: Optional[str] = None
    values: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, str) else str(v) for v in self.values]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Custodian(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["Custodian"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:Custodian"
    class_name: ClassVar[str] = "Custodian"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.Custodian

    id: Union[str, CustodianId] = None
    person_id: Optional[Union[str, PersonValueId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CustodianId):
            self.id = CustodianId(self.id)

        if self.person_id is not None and not isinstance(self.person_id, PersonValueId):
            self.person_id = PersonValueId(self.person_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InstrumentAlternativeIdentifier(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["InstrumentAlternativeIdentifier"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:InstrumentAlternativeIdentifier"
    class_name: ClassVar[str] = "InstrumentAlternativeIdentifier"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.InstrumentAlternativeIdentifier

    id: Union[str, InstrumentAlternativeIdentifierId] = None
    instrument_id: Union[str, InstrumentId] = None
    alt_id: Optional[Union[str, AlternativeIdentifierId]] = None
    instrument_alt_id_provider: Optional[Union[str, "InstrumentAltIdProviderEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InstrumentAlternativeIdentifierId):
            self.id = InstrumentAlternativeIdentifierId(self.id)

        if self._is_empty(self.instrument_id):
            self.MissingRequiredField("instrument_id")
        if not isinstance(self.instrument_id, InstrumentId):
            self.instrument_id = InstrumentId(self.instrument_id)

        if self.alt_id is not None and not isinstance(self.alt_id, AlternativeIdentifierId):
            self.alt_id = AlternativeIdentifierId(self.alt_id)

        if self.instrument_alt_id_provider is not None and not isinstance(self.instrument_alt_id_provider, InstrumentAltIdProviderEnum):
            self.instrument_alt_id_provider = InstrumentAltIdProviderEnum(self.instrument_alt_id_provider)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LabDevice(YAMLRoot):
    """
    A lab device is a physical instrument or equipment used in a laboratory setting for conducting experiments,
    measurements, or analyses. It can include various types of instruments such as microscopes, spectrometers,
    centrifuges, and other specialized equipment. Lab devices are essential for performing scientific research and
    obtaining accurate data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["LabDevice"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:LabDevice"
    class_name: ClassVar[str] = "LabDevice"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.LabDevice

    id: Union[str, LabDeviceId] = None
    description: Optional[str] = None
    device_type: Optional[Union[str, "DeviceTypeEnum"]] = None
    activity_time_id: Optional[Union[str, QuantityValueId]] = None
    activity_speed_id: Optional[Union[str, QuantityValueId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LabDeviceId):
            self.id = LabDeviceId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.device_type is not None and not isinstance(self.device_type, DeviceTypeEnum):
            self.device_type = DeviceTypeEnum(self.device_type)

        if self.activity_time_id is not None and not isinstance(self.activity_time_id, QuantityValueId):
            self.activity_time_id = QuantityValueId(self.activity_time_id)

        if self.activity_speed_id is not None and not isinstance(self.activity_speed_id, QuantityValueId):
            self.activity_speed_id = QuantityValueId(self.activity_speed_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SampleProcessing(YAMLRoot):
    """
    Abstract base for any sample processing activity (physical to physical). Input data should
    be specified on workflow subclasses.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["SampleProcessing"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:SampleProcessing"
    class_name: ClassVar[str] = "SampleProcessing"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.SampleProcessing

    id: Union[str, SampleProcessingId] = None
    processing_steps: str = None
    protocol_url: Optional[str] = None
    protocol_version: Optional[str] = None
    analysis_type: Optional[Union[str, "RouteMethodEnum"]] = None
    method_name: Optional[Union[str, "MethodNameEnum"]] = None
    uses_sample: Optional[Union[str, SampleId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleProcessingId):
            self.id = SampleProcessingId(self.id)

        if self._is_empty(self.processing_steps):
            self.MissingRequiredField("processing_steps")
        if not isinstance(self.processing_steps, str):
            self.processing_steps = str(self.processing_steps)

        if self.protocol_url is not None and not isinstance(self.protocol_url, str):
            self.protocol_url = str(self.protocol_url)

        if self.protocol_version is not None and not isinstance(self.protocol_version, str):
            self.protocol_version = str(self.protocol_version)

        if self.analysis_type is not None and not isinstance(self.analysis_type, RouteMethodEnum):
            self.analysis_type = RouteMethodEnum(self.analysis_type)

        if self.method_name is not None and not isinstance(self.method_name, MethodNameEnum):
            self.method_name = MethodNameEnum(self.method_name)

        if self.uses_sample is not None and not isinstance(self.uses_sample, SampleId):
            self.uses_sample = SampleId(self.uses_sample)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProcessingSampleLink(YAMLRoot):
    """
    A link between a processed sample and the sample processing activity that produced it.
    This class captures the relationship between a processed sample and the sample processing
    activity that generated it, including the step number and role of the sample in the process.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["ProcessingSampleLink"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:ProcessingSampleLink"
    class_name: ClassVar[str] = "ProcessingSampleLink"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.ProcessingSampleLink

    id: Union[str, ProcessingSampleLinkId] = None
    sample_base_id: Union[str, SampleId] = None
    processing_id: Union[str, SampleProcessingId] = None
    step_number: int = None
    role: Union[str, "SampleRole"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessingSampleLinkId):
            self.id = ProcessingSampleLinkId(self.id)

        if self._is_empty(self.sample_base_id):
            self.MissingRequiredField("sample_base_id")
        if not isinstance(self.sample_base_id, SampleId):
            self.sample_base_id = SampleId(self.sample_base_id)

        if self._is_empty(self.processing_id):
            self.MissingRequiredField("processing_id")
        if not isinstance(self.processing_id, SampleProcessingId):
            self.processing_id = SampleProcessingId(self.processing_id)

        if self._is_empty(self.step_number):
            self.MissingRequiredField("step_number")
        if not isinstance(self.step_number, int):
            self.step_number = int(self.step_number)

        if self._is_empty(self.role):
            self.MissingRequiredField("role")
        if not isinstance(self.role, SampleRole):
            self.role = SampleRole(self.role)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InstrumentCustodian(YAMLRoot):
    """
    A link between an instrument and a custodian (person) responsible for it.
    This class captures the relationship between an instrument and the person
    who is responsible for its maintenance, calibration, and proper use.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["InstrumentCustodian"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:InstrumentCustodian"
    class_name: ClassVar[str] = "InstrumentCustodian"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.InstrumentCustodian

    instrument_id: Union[str, InstrumentId] = None
    custodian_id: Union[str, CustodianId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.instrument_id):
            self.MissingRequiredField("instrument_id")
        if not isinstance(self.instrument_id, InstrumentId):
            self.instrument_id = InstrumentId(self.instrument_id)

        if self._is_empty(self.custodian_id):
            self.MissingRequiredField("custodian_id")
        if not isinstance(self.custodian_id, CustodianId):
            self.custodian_id = CustodianId(self.custodian_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WorkflowExecutionFunctionalAnnotation(YAMLRoot):
    """
    A link between a workflow execution and a functional annotation identifier.
    This class captures the relationship between a workflow execution and the
    functional annotation identifier that was used in the analysis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["WorkflowExecutionFunctionalAnnotation"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:WorkflowExecutionFunctionalAnnotation"
    class_name: ClassVar[str] = "WorkflowExecutionFunctionalAnnotation"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.WorkflowExecutionFunctionalAnnotation

    workflow_id: Union[str, DataProcessingActivityId] = None
    functional_annotation_id: Union[str, FunctionalAnnotationIdentifierId] = None
    count: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.workflow_id):
            self.MissingRequiredField("workflow_id")
        if not isinstance(self.workflow_id, DataProcessingActivityId):
            self.workflow_id = DataProcessingActivityId(self.workflow_id)

        if self._is_empty(self.functional_annotation_id):
            self.MissingRequiredField("functional_annotation_id")
        if not isinstance(self.functional_annotation_id, FunctionalAnnotationIdentifierId):
            self.functional_annotation_id = FunctionalAnnotationIdentifierId(self.functional_annotation_id)

        if self.count is not None and not isinstance(self.count, float):
            self.count = float(self.count)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
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
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["XRayDataGenerationActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:XRayDataGenerationActivity"
    class_name: ClassVar[str] = "XRayDataGenerationActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.XRayDataGenerationActivity

    id: Union[str, XRayDataGenerationActivityId] = None
    name: str = None
    acquisition_start_time: Union[str, XSDDateTime] = None
    acquisition_end_time: Union[str, XSDDateTime] = None

@dataclass(repr=False)
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
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["XRFDataGenerationActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:XRFDataGenerationActivity"
    class_name: ClassVar[str] = "XRFDataGenerationActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.XRFDataGenerationActivity

    id: Union[str, XRFDataGenerationActivityId] = None
    name: str = None
    acquisition_start_time: Union[str, XSDDateTime] = None
    acquisition_end_time: Union[str, XSDDateTime] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, XRFDataGenerationActivityId):
            self.id = XRFDataGenerationActivityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
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
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["XRDDataGenerationActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:XRDDataGenerationActivity"
    class_name: ClassVar[str] = "XRDDataGenerationActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.XRDDataGenerationActivity

    id: Union[str, XRDDataGenerationActivityId] = None
    name: str = None
    acquisition_start_time: Union[str, XSDDateTime] = None
    acquisition_end_time: Union[str, XSDDateTime] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, XRDDataGenerationActivityId):
            self.id = XRDDataGenerationActivityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Changelog(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["Changelog"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:Changelog"
    class_name: ClassVar[str] = "Changelog"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.Changelog

    version: Union[str, ChangelogVersion] = None
    changelog: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, ChangelogVersion):
            self.version = ChangelogVersion(self.version)

        if self._is_empty(self.changelog):
            self.MissingRequiredField("changelog")
        if not isinstance(self.changelog, str):
            self.changelog = str(self.changelog)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MassSpectrometryInstrumentData(InstrumentData):
    """
    Raw data files output from a mass spectrometry instrument.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["MassSpectrometryInstrumentData"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:MassSpectrometryInstrumentData"
    class_name: ClassVar[str] = "MassSpectrometryInstrumentData"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.MassSpectrometryInstrumentData

    id: Union[str, MassSpectrometryInstrumentDataId] = None
    name: str = None
    s3_key: str = None
    description: str = None
    produced_by_ms_run: Optional[Union[str, MassSpectrometryDataGenerationActivityId]] = None
    ms_raw_file_type: Optional[Union[str, "MassSpecRawFileTypeEnum"]] = None
    collection_mode: Optional[Union[str, "MassSpectrumCollectionModeEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MassSpectrometryInstrumentDataId):
            self.id = MassSpectrometryInstrumentDataId(self.id)

        if self.produced_by_ms_run is not None and not isinstance(self.produced_by_ms_run, MassSpectrometryDataGenerationActivityId):
            self.produced_by_ms_run = MassSpectrometryDataGenerationActivityId(self.produced_by_ms_run)

        if self.ms_raw_file_type is not None and not isinstance(self.ms_raw_file_type, MassSpecRawFileTypeEnum):
            self.ms_raw_file_type = MassSpecRawFileTypeEnum(self.ms_raw_file_type)

        if self.collection_mode is not None and not isinstance(self.collection_mode, MassSpectrumCollectionModeEnum):
            self.collection_mode = MassSpectrumCollectionModeEnum(self.collection_mode)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MassSpectrometryDataProduct(ProcessedData):
    """
    Abstract base for all mass spectrometry data products.
    Inherits S3/file slots from dataProduct (via processedData is_a chain).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["MassSpectrometryDataProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:MassSpectrometryDataProduct"
    class_name: ClassVar[str] = "MassSpectrometryDataProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.MassSpectrometryDataProduct

    id: Union[str, MassSpectrometryDataProductId] = None
    name: str = None
    s3_key: str = None
    results_from_ms_processing: Optional[Union[str, MassSpectrometryDataProcessingActivityId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.results_from_ms_processing is not None and not isinstance(self.results_from_ms_processing, MassSpectrometryDataProcessingActivityId):
            self.results_from_ms_processing = MassSpectrometryDataProcessingActivityId(self.results_from_ms_processing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MSImageProduct(MassSpectrometryDataProduct):
    """
    one or more image(s) output from a mass spec data processing workflow (eg. LESA, CoreMS QC plots). Should be a zip
    file containing all similar image outputs from one data processing workflow.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["MSImageProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:MSImageProduct"
    class_name: ClassVar[str] = "MSImageProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.MSImageProduct

    id: Union[str, MSImageProductId] = None
    name: str = None
    s3_key: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MSImageProductId):
            self.id = MSImageProductId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularIdentificationProduct(MassSpectrometryDataProduct):
    """
    a file containing molecular formula identifications that was output from a mass spec data processing workflow (eg.
    .csv of m/z and molecular formulae, .hdf5 file).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["MolecularIdentificationProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:MolecularIdentificationProduct"
    class_name: ClassVar[str] = "MolecularIdentificationProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.MolecularIdentificationProduct

    id: Union[str, MolecularIdentificationProductId] = None
    name: str = None
    s3_key: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularIdentificationProductId):
            self.id = MolecularIdentificationProductId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MetaproteomicsProduct(MassSpectrometryDataProduct):
    """
    Abstract parent class for processed metaproteomics data. Details and subclasses TBD.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["MetaproteomicsProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:MetaproteomicsProduct"
    class_name: ClassVar[str] = "MetaproteomicsProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.MetaproteomicsProduct

    id: Union[str, MetaproteomicsProductId] = None
    name: str = None
    s3_key: str = None

@dataclass(repr=False)
class MassSpectrometryDataGenerationActivity(DataGenerationActivity):
    """
    A record of the mass spectrometry run that generates a raw data product.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["MassSpectrometryDataGenerationActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:MassSpectrometryDataGenerationActivity"
    class_name: ClassVar[str] = "MassSpectrometryDataGenerationActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.MassSpectrometryDataGenerationActivity

    id: Union[str, MassSpectrometryDataGenerationActivityId] = None
    name: str = None
    acquisition_start_time: Union[str, XSDDateTime] = None
    acquisition_end_time: Union[str, XSDDateTime] = None
    uses_ms_configuration: Union[dict, "MassSpectrometryConfiguration"] = None
    uses_chromatography: Optional[Union[dict, "ChromatographyConfiguration"]] = None
    analyte_category: Optional[Union[str, "AnalyteCategoryEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MassSpectrometryDataGenerationActivityId):
            self.id = MassSpectrometryDataGenerationActivityId(self.id)

        if self._is_empty(self.uses_ms_configuration):
            self.MissingRequiredField("uses_ms_configuration")
        if not isinstance(self.uses_ms_configuration, MassSpectrometryConfiguration):
            self.uses_ms_configuration = MassSpectrometryConfiguration(**as_dict(self.uses_ms_configuration))

        if self.uses_chromatography is not None and not isinstance(self.uses_chromatography, ChromatographyConfiguration):
            self.uses_chromatography = ChromatographyConfiguration(**as_dict(self.uses_chromatography))

        if self.analyte_category is not None and not isinstance(self.analyte_category, AnalyteCategoryEnum):
            self.analyte_category = AnalyteCategoryEnum(self.analyte_category)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Configuration(YAMLRoot):
    """
    Record of configuration and/or settings for an activity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["Configuration"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:Configuration"
    class_name: ClassVar[str] = "Configuration"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.Configuration

    name: str = None
    id: Union[str, Uuid] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, Uuid):
            self.id = Uuid(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MassSpectrometryConfiguration(Configuration):
    """
    Instrument configuration and setup for a mass spectrometry run.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["MassSpectrometryConfiguration"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:MassSpectrometryConfiguration"
    class_name: ClassVar[str] = "MassSpectrometryConfiguration"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.MassSpectrometryConfiguration

    name: str = None
    id: Union[str, Uuid] = None
    injection: str = None
    ionization: Union[str, "IonizationSourceEnum"] = None
    polarity: Union[str, "PolarityEnum"] = None
    resolution: Union[str, "MassSpecResolutionEnum"] = None
    dd_ms2_resolution: float = None
    loop_count: str = None
    fragmentation: Optional[Union[str, "FragmentationEnum"]] = None
    iat: Optional[float] = None
    fid: Optional[float] = None
    mass_range_max: Optional[float] = None
    mass_range_min: Optional[float] = None
    acquisition_strategy: Optional[Union[str, "MassSpectrometryAcquisitionStrategyEnum"]] = None
    lims_protocol_instance_id: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.injection):
            self.MissingRequiredField("injection")
        if not isinstance(self.injection, str):
            self.injection = str(self.injection)

        if self._is_empty(self.ionization):
            self.MissingRequiredField("ionization")
        if not isinstance(self.ionization, IonizationSourceEnum):
            self.ionization = IonizationSourceEnum(self.ionization)

        if self._is_empty(self.polarity):
            self.MissingRequiredField("polarity")
        if not isinstance(self.polarity, PolarityEnum):
            self.polarity = PolarityEnum(self.polarity)

        if self._is_empty(self.resolution):
            self.MissingRequiredField("resolution")
        if not isinstance(self.resolution, MassSpecResolutionEnum):
            self.resolution = MassSpecResolutionEnum(self.resolution)

        if self._is_empty(self.dd_ms2_resolution):
            self.MissingRequiredField("dd_ms2_resolution")
        if not isinstance(self.dd_ms2_resolution, float):
            self.dd_ms2_resolution = float(self.dd_ms2_resolution)

        if self._is_empty(self.loop_count):
            self.MissingRequiredField("loop_count")
        if not isinstance(self.loop_count, str):
            self.loop_count = str(self.loop_count)

        if self.fragmentation is not None and not isinstance(self.fragmentation, FragmentationEnum):
            self.fragmentation = FragmentationEnum(self.fragmentation)

        if self.iat is not None and not isinstance(self.iat, float):
            self.iat = float(self.iat)

        if self.fid is not None and not isinstance(self.fid, float):
            self.fid = float(self.fid)

        if self.mass_range_max is not None and not isinstance(self.mass_range_max, float):
            self.mass_range_max = float(self.mass_range_max)

        if self.mass_range_min is not None and not isinstance(self.mass_range_min, float):
            self.mass_range_min = float(self.mass_range_min)

        if self.acquisition_strategy is not None and not isinstance(self.acquisition_strategy, MassSpectrometryAcquisitionStrategyEnum):
            self.acquisition_strategy = MassSpectrometryAcquisitionStrategyEnum(self.acquisition_strategy)

        if self.lims_protocol_instance_id is not None and not isinstance(self.lims_protocol_instance_id, int):
            self.lims_protocol_instance_id = int(self.lims_protocol_instance_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChromatographyConfiguration(Configuration):
    """
    Configuration and settings for a chromatography run.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["ChromatographyConfiguration"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:ChromatographyConfiguration"
    class_name: ClassVar[str] = "ChromatographyConfiguration"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.ChromatographyConfiguration

    name: str = None
    id: Union[str, Uuid] = None
    chromatography_type: Union[str, "ChromatographyCategoryEnum"] = None
    column: Optional[str] = None
    column_dimensions: Optional[str] = None
    column_manufacturer: Optional[str] = None
    mobile_phases: Optional[Union[Union[str, MobilePhaseSegmentId], list[Union[str, MobilePhaseSegmentId]]]] = empty_list()
    stationary_phase: Optional[str] = None
    temperature_celsius: Optional[float] = None
    duration_min: Optional[float] = None
    flow_rate_ul_min: Optional[float] = None
    injection_volume_ul: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.chromatography_type):
            self.MissingRequiredField("chromatography_type")
        if not isinstance(self.chromatography_type, ChromatographyCategoryEnum):
            self.chromatography_type = ChromatographyCategoryEnum(self.chromatography_type)

        if self.column is not None and not isinstance(self.column, str):
            self.column = str(self.column)

        if self.column_dimensions is not None and not isinstance(self.column_dimensions, str):
            self.column_dimensions = str(self.column_dimensions)

        if self.column_manufacturer is not None and not isinstance(self.column_manufacturer, str):
            self.column_manufacturer = str(self.column_manufacturer)

        if not isinstance(self.mobile_phases, list):
            self.mobile_phases = [self.mobile_phases] if self.mobile_phases is not None else []
        self.mobile_phases = [v if isinstance(v, MobilePhaseSegmentId) else MobilePhaseSegmentId(v) for v in self.mobile_phases]

        if self.stationary_phase is not None and not isinstance(self.stationary_phase, str):
            self.stationary_phase = str(self.stationary_phase)

        if self.temperature_celsius is not None and not isinstance(self.temperature_celsius, float):
            self.temperature_celsius = float(self.temperature_celsius)

        if self.duration_min is not None and not isinstance(self.duration_min, float):
            self.duration_min = float(self.duration_min)

        if self.flow_rate_ul_min is not None and not isinstance(self.flow_rate_ul_min, float):
            self.flow_rate_ul_min = float(self.flow_rate_ul_min)

        if self.injection_volume_ul is not None and not isinstance(self.injection_volume_ul, float):
            self.injection_volume_ul = float(self.injection_volume_ul)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MobilePhaseSegment(YAMLRoot):
    """
    A segment of the mobile phase used in chromatography during mass spectrometry.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["MobilePhaseSegment"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:MobilePhaseSegment"
    class_name: ClassVar[str] = "MobilePhaseSegment"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.MobilePhaseSegment

    id: Union[str, MobilePhaseSegmentId] = None
    name: str = None
    duration_min: Optional[float] = None
    segment_order: Optional[int] = None
    substance: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MobilePhaseSegmentId):
            self.id = MobilePhaseSegmentId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.duration_min is not None and not isinstance(self.duration_min, float):
            self.duration_min = float(self.duration_min)

        if self.segment_order is not None and not isinstance(self.segment_order, int):
            self.segment_order = int(self.segment_order)

        if self.substance is not None and not isinstance(self.substance, str):
            self.substance = str(self.substance)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MassSpectrometryDataProcessingActivity(DataProcessingActivity):
    """
    Concrete mass spectrometry workflow run. Inherits all DataProcessingActivity
    slots including used_software and version.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["MassSpectrometryDataProcessingActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:MassSpectrometryDataProcessingActivity"
    class_name: ClassVar[str] = "MassSpectrometryDataProcessingActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.MassSpectrometryDataProcessingActivity

    id: Union[str, MassSpectrometryDataProcessingActivityId] = None
    started_at_time: Union[str, XSDDateTime] = None
    uses_calibration: Optional[Union[str, MassSpectrometryStandardRunId]] = None
    uses_raw_ms_data: Optional[Union[str, MassSpectrometryInstrumentDataId]] = None
    lims_task_instance_id: Optional[int] = None
    metaproteomics_analysis_category: Optional[Union[str, "MetaproteomicsAnalysisCategoryEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MassSpectrometryDataProcessingActivityId):
            self.id = MassSpectrometryDataProcessingActivityId(self.id)

        if self.uses_calibration is not None and not isinstance(self.uses_calibration, MassSpectrometryStandardRunId):
            self.uses_calibration = MassSpectrometryStandardRunId(self.uses_calibration)

        if self.uses_raw_ms_data is not None and not isinstance(self.uses_raw_ms_data, MassSpectrometryInstrumentDataId):
            self.uses_raw_ms_data = MassSpectrometryInstrumentDataId(self.uses_raw_ms_data)

        if self.lims_task_instance_id is not None and not isinstance(self.lims_task_instance_id, int):
            self.lims_task_instance_id = int(self.lims_task_instance_id)

        if self.metaproteomics_analysis_category is not None and not isinstance(self.metaproteomics_analysis_category, MetaproteomicsAnalysisCategoryEnum):
            self.metaproteomics_analysis_category = MetaproteomicsAnalysisCategoryEnum(self.metaproteomics_analysis_category)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MassSpectrometryStandardRun(YAMLRoot):
    """
    A record of a mass spectrometry standard run with a batch of samples, which is used for calibration and quality
    control.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["MassSpectrometryStandardRun"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:MassSpectrometryStandardRun"
    class_name: ClassVar[str] = "MassSpectrometryStandardRun"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.MassSpectrometryStandardRun

    id: Union[str, MassSpectrometryStandardRunId] = None
    name: str = None
    description: Optional[str] = None
    internal_calibration: Optional[Union[bool, Bool]] = None
    calibration_target: Optional[Union[str, "CalibrationTargetEnum"]] = None
    calibration_standard: Optional[Union[str, PurchasedMaterialId]] = None
    calibration_data: Optional[Union[str, MassSpectrometryInstrumentDataId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MassSpectrometryStandardRunId):
            self.id = MassSpectrometryStandardRunId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.internal_calibration is not None and not isinstance(self.internal_calibration, Bool):
            self.internal_calibration = Bool(self.internal_calibration)

        if self.calibration_target is not None and not isinstance(self.calibration_target, CalibrationTargetEnum):
            self.calibration_target = CalibrationTargetEnum(self.calibration_target)

        if self.calibration_standard is not None and not isinstance(self.calibration_standard, PurchasedMaterialId):
            self.calibration_standard = PurchasedMaterialId(self.calibration_standard)

        if self.calibration_data is not None and not isinstance(self.calibration_data, MassSpectrometryInstrumentDataId):
            self.calibration_data = MassSpectrometryInstrumentDataId(self.calibration_data)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HasIncubationConditions(YAMLRoot):
    """
    Mixin for activities/setups that involve controlled incubation.
    Used by CultureGrowth activities AND PlateSetupActivity, which share
    temperature and agitation parameters but live in different branches
    of the sampleProcessing is_a tree.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["HasIncubationConditions"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:HasIncubationConditions"
    class_name: ClassVar[str] = "HasIncubationConditions"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.HasIncubationConditions

    temperature_celsius: Optional[float] = None
    agitation_speed_rpm: Optional[int] = None
    oxygen_status: Optional[Union[str, "OxygenStatusEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.temperature_celsius is not None and not isinstance(self.temperature_celsius, float):
            self.temperature_celsius = float(self.temperature_celsius)

        if self.agitation_speed_rpm is not None and not isinstance(self.agitation_speed_rpm, int):
            self.agitation_speed_rpm = int(self.agitation_speed_rpm)

        if self.oxygen_status is not None and not isinstance(self.oxygen_status, OxygenStatusEnum):
            self.oxygen_status = OxygenStatusEnum(self.oxygen_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PurchasedMaterial(YAMLRoot):
    """
    [NEW ABSTRACT CLASS] Lightweight base for non-sample physical lab materials
    that are not instruments.  Currently Strain is the only concrete subtype.
    Activities reference Strain via the strain_ref FK slot.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["PurchasedMaterial"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:PurchasedMaterial"
    class_name: ClassVar[str] = "PurchasedMaterial"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.PurchasedMaterial

    id: Union[str, PurchasedMaterialId] = None
    purchased_material_type: str = None
    name: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.purchased_material_type):
            self.MissingRequiredField("purchased_material_type")
        if not isinstance(self.purchased_material_type, str):
            self.purchased_material_type = str(self.purchased_material_type)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PurchasedMaterialId):
            self.id = PurchasedMaterialId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LabProcessingActivity(YAMLRoot):
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
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["LabProcessingActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:LabProcessingActivity"
    class_name: ClassVar[str] = "LabProcessingActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.LabProcessingActivity

    id: Union[str, LabProcessingActivityId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LabProcessingActivityId):
            self.id = LabProcessingActivityId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
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
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["MediaPreparation"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:MediaPreparation"
    class_name: ClassVar[str] = "MediaPreparation"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.MediaPreparation

    id: Union[str, MediaPreparationId] = None
    processing_steps: str = None
    media_type: Optional[Union[str, "MediaTypeEnum"]] = None
    volume_ml: Optional[float] = None
    media_recipe: Optional[str] = None
    media_formulation: Optional[Union[str, "FormulationEnum"]] = None
    commercial_media_catalog: Optional[str] = None
    sterilization_method: Optional[Union[str, "SterilizationMethodEnum"]] = None
    ph_adjustment: Optional[Union[bool, Bool]] = None
    ph_target: Optional[float] = None
    exposure_sensitivity: Optional[Union[str, list[str]]] = empty_list()
    media_additions: Optional[Union[str, list[str]]] = empty_list()
    storage_temperature: Optional[str] = None
    creation_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MediaPreparationId):
            self.id = MediaPreparationId(self.id)

        if self.media_type is not None and not isinstance(self.media_type, MediaTypeEnum):
            self.media_type = MediaTypeEnum(self.media_type)

        if self.volume_ml is not None and not isinstance(self.volume_ml, float):
            self.volume_ml = float(self.volume_ml)

        if self.media_recipe is not None and not isinstance(self.media_recipe, str):
            self.media_recipe = str(self.media_recipe)

        if self.media_formulation is not None and not isinstance(self.media_formulation, FormulationEnum):
            self.media_formulation = FormulationEnum(self.media_formulation)

        if self.commercial_media_catalog is not None and not isinstance(self.commercial_media_catalog, str):
            self.commercial_media_catalog = str(self.commercial_media_catalog)

        if self.sterilization_method is not None and not isinstance(self.sterilization_method, SterilizationMethodEnum):
            self.sterilization_method = SterilizationMethodEnum(self.sterilization_method)

        if self.ph_adjustment is not None and not isinstance(self.ph_adjustment, Bool):
            self.ph_adjustment = Bool(self.ph_adjustment)

        if self.ph_target is not None and not isinstance(self.ph_target, float):
            self.ph_target = float(self.ph_target)

        if not isinstance(self.exposure_sensitivity, list):
            self.exposure_sensitivity = [self.exposure_sensitivity] if self.exposure_sensitivity is not None else []
        self.exposure_sensitivity = [v if isinstance(v, str) else str(v) for v in self.exposure_sensitivity]

        if not isinstance(self.media_additions, list):
            self.media_additions = [self.media_additions] if self.media_additions is not None else []
        self.media_additions = [v if isinstance(v, str) else str(v) for v in self.media_additions]

        if self.storage_temperature is not None and not isinstance(self.storage_temperature, str):
            self.storage_temperature = str(self.storage_temperature)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CultureGrowth(SampleProcessing):
    """
    Abstract activity for growing cultures from samples or other cultures.

    Concrete subclasses: StrainPurity, StockCulturePreparation,
    PreCultureGrowth, ExperimentalCulture.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["CultureGrowth"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:CultureGrowth"
    class_name: ClassVar[str] = "CultureGrowth"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.CultureGrowth

    id: Union[str, CultureGrowthId] = None
    processing_steps: str = None
    biological_entity_ref: Optional[Union[str, BiologicalEntityId]] = None
    growth_medium: Optional[str] = None
    incubation_time_hours: Optional[float] = None
    container_type: Optional[str] = None
    temperature_celsius: Optional[float] = None
    agitation_speed_rpm: Optional[int] = None
    oxygen_status: Optional[Union[str, "OxygenStatusEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CultureGrowthId):
            self.id = CultureGrowthId(self.id)

        if self.biological_entity_ref is not None and not isinstance(self.biological_entity_ref, BiologicalEntityId):
            self.biological_entity_ref = BiologicalEntityId(self.biological_entity_ref)

        if self.growth_medium is not None and not isinstance(self.growth_medium, str):
            self.growth_medium = str(self.growth_medium)

        if self.incubation_time_hours is not None and not isinstance(self.incubation_time_hours, float):
            self.incubation_time_hours = float(self.incubation_time_hours)

        if self.container_type is not None and not isinstance(self.container_type, str):
            self.container_type = str(self.container_type)

        if self.temperature_celsius is not None and not isinstance(self.temperature_celsius, float):
            self.temperature_celsius = float(self.temperature_celsius)

        if self.agitation_speed_rpm is not None and not isinstance(self.agitation_speed_rpm, int):
            self.agitation_speed_rpm = int(self.agitation_speed_rpm)

        if self.oxygen_status is not None and not isinstance(self.oxygen_status, OxygenStatusEnum):
            self.oxygen_status = OxygenStatusEnum(self.oxygen_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StrainPurity(CultureGrowth):
    """
    Purity check of a strain culture.  Verifies that a sample contains the
    expected strain without contamination.

    Input:  sample(s) via processingSampleLink (role: input_sample)
    Output: typically no new processedSample   pass/fail QC gate.
    Refs:   Media (growth medium), Strain (target organism)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["StrainPurity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:StrainPurity"
    class_name: ClassVar[str] = "StrainPurity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.StrainPurity

    id: Union[str, StrainPurityId] = None
    processing_steps: str = None
    inspection_method: Optional[str] = None
    target_strain: Optional[str] = None
    contaminant_strains: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StrainPurityId):
            self.id = StrainPurityId(self.id)

        if self.inspection_method is not None and not isinstance(self.inspection_method, str):
            self.inspection_method = str(self.inspection_method)

        if self.target_strain is not None and not isinstance(self.target_strain, str):
            self.target_strain = str(self.target_strain)

        if self.contaminant_strains is not None and not isinstance(self.contaminant_strains, str):
            self.contaminant_strains = str(self.contaminant_strains)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StockCulturePreparation(CultureGrowth):
    """
    Preparation of a stock culture from user samples for long-term storage.

    Input:  sample(s) via processingSampleLink (role: input_sample)
    Output: processedSample(type='stock_culture') via processingSampleLink
    Refs:   Media (growth medium), Strain
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["StockCulturePreparation"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:StockCulturePreparation"
    class_name: ClassVar[str] = "StockCulturePreparation"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.StockCulturePreparation

    id: Union[str, StockCulturePreparationId] = None
    processing_steps: str = None
    preparation_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StockCulturePreparationId):
            self.id = StockCulturePreparationId(self.id)

        if self.preparation_date is not None and not isinstance(self.preparation_date, XSDDate):
            self.preparation_date = XSDDate(self.preparation_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PreCultureGrowth(CultureGrowth):
    """
    Growth of a pre-culture to establish viable inoculum before
    experimental culture growth.

    Input:  processedSample(type='stock_culture') via processingSampleLink
    Output: processedSample(type='pre_culture') via processingSampleLink
    Refs:   Media (growth medium), Strain
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["PreCultureGrowth"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:PreCultureGrowth"
    class_name: ClassVar[str] = "PreCultureGrowth"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.PreCultureGrowth

    id: Union[str, PreCultureGrowthId] = None
    processing_steps: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PreCultureGrowthId):
            self.id = PreCultureGrowthId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExperimentalCulture(CultureGrowth):
    """
    Growth of an experimental culture for downstream analysis.
    This is the terminal culture step before plate setup or direct measurement.

    Input:  processedSample(type='pre_culture') via processingSampleLink
    Output: processedSample(type='experimental_culture') via processingSampleLink
    Refs:   Media (growth medium), Strain
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["ExperimentalCulture"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:ExperimentalCulture"
    class_name: ClassVar[str] = "ExperimentalCulture"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.ExperimentalCulture

    id: Union[str, ExperimentalCultureId] = None
    processing_steps: str = None
    treatment_type: Optional[str] = None
    growth_time: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExperimentalCultureId):
            self.id = ExperimentalCultureId(self.id)

        if self.treatment_type is not None and not isinstance(self.treatment_type, str):
            self.treatment_type = str(self.treatment_type)

        if self.growth_time is not None and not isinstance(self.growth_time, str):
            self.growth_time = str(self.growth_time)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
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
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["PlateSetupActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:PlateSetupActivity"
    class_name: ClassVar[str] = "PlateSetupActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.PlateSetupActivity

    id: Union[str, PlateSetupActivityId] = None
    processing_steps: str = None
    plate_type: str = None
    setup_date: Union[str, XSDDateTime] = None
    plate_barcode: Optional[str] = None
    setup_operator_id: Optional[Union[str, PersonValueId]] = None
    setup_instrument: Optional[str] = None
    sealing_method: Optional[str] = None
    well_metadata: Optional[Union[Union[dict, "WellMetadata"], list[Union[dict, "WellMetadata"]]]] = empty_list()
    temperature_celsius: Optional[float] = None
    agitation_speed_rpm: Optional[int] = None
    oxygen_status: Optional[Union[str, "OxygenStatusEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.plate_type):
            self.MissingRequiredField("plate_type")
        if not isinstance(self.plate_type, str):
            self.plate_type = str(self.plate_type)

        if self._is_empty(self.setup_date):
            self.MissingRequiredField("setup_date")
        if not isinstance(self.setup_date, XSDDateTime):
            self.setup_date = XSDDateTime(self.setup_date)

        if self.plate_barcode is not None and not isinstance(self.plate_barcode, str):
            self.plate_barcode = str(self.plate_barcode)

        if self.setup_operator_id is not None and not isinstance(self.setup_operator_id, PersonValueId):
            self.setup_operator_id = PersonValueId(self.setup_operator_id)

        if self.setup_instrument is not None and not isinstance(self.setup_instrument, str):
            self.setup_instrument = str(self.setup_instrument)

        if self.sealing_method is not None and not isinstance(self.sealing_method, str):
            self.sealing_method = str(self.sealing_method)

        self._normalize_inlined_as_list(slot_name="well_metadata", slot_type=WellMetadata, key_name="position", keyed=False)

        if self.temperature_celsius is not None and not isinstance(self.temperature_celsius, float):
            self.temperature_celsius = float(self.temperature_celsius)

        if self.agitation_speed_rpm is not None and not isinstance(self.agitation_speed_rpm, int):
            self.agitation_speed_rpm = int(self.agitation_speed_rpm)

        if self.oxygen_status is not None and not isinstance(self.oxygen_status, OxygenStatusEnum):
            self.oxygen_status = OxygenStatusEnum(self.oxygen_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
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
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["AMP2PlateSetupActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:AMP2PlateSetupActivity"
    class_name: ClassVar[str] = "AMP2PlateSetupActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.AMP2PlateSetupActivity

    id: Union[str, AMP2PlateSetupActivityId] = None
    processing_steps: str = None
    plate_type: str = None
    setup_date: Union[str, XSDDateTime] = None
    media_ref: Optional[Union[str, ProcessedSampleId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AMP2PlateSetupActivityId):
            self.id = AMP2PlateSetupActivityId(self.id)

        if self.media_ref is not None and not isinstance(self.media_ref, ProcessedSampleId):
            self.media_ref = ProcessedSampleId(self.media_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EcoplatePlateSetupActivity(PlateSetupActivity):
    """
    Ecoplate-specific plate setup.
    NO media reference   carbon source and treatment are per-well experimental
    design captured in EcoplateWellMetadata instances.

    Input:  processedSample(type='soil_extract') via processingSampleLink
    Output: processedSample(type='ecoplate_plate') via processingSampleLink

    v1 origin: plate-general.yaml EcoplatePlateSetupActivity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["EcoplatePlateSetupActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:EcoplatePlateSetupActivity"
    class_name: ClassVar[str] = "EcoplatePlateSetupActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.EcoplatePlateSetupActivity

    id: Union[str, EcoplatePlateSetupActivityId] = None
    processing_steps: str = None
    plate_type: str = None
    setup_date: Union[str, XSDDateTime] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EcoplatePlateSetupActivityId):
            self.id = EcoplatePlateSetupActivityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PlateDataGenerationActivity(DataGenerationActivity):
    """
    Abstract base for plate measurement activities.
    Adds timepoint_label for repeated-measurement series
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["PlateDataGenerationActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:PlateDataGenerationActivity"
    class_name: ClassVar[str] = "PlateDataGenerationActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.PlateDataGenerationActivity

    id: Union[str, PlateDataGenerationActivityId] = None
    name: str = None
    acquisition_start_time: Union[str, XSDDateTime] = None
    acquisition_end_time: Union[str, XSDDateTime] = None
    timepoint_label: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.timepoint_label):
            self.MissingRequiredField("timepoint_label")
        if not isinstance(self.timepoint_label, str):
            self.timepoint_label = str(self.timepoint_label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AMP2DataGenerationActivity(PlateDataGenerationActivity):
    """
    AMP2 plate measurement (OD, fluorescence, flow cytometry).
    analyte_id -> processedSample(type='amp2_96well_plate')

    Chained via DataProcessingActivity.parent_workflow_id to track
    multi-timepoint series on the same plate.

    v1 origin: plate-general.yaml AMP2DataGenerationActivity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["AMP2DataGenerationActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:AMP2DataGenerationActivity"
    class_name: ClassVar[str] = "AMP2DataGenerationActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.AMP2DataGenerationActivity

    id: Union[str, AMP2DataGenerationActivityId] = None
    name: str = None
    acquisition_start_time: Union[str, XSDDateTime] = None
    acquisition_end_time: Union[str, XSDDateTime] = None
    timepoint_label: str = None
    wavelength_nm: int = None
    measurement_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AMP2DataGenerationActivityId):
            self.id = AMP2DataGenerationActivityId(self.id)

        if self._is_empty(self.wavelength_nm):
            self.MissingRequiredField("wavelength_nm")
        if not isinstance(self.wavelength_nm, int):
            self.wavelength_nm = int(self.wavelength_nm)

        if self.measurement_type is not None and not isinstance(self.measurement_type, str):
            self.measurement_type = str(self.measurement_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EcoplateDataGenerationActivity(PlateDataGenerationActivity):
    """
    Ecoplate absorbance measurement at a single timepoint.
    analyte_id -> processedSample(type='ecoplate_plate')
    wavelength_nm typically 590 for Biolog EcoPlates.

    v1 origin: plate-general.yaml EcoplateDataGenerationActivity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["EcoplateDataGenerationActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:EcoplateDataGenerationActivity"
    class_name: ClassVar[str] = "EcoplateDataGenerationActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.EcoplateDataGenerationActivity

    id: Union[str, EcoplateDataGenerationActivityId] = None
    name: str = None
    acquisition_start_time: Union[str, XSDDateTime] = None
    acquisition_end_time: Union[str, XSDDateTime] = None
    timepoint_label: str = None
    wavelength_nm: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EcoplateDataGenerationActivityId):
            self.id = EcoplateDataGenerationActivityId(self.id)

        if self._is_empty(self.wavelength_nm):
            self.MissingRequiredField("wavelength_nm")
        if not isinstance(self.wavelength_nm, int):
            self.wavelength_nm = int(self.wavelength_nm)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PlateProduct(YAMLRoot):
    """
    Abstract base for plate measurement data products.
    Common summary slots shared across AMP2 and Ecoplate products.

    v1 origin: plate-general.yaml PlateProduct
    v2 change: follows existing satellite-table pattern (id: range: processedData)
    instead of v1's is_a: dataProduct.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["PlateProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:PlateProduct"
    class_name: ClassVar[str] = "PlateProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.PlateProduct

    wavelength_nm: int = None
    timepoint_label: str = None
    plate_average: Optional[float] = None
    blank_mean: Optional[float] = None
    cv_percent: Optional[float] = None
    well_readings: Optional[Union[Union[dict, "WellReading"], list[Union[dict, "WellReading"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.wavelength_nm):
            self.MissingRequiredField("wavelength_nm")
        if not isinstance(self.wavelength_nm, int):
            self.wavelength_nm = int(self.wavelength_nm)

        if self._is_empty(self.timepoint_label):
            self.MissingRequiredField("timepoint_label")
        if not isinstance(self.timepoint_label, str):
            self.timepoint_label = str(self.timepoint_label)

        if self.plate_average is not None and not isinstance(self.plate_average, float):
            self.plate_average = float(self.plate_average)

        if self.blank_mean is not None and not isinstance(self.blank_mean, float):
            self.blank_mean = float(self.blank_mean)

        if self.cv_percent is not None and not isinstance(self.cv_percent, float):
            self.cv_percent = float(self.cv_percent)

        self._normalize_inlined_as_list(slot_name="well_readings", slot_type=WellReading, key_name="position", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AMP2ODProduct(PlateProduct):
    """
    AMP2 optical density measurement product.
    One row per plate × timepoint.
    processedData.type = 'amp2_od'

    v1 origin: plate-general.yaml AMP2ODProduct
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["AMP2ODProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:AMP2ODProduct"
    class_name: ClassVar[str] = "AMP2ODProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.AMP2ODProduct

    wavelength_nm: int = None
    timepoint_label: str = None
    plate_reader_model: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.plate_reader_model is not None and not isinstance(self.plate_reader_model, str):
            self.plate_reader_model = str(self.plate_reader_model)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EcoplateAbsorbanceProduct(PlateProduct):
    """
    Ecoplate absorbance measurement product.
    One row per plate × timepoint.
    processedData.type = 'ecoplate_absorbance'

    v1 origin: plate-general.yaml EcoplateAbsorbanceProduct
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["EcoplateAbsorbanceProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:EcoplateAbsorbanceProduct"
    class_name: ClassVar[str] = "EcoplateAbsorbanceProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.EcoplateAbsorbanceProduct

    wavelength_nm: int = None
    timepoint_label: str = None
    plate_lot: Optional[str] = None
    uninoculated_mean: Optional[float] = None
    average_well_color_development: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.plate_lot is not None and not isinstance(self.plate_lot, str):
            self.plate_lot = str(self.plate_lot)

        if self.uninoculated_mean is not None and not isinstance(self.uninoculated_mean, float):
            self.uninoculated_mean = float(self.uninoculated_mean)

        if self.average_well_color_development is not None and not isinstance(self.average_well_color_development, float):
            self.average_well_color_development = float(self.average_well_color_development)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WellMetadata(YAMLRoot):
    """
    Base structure for per-well metadata in plate setup.
    NOT a standalone database table; embedded structured entries under
    PlateSetupActivity.well_metadata.
    Subclasses add type-specific fields.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["WellMetadata"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:WellMetadata"
    class_name: ClassVar[str] = "WellMetadata"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.WellMetadata

    position: str = None
    well_type: Optional[str] = None
    replicate_group: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.position):
            self.MissingRequiredField("position")
        if not isinstance(self.position, str):
            self.position = str(self.position)

        if self.well_type is not None and not isinstance(self.well_type, str):
            self.well_type = str(self.well_type)

        if self.replicate_group is not None and not isinstance(self.replicate_group, str):
            self.replicate_group = str(self.replicate_group)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AMP2WellMetadata(WellMetadata):
    """
    AMP2-specific per-well metadata.
    Minimal   media composition comes from the Media entity referenced via
    the activity's media_ref slot.  Per-well data is volumes and replicate info.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["AMP2WellMetadata"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:AMP2WellMetadata"
    class_name: ClassVar[str] = "AMP2WellMetadata"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.AMP2WellMetadata

    position: str = None
    media_volume_ul: float = None
    inoculum_volume_ul: float = None
    media_ref: Optional[Union[str, ProcessedSampleId]] = None
    sample_id: Optional[str] = None
    treatments: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.media_volume_ul):
            self.MissingRequiredField("media_volume_ul")
        if not isinstance(self.media_volume_ul, float):
            self.media_volume_ul = float(self.media_volume_ul)

        if self._is_empty(self.inoculum_volume_ul):
            self.MissingRequiredField("inoculum_volume_ul")
        if not isinstance(self.inoculum_volume_ul, float):
            self.inoculum_volume_ul = float(self.inoculum_volume_ul)

        if self.media_ref is not None and not isinstance(self.media_ref, ProcessedSampleId):
            self.media_ref = ProcessedSampleId(self.media_ref)

        if self.sample_id is not None and not isinstance(self.sample_id, str):
            self.sample_id = str(self.sample_id)

        if not isinstance(self.treatments, list):
            self.treatments = [self.treatments] if self.treatments is not None else []
        self.treatments = [v if isinstance(v, str) else str(v) for v in self.treatments]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EcoplateWellMetadata(WellMetadata):
    """
    Ecoplate-specific per-well metadata.
    Rich   no media entity; carbon source and treatment are per-well
    experimental design variables.

    v1 origin: plate-general.yaml EcoplateWellMetadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["EcoplateWellMetadata"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:EcoplateWellMetadata"
    class_name: ClassVar[str] = "EcoplateWellMetadata"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.EcoplateWellMetadata

    position: str = None
    media_volume_ul: float = None
    carbon_source: str = None
    treatment: Optional[str] = None
    treatment_concentration: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.media_volume_ul):
            self.MissingRequiredField("media_volume_ul")
        if not isinstance(self.media_volume_ul, float):
            self.media_volume_ul = float(self.media_volume_ul)

        if self._is_empty(self.carbon_source):
            self.MissingRequiredField("carbon_source")
        if not isinstance(self.carbon_source, str):
            self.carbon_source = str(self.carbon_source)

        if self.treatment is not None and not isinstance(self.treatment, str):
            self.treatment = str(self.treatment)

        if self.treatment_concentration is not None and not isinstance(self.treatment_concentration, str):
            self.treatment_concentration = str(self.treatment_concentration)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WellReading(YAMLRoot):
    """
    Per-well measurement data. NOT a standalone database table; embedded structured entries under
    PlateProduct.well_readings.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["WellReading"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:WellReading"
    class_name: ClassVar[str] = "WellReading"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.WellReading

    position: str = None
    value: float = None
    flag: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.position):
            self.MissingRequiredField("position")
        if not isinstance(self.position, str):
            self.position = str(self.position)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, float):
            self.value = float(self.value)

        if self.flag is not None and not isinstance(self.flag, str):
            self.flag = str(self.flag)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NucleotideSequencing(DataGenerationActivity):
    """
    A lab activity in which DNA or RNA that was extracted from a sample is sequenced.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["NucleotideSequencing"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:NucleotideSequencing"
    class_name: ClassVar[str] = "NucleotideSequencing"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.NucleotideSequencing

    id: Union[str, NucleotideSequencingId] = None
    name: str = None
    acquisition_start_time: Union[str, XSDDateTime] = None
    acquisition_end_time: Union[str, XSDDateTime] = None
    nucleotide_sequencing_category: Optional[Union[str, "NucleotideSequencingEnum"]] = None
    external_identifiers: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NucleotideSequencingId):
            self.id = NucleotideSequencingId(self.id)

        if self.nucleotide_sequencing_category is not None and not isinstance(self.nucleotide_sequencing_category, NucleotideSequencingEnum):
            self.nucleotide_sequencing_category = NucleotideSequencingEnum(self.nucleotide_sequencing_category)

        if not isinstance(self.external_identifiers, list):
            self.external_identifiers = [self.external_identifiers] if self.external_identifiers is not None else []
        self.external_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.external_identifiers]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NucleotideSequencingInstrumentData(InstrumentData):
    """
    Data generated by a nucleotide sequencing instrument (e.g., raw FASTQ files).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["NucleotideSequencingInstrumentData"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:NucleotideSequencingInstrumentData"
    class_name: ClassVar[str] = "NucleotideSequencingInstrumentData"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.NucleotideSequencingInstrumentData

    id: Union[str, NucleotideSequencingInstrumentDataId] = None
    name: str = None
    s3_key: str = None
    description: str = None
    produced_by_sequencing_activity: Optional[Union[str, NucleotideSequencingId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NucleotideSequencingInstrumentDataId):
            self.id = NucleotideSequencingInstrumentDataId(self.id)

        if self.produced_by_sequencing_activity is not None and not isinstance(self.produced_by_sequencing_activity, NucleotideSequencingId):
            self.produced_by_sequencing_activity = NucleotideSequencingId(self.produced_by_sequencing_activity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MetagenomicsProduct(ProcessedData):
    """
    Abstract base for all metagenomics data products.
    Inherits S3/file slots from dataProduct (via processedData is_a chain).
    Concrete sub-types (Annotation, Binning, GenePhylogeny) use is_a to inherit
    and add only their type-specific slots.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["MetagenomicsProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:MetagenomicsProduct"
    class_name: ClassVar[str] = "MetagenomicsProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.MetagenomicsProduct

    id: Union[str, MetagenomicsProductId] = None
    name: str = None
    s3_key: str = None
    mg_workflow_step: Optional[Union[str, "MetagenomicsSteps"]] = None
    sample_id: Optional[Union[str, SampleId]] = None
    provider_name: Optional[Union[str, ControlledTermValueId]] = None
    raw_fasta_url: Optional[str] = None
    additional_information: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.mg_workflow_step is not None and not isinstance(self.mg_workflow_step, MetagenomicsSteps):
            self.mg_workflow_step = MetagenomicsSteps(self.mg_workflow_step)

        if self.sample_id is not None and not isinstance(self.sample_id, SampleId):
            self.sample_id = SampleId(self.sample_id)

        if self.provider_name is not None and not isinstance(self.provider_name, ControlledTermValueId):
            self.provider_name = ControlledTermValueId(self.provider_name)

        if self.raw_fasta_url is not None and not isinstance(self.raw_fasta_url, str):
            self.raw_fasta_url = str(self.raw_fasta_url)

        if self.additional_information is not None and not isinstance(self.additional_information, str):
            self.additional_information = str(self.additional_information)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MetagenomicsAnnotationProduct(MetagenomicsProduct):
    """
    Top-level archive for functional annotation outputs (zip/tar stored in MinIO).
    Inherits all MetagenomicsProduct and dataProduct slots.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["MetagenomicsAnnotationProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:MetagenomicsAnnotationProduct"
    class_name: ClassVar[str] = "Metagenomics_AnnotationProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.MetagenomicsAnnotationProduct

    id: Union[str, MetagenomicsAnnotationProductId] = None
    name: str = None
    s3_key: str = None
    annotation_database: Optional[Union[str, "AnnotationDatabaseEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetagenomicsAnnotationProductId):
            self.id = MetagenomicsAnnotationProductId(self.id)

        if self.annotation_database is not None and not isinstance(self.annotation_database, AnnotationDatabaseEnum):
            self.annotation_database = AnnotationDatabaseEnum(self.annotation_database)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MetagenomicsBinningProduct(MetagenomicsProduct):
    """
    Top-level archive (zip/tar) for binning results stored in MinIO.
    Inherits all MetagenomicsProduct and dataProduct slots.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["MetagenomicsBinningProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:MetagenomicsBinningProduct"
    class_name: ClassVar[str] = "Metagenomics_BinningProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.MetagenomicsBinningProduct

    id: Union[str, MetagenomicsBinningProductId] = None
    name: str = None
    s3_key: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetagenomicsBinningProductId):
            self.id = MetagenomicsBinningProductId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MetagenomicsGenePhylogenyProduct(MetagenomicsProduct):
    """
    Top-level archive for gene-based phylogeny outputs (zip/tar stored in MinIO).
    Inherits all MetagenomicsProduct and dataProduct slots.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["MetagenomicsGenePhylogenyProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:MetagenomicsGenePhylogenyProduct"
    class_name: ClassVar[str] = "Metagenomics_GenePhylogenyProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.MetagenomicsGenePhylogenyProduct

    id: Union[str, MetagenomicsGenePhylogenyProductId] = None
    name: str = None
    s3_key: str = None
    gene_family: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetagenomicsGenePhylogenyProductId):
            self.id = MetagenomicsGenePhylogenyProductId(self.id)

        if self.gene_family is not None and not isinstance(self.gene_family, str):
            self.gene_family = str(self.gene_family)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MetagenomicsDataProcessingActivity(DataProcessingActivity):
    """
    Concrete metagenomics workflow run. Inherits all DataProcessingActivity
    slots including parent_workflow_id (chain link) and workflow_steps
    (key-value, schema TBD). Specific workflow step type is captured via the
    inherited type attribute (string); expected values:
    'metagenomics_annotation', 'metagenomics_binning', 'metagenomics_phylogeny'.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["MetagenomicsDataProcessingActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:MetagenomicsDataProcessingActivity"
    class_name: ClassVar[str] = "MetagenomicsDataProcessingActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.MetagenomicsDataProcessingActivity

    id: Union[str, MetagenomicsDataProcessingActivityId] = None
    started_at_time: Union[str, XSDDateTime] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetagenomicsDataProcessingActivityId):
            self.id = MetagenomicsDataProcessingActivityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Method(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["Method"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:Method"
    class_name: ClassVar[str] = "Method"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.Method

    analytic: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.analytic):
            self.MissingRequiredField("analytic")
        if not isinstance(self.analytic, str):
            self.analytic = str(self.analytic)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BulkDensityMethod(Method):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["BulkDensityMethod"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:BulkDensityMethod"
    class_name: ClassVar[str] = "BulkDensityMethod"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.BulkDensityMethod

    analytic: str = None

@dataclass(repr=False)
class ElementalAnalysisMethod(Method):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["ElementalAnalysisMethod"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:ElementalAnalysisMethod"
    class_name: ClassVar[str] = "ElementalAnalysisMethod"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.ElementalAnalysisMethod

    analytic: str = None

@dataclass(repr=False)
class EnzymeActivityMethod(Method):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["EnzymeActivityMethod"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:EnzymeActivityMethod"
    class_name: ClassVar[str] = "EnzymeActivityMethod"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.EnzymeActivityMethod

    analytic: str = None
    location: str = None
    incubation_temp_c: Optional[float] = None
    incubation_time: Optional[str] = None
    wavelength: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.location):
            self.MissingRequiredField("location")
        if not isinstance(self.location, str):
            self.location = str(self.location)

        if self.incubation_temp_c is not None and not isinstance(self.incubation_temp_c, float):
            self.incubation_temp_c = float(self.incubation_temp_c)

        if self.incubation_time is not None and not isinstance(self.incubation_time, str):
            self.incubation_time = str(self.incubation_time)

        if self.wavelength is not None and not isinstance(self.wavelength, float):
            self.wavelength = float(self.wavelength)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GravimetricWaterContentMethod(Method):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["GravimetricWaterContentMethod"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:GravimetricWaterContentMethod"
    class_name: ClassVar[str] = "GravimetricWaterContentMethod"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.GravimetricWaterContentMethod

    analytic: str = None
    location: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.location):
            self.MissingRequiredField("location")
        if not isinstance(self.location, str):
            self.location = str(self.location)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HydraulicPropertiesMethod(Method):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["HydraulicPropertiesMethod"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:HydraulicPropertiesMethod"
    class_name: ClassVar[str] = "HydraulicPropertiesMethod"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.HydraulicPropertiesMethod

    analytic: str = None
    location: str = None
    fitting_model: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.location):
            self.MissingRequiredField("location")
        if not isinstance(self.location, str):
            self.location = str(self.location)

        if self._is_empty(self.fitting_model):
            self.MissingRequiredField("fitting_model")
        if not isinstance(self.fitting_model, str):
            self.fitting_model = str(self.fitting_model)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KuoMethod(Method):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["KuoMethod"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:KuoMethod"
    class_name: ClassVar[str] = "KuoMethod"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.KuoMethod

    analytic: str = None
    location: str = None
    detection_limit: str = None
    method: Optional[str] = None
    wavelength: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.location):
            self.MissingRequiredField("location")
        if not isinstance(self.location, str):
            self.location = str(self.location)

        if self._is_empty(self.detection_limit):
            self.MissingRequiredField("detection_limit")
        if not isinstance(self.detection_limit, str):
            self.detection_limit = str(self.detection_limit)

        if self.method is not None and not isinstance(self.method, str):
            self.method = str(self.method)

        if self.wavelength is not None and not isinstance(self.wavelength, str):
            self.wavelength = str(self.wavelength)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MicrobialBiomassMethod(Method):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["MicrobialBiomassMethod"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:MicrobialBiomassMethod"
    class_name: ClassVar[str] = "MicrobialBiomassMethod"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.MicrobialBiomassMethod

    analytic: str = None
    location: str = None
    detector: str = None
    injection_volume: str = None
    sample_volume: str = None
    number_of_injections: float = None
    check_standard_spacing: str = None
    mode: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.location):
            self.MissingRequiredField("location")
        if not isinstance(self.location, str):
            self.location = str(self.location)

        if self._is_empty(self.detector):
            self.MissingRequiredField("detector")
        if not isinstance(self.detector, str):
            self.detector = str(self.detector)

        if self._is_empty(self.injection_volume):
            self.MissingRequiredField("injection_volume")
        if not isinstance(self.injection_volume, str):
            self.injection_volume = str(self.injection_volume)

        if self._is_empty(self.sample_volume):
            self.MissingRequiredField("sample_volume")
        if not isinstance(self.sample_volume, str):
            self.sample_volume = str(self.sample_volume)

        if self._is_empty(self.number_of_injections):
            self.MissingRequiredField("number_of_injections")
        if not isinstance(self.number_of_injections, float):
            self.number_of_injections = float(self.number_of_injections)

        if self._is_empty(self.check_standard_spacing):
            self.MissingRequiredField("check_standard_spacing")
        if not isinstance(self.check_standard_spacing, str):
            self.check_standard_spacing = str(self.check_standard_spacing)

        if self.mode is not None and not isinstance(self.mode, str):
            self.mode = str(self.mode)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PHMethod(Method):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["PHMethod"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:PHMethod"
    class_name: ClassVar[str] = "PH_Method"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.PHMethod

    analytic: str = None
    location: str = None
    calibration: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.location):
            self.MissingRequiredField("location")
        if not isinstance(self.location, str):
            self.location = str(self.location)

        if self._is_empty(self.calibration):
            self.MissingRequiredField("calibration")
        if not isinstance(self.calibration, str):
            self.calibration = str(self.calibration)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RespirationMethod(Method):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["RespirationMethod"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:RespirationMethod"
    class_name: ClassVar[str] = "RespirationMethod"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.RespirationMethod

    analytic: str = None

@dataclass(repr=False)
class TOCTNMethod(Method):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["TOCTNMethod"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:TOCTNMethod"
    class_name: ClassVar[str] = "TOC_TN_Method"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.TOCTNMethod

    analytic: str = None
    location: str = None
    detector: str = None
    injection_volume: str = None
    sample_volume: str = None
    number_of_injections: float = None
    column: Optional[str] = None
    mode: Optional[str] = None
    check_standard_spacing: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.location):
            self.MissingRequiredField("location")
        if not isinstance(self.location, str):
            self.location = str(self.location)

        if self._is_empty(self.detector):
            self.MissingRequiredField("detector")
        if not isinstance(self.detector, str):
            self.detector = str(self.detector)

        if self._is_empty(self.injection_volume):
            self.MissingRequiredField("injection_volume")
        if not isinstance(self.injection_volume, str):
            self.injection_volume = str(self.injection_volume)

        if self._is_empty(self.sample_volume):
            self.MissingRequiredField("sample_volume")
        if not isinstance(self.sample_volume, str):
            self.sample_volume = str(self.sample_volume)

        if self._is_empty(self.number_of_injections):
            self.MissingRequiredField("number_of_injections")
        if not isinstance(self.number_of_injections, float):
            self.number_of_injections = float(self.number_of_injections)

        if self.column is not None and not isinstance(self.column, str):
            self.column = str(self.column)

        if self.mode is not None and not isinstance(self.mode, str):
            self.mode = str(self.mode)

        if self.check_standard_spacing is not None and not isinstance(self.check_standard_spacing, str):
            self.check_standard_spacing = str(self.check_standard_spacing)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TextureMethod(Method):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["TextureMethod"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:TextureMethod"
    class_name: ClassVar[str] = "TextureMethod"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.TextureMethod

    analytic: str = None
    location: str = None
    method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.location):
            self.MissingRequiredField("location")
        if not isinstance(self.location, str):
            self.location = str(self.location)

        if self.method is not None and not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class XrayComputedTomographyMethod(Method):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["XrayComputedTomographyMethod"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:XrayComputedTomographyMethod"
    class_name: ClassVar[str] = "XrayComputedTomographyMethod"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.XrayComputedTomographyMethod

    analytic: str = None
    location: str = None
    x_ray_power: str = None
    cu_filter: str = None
    total_projections_collected: float = None
    rotation: str = None
    frames_recording_per_projection: float = None
    exposure_time_per_frame: str = None
    image_voxel_size_is: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.location):
            self.MissingRequiredField("location")
        if not isinstance(self.location, str):
            self.location = str(self.location)

        if self._is_empty(self.x_ray_power):
            self.MissingRequiredField("x_ray_power")
        if not isinstance(self.x_ray_power, str):
            self.x_ray_power = str(self.x_ray_power)

        if self._is_empty(self.cu_filter):
            self.MissingRequiredField("cu_filter")
        if not isinstance(self.cu_filter, str):
            self.cu_filter = str(self.cu_filter)

        if self._is_empty(self.total_projections_collected):
            self.MissingRequiredField("total_projections_collected")
        if not isinstance(self.total_projections_collected, float):
            self.total_projections_collected = float(self.total_projections_collected)

        if self._is_empty(self.rotation):
            self.MissingRequiredField("rotation")
        if not isinstance(self.rotation, str):
            self.rotation = str(self.rotation)

        if self._is_empty(self.frames_recording_per_projection):
            self.MissingRequiredField("frames_recording_per_projection")
        if not isinstance(self.frames_recording_per_projection, float):
            self.frames_recording_per_projection = float(self.frames_recording_per_projection)

        if self._is_empty(self.exposure_time_per_frame):
            self.MissingRequiredField("exposure_time_per_frame")
        if not isinstance(self.exposure_time_per_frame, str):
            self.exposure_time_per_frame = str(self.exposure_time_per_frame)

        if self._is_empty(self.image_voxel_size_is):
            self.MissingRequiredField("image_voxel_size_is")
        if not isinstance(self.image_voxel_size_is, str):
            self.image_voxel_size_is = str(self.image_voxel_size_is)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BulkDensityProduct(ProcessedData):
    """
    Bulk density analysis product, typically derived via oven-drying and weighing of a known volume of soil.
    One row per sample with columns for bulk density and QC flag.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["BulkDensityProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:BulkDensityProduct"
    class_name: ClassVar[str] = "BulkDensityProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.BulkDensityProduct

    id: Union[str, BulkDensityProductId] = None
    name: str = None
    s3_key: str = None
    measure_type: Optional[Union[str, "ProductMeasureType"]] = None
    bulk_density_id: Optional[Union[str, QuantityValueId]] = None
    flag: Optional[Union[str, "ProcessedDataFlag"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BulkDensityProductId):
            self.id = BulkDensityProductId(self.id)

        if self.measure_type is not None and not isinstance(self.measure_type, ProductMeasureType):
            self.measure_type = ProductMeasureType(self.measure_type)

        if self.bulk_density_id is not None and not isinstance(self.bulk_density_id, QuantityValueId):
            self.bulk_density_id = QuantityValueId(self.bulk_density_id)

        if self.flag is not None and not isinstance(self.flag, ProcessedDataFlag):
            self.flag = ProcessedDataFlag(self.flag)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElementalAnalysisProduct(ProcessedData):
    """
    Elemental analysis product, typically derived via combustion or similar instrument.
    One row per sample with columns for total carbon, total nitrogen, total Kjeldahl nitrogen, and total sulfur.
    Individual QC flags for each measurement using ProcessedDataFlag enum.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["ElementalAnalysisProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:ElementalAnalysisProduct"
    class_name: ClassVar[str] = "ElementalAnalysisProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.ElementalAnalysisProduct

    id: Union[str, ElementalAnalysisProductId] = None
    name: str = None
    s3_key: str = None
    measure_type: Optional[Union[str, "ProductMeasureType"]] = None
    total_carbon_id: Optional[Union[str, QuantityValueId]] = None
    total_nitrogen_id: Optional[Union[str, QuantityValueId]] = None
    total_kjeldahl_nitrogen_id: Optional[Union[str, QuantityValueId]] = None
    total_sulfur_id: Optional[Union[str, QuantityValueId]] = None
    flag_total_carbon: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_total_nitrogen: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_tkn: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_total_sulfur: Optional[Union[str, "ProcessedDataFlag"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ElementalAnalysisProductId):
            self.id = ElementalAnalysisProductId(self.id)

        if self.measure_type is not None and not isinstance(self.measure_type, ProductMeasureType):
            self.measure_type = ProductMeasureType(self.measure_type)

        if self.total_carbon_id is not None and not isinstance(self.total_carbon_id, QuantityValueId):
            self.total_carbon_id = QuantityValueId(self.total_carbon_id)

        if self.total_nitrogen_id is not None and not isinstance(self.total_nitrogen_id, QuantityValueId):
            self.total_nitrogen_id = QuantityValueId(self.total_nitrogen_id)

        if self.total_kjeldahl_nitrogen_id is not None and not isinstance(self.total_kjeldahl_nitrogen_id, QuantityValueId):
            self.total_kjeldahl_nitrogen_id = QuantityValueId(self.total_kjeldahl_nitrogen_id)

        if self.total_sulfur_id is not None and not isinstance(self.total_sulfur_id, QuantityValueId):
            self.total_sulfur_id = QuantityValueId(self.total_sulfur_id)

        if self.flag_total_carbon is not None and not isinstance(self.flag_total_carbon, ProcessedDataFlag):
            self.flag_total_carbon = ProcessedDataFlag(self.flag_total_carbon)

        if self.flag_total_nitrogen is not None and not isinstance(self.flag_total_nitrogen, ProcessedDataFlag):
            self.flag_total_nitrogen = ProcessedDataFlag(self.flag_total_nitrogen)

        if self.flag_tkn is not None and not isinstance(self.flag_tkn, ProcessedDataFlag):
            self.flag_tkn = ProcessedDataFlag(self.flag_tkn)

        if self.flag_total_sulfur is not None and not isinstance(self.flag_total_sulfur, ProcessedDataFlag):
            self.flag_total_sulfur = ProcessedDataFlag(self.flag_total_sulfur)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnzymeProduct(ProcessedData):
    """
    Enzyme activity analysis product, typically derived via colorimetric assay of soil extracts.
    One row per sample with columns for beta-glucosidase activity and QC flag.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["EnzymeProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:EnzymeProduct"
    class_name: ClassVar[str] = "EnzymeProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.EnzymeProduct

    id: Union[str, EnzymeProductId] = None
    name: str = None
    s3_key: str = None
    measure_type: Optional[Union[str, "ProductMeasureType"]] = None
    beta_glucosidase_ug_pnp_per_g_per_h_id: Optional[Union[str, QuantityValueId]] = None
    flag: Optional[Union[str, "ProcessedDataFlag"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnzymeProductId):
            self.id = EnzymeProductId(self.id)

        if self.measure_type is not None and not isinstance(self.measure_type, ProductMeasureType):
            self.measure_type = ProductMeasureType(self.measure_type)

        if self.beta_glucosidase_ug_pnp_per_g_per_h_id is not None and not isinstance(self.beta_glucosidase_ug_pnp_per_g_per_h_id, QuantityValueId):
            self.beta_glucosidase_ug_pnp_per_g_per_h_id = QuantityValueId(self.beta_glucosidase_ug_pnp_per_g_per_h_id)

        if self.flag is not None and not isinstance(self.flag, ProcessedDataFlag):
            self.flag = ProcessedDataFlag(self.flag)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GWCMoistureProduct(ProcessedData):
    """
    Gravimetric water content (GWC) analysis product, typically derived via oven-drying and weighing of a known mass
    of soil.
    One row per sample with columns for GWC and QC flag.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["GWCMoistureProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:GWCMoistureProduct"
    class_name: ClassVar[str] = "GWCMoistureProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.GWCMoistureProduct

    id: Union[str, GWCMoistureProductId] = None
    name: str = None
    s3_key: str = None
    measure_type: Optional[Union[str, "ProductMeasureType"]] = None
    gwc_percent_id: Optional[Union[str, QuantityValueId]] = None
    flag: Optional[Union[str, "ProcessedDataFlag"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GWCMoistureProductId):
            self.id = GWCMoistureProductId(self.id)

        if self.measure_type is not None and not isinstance(self.measure_type, ProductMeasureType):
            self.measure_type = ProductMeasureType(self.measure_type)

        if self.gwc_percent_id is not None and not isinstance(self.gwc_percent_id, QuantityValueId):
            self.gwc_percent_id = QuantityValueId(self.gwc_percent_id)

        if self.flag is not None and not isinstance(self.flag, ProcessedDataFlag):
            self.flag = ProcessedDataFlag(self.flag)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HydraulicPropertiesProduct(ProcessedData):
    """
    Soil hydraulic parameters derived from HYPROP evaporation-experiment data. One row per core section; the four
    attributes are the four VGM model parameters. Proposal_ID, sampling_set, and core_section are inherited from the
    parent processedData record.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["HydraulicPropertiesProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:HydraulicPropertiesProduct"
    class_name: ClassVar[str] = "HydraulicPropertiesProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.HydraulicPropertiesProduct

    id: Union[str, HydraulicPropertiesProductId] = None
    name: str = None
    s3_key: str = None
    measure_type: Optional[Union[str, "ProductMeasureType"]] = None
    alpha: Optional[float] = None
    n: Optional[float] = None
    theta_r: Optional[float] = None
    theta_s: Optional[float] = None
    flag: Optional[Union[str, "ProcessedDataFlag"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HydraulicPropertiesProductId):
            self.id = HydraulicPropertiesProductId(self.id)

        if self.measure_type is not None and not isinstance(self.measure_type, ProductMeasureType):
            self.measure_type = ProductMeasureType(self.measure_type)

        if self.alpha is not None and not isinstance(self.alpha, float):
            self.alpha = float(self.alpha)

        if self.n is not None and not isinstance(self.n, float):
            self.n = float(self.n)

        if self.theta_r is not None and not isinstance(self.theta_r, float):
            self.theta_r = float(self.theta_r)

        if self.theta_s is not None and not isinstance(self.theta_s, float):
            self.theta_s = float(self.theta_s)

        if self.flag is not None and not isinstance(self.flag, ProcessedDataFlag):
            self.flag = ProcessedDataFlag(self.flag)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IonsAnalysisProduct(ProcessedData):
    """
    Ions analysis product, typically derived via ICP-OES or similar instrument.
    One row per sample with columns for each ion measured.
    Individual QC flags for each ion using ProcessedDataFlag enum.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["IonsAnalysisProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:IonsAnalysisProduct"
    class_name: ClassVar[str] = "IonsAnalysisProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.IonsAnalysisProduct

    id: Union[str, IonsAnalysisProductId] = None
    name: str = None
    s3_key: str = None
    measure_type: Optional[Union[str, "ProductMeasureType"]] = None
    sulfate_id: Optional[Union[str, QuantityValueId]] = None
    boron_id: Optional[Union[str, QuantityValueId]] = None
    zinc_id: Optional[Union[str, QuantityValueId]] = None
    manganate_id: Optional[Union[str, QuantityValueId]] = None
    copper_id: Optional[Union[str, QuantityValueId]] = None
    iron_id: Optional[Union[str, QuantityValueId]] = None
    calcium_id: Optional[Union[str, QuantityValueId]] = None
    magnesium_id: Optional[Union[str, QuantityValueId]] = None
    sodium_id: Optional[Union[str, QuantityValueId]] = None
    potassium_id: Optional[Union[str, QuantityValueId]] = None
    total_bases_id: Optional[Union[str, QuantityValueId]] = None
    cation_exchange_capacity_id: Optional[Union[str, QuantityValueId]] = None
    flag_sulfate: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_boron: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_zinc: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_manganate: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_copper: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_iron: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_calcium: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_magnesium: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_sodium: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_potassium: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_total_bases: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_cec: Optional[Union[str, "ProcessedDataFlag"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IonsAnalysisProductId):
            self.id = IonsAnalysisProductId(self.id)

        if self.measure_type is not None and not isinstance(self.measure_type, ProductMeasureType):
            self.measure_type = ProductMeasureType(self.measure_type)

        if self.sulfate_id is not None and not isinstance(self.sulfate_id, QuantityValueId):
            self.sulfate_id = QuantityValueId(self.sulfate_id)

        if self.boron_id is not None and not isinstance(self.boron_id, QuantityValueId):
            self.boron_id = QuantityValueId(self.boron_id)

        if self.zinc_id is not None and not isinstance(self.zinc_id, QuantityValueId):
            self.zinc_id = QuantityValueId(self.zinc_id)

        if self.manganate_id is not None and not isinstance(self.manganate_id, QuantityValueId):
            self.manganate_id = QuantityValueId(self.manganate_id)

        if self.copper_id is not None and not isinstance(self.copper_id, QuantityValueId):
            self.copper_id = QuantityValueId(self.copper_id)

        if self.iron_id is not None and not isinstance(self.iron_id, QuantityValueId):
            self.iron_id = QuantityValueId(self.iron_id)

        if self.calcium_id is not None and not isinstance(self.calcium_id, QuantityValueId):
            self.calcium_id = QuantityValueId(self.calcium_id)

        if self.magnesium_id is not None and not isinstance(self.magnesium_id, QuantityValueId):
            self.magnesium_id = QuantityValueId(self.magnesium_id)

        if self.sodium_id is not None and not isinstance(self.sodium_id, QuantityValueId):
            self.sodium_id = QuantityValueId(self.sodium_id)

        if self.potassium_id is not None and not isinstance(self.potassium_id, QuantityValueId):
            self.potassium_id = QuantityValueId(self.potassium_id)

        if self.total_bases_id is not None and not isinstance(self.total_bases_id, QuantityValueId):
            self.total_bases_id = QuantityValueId(self.total_bases_id)

        if self.cation_exchange_capacity_id is not None and not isinstance(self.cation_exchange_capacity_id, QuantityValueId):
            self.cation_exchange_capacity_id = QuantityValueId(self.cation_exchange_capacity_id)

        if self.flag_sulfate is not None and not isinstance(self.flag_sulfate, ProcessedDataFlag):
            self.flag_sulfate = ProcessedDataFlag(self.flag_sulfate)

        if self.flag_boron is not None and not isinstance(self.flag_boron, ProcessedDataFlag):
            self.flag_boron = ProcessedDataFlag(self.flag_boron)

        if self.flag_zinc is not None and not isinstance(self.flag_zinc, ProcessedDataFlag):
            self.flag_zinc = ProcessedDataFlag(self.flag_zinc)

        if self.flag_manganate is not None and not isinstance(self.flag_manganate, ProcessedDataFlag):
            self.flag_manganate = ProcessedDataFlag(self.flag_manganate)

        if self.flag_copper is not None and not isinstance(self.flag_copper, ProcessedDataFlag):
            self.flag_copper = ProcessedDataFlag(self.flag_copper)

        if self.flag_iron is not None and not isinstance(self.flag_iron, ProcessedDataFlag):
            self.flag_iron = ProcessedDataFlag(self.flag_iron)

        if self.flag_calcium is not None and not isinstance(self.flag_calcium, ProcessedDataFlag):
            self.flag_calcium = ProcessedDataFlag(self.flag_calcium)

        if self.flag_magnesium is not None and not isinstance(self.flag_magnesium, ProcessedDataFlag):
            self.flag_magnesium = ProcessedDataFlag(self.flag_magnesium)

        if self.flag_sodium is not None and not isinstance(self.flag_sodium, ProcessedDataFlag):
            self.flag_sodium = ProcessedDataFlag(self.flag_sodium)

        if self.flag_potassium is not None and not isinstance(self.flag_potassium, ProcessedDataFlag):
            self.flag_potassium = ProcessedDataFlag(self.flag_potassium)

        if self.flag_total_bases is not None and not isinstance(self.flag_total_bases, ProcessedDataFlag):
            self.flag_total_bases = ProcessedDataFlag(self.flag_total_bases)

        if self.flag_cec is not None and not isinstance(self.flag_cec, ProcessedDataFlag):
            self.flag_cec = ProcessedDataFlag(self.flag_cec)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MAOMProduct(YAMLRoot):
    """
    Mineral-Associated Organic Matter (MAOM) analysis product, typically derived via HCl extraction and TOC/TN
    measurement.
    One row per sample with columns for total organic carbon and total nitrogen.
    Individual QC flags for each measurement using ProcessedDataFlag enum. TO BE RENAMED TO HClExtOMProduct
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["MAOMProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:MAOMProduct"
    class_name: ClassVar[str] = "MAOMProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.MAOMProduct

    id: Union[str, MAOMProductId] = None
    measure_type: Optional[Union[str, "ProductMeasureType"]] = None
    replicate: Optional[int] = None
    total_organic_carbon_id: Optional[Union[str, QuantityValueId]] = None
    total_organic_carbon_avg: Optional[float] = None
    total_nitrogen_id: Optional[Union[str, QuantityValueId]] = None
    total_nitrogen_avg: Optional[float] = None
    flag_toc: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_tn: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_toc_avg: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_tn_avg: Optional[Union[str, "ProcessedDataFlag"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MAOMProductId):
            self.id = MAOMProductId(self.id)

        if self.measure_type is not None and not isinstance(self.measure_type, ProductMeasureType):
            self.measure_type = ProductMeasureType(self.measure_type)

        if self.replicate is not None and not isinstance(self.replicate, int):
            self.replicate = int(self.replicate)

        if self.total_organic_carbon_id is not None and not isinstance(self.total_organic_carbon_id, QuantityValueId):
            self.total_organic_carbon_id = QuantityValueId(self.total_organic_carbon_id)

        if self.total_organic_carbon_avg is not None and not isinstance(self.total_organic_carbon_avg, float):
            self.total_organic_carbon_avg = float(self.total_organic_carbon_avg)

        if self.total_nitrogen_id is not None and not isinstance(self.total_nitrogen_id, QuantityValueId):
            self.total_nitrogen_id = QuantityValueId(self.total_nitrogen_id)

        if self.total_nitrogen_avg is not None and not isinstance(self.total_nitrogen_avg, float):
            self.total_nitrogen_avg = float(self.total_nitrogen_avg)

        if self.flag_toc is not None and not isinstance(self.flag_toc, ProcessedDataFlag):
            self.flag_toc = ProcessedDataFlag(self.flag_toc)

        if self.flag_tn is not None and not isinstance(self.flag_tn, ProcessedDataFlag):
            self.flag_tn = ProcessedDataFlag(self.flag_tn)

        if self.flag_toc_avg is not None and not isinstance(self.flag_toc_avg, ProcessedDataFlag):
            self.flag_toc_avg = ProcessedDataFlag(self.flag_toc_avg)

        if self.flag_tn_avg is not None and not isinstance(self.flag_tn_avg, ProcessedDataFlag):
            self.flag_tn_avg = ProcessedDataFlag(self.flag_tn_avg)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MicrobialBiomassProduct(ProcessedData):
    """
    Microbial biomass analysis product, typically derived via chloroform fumigation-extraction (CFE) or similar
    instrument.
    One row per sample with columns for microbial biomass carbon and nitrogen.
    Individual QC flags for each measurement using ProcessedDataFlag enum.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["MicrobialBiomassProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:MicrobialBiomassProduct"
    class_name: ClassVar[str] = "MicrobialBiomassProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.MicrobialBiomassProduct

    id: Union[str, MicrobialBiomassProductId] = None
    name: str = None
    s3_key: str = None
    measure_type: Optional[Union[str, "ProductMeasureType"]] = None
    replicate: Optional[int] = None
    mbc_id: Optional[Union[str, QuantityValueId]] = None
    mbc_avg: Optional[float] = None
    mbn_id: Optional[Union[str, QuantityValueId]] = None
    mbn_avg: Optional[float] = None
    flag_mbc: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_mbn: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_mbc_avg: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_mbn_avg: Optional[Union[str, "ProcessedDataFlag"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MicrobialBiomassProductId):
            self.id = MicrobialBiomassProductId(self.id)

        if self.measure_type is not None and not isinstance(self.measure_type, ProductMeasureType):
            self.measure_type = ProductMeasureType(self.measure_type)

        if self.replicate is not None and not isinstance(self.replicate, int):
            self.replicate = int(self.replicate)

        if self.mbc_id is not None and not isinstance(self.mbc_id, QuantityValueId):
            self.mbc_id = QuantityValueId(self.mbc_id)

        if self.mbc_avg is not None and not isinstance(self.mbc_avg, float):
            self.mbc_avg = float(self.mbc_avg)

        if self.mbn_id is not None and not isinstance(self.mbn_id, QuantityValueId):
            self.mbn_id = QuantityValueId(self.mbn_id)

        if self.mbn_avg is not None and not isinstance(self.mbn_avg, float):
            self.mbn_avg = float(self.mbn_avg)

        if self.flag_mbc is not None and not isinstance(self.flag_mbc, ProcessedDataFlag):
            self.flag_mbc = ProcessedDataFlag(self.flag_mbc)

        if self.flag_mbn is not None and not isinstance(self.flag_mbn, ProcessedDataFlag):
            self.flag_mbn = ProcessedDataFlag(self.flag_mbn)

        if self.flag_mbc_avg is not None and not isinstance(self.flag_mbc_avg, ProcessedDataFlag):
            self.flag_mbc_avg = ProcessedDataFlag(self.flag_mbc_avg)

        if self.flag_mbn_avg is not None and not isinstance(self.flag_mbn_avg, ProcessedDataFlag):
            self.flag_mbn_avg = ProcessedDataFlag(self.flag_mbn_avg)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NitrogenAnalysisProduct(ProcessedData):
    """
    Nitrogen analysis product, typically derived via colorimetric assay of soil extracts.
    One row per sample with columns for nitrate and ammonium concentrations.
    Individual QC flags for each measurement using ProcessedDataFlag enum.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["NitrogenAnalysisProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:NitrogenAnalysisProduct"
    class_name: ClassVar[str] = "NitrogenAnalysisProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.NitrogenAnalysisProduct

    id: Union[str, NitrogenAnalysisProductId] = None
    name: str = None
    s3_key: str = None
    measure_type: Optional[Union[str, "ProductMeasureType"]] = None
    replicate: Optional[int] = None
    no3_n_id: Optional[Union[str, QuantityValueId]] = None
    no3_n_avg: Optional[float] = None
    nh4_n_id: Optional[Union[str, QuantityValueId]] = None
    nh4_n_avg: Optional[float] = None
    flag_no3n: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_nh4n: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_no3n_avg: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_nh4n_avg: Optional[Union[str, "ProcessedDataFlag"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NitrogenAnalysisProductId):
            self.id = NitrogenAnalysisProductId(self.id)

        if self.measure_type is not None and not isinstance(self.measure_type, ProductMeasureType):
            self.measure_type = ProductMeasureType(self.measure_type)

        if self.replicate is not None and not isinstance(self.replicate, int):
            self.replicate = int(self.replicate)

        if self.no3_n_id is not None and not isinstance(self.no3_n_id, QuantityValueId):
            self.no3_n_id = QuantityValueId(self.no3_n_id)

        if self.no3_n_avg is not None and not isinstance(self.no3_n_avg, float):
            self.no3_n_avg = float(self.no3_n_avg)

        if self.nh4_n_id is not None and not isinstance(self.nh4_n_id, QuantityValueId):
            self.nh4_n_id = QuantityValueId(self.nh4_n_id)

        if self.nh4_n_avg is not None and not isinstance(self.nh4_n_avg, float):
            self.nh4_n_avg = float(self.nh4_n_avg)

        if self.flag_no3n is not None and not isinstance(self.flag_no3n, ProcessedDataFlag):
            self.flag_no3n = ProcessedDataFlag(self.flag_no3n)

        if self.flag_nh4n is not None and not isinstance(self.flag_nh4n, ProcessedDataFlag):
            self.flag_nh4n = ProcessedDataFlag(self.flag_nh4n)

        if self.flag_no3n_avg is not None and not isinstance(self.flag_no3n_avg, ProcessedDataFlag):
            self.flag_no3n_avg = ProcessedDataFlag(self.flag_no3n_avg)

        if self.flag_nh4n_avg is not None and not isinstance(self.flag_nh4n_avg, ProcessedDataFlag):
            self.flag_nh4n_avg = ProcessedDataFlag(self.flag_nh4n_avg)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhosphorusAnalysisProduct(ProcessedData):
    """
    Phosphorus analysis product, typically derived via colorimetric assay of soil extracts.
    One row per sample with columns for phosphorus concentration.
    Individual QC flags for each measurement using ProcessedDataFlag enum.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["PhosphorusAnalysisProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:PhosphorusAnalysisProduct"
    class_name: ClassVar[str] = "PhosphorusAnalysisProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.PhosphorusAnalysisProduct

    id: Union[str, PhosphorusAnalysisProductId] = None
    name: str = None
    s3_key: str = None
    measure_type: Optional[Union[str, "ProductMeasureType"]] = None
    replicate: Optional[int] = None
    extraction_method: Optional[str] = None
    phosphorus_id: Optional[Union[str, QuantityValueId]] = None
    phosphorus_avg: Optional[float] = None
    flag: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_avg: Optional[Union[str, "ProcessedDataFlag"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhosphorusAnalysisProductId):
            self.id = PhosphorusAnalysisProductId(self.id)

        if self.measure_type is not None and not isinstance(self.measure_type, ProductMeasureType):
            self.measure_type = ProductMeasureType(self.measure_type)

        if self.replicate is not None and not isinstance(self.replicate, int):
            self.replicate = int(self.replicate)

        if self.extraction_method is not None and not isinstance(self.extraction_method, str):
            self.extraction_method = str(self.extraction_method)

        if self.phosphorus_id is not None and not isinstance(self.phosphorus_id, QuantityValueId):
            self.phosphorus_id = QuantityValueId(self.phosphorus_id)

        if self.phosphorus_avg is not None and not isinstance(self.phosphorus_avg, float):
            self.phosphorus_avg = float(self.phosphorus_avg)

        if self.flag is not None and not isinstance(self.flag, ProcessedDataFlag):
            self.flag = ProcessedDataFlag(self.flag)

        if self.flag_avg is not None and not isinstance(self.flag_avg, ProcessedDataFlag):
            self.flag_avg = ProcessedDataFlag(self.flag_avg)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RespirationProduct(ProcessedData):
    """
    Soil respiration analysis product.
    One row per sample with columns for soil respiration and QC flag.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["RespirationProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:RespirationProduct"
    class_name: ClassVar[str] = "RespirationProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.RespirationProduct

    id: Union[str, RespirationProductId] = None
    name: str = None
    s3_key: str = None
    measure_type: Optional[Union[str, "ProductMeasureType"]] = None
    respiration_co2_c_ug_per_g: Optional[float] = None
    flag: Optional[Union[str, "ProcessedDataFlag"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RespirationProductId):
            self.id = RespirationProductId(self.id)

        if self.measure_type is not None and not isinstance(self.measure_type, ProductMeasureType):
            self.measure_type = ProductMeasureType(self.measure_type)

        if self.respiration_co2_c_ug_per_g is not None and not isinstance(self.respiration_co2_c_ug_per_g, float):
            self.respiration_co2_c_ug_per_g = float(self.respiration_co2_c_ug_per_g)

        if self.flag is not None and not isinstance(self.flag, ProcessedDataFlag):
            self.flag = ProcessedDataFlag(self.flag)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TextureProduct(ProcessedData):
    """
    Soil texture analysis product, typically derived via hydrometer or similar instrument.
    One row per sample with columns for sand, silt, and clay percentages.
    Individual QC flags for each measurement using ProcessedDataFlag enum.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["TextureProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:TextureProduct"
    class_name: ClassVar[str] = "TextureProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.TextureProduct

    id: Union[str, TextureProductId] = None
    name: str = None
    s3_key: str = None
    measure_type: Optional[Union[str, "ProductMeasureType"]] = None
    sand_pct_id: Optional[Union[str, QuantityValueId]] = None
    silt_pct_id: Optional[Union[str, QuantityValueId]] = None
    clay_pct_id: Optional[Union[str, QuantityValueId]] = None
    flag: Optional[Union[str, "ProcessedDataFlag"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TextureProductId):
            self.id = TextureProductId(self.id)

        if self.measure_type is not None and not isinstance(self.measure_type, ProductMeasureType):
            self.measure_type = ProductMeasureType(self.measure_type)

        if self.sand_pct_id is not None and not isinstance(self.sand_pct_id, QuantityValueId):
            self.sand_pct_id = QuantityValueId(self.sand_pct_id)

        if self.silt_pct_id is not None and not isinstance(self.silt_pct_id, QuantityValueId):
            self.silt_pct_id = QuantityValueId(self.silt_pct_id)

        if self.clay_pct_id is not None and not isinstance(self.clay_pct_id, QuantityValueId):
            self.clay_pct_id = QuantityValueId(self.clay_pct_id)

        if self.flag is not None and not isinstance(self.flag, ProcessedDataFlag):
            self.flag = ProcessedDataFlag(self.flag)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TomographyProduct(ProcessedData):
    """
    Soil tomography analysis product, typically derived via X-ray computed tomography (XCT) or similar instrument.
    One row per sample with columns for pore structure metrics and QC flag.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["TomographyProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:TomographyProduct"
    class_name: ClassVar[str] = "TomographyProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.TomographyProduct

    id: Union[str, TomographyProductId] = None
    name: str = None
    s3_key: str = None
    measure_type: Optional[Union[str, "ProductMeasureType"]] = None
    roi_volume_voxel: Optional[float] = None
    voxel_size: Optional[float] = None
    connected_pores: Optional[float] = None
    pore_diameter_min: Optional[float] = None
    pore_diameter_max: Optional[float] = None
    pore_diameter_mean: Optional[float] = None
    pore_diameter_median: Optional[float] = None
    pore_diameter_variance: Optional[float] = None
    pore_volume_mean: Optional[float] = None
    total_pore_volume: Optional[float] = None
    permeability_x: Optional[float] = None
    flow_rate_x: Optional[float] = None
    tortuosity_x: Optional[float] = None
    permeability_y: Optional[float] = None
    flow_rate_y: Optional[float] = None
    tortuosity_y: Optional[float] = None
    permeability_z: Optional[float] = None
    flow_rate_z: Optional[float] = None
    tortuosity_z: Optional[float] = None
    flag_xct: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TomographyProductId):
            self.id = TomographyProductId(self.id)

        if self.measure_type is not None and not isinstance(self.measure_type, ProductMeasureType):
            self.measure_type = ProductMeasureType(self.measure_type)

        if self.roi_volume_voxel is not None and not isinstance(self.roi_volume_voxel, float):
            self.roi_volume_voxel = float(self.roi_volume_voxel)

        if self.voxel_size is not None and not isinstance(self.voxel_size, float):
            self.voxel_size = float(self.voxel_size)

        if self.connected_pores is not None and not isinstance(self.connected_pores, float):
            self.connected_pores = float(self.connected_pores)

        if self.pore_diameter_min is not None and not isinstance(self.pore_diameter_min, float):
            self.pore_diameter_min = float(self.pore_diameter_min)

        if self.pore_diameter_max is not None and not isinstance(self.pore_diameter_max, float):
            self.pore_diameter_max = float(self.pore_diameter_max)

        if self.pore_diameter_mean is not None and not isinstance(self.pore_diameter_mean, float):
            self.pore_diameter_mean = float(self.pore_diameter_mean)

        if self.pore_diameter_median is not None and not isinstance(self.pore_diameter_median, float):
            self.pore_diameter_median = float(self.pore_diameter_median)

        if self.pore_diameter_variance is not None and not isinstance(self.pore_diameter_variance, float):
            self.pore_diameter_variance = float(self.pore_diameter_variance)

        if self.pore_volume_mean is not None and not isinstance(self.pore_volume_mean, float):
            self.pore_volume_mean = float(self.pore_volume_mean)

        if self.total_pore_volume is not None and not isinstance(self.total_pore_volume, float):
            self.total_pore_volume = float(self.total_pore_volume)

        if self.permeability_x is not None and not isinstance(self.permeability_x, float):
            self.permeability_x = float(self.permeability_x)

        if self.flow_rate_x is not None and not isinstance(self.flow_rate_x, float):
            self.flow_rate_x = float(self.flow_rate_x)

        if self.tortuosity_x is not None and not isinstance(self.tortuosity_x, float):
            self.tortuosity_x = float(self.tortuosity_x)

        if self.permeability_y is not None and not isinstance(self.permeability_y, float):
            self.permeability_y = float(self.permeability_y)

        if self.flow_rate_y is not None and not isinstance(self.flow_rate_y, float):
            self.flow_rate_y = float(self.flow_rate_y)

        if self.tortuosity_y is not None and not isinstance(self.tortuosity_y, float):
            self.tortuosity_y = float(self.tortuosity_y)

        if self.permeability_z is not None and not isinstance(self.permeability_z, float):
            self.permeability_z = float(self.permeability_z)

        if self.flow_rate_z is not None and not isinstance(self.flow_rate_z, float):
            self.flow_rate_z = float(self.flow_rate_z)

        if self.tortuosity_z is not None and not isinstance(self.tortuosity_z, float):
            self.tortuosity_z = float(self.tortuosity_z)

        if self.flag_xct is not None and not isinstance(self.flag_xct, str):
            self.flag_xct = str(self.flag_xct)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WEOMProduct(YAMLRoot):
    """
    Water Extractable Organic Matter (WEOM) analysis product, typically derived via Shimadzu TOC-L or similar
    instrument.
    One row per sample with columns for total organic carbon and total nitrogen.
    Individual QC flags for each measurement using ProcessedDataFlag enum.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["WEOMProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:WEOMProduct"
    class_name: ClassVar[str] = "WEOMProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.WEOMProduct

    id: Union[str, WEOMProductId] = None
    measure_type: Optional[Union[str, "ProductMeasureType"]] = None
    replicate: Optional[int] = None
    total_organic_carbon_id: Optional[Union[str, QuantityValueId]] = None
    total_organic_carbon_avg: Optional[float] = None
    total_nitrogen_id: Optional[Union[str, QuantityValueId]] = None
    total_nitrogen_avg: Optional[float] = None
    flag_toc: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_tn: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_toc_avg: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_tn_avg: Optional[Union[str, "ProcessedDataFlag"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WEOMProductId):
            self.id = WEOMProductId(self.id)

        if self.measure_type is not None and not isinstance(self.measure_type, ProductMeasureType):
            self.measure_type = ProductMeasureType(self.measure_type)

        if self.replicate is not None and not isinstance(self.replicate, int):
            self.replicate = int(self.replicate)

        if self.total_organic_carbon_id is not None and not isinstance(self.total_organic_carbon_id, QuantityValueId):
            self.total_organic_carbon_id = QuantityValueId(self.total_organic_carbon_id)

        if self.total_organic_carbon_avg is not None and not isinstance(self.total_organic_carbon_avg, float):
            self.total_organic_carbon_avg = float(self.total_organic_carbon_avg)

        if self.total_nitrogen_id is not None and not isinstance(self.total_nitrogen_id, QuantityValueId):
            self.total_nitrogen_id = QuantityValueId(self.total_nitrogen_id)

        if self.total_nitrogen_avg is not None and not isinstance(self.total_nitrogen_avg, float):
            self.total_nitrogen_avg = float(self.total_nitrogen_avg)

        if self.flag_toc is not None and not isinstance(self.flag_toc, ProcessedDataFlag):
            self.flag_toc = ProcessedDataFlag(self.flag_toc)

        if self.flag_tn is not None and not isinstance(self.flag_tn, ProcessedDataFlag):
            self.flag_tn = ProcessedDataFlag(self.flag_tn)

        if self.flag_toc_avg is not None and not isinstance(self.flag_toc_avg, ProcessedDataFlag):
            self.flag_toc_avg = ProcessedDataFlag(self.flag_toc_avg)

        if self.flag_tn_avg is not None and not isinstance(self.flag_tn_avg, ProcessedDataFlag):
            self.flag_tn_avg = ProcessedDataFlag(self.flag_tn_avg)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PHProduct(ProcessedData):
    """
    Soil pH analysis product, typically derived via pH meter or similar instrument.
    One row per sample with columns for pH and QC flag.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["PHProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:PHProduct"
    class_name: ClassVar[str] = "pHProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.PHProduct

    id: Union[str, PHProductId] = None
    name: str = None
    s3_key: str = None
    measure_type: Optional[Union[str, "ProductMeasureType"]] = None
    ph: Optional[float] = None
    flag: Optional[Union[str, "ProcessedDataFlag"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PHProductId):
            self.id = PHProductId(self.id)

        if self.measure_type is not None and not isinstance(self.measure_type, ProductMeasureType):
            self.measure_type = ProductMeasureType(self.measure_type)

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if self.flag is not None and not isinstance(self.flag, ProcessedDataFlag):
            self.flag = ProcessedDataFlag(self.flag)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
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
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["XRayDataProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:XRayDataProduct"
    class_name: ClassVar[str] = "XRayDataProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.XRayDataProduct

    id: Union[str, XRayDataProductId] = None
    name: str = None
    s3_key: str = None

@dataclass(repr=False)
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
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["XRFElementalProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:XRFElementalProduct"
    class_name: ClassVar[str] = "XRFElementalProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.XRFElementalProduct

    id: Union[str, XRFElementalProductId] = None
    name: str = None
    s3_key: str = None
    measure_type: Optional[Union[str, "ProductMeasureType"]] = None
    cl_mg_per_kg: Optional[float] = None
    v_mg_per_kg: Optional[float] = None
    cr_mg_per_kg: Optional[float] = None
    ni_mg_per_kg: Optional[float] = None
    cu_mg_per_kg: Optional[float] = None
    zn_mg_per_kg: Optional[float] = None
    ga_mg_per_kg: Optional[float] = None
    as_mg_per_kg: Optional[float] = None
    se_mg_per_kg: Optional[float] = None
    br_mg_per_kg: Optional[float] = None
    rb_mg_per_kg: Optional[float] = None
    sr_mg_per_kg: Optional[float] = None
    y_mg_per_kg: Optional[float] = None
    nb_mg_per_kg: Optional[float] = None
    mo_mg_per_kg: Optional[float] = None
    ag_mg_per_kg: Optional[float] = None
    cd_mg_per_kg: Optional[float] = None
    in_mg_per_kg: Optional[float] = None
    sn_mg_per_kg: Optional[float] = None
    sb_mg_per_kg: Optional[float] = None
    cs_mg_per_kg: Optional[float] = None
    ba_mg_per_kg: Optional[float] = None
    la_mg_per_kg: Optional[float] = None
    ce_mg_per_kg: Optional[float] = None
    pb_mg_per_kg: Optional[float] = None
    th_mg_per_kg: Optional[float] = None
    u_mg_per_kg: Optional[float] = None
    flag_cl: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_v: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_cr: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_ni: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_cu: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_zn: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_ga: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_as: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_se: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_br: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_rb: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_sr: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_y: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_nb: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_mo: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_ag: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_cd: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_in: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_sn: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_sb: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_cs: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_ba: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_la: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_ce: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_pb: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_th: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_u: Optional[Union[str, "ProcessedDataFlag"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, XRFElementalProductId):
            self.id = XRFElementalProductId(self.id)

        if self.measure_type is not None and not isinstance(self.measure_type, ProductMeasureType):
            self.measure_type = ProductMeasureType(self.measure_type)

        if self.cl_mg_per_kg is not None and not isinstance(self.cl_mg_per_kg, float):
            self.cl_mg_per_kg = float(self.cl_mg_per_kg)

        if self.v_mg_per_kg is not None and not isinstance(self.v_mg_per_kg, float):
            self.v_mg_per_kg = float(self.v_mg_per_kg)

        if self.cr_mg_per_kg is not None and not isinstance(self.cr_mg_per_kg, float):
            self.cr_mg_per_kg = float(self.cr_mg_per_kg)

        if self.ni_mg_per_kg is not None and not isinstance(self.ni_mg_per_kg, float):
            self.ni_mg_per_kg = float(self.ni_mg_per_kg)

        if self.cu_mg_per_kg is not None and not isinstance(self.cu_mg_per_kg, float):
            self.cu_mg_per_kg = float(self.cu_mg_per_kg)

        if self.zn_mg_per_kg is not None and not isinstance(self.zn_mg_per_kg, float):
            self.zn_mg_per_kg = float(self.zn_mg_per_kg)

        if self.ga_mg_per_kg is not None and not isinstance(self.ga_mg_per_kg, float):
            self.ga_mg_per_kg = float(self.ga_mg_per_kg)

        if self.as_mg_per_kg is not None and not isinstance(self.as_mg_per_kg, float):
            self.as_mg_per_kg = float(self.as_mg_per_kg)

        if self.se_mg_per_kg is not None and not isinstance(self.se_mg_per_kg, float):
            self.se_mg_per_kg = float(self.se_mg_per_kg)

        if self.br_mg_per_kg is not None and not isinstance(self.br_mg_per_kg, float):
            self.br_mg_per_kg = float(self.br_mg_per_kg)

        if self.rb_mg_per_kg is not None and not isinstance(self.rb_mg_per_kg, float):
            self.rb_mg_per_kg = float(self.rb_mg_per_kg)

        if self.sr_mg_per_kg is not None and not isinstance(self.sr_mg_per_kg, float):
            self.sr_mg_per_kg = float(self.sr_mg_per_kg)

        if self.y_mg_per_kg is not None and not isinstance(self.y_mg_per_kg, float):
            self.y_mg_per_kg = float(self.y_mg_per_kg)

        if self.nb_mg_per_kg is not None and not isinstance(self.nb_mg_per_kg, float):
            self.nb_mg_per_kg = float(self.nb_mg_per_kg)

        if self.mo_mg_per_kg is not None and not isinstance(self.mo_mg_per_kg, float):
            self.mo_mg_per_kg = float(self.mo_mg_per_kg)

        if self.ag_mg_per_kg is not None and not isinstance(self.ag_mg_per_kg, float):
            self.ag_mg_per_kg = float(self.ag_mg_per_kg)

        if self.cd_mg_per_kg is not None and not isinstance(self.cd_mg_per_kg, float):
            self.cd_mg_per_kg = float(self.cd_mg_per_kg)

        if self.in_mg_per_kg is not None and not isinstance(self.in_mg_per_kg, float):
            self.in_mg_per_kg = float(self.in_mg_per_kg)

        if self.sn_mg_per_kg is not None and not isinstance(self.sn_mg_per_kg, float):
            self.sn_mg_per_kg = float(self.sn_mg_per_kg)

        if self.sb_mg_per_kg is not None and not isinstance(self.sb_mg_per_kg, float):
            self.sb_mg_per_kg = float(self.sb_mg_per_kg)

        if self.cs_mg_per_kg is not None and not isinstance(self.cs_mg_per_kg, float):
            self.cs_mg_per_kg = float(self.cs_mg_per_kg)

        if self.ba_mg_per_kg is not None and not isinstance(self.ba_mg_per_kg, float):
            self.ba_mg_per_kg = float(self.ba_mg_per_kg)

        if self.la_mg_per_kg is not None and not isinstance(self.la_mg_per_kg, float):
            self.la_mg_per_kg = float(self.la_mg_per_kg)

        if self.ce_mg_per_kg is not None and not isinstance(self.ce_mg_per_kg, float):
            self.ce_mg_per_kg = float(self.ce_mg_per_kg)

        if self.pb_mg_per_kg is not None and not isinstance(self.pb_mg_per_kg, float):
            self.pb_mg_per_kg = float(self.pb_mg_per_kg)

        if self.th_mg_per_kg is not None and not isinstance(self.th_mg_per_kg, float):
            self.th_mg_per_kg = float(self.th_mg_per_kg)

        if self.u_mg_per_kg is not None and not isinstance(self.u_mg_per_kg, float):
            self.u_mg_per_kg = float(self.u_mg_per_kg)

        if self.flag_cl is not None and not isinstance(self.flag_cl, ProcessedDataFlag):
            self.flag_cl = ProcessedDataFlag(self.flag_cl)

        if self.flag_v is not None and not isinstance(self.flag_v, ProcessedDataFlag):
            self.flag_v = ProcessedDataFlag(self.flag_v)

        if self.flag_cr is not None and not isinstance(self.flag_cr, ProcessedDataFlag):
            self.flag_cr = ProcessedDataFlag(self.flag_cr)

        if self.flag_ni is not None and not isinstance(self.flag_ni, ProcessedDataFlag):
            self.flag_ni = ProcessedDataFlag(self.flag_ni)

        if self.flag_cu is not None and not isinstance(self.flag_cu, ProcessedDataFlag):
            self.flag_cu = ProcessedDataFlag(self.flag_cu)

        if self.flag_zn is not None and not isinstance(self.flag_zn, ProcessedDataFlag):
            self.flag_zn = ProcessedDataFlag(self.flag_zn)

        if self.flag_ga is not None and not isinstance(self.flag_ga, ProcessedDataFlag):
            self.flag_ga = ProcessedDataFlag(self.flag_ga)

        if self.flag_as is not None and not isinstance(self.flag_as, ProcessedDataFlag):
            self.flag_as = ProcessedDataFlag(self.flag_as)

        if self.flag_se is not None and not isinstance(self.flag_se, ProcessedDataFlag):
            self.flag_se = ProcessedDataFlag(self.flag_se)

        if self.flag_br is not None and not isinstance(self.flag_br, ProcessedDataFlag):
            self.flag_br = ProcessedDataFlag(self.flag_br)

        if self.flag_rb is not None and not isinstance(self.flag_rb, ProcessedDataFlag):
            self.flag_rb = ProcessedDataFlag(self.flag_rb)

        if self.flag_sr is not None and not isinstance(self.flag_sr, ProcessedDataFlag):
            self.flag_sr = ProcessedDataFlag(self.flag_sr)

        if self.flag_y is not None and not isinstance(self.flag_y, ProcessedDataFlag):
            self.flag_y = ProcessedDataFlag(self.flag_y)

        if self.flag_nb is not None and not isinstance(self.flag_nb, ProcessedDataFlag):
            self.flag_nb = ProcessedDataFlag(self.flag_nb)

        if self.flag_mo is not None and not isinstance(self.flag_mo, ProcessedDataFlag):
            self.flag_mo = ProcessedDataFlag(self.flag_mo)

        if self.flag_ag is not None and not isinstance(self.flag_ag, ProcessedDataFlag):
            self.flag_ag = ProcessedDataFlag(self.flag_ag)

        if self.flag_cd is not None and not isinstance(self.flag_cd, ProcessedDataFlag):
            self.flag_cd = ProcessedDataFlag(self.flag_cd)

        if self.flag_in is not None and not isinstance(self.flag_in, ProcessedDataFlag):
            self.flag_in = ProcessedDataFlag(self.flag_in)

        if self.flag_sn is not None and not isinstance(self.flag_sn, ProcessedDataFlag):
            self.flag_sn = ProcessedDataFlag(self.flag_sn)

        if self.flag_sb is not None and not isinstance(self.flag_sb, ProcessedDataFlag):
            self.flag_sb = ProcessedDataFlag(self.flag_sb)

        if self.flag_cs is not None and not isinstance(self.flag_cs, ProcessedDataFlag):
            self.flag_cs = ProcessedDataFlag(self.flag_cs)

        if self.flag_ba is not None and not isinstance(self.flag_ba, ProcessedDataFlag):
            self.flag_ba = ProcessedDataFlag(self.flag_ba)

        if self.flag_la is not None and not isinstance(self.flag_la, ProcessedDataFlag):
            self.flag_la = ProcessedDataFlag(self.flag_la)

        if self.flag_ce is not None and not isinstance(self.flag_ce, ProcessedDataFlag):
            self.flag_ce = ProcessedDataFlag(self.flag_ce)

        if self.flag_pb is not None and not isinstance(self.flag_pb, ProcessedDataFlag):
            self.flag_pb = ProcessedDataFlag(self.flag_pb)

        if self.flag_th is not None and not isinstance(self.flag_th, ProcessedDataFlag):
            self.flag_th = ProcessedDataFlag(self.flag_th)

        if self.flag_u is not None and not isinstance(self.flag_u, ProcessedDataFlag):
            self.flag_u = ProcessedDataFlag(self.flag_u)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
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
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["XRDPhaseProduct"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:XRDPhaseProduct"
    class_name: ClassVar[str] = "XRDPhaseProduct"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.XRDPhaseProduct

    id: Union[str, XRDPhaseProductId] = None
    name: str = None
    s3_key: str = None
    measure_type: Optional[Union[str, "ProductMeasureType"]] = None
    quartz_percent: Optional[float] = None
    albite_percent: Optional[float] = None
    microcline_percent: Optional[float] = None
    muscovite_percent: Optional[float] = None
    kaolinite_percent: Optional[float] = None
    chlorite_percent: Optional[float] = None
    hornblende_percent: Optional[float] = None
    pyrite_percent: Optional[float] = None
    halite_percent: Optional[float] = None
    gypsum_percent: Optional[float] = None
    flag_quartz: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_albite: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_microcline: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_muscovite: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_kaolinite: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_chlorite: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_hornblende: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_pyrite: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_halite: Optional[Union[str, "ProcessedDataFlag"]] = None
    flag_gypsum: Optional[Union[str, "ProcessedDataFlag"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, XRDPhaseProductId):
            self.id = XRDPhaseProductId(self.id)

        if self.measure_type is not None and not isinstance(self.measure_type, ProductMeasureType):
            self.measure_type = ProductMeasureType(self.measure_type)

        if self.quartz_percent is not None and not isinstance(self.quartz_percent, float):
            self.quartz_percent = float(self.quartz_percent)

        if self.albite_percent is not None and not isinstance(self.albite_percent, float):
            self.albite_percent = float(self.albite_percent)

        if self.microcline_percent is not None and not isinstance(self.microcline_percent, float):
            self.microcline_percent = float(self.microcline_percent)

        if self.muscovite_percent is not None and not isinstance(self.muscovite_percent, float):
            self.muscovite_percent = float(self.muscovite_percent)

        if self.kaolinite_percent is not None and not isinstance(self.kaolinite_percent, float):
            self.kaolinite_percent = float(self.kaolinite_percent)

        if self.chlorite_percent is not None and not isinstance(self.chlorite_percent, float):
            self.chlorite_percent = float(self.chlorite_percent)

        if self.hornblende_percent is not None and not isinstance(self.hornblende_percent, float):
            self.hornblende_percent = float(self.hornblende_percent)

        if self.pyrite_percent is not None and not isinstance(self.pyrite_percent, float):
            self.pyrite_percent = float(self.pyrite_percent)

        if self.halite_percent is not None and not isinstance(self.halite_percent, float):
            self.halite_percent = float(self.halite_percent)

        if self.gypsum_percent is not None and not isinstance(self.gypsum_percent, float):
            self.gypsum_percent = float(self.gypsum_percent)

        if self.flag_quartz is not None and not isinstance(self.flag_quartz, ProcessedDataFlag):
            self.flag_quartz = ProcessedDataFlag(self.flag_quartz)

        if self.flag_albite is not None and not isinstance(self.flag_albite, ProcessedDataFlag):
            self.flag_albite = ProcessedDataFlag(self.flag_albite)

        if self.flag_microcline is not None and not isinstance(self.flag_microcline, ProcessedDataFlag):
            self.flag_microcline = ProcessedDataFlag(self.flag_microcline)

        if self.flag_muscovite is not None and not isinstance(self.flag_muscovite, ProcessedDataFlag):
            self.flag_muscovite = ProcessedDataFlag(self.flag_muscovite)

        if self.flag_kaolinite is not None and not isinstance(self.flag_kaolinite, ProcessedDataFlag):
            self.flag_kaolinite = ProcessedDataFlag(self.flag_kaolinite)

        if self.flag_chlorite is not None and not isinstance(self.flag_chlorite, ProcessedDataFlag):
            self.flag_chlorite = ProcessedDataFlag(self.flag_chlorite)

        if self.flag_hornblende is not None and not isinstance(self.flag_hornblende, ProcessedDataFlag):
            self.flag_hornblende = ProcessedDataFlag(self.flag_hornblende)

        if self.flag_pyrite is not None and not isinstance(self.flag_pyrite, ProcessedDataFlag):
            self.flag_pyrite = ProcessedDataFlag(self.flag_pyrite)

        if self.flag_halite is not None and not isinstance(self.flag_halite, ProcessedDataFlag):
            self.flag_halite = ProcessedDataFlag(self.flag_halite)

        if self.flag_gypsum is not None and not isinstance(self.flag_gypsum, ProcessedDataFlag):
            self.flag_gypsum = ProcessedDataFlag(self.flag_gypsum)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Site(YAMLRoot):
    """
    Site-level metadata for a specific location from which a set of samples are collected.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["Site"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:Site"
    class_name: ClassVar[str] = "Site"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.Site

    id: Union[str, SiteId] = None
    name: str = None
    elev: str = None
    geo_loc_name: str = None
    growth_facil: Union[str, "GrowthFacilityEnum"] = None
    latitude: float = None
    longitude: float = None
    description: Optional[str] = None
    alt: Optional[str] = None
    annual_precpt: Optional[str] = None
    annual_temp: Optional[str] = None
    atmospheric_data: Optional[str] = None
    crop_rotation: Optional[str] = None
    cur_land_use: Optional[Union[str, "LandUseEnum"]] = None
    cur_vegetation: Optional[str] = None
    cur_vegetation_meth: Optional[str] = None
    drainage_class: Optional[Union[str, "DrainageClassEnum"]] = None
    extreme_event: Optional[str] = None
    fao_class: Optional[Union[str, "FAOClassEnum"]] = None
    fire: Optional[str] = None
    flooding: Optional[str] = None
    link_climate_info: Optional[str] = None
    link_class_info: Optional[str] = None
    local_class: Optional[str] = None
    local_class_meth: Optional[str] = None
    neon_site_code: Optional[str] = None
    neon_plot_id: Optional[str] = None
    other_growth_facil: Optional[str] = None
    previous_land_use: Optional[str] = None
    previous_land_use_meth: Optional[str] = None
    profile_position: Optional[Union[str, "ProfilePositionEnum"]] = None
    season_precpt: Optional[str] = None
    season_temp: Optional[str] = None
    slope_aspect: Optional[str] = None
    slope_gradient: Optional[str] = None
    tillage: Optional[Union[str, "TillageEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SiteId):
            self.id = SiteId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.elev):
            self.MissingRequiredField("elev")
        if not isinstance(self.elev, str):
            self.elev = str(self.elev)

        if self._is_empty(self.geo_loc_name):
            self.MissingRequiredField("geo_loc_name")
        if not isinstance(self.geo_loc_name, str):
            self.geo_loc_name = str(self.geo_loc_name)

        if self._is_empty(self.growth_facil):
            self.MissingRequiredField("growth_facil")
        if not isinstance(self.growth_facil, GrowthFacilityEnum):
            self.growth_facil = GrowthFacilityEnum(self.growth_facil)

        if self._is_empty(self.latitude):
            self.MissingRequiredField("latitude")
        if not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self._is_empty(self.longitude):
            self.MissingRequiredField("longitude")
        if not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.alt is not None and not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.annual_precpt is not None and not isinstance(self.annual_precpt, str):
            self.annual_precpt = str(self.annual_precpt)

        if self.annual_temp is not None and not isinstance(self.annual_temp, str):
            self.annual_temp = str(self.annual_temp)

        if self.atmospheric_data is not None and not isinstance(self.atmospheric_data, str):
            self.atmospheric_data = str(self.atmospheric_data)

        if self.crop_rotation is not None and not isinstance(self.crop_rotation, str):
            self.crop_rotation = str(self.crop_rotation)

        if self.cur_land_use is not None and not isinstance(self.cur_land_use, LandUseEnum):
            self.cur_land_use = LandUseEnum(self.cur_land_use)

        if self.cur_vegetation is not None and not isinstance(self.cur_vegetation, str):
            self.cur_vegetation = str(self.cur_vegetation)

        if self.cur_vegetation_meth is not None and not isinstance(self.cur_vegetation_meth, str):
            self.cur_vegetation_meth = str(self.cur_vegetation_meth)

        if self.drainage_class is not None and not isinstance(self.drainage_class, DrainageClassEnum):
            self.drainage_class = DrainageClassEnum(self.drainage_class)

        if self.extreme_event is not None and not isinstance(self.extreme_event, str):
            self.extreme_event = str(self.extreme_event)

        if self.fao_class is not None and not isinstance(self.fao_class, FAOClassEnum):
            self.fao_class = FAOClassEnum(self.fao_class)

        if self.fire is not None and not isinstance(self.fire, str):
            self.fire = str(self.fire)

        if self.flooding is not None and not isinstance(self.flooding, str):
            self.flooding = str(self.flooding)

        if self.link_climate_info is not None and not isinstance(self.link_climate_info, str):
            self.link_climate_info = str(self.link_climate_info)

        if self.link_class_info is not None and not isinstance(self.link_class_info, str):
            self.link_class_info = str(self.link_class_info)

        if self.local_class is not None and not isinstance(self.local_class, str):
            self.local_class = str(self.local_class)

        if self.local_class_meth is not None and not isinstance(self.local_class_meth, str):
            self.local_class_meth = str(self.local_class_meth)

        if self.neon_site_code is not None and not isinstance(self.neon_site_code, str):
            self.neon_site_code = str(self.neon_site_code)

        if self.neon_plot_id is not None and not isinstance(self.neon_plot_id, str):
            self.neon_plot_id = str(self.neon_plot_id)

        if self.other_growth_facil is not None and not isinstance(self.other_growth_facil, str):
            self.other_growth_facil = str(self.other_growth_facil)

        if self.previous_land_use is not None and not isinstance(self.previous_land_use, str):
            self.previous_land_use = str(self.previous_land_use)

        if self.previous_land_use_meth is not None and not isinstance(self.previous_land_use_meth, str):
            self.previous_land_use_meth = str(self.previous_land_use_meth)

        if self.profile_position is not None and not isinstance(self.profile_position, ProfilePositionEnum):
            self.profile_position = ProfilePositionEnum(self.profile_position)

        if self.season_precpt is not None and not isinstance(self.season_precpt, str):
            self.season_precpt = str(self.season_precpt)

        if self.season_temp is not None and not isinstance(self.season_temp, str):
            self.season_temp = str(self.season_temp)

        if self.slope_aspect is not None and not isinstance(self.slope_aspect, str):
            self.slope_aspect = str(self.slope_aspect)

        if self.slope_gradient is not None and not isinstance(self.slope_gradient, str):
            self.slope_gradient = str(self.slope_gradient)

        if self.tillage is not None and not isinstance(self.tillage, TillageEnum):
            self.tillage = TillageEnum(self.tillage)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sample(YAMLRoot):
    """
    A physical sample collected from an environment. The environment can be ecological, laboratory, or any other
    context where samples are collected. This class serves as an abstract class to relate subclasses of samples.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["Sample"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.Sample

    id: Union[str, SampleId] = None
    name: str = None
    description: Optional[str] = None
    emsl_activity: Optional[str] = None
    lims_barcode: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleId):
            self.id = SampleId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.emsl_activity is not None and not isinstance(self.emsl_activity, str):
            self.emsl_activity = str(self.emsl_activity)

        if self.lims_barcode is not None and not isinstance(self.lims_barcode, str):
            self.lims_barcode = str(self.lims_barcode)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AerosolArmSample(Sample):
    """
    An aerosol sample collected by the ARM facility.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["AerosolArmSample"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:AerosolArmSample"
    class_name: ClassVar[str] = "AerosolArmSample"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.AerosolArmSample

    id: Union[str, AerosolArmSampleId] = None
    name: str = None
    aerosol_type: Union[str, "AerosolTypeEnum"] = None
    analysis_type: str = None
    air_temp_regm: Optional[str] = None
    carb_dioxide: Optional[str] = None
    carb_monoxide: Optional[str] = None
    chem_administration: Optional[str] = None
    color_code: Optional[Union[str, "ColorCodeEnum"]] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    experimental_factor: Optional[str] = None
    experimental_factor_other: Optional[str] = None
    external_identifiers: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    extraction_method: Optional[str] = None
    first_blh: Optional[float] = None
    first_blh_quality_index: Optional[str] = None
    first_cbh: Optional[float] = None
    humidity_regm: Optional[str] = None
    isotope_exposure: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    mean_total_cpc_concentration: Optional[float] = None
    mean_total_pops_concentration: Optional[float] = None
    methane: Optional[str] = None
    method_development: Optional[str] = None
    misc_param: Optional[str] = None
    other: Optional[str] = None
    other_treatment: Optional[str] = None
    other_samp_store_temp: Optional[str] = None
    photochemical_exposure: Optional[Union[str, "PhotochemicalExposureEnum"]] = None
    pressure_control: Optional[str] = None
    priority_order: Optional[float] = None
    project: Optional[int] = None
    replicate_number: Optional[int] = None
    samp_store_temp: Optional[Union[str, "SampleStoreTempEnum"]] = None
    sample_link: Optional[str] = None
    sample_name: Optional[str] = None
    sample_processing: Optional[str] = None
    sampled_during: Optional[Union[str, SamplingActivityId]] = None
    second_blh: Optional[float] = None
    second_blh_quality: Optional[str] = None
    second_cbh: Optional[float] = None
    size_frac_low: Optional[str] = None
    size_frac_up: Optional[str] = None
    solar_irradiance: Optional[str] = None
    source_mat_id: Optional[str] = None
    storage_condition: Optional[Union[str, "StorageConditionEnum"]] = None
    storage_condition_other: Optional[str] = None
    technical_reps: Optional[int] = None
    third_blh: Optional[float] = None
    third_blh_quality: Optional[str] = None
    volatile_org_comp: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AerosolArmSampleId):
            self.id = AerosolArmSampleId(self.id)

        if self._is_empty(self.aerosol_type):
            self.MissingRequiredField("aerosol_type")
        if not isinstance(self.aerosol_type, AerosolTypeEnum):
            self.aerosol_type = AerosolTypeEnum(self.aerosol_type)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, str):
            self.analysis_type = str(self.analysis_type)

        if self.air_temp_regm is not None and not isinstance(self.air_temp_regm, str):
            self.air_temp_regm = str(self.air_temp_regm)

        if self.carb_dioxide is not None and not isinstance(self.carb_dioxide, str):
            self.carb_dioxide = str(self.carb_dioxide)

        if self.carb_monoxide is not None and not isinstance(self.carb_monoxide, str):
            self.carb_monoxide = str(self.carb_monoxide)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.color_code is not None and not isinstance(self.color_code, ColorCodeEnum):
            self.color_code = ColorCodeEnum(self.color_code)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.experimental_factor_other is not None and not isinstance(self.experimental_factor_other, str):
            self.experimental_factor_other = str(self.experimental_factor_other)

        if not isinstance(self.external_identifiers, list):
            self.external_identifiers = [self.external_identifiers] if self.external_identifiers is not None else []
        self.external_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.external_identifiers]

        if self.extraction_method is not None and not isinstance(self.extraction_method, str):
            self.extraction_method = str(self.extraction_method)

        if self.first_blh is not None and not isinstance(self.first_blh, float):
            self.first_blh = float(self.first_blh)

        if self.first_blh_quality_index is not None and not isinstance(self.first_blh_quality_index, str):
            self.first_blh_quality_index = str(self.first_blh_quality_index)

        if self.first_cbh is not None and not isinstance(self.first_cbh, float):
            self.first_cbh = float(self.first_cbh)

        if self.humidity_regm is not None and not isinstance(self.humidity_regm, str):
            self.humidity_regm = str(self.humidity_regm)

        if self.isotope_exposure is not None and not isinstance(self.isotope_exposure, str):
            self.isotope_exposure = str(self.isotope_exposure)

        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self.mean_total_cpc_concentration is not None and not isinstance(self.mean_total_cpc_concentration, float):
            self.mean_total_cpc_concentration = float(self.mean_total_cpc_concentration)

        if self.mean_total_pops_concentration is not None and not isinstance(self.mean_total_pops_concentration, float):
            self.mean_total_pops_concentration = float(self.mean_total_pops_concentration)

        if self.methane is not None and not isinstance(self.methane, str):
            self.methane = str(self.methane)

        if self.method_development is not None and not isinstance(self.method_development, str):
            self.method_development = str(self.method_development)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        if self.other is not None and not isinstance(self.other, str):
            self.other = str(self.other)

        if self.other_treatment is not None and not isinstance(self.other_treatment, str):
            self.other_treatment = str(self.other_treatment)

        if self.other_samp_store_temp is not None and not isinstance(self.other_samp_store_temp, str):
            self.other_samp_store_temp = str(self.other_samp_store_temp)

        if self.photochemical_exposure is not None and not isinstance(self.photochemical_exposure, PhotochemicalExposureEnum):
            self.photochemical_exposure = PhotochemicalExposureEnum(self.photochemical_exposure)

        if self.pressure_control is not None and not isinstance(self.pressure_control, str):
            self.pressure_control = str(self.pressure_control)

        if self.priority_order is not None and not isinstance(self.priority_order, float):
            self.priority_order = float(self.priority_order)

        if self.project is not None and not isinstance(self.project, int):
            self.project = int(self.project)

        if self.replicate_number is not None and not isinstance(self.replicate_number, int):
            self.replicate_number = int(self.replicate_number)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, SampleStoreTempEnum):
            self.samp_store_temp = SampleStoreTempEnum(self.samp_store_temp)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if self.sample_name is not None and not isinstance(self.sample_name, str):
            self.sample_name = str(self.sample_name)

        if self.sample_processing is not None and not isinstance(self.sample_processing, str):
            self.sample_processing = str(self.sample_processing)

        if self.sampled_during is not None and not isinstance(self.sampled_during, SamplingActivityId):
            self.sampled_during = SamplingActivityId(self.sampled_during)

        if self.second_blh is not None and not isinstance(self.second_blh, float):
            self.second_blh = float(self.second_blh)

        if self.second_blh_quality is not None and not isinstance(self.second_blh_quality, str):
            self.second_blh_quality = str(self.second_blh_quality)

        if self.second_cbh is not None and not isinstance(self.second_cbh, float):
            self.second_cbh = float(self.second_cbh)

        if self.size_frac_low is not None and not isinstance(self.size_frac_low, str):
            self.size_frac_low = str(self.size_frac_low)

        if self.size_frac_up is not None and not isinstance(self.size_frac_up, str):
            self.size_frac_up = str(self.size_frac_up)

        if self.solar_irradiance is not None and not isinstance(self.solar_irradiance, str):
            self.solar_irradiance = str(self.solar_irradiance)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        if self.storage_condition is not None and not isinstance(self.storage_condition, StorageConditionEnum):
            self.storage_condition = StorageConditionEnum(self.storage_condition)

        if self.storage_condition_other is not None and not isinstance(self.storage_condition_other, str):
            self.storage_condition_other = str(self.storage_condition_other)

        if self.technical_reps is not None and not isinstance(self.technical_reps, int):
            self.technical_reps = int(self.technical_reps)

        if self.third_blh is not None and not isinstance(self.third_blh, float):
            self.third_blh = float(self.third_blh)

        if self.third_blh_quality is not None and not isinstance(self.third_blh_quality, str):
            self.third_blh_quality = str(self.third_blh_quality)

        if self.volatile_org_comp is not None and not isinstance(self.volatile_org_comp, str):
            self.volatile_org_comp = str(self.volatile_org_comp)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AerosolSample(Sample):
    """
    An aerosol sample collected from the environment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["AerosolSample"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:AerosolSample"
    class_name: ClassVar[str] = "AerosolSample"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.AerosolSample

    id: Union[str, AerosolSampleId] = None
    name: str = None
    aerosol_type: Union[str, "AerosolTypeEnum"] = None
    analysis_type: str = None
    air_temp_regm: Optional[str] = None
    carb_dioxide: Optional[str] = None
    carb_monoxide: Optional[str] = None
    chem_administration: Optional[str] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    experimental_factor: Optional[str] = None
    experimental_factor_other: Optional[str] = None
    extraction_method: Optional[str] = None
    external_identifiers: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    humidity_regm: Optional[str] = None
    isotope_exposure: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    methane: Optional[str] = None
    method_development: Optional[str] = None
    misc_param: Optional[str] = None
    other: Optional[str] = None
    other_samp_store_temp: Optional[str] = None
    other_storage_condt: Optional[str] = None
    other_treatment: Optional[str] = None
    oxygen: Optional[str] = None
    photochemical_exposure: Optional[Union[str, "PhotochemicalExposureEnum"]] = None
    pressure_control: Optional[str] = None
    priority_order: Optional[float] = None
    project: Optional[int] = None
    replicate_number: Optional[int] = None
    sample_link: Optional[str] = None
    sample_name: Optional[str] = None
    sample_processing: Optional[str] = None
    sampled_during: Optional[Union[str, SamplingActivityId]] = None
    samp_store_temp: Optional[Union[str, "SampleStoreTempEnum"]] = None
    size_frac_low: Optional[str] = None
    size_frac_up: Optional[str] = None
    solar_irradiance: Optional[str] = None
    source_mat_id: Optional[str] = None
    storage_condition: Optional[Union[str, "StorageConditionEnum"]] = None
    storage_condition_other: Optional[str] = None
    technical_reps: Optional[int] = None
    temperature_exposure: Optional[str] = None
    volatile_org_comp: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AerosolSampleId):
            self.id = AerosolSampleId(self.id)

        if self._is_empty(self.aerosol_type):
            self.MissingRequiredField("aerosol_type")
        if not isinstance(self.aerosol_type, AerosolTypeEnum):
            self.aerosol_type = AerosolTypeEnum(self.aerosol_type)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, str):
            self.analysis_type = str(self.analysis_type)

        if self.air_temp_regm is not None and not isinstance(self.air_temp_regm, str):
            self.air_temp_regm = str(self.air_temp_regm)

        if self.carb_dioxide is not None and not isinstance(self.carb_dioxide, str):
            self.carb_dioxide = str(self.carb_dioxide)

        if self.carb_monoxide is not None and not isinstance(self.carb_monoxide, str):
            self.carb_monoxide = str(self.carb_monoxide)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.experimental_factor_other is not None and not isinstance(self.experimental_factor_other, str):
            self.experimental_factor_other = str(self.experimental_factor_other)

        if self.extraction_method is not None and not isinstance(self.extraction_method, str):
            self.extraction_method = str(self.extraction_method)

        if not isinstance(self.external_identifiers, list):
            self.external_identifiers = [self.external_identifiers] if self.external_identifiers is not None else []
        self.external_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.external_identifiers]

        if self.humidity_regm is not None and not isinstance(self.humidity_regm, str):
            self.humidity_regm = str(self.humidity_regm)

        if self.isotope_exposure is not None and not isinstance(self.isotope_exposure, str):
            self.isotope_exposure = str(self.isotope_exposure)

        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self.methane is not None and not isinstance(self.methane, str):
            self.methane = str(self.methane)

        if self.method_development is not None and not isinstance(self.method_development, str):
            self.method_development = str(self.method_development)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        if self.other is not None and not isinstance(self.other, str):
            self.other = str(self.other)

        if self.other_samp_store_temp is not None and not isinstance(self.other_samp_store_temp, str):
            self.other_samp_store_temp = str(self.other_samp_store_temp)

        if self.other_storage_condt is not None and not isinstance(self.other_storage_condt, str):
            self.other_storage_condt = str(self.other_storage_condt)

        if self.other_treatment is not None and not isinstance(self.other_treatment, str):
            self.other_treatment = str(self.other_treatment)

        if self.oxygen is not None and not isinstance(self.oxygen, str):
            self.oxygen = str(self.oxygen)

        if self.photochemical_exposure is not None and not isinstance(self.photochemical_exposure, PhotochemicalExposureEnum):
            self.photochemical_exposure = PhotochemicalExposureEnum(self.photochemical_exposure)

        if self.pressure_control is not None and not isinstance(self.pressure_control, str):
            self.pressure_control = str(self.pressure_control)

        if self.priority_order is not None and not isinstance(self.priority_order, float):
            self.priority_order = float(self.priority_order)

        if self.project is not None and not isinstance(self.project, int):
            self.project = int(self.project)

        if self.replicate_number is not None and not isinstance(self.replicate_number, int):
            self.replicate_number = int(self.replicate_number)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if self.sample_name is not None and not isinstance(self.sample_name, str):
            self.sample_name = str(self.sample_name)

        if self.sample_processing is not None and not isinstance(self.sample_processing, str):
            self.sample_processing = str(self.sample_processing)

        if self.sampled_during is not None and not isinstance(self.sampled_during, SamplingActivityId):
            self.sampled_during = SamplingActivityId(self.sampled_during)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, SampleStoreTempEnum):
            self.samp_store_temp = SampleStoreTempEnum(self.samp_store_temp)

        if self.size_frac_low is not None and not isinstance(self.size_frac_low, str):
            self.size_frac_low = str(self.size_frac_low)

        if self.size_frac_up is not None and not isinstance(self.size_frac_up, str):
            self.size_frac_up = str(self.size_frac_up)

        if self.solar_irradiance is not None and not isinstance(self.solar_irradiance, str):
            self.solar_irradiance = str(self.solar_irradiance)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        if self.storage_condition is not None and not isinstance(self.storage_condition, StorageConditionEnum):
            self.storage_condition = StorageConditionEnum(self.storage_condition)

        if self.storage_condition_other is not None and not isinstance(self.storage_condition_other, str):
            self.storage_condition_other = str(self.storage_condition_other)

        if self.technical_reps is not None and not isinstance(self.technical_reps, int):
            self.technical_reps = int(self.technical_reps)

        if self.temperature_exposure is not None and not isinstance(self.temperature_exposure, str):
            self.temperature_exposure = str(self.temperature_exposure)

        if self.volatile_org_comp is not None and not isinstance(self.volatile_org_comp, str):
            self.volatile_org_comp = str(self.volatile_org_comp)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
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
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["AMP2UserSample"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:AMP2UserSample"
    class_name: ClassVar[str] = "AMP2UserSample"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.AMP2UserSample

    id: Union[str, AMP2UserSampleId] = None
    biological_entity_ref: Union[str, BiologicalEntityId] = None
    storage_condition: Union[str, "StorageConditionEnum"] = None
    name: str = None
    collection_date: Optional[Union[str, XSDDate]] = None
    growth_facil: Optional[Union[str, "GrowthFacilityEnum"]] = None
    isol_growth_condt: Optional[str] = None
    start_date_inc: Optional[str] = None
    storage_temperature: Optional[str] = None
    shipped_sample_size: Optional[str] = None
    guid_source: Optional[str] = None
    other_guid_source: Optional[str] = None
    analysis_type: Optional[str] = None
    cbi: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AMP2UserSampleId):
            self.id = AMP2UserSampleId(self.id)

        if self._is_empty(self.biological_entity_ref):
            self.MissingRequiredField("biological_entity_ref")
        if not isinstance(self.biological_entity_ref, BiologicalEntityId):
            self.biological_entity_ref = BiologicalEntityId(self.biological_entity_ref)

        if self._is_empty(self.storage_condition):
            self.MissingRequiredField("storage_condition")
        if not isinstance(self.storage_condition, StorageConditionEnum):
            self.storage_condition = StorageConditionEnum(self.storage_condition)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.collection_date is not None and not isinstance(self.collection_date, XSDDate):
            self.collection_date = XSDDate(self.collection_date)

        if self.growth_facil is not None and not isinstance(self.growth_facil, GrowthFacilityEnum):
            self.growth_facil = GrowthFacilityEnum(self.growth_facil)

        if self.isol_growth_condt is not None and not isinstance(self.isol_growth_condt, str):
            self.isol_growth_condt = str(self.isol_growth_condt)

        if self.start_date_inc is not None and not isinstance(self.start_date_inc, str):
            self.start_date_inc = str(self.start_date_inc)

        if self.storage_temperature is not None and not isinstance(self.storage_temperature, str):
            self.storage_temperature = str(self.storage_temperature)

        if self.shipped_sample_size is not None and not isinstance(self.shipped_sample_size, str):
            self.shipped_sample_size = str(self.shipped_sample_size)

        if self.guid_source is not None and not isinstance(self.guid_source, str):
            self.guid_source = str(self.guid_source)

        if self.other_guid_source is not None and not isinstance(self.other_guid_source, str):
            self.other_guid_source = str(self.other_guid_source)

        if self.analysis_type is not None and not isinstance(self.analysis_type, str):
            self.analysis_type = str(self.analysis_type)

        if self.cbi is not None and not isinstance(self.cbi, Bool):
            self.cbi = Bool(self.cbi)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CommerciallyPurchasedSample(Sample):
    """
    A sample containing commercially purchased material.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["CommerciallyPurchasedSample"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:CommerciallyPurchasedSample"
    class_name: ClassVar[str] = "CommerciallyPurchasedSample"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.CommerciallyPurchasedSample

    id: Union[str, CommerciallyPurchasedSampleId] = None
    name: str = None
    analysis_type: str = None
    compound_name: str = None
    cas: Optional[str] = None
    experimental_factor: Optional[str] = None
    experimental_factor_other: Optional[str] = None
    external_identifiers: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    item_number: Optional[str] = None
    method_development: Optional[str] = None
    other: Optional[str] = None
    other_samp_store_temp: Optional[str] = None
    other_storage_condt: Optional[str] = None
    other_treatment: Optional[str] = None
    oxygen_status: Optional[Union[str, "OxygenStatusEnum"]] = None
    production_method: Optional[str] = None
    project: Optional[int] = None
    replicate_number: Optional[int] = None
    sample_link: Optional[str] = None
    sample_name: Optional[str] = None
    sample_processing: Optional[str] = None
    samp_store_temp: Optional[Union[str, "SampleStoreTempEnum"]] = None
    sampled_during: Optional[Union[str, SamplingActivityId]] = None
    source_mat_id: Optional[str] = None
    storage_condition: Optional[Union[str, "StorageConditionEnum"]] = None
    storage_condition_other: Optional[str] = None
    technical_reps: Optional[int] = None
    temp: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CommerciallyPurchasedSampleId):
            self.id = CommerciallyPurchasedSampleId(self.id)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, str):
            self.analysis_type = str(self.analysis_type)

        if self._is_empty(self.compound_name):
            self.MissingRequiredField("compound_name")
        if not isinstance(self.compound_name, str):
            self.compound_name = str(self.compound_name)

        if self.cas is not None and not isinstance(self.cas, str):
            self.cas = str(self.cas)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.experimental_factor_other is not None and not isinstance(self.experimental_factor_other, str):
            self.experimental_factor_other = str(self.experimental_factor_other)

        if not isinstance(self.external_identifiers, list):
            self.external_identifiers = [self.external_identifiers] if self.external_identifiers is not None else []
        self.external_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.external_identifiers]

        if self.item_number is not None and not isinstance(self.item_number, str):
            self.item_number = str(self.item_number)

        if self.method_development is not None and not isinstance(self.method_development, str):
            self.method_development = str(self.method_development)

        if self.other is not None and not isinstance(self.other, str):
            self.other = str(self.other)

        if self.other_samp_store_temp is not None and not isinstance(self.other_samp_store_temp, str):
            self.other_samp_store_temp = str(self.other_samp_store_temp)

        if self.other_storage_condt is not None and not isinstance(self.other_storage_condt, str):
            self.other_storage_condt = str(self.other_storage_condt)

        if self.other_treatment is not None and not isinstance(self.other_treatment, str):
            self.other_treatment = str(self.other_treatment)

        if self.oxygen_status is not None and not isinstance(self.oxygen_status, OxygenStatusEnum):
            self.oxygen_status = OxygenStatusEnum(self.oxygen_status)

        if self.production_method is not None and not isinstance(self.production_method, str):
            self.production_method = str(self.production_method)

        if self.project is not None and not isinstance(self.project, int):
            self.project = int(self.project)

        if self.replicate_number is not None and not isinstance(self.replicate_number, int):
            self.replicate_number = int(self.replicate_number)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if self.sample_name is not None and not isinstance(self.sample_name, str):
            self.sample_name = str(self.sample_name)

        if self.sample_processing is not None and not isinstance(self.sample_processing, str):
            self.sample_processing = str(self.sample_processing)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, SampleStoreTempEnum):
            self.samp_store_temp = SampleStoreTempEnum(self.samp_store_temp)

        if self.sampled_during is not None and not isinstance(self.sampled_during, SamplingActivityId):
            self.sampled_during = SamplingActivityId(self.sampled_during)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        if self.storage_condition is not None and not isinstance(self.storage_condition, StorageConditionEnum):
            self.storage_condition = StorageConditionEnum(self.storage_condition)

        if self.storage_condition_other is not None and not isinstance(self.storage_condition_other, str):
            self.storage_condition_other = str(self.storage_condition_other)

        if self.technical_reps is not None and not isinstance(self.technical_reps, int):
            self.technical_reps = int(self.technical_reps)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CultureEnvironmentalSample(Sample):
    """
    A sample containing organisms cultured from an environmental sample.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["CultureEnvironmentalSample"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:CultureEnvironmentalSample"
    class_name: ClassVar[str] = "CultureEnvironmentalSample"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.CultureEnvironmentalSample

    id: Union[str, CultureEnvironmentalSampleId] = None
    name: str = None
    analysis_type: str = None
    growth_medium: str = None
    host_common_name: str = None
    host_taxid: str = None
    isol_growth_condt: str = None
    start_date_inc: str = None
    air_temp_regm: Optional[str] = None
    biotic_regm: Optional[str] = None
    chem_administration: Optional[str] = None
    encoded_traits: Optional[str] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    experimental_factor: Optional[str] = None
    experimental_factor_other: Optional[str] = None
    external_identifiers: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    extraction_method: Optional[str] = None
    filter_method: Optional[str] = None
    gaseous_environment: Optional[str] = None
    genetic_mod: Optional[str] = None
    host_spec_range: Optional[str] = None
    humidity_regm: Optional[str] = None
    isotope_exposure: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    light_regm: Optional[str] = None
    method_development: Optional[str] = None
    non_microb_biomass: Optional[str] = None
    non_microb_biomass_method: Optional[str] = None
    other: Optional[str] = None
    other_samp_store_temp: Optional[str] = None
    other_storage_condt: Optional[str] = None
    other_treatment: Optional[str] = None
    oxygen_status: Optional[Union[str, "OxygenStatusEnum"]] = None
    pathogenicity: Optional[str] = None
    project: Optional[int] = None
    propagation: Optional[str] = None
    ref_biomaterial: Optional[str] = None
    replicate_number: Optional[int] = None
    biotic_relationship: Optional[Union[str, "BioticRelationshipEnum"]] = None
    samp_store_temp: Optional[Union[str, "SampleStoreTempEnum"]] = None
    sample_link: Optional[str] = None
    sample_name: Optional[str] = None
    sample_processing: Optional[str] = None
    sampled_during: Optional[Union[str, SamplingActivityId]] = None
    source_mat_id: Optional[str] = None
    storage_condition: Optional[Union[str, "StorageConditionEnum"]] = None
    storage_condition_other: Optional[str] = None
    subspecf_gen_lin: Optional[str] = None
    technical_reps: Optional[int] = None
    trophic_level: Optional[Union[str, "TrophicLevelEnum"]] = None
    watering_regm: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CultureEnvironmentalSampleId):
            self.id = CultureEnvironmentalSampleId(self.id)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, str):
            self.analysis_type = str(self.analysis_type)

        if self._is_empty(self.growth_medium):
            self.MissingRequiredField("growth_medium")
        if not isinstance(self.growth_medium, str):
            self.growth_medium = str(self.growth_medium)

        if self._is_empty(self.host_common_name):
            self.MissingRequiredField("host_common_name")
        if not isinstance(self.host_common_name, str):
            self.host_common_name = str(self.host_common_name)

        if self._is_empty(self.host_taxid):
            self.MissingRequiredField("host_taxid")
        if not isinstance(self.host_taxid, str):
            self.host_taxid = str(self.host_taxid)

        if self._is_empty(self.isol_growth_condt):
            self.MissingRequiredField("isol_growth_condt")
        if not isinstance(self.isol_growth_condt, str):
            self.isol_growth_condt = str(self.isol_growth_condt)

        if self._is_empty(self.start_date_inc):
            self.MissingRequiredField("start_date_inc")
        if not isinstance(self.start_date_inc, str):
            self.start_date_inc = str(self.start_date_inc)

        if self.air_temp_regm is not None and not isinstance(self.air_temp_regm, str):
            self.air_temp_regm = str(self.air_temp_regm)

        if self.biotic_regm is not None and not isinstance(self.biotic_regm, str):
            self.biotic_regm = str(self.biotic_regm)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.encoded_traits is not None and not isinstance(self.encoded_traits, str):
            self.encoded_traits = str(self.encoded_traits)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.experimental_factor_other is not None and not isinstance(self.experimental_factor_other, str):
            self.experimental_factor_other = str(self.experimental_factor_other)

        if not isinstance(self.external_identifiers, list):
            self.external_identifiers = [self.external_identifiers] if self.external_identifiers is not None else []
        self.external_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.external_identifiers]

        if self.extraction_method is not None and not isinstance(self.extraction_method, str):
            self.extraction_method = str(self.extraction_method)

        if self.filter_method is not None and not isinstance(self.filter_method, str):
            self.filter_method = str(self.filter_method)

        if self.gaseous_environment is not None and not isinstance(self.gaseous_environment, str):
            self.gaseous_environment = str(self.gaseous_environment)

        if self.genetic_mod is not None and not isinstance(self.genetic_mod, str):
            self.genetic_mod = str(self.genetic_mod)

        if self.host_spec_range is not None and not isinstance(self.host_spec_range, str):
            self.host_spec_range = str(self.host_spec_range)

        if self.humidity_regm is not None and not isinstance(self.humidity_regm, str):
            self.humidity_regm = str(self.humidity_regm)

        if self.isotope_exposure is not None and not isinstance(self.isotope_exposure, str):
            self.isotope_exposure = str(self.isotope_exposure)

        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self.light_regm is not None and not isinstance(self.light_regm, str):
            self.light_regm = str(self.light_regm)

        if self.method_development is not None and not isinstance(self.method_development, str):
            self.method_development = str(self.method_development)

        if self.non_microb_biomass is not None and not isinstance(self.non_microb_biomass, str):
            self.non_microb_biomass = str(self.non_microb_biomass)

        if self.non_microb_biomass_method is not None and not isinstance(self.non_microb_biomass_method, str):
            self.non_microb_biomass_method = str(self.non_microb_biomass_method)

        if self.other is not None and not isinstance(self.other, str):
            self.other = str(self.other)

        if self.other_samp_store_temp is not None and not isinstance(self.other_samp_store_temp, str):
            self.other_samp_store_temp = str(self.other_samp_store_temp)

        if self.other_storage_condt is not None and not isinstance(self.other_storage_condt, str):
            self.other_storage_condt = str(self.other_storage_condt)

        if self.other_treatment is not None and not isinstance(self.other_treatment, str):
            self.other_treatment = str(self.other_treatment)

        if self.oxygen_status is not None and not isinstance(self.oxygen_status, OxygenStatusEnum):
            self.oxygen_status = OxygenStatusEnum(self.oxygen_status)

        if self.pathogenicity is not None and not isinstance(self.pathogenicity, str):
            self.pathogenicity = str(self.pathogenicity)

        if self.project is not None and not isinstance(self.project, int):
            self.project = int(self.project)

        if self.propagation is not None and not isinstance(self.propagation, str):
            self.propagation = str(self.propagation)

        if self.ref_biomaterial is not None and not isinstance(self.ref_biomaterial, str):
            self.ref_biomaterial = str(self.ref_biomaterial)

        if self.replicate_number is not None and not isinstance(self.replicate_number, int):
            self.replicate_number = int(self.replicate_number)

        if self.biotic_relationship is not None and not isinstance(self.biotic_relationship, BioticRelationshipEnum):
            self.biotic_relationship = BioticRelationshipEnum(self.biotic_relationship)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, SampleStoreTempEnum):
            self.samp_store_temp = SampleStoreTempEnum(self.samp_store_temp)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if self.sample_name is not None and not isinstance(self.sample_name, str):
            self.sample_name = str(self.sample_name)

        if self.sample_processing is not None and not isinstance(self.sample_processing, str):
            self.sample_processing = str(self.sample_processing)

        if self.sampled_during is not None and not isinstance(self.sampled_during, SamplingActivityId):
            self.sampled_during = SamplingActivityId(self.sampled_during)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        if self.storage_condition is not None and not isinstance(self.storage_condition, StorageConditionEnum):
            self.storage_condition = StorageConditionEnum(self.storage_condition)

        if self.storage_condition_other is not None and not isinstance(self.storage_condition_other, str):
            self.storage_condition_other = str(self.storage_condition_other)

        if self.subspecf_gen_lin is not None and not isinstance(self.subspecf_gen_lin, str):
            self.subspecf_gen_lin = str(self.subspecf_gen_lin)

        if self.technical_reps is not None and not isinstance(self.technical_reps, int):
            self.technical_reps = int(self.technical_reps)

        if self.trophic_level is not None and not isinstance(self.trophic_level, TrophicLevelEnum):
            self.trophic_level = TrophicLevelEnum(self.trophic_level)

        if self.watering_regm is not None and not isinstance(self.watering_regm, str):
            self.watering_regm = str(self.watering_regm)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EngineeredStrainSample(Sample):
    """
    A sample containing a strain of an organism that has been subjected to genetic engineering.

    This class references a biological_entity for strain identity information (organism_name,
    strain_source, modification_method, genotype_segment_*, component_*, phenotype, trait, etc.)
    and carries only sample-instance-specific slots.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["EngineeredStrainSample"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:EngineeredStrainSample"
    class_name: ClassVar[str] = "EngineeredStrainSample"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.EngineeredStrainSample

    id: Union[str, EngineeredStrainSampleId] = None
    name: str = None
    biological_entity_ref: Optional[Union[str, BiologicalEntityId]] = None
    cbi: Optional[Union[bool, Bool]] = None
    storage_condition: Optional[Union[str, "StorageConditionEnum"]] = None
    storage_temperature: Optional[str] = None
    external_identifiers: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EngineeredStrainSampleId):
            self.id = EngineeredStrainSampleId(self.id)

        if self._is_empty(self.cbi):
            self.MissingRequiredField("cbi")
        if not isinstance(self.cbi, str):
            self.cbi = str(self.cbi)

        if self._is_empty(self.storage_condition):
            self.MissingRequiredField("storage_condition")
        if not isinstance(self.storage_condition, str):
            self.storage_condition = str(self.storage_condition)

        if self.biological_entity_ref is not None and not isinstance(self.biological_entity_ref, BiologicalEntityId):
            self.biological_entity_ref = BiologicalEntityId(self.biological_entity_ref)

        if self.cbi is not None and not isinstance(self.cbi, Bool):
            self.cbi = Bool(self.cbi)

        if self.storage_condition is not None and not isinstance(self.storage_condition, StorageConditionEnum):
            self.storage_condition = StorageConditionEnum(self.storage_condition)

        if self.storage_temperature is not None and not isinstance(self.storage_temperature, str):
            self.storage_temperature = str(self.storage_temperature)

        if not isinstance(self.external_identifiers, list):
            self.external_identifiers = [self.external_identifiers] if self.external_identifiers is not None else []
        self.external_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.external_identifiers]

        if self.storage_temperature is not None and not isinstance(self.storage_temperature, str):
            self.storage_temperature = str(self.storage_temperature)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FieldDeployedTerraformSample(Sample):
    """
    A sample collected from a field-deployed Terraform experiment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["FieldDeployedTerraformSample"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:FieldDeployedTerraformSample"
    class_name: ClassVar[str] = "FieldDeployedTerraformSample"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.FieldDeployedTerraformSample

    id: Union[str, FieldDeployedTerraformSampleId] = None
    name: str = None
    analysis_type: str = None
    initiation_date_inoculation: str = None
    initiation_date_plant: str = None
    latitude: float = None
    longitude: float = None
    synth_env_assembly: str = None
    synth_env_design: Union[str, "SyntheticEnvironmentEnum"] = None
    synth_env_design_method: str = None
    synth_env_material: str = None
    synth_env_treatment: str = None
    synth_start_date: str = None
    air_temp_regm: Optional[str] = None
    biotic_regm: Optional[str] = None
    chem_administration: Optional[str] = None
    cult_root_med: Optional[str] = None
    depth: Optional[str] = None
    encoded_traits: Optional[str] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    external_identifiers: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    gaseous_environment: Optional[str] = None
    genetic_mod: Optional[str] = None
    growth_medium: Optional[str] = None
    host_age: Optional[str] = None
    host_common_name: Optional[str] = None
    host_dry_mass: Optional[str] = None
    host_genotype: Optional[str] = None
    host_height: Optional[str] = None
    host_life_stage: Optional[str] = None
    host_spec_range: Optional[str] = None
    host_taxid: Optional[str] = None
    host_tot_mass: Optional[str] = None
    host_wet_mass: Optional[str] = None
    humidity_regm: Optional[str] = None
    isol_growth_condt: Optional[str] = None
    isotope_exposure: Optional[str] = None
    light_regm: Optional[str] = None
    method_development: Optional[str] = None
    mineral_nutr_regm: Optional[str] = None
    misc_param: Optional[str] = None
    non_min_nutr_regm: Optional[str] = None
    other: Optional[str] = None
    other_samp_store_temp: Optional[str] = None
    other_storage_condt: Optional[str] = None
    other_treatment: Optional[str] = None
    oxygen_status: Optional[Union[str, "OxygenStatusEnum"]] = None
    plant_growth_med: Optional[str] = None
    plant_product: Optional[str] = None
    plant_sex: Optional[Union[str, "PlantSexEnum"]] = None
    plant_struc: Optional[Union[str, "PlantStructureEnum"]] = None
    pressure: Optional[str] = None
    project: Optional[int] = None
    propagation: Optional[str] = None
    redox_potential: Optional[str] = None
    ref_biomaterial: Optional[str] = None
    replicate_number: Optional[int] = None
    root_cond: Optional[str] = None
    root_med_carbon: Optional[str] = None
    root_med_macronutr: Optional[str] = None
    root_med_micronutr: Optional[str] = None
    salt_regm: Optional[str] = None
    sample_link: Optional[str] = None
    sample_name: Optional[str] = None
    sample_processing: Optional[str] = None
    biotic_relationship: Optional[Union[str, "BioticRelationshipEnum"]] = None
    samp_store_temp: Optional[Union[str, "SampleStoreTempEnum"]] = None
    sampled_during: Optional[Union[str, SamplingActivityId]] = None
    source_mat_id: Optional[str] = None
    start_date_inc: Optional[str] = None
    storage_condition: Optional[Union[str, "StorageConditionEnum"]] = None
    storage_condition_other: Optional[str] = None
    technical_reps: Optional[int] = None
    temp: Optional[str] = None
    tiss_cult_growth_med: Optional[str] = None
    water_content: Optional[str] = None
    water_content_meth: Optional[str] = None
    watering_regm: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FieldDeployedTerraformSampleId):
            self.id = FieldDeployedTerraformSampleId(self.id)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, str):
            self.analysis_type = str(self.analysis_type)

        if self._is_empty(self.initiation_date_inoculation):
            self.MissingRequiredField("initiation_date_inoculation")
        if not isinstance(self.initiation_date_inoculation, str):
            self.initiation_date_inoculation = str(self.initiation_date_inoculation)

        if self._is_empty(self.initiation_date_plant):
            self.MissingRequiredField("initiation_date_plant")
        if not isinstance(self.initiation_date_plant, str):
            self.initiation_date_plant = str(self.initiation_date_plant)

        if self._is_empty(self.latitude):
            self.MissingRequiredField("latitude")
        if not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self._is_empty(self.longitude):
            self.MissingRequiredField("longitude")
        if not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self._is_empty(self.synth_env_assembly):
            self.MissingRequiredField("synth_env_assembly")
        if not isinstance(self.synth_env_assembly, str):
            self.synth_env_assembly = str(self.synth_env_assembly)

        if self._is_empty(self.synth_env_design):
            self.MissingRequiredField("synth_env_design")
        if not isinstance(self.synth_env_design, SyntheticEnvironmentEnum):
            self.synth_env_design = SyntheticEnvironmentEnum(self.synth_env_design)

        if self._is_empty(self.synth_env_design_method):
            self.MissingRequiredField("synth_env_design_method")
        if not isinstance(self.synth_env_design_method, str):
            self.synth_env_design_method = str(self.synth_env_design_method)

        if self._is_empty(self.synth_env_material):
            self.MissingRequiredField("synth_env_material")
        if not isinstance(self.synth_env_material, str):
            self.synth_env_material = str(self.synth_env_material)

        if self._is_empty(self.synth_env_treatment):
            self.MissingRequiredField("synth_env_treatment")
        if not isinstance(self.synth_env_treatment, str):
            self.synth_env_treatment = str(self.synth_env_treatment)

        if self._is_empty(self.synth_start_date):
            self.MissingRequiredField("synth_start_date")
        if not isinstance(self.synth_start_date, str):
            self.synth_start_date = str(self.synth_start_date)

        if self.air_temp_regm is not None and not isinstance(self.air_temp_regm, str):
            self.air_temp_regm = str(self.air_temp_regm)

        if self.biotic_regm is not None and not isinstance(self.biotic_regm, str):
            self.biotic_regm = str(self.biotic_regm)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.cult_root_med is not None and not isinstance(self.cult_root_med, str):
            self.cult_root_med = str(self.cult_root_med)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.encoded_traits is not None and not isinstance(self.encoded_traits, str):
            self.encoded_traits = str(self.encoded_traits)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if not isinstance(self.external_identifiers, list):
            self.external_identifiers = [self.external_identifiers] if self.external_identifiers is not None else []
        self.external_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.external_identifiers]

        if self.gaseous_environment is not None and not isinstance(self.gaseous_environment, str):
            self.gaseous_environment = str(self.gaseous_environment)

        if self.genetic_mod is not None and not isinstance(self.genetic_mod, str):
            self.genetic_mod = str(self.genetic_mod)

        if self.growth_medium is not None and not isinstance(self.growth_medium, str):
            self.growth_medium = str(self.growth_medium)

        if self.host_age is not None and not isinstance(self.host_age, str):
            self.host_age = str(self.host_age)

        if self.host_common_name is not None and not isinstance(self.host_common_name, str):
            self.host_common_name = str(self.host_common_name)

        if self.host_dry_mass is not None and not isinstance(self.host_dry_mass, str):
            self.host_dry_mass = str(self.host_dry_mass)

        if self.host_genotype is not None and not isinstance(self.host_genotype, str):
            self.host_genotype = str(self.host_genotype)

        if self.host_height is not None and not isinstance(self.host_height, str):
            self.host_height = str(self.host_height)

        if self.host_life_stage is not None and not isinstance(self.host_life_stage, str):
            self.host_life_stage = str(self.host_life_stage)

        if self.host_spec_range is not None and not isinstance(self.host_spec_range, str):
            self.host_spec_range = str(self.host_spec_range)

        if self.host_taxid is not None and not isinstance(self.host_taxid, str):
            self.host_taxid = str(self.host_taxid)

        if self.host_tot_mass is not None and not isinstance(self.host_tot_mass, str):
            self.host_tot_mass = str(self.host_tot_mass)

        if self.host_wet_mass is not None and not isinstance(self.host_wet_mass, str):
            self.host_wet_mass = str(self.host_wet_mass)

        if self.humidity_regm is not None and not isinstance(self.humidity_regm, str):
            self.humidity_regm = str(self.humidity_regm)

        if self.isol_growth_condt is not None and not isinstance(self.isol_growth_condt, str):
            self.isol_growth_condt = str(self.isol_growth_condt)

        if self.isotope_exposure is not None and not isinstance(self.isotope_exposure, str):
            self.isotope_exposure = str(self.isotope_exposure)

        if self.light_regm is not None and not isinstance(self.light_regm, str):
            self.light_regm = str(self.light_regm)

        if self.method_development is not None and not isinstance(self.method_development, str):
            self.method_development = str(self.method_development)

        if self.mineral_nutr_regm is not None and not isinstance(self.mineral_nutr_regm, str):
            self.mineral_nutr_regm = str(self.mineral_nutr_regm)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        if self.non_min_nutr_regm is not None and not isinstance(self.non_min_nutr_regm, str):
            self.non_min_nutr_regm = str(self.non_min_nutr_regm)

        if self.other is not None and not isinstance(self.other, str):
            self.other = str(self.other)

        if self.other_samp_store_temp is not None and not isinstance(self.other_samp_store_temp, str):
            self.other_samp_store_temp = str(self.other_samp_store_temp)

        if self.other_storage_condt is not None and not isinstance(self.other_storage_condt, str):
            self.other_storage_condt = str(self.other_storage_condt)

        if self.other_treatment is not None and not isinstance(self.other_treatment, str):
            self.other_treatment = str(self.other_treatment)

        if self.oxygen_status is not None and not isinstance(self.oxygen_status, OxygenStatusEnum):
            self.oxygen_status = OxygenStatusEnum(self.oxygen_status)

        if self.plant_growth_med is not None and not isinstance(self.plant_growth_med, str):
            self.plant_growth_med = str(self.plant_growth_med)

        if self.plant_product is not None and not isinstance(self.plant_product, str):
            self.plant_product = str(self.plant_product)

        if self.plant_sex is not None and not isinstance(self.plant_sex, PlantSexEnum):
            self.plant_sex = PlantSexEnum(self.plant_sex)

        if self.plant_struc is not None and not isinstance(self.plant_struc, PlantStructureEnum):
            self.plant_struc = PlantStructureEnum(self.plant_struc)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.project is not None and not isinstance(self.project, int):
            self.project = int(self.project)

        if self.propagation is not None and not isinstance(self.propagation, str):
            self.propagation = str(self.propagation)

        if self.redox_potential is not None and not isinstance(self.redox_potential, str):
            self.redox_potential = str(self.redox_potential)

        if self.ref_biomaterial is not None and not isinstance(self.ref_biomaterial, str):
            self.ref_biomaterial = str(self.ref_biomaterial)

        if self.replicate_number is not None and not isinstance(self.replicate_number, int):
            self.replicate_number = int(self.replicate_number)

        if self.root_cond is not None and not isinstance(self.root_cond, str):
            self.root_cond = str(self.root_cond)

        if self.root_med_carbon is not None and not isinstance(self.root_med_carbon, str):
            self.root_med_carbon = str(self.root_med_carbon)

        if self.root_med_macronutr is not None and not isinstance(self.root_med_macronutr, str):
            self.root_med_macronutr = str(self.root_med_macronutr)

        if self.root_med_micronutr is not None and not isinstance(self.root_med_micronutr, str):
            self.root_med_micronutr = str(self.root_med_micronutr)

        if self.salt_regm is not None and not isinstance(self.salt_regm, str):
            self.salt_regm = str(self.salt_regm)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if self.sample_name is not None and not isinstance(self.sample_name, str):
            self.sample_name = str(self.sample_name)

        if self.sample_processing is not None and not isinstance(self.sample_processing, str):
            self.sample_processing = str(self.sample_processing)

        if self.biotic_relationship is not None and not isinstance(self.biotic_relationship, BioticRelationshipEnum):
            self.biotic_relationship = BioticRelationshipEnum(self.biotic_relationship)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, SampleStoreTempEnum):
            self.samp_store_temp = SampleStoreTempEnum(self.samp_store_temp)

        if self.sampled_during is not None and not isinstance(self.sampled_during, SamplingActivityId):
            self.sampled_during = SamplingActivityId(self.sampled_during)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        if self.start_date_inc is not None and not isinstance(self.start_date_inc, str):
            self.start_date_inc = str(self.start_date_inc)

        if self.storage_condition is not None and not isinstance(self.storage_condition, StorageConditionEnum):
            self.storage_condition = StorageConditionEnum(self.storage_condition)

        if self.storage_condition_other is not None and not isinstance(self.storage_condition_other, str):
            self.storage_condition_other = str(self.storage_condition_other)

        if self.technical_reps is not None and not isinstance(self.technical_reps, int):
            self.technical_reps = int(self.technical_reps)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.tiss_cult_growth_med is not None and not isinstance(self.tiss_cult_growth_med, str):
            self.tiss_cult_growth_med = str(self.tiss_cult_growth_med)

        if self.water_content is not None and not isinstance(self.water_content, str):
            self.water_content = str(self.water_content)

        if self.water_content_meth is not None and not isinstance(self.water_content_meth, str):
            self.water_content_meth = str(self.water_content_meth)

        if self.watering_regm is not None and not isinstance(self.watering_regm, str):
            self.watering_regm = str(self.watering_regm)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MixedCultureSample(Sample):
    """
    A sample containing multiple cultured organisms.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["MixedCultureSample"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:MixedCultureSample"
    class_name: ClassVar[str] = "MixedCultureSample"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.MixedCultureSample

    id: Union[str, MixedCultureSampleId] = None
    name: str = None
    analysis_type: str = None
    growth_medium: str = None
    host_common_name: str = None
    host_taxid: str = None
    isol_growth_condt: str = None
    start_date_inc: str = None
    air_temp_regm: Optional[str] = None
    biotic_regm: Optional[str] = None
    chem_administration: Optional[str] = None
    encoded_traits: Optional[str] = None
    experimental_factor: Optional[str] = None
    experimental_factor_other: Optional[str] = None
    external_identifiers: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    extraction_method: Optional[str] = None
    gaseous_environment: Optional[str] = None
    genetic_mod: Optional[str] = None
    host_spec_range: Optional[str] = None
    humidity_regm: Optional[str] = None
    isotope_exposure: Optional[str] = None
    light_regm: Optional[str] = None
    method_development: Optional[str] = None
    non_microb_biomass: Optional[str] = None
    other: Optional[str] = None
    other_samp_store_temp: Optional[str] = None
    other_storage_condt: Optional[str] = None
    other_treatment: Optional[str] = None
    oxygen_status: Optional[Union[str, "OxygenStatusEnum"]] = None
    pathogenicity: Optional[str] = None
    project: Optional[int] = None
    propagation: Optional[str] = None
    ref_biomaterial: Optional[str] = None
    replicate_number: Optional[int] = None
    biotic_relationship: Optional[Union[str, "BioticRelationshipEnum"]] = None
    sample_link: Optional[str] = None
    sample_name: Optional[str] = None
    sample_processing: Optional[str] = None
    sampled_during: Optional[Union[str, SamplingActivityId]] = None
    samp_store_temp: Optional[Union[str, "SampleStoreTempEnum"]] = None
    source_mat_id: Optional[str] = None
    specific_host: Optional[str] = None
    storage_condition: Optional[Union[str, "StorageConditionEnum"]] = None
    storage_condition_other: Optional[str] = None
    subspecf_gen_lin: Optional[str] = None
    technical_reps: Optional[int] = None
    trophic_level: Optional[Union[str, "TrophicLevelEnum"]] = None
    watering_regm: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MixedCultureSampleId):
            self.id = MixedCultureSampleId(self.id)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, str):
            self.analysis_type = str(self.analysis_type)

        if self._is_empty(self.growth_medium):
            self.MissingRequiredField("growth_medium")
        if not isinstance(self.growth_medium, str):
            self.growth_medium = str(self.growth_medium)

        if self._is_empty(self.host_common_name):
            self.MissingRequiredField("host_common_name")
        if not isinstance(self.host_common_name, str):
            self.host_common_name = str(self.host_common_name)

        if self._is_empty(self.host_taxid):
            self.MissingRequiredField("host_taxid")
        if not isinstance(self.host_taxid, str):
            self.host_taxid = str(self.host_taxid)

        if self._is_empty(self.isol_growth_condt):
            self.MissingRequiredField("isol_growth_condt")
        if not isinstance(self.isol_growth_condt, str):
            self.isol_growth_condt = str(self.isol_growth_condt)

        if self._is_empty(self.start_date_inc):
            self.MissingRequiredField("start_date_inc")
        if not isinstance(self.start_date_inc, str):
            self.start_date_inc = str(self.start_date_inc)

        if self.air_temp_regm is not None and not isinstance(self.air_temp_regm, str):
            self.air_temp_regm = str(self.air_temp_regm)

        if self.biotic_regm is not None and not isinstance(self.biotic_regm, str):
            self.biotic_regm = str(self.biotic_regm)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.encoded_traits is not None and not isinstance(self.encoded_traits, str):
            self.encoded_traits = str(self.encoded_traits)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.experimental_factor_other is not None and not isinstance(self.experimental_factor_other, str):
            self.experimental_factor_other = str(self.experimental_factor_other)

        if not isinstance(self.external_identifiers, list):
            self.external_identifiers = [self.external_identifiers] if self.external_identifiers is not None else []
        self.external_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.external_identifiers]

        if self.extraction_method is not None and not isinstance(self.extraction_method, str):
            self.extraction_method = str(self.extraction_method)

        if self.gaseous_environment is not None and not isinstance(self.gaseous_environment, str):
            self.gaseous_environment = str(self.gaseous_environment)

        if self.genetic_mod is not None and not isinstance(self.genetic_mod, str):
            self.genetic_mod = str(self.genetic_mod)

        if self.host_spec_range is not None and not isinstance(self.host_spec_range, str):
            self.host_spec_range = str(self.host_spec_range)

        if self.humidity_regm is not None and not isinstance(self.humidity_regm, str):
            self.humidity_regm = str(self.humidity_regm)

        if self.isotope_exposure is not None and not isinstance(self.isotope_exposure, str):
            self.isotope_exposure = str(self.isotope_exposure)

        if self.light_regm is not None and not isinstance(self.light_regm, str):
            self.light_regm = str(self.light_regm)

        if self.method_development is not None and not isinstance(self.method_development, str):
            self.method_development = str(self.method_development)

        if self.non_microb_biomass is not None and not isinstance(self.non_microb_biomass, str):
            self.non_microb_biomass = str(self.non_microb_biomass)

        if self.other is not None and not isinstance(self.other, str):
            self.other = str(self.other)

        if self.other_samp_store_temp is not None and not isinstance(self.other_samp_store_temp, str):
            self.other_samp_store_temp = str(self.other_samp_store_temp)

        if self.other_storage_condt is not None and not isinstance(self.other_storage_condt, str):
            self.other_storage_condt = str(self.other_storage_condt)

        if self.other_treatment is not None and not isinstance(self.other_treatment, str):
            self.other_treatment = str(self.other_treatment)

        if self.oxygen_status is not None and not isinstance(self.oxygen_status, OxygenStatusEnum):
            self.oxygen_status = OxygenStatusEnum(self.oxygen_status)

        if self.pathogenicity is not None and not isinstance(self.pathogenicity, str):
            self.pathogenicity = str(self.pathogenicity)

        if self.project is not None and not isinstance(self.project, int):
            self.project = int(self.project)

        if self.propagation is not None and not isinstance(self.propagation, str):
            self.propagation = str(self.propagation)

        if self.ref_biomaterial is not None and not isinstance(self.ref_biomaterial, str):
            self.ref_biomaterial = str(self.ref_biomaterial)

        if self.replicate_number is not None and not isinstance(self.replicate_number, int):
            self.replicate_number = int(self.replicate_number)

        if self.biotic_relationship is not None and not isinstance(self.biotic_relationship, BioticRelationshipEnum):
            self.biotic_relationship = BioticRelationshipEnum(self.biotic_relationship)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if self.sample_name is not None and not isinstance(self.sample_name, str):
            self.sample_name = str(self.sample_name)

        if self.sample_processing is not None and not isinstance(self.sample_processing, str):
            self.sample_processing = str(self.sample_processing)

        if self.sampled_during is not None and not isinstance(self.sampled_during, SamplingActivityId):
            self.sampled_during = SamplingActivityId(self.sampled_during)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, SampleStoreTempEnum):
            self.samp_store_temp = SampleStoreTempEnum(self.samp_store_temp)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        if self.specific_host is not None and not isinstance(self.specific_host, str):
            self.specific_host = str(self.specific_host)

        if self.storage_condition is not None and not isinstance(self.storage_condition, StorageConditionEnum):
            self.storage_condition = StorageConditionEnum(self.storage_condition)

        if self.storage_condition_other is not None and not isinstance(self.storage_condition_other, str):
            self.storage_condition_other = str(self.storage_condition_other)

        if self.subspecf_gen_lin is not None and not isinstance(self.subspecf_gen_lin, str):
            self.subspecf_gen_lin = str(self.subspecf_gen_lin)

        if self.technical_reps is not None and not isinstance(self.technical_reps, int):
            self.technical_reps = int(self.technical_reps)

        if self.trophic_level is not None and not isinstance(self.trophic_level, TrophicLevelEnum):
            self.trophic_level = TrophicLevelEnum(self.trophic_level)

        if self.watering_regm is not None and not isinstance(self.watering_regm, str):
            self.watering_regm = str(self.watering_regm)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MonetSoilSample(Sample):
    """
    A soil sample that has been collected according to the MONet soil sampling protocol. This sample type has specific
    slot requirements related to the MONet soil sampling method, such as infiltration rates.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["MonetSoilSample"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:MonetSoilSample"
    class_name: ClassVar[str] = "MonetSoilSample"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.MonetSoilSample

    id: Union[str, MonetSoilSampleId] = None
    name: str = None
    bulk_elect_conductivity: str = None
    depth: str = None
    latitude: float = None
    longitude: float = None
    sampling_set: int = None
    soil_sample_type: Union[str, "SoilSampleTypeEnum"] = None
    soil_type: Union[str, "SoilTypeEnum"] = None
    soil_type_meth: str = None
    temp: str = None
    water_content: str = None
    agrochem_addition: Optional[str] = None
    chem_administration: Optional[str] = None
    core_group: Optional[Union[str, "MONetCoreGroupEnum"]] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    external_identifiers: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    lims_id: Optional[str] = None
    misc_param: Optional[str] = None
    other: Optional[str] = None
    other_samp_store_temp: Optional[str] = None
    other_storage_condt: Optional[str] = None
    other_treatment: Optional[str] = None
    project: Optional[int] = None
    sample_name: Optional[str] = None
    samp_store_temp: Optional[Union[str, "SampleStoreTempEnum"]] = None
    sampled_during: Optional[Union[str, SamplingActivityId]] = None
    storage_condition: Optional[Union[str, "StorageConditionEnum"]] = None
    storage_condition_other: Optional[str] = None
    water_content_meth: Optional[str] = None
    watering_regm: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MonetSoilSampleId):
            self.id = MonetSoilSampleId(self.id)

        if self._is_empty(self.bulk_elect_conductivity):
            self.MissingRequiredField("bulk_elect_conductivity")
        if not isinstance(self.bulk_elect_conductivity, str):
            self.bulk_elect_conductivity = str(self.bulk_elect_conductivity)

        if self._is_empty(self.depth):
            self.MissingRequiredField("depth")
        if not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self._is_empty(self.latitude):
            self.MissingRequiredField("latitude")
        if not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self._is_empty(self.longitude):
            self.MissingRequiredField("longitude")
        if not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self._is_empty(self.sampling_set):
            self.MissingRequiredField("sampling_set")
        if not isinstance(self.sampling_set, int):
            self.sampling_set = int(self.sampling_set)

        if self._is_empty(self.soil_sample_type):
            self.MissingRequiredField("soil_sample_type")
        if not isinstance(self.soil_sample_type, SoilSampleTypeEnum):
            self.soil_sample_type = SoilSampleTypeEnum(self.soil_sample_type)

        if self._is_empty(self.soil_type):
            self.MissingRequiredField("soil_type")
        if not isinstance(self.soil_type, SoilTypeEnum):
            self.soil_type = SoilTypeEnum(self.soil_type)

        if self._is_empty(self.soil_type_meth):
            self.MissingRequiredField("soil_type_meth")
        if not isinstance(self.soil_type_meth, str):
            self.soil_type_meth = str(self.soil_type_meth)

        if self._is_empty(self.temp):
            self.MissingRequiredField("temp")
        if not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self._is_empty(self.water_content):
            self.MissingRequiredField("water_content")
        if not isinstance(self.water_content, str):
            self.water_content = str(self.water_content)

        if self.agrochem_addition is not None and not isinstance(self.agrochem_addition, str):
            self.agrochem_addition = str(self.agrochem_addition)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.core_group is not None and not isinstance(self.core_group, MONetCoreGroupEnum):
            self.core_group = MONetCoreGroupEnum(self.core_group)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if not isinstance(self.external_identifiers, list):
            self.external_identifiers = [self.external_identifiers] if self.external_identifiers is not None else []
        self.external_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.external_identifiers]

        if self.lims_id is not None and not isinstance(self.lims_id, str):
            self.lims_id = str(self.lims_id)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        if self.other is not None and not isinstance(self.other, str):
            self.other = str(self.other)

        if self.other_samp_store_temp is not None and not isinstance(self.other_samp_store_temp, str):
            self.other_samp_store_temp = str(self.other_samp_store_temp)

        if self.other_storage_condt is not None and not isinstance(self.other_storage_condt, str):
            self.other_storage_condt = str(self.other_storage_condt)

        if self.other_treatment is not None and not isinstance(self.other_treatment, str):
            self.other_treatment = str(self.other_treatment)

        if self.project is not None and not isinstance(self.project, int):
            self.project = int(self.project)

        if self.sample_name is not None and not isinstance(self.sample_name, str):
            self.sample_name = str(self.sample_name)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, SampleStoreTempEnum):
            self.samp_store_temp = SampleStoreTempEnum(self.samp_store_temp)

        if self.sampled_during is not None and not isinstance(self.sampled_during, SamplingActivityId):
            self.sampled_during = SamplingActivityId(self.sampled_during)

        if self.storage_condition is not None and not isinstance(self.storage_condition, StorageConditionEnum):
            self.storage_condition = StorageConditionEnum(self.storage_condition)

        if self.storage_condition_other is not None and not isinstance(self.storage_condition_other, str):
            self.storage_condition_other = str(self.storage_condition_other)

        if self.water_content_meth is not None and not isinstance(self.water_content_meth, str):
            self.water_content_meth = str(self.water_content_meth)

        if self.watering_regm is not None and not isinstance(self.watering_regm, str):
            self.watering_regm = str(self.watering_regm)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OtherUndescribedSample(Sample):
    """
    A sample that does not fit into any of the other described sample types.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["OtherUndescribedSample"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:OtherUndescribedSample"
    class_name: ClassVar[str] = "OtherUndescribedSample"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.OtherUndescribedSample

    id: Union[str, OtherUndescribedSampleId] = None
    name: str = None
    analysis_type: str = None
    latitude: float = None
    longitude: float = None
    sample_type: str = None
    agrochem_addition: Optional[str] = None
    air_temp_regm: Optional[str] = None
    al_sat: Optional[str] = None
    al_sat_meth: Optional[str] = None
    alkalinity: Optional[str] = None
    alkalinity_method: Optional[str] = None
    alkyl_diethers: Optional[str] = None
    aminopept_act: Optional[str] = None
    ammonium: Optional[str] = None
    ances_data: Optional[str] = None
    antibiotic_regm: Optional[str] = None
    bac_prod: Optional[str] = None
    bac_resp: Optional[str] = None
    bacteria_carb_prod: Optional[str] = None
    biochem_oxygen_dem: Optional[str] = None
    biol_stat: Optional[Union[str, "BiolStatEnum"]] = None
    biotic_regm: Optional[str] = None
    bishomohopanol: Optional[str] = None
    bromide: Optional[str] = None
    bulk_elect_conductivity: Optional[str] = None
    calcium: Optional[str] = None
    carb_dioxide: Optional[str] = None
    carb_monoxide: Optional[str] = None
    carb_nitro_ratio: Optional[str] = None
    cas: Optional[str] = None
    chem_administration: Optional[str] = None
    chem_mutagen: Optional[str] = None
    chem_oxygen_dem: Optional[str] = None
    chloride: Optional[str] = None
    chlorophyll: Optional[str] = None
    compound_name: Optional[str] = None
    conduc: Optional[str] = None
    density: Optional[str] = None
    depth: Optional[str] = None
    diether_lipids: Optional[str] = None
    diss_carb_dioxide: Optional[str] = None
    diss_hydrogen: Optional[str] = None
    diss_inorg_carb: Optional[str] = None
    diss_inorg_nitro: Optional[str] = None
    diss_inorg_phosp: Optional[str] = None
    diss_org_carb: Optional[str] = None
    diss_org_nitro: Optional[str] = None
    diss_oxygen: Optional[str] = None
    down_par: Optional[str] = None
    efficiency_percent: Optional[str] = None
    emulsions: Optional[str] = None
    encoded_traits: Optional[str] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    experimental_factor: Optional[str] = None
    experimental_factor_other: Optional[str] = None
    extraction_method: Optional[str] = None
    external_identifiers: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    fertilizer_regm: Optional[str] = None
    filter_method: Optional[str] = None
    fluor: Optional[str] = None
    fungicide_regm: Optional[str] = None
    gaseous_environment: Optional[str] = None
    gaseous_substances: Optional[str] = None
    genetic_mod: Optional[str] = None
    glucosidase_act: Optional[str] = None
    gravity: Optional[str] = None
    growth_habit: Optional[Union[str, "GrowthHabitEnum"]] = None
    growth_hormone_regm: Optional[str] = None
    growth_medium: Optional[str] = None
    heavy_metals: Optional[str] = None
    heavy_metals_meth: Optional[str] = None
    herbicide_regm: Optional[str] = None
    host_age: Optional[str] = None
    host_common_name: Optional[str] = None
    host_disease_stat: Optional[str] = None
    host_dry_mass: Optional[str] = None
    host_height: Optional[str] = None
    host_infra_spec_name: Optional[str] = None
    host_infra_spec_rank: Optional[str] = None
    host_length: Optional[str] = None
    host_life_stage: Optional[str] = None
    host_phenotype: Optional[str] = None
    host_spec_range: Optional[str] = None
    host_symbiont: Optional[str] = None
    host_taxid: Optional[str] = None
    host_tot_mass: Optional[str] = None
    host_wet_mass: Optional[str] = None
    humidity_regm: Optional[str] = None
    indust_eff_percent: Optional[str] = None
    inorg_particles: Optional[str] = None
    isol_growth_condt: Optional[str] = None
    isotope_exposure: Optional[str] = None
    item_number: Optional[str] = None
    light_intensity: Optional[str] = None
    light_regm: Optional[str] = None
    link_addit_analys: Optional[str] = None
    magnesium: Optional[str] = None
    mean_frict_vel: Optional[str] = None
    mean_peak_frict_vel: Optional[str] = None
    mechanical_damage: Optional[str] = None
    method_development: Optional[str] = None
    methane: Optional[str] = None
    micro_biomass_C_meth: Optional[str] = None
    micro_biomass_N_meth: Optional[str] = None
    microbial_biomass: Optional[str] = None
    microbial_biomass_c: Optional[str] = None
    microbial_biomass_n: Optional[str] = None
    microbial_biomass_meth: Optional[str] = None
    mineral_nutr_regm: Optional[str] = None
    misc_param: Optional[str] = None
    n_alkanes: Optional[str] = None
    nitrate: Optional[str] = None
    nitrite: Optional[str] = None
    nitro: Optional[str] = None
    non_microb_biomass: Optional[str] = None
    non_microb_biomass_method: Optional[str] = None
    non_min_nutr_regm: Optional[str] = None
    org_carb: Optional[str] = None
    org_matter: Optional[str] = None
    org_nitro: Optional[str] = None
    org_nitro_method: Optional[str] = None
    org_particles: Optional[str] = None
    organism_count: Optional[str] = None
    other: Optional[str] = None
    other_samp_store_temp: Optional[str] = None
    other_treatment: Optional[str] = None
    oxygen: Optional[str] = None
    oxygen_status: Optional[Union[str, "OxygenStatusEnum"]] = None
    part_org_carb: Optional[str] = None
    part_org_nitro: Optional[str] = None
    particle_class: Optional[str] = None
    pathogenicity: Optional[str] = None
    perturbation: Optional[str] = None
    pesticide_regm: Optional[str] = None
    petroleum_hydrocarb: Optional[str] = None
    ph: Optional[float] = None
    ph_meth: Optional[str] = None
    ph_regm: Optional[str] = None
    phaeopigments: Optional[str] = None
    phosphate: Optional[str] = None
    phosplipid_fatt_acid: Optional[str] = None
    photochemical_exposure: Optional[Union[str, "PhotochemicalExposureEnum"]] = None
    photon_flux: Optional[str] = None
    porosity: Optional[str] = None
    potassium: Optional[str] = None
    pre_treatment: Optional[str] = None
    pressure: Optional[str] = None
    pressure_control: Optional[str] = None
    primary_prod: Optional[str] = None
    primary_treatment: Optional[str] = None
    priority_order: Optional[float] = None
    production_method: Optional[str] = None
    project: Optional[int] = None
    propagation: Optional[str] = None
    radiation_regm: Optional[str] = None
    rainfall_regm: Optional[str] = None
    reactor_type: Optional[str] = None
    redox_potential: Optional[str] = None
    ref_biomaterial: Optional[str] = None
    replicate_number: Optional[int] = None
    salinity: Optional[str] = None
    salinity_method: Optional[str] = None
    salt_regm: Optional[str] = None
    biotic_relationship: Optional[Union[str, "BioticRelationshipEnum"]] = None
    samp_capt_status: Optional[str] = None
    samp_dis_stage: Optional[str] = None
    samp_store_temp: Optional[Union[str, "SampleStoreTempEnum"]] = None
    sample_link: Optional[str] = None
    sample_name: Optional[str] = None
    sample_processing: Optional[str] = None
    sampled_during: Optional[Union[str, SamplingActivityId]] = None
    season_environment: Optional[str] = None
    secondary_treatment: Optional[str] = None
    sewage_type: Optional[str] = None
    sieving: Optional[str] = None
    silicate: Optional[str] = None
    size_frac_low: Optional[str] = None
    size_frac_up: Optional[str] = None
    sludge_retent_time: Optional[str] = None
    sodium: Optional[str] = None
    solar_irradiance: Optional[str] = None
    soluble_inorg_mat: Optional[str] = None
    soluble_org_mat: Optional[str] = None
    soluble_react_phosp: Optional[str] = None
    source_mat_id: Optional[str] = None
    standing_water_regm: Optional[str] = None
    start_date_inc: Optional[str] = None
    storage_condition: Optional[Union[str, "StorageConditionEnum"]] = None
    storage_condition_other: Optional[str] = None
    subspecf_gen_lin: Optional[str] = None
    sulfate: Optional[str] = None
    sulfide: Optional[str] = None
    suspend_part_matter: Optional[str] = None
    suspend_solids: Optional[str] = None
    synth_instrument: Optional[str] = None
    synth_process: Optional[str] = None
    synth_reagents: Optional[str] = None
    technical_reps: Optional[int] = None
    temp: Optional[str] = None
    temperature_exposure: Optional[str] = None
    tertiary_treatment: Optional[str] = None
    tidal_stage: Optional[Union[str, "TidalStageEnum"]] = None
    tiss_cult_growth_med: Optional[str] = None
    tot_carb: Optional[str] = None
    tot_depth_water_col: Optional[str] = None
    tot_diss_nitro: Optional[str] = None
    tot_inorg_nitro: Optional[str] = None
    tot_nitro: Optional[str] = None
    tot_nitro_cont_meth: Optional[str] = None
    tot_nitro_content: Optional[str] = None
    tot_org_c_meth: Optional[str] = None
    tot_org_carb: Optional[str] = None
    tot_part_carb: Optional[str] = None
    tot_phosp: Optional[str] = None
    tot_phosphate: Optional[str] = None
    trophic_level: Optional[Union[str, "TrophicLevelEnum"]] = None
    turbidity: Optional[str] = None
    volatile_org_comp: Optional[str] = None
    wastewater_type: Optional[str] = None
    water_content: Optional[str] = None
    water_current: Optional[str] = None
    water_temp_regm: Optional[str] = None
    watering_regm: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OtherUndescribedSampleId):
            self.id = OtherUndescribedSampleId(self.id)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, str):
            self.analysis_type = str(self.analysis_type)

        if self._is_empty(self.latitude):
            self.MissingRequiredField("latitude")
        if not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self._is_empty(self.longitude):
            self.MissingRequiredField("longitude")
        if not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self._is_empty(self.sample_type):
            self.MissingRequiredField("sample_type")
        if not isinstance(self.sample_type, str):
            self.sample_type = str(self.sample_type)

        if self.agrochem_addition is not None and not isinstance(self.agrochem_addition, str):
            self.agrochem_addition = str(self.agrochem_addition)

        if self.air_temp_regm is not None and not isinstance(self.air_temp_regm, str):
            self.air_temp_regm = str(self.air_temp_regm)

        if self.al_sat is not None and not isinstance(self.al_sat, str):
            self.al_sat = str(self.al_sat)

        if self.al_sat_meth is not None and not isinstance(self.al_sat_meth, str):
            self.al_sat_meth = str(self.al_sat_meth)

        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.alkalinity_method is not None and not isinstance(self.alkalinity_method, str):
            self.alkalinity_method = str(self.alkalinity_method)

        if self.alkyl_diethers is not None and not isinstance(self.alkyl_diethers, str):
            self.alkyl_diethers = str(self.alkyl_diethers)

        if self.aminopept_act is not None and not isinstance(self.aminopept_act, str):
            self.aminopept_act = str(self.aminopept_act)

        if self.ammonium is not None and not isinstance(self.ammonium, str):
            self.ammonium = str(self.ammonium)

        if self.ances_data is not None and not isinstance(self.ances_data, str):
            self.ances_data = str(self.ances_data)

        if self.antibiotic_regm is not None and not isinstance(self.antibiotic_regm, str):
            self.antibiotic_regm = str(self.antibiotic_regm)

        if self.bac_prod is not None and not isinstance(self.bac_prod, str):
            self.bac_prod = str(self.bac_prod)

        if self.bac_resp is not None and not isinstance(self.bac_resp, str):
            self.bac_resp = str(self.bac_resp)

        if self.bacteria_carb_prod is not None and not isinstance(self.bacteria_carb_prod, str):
            self.bacteria_carb_prod = str(self.bacteria_carb_prod)

        if self.biochem_oxygen_dem is not None and not isinstance(self.biochem_oxygen_dem, str):
            self.biochem_oxygen_dem = str(self.biochem_oxygen_dem)

        if self.biol_stat is not None and not isinstance(self.biol_stat, BiolStatEnum):
            self.biol_stat = BiolStatEnum(self.biol_stat)

        if self.biotic_regm is not None and not isinstance(self.biotic_regm, str):
            self.biotic_regm = str(self.biotic_regm)

        if self.bishomohopanol is not None and not isinstance(self.bishomohopanol, str):
            self.bishomohopanol = str(self.bishomohopanol)

        if self.bromide is not None and not isinstance(self.bromide, str):
            self.bromide = str(self.bromide)

        if self.bulk_elect_conductivity is not None and not isinstance(self.bulk_elect_conductivity, str):
            self.bulk_elect_conductivity = str(self.bulk_elect_conductivity)

        if self.calcium is not None and not isinstance(self.calcium, str):
            self.calcium = str(self.calcium)

        if self.carb_dioxide is not None and not isinstance(self.carb_dioxide, str):
            self.carb_dioxide = str(self.carb_dioxide)

        if self.carb_monoxide is not None and not isinstance(self.carb_monoxide, str):
            self.carb_monoxide = str(self.carb_monoxide)

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, str):
            self.carb_nitro_ratio = str(self.carb_nitro_ratio)

        if self.cas is not None and not isinstance(self.cas, str):
            self.cas = str(self.cas)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.chem_mutagen is not None and not isinstance(self.chem_mutagen, str):
            self.chem_mutagen = str(self.chem_mutagen)

        if self.chem_oxygen_dem is not None and not isinstance(self.chem_oxygen_dem, str):
            self.chem_oxygen_dem = str(self.chem_oxygen_dem)

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.chlorophyll is not None and not isinstance(self.chlorophyll, str):
            self.chlorophyll = str(self.chlorophyll)

        if self.compound_name is not None and not isinstance(self.compound_name, str):
            self.compound_name = str(self.compound_name)

        if self.conduc is not None and not isinstance(self.conduc, str):
            self.conduc = str(self.conduc)

        if self.density is not None and not isinstance(self.density, str):
            self.density = str(self.density)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.diether_lipids is not None and not isinstance(self.diether_lipids, str):
            self.diether_lipids = str(self.diether_lipids)

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, str):
            self.diss_carb_dioxide = str(self.diss_carb_dioxide)

        if self.diss_hydrogen is not None and not isinstance(self.diss_hydrogen, str):
            self.diss_hydrogen = str(self.diss_hydrogen)

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, str):
            self.diss_inorg_carb = str(self.diss_inorg_carb)

        if self.diss_inorg_nitro is not None and not isinstance(self.diss_inorg_nitro, str):
            self.diss_inorg_nitro = str(self.diss_inorg_nitro)

        if self.diss_inorg_phosp is not None and not isinstance(self.diss_inorg_phosp, str):
            self.diss_inorg_phosp = str(self.diss_inorg_phosp)

        if self.diss_org_carb is not None and not isinstance(self.diss_org_carb, str):
            self.diss_org_carb = str(self.diss_org_carb)

        if self.diss_org_nitro is not None and not isinstance(self.diss_org_nitro, str):
            self.diss_org_nitro = str(self.diss_org_nitro)

        if self.diss_oxygen is not None and not isinstance(self.diss_oxygen, str):
            self.diss_oxygen = str(self.diss_oxygen)

        if self.down_par is not None and not isinstance(self.down_par, str):
            self.down_par = str(self.down_par)

        if self.efficiency_percent is not None and not isinstance(self.efficiency_percent, str):
            self.efficiency_percent = str(self.efficiency_percent)

        if self.emulsions is not None and not isinstance(self.emulsions, str):
            self.emulsions = str(self.emulsions)

        if self.encoded_traits is not None and not isinstance(self.encoded_traits, str):
            self.encoded_traits = str(self.encoded_traits)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.experimental_factor_other is not None and not isinstance(self.experimental_factor_other, str):
            self.experimental_factor_other = str(self.experimental_factor_other)

        if self.extraction_method is not None and not isinstance(self.extraction_method, str):
            self.extraction_method = str(self.extraction_method)

        if not isinstance(self.external_identifiers, list):
            self.external_identifiers = [self.external_identifiers] if self.external_identifiers is not None else []
        self.external_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.external_identifiers]

        if self.fertilizer_regm is not None and not isinstance(self.fertilizer_regm, str):
            self.fertilizer_regm = str(self.fertilizer_regm)

        if self.filter_method is not None and not isinstance(self.filter_method, str):
            self.filter_method = str(self.filter_method)

        if self.fluor is not None and not isinstance(self.fluor, str):
            self.fluor = str(self.fluor)

        if self.fungicide_regm is not None and not isinstance(self.fungicide_regm, str):
            self.fungicide_regm = str(self.fungicide_regm)

        if self.gaseous_environment is not None and not isinstance(self.gaseous_environment, str):
            self.gaseous_environment = str(self.gaseous_environment)

        if self.gaseous_substances is not None and not isinstance(self.gaseous_substances, str):
            self.gaseous_substances = str(self.gaseous_substances)

        if self.genetic_mod is not None and not isinstance(self.genetic_mod, str):
            self.genetic_mod = str(self.genetic_mod)

        if self.glucosidase_act is not None and not isinstance(self.glucosidase_act, str):
            self.glucosidase_act = str(self.glucosidase_act)

        if self.gravity is not None and not isinstance(self.gravity, str):
            self.gravity = str(self.gravity)

        if self.growth_habit is not None and not isinstance(self.growth_habit, GrowthHabitEnum):
            self.growth_habit = GrowthHabitEnum(self.growth_habit)

        if self.growth_hormone_regm is not None and not isinstance(self.growth_hormone_regm, str):
            self.growth_hormone_regm = str(self.growth_hormone_regm)

        if self.growth_medium is not None and not isinstance(self.growth_medium, str):
            self.growth_medium = str(self.growth_medium)

        if self.heavy_metals is not None and not isinstance(self.heavy_metals, str):
            self.heavy_metals = str(self.heavy_metals)

        if self.heavy_metals_meth is not None and not isinstance(self.heavy_metals_meth, str):
            self.heavy_metals_meth = str(self.heavy_metals_meth)

        if self.herbicide_regm is not None and not isinstance(self.herbicide_regm, str):
            self.herbicide_regm = str(self.herbicide_regm)

        if self.host_age is not None and not isinstance(self.host_age, str):
            self.host_age = str(self.host_age)

        if self.host_common_name is not None and not isinstance(self.host_common_name, str):
            self.host_common_name = str(self.host_common_name)

        if self.host_disease_stat is not None and not isinstance(self.host_disease_stat, str):
            self.host_disease_stat = str(self.host_disease_stat)

        if self.host_dry_mass is not None and not isinstance(self.host_dry_mass, str):
            self.host_dry_mass = str(self.host_dry_mass)

        if self.host_height is not None and not isinstance(self.host_height, str):
            self.host_height = str(self.host_height)

        if self.host_infra_spec_name is not None and not isinstance(self.host_infra_spec_name, str):
            self.host_infra_spec_name = str(self.host_infra_spec_name)

        if self.host_infra_spec_rank is not None and not isinstance(self.host_infra_spec_rank, str):
            self.host_infra_spec_rank = str(self.host_infra_spec_rank)

        if self.host_length is not None and not isinstance(self.host_length, str):
            self.host_length = str(self.host_length)

        if self.host_life_stage is not None and not isinstance(self.host_life_stage, str):
            self.host_life_stage = str(self.host_life_stage)

        if self.host_phenotype is not None and not isinstance(self.host_phenotype, str):
            self.host_phenotype = str(self.host_phenotype)

        if self.host_spec_range is not None and not isinstance(self.host_spec_range, str):
            self.host_spec_range = str(self.host_spec_range)

        if self.host_symbiont is not None and not isinstance(self.host_symbiont, str):
            self.host_symbiont = str(self.host_symbiont)

        if self.host_taxid is not None and not isinstance(self.host_taxid, str):
            self.host_taxid = str(self.host_taxid)

        if self.host_tot_mass is not None and not isinstance(self.host_tot_mass, str):
            self.host_tot_mass = str(self.host_tot_mass)

        if self.host_wet_mass is not None and not isinstance(self.host_wet_mass, str):
            self.host_wet_mass = str(self.host_wet_mass)

        if self.humidity_regm is not None and not isinstance(self.humidity_regm, str):
            self.humidity_regm = str(self.humidity_regm)

        if self.indust_eff_percent is not None and not isinstance(self.indust_eff_percent, str):
            self.indust_eff_percent = str(self.indust_eff_percent)

        if self.inorg_particles is not None and not isinstance(self.inorg_particles, str):
            self.inorg_particles = str(self.inorg_particles)

        if self.isol_growth_condt is not None and not isinstance(self.isol_growth_condt, str):
            self.isol_growth_condt = str(self.isol_growth_condt)

        if self.isotope_exposure is not None and not isinstance(self.isotope_exposure, str):
            self.isotope_exposure = str(self.isotope_exposure)

        if self.item_number is not None and not isinstance(self.item_number, str):
            self.item_number = str(self.item_number)

        if self.light_intensity is not None and not isinstance(self.light_intensity, str):
            self.light_intensity = str(self.light_intensity)

        if self.light_regm is not None and not isinstance(self.light_regm, str):
            self.light_regm = str(self.light_regm)

        if self.link_addit_analys is not None and not isinstance(self.link_addit_analys, str):
            self.link_addit_analys = str(self.link_addit_analys)

        if self.magnesium is not None and not isinstance(self.magnesium, str):
            self.magnesium = str(self.magnesium)

        if self.mean_frict_vel is not None and not isinstance(self.mean_frict_vel, str):
            self.mean_frict_vel = str(self.mean_frict_vel)

        if self.mean_peak_frict_vel is not None and not isinstance(self.mean_peak_frict_vel, str):
            self.mean_peak_frict_vel = str(self.mean_peak_frict_vel)

        if self.mechanical_damage is not None and not isinstance(self.mechanical_damage, str):
            self.mechanical_damage = str(self.mechanical_damage)

        if self.method_development is not None and not isinstance(self.method_development, str):
            self.method_development = str(self.method_development)

        if self.methane is not None and not isinstance(self.methane, str):
            self.methane = str(self.methane)

        if self.micro_biomass_C_meth is not None and not isinstance(self.micro_biomass_C_meth, str):
            self.micro_biomass_C_meth = str(self.micro_biomass_C_meth)

        if self.micro_biomass_N_meth is not None and not isinstance(self.micro_biomass_N_meth, str):
            self.micro_biomass_N_meth = str(self.micro_biomass_N_meth)

        if self.microbial_biomass is not None and not isinstance(self.microbial_biomass, str):
            self.microbial_biomass = str(self.microbial_biomass)

        if self.microbial_biomass_c is not None and not isinstance(self.microbial_biomass_c, str):
            self.microbial_biomass_c = str(self.microbial_biomass_c)

        if self.microbial_biomass_n is not None and not isinstance(self.microbial_biomass_n, str):
            self.microbial_biomass_n = str(self.microbial_biomass_n)

        if self.microbial_biomass_meth is not None and not isinstance(self.microbial_biomass_meth, str):
            self.microbial_biomass_meth = str(self.microbial_biomass_meth)

        if self.mineral_nutr_regm is not None and not isinstance(self.mineral_nutr_regm, str):
            self.mineral_nutr_regm = str(self.mineral_nutr_regm)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        if self.n_alkanes is not None and not isinstance(self.n_alkanes, str):
            self.n_alkanes = str(self.n_alkanes)

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if self.nitrite is not None and not isinstance(self.nitrite, str):
            self.nitrite = str(self.nitrite)

        if self.nitro is not None and not isinstance(self.nitro, str):
            self.nitro = str(self.nitro)

        if self.non_microb_biomass is not None and not isinstance(self.non_microb_biomass, str):
            self.non_microb_biomass = str(self.non_microb_biomass)

        if self.non_microb_biomass_method is not None and not isinstance(self.non_microb_biomass_method, str):
            self.non_microb_biomass_method = str(self.non_microb_biomass_method)

        if self.non_min_nutr_regm is not None and not isinstance(self.non_min_nutr_regm, str):
            self.non_min_nutr_regm = str(self.non_min_nutr_regm)

        if self.org_carb is not None and not isinstance(self.org_carb, str):
            self.org_carb = str(self.org_carb)

        if self.org_matter is not None and not isinstance(self.org_matter, str):
            self.org_matter = str(self.org_matter)

        if self.org_nitro is not None and not isinstance(self.org_nitro, str):
            self.org_nitro = str(self.org_nitro)

        if self.org_nitro_method is not None and not isinstance(self.org_nitro_method, str):
            self.org_nitro_method = str(self.org_nitro_method)

        if self.org_particles is not None and not isinstance(self.org_particles, str):
            self.org_particles = str(self.org_particles)

        if self.organism_count is not None and not isinstance(self.organism_count, str):
            self.organism_count = str(self.organism_count)

        if self.other is not None and not isinstance(self.other, str):
            self.other = str(self.other)

        if self.other_samp_store_temp is not None and not isinstance(self.other_samp_store_temp, str):
            self.other_samp_store_temp = str(self.other_samp_store_temp)

        if self.other_treatment is not None and not isinstance(self.other_treatment, str):
            self.other_treatment = str(self.other_treatment)

        if self.oxygen is not None and not isinstance(self.oxygen, str):
            self.oxygen = str(self.oxygen)

        if self.oxygen_status is not None and not isinstance(self.oxygen_status, OxygenStatusEnum):
            self.oxygen_status = OxygenStatusEnum(self.oxygen_status)

        if self.part_org_carb is not None and not isinstance(self.part_org_carb, str):
            self.part_org_carb = str(self.part_org_carb)

        if self.part_org_nitro is not None and not isinstance(self.part_org_nitro, str):
            self.part_org_nitro = str(self.part_org_nitro)

        if self.particle_class is not None and not isinstance(self.particle_class, str):
            self.particle_class = str(self.particle_class)

        if self.pathogenicity is not None and not isinstance(self.pathogenicity, str):
            self.pathogenicity = str(self.pathogenicity)

        if self.perturbation is not None and not isinstance(self.perturbation, str):
            self.perturbation = str(self.perturbation)

        if self.pesticide_regm is not None and not isinstance(self.pesticide_regm, str):
            self.pesticide_regm = str(self.pesticide_regm)

        if self.petroleum_hydrocarb is not None and not isinstance(self.petroleum_hydrocarb, str):
            self.petroleum_hydrocarb = str(self.petroleum_hydrocarb)

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

        if self.ph_regm is not None and not isinstance(self.ph_regm, str):
            self.ph_regm = str(self.ph_regm)

        if self.phaeopigments is not None and not isinstance(self.phaeopigments, str):
            self.phaeopigments = str(self.phaeopigments)

        if self.phosphate is not None and not isinstance(self.phosphate, str):
            self.phosphate = str(self.phosphate)

        if self.phosplipid_fatt_acid is not None and not isinstance(self.phosplipid_fatt_acid, str):
            self.phosplipid_fatt_acid = str(self.phosplipid_fatt_acid)

        if self.photochemical_exposure is not None and not isinstance(self.photochemical_exposure, PhotochemicalExposureEnum):
            self.photochemical_exposure = PhotochemicalExposureEnum(self.photochemical_exposure)

        if self.photon_flux is not None and not isinstance(self.photon_flux, str):
            self.photon_flux = str(self.photon_flux)

        if self.porosity is not None and not isinstance(self.porosity, str):
            self.porosity = str(self.porosity)

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.pre_treatment is not None and not isinstance(self.pre_treatment, str):
            self.pre_treatment = str(self.pre_treatment)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.pressure_control is not None and not isinstance(self.pressure_control, str):
            self.pressure_control = str(self.pressure_control)

        if self.primary_prod is not None and not isinstance(self.primary_prod, str):
            self.primary_prod = str(self.primary_prod)

        if self.primary_treatment is not None and not isinstance(self.primary_treatment, str):
            self.primary_treatment = str(self.primary_treatment)

        if self.priority_order is not None and not isinstance(self.priority_order, float):
            self.priority_order = float(self.priority_order)

        if self.production_method is not None and not isinstance(self.production_method, str):
            self.production_method = str(self.production_method)

        if self.project is not None and not isinstance(self.project, int):
            self.project = int(self.project)

        if self.propagation is not None and not isinstance(self.propagation, str):
            self.propagation = str(self.propagation)

        if self.radiation_regm is not None and not isinstance(self.radiation_regm, str):
            self.radiation_regm = str(self.radiation_regm)

        if self.rainfall_regm is not None and not isinstance(self.rainfall_regm, str):
            self.rainfall_regm = str(self.rainfall_regm)

        if self.reactor_type is not None and not isinstance(self.reactor_type, str):
            self.reactor_type = str(self.reactor_type)

        if self.redox_potential is not None and not isinstance(self.redox_potential, str):
            self.redox_potential = str(self.redox_potential)

        if self.ref_biomaterial is not None and not isinstance(self.ref_biomaterial, str):
            self.ref_biomaterial = str(self.ref_biomaterial)

        if self.replicate_number is not None and not isinstance(self.replicate_number, int):
            self.replicate_number = int(self.replicate_number)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.salinity_method is not None and not isinstance(self.salinity_method, str):
            self.salinity_method = str(self.salinity_method)

        if self.salt_regm is not None and not isinstance(self.salt_regm, str):
            self.salt_regm = str(self.salt_regm)

        if self.biotic_relationship is not None and not isinstance(self.biotic_relationship, BioticRelationshipEnum):
            self.biotic_relationship = BioticRelationshipEnum(self.biotic_relationship)

        if self.samp_capt_status is not None and not isinstance(self.samp_capt_status, str):
            self.samp_capt_status = str(self.samp_capt_status)

        if self.samp_dis_stage is not None and not isinstance(self.samp_dis_stage, str):
            self.samp_dis_stage = str(self.samp_dis_stage)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, SampleStoreTempEnum):
            self.samp_store_temp = SampleStoreTempEnum(self.samp_store_temp)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if self.sample_name is not None and not isinstance(self.sample_name, str):
            self.sample_name = str(self.sample_name)

        if self.sample_processing is not None and not isinstance(self.sample_processing, str):
            self.sample_processing = str(self.sample_processing)

        if self.sampled_during is not None and not isinstance(self.sampled_during, SamplingActivityId):
            self.sampled_during = SamplingActivityId(self.sampled_during)

        if self.season_environment is not None and not isinstance(self.season_environment, str):
            self.season_environment = str(self.season_environment)

        if self.secondary_treatment is not None and not isinstance(self.secondary_treatment, str):
            self.secondary_treatment = str(self.secondary_treatment)

        if self.sewage_type is not None and not isinstance(self.sewage_type, str):
            self.sewage_type = str(self.sewage_type)

        if self.sieving is not None and not isinstance(self.sieving, str):
            self.sieving = str(self.sieving)

        if self.silicate is not None and not isinstance(self.silicate, str):
            self.silicate = str(self.silicate)

        if self.size_frac_low is not None and not isinstance(self.size_frac_low, str):
            self.size_frac_low = str(self.size_frac_low)

        if self.size_frac_up is not None and not isinstance(self.size_frac_up, str):
            self.size_frac_up = str(self.size_frac_up)

        if self.sludge_retent_time is not None and not isinstance(self.sludge_retent_time, str):
            self.sludge_retent_time = str(self.sludge_retent_time)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if self.solar_irradiance is not None and not isinstance(self.solar_irradiance, str):
            self.solar_irradiance = str(self.solar_irradiance)

        if self.soluble_inorg_mat is not None and not isinstance(self.soluble_inorg_mat, str):
            self.soluble_inorg_mat = str(self.soluble_inorg_mat)

        if self.soluble_org_mat is not None and not isinstance(self.soluble_org_mat, str):
            self.soluble_org_mat = str(self.soluble_org_mat)

        if self.soluble_react_phosp is not None and not isinstance(self.soluble_react_phosp, str):
            self.soluble_react_phosp = str(self.soluble_react_phosp)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        if self.standing_water_regm is not None and not isinstance(self.standing_water_regm, str):
            self.standing_water_regm = str(self.standing_water_regm)

        if self.start_date_inc is not None and not isinstance(self.start_date_inc, str):
            self.start_date_inc = str(self.start_date_inc)

        if self.storage_condition is not None and not isinstance(self.storage_condition, StorageConditionEnum):
            self.storage_condition = StorageConditionEnum(self.storage_condition)

        if self.storage_condition_other is not None and not isinstance(self.storage_condition_other, str):
            self.storage_condition_other = str(self.storage_condition_other)

        if self.subspecf_gen_lin is not None and not isinstance(self.subspecf_gen_lin, str):
            self.subspecf_gen_lin = str(self.subspecf_gen_lin)

        if self.sulfate is not None and not isinstance(self.sulfate, str):
            self.sulfate = str(self.sulfate)

        if self.sulfide is not None and not isinstance(self.sulfide, str):
            self.sulfide = str(self.sulfide)

        if self.suspend_part_matter is not None and not isinstance(self.suspend_part_matter, str):
            self.suspend_part_matter = str(self.suspend_part_matter)

        if self.suspend_solids is not None and not isinstance(self.suspend_solids, str):
            self.suspend_solids = str(self.suspend_solids)

        if self.synth_instrument is not None and not isinstance(self.synth_instrument, str):
            self.synth_instrument = str(self.synth_instrument)

        if self.synth_process is not None and not isinstance(self.synth_process, str):
            self.synth_process = str(self.synth_process)

        if self.synth_reagents is not None and not isinstance(self.synth_reagents, str):
            self.synth_reagents = str(self.synth_reagents)

        if self.technical_reps is not None and not isinstance(self.technical_reps, int):
            self.technical_reps = int(self.technical_reps)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.temperature_exposure is not None and not isinstance(self.temperature_exposure, str):
            self.temperature_exposure = str(self.temperature_exposure)

        if self.tertiary_treatment is not None and not isinstance(self.tertiary_treatment, str):
            self.tertiary_treatment = str(self.tertiary_treatment)

        if self.tidal_stage is not None and not isinstance(self.tidal_stage, TidalStageEnum):
            self.tidal_stage = TidalStageEnum(self.tidal_stage)

        if self.tiss_cult_growth_med is not None and not isinstance(self.tiss_cult_growth_med, str):
            self.tiss_cult_growth_med = str(self.tiss_cult_growth_med)

        if self.tot_carb is not None and not isinstance(self.tot_carb, str):
            self.tot_carb = str(self.tot_carb)

        if self.tot_depth_water_col is not None and not isinstance(self.tot_depth_water_col, str):
            self.tot_depth_water_col = str(self.tot_depth_water_col)

        if self.tot_diss_nitro is not None and not isinstance(self.tot_diss_nitro, str):
            self.tot_diss_nitro = str(self.tot_diss_nitro)

        if self.tot_inorg_nitro is not None and not isinstance(self.tot_inorg_nitro, str):
            self.tot_inorg_nitro = str(self.tot_inorg_nitro)

        if self.tot_nitro is not None and not isinstance(self.tot_nitro, str):
            self.tot_nitro = str(self.tot_nitro)

        if self.tot_nitro_cont_meth is not None and not isinstance(self.tot_nitro_cont_meth, str):
            self.tot_nitro_cont_meth = str(self.tot_nitro_cont_meth)

        if self.tot_nitro_content is not None and not isinstance(self.tot_nitro_content, str):
            self.tot_nitro_content = str(self.tot_nitro_content)

        if self.tot_org_c_meth is not None and not isinstance(self.tot_org_c_meth, str):
            self.tot_org_c_meth = str(self.tot_org_c_meth)

        if self.tot_org_carb is not None and not isinstance(self.tot_org_carb, str):
            self.tot_org_carb = str(self.tot_org_carb)

        if self.tot_part_carb is not None and not isinstance(self.tot_part_carb, str):
            self.tot_part_carb = str(self.tot_part_carb)

        if self.tot_phosp is not None and not isinstance(self.tot_phosp, str):
            self.tot_phosp = str(self.tot_phosp)

        if self.tot_phosphate is not None and not isinstance(self.tot_phosphate, str):
            self.tot_phosphate = str(self.tot_phosphate)

        if self.trophic_level is not None and not isinstance(self.trophic_level, TrophicLevelEnum):
            self.trophic_level = TrophicLevelEnum(self.trophic_level)

        if self.turbidity is not None and not isinstance(self.turbidity, str):
            self.turbidity = str(self.turbidity)

        if self.volatile_org_comp is not None and not isinstance(self.volatile_org_comp, str):
            self.volatile_org_comp = str(self.volatile_org_comp)

        if self.wastewater_type is not None and not isinstance(self.wastewater_type, str):
            self.wastewater_type = str(self.wastewater_type)

        if self.water_content is not None and not isinstance(self.water_content, str):
            self.water_content = str(self.water_content)

        if self.water_current is not None and not isinstance(self.water_current, str):
            self.water_current = str(self.water_current)

        if self.water_temp_regm is not None and not isinstance(self.water_temp_regm, str):
            self.water_temp_regm = str(self.water_temp_regm)

        if self.watering_regm is not None and not isinstance(self.watering_regm, str):
            self.watering_regm = str(self.watering_regm)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PlantSample(Sample):
    """
    A sample containing plant material.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["PlantSample"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:PlantSample"
    class_name: ClassVar[str] = "PlantSample"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.PlantSample

    id: Union[str, PlantSampleId] = None
    name: str = None
    analysis_type: str = None
    latitude: float = None
    longitude: float = None
    plant_common_name: str = None
    plant_struc: Union[str, "PlantStructureEnum"] = None
    plant_taxid: str = None
    air_temp_regm: Optional[str] = None
    ances_data: Optional[str] = None
    biol_stat: Optional[Union[str, "BiolStatEnum"]] = None
    biotic_regm: Optional[str] = None
    chem_administration: Optional[str] = None
    chem_mutagen: Optional[str] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    experimental_factor: Optional[str] = None
    experimental_factor_other: Optional[str] = None
    extraction_method: Optional[str] = None
    external_identifiers: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    fertilizer_regm: Optional[str] = None
    fungicide_regm: Optional[str] = None
    gaseous_environment: Optional[str] = None
    genetic_mod: Optional[str] = None
    gravity: Optional[str] = None
    growth_habit: Optional[Union[str, "GrowthHabitEnum"]] = None
    growth_hormone_regm: Optional[str] = None
    herbicide_regm: Optional[str] = None
    host_height: Optional[str] = None
    host_length: Optional[str] = None
    host_life_stage: Optional[str] = None
    humidity_regm: Optional[str] = None
    isotope_exposure: Optional[str] = None
    light_regm: Optional[str] = None
    mechanical_damage: Optional[str] = None
    method_development: Optional[str] = None
    mineral_nutr_regm: Optional[str] = None
    misc_param: Optional[str] = None
    non_microb_biomass: Optional[str] = None
    non_microb_biomass_method: Optional[str] = None
    non_min_nutr_regm: Optional[str] = None
    other: Optional[str] = None
    other_samp_store_temp: Optional[str] = None
    other_storage_condt: Optional[str] = None
    other_treatment: Optional[str] = None
    pesticide_regm: Optional[str] = None
    ph_regm: Optional[str] = None
    plant_age: Optional[str] = None
    plant_disease_stat: Optional[str] = None
    plant_dry_mass: Optional[str] = None
    plant_genotype: Optional[str] = None
    plant_growth_med: Optional[str] = None
    plant_sex: Optional[Union[str, "PlantSexEnum"]] = None
    plant_wet_mass: Optional[str] = None
    project: Optional[int] = None
    rainfall_regm: Optional[str] = None
    replicate_number: Optional[int] = None
    root_cond: Optional[str] = None
    root_med_carbon: Optional[str] = None
    root_med_macronutr: Optional[str] = None
    root_med_micronutr: Optional[str] = None
    root_med_ph: Optional[float] = None
    root_med_regl: Optional[str] = None
    root_med_solid: Optional[str] = None
    root_med_suppl: Optional[str] = None
    salinity: Optional[str] = None
    salinity_method: Optional[str] = None
    salt_regm: Optional[str] = None
    sample_link: Optional[str] = None
    sample_name: Optional[str] = None
    sample_processing: Optional[str] = None
    samp_store_temp: Optional[Union[str, "SampleStoreTempEnum"]] = None
    sampled_during: Optional[Union[str, SamplingActivityId]] = None
    source_mat_id: Optional[str] = None
    standing_water_regm: Optional[str] = None
    start_date_inc: Optional[str] = None
    storage_condition: Optional[Union[str, "StorageConditionEnum"]] = None
    storage_condition_other: Optional[str] = None
    technical_reps: Optional[int] = None
    temp: Optional[str] = None
    water_temp_regm: Optional[str] = None
    watering_regm: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlantSampleId):
            self.id = PlantSampleId(self.id)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, str):
            self.analysis_type = str(self.analysis_type)

        if self._is_empty(self.latitude):
            self.MissingRequiredField("latitude")
        if not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self._is_empty(self.longitude):
            self.MissingRequiredField("longitude")
        if not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self._is_empty(self.plant_common_name):
            self.MissingRequiredField("plant_common_name")
        if not isinstance(self.plant_common_name, str):
            self.plant_common_name = str(self.plant_common_name)

        if self._is_empty(self.plant_struc):
            self.MissingRequiredField("plant_struc")
        if not isinstance(self.plant_struc, PlantStructureEnum):
            self.plant_struc = PlantStructureEnum(self.plant_struc)

        if self._is_empty(self.plant_taxid):
            self.MissingRequiredField("plant_taxid")
        if not isinstance(self.plant_taxid, str):
            self.plant_taxid = str(self.plant_taxid)

        if self.air_temp_regm is not None and not isinstance(self.air_temp_regm, str):
            self.air_temp_regm = str(self.air_temp_regm)

        if self.ances_data is not None and not isinstance(self.ances_data, str):
            self.ances_data = str(self.ances_data)

        if self.biol_stat is not None and not isinstance(self.biol_stat, BiolStatEnum):
            self.biol_stat = BiolStatEnum(self.biol_stat)

        if self.biotic_regm is not None and not isinstance(self.biotic_regm, str):
            self.biotic_regm = str(self.biotic_regm)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.chem_mutagen is not None and not isinstance(self.chem_mutagen, str):
            self.chem_mutagen = str(self.chem_mutagen)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.experimental_factor_other is not None and not isinstance(self.experimental_factor_other, str):
            self.experimental_factor_other = str(self.experimental_factor_other)

        if self.extraction_method is not None and not isinstance(self.extraction_method, str):
            self.extraction_method = str(self.extraction_method)

        if not isinstance(self.external_identifiers, list):
            self.external_identifiers = [self.external_identifiers] if self.external_identifiers is not None else []
        self.external_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.external_identifiers]

        if self.fertilizer_regm is not None and not isinstance(self.fertilizer_regm, str):
            self.fertilizer_regm = str(self.fertilizer_regm)

        if self.fungicide_regm is not None and not isinstance(self.fungicide_regm, str):
            self.fungicide_regm = str(self.fungicide_regm)

        if self.gaseous_environment is not None and not isinstance(self.gaseous_environment, str):
            self.gaseous_environment = str(self.gaseous_environment)

        if self.genetic_mod is not None and not isinstance(self.genetic_mod, str):
            self.genetic_mod = str(self.genetic_mod)

        if self.gravity is not None and not isinstance(self.gravity, str):
            self.gravity = str(self.gravity)

        if self.growth_habit is not None and not isinstance(self.growth_habit, GrowthHabitEnum):
            self.growth_habit = GrowthHabitEnum(self.growth_habit)

        if self.growth_hormone_regm is not None and not isinstance(self.growth_hormone_regm, str):
            self.growth_hormone_regm = str(self.growth_hormone_regm)

        if self.herbicide_regm is not None and not isinstance(self.herbicide_regm, str):
            self.herbicide_regm = str(self.herbicide_regm)

        if self.host_height is not None and not isinstance(self.host_height, str):
            self.host_height = str(self.host_height)

        if self.host_length is not None and not isinstance(self.host_length, str):
            self.host_length = str(self.host_length)

        if self.host_life_stage is not None and not isinstance(self.host_life_stage, str):
            self.host_life_stage = str(self.host_life_stage)

        if self.humidity_regm is not None and not isinstance(self.humidity_regm, str):
            self.humidity_regm = str(self.humidity_regm)

        if self.isotope_exposure is not None and not isinstance(self.isotope_exposure, str):
            self.isotope_exposure = str(self.isotope_exposure)

        if self.light_regm is not None and not isinstance(self.light_regm, str):
            self.light_regm = str(self.light_regm)

        if self.mechanical_damage is not None and not isinstance(self.mechanical_damage, str):
            self.mechanical_damage = str(self.mechanical_damage)

        if self.method_development is not None and not isinstance(self.method_development, str):
            self.method_development = str(self.method_development)

        if self.mineral_nutr_regm is not None and not isinstance(self.mineral_nutr_regm, str):
            self.mineral_nutr_regm = str(self.mineral_nutr_regm)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        if self.non_microb_biomass is not None and not isinstance(self.non_microb_biomass, str):
            self.non_microb_biomass = str(self.non_microb_biomass)

        if self.non_microb_biomass_method is not None and not isinstance(self.non_microb_biomass_method, str):
            self.non_microb_biomass_method = str(self.non_microb_biomass_method)

        if self.non_min_nutr_regm is not None and not isinstance(self.non_min_nutr_regm, str):
            self.non_min_nutr_regm = str(self.non_min_nutr_regm)

        if self.other is not None and not isinstance(self.other, str):
            self.other = str(self.other)

        if self.other_samp_store_temp is not None and not isinstance(self.other_samp_store_temp, str):
            self.other_samp_store_temp = str(self.other_samp_store_temp)

        if self.other_storage_condt is not None and not isinstance(self.other_storage_condt, str):
            self.other_storage_condt = str(self.other_storage_condt)

        if self.other_treatment is not None and not isinstance(self.other_treatment, str):
            self.other_treatment = str(self.other_treatment)

        if self.pesticide_regm is not None and not isinstance(self.pesticide_regm, str):
            self.pesticide_regm = str(self.pesticide_regm)

        if self.ph_regm is not None and not isinstance(self.ph_regm, str):
            self.ph_regm = str(self.ph_regm)

        if self.plant_age is not None and not isinstance(self.plant_age, str):
            self.plant_age = str(self.plant_age)

        if self.plant_disease_stat is not None and not isinstance(self.plant_disease_stat, str):
            self.plant_disease_stat = str(self.plant_disease_stat)

        if self.plant_dry_mass is not None and not isinstance(self.plant_dry_mass, str):
            self.plant_dry_mass = str(self.plant_dry_mass)

        if self.plant_genotype is not None and not isinstance(self.plant_genotype, str):
            self.plant_genotype = str(self.plant_genotype)

        if self.plant_growth_med is not None and not isinstance(self.plant_growth_med, str):
            self.plant_growth_med = str(self.plant_growth_med)

        if self.plant_sex is not None and not isinstance(self.plant_sex, PlantSexEnum):
            self.plant_sex = PlantSexEnum(self.plant_sex)

        if self.plant_wet_mass is not None and not isinstance(self.plant_wet_mass, str):
            self.plant_wet_mass = str(self.plant_wet_mass)

        if self.project is not None and not isinstance(self.project, int):
            self.project = int(self.project)

        if self.rainfall_regm is not None and not isinstance(self.rainfall_regm, str):
            self.rainfall_regm = str(self.rainfall_regm)

        if self.replicate_number is not None and not isinstance(self.replicate_number, int):
            self.replicate_number = int(self.replicate_number)

        if self.root_cond is not None and not isinstance(self.root_cond, str):
            self.root_cond = str(self.root_cond)

        if self.root_med_carbon is not None and not isinstance(self.root_med_carbon, str):
            self.root_med_carbon = str(self.root_med_carbon)

        if self.root_med_macronutr is not None and not isinstance(self.root_med_macronutr, str):
            self.root_med_macronutr = str(self.root_med_macronutr)

        if self.root_med_micronutr is not None and not isinstance(self.root_med_micronutr, str):
            self.root_med_micronutr = str(self.root_med_micronutr)

        if self.root_med_ph is not None and not isinstance(self.root_med_ph, float):
            self.root_med_ph = float(self.root_med_ph)

        if self.root_med_regl is not None and not isinstance(self.root_med_regl, str):
            self.root_med_regl = str(self.root_med_regl)

        if self.root_med_solid is not None and not isinstance(self.root_med_solid, str):
            self.root_med_solid = str(self.root_med_solid)

        if self.root_med_suppl is not None and not isinstance(self.root_med_suppl, str):
            self.root_med_suppl = str(self.root_med_suppl)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.salinity_method is not None and not isinstance(self.salinity_method, str):
            self.salinity_method = str(self.salinity_method)

        if self.salt_regm is not None and not isinstance(self.salt_regm, str):
            self.salt_regm = str(self.salt_regm)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if self.sample_name is not None and not isinstance(self.sample_name, str):
            self.sample_name = str(self.sample_name)

        if self.sample_processing is not None and not isinstance(self.sample_processing, str):
            self.sample_processing = str(self.sample_processing)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, SampleStoreTempEnum):
            self.samp_store_temp = SampleStoreTempEnum(self.samp_store_temp)

        if self.sampled_during is not None and not isinstance(self.sampled_during, SamplingActivityId):
            self.sampled_during = SamplingActivityId(self.sampled_during)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        if self.standing_water_regm is not None and not isinstance(self.standing_water_regm, str):
            self.standing_water_regm = str(self.standing_water_regm)

        if self.start_date_inc is not None and not isinstance(self.start_date_inc, str):
            self.start_date_inc = str(self.start_date_inc)

        if self.storage_condition is not None and not isinstance(self.storage_condition, StorageConditionEnum):
            self.storage_condition = StorageConditionEnum(self.storage_condition)

        if self.storage_condition_other is not None and not isinstance(self.storage_condition_other, str):
            self.storage_condition_other = str(self.storage_condition_other)

        if self.technical_reps is not None and not isinstance(self.technical_reps, int):
            self.technical_reps = int(self.technical_reps)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.water_temp_regm is not None and not isinstance(self.water_temp_regm, str):
            self.water_temp_regm = str(self.water_temp_regm)

        if self.watering_regm is not None and not isinstance(self.watering_regm, str):
            self.watering_regm = str(self.watering_regm)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PureCultureSample(Sample):
    """
    A sample of a culture containing a single organism.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["PureCultureSample"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:PureCultureSample"
    class_name: ClassVar[str] = "PureCultureSample"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.PureCultureSample

    id: Union[str, PureCultureSampleId] = None
    name: str = None
    analysis_type: str = None
    growth_medium: str = None
    host_common_name: str = None
    host_taxid: str = None
    isol_growth_condt: str = None
    start_date_inc: str = None
    air_temp_regm: Optional[str] = None
    biotic_regm: Optional[str] = None
    chem_administration: Optional[str] = None
    encoded_traits: Optional[str] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    experimental_factor: Optional[str] = None
    experimental_factor_other: Optional[str] = None
    extraction_method: Optional[str] = None
    external_identifiers: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    filter_method: Optional[str] = None
    gaseous_environment: Optional[str] = None
    genetic_mod: Optional[str] = None
    host_spec_range: Optional[str] = None
    humidity_regm: Optional[str] = None
    isotope_exposure: Optional[str] = None
    light_regm: Optional[str] = None
    method_development: Optional[str] = None
    non_microb_biomass: Optional[str] = None
    non_microb_biomass_method: Optional[str] = None
    other: Optional[str] = None
    other_samp_store_temp: Optional[str] = None
    other_storage_condt: Optional[str] = None
    other_treatment: Optional[str] = None
    oxygen_status: Optional[Union[str, "OxygenStatusEnum"]] = None
    pathogenicity: Optional[str] = None
    project: Optional[int] = None
    propagation: Optional[str] = None
    ref_biomaterial: Optional[str] = None
    replicate_number: Optional[int] = None
    biotic_relationship: Optional[Union[str, "BioticRelationshipEnum"]] = None
    samp_store_temp: Optional[Union[str, "SampleStoreTempEnum"]] = None
    sample_link: Optional[str] = None
    sample_name: Optional[str] = None
    sample_processing: Optional[str] = None
    sampled_during: Optional[Union[str, SamplingActivityId]] = None
    source_mat_id: Optional[str] = None
    storage_condition: Optional[Union[str, "StorageConditionEnum"]] = None
    storage_condition_other: Optional[str] = None
    subspecf_gen_lin: Optional[str] = None
    technical_reps: Optional[int] = None
    trophic_level: Optional[Union[str, "TrophicLevelEnum"]] = None
    watering_regm: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PureCultureSampleId):
            self.id = PureCultureSampleId(self.id)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, str):
            self.analysis_type = str(self.analysis_type)

        if self._is_empty(self.growth_medium):
            self.MissingRequiredField("growth_medium")
        if not isinstance(self.growth_medium, str):
            self.growth_medium = str(self.growth_medium)

        if self._is_empty(self.host_common_name):
            self.MissingRequiredField("host_common_name")
        if not isinstance(self.host_common_name, str):
            self.host_common_name = str(self.host_common_name)

        if self._is_empty(self.host_taxid):
            self.MissingRequiredField("host_taxid")
        if not isinstance(self.host_taxid, str):
            self.host_taxid = str(self.host_taxid)

        if self._is_empty(self.isol_growth_condt):
            self.MissingRequiredField("isol_growth_condt")
        if not isinstance(self.isol_growth_condt, str):
            self.isol_growth_condt = str(self.isol_growth_condt)

        if self._is_empty(self.start_date_inc):
            self.MissingRequiredField("start_date_inc")
        if not isinstance(self.start_date_inc, str):
            self.start_date_inc = str(self.start_date_inc)

        if self.air_temp_regm is not None and not isinstance(self.air_temp_regm, str):
            self.air_temp_regm = str(self.air_temp_regm)

        if self.biotic_regm is not None and not isinstance(self.biotic_regm, str):
            self.biotic_regm = str(self.biotic_regm)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.encoded_traits is not None and not isinstance(self.encoded_traits, str):
            self.encoded_traits = str(self.encoded_traits)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.experimental_factor_other is not None and not isinstance(self.experimental_factor_other, str):
            self.experimental_factor_other = str(self.experimental_factor_other)

        if self.extraction_method is not None and not isinstance(self.extraction_method, str):
            self.extraction_method = str(self.extraction_method)

        if not isinstance(self.external_identifiers, list):
            self.external_identifiers = [self.external_identifiers] if self.external_identifiers is not None else []
        self.external_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.external_identifiers]

        if self.filter_method is not None and not isinstance(self.filter_method, str):
            self.filter_method = str(self.filter_method)

        if self.gaseous_environment is not None and not isinstance(self.gaseous_environment, str):
            self.gaseous_environment = str(self.gaseous_environment)

        if self.genetic_mod is not None and not isinstance(self.genetic_mod, str):
            self.genetic_mod = str(self.genetic_mod)

        if self.host_spec_range is not None and not isinstance(self.host_spec_range, str):
            self.host_spec_range = str(self.host_spec_range)

        if self.humidity_regm is not None and not isinstance(self.humidity_regm, str):
            self.humidity_regm = str(self.humidity_regm)

        if self.isotope_exposure is not None and not isinstance(self.isotope_exposure, str):
            self.isotope_exposure = str(self.isotope_exposure)

        if self.light_regm is not None and not isinstance(self.light_regm, str):
            self.light_regm = str(self.light_regm)

        if self.method_development is not None and not isinstance(self.method_development, str):
            self.method_development = str(self.method_development)

        if self.non_microb_biomass is not None and not isinstance(self.non_microb_biomass, str):
            self.non_microb_biomass = str(self.non_microb_biomass)

        if self.non_microb_biomass_method is not None and not isinstance(self.non_microb_biomass_method, str):
            self.non_microb_biomass_method = str(self.non_microb_biomass_method)

        if self.other is not None and not isinstance(self.other, str):
            self.other = str(self.other)

        if self.other_samp_store_temp is not None and not isinstance(self.other_samp_store_temp, str):
            self.other_samp_store_temp = str(self.other_samp_store_temp)

        if self.other_storage_condt is not None and not isinstance(self.other_storage_condt, str):
            self.other_storage_condt = str(self.other_storage_condt)

        if self.other_treatment is not None and not isinstance(self.other_treatment, str):
            self.other_treatment = str(self.other_treatment)

        if self.oxygen_status is not None and not isinstance(self.oxygen_status, OxygenStatusEnum):
            self.oxygen_status = OxygenStatusEnum(self.oxygen_status)

        if self.pathogenicity is not None and not isinstance(self.pathogenicity, str):
            self.pathogenicity = str(self.pathogenicity)

        if self.project is not None and not isinstance(self.project, int):
            self.project = int(self.project)

        if self.propagation is not None and not isinstance(self.propagation, str):
            self.propagation = str(self.propagation)

        if self.ref_biomaterial is not None and not isinstance(self.ref_biomaterial, str):
            self.ref_biomaterial = str(self.ref_biomaterial)

        if self.replicate_number is not None and not isinstance(self.replicate_number, int):
            self.replicate_number = int(self.replicate_number)

        if self.biotic_relationship is not None and not isinstance(self.biotic_relationship, BioticRelationshipEnum):
            self.biotic_relationship = BioticRelationshipEnum(self.biotic_relationship)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, SampleStoreTempEnum):
            self.samp_store_temp = SampleStoreTempEnum(self.samp_store_temp)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if self.sample_name is not None and not isinstance(self.sample_name, str):
            self.sample_name = str(self.sample_name)

        if self.sample_processing is not None and not isinstance(self.sample_processing, str):
            self.sample_processing = str(self.sample_processing)

        if self.sampled_during is not None and not isinstance(self.sampled_during, SamplingActivityId):
            self.sampled_during = SamplingActivityId(self.sampled_during)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        if self.storage_condition is not None and not isinstance(self.storage_condition, StorageConditionEnum):
            self.storage_condition = StorageConditionEnum(self.storage_condition)

        if self.storage_condition_other is not None and not isinstance(self.storage_condition_other, str):
            self.storage_condition_other = str(self.storage_condition_other)

        if self.subspecf_gen_lin is not None and not isinstance(self.subspecf_gen_lin, str):
            self.subspecf_gen_lin = str(self.subspecf_gen_lin)

        if self.technical_reps is not None and not isinstance(self.technical_reps, int):
            self.technical_reps = int(self.technical_reps)

        if self.trophic_level is not None and not isinstance(self.trophic_level, TrophicLevelEnum):
            self.trophic_level = TrophicLevelEnum(self.trophic_level)

        if self.watering_regm is not None and not isinstance(self.watering_regm, str):
            self.watering_regm = str(self.watering_regm)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SedimentSample(Sample):
    """
    A sample of sediment collected from the environment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["SedimentSample"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:SedimentSample"
    class_name: ClassVar[str] = "SedimentSample"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.SedimentSample

    id: Union[str, SedimentSampleId] = None
    name: str = None
    analysis_type: str = None
    depth: str = None
    latitude: float = None
    longitude: float = None
    air_temp_regm: Optional[str] = None
    alkalinity: Optional[str] = None
    alkalinity_method: Optional[str] = None
    alkyl_diethers: Optional[str] = None
    aminopept_act: Optional[str] = None
    ammonium: Optional[str] = None
    bacteria_carb_prod: Optional[str] = None
    biotic_regm: Optional[str] = None
    bishomohopanol: Optional[str] = None
    bromide: Optional[str] = None
    calcium: Optional[str] = None
    carb_nitro_ratio: Optional[str] = None
    chem_administration: Optional[str] = None
    chloride: Optional[str] = None
    chlorophyll: Optional[str] = None
    density: Optional[str] = None
    diether_lipids: Optional[str] = None
    diss_carb_dioxide: Optional[str] = None
    diss_hydrogen: Optional[str] = None
    diss_inorg_carb: Optional[str] = None
    diss_org_carb: Optional[str] = None
    diss_org_nitro: Optional[str] = None
    diss_oxygen: Optional[str] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    experimental_factor: Optional[str] = None
    experimental_factor_other: Optional[str] = None
    extraction_method: Optional[str] = None
    external_identifiers: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    gaseous_environment: Optional[str] = None
    glucosidase_act: Optional[str] = None
    humidity_regm: Optional[str] = None
    isotope_exposure: Optional[str] = None
    light_regm: Optional[str] = None
    magnesium: Optional[str] = None
    mean_frict_vel: Optional[str] = None
    mean_peak_frict_vel: Optional[str] = None
    methane: Optional[str] = None
    method_development: Optional[str] = None
    micro_biomass_c_meth: Optional[str] = None
    micro_biomass_n_meth: Optional[str] = None
    microbial_biomass: Optional[str] = None
    microbial_biomass_c: Optional[str] = None
    microbial_biomass_meth: Optional[str] = None
    microbial_biomass_n: Optional[str] = None
    misc_param: Optional[str] = None
    n_alkanes: Optional[str] = None
    nitrate: Optional[str] = None
    nitrite: Optional[str] = None
    nitro: Optional[str] = None
    non_microb_biomass: Optional[str] = None
    non_microb_biomass_method: Optional[str] = None
    org_carb: Optional[str] = None
    org_matter: Optional[str] = None
    org_nitro: Optional[str] = None
    org_nitro_method: Optional[str] = None
    other: Optional[str] = None
    other_samp_store_temp: Optional[str] = None
    other_storage_condt: Optional[str] = None
    other_treatment: Optional[str] = None
    oxygen_status: Optional[Union[str, "OxygenStatusEnum"]] = None
    part_org_carb: Optional[str] = None
    particle_class: Optional[str] = None
    perturbation: Optional[str] = None
    petroleum_hydrocarb: Optional[str] = None
    ph: Optional[float] = None
    ph_meth: Optional[str] = None
    phaeopigments: Optional[str] = None
    phosphate: Optional[str] = None
    phosplipid_fatt_acid: Optional[str] = None
    porosity: Optional[str] = None
    potassium: Optional[str] = None
    pressure: Optional[str] = None
    project: Optional[int] = None
    redox_potential: Optional[str] = None
    replicate_number: Optional[int] = None
    salinity: Optional[str] = None
    salinity_method: Optional[str] = None
    sample_link: Optional[str] = None
    sample_name: Optional[str] = None
    sample_processing: Optional[str] = None
    biotic_relationship: Optional[Union[str, "BioticRelationshipEnum"]] = None
    samp_store_temp: Optional[Union[str, "SampleStoreTempEnum"]] = None
    sampled_during: Optional[Union[str, SamplingActivityId]] = None
    sediment_type: Optional[Union[str, "SedimentTypeEnum"]] = None
    sieving: Optional[str] = None
    silicate: Optional[str] = None
    sodium: Optional[str] = None
    source_mat_id: Optional[str] = None
    start_date_inc: Optional[str] = None
    storage_condition: Optional[Union[str, "StorageConditionEnum"]] = None
    storage_condition_other: Optional[str] = None
    sulfate: Optional[str] = None
    sulfide: Optional[str] = None
    technical_reps: Optional[int] = None
    temp: Optional[str] = None
    tidal_stage: Optional[Union[str, "TidalStageEnum"]] = None
    tot_carb: Optional[str] = None
    tot_depth_water_col: Optional[str] = None
    tot_nitro_cont_meth: Optional[str] = None
    tot_nitro_content: Optional[str] = None
    tot_org_c_meth: Optional[str] = None
    tot_org_carb: Optional[str] = None
    turbidity: Optional[str] = None
    water_content: Optional[str] = None
    water_content_meth: Optional[str] = None
    watering_regm: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SedimentSampleId):
            self.id = SedimentSampleId(self.id)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, str):
            self.analysis_type = str(self.analysis_type)

        if self._is_empty(self.depth):
            self.MissingRequiredField("depth")
        if not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self._is_empty(self.latitude):
            self.MissingRequiredField("latitude")
        if not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self._is_empty(self.longitude):
            self.MissingRequiredField("longitude")
        if not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self.air_temp_regm is not None and not isinstance(self.air_temp_regm, str):
            self.air_temp_regm = str(self.air_temp_regm)

        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.alkalinity_method is not None and not isinstance(self.alkalinity_method, str):
            self.alkalinity_method = str(self.alkalinity_method)

        if self.alkyl_diethers is not None and not isinstance(self.alkyl_diethers, str):
            self.alkyl_diethers = str(self.alkyl_diethers)

        if self.aminopept_act is not None and not isinstance(self.aminopept_act, str):
            self.aminopept_act = str(self.aminopept_act)

        if self.ammonium is not None and not isinstance(self.ammonium, str):
            self.ammonium = str(self.ammonium)

        if self.bacteria_carb_prod is not None and not isinstance(self.bacteria_carb_prod, str):
            self.bacteria_carb_prod = str(self.bacteria_carb_prod)

        if self.biotic_regm is not None and not isinstance(self.biotic_regm, str):
            self.biotic_regm = str(self.biotic_regm)

        if self.bishomohopanol is not None and not isinstance(self.bishomohopanol, str):
            self.bishomohopanol = str(self.bishomohopanol)

        if self.bromide is not None and not isinstance(self.bromide, str):
            self.bromide = str(self.bromide)

        if self.calcium is not None and not isinstance(self.calcium, str):
            self.calcium = str(self.calcium)

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, str):
            self.carb_nitro_ratio = str(self.carb_nitro_ratio)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.chlorophyll is not None and not isinstance(self.chlorophyll, str):
            self.chlorophyll = str(self.chlorophyll)

        if self.density is not None and not isinstance(self.density, str):
            self.density = str(self.density)

        if self.diether_lipids is not None and not isinstance(self.diether_lipids, str):
            self.diether_lipids = str(self.diether_lipids)

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, str):
            self.diss_carb_dioxide = str(self.diss_carb_dioxide)

        if self.diss_hydrogen is not None and not isinstance(self.diss_hydrogen, str):
            self.diss_hydrogen = str(self.diss_hydrogen)

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, str):
            self.diss_inorg_carb = str(self.diss_inorg_carb)

        if self.diss_org_carb is not None and not isinstance(self.diss_org_carb, str):
            self.diss_org_carb = str(self.diss_org_carb)

        if self.diss_org_nitro is not None and not isinstance(self.diss_org_nitro, str):
            self.diss_org_nitro = str(self.diss_org_nitro)

        if self.diss_oxygen is not None and not isinstance(self.diss_oxygen, str):
            self.diss_oxygen = str(self.diss_oxygen)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.experimental_factor_other is not None and not isinstance(self.experimental_factor_other, str):
            self.experimental_factor_other = str(self.experimental_factor_other)

        if self.extraction_method is not None and not isinstance(self.extraction_method, str):
            self.extraction_method = str(self.extraction_method)

        if not isinstance(self.external_identifiers, list):
            self.external_identifiers = [self.external_identifiers] if self.external_identifiers is not None else []
        self.external_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.external_identifiers]

        if self.gaseous_environment is not None and not isinstance(self.gaseous_environment, str):
            self.gaseous_environment = str(self.gaseous_environment)

        if self.glucosidase_act is not None and not isinstance(self.glucosidase_act, str):
            self.glucosidase_act = str(self.glucosidase_act)

        if self.humidity_regm is not None and not isinstance(self.humidity_regm, str):
            self.humidity_regm = str(self.humidity_regm)

        if self.isotope_exposure is not None and not isinstance(self.isotope_exposure, str):
            self.isotope_exposure = str(self.isotope_exposure)

        if self.light_regm is not None and not isinstance(self.light_regm, str):
            self.light_regm = str(self.light_regm)

        if self.magnesium is not None and not isinstance(self.magnesium, str):
            self.magnesium = str(self.magnesium)

        if self.mean_frict_vel is not None and not isinstance(self.mean_frict_vel, str):
            self.mean_frict_vel = str(self.mean_frict_vel)

        if self.mean_peak_frict_vel is not None and not isinstance(self.mean_peak_frict_vel, str):
            self.mean_peak_frict_vel = str(self.mean_peak_frict_vel)

        if self.methane is not None and not isinstance(self.methane, str):
            self.methane = str(self.methane)

        if self.method_development is not None and not isinstance(self.method_development, str):
            self.method_development = str(self.method_development)

        if self.micro_biomass_c_meth is not None and not isinstance(self.micro_biomass_c_meth, str):
            self.micro_biomass_c_meth = str(self.micro_biomass_c_meth)

        if self.micro_biomass_n_meth is not None and not isinstance(self.micro_biomass_n_meth, str):
            self.micro_biomass_n_meth = str(self.micro_biomass_n_meth)

        if self.microbial_biomass is not None and not isinstance(self.microbial_biomass, str):
            self.microbial_biomass = str(self.microbial_biomass)

        if self.microbial_biomass_c is not None and not isinstance(self.microbial_biomass_c, str):
            self.microbial_biomass_c = str(self.microbial_biomass_c)

        if self.microbial_biomass_meth is not None and not isinstance(self.microbial_biomass_meth, str):
            self.microbial_biomass_meth = str(self.microbial_biomass_meth)

        if self.microbial_biomass_n is not None and not isinstance(self.microbial_biomass_n, str):
            self.microbial_biomass_n = str(self.microbial_biomass_n)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        if self.n_alkanes is not None and not isinstance(self.n_alkanes, str):
            self.n_alkanes = str(self.n_alkanes)

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if self.nitrite is not None and not isinstance(self.nitrite, str):
            self.nitrite = str(self.nitrite)

        if self.nitro is not None and not isinstance(self.nitro, str):
            self.nitro = str(self.nitro)

        if self.non_microb_biomass is not None and not isinstance(self.non_microb_biomass, str):
            self.non_microb_biomass = str(self.non_microb_biomass)

        if self.non_microb_biomass_method is not None and not isinstance(self.non_microb_biomass_method, str):
            self.non_microb_biomass_method = str(self.non_microb_biomass_method)

        if self.org_carb is not None and not isinstance(self.org_carb, str):
            self.org_carb = str(self.org_carb)

        if self.org_matter is not None and not isinstance(self.org_matter, str):
            self.org_matter = str(self.org_matter)

        if self.org_nitro is not None and not isinstance(self.org_nitro, str):
            self.org_nitro = str(self.org_nitro)

        if self.org_nitro_method is not None and not isinstance(self.org_nitro_method, str):
            self.org_nitro_method = str(self.org_nitro_method)

        if self.other is not None and not isinstance(self.other, str):
            self.other = str(self.other)

        if self.other_samp_store_temp is not None and not isinstance(self.other_samp_store_temp, str):
            self.other_samp_store_temp = str(self.other_samp_store_temp)

        if self.other_storage_condt is not None and not isinstance(self.other_storage_condt, str):
            self.other_storage_condt = str(self.other_storage_condt)

        if self.other_treatment is not None and not isinstance(self.other_treatment, str):
            self.other_treatment = str(self.other_treatment)

        if self.oxygen_status is not None and not isinstance(self.oxygen_status, OxygenStatusEnum):
            self.oxygen_status = OxygenStatusEnum(self.oxygen_status)

        if self.part_org_carb is not None and not isinstance(self.part_org_carb, str):
            self.part_org_carb = str(self.part_org_carb)

        if self.particle_class is not None and not isinstance(self.particle_class, str):
            self.particle_class = str(self.particle_class)

        if self.perturbation is not None and not isinstance(self.perturbation, str):
            self.perturbation = str(self.perturbation)

        if self.petroleum_hydrocarb is not None and not isinstance(self.petroleum_hydrocarb, str):
            self.petroleum_hydrocarb = str(self.petroleum_hydrocarb)

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

        if self.phaeopigments is not None and not isinstance(self.phaeopigments, str):
            self.phaeopigments = str(self.phaeopigments)

        if self.phosphate is not None and not isinstance(self.phosphate, str):
            self.phosphate = str(self.phosphate)

        if self.phosplipid_fatt_acid is not None and not isinstance(self.phosplipid_fatt_acid, str):
            self.phosplipid_fatt_acid = str(self.phosplipid_fatt_acid)

        if self.porosity is not None and not isinstance(self.porosity, str):
            self.porosity = str(self.porosity)

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.project is not None and not isinstance(self.project, int):
            self.project = int(self.project)

        if self.redox_potential is not None and not isinstance(self.redox_potential, str):
            self.redox_potential = str(self.redox_potential)

        if self.replicate_number is not None and not isinstance(self.replicate_number, int):
            self.replicate_number = int(self.replicate_number)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.salinity_method is not None and not isinstance(self.salinity_method, str):
            self.salinity_method = str(self.salinity_method)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if self.sample_name is not None and not isinstance(self.sample_name, str):
            self.sample_name = str(self.sample_name)

        if self.sample_processing is not None and not isinstance(self.sample_processing, str):
            self.sample_processing = str(self.sample_processing)

        if self.biotic_relationship is not None and not isinstance(self.biotic_relationship, BioticRelationshipEnum):
            self.biotic_relationship = BioticRelationshipEnum(self.biotic_relationship)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, SampleStoreTempEnum):
            self.samp_store_temp = SampleStoreTempEnum(self.samp_store_temp)

        if self.sampled_during is not None and not isinstance(self.sampled_during, SamplingActivityId):
            self.sampled_during = SamplingActivityId(self.sampled_during)

        if self.sediment_type is not None and not isinstance(self.sediment_type, SedimentTypeEnum):
            self.sediment_type = SedimentTypeEnum(self.sediment_type)

        if self.sieving is not None and not isinstance(self.sieving, str):
            self.sieving = str(self.sieving)

        if self.silicate is not None and not isinstance(self.silicate, str):
            self.silicate = str(self.silicate)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        if self.start_date_inc is not None and not isinstance(self.start_date_inc, str):
            self.start_date_inc = str(self.start_date_inc)

        if self.storage_condition is not None and not isinstance(self.storage_condition, StorageConditionEnum):
            self.storage_condition = StorageConditionEnum(self.storage_condition)

        if self.storage_condition_other is not None and not isinstance(self.storage_condition_other, str):
            self.storage_condition_other = str(self.storage_condition_other)

        if self.sulfate is not None and not isinstance(self.sulfate, str):
            self.sulfate = str(self.sulfate)

        if self.sulfide is not None and not isinstance(self.sulfide, str):
            self.sulfide = str(self.sulfide)

        if self.technical_reps is not None and not isinstance(self.technical_reps, int):
            self.technical_reps = int(self.technical_reps)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.tidal_stage is not None and not isinstance(self.tidal_stage, TidalStageEnum):
            self.tidal_stage = TidalStageEnum(self.tidal_stage)

        if self.tot_carb is not None and not isinstance(self.tot_carb, str):
            self.tot_carb = str(self.tot_carb)

        if self.tot_depth_water_col is not None and not isinstance(self.tot_depth_water_col, str):
            self.tot_depth_water_col = str(self.tot_depth_water_col)

        if self.tot_nitro_cont_meth is not None and not isinstance(self.tot_nitro_cont_meth, str):
            self.tot_nitro_cont_meth = str(self.tot_nitro_cont_meth)

        if self.tot_nitro_content is not None and not isinstance(self.tot_nitro_content, str):
            self.tot_nitro_content = str(self.tot_nitro_content)

        if self.tot_org_c_meth is not None and not isinstance(self.tot_org_c_meth, str):
            self.tot_org_c_meth = str(self.tot_org_c_meth)

        if self.tot_org_carb is not None and not isinstance(self.tot_org_carb, str):
            self.tot_org_carb = str(self.tot_org_carb)

        if self.turbidity is not None and not isinstance(self.turbidity, str):
            self.turbidity = str(self.turbidity)

        if self.water_content is not None and not isinstance(self.water_content, str):
            self.water_content = str(self.water_content)

        if self.water_content_meth is not None and not isinstance(self.water_content_meth, str):
            self.water_content_meth = str(self.water_content_meth)

        if self.watering_regm is not None and not isinstance(self.watering_regm, str):
            self.watering_regm = str(self.watering_regm)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SoilSample(Sample):
    """
    A sample of soil collected from the environment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["SoilSample"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:SoilSample"
    class_name: ClassVar[str] = "SoilSample"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.SoilSample

    id: Union[str, SoilSampleId] = None
    name: str = None
    analysis_type: str = None
    depth: str = None
    latitude: float = None
    longitude: float = None
    agrochem_addition: Optional[str] = None
    air_temp_regm: Optional[str] = None
    al_sat: Optional[str] = None
    al_sat_meth: Optional[str] = None
    biotic_regm: Optional[str] = None
    bulk_elect_conductivity: Optional[str] = None
    chem_administration: Optional[str] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    experimental_factor: Optional[str] = None
    experimental_factor_other: Optional[str] = None
    extraction_method: Optional[str] = None
    external_identifiers: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    filter_method: Optional[str] = None
    gaseous_environment: Optional[str] = None
    heavy_metals: Optional[str] = None
    heavy_metals_meth: Optional[str] = None
    horizon_meth: Optional[str] = None
    humidity_regm: Optional[str] = None
    isotope_exposure: Optional[str] = None
    light_regm: Optional[str] = None
    link_addit_analys: Optional[str] = None
    method_development: Optional[str] = None
    micro_biomass_c_meth: Optional[str] = None
    micro_biomass_n_meth: Optional[str] = None
    microbial_biomass: Optional[str] = None
    microbial_biomass_c: Optional[str] = None
    microbial_biomass_meth: Optional[str] = None
    microbial_biomass_n: Optional[str] = None
    misc_param: Optional[str] = None
    non_microb_biomass: Optional[str] = None
    non_microb_biomass_method: Optional[str] = None
    other: Optional[str] = None
    other_samp_store_temp: Optional[str] = None
    other_storage_condt: Optional[str] = None
    other_treatment: Optional[str] = None
    oxygen_status: Optional[Union[str, "OxygenStatusEnum"]] = None
    perturbation: Optional[str] = None
    ph: Optional[float] = None
    ph_meth: Optional[str] = None
    project: Optional[int] = None
    replicate_number: Optional[int] = None
    salinity: Optional[str] = None
    salinity_method: Optional[str] = None
    biotic_relationship: Optional[Union[str, "BioticRelationshipEnum"]] = None
    samp_store_temp: Optional[Union[str, "SampleStoreTempEnum"]] = None
    sample_link: Optional[str] = None
    sample_name: Optional[str] = None
    sample_processing: Optional[str] = None
    sampled_during: Optional[Union[str, SamplingActivityId]] = None
    sieving: Optional[str] = None
    size_frac_low: Optional[str] = None
    size_frac_up: Optional[str] = None
    soil_horizon: Optional[Union[str, "SoilHorizonEnum"]] = None
    soil_sample_type: Optional[Union[str, "SoilSampleTypeEnum"]] = None
    soil_texture: Optional[str] = None
    soil_type: Optional[Union[str, "SoilTypeEnum"]] = None
    soil_type_meth: Optional[str] = None
    source_mat_id: Optional[str] = None
    start_date_inc: Optional[str] = None
    storage_condition: Optional[Union[str, "StorageConditionEnum"]] = None
    storage_condition_other: Optional[str] = None
    technical_reps: Optional[int] = None
    temp: Optional[str] = None
    texture_meth: Optional[str] = None
    tot_nitro_cont_meth: Optional[str] = None
    tot_nitro_content: Optional[str] = None
    tot_org_c_meth: Optional[str] = None
    tot_org_carb: Optional[str] = None
    water_content: Optional[str] = None
    water_content_meth: Optional[str] = None
    watering_regm: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SoilSampleId):
            self.id = SoilSampleId(self.id)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, str):
            self.analysis_type = str(self.analysis_type)

        if self._is_empty(self.depth):
            self.MissingRequiredField("depth")
        if not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self._is_empty(self.latitude):
            self.MissingRequiredField("latitude")
        if not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self._is_empty(self.longitude):
            self.MissingRequiredField("longitude")
        if not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self.agrochem_addition is not None and not isinstance(self.agrochem_addition, str):
            self.agrochem_addition = str(self.agrochem_addition)

        if self.air_temp_regm is not None and not isinstance(self.air_temp_regm, str):
            self.air_temp_regm = str(self.air_temp_regm)

        if self.al_sat is not None and not isinstance(self.al_sat, str):
            self.al_sat = str(self.al_sat)

        if self.al_sat_meth is not None and not isinstance(self.al_sat_meth, str):
            self.al_sat_meth = str(self.al_sat_meth)

        if self.biotic_regm is not None and not isinstance(self.biotic_regm, str):
            self.biotic_regm = str(self.biotic_regm)

        if self.bulk_elect_conductivity is not None and not isinstance(self.bulk_elect_conductivity, str):
            self.bulk_elect_conductivity = str(self.bulk_elect_conductivity)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.experimental_factor_other is not None and not isinstance(self.experimental_factor_other, str):
            self.experimental_factor_other = str(self.experimental_factor_other)

        if self.extraction_method is not None and not isinstance(self.extraction_method, str):
            self.extraction_method = str(self.extraction_method)

        if not isinstance(self.external_identifiers, list):
            self.external_identifiers = [self.external_identifiers] if self.external_identifiers is not None else []
        self.external_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.external_identifiers]

        if self.filter_method is not None and not isinstance(self.filter_method, str):
            self.filter_method = str(self.filter_method)

        if self.gaseous_environment is not None and not isinstance(self.gaseous_environment, str):
            self.gaseous_environment = str(self.gaseous_environment)

        if self.heavy_metals is not None and not isinstance(self.heavy_metals, str):
            self.heavy_metals = str(self.heavy_metals)

        if self.heavy_metals_meth is not None and not isinstance(self.heavy_metals_meth, str):
            self.heavy_metals_meth = str(self.heavy_metals_meth)

        if self.horizon_meth is not None and not isinstance(self.horizon_meth, str):
            self.horizon_meth = str(self.horizon_meth)

        if self.humidity_regm is not None and not isinstance(self.humidity_regm, str):
            self.humidity_regm = str(self.humidity_regm)

        if self.isotope_exposure is not None and not isinstance(self.isotope_exposure, str):
            self.isotope_exposure = str(self.isotope_exposure)

        if self.light_regm is not None and not isinstance(self.light_regm, str):
            self.light_regm = str(self.light_regm)

        if self.link_addit_analys is not None and not isinstance(self.link_addit_analys, str):
            self.link_addit_analys = str(self.link_addit_analys)

        if self.method_development is not None and not isinstance(self.method_development, str):
            self.method_development = str(self.method_development)

        if self.micro_biomass_c_meth is not None and not isinstance(self.micro_biomass_c_meth, str):
            self.micro_biomass_c_meth = str(self.micro_biomass_c_meth)

        if self.micro_biomass_n_meth is not None and not isinstance(self.micro_biomass_n_meth, str):
            self.micro_biomass_n_meth = str(self.micro_biomass_n_meth)

        if self.microbial_biomass is not None and not isinstance(self.microbial_biomass, str):
            self.microbial_biomass = str(self.microbial_biomass)

        if self.microbial_biomass_c is not None and not isinstance(self.microbial_biomass_c, str):
            self.microbial_biomass_c = str(self.microbial_biomass_c)

        if self.microbial_biomass_meth is not None and not isinstance(self.microbial_biomass_meth, str):
            self.microbial_biomass_meth = str(self.microbial_biomass_meth)

        if self.microbial_biomass_n is not None and not isinstance(self.microbial_biomass_n, str):
            self.microbial_biomass_n = str(self.microbial_biomass_n)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        if self.non_microb_biomass is not None and not isinstance(self.non_microb_biomass, str):
            self.non_microb_biomass = str(self.non_microb_biomass)

        if self.non_microb_biomass_method is not None and not isinstance(self.non_microb_biomass_method, str):
            self.non_microb_biomass_method = str(self.non_microb_biomass_method)

        if self.other is not None and not isinstance(self.other, str):
            self.other = str(self.other)

        if self.other_samp_store_temp is not None and not isinstance(self.other_samp_store_temp, str):
            self.other_samp_store_temp = str(self.other_samp_store_temp)

        if self.other_storage_condt is not None and not isinstance(self.other_storage_condt, str):
            self.other_storage_condt = str(self.other_storage_condt)

        if self.other_treatment is not None and not isinstance(self.other_treatment, str):
            self.other_treatment = str(self.other_treatment)

        if self.oxygen_status is not None and not isinstance(self.oxygen_status, OxygenStatusEnum):
            self.oxygen_status = OxygenStatusEnum(self.oxygen_status)

        if self.perturbation is not None and not isinstance(self.perturbation, str):
            self.perturbation = str(self.perturbation)

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

        if self.project is not None and not isinstance(self.project, int):
            self.project = int(self.project)

        if self.replicate_number is not None and not isinstance(self.replicate_number, int):
            self.replicate_number = int(self.replicate_number)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.salinity_method is not None and not isinstance(self.salinity_method, str):
            self.salinity_method = str(self.salinity_method)

        if self.biotic_relationship is not None and not isinstance(self.biotic_relationship, BioticRelationshipEnum):
            self.biotic_relationship = BioticRelationshipEnum(self.biotic_relationship)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, SampleStoreTempEnum):
            self.samp_store_temp = SampleStoreTempEnum(self.samp_store_temp)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if self.sample_name is not None and not isinstance(self.sample_name, str):
            self.sample_name = str(self.sample_name)

        if self.sample_processing is not None and not isinstance(self.sample_processing, str):
            self.sample_processing = str(self.sample_processing)

        if self.sampled_during is not None and not isinstance(self.sampled_during, SamplingActivityId):
            self.sampled_during = SamplingActivityId(self.sampled_during)

        if self.sieving is not None and not isinstance(self.sieving, str):
            self.sieving = str(self.sieving)

        if self.size_frac_low is not None and not isinstance(self.size_frac_low, str):
            self.size_frac_low = str(self.size_frac_low)

        if self.size_frac_up is not None and not isinstance(self.size_frac_up, str):
            self.size_frac_up = str(self.size_frac_up)

        if self.soil_horizon is not None and not isinstance(self.soil_horizon, SoilHorizonEnum):
            self.soil_horizon = SoilHorizonEnum(self.soil_horizon)

        if self.soil_sample_type is not None and not isinstance(self.soil_sample_type, SoilSampleTypeEnum):
            self.soil_sample_type = SoilSampleTypeEnum(self.soil_sample_type)

        if self.soil_texture is not None and not isinstance(self.soil_texture, str):
            self.soil_texture = str(self.soil_texture)

        if self.soil_type is not None and not isinstance(self.soil_type, SoilTypeEnum):
            self.soil_type = SoilTypeEnum(self.soil_type)

        if self.soil_type_meth is not None and not isinstance(self.soil_type_meth, str):
            self.soil_type_meth = str(self.soil_type_meth)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        if self.start_date_inc is not None and not isinstance(self.start_date_inc, str):
            self.start_date_inc = str(self.start_date_inc)

        if self.storage_condition is not None and not isinstance(self.storage_condition, StorageConditionEnum):
            self.storage_condition = StorageConditionEnum(self.storage_condition)

        if self.storage_condition_other is not None and not isinstance(self.storage_condition_other, str):
            self.storage_condition_other = str(self.storage_condition_other)

        if self.technical_reps is not None and not isinstance(self.technical_reps, int):
            self.technical_reps = int(self.technical_reps)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.texture_meth is not None and not isinstance(self.texture_meth, str):
            self.texture_meth = str(self.texture_meth)

        if self.tot_nitro_cont_meth is not None and not isinstance(self.tot_nitro_cont_meth, str):
            self.tot_nitro_cont_meth = str(self.tot_nitro_cont_meth)

        if self.tot_nitro_content is not None and not isinstance(self.tot_nitro_content, str):
            self.tot_nitro_content = str(self.tot_nitro_content)

        if self.tot_org_c_meth is not None and not isinstance(self.tot_org_c_meth, str):
            self.tot_org_c_meth = str(self.tot_org_c_meth)

        if self.tot_org_carb is not None and not isinstance(self.tot_org_carb, str):
            self.tot_org_carb = str(self.tot_org_carb)

        if self.water_content is not None and not isinstance(self.water_content, str):
            self.water_content = str(self.water_content)

        if self.water_content_meth is not None and not isinstance(self.water_content_meth, str):
            self.water_content_meth = str(self.water_content_meth)

        if self.watering_regm is not None and not isinstance(self.watering_regm, str):
            self.watering_regm = str(self.watering_regm)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SynthesizedMaterialSample(Sample):
    """
    A sample containing synthetically generated material.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["SynthesizedMaterialSample"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:SynthesizedMaterialSample"
    class_name: ClassVar[str] = "SynthesizedMaterialSample"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.SynthesizedMaterialSample

    id: Union[str, SynthesizedMaterialSampleId] = None
    name: str = None
    analysis_type: str = None
    synth_instrument: str = None
    synth_reagents: str = None
    cas: Optional[str] = None
    compound_name: Optional[str] = None
    experimental_factor: Optional[str] = None
    experimental_factor_other: Optional[str] = None
    external_identifiers: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    genetic_mod: Optional[str] = None
    item_number: Optional[str] = None
    other: Optional[str] = None
    other_samp_store_temp: Optional[str] = None
    other_storage_condt: Optional[str] = None
    oxygen_status: Optional[Union[str, "OxygenStatusEnum"]] = None
    product_name: Optional[str] = None
    production_method: Optional[str] = None
    project: Optional[int] = None
    replicate_number: Optional[int] = None
    sample_link: Optional[str] = None
    sample_name: Optional[str] = None
    sample_processing: Optional[str] = None
    samp_store_temp: Optional[Union[str, "SampleStoreTempEnum"]] = None
    sampled_during: Optional[Union[str, SamplingActivityId]] = None
    source_mat_id: Optional[str] = None
    storage_condition: Optional[Union[str, "StorageConditionEnum"]] = None
    storage_condition_other: Optional[str] = None
    synth_process: Optional[str] = None
    technical_reps: Optional[int] = None
    temp: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SynthesizedMaterialSampleId):
            self.id = SynthesizedMaterialSampleId(self.id)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, str):
            self.analysis_type = str(self.analysis_type)

        if self._is_empty(self.synth_instrument):
            self.MissingRequiredField("synth_instrument")
        if not isinstance(self.synth_instrument, str):
            self.synth_instrument = str(self.synth_instrument)

        if self._is_empty(self.synth_reagents):
            self.MissingRequiredField("synth_reagents")
        if not isinstance(self.synth_reagents, str):
            self.synth_reagents = str(self.synth_reagents)

        if self.cas is not None and not isinstance(self.cas, str):
            self.cas = str(self.cas)

        if self.compound_name is not None and not isinstance(self.compound_name, str):
            self.compound_name = str(self.compound_name)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.experimental_factor_other is not None and not isinstance(self.experimental_factor_other, str):
            self.experimental_factor_other = str(self.experimental_factor_other)

        if not isinstance(self.external_identifiers, list):
            self.external_identifiers = [self.external_identifiers] if self.external_identifiers is not None else []
        self.external_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.external_identifiers]

        if self.genetic_mod is not None and not isinstance(self.genetic_mod, str):
            self.genetic_mod = str(self.genetic_mod)

        if self.item_number is not None and not isinstance(self.item_number, str):
            self.item_number = str(self.item_number)

        if self.other is not None and not isinstance(self.other, str):
            self.other = str(self.other)

        if self.other_samp_store_temp is not None and not isinstance(self.other_samp_store_temp, str):
            self.other_samp_store_temp = str(self.other_samp_store_temp)

        if self.other_storage_condt is not None and not isinstance(self.other_storage_condt, str):
            self.other_storage_condt = str(self.other_storage_condt)

        if self.oxygen_status is not None and not isinstance(self.oxygen_status, OxygenStatusEnum):
            self.oxygen_status = OxygenStatusEnum(self.oxygen_status)

        if self.product_name is not None and not isinstance(self.product_name, str):
            self.product_name = str(self.product_name)

        if self.production_method is not None and not isinstance(self.production_method, str):
            self.production_method = str(self.production_method)

        if self.project is not None and not isinstance(self.project, int):
            self.project = int(self.project)

        if self.replicate_number is not None and not isinstance(self.replicate_number, int):
            self.replicate_number = int(self.replicate_number)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if self.sample_name is not None and not isinstance(self.sample_name, str):
            self.sample_name = str(self.sample_name)

        if self.sample_processing is not None and not isinstance(self.sample_processing, str):
            self.sample_processing = str(self.sample_processing)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, SampleStoreTempEnum):
            self.samp_store_temp = SampleStoreTempEnum(self.samp_store_temp)

        if self.sampled_during is not None and not isinstance(self.sampled_during, SamplingActivityId):
            self.sampled_during = SamplingActivityId(self.sampled_during)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        if self.storage_condition is not None and not isinstance(self.storage_condition, StorageConditionEnum):
            self.storage_condition = StorageConditionEnum(self.storage_condition)

        if self.storage_condition_other is not None and not isinstance(self.storage_condition_other, str):
            self.storage_condition_other = str(self.storage_condition_other)

        if self.synth_process is not None and not isinstance(self.synth_process, str):
            self.synth_process = str(self.synth_process)

        if self.technical_reps is not None and not isinstance(self.technical_reps, int):
            self.technical_reps = int(self.technical_reps)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TerraformSample(Sample):
    """
    A sample collected from a Terraform experiment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["TerraformSample"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:TerraformSample"
    class_name: ClassVar[str] = "TerraformSample"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.TerraformSample

    id: Union[str, TerraformSampleId] = None
    name: str = None
    analysis_type: str = None
    initiation_date_inoculation: str = None
    initiation_date_plant: str = None
    synth_env_assembly: str = None
    synth_env_design: Union[str, "SyntheticEnvironmentEnum"] = None
    synth_env_design_method: str = None
    synth_env_material: str = None
    synth_env_treatment: str = None
    synth_start_date: str = None
    air_temp_regm: Optional[str] = None
    biotic_regm: Optional[str] = None
    chem_administration: Optional[str] = None
    cult_root_med: Optional[str] = None
    encoded_traits: Optional[str] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    external_identifiers: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    gaseous_environment: Optional[str] = None
    genetic_mod: Optional[str] = None
    growth_medium: Optional[str] = None
    host_age: Optional[str] = None
    host_common_name: Optional[str] = None
    host_dry_mass: Optional[str] = None
    host_genotype: Optional[str] = None
    host_height: Optional[str] = None
    host_life_stage: Optional[str] = None
    host_spec_range: Optional[str] = None
    host_taxid: Optional[str] = None
    host_tot_mass: Optional[str] = None
    host_wet_mass: Optional[str] = None
    humidity_regm: Optional[str] = None
    isol_growth_condt: Optional[str] = None
    isotope_exposure: Optional[str] = None
    light_regm: Optional[str] = None
    method_development: Optional[str] = None
    mineral_nutr_regm: Optional[str] = None
    misc_param: Optional[str] = None
    non_min_nutr_regm: Optional[str] = None
    other: Optional[str] = None
    other_samp_store_temp: Optional[str] = None
    other_storage_condt: Optional[str] = None
    other_treatment: Optional[str] = None
    oxygen_status: Optional[Union[str, "OxygenStatusEnum"]] = None
    plant_growth_med: Optional[str] = None
    plant_product: Optional[str] = None
    plant_sex: Optional[Union[str, "PlantSexEnum"]] = None
    plant_struc: Optional[Union[str, "PlantStructureEnum"]] = None
    pressure: Optional[str] = None
    project: Optional[int] = None
    propagation: Optional[str] = None
    redox_potential: Optional[str] = None
    ref_biomaterial: Optional[str] = None
    replicate_number: Optional[int] = None
    root_cond: Optional[str] = None
    root_med_carbon: Optional[str] = None
    root_med_macronutr: Optional[str] = None
    root_med_micronutr: Optional[str] = None
    salt_regm: Optional[str] = None
    sample_link: Optional[str] = None
    sample_name: Optional[str] = None
    sample_processing: Optional[str] = None
    biotic_relationship: Optional[Union[str, "BioticRelationshipEnum"]] = None
    samp_store_temp: Optional[Union[str, "SampleStoreTempEnum"]] = None
    sampled_during: Optional[Union[str, SamplingActivityId]] = None
    source_mat_id: Optional[str] = None
    storage_condition: Optional[Union[str, "StorageConditionEnum"]] = None
    storage_condition_other: Optional[str] = None
    technical_reps: Optional[int] = None
    temp: Optional[str] = None
    tiss_cult_growth_med: Optional[str] = None
    water_content: Optional[str] = None
    water_content_meth: Optional[str] = None
    watering_regm: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TerraformSampleId):
            self.id = TerraformSampleId(self.id)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, str):
            self.analysis_type = str(self.analysis_type)

        if self._is_empty(self.initiation_date_inoculation):
            self.MissingRequiredField("initiation_date_inoculation")
        if not isinstance(self.initiation_date_inoculation, str):
            self.initiation_date_inoculation = str(self.initiation_date_inoculation)

        if self._is_empty(self.initiation_date_plant):
            self.MissingRequiredField("initiation_date_plant")
        if not isinstance(self.initiation_date_plant, str):
            self.initiation_date_plant = str(self.initiation_date_plant)

        if self._is_empty(self.synth_env_assembly):
            self.MissingRequiredField("synth_env_assembly")
        if not isinstance(self.synth_env_assembly, str):
            self.synth_env_assembly = str(self.synth_env_assembly)

        if self._is_empty(self.synth_env_design):
            self.MissingRequiredField("synth_env_design")
        if not isinstance(self.synth_env_design, SyntheticEnvironmentEnum):
            self.synth_env_design = SyntheticEnvironmentEnum(self.synth_env_design)

        if self._is_empty(self.synth_env_design_method):
            self.MissingRequiredField("synth_env_design_method")
        if not isinstance(self.synth_env_design_method, str):
            self.synth_env_design_method = str(self.synth_env_design_method)

        if self._is_empty(self.synth_env_material):
            self.MissingRequiredField("synth_env_material")
        if not isinstance(self.synth_env_material, str):
            self.synth_env_material = str(self.synth_env_material)

        if self._is_empty(self.synth_env_treatment):
            self.MissingRequiredField("synth_env_treatment")
        if not isinstance(self.synth_env_treatment, str):
            self.synth_env_treatment = str(self.synth_env_treatment)

        if self._is_empty(self.synth_start_date):
            self.MissingRequiredField("synth_start_date")
        if not isinstance(self.synth_start_date, str):
            self.synth_start_date = str(self.synth_start_date)

        if self.air_temp_regm is not None and not isinstance(self.air_temp_regm, str):
            self.air_temp_regm = str(self.air_temp_regm)

        if self.biotic_regm is not None and not isinstance(self.biotic_regm, str):
            self.biotic_regm = str(self.biotic_regm)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.cult_root_med is not None and not isinstance(self.cult_root_med, str):
            self.cult_root_med = str(self.cult_root_med)

        if self.encoded_traits is not None and not isinstance(self.encoded_traits, str):
            self.encoded_traits = str(self.encoded_traits)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if not isinstance(self.external_identifiers, list):
            self.external_identifiers = [self.external_identifiers] if self.external_identifiers is not None else []
        self.external_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.external_identifiers]

        if self.gaseous_environment is not None and not isinstance(self.gaseous_environment, str):
            self.gaseous_environment = str(self.gaseous_environment)

        if self.genetic_mod is not None and not isinstance(self.genetic_mod, str):
            self.genetic_mod = str(self.genetic_mod)

        if self.growth_medium is not None and not isinstance(self.growth_medium, str):
            self.growth_medium = str(self.growth_medium)

        if self.host_age is not None and not isinstance(self.host_age, str):
            self.host_age = str(self.host_age)

        if self.host_common_name is not None and not isinstance(self.host_common_name, str):
            self.host_common_name = str(self.host_common_name)

        if self.host_dry_mass is not None and not isinstance(self.host_dry_mass, str):
            self.host_dry_mass = str(self.host_dry_mass)

        if self.host_genotype is not None and not isinstance(self.host_genotype, str):
            self.host_genotype = str(self.host_genotype)

        if self.host_height is not None and not isinstance(self.host_height, str):
            self.host_height = str(self.host_height)

        if self.host_life_stage is not None and not isinstance(self.host_life_stage, str):
            self.host_life_stage = str(self.host_life_stage)

        if self.host_spec_range is not None and not isinstance(self.host_spec_range, str):
            self.host_spec_range = str(self.host_spec_range)

        if self.host_taxid is not None and not isinstance(self.host_taxid, str):
            self.host_taxid = str(self.host_taxid)

        if self.host_tot_mass is not None and not isinstance(self.host_tot_mass, str):
            self.host_tot_mass = str(self.host_tot_mass)

        if self.host_wet_mass is not None and not isinstance(self.host_wet_mass, str):
            self.host_wet_mass = str(self.host_wet_mass)

        if self.humidity_regm is not None and not isinstance(self.humidity_regm, str):
            self.humidity_regm = str(self.humidity_regm)

        if self.isol_growth_condt is not None and not isinstance(self.isol_growth_condt, str):
            self.isol_growth_condt = str(self.isol_growth_condt)

        if self.isotope_exposure is not None and not isinstance(self.isotope_exposure, str):
            self.isotope_exposure = str(self.isotope_exposure)

        if self.light_regm is not None and not isinstance(self.light_regm, str):
            self.light_regm = str(self.light_regm)

        if self.method_development is not None and not isinstance(self.method_development, str):
            self.method_development = str(self.method_development)

        if self.mineral_nutr_regm is not None and not isinstance(self.mineral_nutr_regm, str):
            self.mineral_nutr_regm = str(self.mineral_nutr_regm)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        if self.non_min_nutr_regm is not None and not isinstance(self.non_min_nutr_regm, str):
            self.non_min_nutr_regm = str(self.non_min_nutr_regm)

        if self.other is not None and not isinstance(self.other, str):
            self.other = str(self.other)

        if self.other_samp_store_temp is not None and not isinstance(self.other_samp_store_temp, str):
            self.other_samp_store_temp = str(self.other_samp_store_temp)

        if self.other_storage_condt is not None and not isinstance(self.other_storage_condt, str):
            self.other_storage_condt = str(self.other_storage_condt)

        if self.other_treatment is not None and not isinstance(self.other_treatment, str):
            self.other_treatment = str(self.other_treatment)

        if self.oxygen_status is not None and not isinstance(self.oxygen_status, OxygenStatusEnum):
            self.oxygen_status = OxygenStatusEnum(self.oxygen_status)

        if self.plant_growth_med is not None and not isinstance(self.plant_growth_med, str):
            self.plant_growth_med = str(self.plant_growth_med)

        if self.plant_product is not None and not isinstance(self.plant_product, str):
            self.plant_product = str(self.plant_product)

        if self.plant_sex is not None and not isinstance(self.plant_sex, PlantSexEnum):
            self.plant_sex = PlantSexEnum(self.plant_sex)

        if self.plant_struc is not None and not isinstance(self.plant_struc, PlantStructureEnum):
            self.plant_struc = PlantStructureEnum(self.plant_struc)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.project is not None and not isinstance(self.project, int):
            self.project = int(self.project)

        if self.propagation is not None and not isinstance(self.propagation, str):
            self.propagation = str(self.propagation)

        if self.redox_potential is not None and not isinstance(self.redox_potential, str):
            self.redox_potential = str(self.redox_potential)

        if self.ref_biomaterial is not None and not isinstance(self.ref_biomaterial, str):
            self.ref_biomaterial = str(self.ref_biomaterial)

        if self.replicate_number is not None and not isinstance(self.replicate_number, int):
            self.replicate_number = int(self.replicate_number)

        if self.root_cond is not None and not isinstance(self.root_cond, str):
            self.root_cond = str(self.root_cond)

        if self.root_med_carbon is not None and not isinstance(self.root_med_carbon, str):
            self.root_med_carbon = str(self.root_med_carbon)

        if self.root_med_macronutr is not None and not isinstance(self.root_med_macronutr, str):
            self.root_med_macronutr = str(self.root_med_macronutr)

        if self.root_med_micronutr is not None and not isinstance(self.root_med_micronutr, str):
            self.root_med_micronutr = str(self.root_med_micronutr)

        if self.salt_regm is not None and not isinstance(self.salt_regm, str):
            self.salt_regm = str(self.salt_regm)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if self.sample_name is not None and not isinstance(self.sample_name, str):
            self.sample_name = str(self.sample_name)

        if self.sample_processing is not None and not isinstance(self.sample_processing, str):
            self.sample_processing = str(self.sample_processing)

        if self.biotic_relationship is not None and not isinstance(self.biotic_relationship, BioticRelationshipEnum):
            self.biotic_relationship = BioticRelationshipEnum(self.biotic_relationship)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, SampleStoreTempEnum):
            self.samp_store_temp = SampleStoreTempEnum(self.samp_store_temp)

        if self.sampled_during is not None and not isinstance(self.sampled_during, SamplingActivityId):
            self.sampled_during = SamplingActivityId(self.sampled_during)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        if self.storage_condition is not None and not isinstance(self.storage_condition, StorageConditionEnum):
            self.storage_condition = StorageConditionEnum(self.storage_condition)

        if self.storage_condition_other is not None and not isinstance(self.storage_condition_other, str):
            self.storage_condition_other = str(self.storage_condition_other)

        if self.technical_reps is not None and not isinstance(self.technical_reps, int):
            self.technical_reps = int(self.technical_reps)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.tiss_cult_growth_med is not None and not isinstance(self.tiss_cult_growth_med, str):
            self.tiss_cult_growth_med = str(self.tiss_cult_growth_med)

        if self.water_content is not None and not isinstance(self.water_content, str):
            self.water_content = str(self.water_content)

        if self.water_content_meth is not None and not isinstance(self.water_content_meth, str):
            self.water_content_meth = str(self.water_content_meth)

        if self.watering_regm is not None and not isinstance(self.watering_regm, str):
            self.watering_regm = str(self.watering_regm)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WaterSample(Sample):
    """
    A sample of water collected from the environment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["WaterSample"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:WaterSample"
    class_name: ClassVar[str] = "WaterSample"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.WaterSample

    id: Union[str, WaterSampleId] = None
    name: str = None
    analysis_type: str = None
    depth: str = None
    filter_method: str = None
    latitude: float = None
    longitude: float = None
    size_frac_low: str = None
    size_frac_up: str = None
    air_temp_regm: Optional[str] = None
    alkalinity: Optional[str] = None
    alkalinity_method: Optional[str] = None
    alkyl_diethers: Optional[str] = None
    aminopept_act: Optional[str] = None
    ammonium: Optional[str] = None
    bac_prod: Optional[str] = None
    bac_resp: Optional[str] = None
    bacteria_carb_prod: Optional[str] = None
    biotic_regm: Optional[str] = None
    bishomohopanol: Optional[str] = None
    bromide: Optional[str] = None
    calcium: Optional[str] = None
    carb_nitro_ratio: Optional[str] = None
    chem_administration: Optional[str] = None
    chloride: Optional[str] = None
    chlorophyll: Optional[str] = None
    conduc: Optional[str] = None
    density: Optional[str] = None
    diether_lipids: Optional[str] = None
    diss_carb_dioxide: Optional[str] = None
    diss_hydrogen: Optional[str] = None
    diss_inorg_carb: Optional[str] = None
    diss_inorg_nitro: Optional[str] = None
    diss_inorg_phosp: Optional[str] = None
    diss_org_carb: Optional[str] = None
    diss_org_nitro: Optional[str] = None
    diss_oxygen: Optional[str] = None
    down_par: Optional[str] = None
    env_broad_scale: Optional[str] = None
    env_local_scale: Optional[str] = None
    env_medium: Optional[str] = None
    experimental_factor: Optional[str] = None
    experimental_factor_other: Optional[str] = None
    external_identifiers: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    extraction_method: Optional[str] = None
    fluor: Optional[str] = None
    gaseous_environment: Optional[str] = None
    glucosidase_act: Optional[str] = None
    isotope_exposure: Optional[str] = None
    light_intensity: Optional[str] = None
    magnesium: Optional[str] = None
    mean_frict_vel: Optional[str] = None
    mean_peak_frict_vel: Optional[str] = None
    method_development: Optional[str] = None
    misc_param: Optional[str] = None
    n_alkanes: Optional[str] = None
    nitrate: Optional[str] = None
    nitrite: Optional[str] = None
    nitro: Optional[str] = None
    non_microb_biomass: Optional[str] = None
    non_microb_biomass_method: Optional[str] = None
    org_carb: Optional[str] = None
    org_matter: Optional[str] = None
    org_nitro: Optional[str] = None
    org_nitro_method: Optional[str] = None
    other: Optional[str] = None
    other_samp_store_temp: Optional[str] = None
    other_storage_condt: Optional[str] = None
    other_treatment: Optional[str] = None
    oxygen_status: Optional[Union[str, "OxygenStatusEnum"]] = None
    part_org_carb: Optional[str] = None
    part_org_nitro: Optional[str] = None
    perturbation: Optional[str] = None
    petroleum_hydrocarb: Optional[str] = None
    ph: Optional[float] = None
    ph_meth: Optional[str] = None
    phaeopigments: Optional[str] = None
    phosphate: Optional[str] = None
    phosplipid_fatt_acid: Optional[str] = None
    photon_flux: Optional[str] = None
    potassium: Optional[str] = None
    pressure: Optional[str] = None
    primary_prod: Optional[str] = None
    project: Optional[int] = None
    redox_potential: Optional[str] = None
    replicate_number: Optional[int] = None
    salinity: Optional[str] = None
    salinity_method: Optional[str] = None
    sample_link: Optional[str] = None
    sample_name: Optional[str] = None
    sampled_during: Optional[Union[str, SamplingActivityId]] = None
    silicate: Optional[str] = None
    sodium: Optional[str] = None
    soluble_react_phosp: Optional[str] = None
    source_mat_id: Optional[str] = None
    start_date_inc: Optional[str] = None
    storage_condition: Optional[Union[str, "StorageConditionEnum"]] = None
    storage_condition_other: Optional[str] = None
    sulfate: Optional[str] = None
    sulfide: Optional[str] = None
    samp_store_temp: Optional[Union[str, "SampleStoreTempEnum"]] = None
    suspend_part_matter: Optional[str] = None
    technical_reps: Optional[int] = None
    temp: Optional[str] = None
    tidal_stage: Optional[Union[str, "TidalStageEnum"]] = None
    tot_depth_water_col: Optional[str] = None
    tot_diss_nitro: Optional[str] = None
    tot_inorg_nitro: Optional[str] = None
    tot_nitro: Optional[str] = None
    tot_part_carb: Optional[str] = None
    tot_phosp: Optional[str] = None
    turbidity: Optional[str] = None
    water_current: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WaterSampleId):
            self.id = WaterSampleId(self.id)

        if self._is_empty(self.analysis_type):
            self.MissingRequiredField("analysis_type")
        if not isinstance(self.analysis_type, str):
            self.analysis_type = str(self.analysis_type)

        if self._is_empty(self.depth):
            self.MissingRequiredField("depth")
        if not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self._is_empty(self.filter_method):
            self.MissingRequiredField("filter_method")
        if not isinstance(self.filter_method, str):
            self.filter_method = str(self.filter_method)

        if self._is_empty(self.latitude):
            self.MissingRequiredField("latitude")
        if not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self._is_empty(self.longitude):
            self.MissingRequiredField("longitude")
        if not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self._is_empty(self.size_frac_low):
            self.MissingRequiredField("size_frac_low")
        if not isinstance(self.size_frac_low, str):
            self.size_frac_low = str(self.size_frac_low)

        if self._is_empty(self.size_frac_up):
            self.MissingRequiredField("size_frac_up")
        if not isinstance(self.size_frac_up, str):
            self.size_frac_up = str(self.size_frac_up)

        if self.air_temp_regm is not None and not isinstance(self.air_temp_regm, str):
            self.air_temp_regm = str(self.air_temp_regm)

        if self.alkalinity is not None and not isinstance(self.alkalinity, str):
            self.alkalinity = str(self.alkalinity)

        if self.alkalinity_method is not None and not isinstance(self.alkalinity_method, str):
            self.alkalinity_method = str(self.alkalinity_method)

        if self.alkyl_diethers is not None and not isinstance(self.alkyl_diethers, str):
            self.alkyl_diethers = str(self.alkyl_diethers)

        if self.aminopept_act is not None and not isinstance(self.aminopept_act, str):
            self.aminopept_act = str(self.aminopept_act)

        if self.ammonium is not None and not isinstance(self.ammonium, str):
            self.ammonium = str(self.ammonium)

        if self.bac_prod is not None and not isinstance(self.bac_prod, str):
            self.bac_prod = str(self.bac_prod)

        if self.bac_resp is not None and not isinstance(self.bac_resp, str):
            self.bac_resp = str(self.bac_resp)

        if self.bacteria_carb_prod is not None and not isinstance(self.bacteria_carb_prod, str):
            self.bacteria_carb_prod = str(self.bacteria_carb_prod)

        if self.biotic_regm is not None and not isinstance(self.biotic_regm, str):
            self.biotic_regm = str(self.biotic_regm)

        if self.bishomohopanol is not None and not isinstance(self.bishomohopanol, str):
            self.bishomohopanol = str(self.bishomohopanol)

        if self.bromide is not None and not isinstance(self.bromide, str):
            self.bromide = str(self.bromide)

        if self.calcium is not None and not isinstance(self.calcium, str):
            self.calcium = str(self.calcium)

        if self.carb_nitro_ratio is not None and not isinstance(self.carb_nitro_ratio, str):
            self.carb_nitro_ratio = str(self.carb_nitro_ratio)

        if self.chem_administration is not None and not isinstance(self.chem_administration, str):
            self.chem_administration = str(self.chem_administration)

        if self.chloride is not None and not isinstance(self.chloride, str):
            self.chloride = str(self.chloride)

        if self.chlorophyll is not None and not isinstance(self.chlorophyll, str):
            self.chlorophyll = str(self.chlorophyll)

        if self.conduc is not None and not isinstance(self.conduc, str):
            self.conduc = str(self.conduc)

        if self.density is not None and not isinstance(self.density, str):
            self.density = str(self.density)

        if self.diether_lipids is not None and not isinstance(self.diether_lipids, str):
            self.diether_lipids = str(self.diether_lipids)

        if self.diss_carb_dioxide is not None and not isinstance(self.diss_carb_dioxide, str):
            self.diss_carb_dioxide = str(self.diss_carb_dioxide)

        if self.diss_hydrogen is not None and not isinstance(self.diss_hydrogen, str):
            self.diss_hydrogen = str(self.diss_hydrogen)

        if self.diss_inorg_carb is not None and not isinstance(self.diss_inorg_carb, str):
            self.diss_inorg_carb = str(self.diss_inorg_carb)

        if self.diss_inorg_nitro is not None and not isinstance(self.diss_inorg_nitro, str):
            self.diss_inorg_nitro = str(self.diss_inorg_nitro)

        if self.diss_inorg_phosp is not None and not isinstance(self.diss_inorg_phosp, str):
            self.diss_inorg_phosp = str(self.diss_inorg_phosp)

        if self.diss_org_carb is not None and not isinstance(self.diss_org_carb, str):
            self.diss_org_carb = str(self.diss_org_carb)

        if self.diss_org_nitro is not None and not isinstance(self.diss_org_nitro, str):
            self.diss_org_nitro = str(self.diss_org_nitro)

        if self.diss_oxygen is not None and not isinstance(self.diss_oxygen, str):
            self.diss_oxygen = str(self.diss_oxygen)

        if self.down_par is not None and not isinstance(self.down_par, str):
            self.down_par = str(self.down_par)

        if self.env_broad_scale is not None and not isinstance(self.env_broad_scale, str):
            self.env_broad_scale = str(self.env_broad_scale)

        if self.env_local_scale is not None and not isinstance(self.env_local_scale, str):
            self.env_local_scale = str(self.env_local_scale)

        if self.env_medium is not None and not isinstance(self.env_medium, str):
            self.env_medium = str(self.env_medium)

        if self.experimental_factor is not None and not isinstance(self.experimental_factor, str):
            self.experimental_factor = str(self.experimental_factor)

        if self.experimental_factor_other is not None and not isinstance(self.experimental_factor_other, str):
            self.experimental_factor_other = str(self.experimental_factor_other)

        if not isinstance(self.external_identifiers, list):
            self.external_identifiers = [self.external_identifiers] if self.external_identifiers is not None else []
        self.external_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.external_identifiers]

        if self.extraction_method is not None and not isinstance(self.extraction_method, str):
            self.extraction_method = str(self.extraction_method)

        if self.fluor is not None and not isinstance(self.fluor, str):
            self.fluor = str(self.fluor)

        if self.gaseous_environment is not None and not isinstance(self.gaseous_environment, str):
            self.gaseous_environment = str(self.gaseous_environment)

        if self.glucosidase_act is not None and not isinstance(self.glucosidase_act, str):
            self.glucosidase_act = str(self.glucosidase_act)

        if self.isotope_exposure is not None and not isinstance(self.isotope_exposure, str):
            self.isotope_exposure = str(self.isotope_exposure)

        if self.light_intensity is not None and not isinstance(self.light_intensity, str):
            self.light_intensity = str(self.light_intensity)

        if self.magnesium is not None and not isinstance(self.magnesium, str):
            self.magnesium = str(self.magnesium)

        if self.mean_frict_vel is not None and not isinstance(self.mean_frict_vel, str):
            self.mean_frict_vel = str(self.mean_frict_vel)

        if self.mean_peak_frict_vel is not None and not isinstance(self.mean_peak_frict_vel, str):
            self.mean_peak_frict_vel = str(self.mean_peak_frict_vel)

        if self.method_development is not None and not isinstance(self.method_development, str):
            self.method_development = str(self.method_development)

        if self.misc_param is not None and not isinstance(self.misc_param, str):
            self.misc_param = str(self.misc_param)

        if self.n_alkanes is not None and not isinstance(self.n_alkanes, str):
            self.n_alkanes = str(self.n_alkanes)

        if self.nitrate is not None and not isinstance(self.nitrate, str):
            self.nitrate = str(self.nitrate)

        if self.nitrite is not None and not isinstance(self.nitrite, str):
            self.nitrite = str(self.nitrite)

        if self.nitro is not None and not isinstance(self.nitro, str):
            self.nitro = str(self.nitro)

        if self.non_microb_biomass is not None and not isinstance(self.non_microb_biomass, str):
            self.non_microb_biomass = str(self.non_microb_biomass)

        if self.non_microb_biomass_method is not None and not isinstance(self.non_microb_biomass_method, str):
            self.non_microb_biomass_method = str(self.non_microb_biomass_method)

        if self.org_carb is not None and not isinstance(self.org_carb, str):
            self.org_carb = str(self.org_carb)

        if self.org_matter is not None and not isinstance(self.org_matter, str):
            self.org_matter = str(self.org_matter)

        if self.org_nitro is not None and not isinstance(self.org_nitro, str):
            self.org_nitro = str(self.org_nitro)

        if self.org_nitro_method is not None and not isinstance(self.org_nitro_method, str):
            self.org_nitro_method = str(self.org_nitro_method)

        if self.other is not None and not isinstance(self.other, str):
            self.other = str(self.other)

        if self.other_samp_store_temp is not None and not isinstance(self.other_samp_store_temp, str):
            self.other_samp_store_temp = str(self.other_samp_store_temp)

        if self.other_storage_condt is not None and not isinstance(self.other_storage_condt, str):
            self.other_storage_condt = str(self.other_storage_condt)

        if self.other_treatment is not None and not isinstance(self.other_treatment, str):
            self.other_treatment = str(self.other_treatment)

        if self.oxygen_status is not None and not isinstance(self.oxygen_status, OxygenStatusEnum):
            self.oxygen_status = OxygenStatusEnum(self.oxygen_status)

        if self.part_org_carb is not None and not isinstance(self.part_org_carb, str):
            self.part_org_carb = str(self.part_org_carb)

        if self.part_org_nitro is not None and not isinstance(self.part_org_nitro, str):
            self.part_org_nitro = str(self.part_org_nitro)

        if self.perturbation is not None and not isinstance(self.perturbation, str):
            self.perturbation = str(self.perturbation)

        if self.petroleum_hydrocarb is not None and not isinstance(self.petroleum_hydrocarb, str):
            self.petroleum_hydrocarb = str(self.petroleum_hydrocarb)

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if self.ph_meth is not None and not isinstance(self.ph_meth, str):
            self.ph_meth = str(self.ph_meth)

        if self.phaeopigments is not None and not isinstance(self.phaeopigments, str):
            self.phaeopigments = str(self.phaeopigments)

        if self.phosphate is not None and not isinstance(self.phosphate, str):
            self.phosphate = str(self.phosphate)

        if self.phosplipid_fatt_acid is not None and not isinstance(self.phosplipid_fatt_acid, str):
            self.phosplipid_fatt_acid = str(self.phosplipid_fatt_acid)

        if self.photon_flux is not None and not isinstance(self.photon_flux, str):
            self.photon_flux = str(self.photon_flux)

        if self.potassium is not None and not isinstance(self.potassium, str):
            self.potassium = str(self.potassium)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.primary_prod is not None and not isinstance(self.primary_prod, str):
            self.primary_prod = str(self.primary_prod)

        if self.project is not None and not isinstance(self.project, int):
            self.project = int(self.project)

        if self.redox_potential is not None and not isinstance(self.redox_potential, str):
            self.redox_potential = str(self.redox_potential)

        if self.replicate_number is not None and not isinstance(self.replicate_number, int):
            self.replicate_number = int(self.replicate_number)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.salinity_method is not None and not isinstance(self.salinity_method, str):
            self.salinity_method = str(self.salinity_method)

        if self.sample_link is not None and not isinstance(self.sample_link, str):
            self.sample_link = str(self.sample_link)

        if self.sample_name is not None and not isinstance(self.sample_name, str):
            self.sample_name = str(self.sample_name)

        if self.sampled_during is not None and not isinstance(self.sampled_during, SamplingActivityId):
            self.sampled_during = SamplingActivityId(self.sampled_during)

        if self.silicate is not None and not isinstance(self.silicate, str):
            self.silicate = str(self.silicate)

        if self.sodium is not None and not isinstance(self.sodium, str):
            self.sodium = str(self.sodium)

        if self.soluble_react_phosp is not None and not isinstance(self.soluble_react_phosp, str):
            self.soluble_react_phosp = str(self.soluble_react_phosp)

        if self.source_mat_id is not None and not isinstance(self.source_mat_id, str):
            self.source_mat_id = str(self.source_mat_id)

        if self.start_date_inc is not None and not isinstance(self.start_date_inc, str):
            self.start_date_inc = str(self.start_date_inc)

        if self.storage_condition is not None and not isinstance(self.storage_condition, StorageConditionEnum):
            self.storage_condition = StorageConditionEnum(self.storage_condition)

        if self.storage_condition_other is not None and not isinstance(self.storage_condition_other, str):
            self.storage_condition_other = str(self.storage_condition_other)

        if self.sulfate is not None and not isinstance(self.sulfate, str):
            self.sulfate = str(self.sulfate)

        if self.sulfide is not None and not isinstance(self.sulfide, str):
            self.sulfide = str(self.sulfide)

        if self.samp_store_temp is not None and not isinstance(self.samp_store_temp, SampleStoreTempEnum):
            self.samp_store_temp = SampleStoreTempEnum(self.samp_store_temp)

        if self.suspend_part_matter is not None and not isinstance(self.suspend_part_matter, str):
            self.suspend_part_matter = str(self.suspend_part_matter)

        if self.technical_reps is not None and not isinstance(self.technical_reps, int):
            self.technical_reps = int(self.technical_reps)

        if self.temp is not None and not isinstance(self.temp, str):
            self.temp = str(self.temp)

        if self.tidal_stage is not None and not isinstance(self.tidal_stage, TidalStageEnum):
            self.tidal_stage = TidalStageEnum(self.tidal_stage)

        if self.tot_depth_water_col is not None and not isinstance(self.tot_depth_water_col, str):
            self.tot_depth_water_col = str(self.tot_depth_water_col)

        if self.tot_diss_nitro is not None and not isinstance(self.tot_diss_nitro, str):
            self.tot_diss_nitro = str(self.tot_diss_nitro)

        if self.tot_inorg_nitro is not None and not isinstance(self.tot_inorg_nitro, str):
            self.tot_inorg_nitro = str(self.tot_inorg_nitro)

        if self.tot_nitro is not None and not isinstance(self.tot_nitro, str):
            self.tot_nitro = str(self.tot_nitro)

        if self.tot_part_carb is not None and not isinstance(self.tot_part_carb, str):
            self.tot_part_carb = str(self.tot_part_carb)

        if self.tot_phosp is not None and not isinstance(self.tot_phosp, str):
            self.tot_phosp = str(self.tot_phosp)

        if self.turbidity is not None and not isinstance(self.turbidity, str):
            self.turbidity = str(self.turbidity)

        if self.water_current is not None and not isinstance(self.water_current, str):
            self.water_current = str(self.water_current)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProcessedSample(Sample):
    """
    A sample that has undergone processing or analysis. Processed Sample entities are derived from Activities. The
    upstream SampleProcessing that produced this ProcessedSample is referenced via sampled_during.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["ProcessedSample"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:ProcessedSample"
    class_name: ClassVar[str] = "ProcessedSample"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.ProcessedSample

    id: Union[str, ProcessedSampleId] = None
    name: str = None
    storage_location: Optional[str] = None
    label_text: Optional[str] = None
    concentration_ug_per_uL: Optional[float] = None
    total_amount_ug: Optional[float] = None
    volume_uL: Optional[float] = None
    sampled_portion: Optional[Union[str, "SamplePortionEnum"]] = None
    sampled_during: Optional[Union[str, SampleProcessingId]] = None
    replicate: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessedSampleId):
            self.id = ProcessedSampleId(self.id)

        if self.storage_location is not None and not isinstance(self.storage_location, str):
            self.storage_location = str(self.storage_location)

        if self.label_text is not None and not isinstance(self.label_text, str):
            self.label_text = str(self.label_text)

        if self.concentration_ug_per_uL is not None and not isinstance(self.concentration_ug_per_uL, float):
            self.concentration_ug_per_uL = float(self.concentration_ug_per_uL)

        if self.total_amount_ug is not None and not isinstance(self.total_amount_ug, float):
            self.total_amount_ug = float(self.total_amount_ug)

        if self.volume_uL is not None and not isinstance(self.volume_uL, float):
            self.volume_uL = float(self.volume_uL)

        if self.sampled_portion is not None and not isinstance(self.sampled_portion, SamplePortionEnum):
            self.sampled_portion = SamplePortionEnum(self.sampled_portion)

        if self.sampled_during is not None and not isinstance(self.sampled_during, SampleProcessingId):
            self.sampled_during = SampleProcessingId(self.sampled_during)

        if self.replicate is not None and not isinstance(self.replicate, int):
            self.replicate = int(self.replicate)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CoreSection(ProcessedSample):
    """
    A section of a core sample (TOP, MID, BTM).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["CoreSection"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:CoreSection"
    class_name: ClassVar[str] = "CoreSection"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.CoreSection

    id: Union[str, CoreSectionId] = None
    name: str = None
    core_section: Union[str, "CoreSectionEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CoreSectionId):
            self.id = CoreSectionId(self.id)

        if self._is_empty(self.core_section):
            self.MissingRequiredField("core_section")
        if not isinstance(self.core_section, CoreSectionEnum):
            self.core_section = CoreSectionEnum(self.core_section)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SamplingActivity(YAMLRoot):
    """
    An activity that involves the collection of a sample. This class serves as an abstract class to relate subclasses
    of sampling activities. Samples reference their parent sampling activity via the 'sampled_during' slot.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["SamplingActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:SamplingActivity"
    class_name: ClassVar[str] = "SamplingActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.SamplingActivity

    id: Union[str, SamplingActivityId] = None
    name: str = None
    description: Optional[str] = None
    project: Optional[int] = None
    emsl_activity: Optional[str] = None
    collection_date: Optional[Union[str, XSDDate]] = None
    shipped_sample_size: Optional[str] = None
    sampled_at_site: Optional[Union[str, SiteId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SamplingActivityId):
            self.id = SamplingActivityId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.project is not None and not isinstance(self.project, int):
            self.project = int(self.project)

        if self.emsl_activity is not None and not isinstance(self.emsl_activity, str):
            self.emsl_activity = str(self.emsl_activity)

        if self.collection_date is not None and not isinstance(self.collection_date, XSDDate):
            self.collection_date = XSDDate(self.collection_date)

        if self.shipped_sample_size is not None and not isinstance(self.shipped_sample_size, str):
            self.shipped_sample_size = str(self.shipped_sample_size)

        if self.sampled_at_site is not None and not isinstance(self.sampled_at_site, SiteId):
            self.sampled_at_site = SiteId(self.sampled_at_site)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AerosolArmSamplingActivity(SamplingActivity):
    """
    A sampling activity where aerosol samples were collected by ARM.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["AerosolArmSamplingActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:AerosolArmSamplingActivity"
    class_name: ClassVar[str] = "AerosolArmSamplingActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.AerosolArmSamplingActivity

    id: Union[str, AerosolArmSamplingActivityId] = None
    name: str = None
    humidity: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AerosolArmSamplingActivityId):
            self.id = AerosolArmSamplingActivityId(self.id)

        if self.humidity is not None and not isinstance(self.humidity, str):
            self.humidity = str(self.humidity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AerosolSamplingActivity(SamplingActivity):
    """
    A sampling activity where aerosol samples were collected.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["AerosolSamplingActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:AerosolSamplingActivity"
    class_name: ClassVar[str] = "AerosolSamplingActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.AerosolSamplingActivity

    id: Union[str, AerosolSamplingActivityId] = None
    name: str = None
    collection_time: Optional[str] = None
    humidity: Optional[str] = None
    sample_collected: Optional[str] = None
    sample_collection_dev: Optional[str] = None
    sampling_duration: Optional[str] = None
    wind_direction: Optional[Union[str, "CardinalDirectionEnum"]] = None
    wind_speed: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AerosolSamplingActivityId):
            self.id = AerosolSamplingActivityId(self.id)

        if self.collection_time is not None and not isinstance(self.collection_time, str):
            self.collection_time = str(self.collection_time)

        if self.humidity is not None and not isinstance(self.humidity, str):
            self.humidity = str(self.humidity)

        if self.sample_collected is not None and not isinstance(self.sample_collected, str):
            self.sample_collected = str(self.sample_collected)

        if self.sample_collection_dev is not None and not isinstance(self.sample_collection_dev, str):
            self.sample_collection_dev = str(self.sample_collection_dev)

        if self.sampling_duration is not None and not isinstance(self.sampling_duration, str):
            self.sampling_duration = str(self.sampling_duration)

        if self.wind_direction is not None and not isinstance(self.wind_direction, CardinalDirectionEnum):
            self.wind_direction = CardinalDirectionEnum(self.wind_direction)

        if self.wind_speed is not None and not isinstance(self.wind_speed, str):
            self.wind_speed = str(self.wind_speed)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CommerciallyPurchasedSamplingActivity(SamplingActivity):
    """
    Collection of samples that were purchased by the user.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["CommerciallyPurchasedSamplingActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:CommerciallyPurchasedSamplingActivity"
    class_name: ClassVar[str] = "CommerciallyPurchasedSamplingActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.CommerciallyPurchasedSamplingActivity

    id: Union[str, CommerciallyPurchasedSamplingActivityId] = None
    name: str = None
    sample_collected: Optional[str] = None
    sample_collection_dev: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CommerciallyPurchasedSamplingActivityId):
            self.id = CommerciallyPurchasedSamplingActivityId(self.id)

        if self.sample_collected is not None and not isinstance(self.sample_collected, str):
            self.sample_collected = str(self.sample_collected)

        if self.sample_collection_dev is not None and not isinstance(self.sample_collection_dev, str):
            self.sample_collection_dev = str(self.sample_collection_dev)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CultureEnvironmentalSamplingActivity(SamplingActivity):
    """
    Collection of samples from a culture of organisms taken from the environment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["CultureEnvironmentalSamplingActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:CultureEnvironmentalSamplingActivity"
    class_name: ClassVar[str] = "CultureEnvironmentalSamplingActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.CultureEnvironmentalSamplingActivity

    id: Union[str, CultureEnvironmentalSamplingActivityId] = None
    name: str = None
    collection_time: Optional[str] = None
    sample_collected: Optional[str] = None
    sample_collection_dev: Optional[str] = None
    sample_collection_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CultureEnvironmentalSamplingActivityId):
            self.id = CultureEnvironmentalSamplingActivityId(self.id)

        if self.collection_time is not None and not isinstance(self.collection_time, str):
            self.collection_time = str(self.collection_time)

        if self.sample_collected is not None and not isinstance(self.sample_collected, str):
            self.sample_collected = str(self.sample_collected)

        if self.sample_collection_dev is not None and not isinstance(self.sample_collection_dev, str):
            self.sample_collection_dev = str(self.sample_collection_dev)

        if self.sample_collection_method is not None and not isinstance(self.sample_collection_method, str):
            self.sample_collection_method = str(self.sample_collection_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EngineeredStrainSamplingActivity(SamplingActivity):
    """
    Collection of samples from a culture of an engineered organism.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["EngineeredStrainSamplingActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:EngineeredStrainSamplingActivity"
    class_name: ClassVar[str] = "EngineeredStrainSamplingActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.EngineeredStrainSamplingActivity

    id: Union[str, EngineeredStrainSamplingActivityId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EngineeredStrainSamplingActivityId):
            self.id = EngineeredStrainSamplingActivityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FieldDeployedTerraformSamplingActivity(SamplingActivity):
    """
    Collection of samples from a field-deployed Terraform device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["FieldDeployedTerraformSamplingActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:FieldDeployedTerraformSamplingActivity"
    class_name: ClassVar[str] = "FieldDeployedTerraformSamplingActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.FieldDeployedTerraformSamplingActivity

    id: Union[str, FieldDeployedTerraformSamplingActivityId] = None
    name: str = None
    collection_time: Optional[str] = None
    sample_collected: Optional[str] = None
    sample_collection_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FieldDeployedTerraformSamplingActivityId):
            self.id = FieldDeployedTerraformSamplingActivityId(self.id)

        if self.collection_time is not None and not isinstance(self.collection_time, str):
            self.collection_time = str(self.collection_time)

        if self.sample_collected is not None and not isinstance(self.sample_collected, str):
            self.sample_collected = str(self.sample_collected)

        if self.sample_collection_method is not None and not isinstance(self.sample_collection_method, str):
            self.sample_collection_method = str(self.sample_collection_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MixedCultureSamplingActivity(SamplingActivity):
    """
    Collection of samples from a mixed culture.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["MixedCultureSamplingActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:MixedCultureSamplingActivity"
    class_name: ClassVar[str] = "MixedCultureSamplingActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.MixedCultureSamplingActivity

    id: Union[str, MixedCultureSamplingActivityId] = None
    name: str = None
    collection_time: Optional[str] = None
    sample_collected: Optional[str] = None
    sample_collection_dev: Optional[str] = None
    sample_collection_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MixedCultureSamplingActivityId):
            self.id = MixedCultureSamplingActivityId(self.id)

        if self.collection_time is not None and not isinstance(self.collection_time, str):
            self.collection_time = str(self.collection_time)

        if self.sample_collected is not None and not isinstance(self.sample_collected, str):
            self.sample_collected = str(self.sample_collected)

        if self.sample_collection_dev is not None and not isinstance(self.sample_collection_dev, str):
            self.sample_collection_dev = str(self.sample_collection_dev)

        if self.sample_collection_method is not None and not isinstance(self.sample_collection_method, str):
            self.sample_collection_method = str(self.sample_collection_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MonetSoilSamplingActivity(SamplingActivity):
    """
    Collection of soil cores according to the MONet soil sampling protocol.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["MonetSoilSamplingActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:MonetSoilSamplingActivity"
    class_name: ClassVar[str] = "MonetSoilSamplingActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.MonetSoilSamplingActivity

    id: Union[str, MonetSoilSamplingActivityId] = None
    name: str = None
    collection_time: str = None
    infiltration_1: str = None
    infiltration_2: str = None
    sample_collection_dev: str = None
    infiltration_notes: Optional[str] = None
    weather: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MonetSoilSamplingActivityId):
            self.id = MonetSoilSamplingActivityId(self.id)

        if self._is_empty(self.collection_time):
            self.MissingRequiredField("collection_time")
        if not isinstance(self.collection_time, str):
            self.collection_time = str(self.collection_time)

        if self._is_empty(self.infiltration_1):
            self.MissingRequiredField("infiltration_1")
        if not isinstance(self.infiltration_1, str):
            self.infiltration_1 = str(self.infiltration_1)

        if self._is_empty(self.infiltration_2):
            self.MissingRequiredField("infiltration_2")
        if not isinstance(self.infiltration_2, str):
            self.infiltration_2 = str(self.infiltration_2)

        if self._is_empty(self.sample_collection_dev):
            self.MissingRequiredField("sample_collection_dev")
        if not isinstance(self.sample_collection_dev, str):
            self.sample_collection_dev = str(self.sample_collection_dev)

        if self.infiltration_notes is not None and not isinstance(self.infiltration_notes, str):
            self.infiltration_notes = str(self.infiltration_notes)

        if self.weather is not None and not isinstance(self.weather, str):
            self.weather = str(self.weather)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OtherUndescribedSamplingActivity(SamplingActivity):
    """
    Collection of samples from source that does not fit into any of the other categories.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["OtherUndescribedSamplingActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:OtherUndescribedSamplingActivity"
    class_name: ClassVar[str] = "OtherUndescribedSamplingActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.OtherUndescribedSamplingActivity

    id: Union[str, OtherUndescribedSamplingActivityId] = None
    name: str = None
    collection_time: Optional[str] = None
    humidity: Optional[str] = None
    sample_collected: Optional[str] = None
    sample_collection_dev: Optional[str] = None
    sample_collection_method: Optional[str] = None
    sampling_duration: Optional[str] = None
    wind_direction: Optional[Union[str, "CardinalDirectionEnum"]] = None
    wind_speed: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OtherUndescribedSamplingActivityId):
            self.id = OtherUndescribedSamplingActivityId(self.id)

        if self.collection_time is not None and not isinstance(self.collection_time, str):
            self.collection_time = str(self.collection_time)

        if self.humidity is not None and not isinstance(self.humidity, str):
            self.humidity = str(self.humidity)

        if self.sample_collected is not None and not isinstance(self.sample_collected, str):
            self.sample_collected = str(self.sample_collected)

        if self.sample_collection_dev is not None and not isinstance(self.sample_collection_dev, str):
            self.sample_collection_dev = str(self.sample_collection_dev)

        if self.sample_collection_method is not None and not isinstance(self.sample_collection_method, str):
            self.sample_collection_method = str(self.sample_collection_method)

        if self.sampling_duration is not None and not isinstance(self.sampling_duration, str):
            self.sampling_duration = str(self.sampling_duration)

        if self.wind_direction is not None and not isinstance(self.wind_direction, CardinalDirectionEnum):
            self.wind_direction = CardinalDirectionEnum(self.wind_direction)

        if self.wind_speed is not None and not isinstance(self.wind_speed, str):
            self.wind_speed = str(self.wind_speed)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PlantSamplingActivity(SamplingActivity):
    """
    Collection of samples associated with plants.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["PlantSamplingActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:PlantSamplingActivity"
    class_name: ClassVar[str] = "PlantSamplingActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.PlantSamplingActivity

    id: Union[str, PlantSamplingActivityId] = None
    name: str = None
    collection_time: Optional[str] = None
    sample_collected: Optional[str] = None
    sample_collection_dev: Optional[str] = None
    sample_collection_method: Optional[str] = None
    weather: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlantSamplingActivityId):
            self.id = PlantSamplingActivityId(self.id)

        if self.collection_time is not None and not isinstance(self.collection_time, str):
            self.collection_time = str(self.collection_time)

        if self.sample_collected is not None and not isinstance(self.sample_collected, str):
            self.sample_collected = str(self.sample_collected)

        if self.sample_collection_dev is not None and not isinstance(self.sample_collection_dev, str):
            self.sample_collection_dev = str(self.sample_collection_dev)

        if self.sample_collection_method is not None and not isinstance(self.sample_collection_method, str):
            self.sample_collection_method = str(self.sample_collection_method)

        if self.weather is not None and not isinstance(self.weather, str):
            self.weather = str(self.weather)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PureCultureSamplingActivity(SamplingActivity):
    """
    Collection of samples from a culture containing a single organism.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["PureCultureSamplingActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:PureCultureSamplingActivity"
    class_name: ClassVar[str] = "PureCultureSamplingActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.PureCultureSamplingActivity

    id: Union[str, PureCultureSamplingActivityId] = None
    name: str = None
    collection_time: Optional[str] = None
    sample_collected: Optional[str] = None
    sample_collection_dev: Optional[str] = None
    sample_collection_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PureCultureSamplingActivityId):
            self.id = PureCultureSamplingActivityId(self.id)

        if self.collection_time is not None and not isinstance(self.collection_time, str):
            self.collection_time = str(self.collection_time)

        if self.sample_collected is not None and not isinstance(self.sample_collected, str):
            self.sample_collected = str(self.sample_collected)

        if self.sample_collection_dev is not None and not isinstance(self.sample_collection_dev, str):
            self.sample_collection_dev = str(self.sample_collection_dev)

        if self.sample_collection_method is not None and not isinstance(self.sample_collection_method, str):
            self.sample_collection_method = str(self.sample_collection_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SedimentSamplingActivity(SamplingActivity):
    """
    Collection of sediment samples from the environment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["SedimentSamplingActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:SedimentSamplingActivity"
    class_name: ClassVar[str] = "SedimentSamplingActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.SedimentSamplingActivity

    id: Union[str, SedimentSamplingActivityId] = None
    name: str = None
    collection_time: Optional[str] = None
    sample_collected: Optional[str] = None
    sample_collection_dev: Optional[str] = None
    sample_collection_method: Optional[str] = None
    weather: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SedimentSamplingActivityId):
            self.id = SedimentSamplingActivityId(self.id)

        if self.collection_time is not None and not isinstance(self.collection_time, str):
            self.collection_time = str(self.collection_time)

        if self.sample_collected is not None and not isinstance(self.sample_collected, str):
            self.sample_collected = str(self.sample_collected)

        if self.sample_collection_dev is not None and not isinstance(self.sample_collection_dev, str):
            self.sample_collection_dev = str(self.sample_collection_dev)

        if self.sample_collection_method is not None and not isinstance(self.sample_collection_method, str):
            self.sample_collection_method = str(self.sample_collection_method)

        if self.weather is not None and not isinstance(self.weather, str):
            self.weather = str(self.weather)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SoilSamplingActivity(SamplingActivity):
    """
    Collection of soil samples from the environment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["SoilSamplingActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:SoilSamplingActivity"
    class_name: ClassVar[str] = "SoilSamplingActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.SoilSamplingActivity

    id: Union[str, SoilSamplingActivityId] = None
    name: str = None
    description: Optional[str] = None
    collection_time: Optional[str] = None
    infiltration_1: Optional[str] = None
    infiltration_2: Optional[str] = None
    infiltration_notes: Optional[str] = None
    sample_collected: Optional[str] = None
    sample_collection_dev: Optional[str] = None
    sample_collection_method: Optional[str] = None
    wind_direction: Optional[Union[str, "CardinalDirectionEnum"]] = None
    weather: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SoilSamplingActivityId):
            self.id = SoilSamplingActivityId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.collection_time is not None and not isinstance(self.collection_time, str):
            self.collection_time = str(self.collection_time)

        if self.infiltration_1 is not None and not isinstance(self.infiltration_1, str):
            self.infiltration_1 = str(self.infiltration_1)

        if self.infiltration_2 is not None and not isinstance(self.infiltration_2, str):
            self.infiltration_2 = str(self.infiltration_2)

        if self.infiltration_notes is not None and not isinstance(self.infiltration_notes, str):
            self.infiltration_notes = str(self.infiltration_notes)

        if self.sample_collected is not None and not isinstance(self.sample_collected, str):
            self.sample_collected = str(self.sample_collected)

        if self.sample_collection_dev is not None and not isinstance(self.sample_collection_dev, str):
            self.sample_collection_dev = str(self.sample_collection_dev)

        if self.sample_collection_method is not None and not isinstance(self.sample_collection_method, str):
            self.sample_collection_method = str(self.sample_collection_method)

        if self.wind_direction is not None and not isinstance(self.wind_direction, CardinalDirectionEnum):
            self.wind_direction = CardinalDirectionEnum(self.wind_direction)

        if self.weather is not None and not isinstance(self.weather, str):
            self.weather = str(self.weather)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SynthesizedMaterialSamplingActivity(SamplingActivity):
    """
    Collection of samples of a synthesized material.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["SynthesizedMaterialSamplingActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:SynthesizedMaterialSamplingActivity"
    class_name: ClassVar[str] = "SynthesizedMaterialSamplingActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.SynthesizedMaterialSamplingActivity

    id: Union[str, SynthesizedMaterialSamplingActivityId] = None
    name: str = None
    sample_collected: Optional[str] = None
    sample_collection_dev: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SynthesizedMaterialSamplingActivityId):
            self.id = SynthesizedMaterialSamplingActivityId(self.id)

        if self.sample_collected is not None and not isinstance(self.sample_collected, str):
            self.sample_collected = str(self.sample_collected)

        if self.sample_collection_dev is not None and not isinstance(self.sample_collection_dev, str):
            self.sample_collection_dev = str(self.sample_collection_dev)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TerraformSamplingActivity(SamplingActivity):
    """
    Collection of samples from a Terraform device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["TerraformSamplingActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:TerraformSamplingActivity"
    class_name: ClassVar[str] = "TerraformSamplingActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.TerraformSamplingActivity

    id: Union[str, TerraformSamplingActivityId] = None
    name: str = None
    collection_time: Optional[str] = None
    sample_collected: Optional[str] = None
    sample_collection_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TerraformSamplingActivityId):
            self.id = TerraformSamplingActivityId(self.id)

        if self.collection_time is not None and not isinstance(self.collection_time, str):
            self.collection_time = str(self.collection_time)

        if self.sample_collected is not None and not isinstance(self.sample_collected, str):
            self.sample_collected = str(self.sample_collected)

        if self.sample_collection_method is not None and not isinstance(self.sample_collection_method, str):
            self.sample_collection_method = str(self.sample_collection_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WaterSamplingActivity(SamplingActivity):
    """
    Collection of water samples.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["WaterSamplingActivity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:WaterSamplingActivity"
    class_name: ClassVar[str] = "WaterSamplingActivity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.WaterSamplingActivity

    id: Union[str, WaterSamplingActivityId] = None
    name: str = None
    sample_collection_dev: str = None
    sample_collection_method: str = None
    collection_time: Optional[str] = None
    sample_collected: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WaterSamplingActivityId):
            self.id = WaterSamplingActivityId(self.id)

        if self._is_empty(self.sample_collection_dev):
            self.MissingRequiredField("sample_collection_dev")
        if not isinstance(self.sample_collection_dev, str):
            self.sample_collection_dev = str(self.sample_collection_dev)

        if self._is_empty(self.sample_collection_method):
            self.MissingRequiredField("sample_collection_method")
        if not isinstance(self.sample_collection_method, str):
            self.sample_collection_method = str(self.sample_collection_method)

        if self.collection_time is not None and not isinstance(self.collection_time, str):
            self.collection_time = str(self.collection_time)

        if self.sample_collected is not None and not isinstance(self.sample_collected, str):
            self.sample_collected = str(self.sample_collected)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiologicalEntity(YAMLRoot):
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
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["BiologicalEntity"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:BiologicalEntity"
    class_name: ClassVar[str] = "biological_entity"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.BiologicalEntity

    id: Union[str, BiologicalEntityId] = None
    name: str = None
    strain_identifier: str = None
    description: Optional[str] = None
    organism_name: Optional[str] = None
    taxonomy_id: Optional[str] = None
    host_common_name: Optional[str] = None
    host_taxid: Optional[str] = None
    strain_source: Optional[str] = None
    strain_type: Optional[Union[str, "StrainTypeEnum"]] = None
    modification_method: Optional[Union[str, "ModificationMethodEnum"]] = None
    strain_description: Optional[str] = None
    strain_mutation: Optional[str] = None
    phenotype: Optional[str] = None
    trait: Optional[Union[str, "IntendedTraitEnum"]] = None
    encoded_traits: Optional[str] = None
    genotype_segment_category: Optional[Union[str, "GenotypeSegmentEnum"]] = None
    genotype_segment_name: Optional[str] = None
    component_name: Optional[str] = None
    construct_component: Optional[Union[str, "ConstructComponentEnum"]] = None
    donor_organism: Optional[str] = None
    component_description: Optional[str] = None
    trophic_level: Optional[Union[str, "TrophicLevelEnum"]] = None
    pathogenicity: Optional[str] = None
    host_spec_range: Optional[str] = None
    propagation: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiologicalEntityId):
            self.id = BiologicalEntityId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.strain_identifier):
            self.MissingRequiredField("strain_identifier")
        if not isinstance(self.strain_identifier, str):
            self.strain_identifier = str(self.strain_identifier)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.organism_name is not None and not isinstance(self.organism_name, str):
            self.organism_name = str(self.organism_name)

        if self.taxonomy_id is not None and not isinstance(self.taxonomy_id, str):
            self.taxonomy_id = str(self.taxonomy_id)

        if self.host_common_name is not None and not isinstance(self.host_common_name, str):
            self.host_common_name = str(self.host_common_name)

        if self.host_taxid is not None and not isinstance(self.host_taxid, str):
            self.host_taxid = str(self.host_taxid)

        if self.strain_source is not None and not isinstance(self.strain_source, str):
            self.strain_source = str(self.strain_source)

        if self.strain_type is not None and not isinstance(self.strain_type, StrainTypeEnum):
            self.strain_type = StrainTypeEnum(self.strain_type)

        if self.modification_method is not None and not isinstance(self.modification_method, ModificationMethodEnum):
            self.modification_method = ModificationMethodEnum(self.modification_method)

        if self.strain_description is not None and not isinstance(self.strain_description, str):
            self.strain_description = str(self.strain_description)

        if self.strain_mutation is not None and not isinstance(self.strain_mutation, str):
            self.strain_mutation = str(self.strain_mutation)

        if self.phenotype is not None and not isinstance(self.phenotype, str):
            self.phenotype = str(self.phenotype)

        if self.trait is not None and not isinstance(self.trait, IntendedTraitEnum):
            self.trait = IntendedTraitEnum(self.trait)

        if self.encoded_traits is not None and not isinstance(self.encoded_traits, str):
            self.encoded_traits = str(self.encoded_traits)

        if self.genotype_segment_category is not None and not isinstance(self.genotype_segment_category, GenotypeSegmentEnum):
            self.genotype_segment_category = GenotypeSegmentEnum(self.genotype_segment_category)

        if self.genotype_segment_name is not None and not isinstance(self.genotype_segment_name, str):
            self.genotype_segment_name = str(self.genotype_segment_name)

        if self.component_name is not None and not isinstance(self.component_name, str):
            self.component_name = str(self.component_name)

        if self.construct_component is not None and not isinstance(self.construct_component, ConstructComponentEnum):
            self.construct_component = ConstructComponentEnum(self.construct_component)

        if self.donor_organism is not None and not isinstance(self.donor_organism, str):
            self.donor_organism = str(self.donor_organism)

        if self.component_description is not None and not isinstance(self.component_description, str):
            self.component_description = str(self.component_description)

        if self.trophic_level is not None and not isinstance(self.trophic_level, TrophicLevelEnum):
            self.trophic_level = TrophicLevelEnum(self.trophic_level)

        if self.pathogenicity is not None and not isinstance(self.pathogenicity, str):
            self.pathogenicity = str(self.pathogenicity)

        if self.host_spec_range is not None and not isinstance(self.host_spec_range, str):
            self.host_spec_range = str(self.host_spec_range)

        if self.propagation is not None and not isinstance(self.propagation, str):
            self.propagation = str(self.propagation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Study(YAMLRoot):
    """
    A study or research project, typically associated with a proposal and a set of experiments.
    A study may have multiple participants, each with different roles, and may be associated with
    one or more campaigns. The study may also have associated DOIs and funding sources.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["Study"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.Study

    id: Union[str, StudyId] = None
    project_id: int = None
    name: str = None
    principal_investigator: Union[str, PersonValueId] = None
    external_identifiers: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    title: Optional[str] = None
    proposal_abstract: Optional[str] = None
    description: Optional[str] = None
    has_participants: Optional[Union[Union[str, ProjectParticipantId], list[Union[str, ProjectParticipantId]]]] = empty_list()
    collaborating_institution: Optional[str] = None
    project_status: Optional[Union[str, "ProjectStatusEnum"]] = None
    project_start: Optional[Union[str, XSDDateTime]] = None
    project_end: Optional[Union[str, XSDDateTime]] = None
    associated_dois: Optional[Union[Union[dict, "DOI"], list[Union[dict, "DOI"]]]] = empty_list()
    funding_sources: Optional[Union[Union[dict, "DOI"], list[Union[dict, "DOI"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)

        if self._is_empty(self.project_id):
            self.MissingRequiredField("project_id")
        if not isinstance(self.project_id, int):
            self.project_id = int(self.project_id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.principal_investigator):
            self.MissingRequiredField("principal_investigator")
        if not isinstance(self.principal_investigator, PersonValueId):
            self.principal_investigator = PersonValueId(self.principal_investigator)

        if not isinstance(self.external_identifiers, list):
            self.external_identifiers = [self.external_identifiers] if self.external_identifiers is not None else []
        self.external_identifiers = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.external_identifiers]

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.proposal_abstract is not None and not isinstance(self.proposal_abstract, str):
            self.proposal_abstract = str(self.proposal_abstract)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.has_participants, list):
            self.has_participants = [self.has_participants] if self.has_participants is not None else []
        self.has_participants = [v if isinstance(v, ProjectParticipantId) else ProjectParticipantId(v) for v in self.has_participants]

        if self.collaborating_institution is not None and not isinstance(self.collaborating_institution, str):
            self.collaborating_institution = str(self.collaborating_institution)

        if self.project_status is not None and not isinstance(self.project_status, ProjectStatusEnum):
            self.project_status = ProjectStatusEnum(self.project_status)

        if self.project_start is not None and not isinstance(self.project_start, XSDDateTime):
            self.project_start = XSDDateTime(self.project_start)

        if self.project_end is not None and not isinstance(self.project_end, XSDDateTime):
            self.project_end = XSDDateTime(self.project_end)

        self._normalize_inlined_as_list(slot_name="associated_dois", slot_type=DOI, key_name="doi_value", keyed=False)

        self._normalize_inlined_as_list(slot_name="funding_sources", slot_type=DOI, key_name="doi_value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProjectParticipant(YAMLRoot):
    """
    A record of a person and their role on an EMSL project.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["ProjectParticipant"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:ProjectParticipant"
    class_name: ClassVar[str] = "ProjectParticipant"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.ProjectParticipant

    id: Union[str, ProjectParticipantId] = None
    role: Union[str, "NexusRoleEnum"] = None
    person: Union[str, PersonValueId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProjectParticipantId):
            self.id = ProjectParticipantId(self.id)

        if self._is_empty(self.role):
            self.MissingRequiredField("role")
        if not isinstance(self.role, NexusRoleEnum):
            self.role = NexusRoleEnum(self.role)

        if self._is_empty(self.person):
            self.MissingRequiredField("person")
        if not isinstance(self.person, PersonValueId):
            self.person = PersonValueId(self.person)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DOI(YAMLRoot):
    """
    A digital object identifier (DOI) representing a persistent link to a digital resource.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["DOI"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:DOI"
    class_name: ClassVar[str] = "DOI"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.DOI

    doi_value: Union[str, URIorCURIE] = None
    doi_category: Optional[Union[str, "DoiCategoryEnum"]] = None
    doi_provider: Optional[Union[str, "DoiProviderEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.doi_value):
            self.MissingRequiredField("doi_value")
        if not isinstance(self.doi_value, URIorCURIE):
            self.doi_value = URIorCURIE(self.doi_value)

        if self.doi_category is not None and not isinstance(self.doi_category, DoiCategoryEnum):
            self.doi_category = DoiCategoryEnum(self.doi_category)

        if self.doi_provider is not None and not isinstance(self.doi_provider, DoiProviderEnum):
            self.doi_provider = DoiProviderEnum(self.doi_provider)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TimestampValue(YAMLRoot):
    """
    A timestamp value with optional description. No pattern at present,
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["TimestampValue"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:TimestampValue"
    class_name: ClassVar[str] = "TimestampValue"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.TimestampValue

    id: Union[str, TimestampValueId] = None
    description: Optional[str] = None
    has_raw_value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TimestampValueId):
            self.id = TimestampValueId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.has_raw_value is not None and not isinstance(self.has_raw_value, str):
            self.has_raw_value = str(self.has_raw_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TextValue(YAMLRoot):
    """
    A text value with optional description and language.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["TextValue"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:TextValue"
    class_name: ClassVar[str] = "TextValue"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.TextValue

    id: Union[str, TextValueId] = None
    description: Optional[str] = None
    language: Optional[str] = None
    has_raw_value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TextValueId):
            self.id = TextValueId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.language is not None and not isinstance(self.language, str):
            self.language = str(self.language)

        if self.has_raw_value is not None and not isinstance(self.has_raw_value, str):
            self.has_raw_value = str(self.has_raw_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SoftwareControlledTermValue(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["SoftwareControlledTermValue"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:SoftwareControlledTermValue"
    class_name: ClassVar[str] = "SoftwareControlledTermValue"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.SoftwareControlledTermValue

    id: Union[str, SoftwareControlledTermValueId] = None
    name: str = None
    version: str = None
    description: Optional[str] = None
    has_raw_value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SoftwareControlledTermValueId):
            self.id = SoftwareControlledTermValueId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.has_raw_value is not None and not isinstance(self.has_raw_value, str):
            self.has_raw_value = str(self.has_raw_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControlledTermValue(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["ControlledTermValue"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:ControlledTermValue"
    class_name: ClassVar[str] = "ControlledTermValue"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.ControlledTermValue

    id: Union[str, ControlledTermValueId] = None
    description: Optional[str] = None
    has_raw_value: Optional[str] = None
    term: Optional[str] = None
    term_id: Optional[Union[str, URIorCURIE]] = None
    controlled_term_provider: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ControlledTermValueId):
            self.id = ControlledTermValueId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.has_raw_value is not None and not isinstance(self.has_raw_value, str):
            self.has_raw_value = str(self.has_raw_value)

        if self.term is not None and not isinstance(self.term, str):
            self.term = str(self.term)

        if self.term_id is not None and not isinstance(self.term_id, URIorCURIE):
            self.term_id = URIorCURIE(self.term_id)

        if self.controlled_term_provider is not None and not isinstance(self.controlled_term_provider, str):
            self.controlled_term_provider = str(self.controlled_term_provider)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonValue(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["PersonValue"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:PersonValue"
    class_name: ClassVar[str] = "PersonValue"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.PersonValue

    id: Union[str, PersonValueId] = None
    first_name: str = None
    last_name: str = None
    email: Optional[str] = None
    middle_initial: Optional[str] = None
    orcid: Optional[str] = None
    profile_image_url: Optional[str] = None
    websites: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonValueId):
            self.id = PersonValueId(self.id)

        if self._is_empty(self.first_name):
            self.MissingRequiredField("first_name")
        if not isinstance(self.first_name, str):
            self.first_name = str(self.first_name)

        if self._is_empty(self.last_name):
            self.MissingRequiredField("last_name")
        if not isinstance(self.last_name, str):
            self.last_name = str(self.last_name)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.middle_initial is not None and not isinstance(self.middle_initial, str):
            self.middle_initial = str(self.middle_initial)

        if self.orcid is not None and not isinstance(self.orcid, str):
            self.orcid = str(self.orcid)

        if self.profile_image_url is not None and not isinstance(self.profile_image_url, str):
            self.profile_image_url = str(self.profile_image_url)

        if self.websites is not None and not isinstance(self.websites, str):
            self.websites = str(self.websites)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityValue(YAMLRoot):
    """
    A quantity value with numeric value and optional unit
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["QuantityValue"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.QuantityValue

    id: Union[str, QuantityValueId] = None
    description: Optional[str] = None
    has_value_unit: Optional[str] = None
    has_unit: Optional[str] = None
    has_numeric_value: Optional[float] = None
    has_minimum_numeric_value: Optional[float] = None
    has_maximum_numeric_value: Optional[float] = None
    has_raw_value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuantityValueId):
            self.id = QuantityValueId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.has_value_unit is not None and not isinstance(self.has_value_unit, str):
            self.has_value_unit = str(self.has_value_unit)

        if self.has_unit is not None and not isinstance(self.has_unit, str):
            self.has_unit = str(self.has_unit)

        if self.has_numeric_value is not None and not isinstance(self.has_numeric_value, float):
            self.has_numeric_value = float(self.has_numeric_value)

        if self.has_minimum_numeric_value is not None and not isinstance(self.has_minimum_numeric_value, float):
            self.has_minimum_numeric_value = float(self.has_minimum_numeric_value)

        if self.has_maximum_numeric_value is not None and not isinstance(self.has_maximum_numeric_value, float):
            self.has_maximum_numeric_value = float(self.has_maximum_numeric_value)

        if self.has_raw_value is not None and not isinstance(self.has_raw_value, str):
            self.has_raw_value = str(self.has_raw_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConditioningValue(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["ConditioningValue"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:ConditioningValue"
    class_name: ClassVar[str] = "ConditioningValue"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.ConditioningValue

    id: Union[str, ConditioningValueId] = None
    source_material: Optional[str] = None
    instrument: Optional[str] = None
    gas: Optional[str] = None
    pressure: Optional[str] = None
    has_raw_value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConditioningValueId):
            self.id = ConditioningValueId(self.id)

        if self.source_material is not None and not isinstance(self.source_material, str):
            self.source_material = str(self.source_material)

        if self.instrument is not None and not isinstance(self.instrument, str):
            self.instrument = str(self.instrument)

        if self.gas is not None and not isinstance(self.gas, str):
            self.gas = str(self.gas)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.has_raw_value is not None and not isinstance(self.has_raw_value, str):
            self.has_raw_value = str(self.has_raw_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ZipDownload(YAMLRoot):
    """
    A zip download record, capturing the details of a zip file download event.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA["ZipDownload"]
    class_class_curie: ClassVar[str] = "analysis_api_schema:ZipDownload"
    class_name: ClassVar[str] = "zipDownload"
    class_model_uri: ClassVar[URIRef] = ANALYSIS_API_SCHEMA.ZipDownload

    id: Union[str, ZipDownloadId] = None
    time: Union[str, XSDDateTime] = None
    user: str = None
    files: int = None
    packages: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ZipDownloadId):
            self.id = ZipDownloadId(self.id)

        if self._is_empty(self.time):
            self.MissingRequiredField("time")
        if not isinstance(self.time, XSDDateTime):
            self.time = XSDDateTime(self.time)

        if self._is_empty(self.user):
            self.MissingRequiredField("user")
        if not isinstance(self.user, str):
            self.user = str(self.user)

        if self._is_empty(self.files):
            self.MissingRequiredField("files")
        if not isinstance(self.files, int):
            self.files = int(self.files)

        if self.packages is not None and not isinstance(self.packages, str):
            self.packages = str(self.packages)

        super().__post_init__(**kwargs)


# Enumerations
class AerosolTypeEnum(EnumDefinitionImpl):
    """
    Types of aerosol samples
    """
    sea_salt = PermissibleValue(
        text="sea_salt",
        description="Sea salt aerosol")
    dust = PermissibleValue(
        text="dust",
        description="Dust aerosol")
    volcanic_ash = PermissibleValue(
        text="volcanic_ash",
        description="Volcanic ash aerosol")

    _defn = EnumDefinition(
        name="AerosolTypeEnum",
        description="Types of aerosol samples",
    )

class AlternateIdentifierType(EnumDefinitionImpl):

    instrument_alt_id = PermissibleValue(text="instrument_alt_id")

    _defn = EnumDefinition(
        name="AlternateIdentifierType",
    )

class AnalysisTypeEnum(EnumDefinitionImpl):
    """
    Enumeration of common analyses performed on samples shipped to EMSL
    """
    metabolome = PermissibleValue(text="metabolome")
    proteome = PermissibleValue(text="proteome")
    lipidome = PermissibleValue(text="lipidome")
    genome = PermissibleValue(text="genome")
    transcriptome = PermissibleValue(text="transcriptome")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="AnalysisTypeEnum",
        description="Enumeration of common analyses performed on samples shipped to EMSL",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "organic matter",
            PermissibleValue(text="organic matter"))
        setattr(cls, "molecular structure",
            PermissibleValue(text="molecular structure"))
        setattr(cls, "chemical speciation mapping",
            PermissibleValue(text="chemical speciation mapping"))
        setattr(cls, "isotope profiling",
            PermissibleValue(text="isotope profiling"))
        setattr(cls, "imaging- xray",
            PermissibleValue(text="imaging- xray"))
        setattr(cls, "imaging- electron",
            PermissibleValue(text="imaging- electron"))
        setattr(cls, "imaging- ion",
            PermissibleValue(text="imaging- ion"))
        setattr(cls, "imaging- light",
            PermissibleValue(text="imaging- light"))
        setattr(cls, "hydraulic properties",
            PermissibleValue(text="hydraulic properties"))

class AnalyteCategoryEnum(EnumDefinitionImpl):
    """
    bundling common terms for different omics types by biomolecule being analyzed
    """
    dna = PermissibleValue(text="dna")
    rna = PermissibleValue(text="rna")
    protein = PermissibleValue(text="protein")
    metabolite = PermissibleValue(text="metabolite")
    lipid = PermissibleValue(text="lipid")
    natural_organic_matter = PermissibleValue(text="natural_organic_matter")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="AnalyteCategoryEnum",
        description="bundling common terms for different omics types by biomolecule being analyzed",
    )

class AnnotationDatabaseEnum(EnumDefinitionImpl):

    PFAM = PermissibleValue(text="PFAM")
    COG = PermissibleValue(text="COG")
    KEGG = PermissibleValue(text="KEGG")

    _defn = EnumDefinition(
        name="AnnotationDatabaseEnum",
    )

class BinQuality(EnumDefinitionImpl):

    HQ = PermissibleValue(text="HQ")
    MQ = PermissibleValue(text="MQ")
    LQ = PermissibleValue(text="LQ")

    _defn = EnumDefinition(
        name="BinQuality",
    )

class BiolStatEnum(EnumDefinitionImpl):

    wild = PermissibleValue(text="wild")
    natural = PermissibleValue(text="natural")
    hybrid = PermissibleValue(text="hybrid")
    mutant = PermissibleValue(text="mutant")

    _defn = EnumDefinition(
        name="BiolStatEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "semi-natural",
            PermissibleValue(text="semi-natural"))
        setattr(cls, "inbred line",
            PermissibleValue(text="inbred line"))
        setattr(cls, "breeder's line",
            PermissibleValue(text="breeder's line"))
        setattr(cls, "clonal selection",
            PermissibleValue(text="clonal selection"))

class BioticRelationshipEnum(EnumDefinitionImpl):
    """
    Sample biotic relationships
    """
    free_living = PermissibleValue(
        text="free_living",
        description="Free-living organism")
    parasite = PermissibleValue(
        text="parasite",
        description="Parasitic organism")
    commensal = PermissibleValue(
        text="commensal",
        description="Commensal organism")
    symbiont = PermissibleValue(
        text="symbiont",
        description="Symbiotic organism")

    _defn = EnumDefinition(
        name="BioticRelationshipEnum",
        description="Sample biotic relationships",
    )

class CalibrationTargetEnum(EnumDefinitionImpl):

    mass_charge_ratio = PermissibleValue(
        text="mass_charge_ratio",
        title="m/z")
    retention_time = PermissibleValue(text="retention_time")
    retention_index = PermissibleValue(text="retention_index")

    _defn = EnumDefinition(
        name="CalibrationTargetEnum",
    )

class CardinalDirectionEnum(EnumDefinitionImpl):

    north = PermissibleValue(text="north")
    north_east = PermissibleValue(text="north_east")
    east = PermissibleValue(text="east")
    south_east = PermissibleValue(text="south_east")
    south = PermissibleValue(text="south")
    south_west = PermissibleValue(text="south_west")
    west = PermissibleValue(text="west")
    north_west = PermissibleValue(text="north_west")

    _defn = EnumDefinition(
        name="CardinalDirectionEnum",
    )

class ChemicalEntityEnum(EnumDefinitionImpl):
    """
    Common names or identifiers for chemical entities.
    """
    acetonitrile = PermissibleValue(
        text="acetonitrile",
        meaning=CHEBI["38472"])
    acetic_acid = PermissibleValue(
        text="acetic_acid",
        meaning=CHEBI["15366"])
    alphaLP = PermissibleValue(
        text="alphaLP",
        meaning=EC["3.4.21.12"])
    ammonium_acetate = PermissibleValue(
        text="ammonium_acetate",
        meaning=CHEBI["62947"])
    ammonium_bicarbonate = PermissibleValue(
        text="ammonium_bicarbonate",
        meaning=CHEBI["184335"])
    amitriptyline = PermissibleValue(
        text="amitriptyline",
        meaning=CHEBI["2666"])
    chloroform = PermissibleValue(
        text="chloroform",
        meaning=CHEBI["35255"])
    chymotrypsin = PermissibleValue(
        text="chymotrypsin",
        meaning=MS["1001306"])
    ethanol = PermissibleValue(
        text="ethanol",
        meaning=CHEBI["16236"])
    formic_acid = PermissibleValue(
        text="formic_acid",
        meaning=CHEBI["30751"])
    glucose = PermissibleValue(
        text="glucose",
        meaning=CHEBI["17234"])
    hydrochloric_acid = PermissibleValue(
        text="hydrochloric_acid",
        meaning=CHEBI["17883"])
    isopropyl_alcohol = PermissibleValue(
        text="isopropyl_alcohol",
        meaning=CHEBI["17824"])
    methanol = PermissibleValue(
        text="methanol",
        meaning=CHEBI["17790"])
    methoxyamine = PermissibleValue(
        text="methoxyamine",
        meaning=CHEBI["192842"])
    medronic_acid = PermissibleValue(
        text="medronic_acid",
        meaning=CHEBI["43945"])
    phosphoric_acid = PermissibleValue(
        text="phosphoric_acid",
        meaning=CHEBI["26078"])
    trimethylchlorosilane = PermissibleValue(
        text="trimethylchlorosilane",
        meaning=CHEBI["85069"])
    trypsin = PermissibleValue(
        text="trypsin",
        meaning=MS["1001251"])
    water = PermissibleValue(
        text="water",
        meaning=CHEBI["15377"])

    _defn = EnumDefinition(
        name="ChemicalEntityEnum",
        description="Common names or identifiers for chemical entities.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Arg-C",
            PermissibleValue(
                text="Arg-C",
                meaning=MS["1001303"]))
        setattr(cls, "Asp-N",
            PermissibleValue(
                text="Asp-N",
                meaning=MS["1001304"]))
        setattr(cls, "Glu-C",
            PermissibleValue(
                text="Glu-C",
                meaning=MS["1001917"]))
        setattr(cls, "Lys-C",
            PermissibleValue(
                text="Lys-C",
                meaning=MS["1001309"]))
        setattr(cls, "Lys-N",
            PermissibleValue(
                text="Lys-N",
                meaning=MS["1003093"]))
        setattr(cls, "N-methyl-N-trimethylsilyltrifluoroacetamide",
            PermissibleValue(
                text="N-methyl-N-trimethylsilyltrifluoroacetamide",
                meaning=CHEBI["85064"]))

class ChromatographyCategoryEnum(EnumDefinitionImpl):

    liquid_chromatography = PermissibleValue(text="liquid_chromatography")
    gas_chromatography = PermissibleValue(text="gas_chromatography")
    solid_phase_extraction = PermissibleValue(text="solid_phase_extraction")

    _defn = EnumDefinition(
        name="ChromatographyCategoryEnum",
    )

class ColorCodeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ColorCodeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Red- 0-250m Profiling",
            PermissibleValue(text="Red- 0-250m Profiling"))
        setattr(cls, "Red Hashed- 0-250m Loitering",
            PermissibleValue(text="Red Hashed- 0-250m Loitering"))
        setattr(cls, "Yellow- 251-500m Profiling",
            PermissibleValue(text="Yellow- 251-500m Profiling"))
        setattr(cls, "Yellow Hashed- 251-500m Loitering",
            PermissibleValue(text="Yellow Hashed- 251-500m Loitering"))
        setattr(cls, "Green- 501-750m Profiling",
            PermissibleValue(text="Green- 501-750m Profiling"))
        setattr(cls, "Green Hashed- 501-750m Loitering",
            PermissibleValue(text="Green Hashed- 501-750m Loitering"))
        setattr(cls, "Blue- 751-1000m Profiling",
            PermissibleValue(text="Blue- 751-1000m Profiling"))
        setattr(cls, "Blue Hashed- 751-1000m Loitering",
            PermissibleValue(text="Blue Hashed- 751-1000m Loitering"))
        setattr(cls, "Purple- >=1001m Profiling",
            PermissibleValue(text="Purple- >=1001m Profiling"))
        setattr(cls, "Purple Hashed- >=1001m Loitering",
            PermissibleValue(text="Purple Hashed- >=1001m Loitering"))

class ConstructComponentEnum(EnumDefinitionImpl):

    Enhancer = PermissibleValue(text="Enhancer")
    Exon = PermissibleValue(text="Exon")
    Gene = PermissibleValue(text="Gene")
    Intron = PermissibleValue(text="Intron")
    Promoter = PermissibleValue(text="Promoter")
    Spacer = PermissibleValue(text="Spacer")
    Terminator = PermissibleValue(text="Terminator")

    _defn = EnumDefinition(
        name="ConstructComponentEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "None",
            PermissibleValue(text="None"))
        setattr(cls, "3'UTR",
            PermissibleValue(text="3'UTR"))
        setattr(cls, "5'UTR",
            PermissibleValue(text="5'UTR"))
        setattr(cls, "Epitope Tag",
            PermissibleValue(text="Epitope Tag"))
        setattr(cls, "Flanking Element",
            PermissibleValue(text="Flanking Element"))
        setattr(cls, "Leader Sequence",
            PermissibleValue(text="Leader Sequence"))
        setattr(cls, "Recognition Sequence",
            PermissibleValue(text="Recognition Sequence"))
        setattr(cls, "Signal Sequence",
            PermissibleValue(text="Signal Sequence"))
        setattr(cls, "Targeting Sequence",
            PermissibleValue(text="Targeting Sequence"))
        setattr(cls, "Transit Peptide",
            PermissibleValue(text="Transit Peptide"))
        setattr(cls, "Vector Sequence",
            PermissibleValue(text="Vector Sequence"))

class ContainerTypeEnum(EnumDefinitionImpl):

    screw_top_conical = PermissibleValue(text="screw_top_conical")

    _defn = EnumDefinition(
        name="ContainerTypeEnum",
    )

class CoreSectionEnum(EnumDefinitionImpl):
    """
    Sections of a core sample
    """
    TOP = PermissibleValue(
        text="TOP",
        description="Top section of core")
    BTM = PermissibleValue(
        text="BTM",
        description="Bottom section of core")
    MID = PermissibleValue(
        text="MID",
        description="Middle section of core")

    _defn = EnumDefinition(
        name="CoreSectionEnum",
        description="Sections of a core sample",
    )

class DeviceTypeEnum(EnumDefinitionImpl):

    orbital_shaker = PermissibleValue(text="orbital_shaker")
    thermomixer = PermissibleValue(text="thermomixer")

    _defn = EnumDefinition(
        name="DeviceTypeEnum",
    )

class DoiCategoryEnum(EnumDefinitionImpl):
    """
    The authority, or organization, the DOI is associated with
    """
    award_doi = PermissibleValue(
        text="award_doi",
        description="A type of DOI that resolves to a funding authority.")
    dataset_doi = PermissibleValue(
        text="dataset_doi",
        description="A type of DOI that resolves to generated data.")
    publication_doi = PermissibleValue(
        text="publication_doi",
        description="A type of DOI that resolves to a publication.")
    data_management_plan_doi = PermissibleValue(
        text="data_management_plan_doi",
        description="A type of DOI that resolves to a data management plan.")

    _defn = EnumDefinition(
        name="DoiCategoryEnum",
        description="The authority, or organization, the DOI is associated with",
    )

class DoiProviderEnum(EnumDefinitionImpl):
    """
    The authority, or organization, the DOI is associated with
    """
    emsl = PermissibleValue(
        text="emsl",
        title="EMSL",
        meaning=ROR["04rc0xn13"])
    jgi = PermissibleValue(
        text="jgi",
        title="JGI",
        meaning=ROR["04xm1d337"])
    kbase = PermissibleValue(
        text="kbase",
        title="KBase",
        meaning=ROR["01znn6x10"])
    osti = PermissibleValue(
        text="osti",
        title="OSTI",
        meaning=ROR["031478740"])
    ess_dive = PermissibleValue(
        text="ess_dive",
        title="ESS-DIVE",
        meaning=ROR["01t14bp54"])
    massive = PermissibleValue(
        text="massive",
        title="MassIVE")
    gsc = PermissibleValue(
        text="gsc",
        title="GSC")
    zenodo = PermissibleValue(
        text="zenodo",
        title="Zenodo")
    edi = PermissibleValue(
        text="edi",
        title="EDI",
        meaning=ROR["0330j0z60"])
    figshare = PermissibleValue(
        text="figshare",
        title="Figshare",
        meaning=ROR["041mxqs23"])

    _defn = EnumDefinition(
        name="DoiProviderEnum",
        description="The authority, or organization, the DOI is associated with",
    )

class DrainageClassEnum(EnumDefinitionImpl):
    """
    Soil drainage classifications
    """
    excessively_drained = PermissibleValue(
        text="excessively_drained",
        description="Excessively drained soil")
    moderately_well = PermissibleValue(
        text="moderately_well",
        description="Moderately well drained soil")
    poorly = PermissibleValue(
        text="poorly",
        description="Poorly drained soil")
    somewhat_poorly = PermissibleValue(
        text="somewhat_poorly",
        description="Somewhat poorly drained soil")
    very_poorly = PermissibleValue(
        text="very_poorly",
        description="Very poorly drained soil")
    well = PermissibleValue(
        text="well",
        description="Well drained soil")

    _defn = EnumDefinition(
        name="DrainageClassEnum",
        description="Soil drainage classifications",
    )

class EluentIntroductionEnum(EnumDefinitionImpl):
    """
    The method used to introduce the eluent into the mass spectrometer.
    """
    direct_infusion_syringe = PermissibleValue(
        text="direct_infusion_syringe",
        description="Direct infusion of the sample into the mass spectrometer")
    liquid_chromatography = PermissibleValue(
        text="liquid_chromatography",
        description="Introduction via liquid chromatography")
    gas_chromatography = PermissibleValue(
        text="gas_chromatography",
        description="Introduction via gas chromatography")
    direct_infusion_autosampler = PermissibleValue(
        text="direct_infusion_autosampler",
        description="Direct infusion using an autosampler")

    _defn = EnumDefinition(
        name="EluentIntroductionEnum",
        description="The method used to introduce the eluent into the mass spectrometer.",
    )

class ExecutionResourceEnum(EnumDefinitionImpl):
    """
    The computing resource or facility where the processing was executed.
    """
    nersc_cori = PermissibleValue(
        text="nersc_cori",
        description="NERSC Cori supercomputer")
    nersc_perlmutter = PermissibleValue(
        text="nersc_perlmutter",
        description="NERSC Perlmutter supercomputer")
    emsl_rzr = PermissibleValue(
        text="emsl_rzr",
        description="Environmental Molecular Sciences Laboratory RZR cluster")
    emsl_tahoma = PermissibleValue(
        text="emsl_tahoma",
        description="Environmental Molecular Sciences Laboratory Tahoma cluster")

    _defn = EnumDefinition(
        name="ExecutionResourceEnum",
        description="The computing resource or facility where the processing was executed.",
    )

class FAOClassEnum(EnumDefinitionImpl):
    """
    FAO soil classification system
    """
    Acrisols = PermissibleValue(text="Acrisols")
    Alisols = PermissibleValue(text="Alisols")
    Andosols = PermissibleValue(text="Andosols")
    Anthrosols = PermissibleValue(text="Anthrosols")
    Arenosols = PermissibleValue(text="Arenosols")
    Calcisols = PermissibleValue(text="Calcisols")
    Cambisols = PermissibleValue(text="Cambisols")
    Chernozems = PermissibleValue(text="Chernozems")
    Cryosols = PermissibleValue(text="Cryosols")
    Durisols = PermissibleValue(text="Durisols")
    Ferrasols = PermissibleValue(text="Ferrasols")
    Fluvisols = PermissibleValue(text="Fluvisols")
    Gleysols = PermissibleValue(text="Gleysols")
    Gypsisols = PermissibleValue(text="Gypsisols")
    Histosols = PermissibleValue(text="Histosols")
    Kastanozems = PermissibleValue(text="Kastanozems")
    Leptosols = PermissibleValue(text="Leptosols")
    Lixisols = PermissibleValue(text="Lixisols")
    Luvisols = PermissibleValue(text="Luvisols")
    Nitosols = PermissibleValue(text="Nitosols")
    Phaeozems = PermissibleValue(text="Phaeozems")
    Planosols = PermissibleValue(text="Planosols")
    Plinthosols = PermissibleValue(text="Plinthosols")
    Podzols = PermissibleValue(text="Podzols")
    Solonchaks = PermissibleValue(text="Solonchaks")
    Solonetz = PermissibleValue(text="Solonetz")
    Stagnosols = PermissibleValue(text="Stagnosols")
    Technosols = PermissibleValue(text="Technosols")
    Umbrisols = PermissibleValue(text="Umbrisols")
    Vertisols = PermissibleValue(text="Vertisols")

    _defn = EnumDefinition(
        name="FAOClassEnum",
        description="FAO soil classification system",
    )

class FileTypeEnum(EnumDefinitionImpl):

    FT_ICR_MS_Analysis_Results = PermissibleValue(text="FT_ICR_MS_Analysis_Results")
    GC_MS_Metabolomics_Results = PermissibleValue(text="GC_MS_Metabolomics_Results")
    Metaproteomics_Workflow_Statistics = PermissibleValue(text="Metaproteomics_Workflow_Statistics")
    Protein_Report = PermissibleValue(text="Protein_Report")
    Peptide_Report = PermissibleValue(text="Peptide_Report")
    Unfiltered_Metaproteomics_Results = PermissibleValue(text="Unfiltered_Metaproteomics_Results")
    Read_Count_and_RPKM = PermissibleValue(text="Read_Count_and_RPKM")
    QC_non_rRNA_R2 = PermissibleValue(text="QC_non_rRNA_R2")
    QC_non_rRNA_R1 = PermissibleValue(text="QC_non_rRNA_R1")
    Metagenome_Bins = PermissibleValue(text="Metagenome_Bins")
    CheckM_Statistics = PermissibleValue(text="CheckM_Statistics")
    GOTTCHA2_Krona_Plot = PermissibleValue(text="GOTTCHA2_Krona_Plot")
    Kraken2_Krona_Plot = PermissibleValue(text="Kraken2_Krona_Plot")
    Centrifuge_Krona_Plot = PermissibleValue(text="Centrifuge_Krona_Plot")
    Kraken2_Classification_Report = PermissibleValue(text="Kraken2_Classification_Report")
    Kraken2_Taxonomic_Classification = PermissibleValue(text="Kraken2_Taxonomic_Classification")
    Centrifuge_Classification_Report = PermissibleValue(text="Centrifuge_Classification_Report")
    Centrifuge_Taxonomic_Classification = PermissibleValue(text="Centrifuge_Taxonomic_Classification")
    Structural_Annotation_GFF = PermissibleValue(text="Structural_Annotation_GFF")
    Functional_Annotation_GFF = PermissibleValue(text="Functional_Annotation_GFF")
    Annotation_Amino_Acid_FASTA = PermissibleValue(text="Annotation_Amino_Acid_FASTA")
    Annotation_Enzyme_Commission = PermissibleValue(text="Annotation_Enzyme_Commission")
    Annotation_KEGG_Orthology = PermissibleValue(text="Annotation_KEGG_Orthology")
    Assembly_Coverage_BAM = PermissibleValue(text="Assembly_Coverage_BAM")
    Assembly_AGP = PermissibleValue(text="Assembly_AGP")
    Assembly_Scaffolds = PermissibleValue(text="Assembly_Scaffolds")
    Assembly_Contigs = PermissibleValue(text="Assembly_Contigs")
    Assembly_Coverage_Stats = PermissibleValue(text="Assembly_Coverage_Stats")
    Filtered_Sequencing_Reads = PermissibleValue(text="Filtered_Sequencing_Reads")
    QC_Statistics = PermissibleValue(text="QC_Statistics")
    TIGRFam_Annotation_GFF = PermissibleValue(text="TIGRFam_Annotation_GFF")
    Clusters_of_Orthologous_Groups_COG_Annotation_GFF = PermissibleValue(text="Clusters_of_Orthologous_Groups_COG_Annotation_GFF")
    CATH_FunFams_Functional_Families_Annotation_GFF = PermissibleValue(text="CATH_FunFams_Functional_Families_Annotation_GFF")
    SUPERFam_Annotation_GFF = PermissibleValue(text="SUPERFam_Annotation_GFF")
    SMART_Annotation_GFF = PermissibleValue(text="SMART_Annotation_GFF")
    Pfam_Annotation_GFF = PermissibleValue(text="Pfam_Annotation_GFF")
    Direct_Infusion_FT_ICR_MS_Raw_Data = PermissibleValue(text="Direct_Infusion_FT_ICR_MS_Raw_Data")

    _defn = EnumDefinition(
        name="FileTypeEnum",
    )

class FormulationEnum(EnumDefinitionImpl):
    """
    Method used to formulate media.
    """
    manual_mix = PermissibleValue(
        text="manual_mix",
        description="Manually mixed from individual components")
    commercial = PermissibleValue(
        text="commercial",
        description="Commercially prepared (see commercial_media_catalog)")
    premixed = PermissibleValue(
        text="premixed",
        description="Pre-mixed from a stock solution")

    _defn = EnumDefinition(
        name="FormulationEnum",
        description="Method used to formulate media.",
    )

class FragmentationEnum(EnumDefinitionImpl):
    """
    The fragmentation techniques used in mass spectrometry.
    """
    HCD = PermissibleValue(
        text="HCD",
        description="Higher-energy Collisional Dissociation")
    CID = PermissibleValue(
        text="CID",
        description="Collision-Induced Dissociation")
    ETD = PermissibleValue(
        text="ETD",
        description="Electron Transfer Dissociation")

    _defn = EnumDefinition(
        name="FragmentationEnum",
        description="The fragmentation techniques used in mass spectrometry.",
    )

class GenotypeSegmentEnum(EnumDefinitionImpl):

    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="GenotypeSegmentEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Empty Transformation Vector",
            PermissibleValue(text="Empty Transformation Vector"))
        setattr(cls, "Gene Knock-Out",
            PermissibleValue(text="Gene Knock-Out"))
        setattr(cls, "Gene Silencer",
            PermissibleValue(text="Gene Silencer"))
        setattr(cls, "Gene(s) of Interest",
            PermissibleValue(text="Gene(s) of Interest"))
        setattr(cls, "RNA Interface (RNAi)",
            PermissibleValue(text="RNA Interface (RNAi)"))
        setattr(cls, "Screenable Marker",
            PermissibleValue(text="Screenable Marker"))
        setattr(cls, "Selectable Marker",
            PermissibleValue(text="Selectable Marker"))
        setattr(cls, "Virus Genome",
            PermissibleValue(text="Virus Genome"))
        setattr(cls, "Wild Type",
            PermissibleValue(text="Wild Type"))
        setattr(cls, "Recombination Site",
            PermissibleValue(text="Recombination Site"))

class GrowthFacilityEnum(EnumDefinitionImpl):
    """
    Types of growth facilities
    """
    field = PermissibleValue(
        text="field",
        description="Field conditions")
    commercially_purchased = PermissibleValue(
        text="commercially_purchased",
        description="Commercially purchased")
    experimental_garden = PermissibleValue(
        text="experimental_garden",
        description="Experimental garden")
    field_incubation = PermissibleValue(
        text="field_incubation",
        description="Field incubation")
    greenhouse = PermissibleValue(
        text="greenhouse",
        description="Greenhouse")
    growth_chamber = PermissibleValue(
        text="growth_chamber",
        description="Growth chamber")
    lab_incubation = PermissibleValue(
        text="lab_incubation",
        description="Laboratory incubation")
    open_top_chamber = PermissibleValue(
        text="open_top_chamber",
        description="Open top chamber")
    other = PermissibleValue(
        text="other",
        description="Other growth facility type")

    _defn = EnumDefinition(
        name="GrowthFacilityEnum",
        description="Types of growth facilities",
    )

class GrowthHabitEnum(EnumDefinitionImpl):

    erect = PermissibleValue(text="erect")
    spreading = PermissibleValue(text="spreading")
    prostrate = PermissibleValue(text="prostrate")

    _defn = EnumDefinition(
        name="GrowthHabitEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "semi-erect",
            PermissibleValue(text="semi-erect"))

class InstitutionEnum(EnumDefinitionImpl):
    """
    The organization that processed the sample / ran the pipeline / participated in the project.
    """
    nmdc = PermissibleValue(
        text="nmdc",
        title="National Microbiome Data Collaborative")
    ucsd = PermissibleValue(
        text="ucsd",
        title="University of California, San Diego")
    jgi = PermissibleValue(
        text="jgi",
        title="Joint Genome Institute")
    emsl = PermissibleValue(
        text="emsl",
        title="Environmental Molecular Sciences Laboratory")
    battelle = PermissibleValue(
        text="battelle",
        title="Battelle Memorial Institute")
    anl = PermissibleValue(
        text="anl",
        title="Argonne National Laboratory")
    ucd_genome_center = PermissibleValue(
        text="ucd_genome_center",
        title="University of California, Davis Genome Center")
    azenta = PermissibleValue(
        text="azenta",
        title="Azenta Life Sciences")

    _defn = EnumDefinition(
        name="InstitutionEnum",
        description="The organization that processed the sample / ran the pipeline / participated in the project.",
    )

class InstrumentAltIdProviderEnum(EnumDefinitionImpl):

    nexus = PermissibleValue(text="nexus")
    dms = PermissibleValue(text="dms")

    _defn = EnumDefinition(
        name="InstrumentAltIdProviderEnum",
    )

class IntendedTraitEnum(EnumDefinitionImpl):

    other = PermissibleValue(
        text="other",
        title="Other")
    product_quality = PermissibleValue(
        text="product_quality",
        title="Product Quality")
    agronomic_properties = PermissibleValue(
        text="agronomic_properties",
        title="Agronomic Properties")
    bacterial_resistance = PermissibleValue(
        text="bacterial_resistance",
        title="Bacterial Resistance")
    herbicide_resistance = PermissibleValue(
        text="herbicide_resistance",
        title="Herbicide Resistance")
    insect_resistance = PermissibleValue(
        text="insect_resistance",
        title="Insect Resistance")
    marker_gene = PermissibleValue(
        text="marker_gene",
        title="Marker Gene")
    nematode_resistance = PermissibleValue(
        text="nematode_resistance",
        title="Nematode Resistance")
    virus_resistance = PermissibleValue(
        text="virus_resistance",
        title="Virus Resistance")

    _defn = EnumDefinition(
        name="IntendedTraitEnum",
    )

class IonizationSourceEnum(EnumDefinitionImpl):

    electrospray_ionization = PermissibleValue(text="electrospray_ionization")
    matrix_assisted_laser_desorption_ionization = PermissibleValue(text="matrix_assisted_laser_desorption_ionization")
    atmospheric_pressure_photo_ionization = PermissibleValue(text="atmospheric_pressure_photo_ionization")
    atmospheric_pressure_chemical_ionization = PermissibleValue(text="atmospheric_pressure_chemical_ionization")
    electron_ionization = PermissibleValue(text="electron_ionization")

    _defn = EnumDefinition(
        name="IonizationSourceEnum",
    )

class LandUseEnum(EnumDefinitionImpl):
    """
    Land use classifications
    """
    badlands = PermissibleValue(
        text="badlands",
        description="Badlands")
    cities = PermissibleValue(
        text="cities",
        description="Urban/city areas")
    conifers = PermissibleValue(
        text="conifers",
        description="Coniferous forests (e.g. pine, spruce, fir, cypress)")
    crop_trees = PermissibleValue(
        text="crop_trees",
        description="Crop trees (nuts, fruit, christmas trees, nursery trees)")
    farmstead = PermissibleValue(
        text="farmstead",
        description="Farmstead")
    gravel = PermissibleValue(
        text="gravel",
        description="Gravel areas")
    hardwoods = PermissibleValue(
        text="hardwoods",
        description="Hardwood forests (e.g. oak, hickory, elm, aspen)")
    hayland = PermissibleValue(
        text="hayland",
        description="Hayland")
    horticultural_plants = PermissibleValue(
        text="horticultural_plants",
        description="Horticultural plants (e.g. tulips)")
    industrial_areas = PermissibleValue(
        text="industrial_areas",
        description="Industrial areas")
    intermixed = PermissibleValue(
        text="intermixed",
        description="Intermixed hardwood and conifers")
    marshlands = PermissibleValue(
        text="marshlands",
        description="Marshlands (grass, sedges, rushes)")
    meadows = PermissibleValue(
        text="meadows",
        description="Meadows (grasses, alfalfa, fescue, bromegrass, timothy)")
    mines_quarries = PermissibleValue(
        text="mines_quarries",
        description="Mines and quarries")
    mudflats = PermissibleValue(
        text="mudflats",
        description="Mudflats")
    oil_waste = PermissibleValue(
        text="oil_waste",
        description="Oil waste areas")
    pastureland = PermissibleValue(
        text="pastureland",
        description="Pastureland (grasslands used for livestock grazing)")
    permanent_snow_or_ice = PermissibleValue(
        text="permanent_snow_or_ice",
        description="Permanent snow or ice")
    rainforest = PermissibleValue(
        text="rainforest",
        description="Rainforest (evergreen forest receiving >406 cm annual rainfall)")
    rangeland = PermissibleValue(
        text="rangeland",
        description="Rangeland")
    roads_railroads = PermissibleValue(
        text="roads_railroads",
        description="Roads and railroads")
    rock = PermissibleValue(
        text="rock",
        description="Rock surfaces")
    row_crops = PermissibleValue(
        text="row_crops",
        description="Row crops")
    saline_seeps = PermissibleValue(
        text="saline_seeps",
        description="Saline seeps")
    salt_flats = PermissibleValue(
        text="salt_flats",
        description="Salt flats")
    sand = PermissibleValue(
        text="sand",
        description="Sand areas")
    shrub_crops = PermissibleValue(
        text="shrub_crops",
        description="Shrub crops (blueberries, nursery ornamentals, filberts)")
    shrub_land = PermissibleValue(
        text="shrub_land",
        description="Shrub land (e.g. mesquite, sage-brush, creosote bush, shrub oak, eucalyptus)")
    small_grains = PermissibleValue(
        text="small_grains",
        description="Small grains")
    successional_shrub_land = PermissibleValue(
        text="successional_shrub_land",
        description="""Successional shrub land (tree saplings, hazels, sumacs, chokecherry, shrub dogwoods, blackberries)""")
    swamp = PermissibleValue(
        text="swamp",
        description="Swamp (permanent or semi-permanent water body dominated by woody plants)")
    tropical = PermissibleValue(
        text="tropical",
        description="Tropical vegetation (e.g. mangrove, palms)")
    tundra = PermissibleValue(
        text="tundra",
        description="Tundra (mosses, lichens)")
    vegetable_crops = PermissibleValue(
        text="vegetable_crops",
        description="Vegetable crops")
    vine_crops = PermissibleValue(
        text="vine_crops",
        description="Vine crops (grapes)")

    _defn = EnumDefinition(
        name="LandUseEnum",
        description="Land use classifications",
    )

class MassAnalyzerEnum(EnumDefinitionImpl):

    quadrupole = PermissibleValue(text="quadrupole")
    time_of_flight = PermissibleValue(text="time_of_flight")
    orbitrap = PermissibleValue(text="orbitrap")
    ion_trap = PermissibleValue(text="ion_trap")
    ion_cyclotron_resonance = PermissibleValue(text="ion_cyclotron_resonance")
    fourier_transform_ion_cyclotron_resonance = PermissibleValue(text="fourier_transform_ion_cyclotron_resonance")

    _defn = EnumDefinition(
        name="MassAnalyzerEnum",
    )

class MassSpecRawFileTypeEnum(EnumDefinitionImpl):

    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="MassSpecRawFileTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, ".d",
            PermissibleValue(text=".d"))
        setattr(cls, ".raw",
            PermissibleValue(text=".raw"))

class MassSpecResolutionEnum(EnumDefinitionImpl):

    high = PermissibleValue(
        text="high",
        description="higher than unit resolution")
    low = PermissibleValue(
        text="low",
        description="at unit resolution")

    _defn = EnumDefinition(
        name="MassSpecResolutionEnum",
    )

class MassSpectrometryAcquisitionStrategyEnum(EnumDefinitionImpl):

    data_independent_acquisition = PermissibleValue(
        text="data_independent_acquisition",
        description="""Data independent mass spectrometer acquisition method wherein the full mass range is fragmented. Examples of such an approach include MS^E, AIF, and bbCID.""")
    data_dependent_acquisition = PermissibleValue(
        text="data_dependent_acquisition",
        description="""Mass spectrometer data acquisition method wherein MSn spectra are triggered based on the m/z of precursor ions detected in the same run.""")
    full_scan_only = PermissibleValue(
        text="full_scan_only",
        description="Mass spectrometer data acquisition method wherein only MS1 data are acquired.")

    _defn = EnumDefinition(
        name="MassSpectrometryAcquisitionStrategyEnum",
    )

class MassSpectrumCollectionModeEnum(EnumDefinitionImpl):

    full_profile = PermissibleValue(text="full_profile")
    reduced_profile = PermissibleValue(text="reduced_profile")
    centroid = PermissibleValue(text="centroid")

    _defn = EnumDefinition(
        name="MassSpectrumCollectionModeEnum",
    )

class MediaTypeEnum(EnumDefinitionImpl):
    """
    Purpose/context of the media preparation.
    """
    strain_purity = PermissibleValue(
        text="strain_purity",
        description="Media used in strain purity checks")
    stock_culture = PermissibleValue(
        text="stock_culture",
        description="Media used in stock culture preparation")
    pre_culture = PermissibleValue(
        text="pre_culture",
        description="Media used in pre-culture growth")
    rich_media = PermissibleValue(
        text="rich_media",
        description="Rich media for experimental culture growth")
    minimal_media = PermissibleValue(
        text="minimal_media",
        description="Minimal/defined media for experimental culture growth")

    _defn = EnumDefinition(
        name="MediaTypeEnum",
        description="Purpose/context of the media preparation.",
    )

class MetagenomicsSteps(EnumDefinitionImpl):

    ReadQcAnalysis = PermissibleValue(text="ReadQcAnalysis")
    MetagenomeAssembly = PermissibleValue(text="MetagenomeAssembly")
    ReadBasedTaxonomyAnalysis = PermissibleValue(text="ReadBasedTaxonomyAnalysis")
    MetagenomeAnnotation = PermissibleValue(text="MetagenomeAnnotation")
    MagsAnalysis = PermissibleValue(text="MagsAnalysis")
    FunctionalAnnotation = PermissibleValue(text="FunctionalAnnotation")
    GenePhylogeny = PermissibleValue(text="GenePhylogeny")

    _defn = EnumDefinition(
        name="MetagenomicsSteps",
    )

class MetaproteomicsAnalysisCategoryEnum(EnumDefinitionImpl):
    """
    The category of metaproteomics analysis being performed.
    """
    matched_metagenome = PermissibleValue(
        text="matched_metagenome",
        description="A metaproteomics analysis matched to a metagenome from the same biosample.")
    in_silico_metagenome = PermissibleValue(
        text="in_silico_metagenome",
        description="A metaproteomics analysis matched to an in silico generated metagenome.")
    WITHDRAWN = PermissibleValue(text="WITHDRAWN")

    _defn = EnumDefinition(
        name="MetaproteomicsAnalysisCategoryEnum",
        description="The category of metaproteomics analysis being performed.",
    )

class MethodNameEnum(EnumDefinitionImpl):

    MAOM = PermissibleValue(text="MAOM")
    WOEM = PermissibleValue(text="WOEM")

    _defn = EnumDefinition(
        name="MethodNameEnum",
    )

class ModelEnum(EnumDefinitionImpl):

    exploris_21T = PermissibleValue(text="exploris_21T")
    exploris_240 = PermissibleValue(text="exploris_240")
    exploris_480 = PermissibleValue(text="exploris_480")
    ltq_orbitrap_velos = PermissibleValue(text="ltq_orbitrap_velos")
    orbitrap_fusion_lumos = PermissibleValue(text="orbitrap_fusion_lumos")
    orbitrap_eclipse_tribid = PermissibleValue(text="orbitrap_eclipse_tribid")
    orbitrap_q_exactive = PermissibleValue(text="orbitrap_q_exactive")
    orbitrap_iqx_tribrid = PermissibleValue(text="orbitrap_iqx_tribrid")
    orbitrap_exploris_120 = PermissibleValue(text="orbitrap_exploris_120")
    solarix_7T = PermissibleValue(text="solarix_7T")
    solarix_12T = PermissibleValue(text="solarix_12T")
    solarix_15T = PermissibleValue(text="solarix_15T")
    agilent_8890A = PermissibleValue(text="agilent_8890A")
    agilent_7980A = PermissibleValue(text="agilent_7980A")
    vortex_genie_2 = PermissibleValue(text="vortex_genie_2")
    novaseq = PermissibleValue(text="novaseq")
    novaseq_6000 = PermissibleValue(
        text="novaseq_6000",
        meaning=OBI["0002630"])
    novaseq_x = PermissibleValue(text="novaseq_x")
    hiseq = PermissibleValue(text="hiseq")
    hiseq_1000 = PermissibleValue(
        text="hiseq_1000",
        meaning=OBI["0002022"])
    hiseq_1500 = PermissibleValue(
        text="hiseq_1500",
        meaning=OBI["0003386"])
    hiseq_2000 = PermissibleValue(
        text="hiseq_2000",
        meaning=OBI["0002001"])
    hiseq_2500 = PermissibleValue(
        text="hiseq_2500",
        meaning=OBI["0002002"])
    hiseq_3000 = PermissibleValue(
        text="hiseq_3000",
        meaning=OBI["0002048"])
    hiseq_4000 = PermissibleValue(
        text="hiseq_4000",
        meaning=OBI["0002049"])
    hiseq_x_ten = PermissibleValue(
        text="hiseq_x_ten",
        meaning=OBI["0002129"])
    miniseq = PermissibleValue(
        text="miniseq",
        meaning=OBI["0003114"])
    miseq = PermissibleValue(
        text="miseq",
        meaning=OBI["0002003"])
    nextseq_1000 = PermissibleValue(
        text="nextseq_1000",
        meaning=OBI["0003606"])
    nextseq = PermissibleValue(text="nextseq")
    nextseq_500 = PermissibleValue(
        text="nextseq_500",
        meaning=OBI["0002021"])
    nextseq_550 = PermissibleValue(
        text="nextseq_550",
        meaning=OBI["0003387"])
    gridion = PermissibleValue(
        text="gridion",
        meaning=OBI["0002751"])
    minion = PermissibleValue(
        text="minion",
        meaning=OBI["0002750"])
    promethion = PermissibleValue(
        text="promethion",
        meaning=OBI["0002752"])
    rs_II = PermissibleValue(
        text="rs_II",
        meaning=OBI["0002012"])
    sequel = PermissibleValue(
        text="sequel",
        meaning=OBI["0002632"])
    sequel_II = PermissibleValue(
        text="sequel_II",
        meaning=OBI["0002633"])
    revio = PermissibleValue(text="revio")
    scimax = PermissibleValue(text="scimax")
    ed_400_with_rs_422 = PermissibleValue(text="ed_400_with_rs_422")
    mettler_toledo_30029066 = PermissibleValue(text="mettler_toledo_30029066")
    mettler_toledo_30266628 = PermissibleValue(text="mettler_toledo_30266628")
    ums_hyprop2_020210 = PermissibleValue(text="ums_hyprop2_020210")
    fialyzer_1000 = PermissibleValue(text="fialyzer_1000")
    fialyzer_1001 = PermissibleValue(text="fialyzer_1001")
    fialyzer_1002 = PermissibleValue(text="fialyzer_1002")
    orbitrap_q_exactive_plus = PermissibleValue(text="orbitrap_q_exactive_plus")
    toc_5000A = PermissibleValue(text="toc_5000A")
    toc_lcsh = PermissibleValue(text="toc_lcsh")
    sr_1 = PermissibleValue(text="sr_1")
    xth320 = PermissibleValue(text="xth320")

    _defn = EnumDefinition(
        name="ModelEnum",
    )

class ModificationMethodEnum(EnumDefinitionImpl):
    """
    Methods used to introduce genetic modifications into organisms.
    """
    electroporation = PermissibleValue(
        text="electroporation",
        description="Introduction of DNA via electrical pulses")
    conjugation = PermissibleValue(
        text="conjugation",
        description="Transfer of DNA via bacterial conjugation")
    transformation = PermissibleValue(
        text="transformation",
        description="Natural or chemical competence-based DNA uptake")
    transduction = PermissibleValue(
        text="transduction",
        description="Phage-mediated DNA transfer")
    crispr = PermissibleValue(
        text="crispr",
        description="CRISPR-based genome editing")
    homologous_recombination = PermissibleValue(
        text="homologous_recombination",
        description="Integration via homologous recombination")
    transposon = PermissibleValue(
        text="transposon",
        description="Transposon-mediated insertion")
    other = PermissibleValue(
        text="other",
        title="Other",
        description="Other modification method not listed")
    p_element = PermissibleValue(
        text="p_element",
        title="P-element")
    phage_transformation = PermissibleValue(
        text="phage_transformation",
        title="Phage Transformation")
    piggybac = PermissibleValue(
        text="piggybac",
        title="Piggybac")
    polyethylene_glycol_mediated = PermissibleValue(
        text="polyethylene_glycol_mediated",
        title="Polyethylene Glycol-mediated")
    replicon = PermissibleValue(
        text="replicon",
        title="Replicon")
    whisker_mediated_transformation = PermissibleValue(
        text="whisker_mediated_transformation",
        title="Whisker-mediated Transformation")

    _defn = EnumDefinition(
        name="ModificationMethodEnum",
        description="Methods used to introduce genetic modifications into organisms.",
    )

class MONetCoreGroupEnum(EnumDefinitionImpl):
    """
    Core groups when sampling according to the MONet sampling protocol
    """
    A = PermissibleValue(text="A")
    B = PermissibleValue(text="B")
    C1 = PermissibleValue(text="C1")
    C2 = PermissibleValue(text="C2")
    C3 = PermissibleValue(text="C3")
    C4 = PermissibleValue(text="C4")

    _defn = EnumDefinition(
        name="MONetCoreGroupEnum",
        description="Core groups when sampling according to the MONet sampling protocol",
    )

class NEONDomainEnum(EnumDefinitionImpl):
    """
    NEON ecological domains
    """
    northeast = PermissibleValue(
        text="northeast",
        title="Northeast domain")
    mid_atlantic = PermissibleValue(
        text="mid_atlantic",
        title="Mid-Atlantic domain")
    southeast = PermissibleValue(
        text="southeast",
        title="Southeast domain")
    atlantic_neotropical = PermissibleValue(
        text="atlantic_neotropical",
        title="Atlantic Neotropical domain")
    great_lakes = PermissibleValue(
        text="great_lakes",
        title="Great Lakes domain")
    prairie_peninsula = PermissibleValue(
        text="prairie_peninsula",
        title="Prairie Peninsula domain")
    appalachians_and_cumberland_plateau = PermissibleValue(
        text="appalachians_and_cumberland_plateau",
        title="Appalachians and Cumberland Plateau domain")
    ozarks_complex = PermissibleValue(
        text="ozarks_complex",
        title="Ozarks Complex domain")
    northern_plains = PermissibleValue(
        text="northern_plains",
        title="Northern Plains domain")
    central_plains = PermissibleValue(
        text="central_plains",
        title="Central Plains domain")
    southern_plains = PermissibleValue(
        text="southern_plains",
        title="Southern Plains domain")
    desert_southwest = PermissibleValue(
        text="desert_southwest",
        title="Desert Southwest domain")
    northern_rockies = PermissibleValue(
        text="northern_rockies",
        title="Northern Rockies domain")
    southern_rockies_and_colorado_plateau = PermissibleValue(
        text="southern_rockies_and_colorado_plateau",
        title="Southern Rockies and Colorado Plateau domain")
    great_basin = PermissibleValue(
        text="great_basin",
        title="Great Basin domain")
    sierra_nevada = PermissibleValue(
        text="sierra_nevada",
        title="Sierra Nevada domain")
    pacific_northwest = PermissibleValue(
        text="pacific_northwest",
        title="Pacific Northwest domain")
    pacific_southwest = PermissibleValue(
        text="pacific_southwest",
        title="Pacific Southwest domain")
    tundra = PermissibleValue(
        text="tundra",
        title="Tundra domain")
    taiga = PermissibleValue(
        text="taiga",
        title="Taiga domain")
    pacific_tropical = PermissibleValue(
        text="pacific_tropical",
        title="Pacific Tropical domain")

    _defn = EnumDefinition(
        name="NEONDomainEnum",
        description="NEON ecological domains",
    )

class NexusRoleEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="NexusRoleEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Principal Investigator",
            PermissibleValue(text="Principal Investigator"))
        setattr(cls, "Co-Investigator",
            PermissibleValue(text="Co-Investigator"))
        setattr(cls, "Team Member",
            PermissibleValue(text="Team Member"))
        setattr(cls, "Integrated Research Platform Lead",
            PermissibleValue(text="Integrated Research Platform Lead"))
        setattr(cls, "Administrative Coordinator",
            PermissibleValue(text="Administrative Coordinator"))
        setattr(cls, "Project Manager",
            PermissibleValue(text="Project Manager"))
        setattr(cls, "Metadata POC",
            PermissibleValue(text="Metadata POC"))
        setattr(cls, "Science Lead",
            PermissibleValue(text="Science Lead"))
        setattr(cls, "Science POC",
            PermissibleValue(text="Science POC"))

class NucleotideSequencingEnum(EnumDefinitionImpl):

    metagenome = PermissibleValue(
        text="metagenome",
        title="Metagenome")
    metatranscriptome = PermissibleValue(
        text="metatranscriptome",
        title="Metatranscriptome")
    amplicon_sequencing_assay = PermissibleValue(
        text="amplicon_sequencing_assay",
        title="Amplicon",
        meaning=OBI["0002767"])

    _defn = EnumDefinition(
        name="NucleotideSequencingEnum",
    )

class OxygenStatusEnum(EnumDefinitionImpl):
    """
    Oxygen status of samples
    """
    aerobic = PermissibleValue(
        text="aerobic",
        description="Aerobic conditions")
    anaerobic = PermissibleValue(
        text="anaerobic",
        description="Anaerobic conditions")
    anoxic = PermissibleValue(
        text="anoxic",
        description="Anoxic conditions")
    facultative = PermissibleValue(
        text="facultative",
        description="Facultative conditions")
    microaerophilic = PermissibleValue(
        text="microaerophilic",
        description="Microaerophilic conditions")
    microanaerobe = PermissibleValue(
        text="microanaerobe",
        description="Microanaerobe conditions")
    obligate_aerobe = PermissibleValue(
        text="obligate_aerobe",
        description="Obligate aerobe conditions")
    obligate_anaerobe = PermissibleValue(
        text="obligate_anaerobe",
        description="Obligate anaerobe conditions")

    _defn = EnumDefinition(
        name="OxygenStatusEnum",
        description="Oxygen status of samples",
    )

class PassFailEnum(EnumDefinitionImpl):
    """
    Result/status for a process (e.g., QC outcome).
    """
    fail = PermissibleValue(text="fail")

    _defn = EnumDefinition(
        name="PassFailEnum",
        description="Result/status for a process (e.g., QC outcome).",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "pass",
            PermissibleValue(text="pass"))

class PhotochemicalExposureEnum(EnumDefinitionImpl):

    ultraviolet = PermissibleValue(text="ultraviolet")
    infrared = PermissibleValue(text="infrared")

    _defn = EnumDefinition(
        name="PhotochemicalExposureEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "visible light",
            PermissibleValue(text="visible light"))

class PlantSexEnum(EnumDefinitionImpl):

    androdioecious = PermissibleValue(text="androdioecious")
    androecious = PermissibleValue(text="androecious")
    androgynomonoecious = PermissibleValue(text="androgynomonoecious")
    androgynous = PermissibleValue(text="androgynous")
    andromonoecious = PermissibleValue(text="andromonoecious")
    bisexual = PermissibleValue(text="bisexual")
    dichogamous = PermissibleValue(text="dichogamous")
    diclinous = PermissibleValue(text="diclinous")
    dioecious = PermissibleValue(text="dioecious")
    gynodioecious = PermissibleValue(text="gynodioecious")
    gynoecious = PermissibleValue(text="gynoecious")
    gynomonoecious = PermissibleValue(text="gynomonoecious")
    hermaphroditic = PermissibleValue(text="hermaphroditic")
    imperfect = PermissibleValue(text="imperfect")
    monoclinous = PermissibleValue(text="monoclinous")
    monoecious = PermissibleValue(text="monoecious")
    perfect = PermissibleValue(text="perfect")
    polygamodioecious = PermissibleValue(text="polygamodioecious")
    polygamomonoecious = PermissibleValue(text="polygamomonoecious")
    polygamous = PermissibleValue(text="polygamous")
    protandrous = PermissibleValue(text="protandrous")
    protogynous = PermissibleValue(text="protogynous")
    subandroecious = PermissibleValue(text="subandroecious")
    subdioecious = PermissibleValue(text="subdioecious")
    subgynoecious = PermissibleValue(text="subgynoecious")
    synoecious = PermissibleValue(text="synoecious")
    trimonoecious = PermissibleValue(text="trimonoecious")
    trioecious = PermissibleValue(text="trioecious")
    unisexual = PermissibleValue(text="unisexual")

    _defn = EnumDefinition(
        name="PlantSexEnum",
    )

class PlantStructureEnum(EnumDefinitionImpl):

    stem = PermissibleValue(
        text="stem",
        title="stem [PO:0009047]",
        meaning=PO["0009047"])
    leaf = PermissibleValue(
        text="leaf",
        title="leaf [PO:0025034]",
        meaning=PO["0025034"])
    root = PermissibleValue(
        text="root",
        title="root [PO:0009005]",
        meaning=PO["0009005"])
    fine_root = PermissibleValue(
        text="fine_root",
        title="fine root [BTO:0005194]",
        meaning=BTO["0005194"])
    whole_plant = PermissibleValue(
        text="whole_plant",
        title="whole plant [BTO:0001461]",
        meaning=BTO["0001461"])
    stamen = PermissibleValue(
        text="stamen",
        title="stamen [PO:0009029]",
        meaning=PO["0009029"])
    carpel = PermissibleValue(
        text="carpel",
        title="carpel [PO:0009030]",
        meaning=PO["0009030"])
    seed = PermissibleValue(
        text="seed",
        title="seed [PO:0009010]",
        meaning=PO["0009010"])
    rhizodeposits = PermissibleValue(text="rhizodeposits")

    _defn = EnumDefinition(
        name="PlantStructureEnum",
    )

class PolarityEnum(EnumDefinitionImpl):
    """
    The polarity mode used in the mass spectrometry analysis.
    """
    positive = PermissibleValue(text="positive")
    negative = PermissibleValue(text="negative")

    _defn = EnumDefinition(
        name="PolarityEnum",
        description="The polarity mode used in the mass spectrometry analysis.",
    )

class ProcessedDataFlag(EnumDefinitionImpl):

    Below_Detection = PermissibleValue(text="Below_Detection")
    Below_Reporting_Limit = PermissibleValue(text="Below_Reporting_Limit")
    High_Background = PermissibleValue(text="High_Background")
    Out_of_Range = PermissibleValue(text="Out_of_Range")
    Outlier = PermissibleValue(text="Outlier")
    Data_not_available = PermissibleValue(text="Data_not_available")
    Failed_QC = PermissibleValue(text="Failed_QC")
    Insufficient_Material = PermissibleValue(text="Insufficient_Material")

    _defn = EnumDefinition(
        name="ProcessedDataFlag",
    )

class ProductMeasureType(EnumDefinitionImpl):

    Single = PermissibleValue(text="Single")
    Replicate = PermissibleValue(text="Replicate")
    Average = PermissibleValue(text="Average")

    _defn = EnumDefinition(
        name="ProductMeasureType",
    )

class ProfilePositionEnum(EnumDefinitionImpl):
    """
    Soil profile positions
    """
    backslope = PermissibleValue(
        text="backslope",
        description="Backslope position")
    footslope = PermissibleValue(
        text="footslope",
        description="Footslope position")
    shoulder = PermissibleValue(
        text="shoulder",
        description="Shoulder position")
    summit = PermissibleValue(
        text="summit",
        description="Summit position")
    toeslope = PermissibleValue(
        text="toeslope",
        description="Toeslope position")

    _defn = EnumDefinition(
        name="ProfilePositionEnum",
        description="Soil profile positions",
    )

class ProjectStatusEnum(EnumDefinitionImpl):

    STARTED = PermissibleValue(text="STARTED")
    COMPLETED = PermissibleValue(text="COMPLETED")
    CLOSED = PermissibleValue(text="CLOSED")
    EXTENDED = PermissibleValue(text="EXTENDED")
    ACCEPTED = PermissibleValue(text="ACCEPTED")
    WITHDRAWN = PermissibleValue(text="WITHDRAWN")

    _defn = EnumDefinition(
        name="ProjectStatusEnum",
    )

class RouteMethodEnum(EnumDefinitionImpl):

    analysis_activity = PermissibleValue(text="analysis_activity")
    lcms_metabolomics_method = PermissibleValue(text="lcms_metabolomics_method")
    fticr_acquisition_method = PermissibleValue(text="fticr_acquisition_method")
    gravimetric_water_content_method = PermissibleValue(text="gravimetric_water_content_method")
    ph_method = PermissibleValue(text="ph_method")
    hydraulic_properties_method = PermissibleValue(text="hydraulic_properties_method")
    microbial_biomass_method = PermissibleValue(text="microbial_biomass_method")
    xray_computed_tomography_method = PermissibleValue(text="xray_computed_tomography_method")
    REGEN = PermissibleValue(text="REGEN")
    KUO = PermissibleValue(text="KUO")
    respiration_method = PermissibleValue(text="respiration_method")
    texture_method = PermissibleValue(text="texture_method")
    enzyme_activity_method = PermissibleValue(text="enzyme_activity_method")
    elemental_analysis_method = PermissibleValue(text="elemental_analysis_method")
    toc_tn_method = PermissibleValue(text="toc_tn_method")
    bulk_density_method = PermissibleValue(text="bulk_density_method")
    metagenomics_method = PermissibleValue(text="metagenomics_method")
    xrf_analysis = PermissibleValue(text="xrf_analysis")
    xrd_analysis = PermissibleValue(text="xrd_analysis")

    _defn = EnumDefinition(
        name="RouteMethodEnum",
    )

class SampleBaseType(EnumDefinitionImpl):
    """
    Base types for sample entities
    """
    sample = PermissibleValue(
        text="sample",
        description="A physical sample")
    processed_sample = PermissibleValue(
        text="processed_sample",
        description="A sample that has undergone processing")

    _defn = EnumDefinition(
        name="SampleBaseType",
        description="Base types for sample entities",
    )

class SamplePortionEnum(EnumDefinitionImpl):

    supernatant = PermissibleValue(text="supernatant")
    pellet = PermissibleValue(text="pellet")
    organic_layer = PermissibleValue(
        text="organic_layer",
        title="Organic layer",
        description="The portion of a mixture containing dissolved organic material")
    aqueous_layer = PermissibleValue(
        text="aqueous_layer",
        title="Aqueous layer",
        description="The portion of a mixture containing molecules dissolved in water")
    interlayer = PermissibleValue(
        text="interlayer",
        title="Interlayer",
        description="The layer of material between liquid layers of a separated mixture")
    chloroform_layer = PermissibleValue(
        text="chloroform_layer",
        title="Chloroform layer",
        description="The portion of a mixture containing molecules dissolved in chloroform")
    methanol_layer = PermissibleValue(
        text="methanol_layer",
        title="Methanol layer",
        description="The portion of a mixture containing molecules dissolved in methanol")

    _defn = EnumDefinition(
        name="SamplePortionEnum",
    )

class SampleRole(EnumDefinitionImpl):

    input_sample = PermissibleValue(text="input_sample")
    output_sample = PermissibleValue(text="output_sample")

    _defn = EnumDefinition(
        name="SampleRole",
    )

class SampleStoreTempEnum(EnumDefinitionImpl):
    """
    Sample storage temperature conditions
    """
    fresh4 = PermissibleValue(
        text="fresh4",
        description="Fresh storage at 4°C")
    freshroom = PermissibleValue(
        text="freshroom",
        description="Fresh storage at room temperature")
    frozen20 = PermissibleValue(
        text="frozen20",
        description="Frozen storage at -20°C")
    frozen80 = PermissibleValue(
        text="frozen80",
        description="Frozen storage at -80°C")
    other = PermissibleValue(
        text="other",
        description="Other storage temperature")

    _defn = EnumDefinition(
        name="SampleStoreTempEnum",
        description="Sample storage temperature conditions",
    )

class SampleType(EnumDefinitionImpl):
    """
    Types of samples that can be collected
    """
    soil_sample = PermissibleValue(
        text="soil_sample",
        description="Soil sample")
    aerosol_sample = PermissibleValue(
        text="aerosol_sample",
        description="Aerosol sample")

    _defn = EnumDefinition(
        name="SampleType",
        description="Types of samples that can be collected",
    )

class SamplingActivityTypeEnum(EnumDefinitionImpl):
    """
    Types of sampling activities
    """
    soil = PermissibleValue(
        text="soil",
        description="Soil sampling activity")
    water = PermissibleValue(
        text="water",
        description="Water sampling activity")
    air = PermissibleValue(
        text="air",
        description="Air sampling activity")
    plant = PermissibleValue(
        text="plant",
        description="Plant sampling activity")
    none = PermissibleValue(
        text="none",
        description="No specific activity type")

    _defn = EnumDefinition(
        name="SamplingActivityTypeEnum",
        description="Types of sampling activities",
    )

class SedimentTypeEnum(EnumDefinitionImpl):
    """
    Types of sediment
    """
    biogenous = PermissibleValue(
        text="biogenous",
        description="Biogenous sediment")
    cosmogenous = PermissibleValue(
        text="cosmogenous",
        description="Cosmogenous sediment")
    hydrogenous = PermissibleValue(
        text="hydrogenous",
        description="Hydrogenous sediment")
    lithogenous = PermissibleValue(
        text="lithogenous",
        description="Lithogenous sediment")

    _defn = EnumDefinition(
        name="SedimentTypeEnum",
        description="Types of sediment",
    )

class SitePhotoCategoryEnum(EnumDefinitionImpl):

    landscape = PermissibleValue(text="landscape")
    measure = PermissibleValue(text="measure")

    _defn = EnumDefinition(
        name="SitePhotoCategoryEnum",
    )

class SoilHorizonEnum(EnumDefinitionImpl):
    """
    Soil horizon classifications
    """
    a_horizon = PermissibleValue(
        text="a_horizon",
        description="""The surface horizon, also called topsoil. It has a defined soil structure, and is mostly made up of humus (decayed organic matter).""")
    b_horizon = PermissibleValue(
        text="b_horizon",
        description="""Also known as the subsoil. It is greatly composed of material illuviated (washed in from) layers above it. It is typically denser than the A horizon and has a clayey texture.""")
    c_horizon = PermissibleValue(
        text="c_horizon",
        description="""Also known as the substratum is unconsolidated material deepest in the pit and closest to the bedrock.""")
    e_horizon = PermissibleValue(
        text="e_horizon",
        description="""Used to refer to subsurface horizons that have undergone a significant loss of minerals, also known as Eluviation (or leaching).""")
    o_horizon = PermissibleValue(
        text="o_horizon",
        description="""The organic horizon. Typically at the top of the soil structure and is made up of mostly organic matter.""")
    permafrost = PermissibleValue(
        text="permafrost",
        description="Soil that continuously remains below 0 °C (32 °F) for two years or more.")
    r_layer = PermissibleValue(
        text="r_layer",
        description="""Hard bedrock, which is usually the lowest layer. It is characterized by tightly bound and unbreakable materials.""")
    m_horizon = PermissibleValue(
        text="m_horizon",
        description="Mineral horizon")

    _defn = EnumDefinition(
        name="SoilHorizonEnum",
        description="Soil horizon classifications",
    )

class SoilSampleTypeEnum(EnumDefinitionImpl):
    """
    Specific types of soil samples
    """
    soil_core = PermissibleValue(
        text="soil_core",
        title="soil core",
        description="Soil core sample")
    surface_layer = PermissibleValue(
        text="surface_layer",
        title="surface layer",
        description="Surface layer soil sample")

    _defn = EnumDefinition(
        name="SoilSampleTypeEnum",
        description="Specific types of soil samples",
    )

class SoilTypeEnum(EnumDefinitionImpl):
    """
    USDA soil taxonomy classifications
    """
    alfisol = PermissibleValue(
        text="alfisol",
        title="Alfisol")
    andisol = PermissibleValue(
        text="andisol",
        title="Andisol")
    aridisol = PermissibleValue(
        text="aridisol",
        title="Aridisol")
    entisol = PermissibleValue(
        text="entisol",
        title="Entisol")
    gelisol = PermissibleValue(
        text="gelisol",
        title="Gelisol")
    histosol = PermissibleValue(
        text="histosol",
        title="Histosol")
    inceptisol = PermissibleValue(
        text="inceptisol",
        title="Inceptisol")
    mollisol = PermissibleValue(
        text="mollisol",
        title="Mollisol")
    oxisol = PermissibleValue(
        text="oxisol",
        title="Oxisol")
    spodosol = PermissibleValue(
        text="spodosol",
        title="Spodosol")
    ultisol = PermissibleValue(
        text="ultisol",
        title="Ultisol")
    vertisol = PermissibleValue(
        text="vertisol",
        title="Vertisol")

    _defn = EnumDefinition(
        name="SoilTypeEnum",
        description="USDA soil taxonomy classifications",
    )

class StationaryPhaseEnum(EnumDefinitionImpl):
    """
    The stationary phase used in chromatography.
    """
    C18 = PermissibleValue(
        text="C18",
        description="A stationary phase consisting of octadecyl chains (C18) bonded to silica particles.")
    C8 = PermissibleValue(
        text="C8",
        description="A stationary phase consisting of octyl chains (C8) bonded to silica particles.")
    C4 = PermissibleValue(
        text="C4",
        description="A stationary phase consisting of butyl chains (C4) bonded to silica particles.")
    C2 = PermissibleValue(
        text="C2",
        description="A stationary phase consisting of ethyl chains (C2) bonded to silica particles.")
    C1 = PermissibleValue(
        text="C1",
        description="A stationary phase consisting of methyl chains (C1) bonded to silica particles.")
    C30 = PermissibleValue(
        text="C30",
        description="A stationary phase consisting of triacontyl chains (C30) bonded to silica particles.")
    C60 = PermissibleValue(
        text="C60",
        description="A stationary phase consisting of hexatriacontyl chains (C60) bonded to silica particles.")
    CNT = PermissibleValue(
        text="CNT",
        description="Carbon Nanotube stationary phase.")
    CN = PermissibleValue(
        text="CN",
        description="Cyano (CN) bonded stationary phase.")
    Diol = PermissibleValue(
        text="Diol",
        description="A stationary phase with diol (1,2-diol) functional groups.")
    HILIC = PermissibleValue(
        text="HILIC",
        description="Hydrophilic Interaction Chromatography (HILIC) stationary phase.")
    HLB = PermissibleValue(
        text="HLB",
        description="Hydrophilic-Lipophilic-Balance (HLB) stationary phase.")
    NH2 = PermissibleValue(
        text="NH2",
        description="Amino (NH2) bonded stationary phase.")
    Phenyl = PermissibleValue(
        text="Phenyl",
        description="Phenyl bonded stationary phase.")
    Polysiloxane = PermissibleValue(
        text="Polysiloxane",
        description="A stationary phase made of polysiloxane, usually used in gas chromatography.")
    SAX = PermissibleValue(
        text="SAX",
        description="Strong Anion Exchange (SAX) stationary phase.")
    SCX = PermissibleValue(
        text="SCX",
        description="Strong Cation Exchange (SCX) stationary phase.")
    Silica = PermissibleValue(
        text="Silica",
        description="A stationary phase made of silica, commonly used in chromatography.")
    WCX = PermissibleValue(
        text="WCX",
        description="Weak Cation Exchange (WCX) stationary phase.")
    WAX = PermissibleValue(
        text="WAX",
        description="Weak Anion Exchange (WAX) stationary phase.")

    _defn = EnumDefinition(
        name="StationaryPhaseEnum",
        description="The stationary phase used in chromatography.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "BEH-HILIC",
            PermissibleValue(
                text="BEH-HILIC",
                description="""Hydrophilic Interaction Chromatography (HILIC) employing BEH (Bridged Ethylene Hybrid) particles as the stationary phase."""))
        setattr(cls, "PS-DVB",
            PermissibleValue(
                text="PS-DVB",
                description="""Polystyrene-divinylbenzene stationary phase, often used in solid-phase extraction, including proprietary Priority PolLutant (PPL)."""))
        setattr(cls, "ZIC-HILIC",
            PermissibleValue(
                text="ZIC-HILIC",
                description="Zwitterionic Hydrophilic Interaction Chromatography (ZIC-HILIC) stationary phase."))
        setattr(cls, "ZIC-pHILIC",
            PermissibleValue(
                text="ZIC-pHILIC",
                description="""Zwitterionic pH-Responsive Hydrophilic Interaction Chromatography (ZIC-pHILIC) stationary phase."""))
        setattr(cls, "ZIC-cHILIC",
            PermissibleValue(
                text="ZIC-cHILIC",
                description="""Zwitterionic Charged Hydrophilic Interaction Chromatography (ZIC-cHILIC) stationary phase."""))

class SterilizationMethodEnum(EnumDefinitionImpl):
    """
    Method used to sterilize media or other entities.
    """
    autoclave = PermissibleValue(
        text="autoclave",
        description="Autoclaved")
    filter = PermissibleValue(
        text="filter",
        description="Filter-sterilised (typically 0.22 μm)")
    uv = PermissibleValue(
        text="uv",
        description="UV-sterilised")
    none = PermissibleValue(
        text="none",
        description="Not sterilised (used as-is)")

    _defn = EnumDefinition(
        name="SterilizationMethodEnum",
        description="Method used to sterilize media or other entities.",
    )

class StorageConditionEnum(EnumDefinitionImpl):
    """
    Sample storage conditions
    """
    fresh = PermissibleValue(
        text="fresh",
        description="Fresh sample")
    frozen = PermissibleValue(
        text="frozen",
        description="Frozen sample")
    lyophilized = PermissibleValue(
        text="lyophilized",
        description="Lyophilized (freeze-dried) sample")
    other = PermissibleValue(
        text="other",
        description="Other storage condition")

    _defn = EnumDefinition(
        name="StorageConditionEnum",
        description="Sample storage conditions",
    )

class StrainTypeEnum(EnumDefinitionImpl):
    """
    Types of microbial strains/organisms.
    """
    bacterial = PermissibleValue(
        text="bacterial",
        description="Bacterial strain")
    fungal = PermissibleValue(
        text="fungal",
        description="Fungal strain")
    archaeal = PermissibleValue(
        text="archaeal",
        description="Archaeal strain")
    viral = PermissibleValue(
        text="viral",
        description="Viral isolate")
    algal = PermissibleValue(
        text="algal",
        description="Algal strain")
    protist = PermissibleValue(
        text="protist",
        description="Protist strain")
    other = PermissibleValue(
        text="other",
        description="Other organism type")

    _defn = EnumDefinition(
        name="StrainTypeEnum",
        description="Types of microbial strains/organisms.",
    )

class SyntheticEnvironmentEnum(EnumDefinitionImpl):

    pore_scale_micromodels = PermissibleValue(
        text="pore_scale_micromodels",
        title="Pore-scale micromodels")
    rhizochip = PermissibleValue(
        text="rhizochip",
        title="RhizoChip")
    subtap = PermissibleValue(
        text="subtap",
        title="SubTap microbial and rhizosphere platforms")
    three_d_bioprinted_synthetic_soil_aggregates = PermissibleValue(
        text="three_d_bioprinted_synthetic_soil_aggregates",
        title="3-D Bioprinted Synthetic Soil Aggregates")
    pore2chip = PermissibleValue(
        text="pore2chip",
        title="Pore2Chip")

    _defn = EnumDefinition(
        name="SyntheticEnvironmentEnum",
    )

class TidalStageEnum(EnumDefinitionImpl):

    low_tide = PermissibleValue(text="low_tide")
    high_tide = PermissibleValue(text="high_tide")
    ebb_tide = PermissibleValue(text="ebb_tide")
    flood_tide = PermissibleValue(text="flood_tide")

    _defn = EnumDefinition(
        name="TidalStageEnum",
    )

class TillageEnum(EnumDefinitionImpl):
    """
    Tillage methods
    """
    chisel = PermissibleValue(
        text="chisel",
        description="Chisel tillage")
    cutting_disc = PermissibleValue(
        text="cutting_disc",
        description="Cutting disc tillage")
    disc_plough = PermissibleValue(
        text="disc_plough",
        description="Disc plough tillage")
    drill = PermissibleValue(
        text="drill",
        description="Drill tillage")
    mouldboard = PermissibleValue(
        text="mouldboard",
        description="Mouldboard tillage")
    ridge_till = PermissibleValue(
        text="ridge_till",
        description="Ridge till")
    strip_tillage = PermissibleValue(
        text="strip_tillage",
        description="Strip tillage")
    tined = PermissibleValue(
        text="tined",
        description="Tined tillage")
    zonal_tillage = PermissibleValue(
        text="zonal_tillage",
        description="Zonal tillage")

    _defn = EnumDefinition(
        name="TillageEnum",
        description="Tillage methods",
    )

class TrophicLevelEnum(EnumDefinitionImpl):
    """
    Enumeration of trophic levels for organisms.
    """
    autotroph = PermissibleValue(
        text="autotroph",
        description="Organism that produces complex organic compounds from simple substances")
    carboxydotroph = PermissibleValue(
        text="carboxydotroph",
        description="Organism that oxidizes carbon monoxide as energy source")
    chemoautolithotroph = PermissibleValue(
        text="chemoautolithotroph",
        description="Chemolithoautotroph using inorganic compounds")
    chemoautotroph = PermissibleValue(
        text="chemoautotroph",
        description="Organism using chemical energy to synthesize organic compounds")
    chemoheterotroph = PermissibleValue(
        text="chemoheterotroph",
        description="Organism obtaining energy by oxidizing organic compounds")
    chemolithoautotroph = PermissibleValue(
        text="chemolithoautotroph",
        description="Organism using inorganic electron donors")
    chemolithotroph = PermissibleValue(
        text="chemolithotroph",
        description="Organism deriving energy from inorganic compounds")
    chemoorganoheterotroph = PermissibleValue(
        text="chemoorganoheterotroph",
        description="Organism using organic compounds as electron donors")
    chemoorganotroph = PermissibleValue(
        text="chemoorganotroph",
        description="Organism obtaining energy from organic compounds")
    chemosynthetic = PermissibleValue(
        text="chemosynthetic",
        description="Organism using chemosynthesis")
    chemotroph = PermissibleValue(
        text="chemotroph",
        description="Organism obtaining energy from chemical reactions")
    copiotroph = PermissibleValue(
        text="copiotroph",
        description="Organism thriving in nutrient-rich environments")
    diazotroph = PermissibleValue(
        text="diazotroph",
        description="Organism capable of nitrogen fixation")
    facultative = PermissibleValue(
        text="facultative",
        description="Organism capable of multiple metabolic modes")
    heterotroph = PermissibleValue(
        text="heterotroph",
        description="Organism requiring organic compounds for nutrition")
    lithoautotroph = PermissibleValue(
        text="lithoautotroph",
        description="Organism using inorganic substrates")
    lithoheterotroph = PermissibleValue(
        text="lithoheterotroph",
        description="Organism using inorganic electron donors with organic carbon")
    lithotroph = PermissibleValue(
        text="lithotroph",
        description="Organism using inorganic electron donors")
    methanotroph = PermissibleValue(
        text="methanotroph",
        description="Organism using methane as carbon/energy source")
    methylotroph = PermissibleValue(
        text="methylotroph",
        description="Organism using reduced one-carbon compounds")
    mixotroph = PermissibleValue(
        text="mixotroph",
        description="Organism combining autotrophy and heterotrophy")
    obligate = PermissibleValue(
        text="obligate",
        description="Organism restricted to one metabolic mode")
    oligotroph = PermissibleValue(
        text="oligotroph",
        description="Organism thriving in nutrient-poor environments")
    organoheterotroph = PermissibleValue(
        text="organoheterotroph",
        description="Organism using organic compounds")
    organotroph = PermissibleValue(
        text="organotroph",
        description="Organism obtaining electrons from organic compounds")
    osmotroph = PermissibleValue(
        text="osmotroph",
        description="Organism absorbing dissolved nutrients")
    photoheterotroph = PermissibleValue(
        text="photoheterotroph",
        description="Organism using light with organic carbon")
    photoautotroph = PermissibleValue(
        text="photoautotroph",
        description="Organism using light to fix carbon dioxide")
    photolithoautotroph = PermissibleValue(
        text="photolithoautotroph",
        description="Photosynthetic organism using inorganic electron donors")
    photolithotroph = PermissibleValue(
        text="photolithotroph",
        description="Organism using light and inorganic electron donors")
    phototroph = PermissibleValue(
        text="phototroph",
        description="Organism using light as energy source")

    _defn = EnumDefinition(
        name="TrophicLevelEnum",
        description="Enumeration of trophic levels for organisms.",
    )

class VendorEnum(EnumDefinitionImpl):

    waters = PermissibleValue(text="waters")
    agilent = PermissibleValue(text="agilent")
    bruker = PermissibleValue(text="bruker")
    thermo_fisher = PermissibleValue(text="thermo_fisher")
    perkin_elmer = PermissibleValue(text="perkin_elmer")
    scientific_industries = PermissibleValue(text="scientific_industries")
    illumina = PermissibleValue(text="illumina")
    nikon = PermissibleValue(text="nikon")
    fia_lab = PermissibleValue(text="fia_lab")
    shimadzu = PermissibleValue(text="shimadzu")
    regen_ag_lab = PermissibleValue(text="regen_ag_lab")
    kuo = PermissibleValue(text="kuo")
    rigaku = PermissibleValue(text="rigaku")
    panalytical = PermissibleValue(text="panalytical")

    _defn = EnumDefinition(
        name="VendorEnum",
    )

class YesNoEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="YesNoEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "True",
            PermissibleValue(text="True"))
        setattr(cls, "False",
            PermissibleValue(text="False"))

# Slots
class slots:
    pass

slots.acquisition_strategy = Slot(uri=ANALYSIS_API_SCHEMA.acquisition_strategy, name="acquisition_strategy", curie=ANALYSIS_API_SCHEMA.curie('acquisition_strategy'),
                   model_uri=ANALYSIS_API_SCHEMA.acquisition_strategy, domain=None, range=Optional[Union[str, "MassSpectrometryAcquisitionStrategyEnum"]])

slots.additional_information = Slot(uri=ANALYSIS_API_SCHEMA.additional_information, name="additional_information", curie=ANALYSIS_API_SCHEMA.curie('additional_information'),
                   model_uri=ANALYSIS_API_SCHEMA.additional_information, domain=None, range=Optional[str])

slots.aerosol_type = Slot(uri=ANALYSIS_API_SCHEMA.aerosol_type, name="aerosol_type", curie=ANALYSIS_API_SCHEMA.curie('aerosol_type'),
                   model_uri=ANALYSIS_API_SCHEMA.aerosol_type, domain=None, range=Union[str, "AerosolTypeEnum"])

slots.agitation_speed_rpm = Slot(uri=ANALYSIS_API_SCHEMA.agitation_speed_rpm, name="agitation_speed_rpm", curie=ANALYSIS_API_SCHEMA.curie('agitation_speed_rpm'),
                   model_uri=ANALYSIS_API_SCHEMA.agitation_speed_rpm, domain=None, range=Optional[int])

slots.agrochem_addition = Slot(uri=ANALYSIS_API_SCHEMA.agrochem_addition, name="agrochem_addition", curie=ANALYSIS_API_SCHEMA.curie('agrochem_addition'),
                   model_uri=ANALYSIS_API_SCHEMA.agrochem_addition, domain=None, range=Optional[str])

slots.air_temp_regm = Slot(uri=ANALYSIS_API_SCHEMA.air_temp_regm, name="air_temp_regm", curie=ANALYSIS_API_SCHEMA.curie('air_temp_regm'),
                   model_uri=ANALYSIS_API_SCHEMA.air_temp_regm, domain=None, range=Optional[str])

slots.al_sat = Slot(uri=ANALYSIS_API_SCHEMA.al_sat, name="al_sat", curie=ANALYSIS_API_SCHEMA.curie('al_sat'),
                   model_uri=ANALYSIS_API_SCHEMA.al_sat, domain=None, range=Optional[str])

slots.al_sat_meth = Slot(uri=ANALYSIS_API_SCHEMA.al_sat_meth, name="al_sat_meth", curie=ANALYSIS_API_SCHEMA.curie('al_sat_meth'),
                   model_uri=ANALYSIS_API_SCHEMA.al_sat_meth, domain=None, range=Optional[str])

slots.alkalinity = Slot(uri=ANALYSIS_API_SCHEMA.alkalinity, name="alkalinity", curie=ANALYSIS_API_SCHEMA.curie('alkalinity'),
                   model_uri=ANALYSIS_API_SCHEMA.alkalinity, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(mg|meq)/L$'))

slots.alkalinity_method = Slot(uri=ANALYSIS_API_SCHEMA.alkalinity_method, name="alkalinity_method", curie=ANALYSIS_API_SCHEMA.curie('alkalinity_method'),
                   model_uri=ANALYSIS_API_SCHEMA.alkalinity_method, domain=None, range=Optional[str])

slots.alkyl_diethers = Slot(uri=ANALYSIS_API_SCHEMA.alkyl_diethers, name="alkyl_diethers", curie=ANALYSIS_API_SCHEMA.curie('alkyl_diethers'),
                   model_uri=ANALYSIS_API_SCHEMA.alkyl_diethers, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.alt = Slot(uri=ANALYSIS_API_SCHEMA.alt, name="alt", curie=ANALYSIS_API_SCHEMA.curie('alt'),
                   model_uri=ANALYSIS_API_SCHEMA.alt, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?m(?:-\d+(\.\d+)?m)?$'))

slots.aminopept_act = Slot(uri=ANALYSIS_API_SCHEMA.aminopept_act, name="aminopept_act", curie=ANALYSIS_API_SCHEMA.curie('aminopept_act'),
                   model_uri=ANALYSIS_API_SCHEMA.aminopept_act, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*mol/L/h$'))

slots.ammonium = Slot(uri=ANALYSIS_API_SCHEMA.ammonium, name="ammonium", curie=ANALYSIS_API_SCHEMA.curie('ammonium'),
                   model_uri=ANALYSIS_API_SCHEMA.ammonium, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(umol/L|mg/L|ppm)$'))

slots.analysis_type = Slot(uri=ANALYSIS_API_SCHEMA.analysis_type, name="analysis_type", curie=ANALYSIS_API_SCHEMA.curie('analysis_type'),
                   model_uri=ANALYSIS_API_SCHEMA.analysis_type, domain=None, range=Optional[str])

slots.analyte_category = Slot(uri=ANALYSIS_API_SCHEMA.analyte_category, name="analyte_category", curie=ANALYSIS_API_SCHEMA.curie('analyte_category'),
                   model_uri=ANALYSIS_API_SCHEMA.analyte_category, domain=None, range=Optional[Union[str, "AnalyteCategoryEnum"]])

slots.analytic = Slot(uri=ANALYSIS_API_SCHEMA.analytic, name="analytic", curie=ANALYSIS_API_SCHEMA.curie('analytic'),
                   model_uri=ANALYSIS_API_SCHEMA.analytic, domain=None, range=str)

slots.ances_data = Slot(uri=ANALYSIS_API_SCHEMA.ances_data, name="ances_data", curie=ANALYSIS_API_SCHEMA.curie('ances_data'),
                   model_uri=ANALYSIS_API_SCHEMA.ances_data, domain=None, range=Optional[str])

slots.annotation_database = Slot(uri=ANALYSIS_API_SCHEMA.annotation_database, name="annotation_database", curie=ANALYSIS_API_SCHEMA.curie('annotation_database'),
                   model_uri=ANALYSIS_API_SCHEMA.annotation_database, domain=None, range=Optional[Union[str, "AnnotationDatabaseEnum"]])

slots.annual_precpt = Slot(uri=ANALYSIS_API_SCHEMA.annual_precpt, name="annual_precpt", curie=ANALYSIS_API_SCHEMA.curie('annual_precpt'),
                   model_uri=ANALYSIS_API_SCHEMA.annual_precpt, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*mm$'))

slots.annual_temp = Slot(uri=ANALYSIS_API_SCHEMA.annual_temp, name="annual_temp", curie=ANALYSIS_API_SCHEMA.curie('annual_temp'),
                   model_uri=ANALYSIS_API_SCHEMA.annual_temp, domain=None, range=Optional[str],
                   pattern=re.compile(r'^-?\d+(\.\d+)?\s*C$'))

slots.antibiotic_regm = Slot(uri=ANALYSIS_API_SCHEMA.antibiotic_regm, name="antibiotic_regm", curie=ANALYSIS_API_SCHEMA.curie('antibiotic_regm'),
                   model_uri=ANALYSIS_API_SCHEMA.antibiotic_regm, domain=None, range=Optional[str])

slots.aq = Slot(uri=ANALYSIS_API_SCHEMA.aq, name="aq", curie=ANALYSIS_API_SCHEMA.curie('aq'),
                   model_uri=ANALYSIS_API_SCHEMA.aq, domain=None, range=Optional[float])

slots.atmospheric_data = Slot(uri=ANALYSIS_API_SCHEMA.atmospheric_data, name="atmospheric_data", curie=ANALYSIS_API_SCHEMA.curie('atmospheric_data'),
                   model_uri=ANALYSIS_API_SCHEMA.atmospheric_data, domain=None, range=Optional[str])

slots.average_well_color_development = Slot(uri=ANALYSIS_API_SCHEMA.average_well_color_development, name="average_well_color_development", curie=ANALYSIS_API_SCHEMA.curie('average_well_color_development'),
                   model_uri=ANALYSIS_API_SCHEMA.average_well_color_development, domain=None, range=Optional[float])

slots.bac_prod = Slot(uri=ANALYSIS_API_SCHEMA.bac_prod, name="bac_prod", curie=ANALYSIS_API_SCHEMA.curie('bac_prod'),
                   model_uri=ANALYSIS_API_SCHEMA.bac_prod, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.bac_resp = Slot(uri=ANALYSIS_API_SCHEMA.bac_resp, name="bac_resp", curie=ANALYSIS_API_SCHEMA.curie('bac_resp'),
                   model_uri=ANALYSIS_API_SCHEMA.bac_resp, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.bacteria_carb_prod = Slot(uri=ANALYSIS_API_SCHEMA.bacteria_carb_prod, name="bacteria_carb_prod", curie=ANALYSIS_API_SCHEMA.curie('bacteria_carb_prod'),
                   model_uri=ANALYSIS_API_SCHEMA.bacteria_carb_prod, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.biochem_oxygen_dem = Slot(uri=ANALYSIS_API_SCHEMA.biochem_oxygen_dem, name="biochem_oxygen_dem", curie=ANALYSIS_API_SCHEMA.curie('biochem_oxygen_dem'),
                   model_uri=ANALYSIS_API_SCHEMA.biochem_oxygen_dem, domain=None, range=Optional[str])

slots.biol_stat = Slot(uri=ANALYSIS_API_SCHEMA.biol_stat, name="biol_stat", curie=ANALYSIS_API_SCHEMA.curie('biol_stat'),
                   model_uri=ANALYSIS_API_SCHEMA.biol_stat, domain=None, range=Optional[Union[str, "BiolStatEnum"]])

slots.biological_entity_ref = Slot(uri=ANALYSIS_API_SCHEMA.biological_entity_ref, name="biological_entity_ref", curie=ANALYSIS_API_SCHEMA.curie('biological_entity_ref'),
                   model_uri=ANALYSIS_API_SCHEMA.biological_entity_ref, domain=None, range=Optional[Union[str, BiologicalEntityId]])

slots.biotic_regm = Slot(uri=ANALYSIS_API_SCHEMA.biotic_regm, name="biotic_regm", curie=ANALYSIS_API_SCHEMA.curie('biotic_regm'),
                   model_uri=ANALYSIS_API_SCHEMA.biotic_regm, domain=None, range=Optional[str])

slots.biotic_relationship = Slot(uri=ANALYSIS_API_SCHEMA.biotic_relationship, name="biotic_relationship", curie=ANALYSIS_API_SCHEMA.curie('biotic_relationship'),
                   model_uri=ANALYSIS_API_SCHEMA.biotic_relationship, domain=None, range=Optional[Union[str, "BioticRelationshipEnum"]])

slots.bishomohopanol = Slot(uri=ANALYSIS_API_SCHEMA.bishomohopanol, name="bishomohopanol", curie=ANALYSIS_API_SCHEMA.curie('bishomohopanol'),
                   model_uri=ANALYSIS_API_SCHEMA.bishomohopanol, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(ug/L|ug/g)$'))

slots.blank_mean = Slot(uri=ANALYSIS_API_SCHEMA.blank_mean, name="blank_mean", curie=ANALYSIS_API_SCHEMA.curie('blank_mean'),
                   model_uri=ANALYSIS_API_SCHEMA.blank_mean, domain=None, range=Optional[float])

slots.bromide = Slot(uri=ANALYSIS_API_SCHEMA.bromide, name="bromide", curie=ANALYSIS_API_SCHEMA.curie('bromide'),
                   model_uri=ANALYSIS_API_SCHEMA.bromide, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*ppm$'))

slots.bulk_elect_conductivity = Slot(uri=ANALYSIS_API_SCHEMA.bulk_elect_conductivity, name="bulk_elect_conductivity", curie=ANALYSIS_API_SCHEMA.curie('bulk_elect_conductivity'),
                   model_uri=ANALYSIS_API_SCHEMA.bulk_elect_conductivity, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*mS/cm$'))

slots.calcium = Slot(uri=ANALYSIS_API_SCHEMA.calcium, name="calcium", curie=ANALYSIS_API_SCHEMA.curie('calcium'),
                   model_uri=ANALYSIS_API_SCHEMA.calcium, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(mg/L|umol/L|ppm)$'))

slots.calibration_data = Slot(uri=ANALYSIS_API_SCHEMA.calibration_data, name="calibration_data", curie=ANALYSIS_API_SCHEMA.curie('calibration_data'),
                   model_uri=ANALYSIS_API_SCHEMA.calibration_data, domain=None, range=Optional[Union[str, MassSpectrometryInstrumentDataId]])

slots.calibration_standard = Slot(uri=ANALYSIS_API_SCHEMA.calibration_standard, name="calibration_standard", curie=ANALYSIS_API_SCHEMA.curie('calibration_standard'),
                   model_uri=ANALYSIS_API_SCHEMA.calibration_standard, domain=None, range=Optional[Union[str, PurchasedMaterialId]])

slots.calibration_target = Slot(uri=ANALYSIS_API_SCHEMA.calibration_target, name="calibration_target", curie=ANALYSIS_API_SCHEMA.curie('calibration_target'),
                   model_uri=ANALYSIS_API_SCHEMA.calibration_target, domain=None, range=Optional[Union[str, "CalibrationTargetEnum"]])

slots.carb_dioxide = Slot(uri=ANALYSIS_API_SCHEMA.carb_dioxide, name="carb_dioxide", curie=ANALYSIS_API_SCHEMA.curie('carb_dioxide'),
                   model_uri=ANALYSIS_API_SCHEMA.carb_dioxide, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(umol/L|ppm)$'))

slots.carb_monoxide = Slot(uri=ANALYSIS_API_SCHEMA.carb_monoxide, name="carb_monoxide", curie=ANALYSIS_API_SCHEMA.curie('carb_monoxide'),
                   model_uri=ANALYSIS_API_SCHEMA.carb_monoxide, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(umol/L|ppm)$'))

slots.carb_nitro_ratio = Slot(uri=ANALYSIS_API_SCHEMA.carb_nitro_ratio, name="carb_nitro_ratio", curie=ANALYSIS_API_SCHEMA.curie('carb_nitro_ratio'),
                   model_uri=ANALYSIS_API_SCHEMA.carb_nitro_ratio, domain=None, range=Optional[str])

slots.cas = Slot(uri=ANALYSIS_API_SCHEMA.cas, name="cas", curie=ANALYSIS_API_SCHEMA.curie('cas'),
                   model_uri=ANALYSIS_API_SCHEMA.cas, domain=None, range=Optional[str])

slots.cbi = Slot(uri=ANALYSIS_API_SCHEMA.cbi, name="cbi", curie=ANALYSIS_API_SCHEMA.curie('cbi'),
                   model_uri=ANALYSIS_API_SCHEMA.cbi, domain=None, range=Optional[Union[bool, Bool]])

slots.chem_administration = Slot(uri=ANALYSIS_API_SCHEMA.chem_administration, name="chem_administration", curie=ANALYSIS_API_SCHEMA.curie('chem_administration'),
                   model_uri=ANALYSIS_API_SCHEMA.chem_administration, domain=None, range=Optional[str])

slots.chem_mutagen = Slot(uri=ANALYSIS_API_SCHEMA.chem_mutagen, name="chem_mutagen", curie=ANALYSIS_API_SCHEMA.curie('chem_mutagen'),
                   model_uri=ANALYSIS_API_SCHEMA.chem_mutagen, domain=None, range=Optional[str])

slots.chem_oxygen_dem = Slot(uri=ANALYSIS_API_SCHEMA.chem_oxygen_dem, name="chem_oxygen_dem", curie=ANALYSIS_API_SCHEMA.curie('chem_oxygen_dem'),
                   model_uri=ANALYSIS_API_SCHEMA.chem_oxygen_dem, domain=None, range=Optional[str])

slots.chloride = Slot(uri=ANALYSIS_API_SCHEMA.chloride, name="chloride", curie=ANALYSIS_API_SCHEMA.curie('chloride'),
                   model_uri=ANALYSIS_API_SCHEMA.chloride, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(mg/L|ppm)$'))

slots.chlorophyll = Slot(uri=ANALYSIS_API_SCHEMA.chlorophyll, name="chlorophyll", curie=ANALYSIS_API_SCHEMA.curie('chlorophyll'),
                   model_uri=ANALYSIS_API_SCHEMA.chlorophyll, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(mg/m3|ug/L)$'))

slots.chromatography_type = Slot(uri=ANALYSIS_API_SCHEMA.chromatography_type, name="chromatography_type", curie=ANALYSIS_API_SCHEMA.curie('chromatography_type'),
                   model_uri=ANALYSIS_API_SCHEMA.chromatography_type, domain=None, range=Union[str, "ChromatographyCategoryEnum"])

slots.collection_date = Slot(uri=ANALYSIS_API_SCHEMA.collection_date, name="collection_date", curie=ANALYSIS_API_SCHEMA.curie('collection_date'),
                   model_uri=ANALYSIS_API_SCHEMA.collection_date, domain=None, range=Optional[Union[str, XSDDate]],
                   pattern=re.compile(r'^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$'))

slots.collection_mode = Slot(uri=ANALYSIS_API_SCHEMA.collection_mode, name="collection_mode", curie=ANALYSIS_API_SCHEMA.curie('collection_mode'),
                   model_uri=ANALYSIS_API_SCHEMA.collection_mode, domain=None, range=Optional[Union[str, "MassSpectrumCollectionModeEnum"]])

slots.collection_time = Slot(uri=ANALYSIS_API_SCHEMA.collection_time, name="collection_time", curie=ANALYSIS_API_SCHEMA.curie('collection_time'),
                   model_uri=ANALYSIS_API_SCHEMA.collection_time, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])\s*(hh:mm:ss|HH:MM:SS)$'))

slots.color_code = Slot(uri=ANALYSIS_API_SCHEMA.color_code, name="color_code", curie=ANALYSIS_API_SCHEMA.curie('color_code'),
                   model_uri=ANALYSIS_API_SCHEMA.color_code, domain=None, range=Optional[Union[str, "ColorCodeEnum"]])

slots.column = Slot(uri=ANALYSIS_API_SCHEMA.column, name="column", curie=ANALYSIS_API_SCHEMA.curie('column'),
                   model_uri=ANALYSIS_API_SCHEMA.column, domain=None, range=Optional[str])

slots.column_dimensions = Slot(uri=ANALYSIS_API_SCHEMA.column_dimensions, name="column_dimensions", curie=ANALYSIS_API_SCHEMA.curie('column_dimensions'),
                   model_uri=ANALYSIS_API_SCHEMA.column_dimensions, domain=None, range=Optional[str])

slots.column_manufacturer = Slot(uri=ANALYSIS_API_SCHEMA.column_manufacturer, name="column_manufacturer", curie=ANALYSIS_API_SCHEMA.curie('column_manufacturer'),
                   model_uri=ANALYSIS_API_SCHEMA.column_manufacturer, domain=None, range=Optional[str])

slots.commercial_media_catalog = Slot(uri=ANALYSIS_API_SCHEMA.commercial_media_catalog, name="commercial_media_catalog", curie=ANALYSIS_API_SCHEMA.curie('commercial_media_catalog'),
                   model_uri=ANALYSIS_API_SCHEMA.commercial_media_catalog, domain=None, range=Optional[str])

slots.component_description = Slot(uri=ANALYSIS_API_SCHEMA.component_description, name="component_description", curie=ANALYSIS_API_SCHEMA.curie('component_description'),
                   model_uri=ANALYSIS_API_SCHEMA.component_description, domain=None, range=Optional[str])

slots.component_name = Slot(uri=ANALYSIS_API_SCHEMA.component_name, name="component_name", curie=ANALYSIS_API_SCHEMA.curie('component_name'),
                   model_uri=ANALYSIS_API_SCHEMA.component_name, domain=None, range=Optional[str])

slots.compound_name = Slot(uri=ANALYSIS_API_SCHEMA.compound_name, name="compound_name", curie=ANALYSIS_API_SCHEMA.curie('compound_name'),
                   model_uri=ANALYSIS_API_SCHEMA.compound_name, domain=None, range=Optional[str])

slots.concentration_ug_per_uL = Slot(uri=ANALYSIS_API_SCHEMA.concentration_ug_per_uL, name="concentration_ug_per_uL", curie=ANALYSIS_API_SCHEMA.curie('concentration_ug_per_uL'),
                   model_uri=ANALYSIS_API_SCHEMA.concentration_ug_per_uL, domain=None, range=Optional[float])

slots.condition_received = Slot(uri=ANALYSIS_API_SCHEMA.condition_received, name="condition_received", curie=ANALYSIS_API_SCHEMA.curie('condition_received'),
                   model_uri=ANALYSIS_API_SCHEMA.condition_received, domain=None, range=Optional[str])

slots.conduc = Slot(uri=ANALYSIS_API_SCHEMA.conduc, name="conduc", curie=ANALYSIS_API_SCHEMA.curie('conduc'),
                   model_uri=ANALYSIS_API_SCHEMA.conduc, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.confirmed_receipt = Slot(uri=ANALYSIS_API_SCHEMA.confirmed_receipt, name="confirmed_receipt", curie=ANALYSIS_API_SCHEMA.curie('confirmed_receipt'),
                   model_uri=ANALYSIS_API_SCHEMA.confirmed_receipt, domain=None, range=Optional[Union[bool, Bool]])

slots.construct_component = Slot(uri=ANALYSIS_API_SCHEMA.construct_component, name="construct_component", curie=ANALYSIS_API_SCHEMA.curie('construct_component'),
                   model_uri=ANALYSIS_API_SCHEMA.construct_component, domain=None, range=Optional[Union[str, "ConstructComponentEnum"]])

slots.container_type = Slot(uri=ANALYSIS_API_SCHEMA.container_type, name="container_type", curie=ANALYSIS_API_SCHEMA.curie('container_type'),
                   model_uri=ANALYSIS_API_SCHEMA.container_type, domain=None, range=Optional[str])

slots.contaminant_strains = Slot(uri=ANALYSIS_API_SCHEMA.contaminant_strains, name="contaminant_strains", curie=ANALYSIS_API_SCHEMA.curie('contaminant_strains'),
                   model_uri=ANALYSIS_API_SCHEMA.contaminant_strains, domain=None, range=Optional[str])

slots.core_group = Slot(uri=ANALYSIS_API_SCHEMA.core_group, name="core_group", curie=ANALYSIS_API_SCHEMA.curie('core_group'),
                   model_uri=ANALYSIS_API_SCHEMA.core_group, domain=None, range=Optional[Union[str, "MONetCoreGroupEnum"]])

slots.core_section = Slot(uri=ANALYSIS_API_SCHEMA.core_section, name="core_section", curie=ANALYSIS_API_SCHEMA.curie('core_section'),
                   model_uri=ANALYSIS_API_SCHEMA.core_section, domain=None, range=Optional[Union[str, "CoreSectionEnum"]])

slots.creation_date = Slot(uri=ANALYSIS_API_SCHEMA.creation_date, name="creation_date", curie=ANALYSIS_API_SCHEMA.curie('creation_date'),
                   model_uri=ANALYSIS_API_SCHEMA.creation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.crop_rotation = Slot(uri=ANALYSIS_API_SCHEMA.crop_rotation, name="crop_rotation", curie=ANALYSIS_API_SCHEMA.curie('crop_rotation'),
                   model_uri=ANALYSIS_API_SCHEMA.crop_rotation, domain=None, range=Optional[str])

slots.cult_root_med = Slot(uri=ANALYSIS_API_SCHEMA.cult_root_med, name="cult_root_med", curie=ANALYSIS_API_SCHEMA.curie('cult_root_med'),
                   model_uri=ANALYSIS_API_SCHEMA.cult_root_med, domain=None, range=Optional[str])

slots.cur_land_use = Slot(uri=ANALYSIS_API_SCHEMA.cur_land_use, name="cur_land_use", curie=ANALYSIS_API_SCHEMA.curie('cur_land_use'),
                   model_uri=ANALYSIS_API_SCHEMA.cur_land_use, domain=None, range=Optional[Union[str, "LandUseEnum"]])

slots.cur_vegetation = Slot(uri=ANALYSIS_API_SCHEMA.cur_vegetation, name="cur_vegetation", curie=ANALYSIS_API_SCHEMA.curie('cur_vegetation'),
                   model_uri=ANALYSIS_API_SCHEMA.cur_vegetation, domain=None, range=Optional[str])

slots.cur_vegetation_meth = Slot(uri=ANALYSIS_API_SCHEMA.cur_vegetation_meth, name="cur_vegetation_meth", curie=ANALYSIS_API_SCHEMA.curie('cur_vegetation_meth'),
                   model_uri=ANALYSIS_API_SCHEMA.cur_vegetation_meth, domain=None, range=Optional[str])

slots.cv_percent = Slot(uri=ANALYSIS_API_SCHEMA.cv_percent, name="cv_percent", curie=ANALYSIS_API_SCHEMA.curie('cv_percent'),
                   model_uri=ANALYSIS_API_SCHEMA.cv_percent, domain=None, range=Optional[float])

slots.date_received = Slot(uri=ANALYSIS_API_SCHEMA.date_received, name="date_received", curie=ANALYSIS_API_SCHEMA.curie('date_received'),
                   model_uri=ANALYSIS_API_SCHEMA.date_received, domain=None, range=Optional[Union[str, XSDDate]])

slots.dd_ms2_resolution = Slot(uri=ANALYSIS_API_SCHEMA.dd_ms2_resolution, name="dd_ms2_resolution", curie=ANALYSIS_API_SCHEMA.curie('dd_ms2_resolution'),
                   model_uri=ANALYSIS_API_SCHEMA.dd_ms2_resolution, domain=None, range=float)

slots.density = Slot(uri=ANALYSIS_API_SCHEMA.density, name="density", curie=ANALYSIS_API_SCHEMA.curie('density'),
                   model_uri=ANALYSIS_API_SCHEMA.density, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(g/m3|g/cm3)$'))

slots.depth = Slot(uri=ANALYSIS_API_SCHEMA.depth, name="depth", curie=ANALYSIS_API_SCHEMA.curie('depth'),
                   model_uri=ANALYSIS_API_SCHEMA.depth, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?(-\d+(\.\d+)?)?\s*m$'))

slots.description = Slot(uri=ANALYSIS_API_SCHEMA.description, name="description", curie=ANALYSIS_API_SCHEMA.curie('description'),
                   model_uri=ANALYSIS_API_SCHEMA.description, domain=None, range=Optional[str])

slots.diether_lipids = Slot(uri=ANALYSIS_API_SCHEMA.diether_lipids, name="diether_lipids", curie=ANALYSIS_API_SCHEMA.curie('diether_lipids'),
                   model_uri=ANALYSIS_API_SCHEMA.diether_lipids, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*ng/L$'))

slots.diss_carb_dioxide = Slot(uri=ANALYSIS_API_SCHEMA.diss_carb_dioxide, name="diss_carb_dioxide", curie=ANALYSIS_API_SCHEMA.curie('diss_carb_dioxide'),
                   model_uri=ANALYSIS_API_SCHEMA.diss_carb_dioxide, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(umol|mg)/L$'))

slots.diss_hydrogen = Slot(uri=ANALYSIS_API_SCHEMA.diss_hydrogen, name="diss_hydrogen", curie=ANALYSIS_API_SCHEMA.curie('diss_hydrogen'),
                   model_uri=ANALYSIS_API_SCHEMA.diss_hydrogen, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*umol/L$'))

slots.diss_inorg_carb = Slot(uri=ANALYSIS_API_SCHEMA.diss_inorg_carb, name="diss_inorg_carb", curie=ANALYSIS_API_SCHEMA.curie('diss_inorg_carb'),
                   model_uri=ANALYSIS_API_SCHEMA.diss_inorg_carb, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(ug/L|mg/L|ppm)$'))

slots.diss_inorg_nitro = Slot(uri=ANALYSIS_API_SCHEMA.diss_inorg_nitro, name="diss_inorg_nitro", curie=ANALYSIS_API_SCHEMA.curie('diss_inorg_nitro'),
                   model_uri=ANALYSIS_API_SCHEMA.diss_inorg_nitro, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(umol/L|ug/L)$'))

slots.diss_inorg_phosp = Slot(uri=ANALYSIS_API_SCHEMA.diss_inorg_phosp, name="diss_inorg_phosp", curie=ANALYSIS_API_SCHEMA.curie('diss_inorg_phosp'),
                   model_uri=ANALYSIS_API_SCHEMA.diss_inorg_phosp, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.diss_org_carb = Slot(uri=ANALYSIS_API_SCHEMA.diss_org_carb, name="diss_org_carb", curie=ANALYSIS_API_SCHEMA.curie('diss_org_carb'),
                   model_uri=ANALYSIS_API_SCHEMA.diss_org_carb, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(umol/L|mg/L)$'))

slots.diss_org_nitro = Slot(uri=ANALYSIS_API_SCHEMA.diss_org_nitro, name="diss_org_nitro", curie=ANALYSIS_API_SCHEMA.curie('diss_org_nitro'),
                   model_uri=ANALYSIS_API_SCHEMA.diss_org_nitro, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.diss_oxygen = Slot(uri=ANALYSIS_API_SCHEMA.diss_oxygen, name="diss_oxygen", curie=ANALYSIS_API_SCHEMA.curie('diss_oxygen'),
                   model_uri=ANALYSIS_API_SCHEMA.diss_oxygen, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(umol/kg|mg/L)$'))

slots.donor_organism = Slot(uri=ANALYSIS_API_SCHEMA.donor_organism, name="donor_organism", curie=ANALYSIS_API_SCHEMA.curie('donor_organism'),
                   model_uri=ANALYSIS_API_SCHEMA.donor_organism, domain=None, range=Optional[str])

slots.down_par = Slot(uri=ANALYSIS_API_SCHEMA.down_par, name="down_par", curie=ANALYSIS_API_SCHEMA.curie('down_par'),
                   model_uri=ANALYSIS_API_SCHEMA.down_par, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.drainage_class = Slot(uri=ANALYSIS_API_SCHEMA.drainage_class, name="drainage_class", curie=ANALYSIS_API_SCHEMA.curie('drainage_class'),
                   model_uri=ANALYSIS_API_SCHEMA.drainage_class, domain=None, range=Optional[Union[str, "DrainageClassEnum"]])

slots.duration_min = Slot(uri=ANALYSIS_API_SCHEMA.duration_min, name="duration_min", curie=ANALYSIS_API_SCHEMA.curie('duration_min'),
                   model_uri=ANALYSIS_API_SCHEMA.duration_min, domain=None, range=Optional[float])

slots.efficiency_percent = Slot(uri=ANALYSIS_API_SCHEMA.efficiency_percent, name="efficiency_percent", curie=ANALYSIS_API_SCHEMA.curie('efficiency_percent'),
                   model_uri=ANALYSIS_API_SCHEMA.efficiency_percent, domain=None, range=Optional[str])

slots.elev = Slot(uri=ANALYSIS_API_SCHEMA.elev, name="elev", curie=ANALYSIS_API_SCHEMA.curie('elev'),
                   model_uri=ANALYSIS_API_SCHEMA.elev, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*m$'))

slots.email = Slot(uri=ANALYSIS_API_SCHEMA.email, name="email", curie=ANALYSIS_API_SCHEMA.curie('email'),
                   model_uri=ANALYSIS_API_SCHEMA.email, domain=None, range=Optional[str])

slots.emsl_activity = Slot(uri=ANALYSIS_API_SCHEMA.emsl_activity, name="emsl_activity", curie=ANALYSIS_API_SCHEMA.curie('emsl_activity'),
                   model_uri=ANALYSIS_API_SCHEMA.emsl_activity, domain=None, range=Optional[str])

slots.emulsions = Slot(uri=ANALYSIS_API_SCHEMA.emulsions, name="emulsions", curie=ANALYSIS_API_SCHEMA.curie('emulsions'),
                   model_uri=ANALYSIS_API_SCHEMA.emulsions, domain=None, range=Optional[str])

slots.encoded_traits = Slot(uri=ANALYSIS_API_SCHEMA.encoded_traits, name="encoded_traits", curie=ANALYSIS_API_SCHEMA.curie('encoded_traits'),
                   model_uri=ANALYSIS_API_SCHEMA.encoded_traits, domain=None, range=Optional[str])

slots.env_broad_scale = Slot(uri=ANALYSIS_API_SCHEMA.env_broad_scale, name="env_broad_scale", curie=ANALYSIS_API_SCHEMA.curie('env_broad_scale'),
                   model_uri=ANALYSIS_API_SCHEMA.env_broad_scale, domain=None, range=Optional[str],
                   pattern=re.compile(r'^_*\s*[a-zA-Z\s]+\[ENVO:\d+\]$'))

slots.env_local_scale = Slot(uri=ANALYSIS_API_SCHEMA.env_local_scale, name="env_local_scale", curie=ANALYSIS_API_SCHEMA.curie('env_local_scale'),
                   model_uri=ANALYSIS_API_SCHEMA.env_local_scale, domain=None, range=Optional[str],
                   pattern=re.compile(r'^_*\s*[a-zA-Z\s]+\[ENVO:\d+\]$'))

slots.env_medium = Slot(uri=ANALYSIS_API_SCHEMA.env_medium, name="env_medium", curie=ANALYSIS_API_SCHEMA.curie('env_medium'),
                   model_uri=ANALYSIS_API_SCHEMA.env_medium, domain=None, range=Optional[str],
                   pattern=re.compile(r'^_*\s*[a-zA-Z\s]+\[ENVO:\d+\]$'))

slots.experimental_factor = Slot(uri=ANALYSIS_API_SCHEMA.experimental_factor, name="experimental_factor", curie=ANALYSIS_API_SCHEMA.curie('experimental_factor'),
                   model_uri=ANALYSIS_API_SCHEMA.experimental_factor, domain=None, range=Optional[str])

slots.experimental_factor_other = Slot(uri=ANALYSIS_API_SCHEMA.experimental_factor_other, name="experimental_factor_other", curie=ANALYSIS_API_SCHEMA.curie('experimental_factor_other'),
                   model_uri=ANALYSIS_API_SCHEMA.experimental_factor_other, domain=None, range=Optional[str])

slots.exposure_sensitivity = Slot(uri=ANALYSIS_API_SCHEMA.exposure_sensitivity, name="exposure_sensitivity", curie=ANALYSIS_API_SCHEMA.curie('exposure_sensitivity'),
                   model_uri=ANALYSIS_API_SCHEMA.exposure_sensitivity, domain=None, range=Optional[Union[str, list[str]]])

slots.external_identifiers = Slot(uri=ANALYSIS_API_SCHEMA.external_identifiers, name="external_identifiers", curie=ANALYSIS_API_SCHEMA.curie('external_identifiers'),
                   model_uri=ANALYSIS_API_SCHEMA.external_identifiers, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.extraction_method = Slot(uri=ANALYSIS_API_SCHEMA.extraction_method, name="extraction_method", curie=ANALYSIS_API_SCHEMA.curie('extraction_method'),
                   model_uri=ANALYSIS_API_SCHEMA.extraction_method, domain=None, range=Optional[str])

slots.extreme_event = Slot(uri=ANALYSIS_API_SCHEMA.extreme_event, name="extreme_event", curie=ANALYSIS_API_SCHEMA.curie('extreme_event'),
                   model_uri=ANALYSIS_API_SCHEMA.extreme_event, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$'))

slots.fao_class = Slot(uri=ANALYSIS_API_SCHEMA.fao_class, name="fao_class", curie=ANALYSIS_API_SCHEMA.curie('fao_class'),
                   model_uri=ANALYSIS_API_SCHEMA.fao_class, domain=None, range=Optional[Union[str, "FAOClassEnum"]])

slots.fertilizer_regm = Slot(uri=ANALYSIS_API_SCHEMA.fertilizer_regm, name="fertilizer_regm", curie=ANALYSIS_API_SCHEMA.curie('fertilizer_regm'),
                   model_uri=ANALYSIS_API_SCHEMA.fertilizer_regm, domain=None, range=Optional[str])

slots.fid = Slot(uri=ANALYSIS_API_SCHEMA.fid, name="fid", curie=ANALYSIS_API_SCHEMA.curie('fid'),
                   model_uri=ANALYSIS_API_SCHEMA.fid, domain=None, range=Optional[float])

slots.file_curie = Slot(uri=ANALYSIS_API_SCHEMA.file_curie, name="file_curie", curie=ANALYSIS_API_SCHEMA.curie('file_curie'),
                   model_uri=ANALYSIS_API_SCHEMA.file_curie, domain=None, range=Optional[str])

slots.filesize = Slot(uri=ANALYSIS_API_SCHEMA.filesize, name="filesize", curie=ANALYSIS_API_SCHEMA.curie('filesize'),
                   model_uri=ANALYSIS_API_SCHEMA.filesize, domain=None, range=Optional[int])

slots.filter_method = Slot(uri=ANALYSIS_API_SCHEMA.filter_method, name="filter_method", curie=ANALYSIS_API_SCHEMA.curie('filter_method'),
                   model_uri=ANALYSIS_API_SCHEMA.filter_method, domain=None, range=Optional[str])

slots.fire = Slot(uri=ANALYSIS_API_SCHEMA.fire, name="fire", curie=ANALYSIS_API_SCHEMA.curie('fire'),
                   model_uri=ANALYSIS_API_SCHEMA.fire, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$'))

slots.first_blh = Slot(uri=ANALYSIS_API_SCHEMA.first_blh, name="first_blh", curie=ANALYSIS_API_SCHEMA.curie('first_blh'),
                   model_uri=ANALYSIS_API_SCHEMA.first_blh, domain=None, range=Optional[float])

slots.first_blh_quality_index = Slot(uri=ANALYSIS_API_SCHEMA.first_blh_quality_index, name="first_blh_quality_index", curie=ANALYSIS_API_SCHEMA.curie('first_blh_quality_index'),
                   model_uri=ANALYSIS_API_SCHEMA.first_blh_quality_index, domain=None, range=Optional[str])

slots.first_cbh = Slot(uri=ANALYSIS_API_SCHEMA.first_cbh, name="first_cbh", curie=ANALYSIS_API_SCHEMA.curie('first_cbh'),
                   model_uri=ANALYSIS_API_SCHEMA.first_cbh, domain=None, range=Optional[float])

slots.flooding = Slot(uri=ANALYSIS_API_SCHEMA.flooding, name="flooding", curie=ANALYSIS_API_SCHEMA.curie('flooding'),
                   model_uri=ANALYSIS_API_SCHEMA.flooding, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$'))

slots.flow_rate_ul_min = Slot(uri=ANALYSIS_API_SCHEMA.flow_rate_ul_min, name="flow_rate_ul_min", curie=ANALYSIS_API_SCHEMA.curie('flow_rate_ul_min'),
                   model_uri=ANALYSIS_API_SCHEMA.flow_rate_ul_min, domain=None, range=Optional[float])

slots.fluor = Slot(uri=ANALYSIS_API_SCHEMA.fluor, name="fluor", curie=ANALYSIS_API_SCHEMA.curie('fluor'),
                   model_uri=ANALYSIS_API_SCHEMA.fluor, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.fragmentation = Slot(uri=ANALYSIS_API_SCHEMA.fragmentation, name="fragmentation", curie=ANALYSIS_API_SCHEMA.curie('fragmentation'),
                   model_uri=ANALYSIS_API_SCHEMA.fragmentation, domain=None, range=Optional[Union[str, "FragmentationEnum"]])

slots.fungicide_regm = Slot(uri=ANALYSIS_API_SCHEMA.fungicide_regm, name="fungicide_regm", curie=ANALYSIS_API_SCHEMA.curie('fungicide_regm'),
                   model_uri=ANALYSIS_API_SCHEMA.fungicide_regm, domain=None, range=Optional[str])

slots.gaseous_environment = Slot(uri=ANALYSIS_API_SCHEMA.gaseous_environment, name="gaseous_environment", curie=ANALYSIS_API_SCHEMA.curie('gaseous_environment'),
                   model_uri=ANALYSIS_API_SCHEMA.gaseous_environment, domain=None, range=Optional[str])

slots.gaseous_substances = Slot(uri=ANALYSIS_API_SCHEMA.gaseous_substances, name="gaseous_substances", curie=ANALYSIS_API_SCHEMA.curie('gaseous_substances'),
                   model_uri=ANALYSIS_API_SCHEMA.gaseous_substances, domain=None, range=Optional[str])

slots.gene_family = Slot(uri=ANALYSIS_API_SCHEMA.gene_family, name="gene_family", curie=ANALYSIS_API_SCHEMA.curie('gene_family'),
                   model_uri=ANALYSIS_API_SCHEMA.gene_family, domain=None, range=Optional[str])

slots.genetic_mod = Slot(uri=ANALYSIS_API_SCHEMA.genetic_mod, name="genetic_mod", curie=ANALYSIS_API_SCHEMA.curie('genetic_mod'),
                   model_uri=ANALYSIS_API_SCHEMA.genetic_mod, domain=None, range=Optional[str])

slots.genotype_segment_category = Slot(uri=ANALYSIS_API_SCHEMA.genotype_segment_category, name="genotype_segment_category", curie=ANALYSIS_API_SCHEMA.curie('genotype_segment_category'),
                   model_uri=ANALYSIS_API_SCHEMA.genotype_segment_category, domain=None, range=Optional[Union[str, "GenotypeSegmentEnum"]])

slots.genotype_segment_name = Slot(uri=ANALYSIS_API_SCHEMA.genotype_segment_name, name="genotype_segment_name", curie=ANALYSIS_API_SCHEMA.curie('genotype_segment_name'),
                   model_uri=ANALYSIS_API_SCHEMA.genotype_segment_name, domain=None, range=Optional[str])

slots.geo_loc_name = Slot(uri=ANALYSIS_API_SCHEMA.geo_loc_name, name="geo_loc_name", curie=ANALYSIS_API_SCHEMA.curie('geo_loc_name'),
                   model_uri=ANALYSIS_API_SCHEMA.geo_loc_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^([^\s-]{12}|[^\s-]+.+[^\s-]+):\s?([^\s-]{12}|[^\s-]+.+[^\s-]+)\s?([^\s-]{12}|[^\s-]+.+[^\s-]+)$'))

slots.glucosidase_act = Slot(uri=ANALYSIS_API_SCHEMA.glucosidase_act, name="glucosidase_act", curie=ANALYSIS_API_SCHEMA.curie('glucosidase_act'),
                   model_uri=ANALYSIS_API_SCHEMA.glucosidase_act, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*mol/L/h$'))

slots.gravity = Slot(uri=ANALYSIS_API_SCHEMA.gravity, name="gravity", curie=ANALYSIS_API_SCHEMA.curie('gravity'),
                   model_uri=ANALYSIS_API_SCHEMA.gravity, domain=None, range=Optional[str])

slots.growth_facil = Slot(uri=ANALYSIS_API_SCHEMA.growth_facil, name="growth_facil", curie=ANALYSIS_API_SCHEMA.curie('growth_facil'),
                   model_uri=ANALYSIS_API_SCHEMA.growth_facil, domain=None, range=Optional[Union[str, "GrowthFacilityEnum"]])

slots.growth_habit = Slot(uri=ANALYSIS_API_SCHEMA.growth_habit, name="growth_habit", curie=ANALYSIS_API_SCHEMA.curie('growth_habit'),
                   model_uri=ANALYSIS_API_SCHEMA.growth_habit, domain=None, range=Optional[Union[str, "GrowthHabitEnum"]])

slots.growth_hormone_regm = Slot(uri=ANALYSIS_API_SCHEMA.growth_hormone_regm, name="growth_hormone_regm", curie=ANALYSIS_API_SCHEMA.curie('growth_hormone_regm'),
                   model_uri=ANALYSIS_API_SCHEMA.growth_hormone_regm, domain=None, range=Optional[str])

slots.growth_medium = Slot(uri=ANALYSIS_API_SCHEMA.growth_medium, name="growth_medium", curie=ANALYSIS_API_SCHEMA.curie('growth_medium'),
                   model_uri=ANALYSIS_API_SCHEMA.growth_medium, domain=None, range=Optional[str])

slots.growth_time = Slot(uri=ANALYSIS_API_SCHEMA.growth_time, name="growth_time", curie=ANALYSIS_API_SCHEMA.curie('growth_time'),
                   model_uri=ANALYSIS_API_SCHEMA.growth_time, domain=None, range=Optional[str])

slots.guid_source = Slot(uri=ANALYSIS_API_SCHEMA.guid_source, name="guid_source", curie=ANALYSIS_API_SCHEMA.curie('guid_source'),
                   model_uri=ANALYSIS_API_SCHEMA.guid_source, domain=None, range=Optional[str])

slots.heavy_metals = Slot(uri=ANALYSIS_API_SCHEMA.heavy_metals, name="heavy_metals", curie=ANALYSIS_API_SCHEMA.curie('heavy_metals'),
                   model_uri=ANALYSIS_API_SCHEMA.heavy_metals, domain=None, range=Optional[str])

slots.heavy_metals_meth = Slot(uri=ANALYSIS_API_SCHEMA.heavy_metals_meth, name="heavy_metals_meth", curie=ANALYSIS_API_SCHEMA.curie('heavy_metals_meth'),
                   model_uri=ANALYSIS_API_SCHEMA.heavy_metals_meth, domain=None, range=Optional[str])

slots.herbicide_regm = Slot(uri=ANALYSIS_API_SCHEMA.herbicide_regm, name="herbicide_regm", curie=ANALYSIS_API_SCHEMA.curie('herbicide_regm'),
                   model_uri=ANALYSIS_API_SCHEMA.herbicide_regm, domain=None, range=Optional[str])

slots.horizon_meth = Slot(uri=ANALYSIS_API_SCHEMA.horizon_meth, name="horizon_meth", curie=ANALYSIS_API_SCHEMA.curie('horizon_meth'),
                   model_uri=ANALYSIS_API_SCHEMA.horizon_meth, domain=None, range=Optional[str])

slots.host_age = Slot(uri=ANALYSIS_API_SCHEMA.host_age, name="host_age", curie=ANALYSIS_API_SCHEMA.curie('host_age'),
                   model_uri=ANALYSIS_API_SCHEMA.host_age, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(a|d|h)$'))

slots.host_common_name = Slot(uri=ANALYSIS_API_SCHEMA.host_common_name, name="host_common_name", curie=ANALYSIS_API_SCHEMA.curie('host_common_name'),
                   model_uri=ANALYSIS_API_SCHEMA.host_common_name, domain=None, range=Optional[str])

slots.host_disease_stat = Slot(uri=ANALYSIS_API_SCHEMA.host_disease_stat, name="host_disease_stat", curie=ANALYSIS_API_SCHEMA.curie('host_disease_stat'),
                   model_uri=ANALYSIS_API_SCHEMA.host_disease_stat, domain=None, range=Optional[str])

slots.host_dry_mass = Slot(uri=ANALYSIS_API_SCHEMA.host_dry_mass, name="host_dry_mass", curie=ANALYSIS_API_SCHEMA.curie('host_dry_mass'),
                   model_uri=ANALYSIS_API_SCHEMA.host_dry_mass, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(kg|g)$'))

slots.host_genotype = Slot(uri=ANALYSIS_API_SCHEMA.host_genotype, name="host_genotype", curie=ANALYSIS_API_SCHEMA.curie('host_genotype'),
                   model_uri=ANALYSIS_API_SCHEMA.host_genotype, domain=None, range=Optional[str])

slots.host_height = Slot(uri=ANALYSIS_API_SCHEMA.host_height, name="host_height", curie=ANALYSIS_API_SCHEMA.curie('host_height'),
                   model_uri=ANALYSIS_API_SCHEMA.host_height, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(cm|mm|m)$'))

slots.host_infra_spec_name = Slot(uri=ANALYSIS_API_SCHEMA.host_infra_spec_name, name="host_infra_spec_name", curie=ANALYSIS_API_SCHEMA.curie('host_infra_spec_name'),
                   model_uri=ANALYSIS_API_SCHEMA.host_infra_spec_name, domain=None, range=Optional[str])

slots.host_infra_spec_rank = Slot(uri=ANALYSIS_API_SCHEMA.host_infra_spec_rank, name="host_infra_spec_rank", curie=ANALYSIS_API_SCHEMA.curie('host_infra_spec_rank'),
                   model_uri=ANALYSIS_API_SCHEMA.host_infra_spec_rank, domain=None, range=Optional[str])

slots.host_length = Slot(uri=ANALYSIS_API_SCHEMA.host_length, name="host_length", curie=ANALYSIS_API_SCHEMA.curie('host_length'),
                   model_uri=ANALYSIS_API_SCHEMA.host_length, domain=None, range=Optional[str])

slots.host_life_stage = Slot(uri=ANALYSIS_API_SCHEMA.host_life_stage, name="host_life_stage", curie=ANALYSIS_API_SCHEMA.curie('host_life_stage'),
                   model_uri=ANALYSIS_API_SCHEMA.host_life_stage, domain=None, range=Optional[str])

slots.host_phenotype = Slot(uri=ANALYSIS_API_SCHEMA.host_phenotype, name="host_phenotype", curie=ANALYSIS_API_SCHEMA.curie('host_phenotype'),
                   model_uri=ANALYSIS_API_SCHEMA.host_phenotype, domain=None, range=Optional[str])

slots.host_spec_range = Slot(uri=ANALYSIS_API_SCHEMA.host_spec_range, name="host_spec_range", curie=ANALYSIS_API_SCHEMA.curie('host_spec_range'),
                   model_uri=ANALYSIS_API_SCHEMA.host_spec_range, domain=None, range=Optional[str],
                   pattern=re.compile(r'NCBITaxon:\d+'))

slots.host_symbiont = Slot(uri=ANALYSIS_API_SCHEMA.host_symbiont, name="host_symbiont", curie=ANALYSIS_API_SCHEMA.curie('host_symbiont'),
                   model_uri=ANALYSIS_API_SCHEMA.host_symbiont, domain=None, range=Optional[str])

slots.host_taxid = Slot(uri=ANALYSIS_API_SCHEMA.host_taxid, name="host_taxid", curie=ANALYSIS_API_SCHEMA.curie('host_taxid'),
                   model_uri=ANALYSIS_API_SCHEMA.host_taxid, domain=None, range=Optional[str],
                   pattern=re.compile(r'NCBITaxon:\d+'))

slots.host_tot_mass = Slot(uri=ANALYSIS_API_SCHEMA.host_tot_mass, name="host_tot_mass", curie=ANALYSIS_API_SCHEMA.curie('host_tot_mass'),
                   model_uri=ANALYSIS_API_SCHEMA.host_tot_mass, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(kg|g)$'))

slots.host_wet_mass = Slot(uri=ANALYSIS_API_SCHEMA.host_wet_mass, name="host_wet_mass", curie=ANALYSIS_API_SCHEMA.curie('host_wet_mass'),
                   model_uri=ANALYSIS_API_SCHEMA.host_wet_mass, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(kg|g)$'))

slots.humidity = Slot(uri=ANALYSIS_API_SCHEMA.humidity, name="humidity", curie=ANALYSIS_API_SCHEMA.curie('humidity'),
                   model_uri=ANALYSIS_API_SCHEMA.humidity, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.humidity_regm = Slot(uri=ANALYSIS_API_SCHEMA.humidity_regm, name="humidity_regm", curie=ANALYSIS_API_SCHEMA.curie('humidity_regm'),
                   model_uri=ANALYSIS_API_SCHEMA.humidity_regm, domain=None, range=Optional[str])

slots.iat = Slot(uri=ANALYSIS_API_SCHEMA.iat, name="iat", curie=ANALYSIS_API_SCHEMA.curie('iat'),
                   model_uri=ANALYSIS_API_SCHEMA.iat, domain=None, range=Optional[float])

slots.incubation_time_hours = Slot(uri=ANALYSIS_API_SCHEMA.incubation_time_hours, name="incubation_time_hours", curie=ANALYSIS_API_SCHEMA.curie('incubation_time_hours'),
                   model_uri=ANALYSIS_API_SCHEMA.incubation_time_hours, domain=None, range=Optional[float])

slots.indust_eff_percent = Slot(uri=ANALYSIS_API_SCHEMA.indust_eff_percent, name="indust_eff_percent", curie=ANALYSIS_API_SCHEMA.curie('indust_eff_percent'),
                   model_uri=ANALYSIS_API_SCHEMA.indust_eff_percent, domain=None, range=Optional[str])

slots.infiltration_1 = Slot(uri=ANALYSIS_API_SCHEMA.infiltration_1, name="infiltration_1", curie=ANALYSIS_API_SCHEMA.curie('infiltration_1'),
                   model_uri=ANALYSIS_API_SCHEMA.infiltration_1, domain=None, range=Optional[str],
                   pattern=re.compile(r'^((0[0-9]|[1-5][0-9]):([0-5][0-9])\smm:ss|did not collect|failed)$'))

slots.infiltration_2 = Slot(uri=ANALYSIS_API_SCHEMA.infiltration_2, name="infiltration_2", curie=ANALYSIS_API_SCHEMA.curie('infiltration_2'),
                   model_uri=ANALYSIS_API_SCHEMA.infiltration_2, domain=None, range=Optional[str],
                   pattern=re.compile(r'^((0[0-9]|[1-5][0-9]):([0-5][0-9])\smm:ss|did not collect|failed)'))

slots.infiltration_notes = Slot(uri=ANALYSIS_API_SCHEMA.infiltration_notes, name="infiltration_notes", curie=ANALYSIS_API_SCHEMA.curie('infiltration_notes'),
                   model_uri=ANALYSIS_API_SCHEMA.infiltration_notes, domain=None, range=Optional[str])

slots.initiation_date_inoculation = Slot(uri=ANALYSIS_API_SCHEMA.initiation_date_inoculation, name="initiation_date_inoculation", curie=ANALYSIS_API_SCHEMA.curie('initiation_date_inoculation'),
                   model_uri=ANALYSIS_API_SCHEMA.initiation_date_inoculation, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$'))

slots.initiation_date_plant = Slot(uri=ANALYSIS_API_SCHEMA.initiation_date_plant, name="initiation_date_plant", curie=ANALYSIS_API_SCHEMA.curie('initiation_date_plant'),
                   model_uri=ANALYSIS_API_SCHEMA.initiation_date_plant, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$'))

slots.injection = Slot(uri=ANALYSIS_API_SCHEMA.injection, name="injection", curie=ANALYSIS_API_SCHEMA.curie('injection'),
                   model_uri=ANALYSIS_API_SCHEMA.injection, domain=None, range=str)

slots.injection_volume_ul = Slot(uri=ANALYSIS_API_SCHEMA.injection_volume_ul, name="injection_volume_ul", curie=ANALYSIS_API_SCHEMA.curie('injection_volume_ul'),
                   model_uri=ANALYSIS_API_SCHEMA.injection_volume_ul, domain=None, range=Optional[float])

slots.inorg_particles = Slot(uri=ANALYSIS_API_SCHEMA.inorg_particles, name="inorg_particles", curie=ANALYSIS_API_SCHEMA.curie('inorg_particles'),
                   model_uri=ANALYSIS_API_SCHEMA.inorg_particles, domain=None, range=Optional[str])

slots.inspection_method = Slot(uri=ANALYSIS_API_SCHEMA.inspection_method, name="inspection_method", curie=ANALYSIS_API_SCHEMA.curie('inspection_method'),
                   model_uri=ANALYSIS_API_SCHEMA.inspection_method, domain=None, range=Optional[str])

slots.internal_calibration = Slot(uri=ANALYSIS_API_SCHEMA.internal_calibration, name="internal_calibration", curie=ANALYSIS_API_SCHEMA.curie('internal_calibration'),
                   model_uri=ANALYSIS_API_SCHEMA.internal_calibration, domain=None, range=Optional[Union[bool, Bool]])

slots.ionization = Slot(uri=ANALYSIS_API_SCHEMA.ionization, name="ionization", curie=ANALYSIS_API_SCHEMA.curie('ionization'),
                   model_uri=ANALYSIS_API_SCHEMA.ionization, domain=None, range=Union[str, "IonizationSourceEnum"])

slots.isol_growth_condt = Slot(uri=ANALYSIS_API_SCHEMA.isol_growth_condt, name="isol_growth_condt", curie=ANALYSIS_API_SCHEMA.curie('isol_growth_condt'),
                   model_uri=ANALYSIS_API_SCHEMA.isol_growth_condt, domain=None, range=Optional[str])

slots.isolation_window = Slot(uri=ANALYSIS_API_SCHEMA.isolation_window, name="isolation_window", curie=ANALYSIS_API_SCHEMA.curie('isolation_window'),
                   model_uri=ANALYSIS_API_SCHEMA.isolation_window, domain=None, range=str)

slots.isotope_exposure = Slot(uri=ANALYSIS_API_SCHEMA.isotope_exposure, name="isotope_exposure", curie=ANALYSIS_API_SCHEMA.curie('isotope_exposure'),
                   model_uri=ANALYSIS_API_SCHEMA.isotope_exposure, domain=None, range=Optional[str])

slots.item_number = Slot(uri=ANALYSIS_API_SCHEMA.item_number, name="item_number", curie=ANALYSIS_API_SCHEMA.curie('item_number'),
                   model_uri=ANALYSIS_API_SCHEMA.item_number, domain=None, range=Optional[str])

slots.label_text = Slot(uri=ANALYSIS_API_SCHEMA.label_text, name="label_text", curie=ANALYSIS_API_SCHEMA.curie('label_text'),
                   model_uri=ANALYSIS_API_SCHEMA.label_text, domain=None, range=Optional[str])

slots.latitude = Slot(uri=ANALYSIS_API_SCHEMA.latitude, name="latitude", curie=ANALYSIS_API_SCHEMA.curie('latitude'),
                   model_uri=ANALYSIS_API_SCHEMA.latitude, domain=None, range=Optional[float])

slots.light_intensity = Slot(uri=ANALYSIS_API_SCHEMA.light_intensity, name="light_intensity", curie=ANALYSIS_API_SCHEMA.curie('light_intensity'),
                   model_uri=ANALYSIS_API_SCHEMA.light_intensity, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.light_regm = Slot(uri=ANALYSIS_API_SCHEMA.light_regm, name="light_regm", curie=ANALYSIS_API_SCHEMA.curie('light_regm'),
                   model_uri=ANALYSIS_API_SCHEMA.light_regm, domain=None, range=Optional[str])

slots.lims_barcode = Slot(uri=ANALYSIS_API_SCHEMA.lims_barcode, name="lims_barcode", curie=ANALYSIS_API_SCHEMA.curie('lims_barcode'),
                   model_uri=ANALYSIS_API_SCHEMA.lims_barcode, domain=None, range=Optional[str])

slots.lims_id = Slot(uri=ANALYSIS_API_SCHEMA.lims_id, name="lims_id", curie=ANALYSIS_API_SCHEMA.curie('lims_id'),
                   model_uri=ANALYSIS_API_SCHEMA.lims_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^INGEST_SAMPLE_\d{9}$'))

slots.lims_protocol_instance_id = Slot(uri=ANALYSIS_API_SCHEMA.lims_protocol_instance_id, name="lims_protocol_instance_id", curie=ANALYSIS_API_SCHEMA.curie('lims_protocol_instance_id'),
                   model_uri=ANALYSIS_API_SCHEMA.lims_protocol_instance_id, domain=None, range=Optional[int])

slots.lims_task_instance_id = Slot(uri=ANALYSIS_API_SCHEMA.lims_task_instance_id, name="lims_task_instance_id", curie=ANALYSIS_API_SCHEMA.curie('lims_task_instance_id'),
                   model_uri=ANALYSIS_API_SCHEMA.lims_task_instance_id, domain=None, range=Optional[int])

slots.link_addit_analys = Slot(uri=ANALYSIS_API_SCHEMA.link_addit_analys, name="link_addit_analys", curie=ANALYSIS_API_SCHEMA.curie('link_addit_analys'),
                   model_uri=ANALYSIS_API_SCHEMA.link_addit_analys, domain=None, range=Optional[str])

slots.link_class_info = Slot(uri=ANALYSIS_API_SCHEMA.link_class_info, name="link_class_info", curie=ANALYSIS_API_SCHEMA.curie('link_class_info'),
                   model_uri=ANALYSIS_API_SCHEMA.link_class_info, domain=None, range=Optional[str])

slots.link_climate_info = Slot(uri=ANALYSIS_API_SCHEMA.link_climate_info, name="link_climate_info", curie=ANALYSIS_API_SCHEMA.curie('link_climate_info'),
                   model_uri=ANALYSIS_API_SCHEMA.link_climate_info, domain=None, range=Optional[str])

slots.local_class = Slot(uri=ANALYSIS_API_SCHEMA.local_class, name="local_class", curie=ANALYSIS_API_SCHEMA.curie('local_class'),
                   model_uri=ANALYSIS_API_SCHEMA.local_class, domain=None, range=Optional[str])

slots.local_class_meth = Slot(uri=ANALYSIS_API_SCHEMA.local_class_meth, name="local_class_meth", curie=ANALYSIS_API_SCHEMA.curie('local_class_meth'),
                   model_uri=ANALYSIS_API_SCHEMA.local_class_meth, domain=None, range=Optional[str])

slots.location = Slot(uri=ANALYSIS_API_SCHEMA.location, name="location", curie=ANALYSIS_API_SCHEMA.curie('location'),
                   model_uri=ANALYSIS_API_SCHEMA.location, domain=None, range=str)

slots.longitude = Slot(uri=ANALYSIS_API_SCHEMA.longitude, name="longitude", curie=ANALYSIS_API_SCHEMA.curie('longitude'),
                   model_uri=ANALYSIS_API_SCHEMA.longitude, domain=None, range=Optional[float])

slots.loop_count = Slot(uri=ANALYSIS_API_SCHEMA.loop_count, name="loop_count", curie=ANALYSIS_API_SCHEMA.curie('loop_count'),
                   model_uri=ANALYSIS_API_SCHEMA.loop_count, domain=None, range=str)

slots.magnesium = Slot(uri=ANALYSIS_API_SCHEMA.magnesium, name="magnesium", curie=ANALYSIS_API_SCHEMA.curie('magnesium'),
                   model_uri=ANALYSIS_API_SCHEMA.magnesium, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(umol/kg|mol/L|mg/L|ppm)$'))

slots.mass_range_max = Slot(uri=ANALYSIS_API_SCHEMA.mass_range_max, name="mass_range_max", curie=ANALYSIS_API_SCHEMA.curie('mass_range_max'),
                   model_uri=ANALYSIS_API_SCHEMA.mass_range_max, domain=None, range=Optional[float])

slots.mass_range_min = Slot(uri=ANALYSIS_API_SCHEMA.mass_range_min, name="mass_range_min", curie=ANALYSIS_API_SCHEMA.curie('mass_range_min'),
                   model_uri=ANALYSIS_API_SCHEMA.mass_range_min, domain=None, range=Optional[float])

slots.md5checksum = Slot(uri=ANALYSIS_API_SCHEMA.md5checksum, name="md5checksum", curie=ANALYSIS_API_SCHEMA.curie('md5checksum'),
                   model_uri=ANALYSIS_API_SCHEMA.md5checksum, domain=None, range=Optional[str])

slots.mean_frict_vel = Slot(uri=ANALYSIS_API_SCHEMA.mean_frict_vel, name="mean_frict_vel", curie=ANALYSIS_API_SCHEMA.curie('mean_frict_vel'),
                   model_uri=ANALYSIS_API_SCHEMA.mean_frict_vel, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*m/s$'))

slots.mean_peak_frict_vel = Slot(uri=ANALYSIS_API_SCHEMA.mean_peak_frict_vel, name="mean_peak_frict_vel", curie=ANALYSIS_API_SCHEMA.curie('mean_peak_frict_vel'),
                   model_uri=ANALYSIS_API_SCHEMA.mean_peak_frict_vel, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*m/s$'))

slots.mean_total_cpc_concentration = Slot(uri=ANALYSIS_API_SCHEMA.mean_total_cpc_concentration, name="mean_total_cpc_concentration", curie=ANALYSIS_API_SCHEMA.curie('mean_total_cpc_concentration'),
                   model_uri=ANALYSIS_API_SCHEMA.mean_total_cpc_concentration, domain=None, range=Optional[float])

slots.mean_total_pops_concentration = Slot(uri=ANALYSIS_API_SCHEMA.mean_total_pops_concentration, name="mean_total_pops_concentration", curie=ANALYSIS_API_SCHEMA.curie('mean_total_pops_concentration'),
                   model_uri=ANALYSIS_API_SCHEMA.mean_total_pops_concentration, domain=None, range=Optional[float])

slots.measure_type = Slot(uri=ANALYSIS_API_SCHEMA.measure_type, name="measure_type", curie=ANALYSIS_API_SCHEMA.curie('measure_type'),
                   model_uri=ANALYSIS_API_SCHEMA.measure_type, domain=None, range=Optional[Union[str, "ProductMeasureType"]])

slots.measurement_type = Slot(uri=ANALYSIS_API_SCHEMA.measurement_type, name="measurement_type", curie=ANALYSIS_API_SCHEMA.curie('measurement_type'),
                   model_uri=ANALYSIS_API_SCHEMA.measurement_type, domain=None, range=Optional[str])

slots.mechanical_damage = Slot(uri=ANALYSIS_API_SCHEMA.mechanical_damage, name="mechanical_damage", curie=ANALYSIS_API_SCHEMA.curie('mechanical_damage'),
                   model_uri=ANALYSIS_API_SCHEMA.mechanical_damage, domain=None, range=Optional[str])

slots.media_additions = Slot(uri=ANALYSIS_API_SCHEMA.media_additions, name="media_additions", curie=ANALYSIS_API_SCHEMA.curie('media_additions'),
                   model_uri=ANALYSIS_API_SCHEMA.media_additions, domain=None, range=Optional[Union[str, list[str]]])

slots.media_formulation = Slot(uri=ANALYSIS_API_SCHEMA.media_formulation, name="media_formulation", curie=ANALYSIS_API_SCHEMA.curie('media_formulation'),
                   model_uri=ANALYSIS_API_SCHEMA.media_formulation, domain=None, range=Optional[Union[str, "FormulationEnum"]])

slots.media_recipe = Slot(uri=ANALYSIS_API_SCHEMA.media_recipe, name="media_recipe", curie=ANALYSIS_API_SCHEMA.curie('media_recipe'),
                   model_uri=ANALYSIS_API_SCHEMA.media_recipe, domain=None, range=Optional[str])

slots.media_ref = Slot(uri=ANALYSIS_API_SCHEMA.media_ref, name="media_ref", curie=ANALYSIS_API_SCHEMA.curie('media_ref'),
                   model_uri=ANALYSIS_API_SCHEMA.media_ref, domain=None, range=Optional[Union[str, ProcessedSampleId]])

slots.media_type = Slot(uri=ANALYSIS_API_SCHEMA.media_type, name="media_type", curie=ANALYSIS_API_SCHEMA.curie('media_type'),
                   model_uri=ANALYSIS_API_SCHEMA.media_type, domain=None, range=Optional[Union[str, "MediaTypeEnum"]])

slots.metaproteomics_analysis_category = Slot(uri=ANALYSIS_API_SCHEMA.metaproteomics_analysis_category, name="metaproteomics_analysis_category", curie=ANALYSIS_API_SCHEMA.curie('metaproteomics_analysis_category'),
                   model_uri=ANALYSIS_API_SCHEMA.metaproteomics_analysis_category, domain=None, range=Optional[Union[str, "MetaproteomicsAnalysisCategoryEnum"]])

slots.methane = Slot(uri=ANALYSIS_API_SCHEMA.methane, name="methane", curie=ANALYSIS_API_SCHEMA.curie('methane'),
                   model_uri=ANALYSIS_API_SCHEMA.methane, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(umol/L|ppm|ppb)$'))

slots.method = Slot(uri=ANALYSIS_API_SCHEMA.method, name="method", curie=ANALYSIS_API_SCHEMA.curie('method'),
                   model_uri=ANALYSIS_API_SCHEMA.method, domain=None, range=Optional[str])

slots.method_development = Slot(uri=ANALYSIS_API_SCHEMA.method_development, name="method_development", curie=ANALYSIS_API_SCHEMA.curie('method_development'),
                   model_uri=ANALYSIS_API_SCHEMA.method_development, domain=None, range=Optional[str])

slots.mg_workflow_step = Slot(uri=ANALYSIS_API_SCHEMA.mg_workflow_step, name="mg_workflow_step", curie=ANALYSIS_API_SCHEMA.curie('mg_workflow_step'),
                   model_uri=ANALYSIS_API_SCHEMA.mg_workflow_step, domain=None, range=Optional[Union[str, "MetagenomicsSteps"]])

slots.micro_biomass_C_meth = Slot(uri=ANALYSIS_API_SCHEMA.micro_biomass_C_meth, name="micro_biomass_C_meth", curie=ANALYSIS_API_SCHEMA.curie('micro_biomass_C_meth'),
                   model_uri=ANALYSIS_API_SCHEMA.micro_biomass_C_meth, domain=None, range=Optional[str])

slots.micro_biomass_c_meth = Slot(uri=ANALYSIS_API_SCHEMA.micro_biomass_c_meth, name="micro_biomass_c_meth", curie=ANALYSIS_API_SCHEMA.curie('micro_biomass_c_meth'),
                   model_uri=ANALYSIS_API_SCHEMA.micro_biomass_c_meth, domain=None, range=Optional[str])

slots.micro_biomass_N_meth = Slot(uri=ANALYSIS_API_SCHEMA.micro_biomass_N_meth, name="micro_biomass_N_meth", curie=ANALYSIS_API_SCHEMA.curie('micro_biomass_N_meth'),
                   model_uri=ANALYSIS_API_SCHEMA.micro_biomass_N_meth, domain=None, range=Optional[str])

slots.micro_biomass_n_meth = Slot(uri=ANALYSIS_API_SCHEMA.micro_biomass_n_meth, name="micro_biomass_n_meth", curie=ANALYSIS_API_SCHEMA.curie('micro_biomass_n_meth'),
                   model_uri=ANALYSIS_API_SCHEMA.micro_biomass_n_meth, domain=None, range=Optional[str])

slots.microbial_biomass = Slot(uri=ANALYSIS_API_SCHEMA.microbial_biomass, name="microbial_biomass", curie=ANALYSIS_API_SCHEMA.curie('microbial_biomass'),
                   model_uri=ANALYSIS_API_SCHEMA.microbial_biomass, domain=None, range=Optional[str])

slots.microbial_biomass_c = Slot(uri=ANALYSIS_API_SCHEMA.microbial_biomass_c, name="microbial_biomass_c", curie=ANALYSIS_API_SCHEMA.curie('microbial_biomass_c'),
                   model_uri=ANALYSIS_API_SCHEMA.microbial_biomass_c, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.microbial_biomass_meth = Slot(uri=ANALYSIS_API_SCHEMA.microbial_biomass_meth, name="microbial_biomass_meth", curie=ANALYSIS_API_SCHEMA.curie('microbial_biomass_meth'),
                   model_uri=ANALYSIS_API_SCHEMA.microbial_biomass_meth, domain=None, range=Optional[str])

slots.microbial_biomass_n = Slot(uri=ANALYSIS_API_SCHEMA.microbial_biomass_n, name="microbial_biomass_n", curie=ANALYSIS_API_SCHEMA.curie('microbial_biomass_n'),
                   model_uri=ANALYSIS_API_SCHEMA.microbial_biomass_n, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.mineral_nutr_regm = Slot(uri=ANALYSIS_API_SCHEMA.mineral_nutr_regm, name="mineral_nutr_regm", curie=ANALYSIS_API_SCHEMA.curie('mineral_nutr_regm'),
                   model_uri=ANALYSIS_API_SCHEMA.mineral_nutr_regm, domain=None, range=Optional[str])

slots.misc_param = Slot(uri=ANALYSIS_API_SCHEMA.misc_param, name="misc_param", curie=ANALYSIS_API_SCHEMA.curie('misc_param'),
                   model_uri=ANALYSIS_API_SCHEMA.misc_param, domain=None, range=Optional[str])

slots.mobile_phases = Slot(uri=ANALYSIS_API_SCHEMA.mobile_phases, name="mobile_phases", curie=ANALYSIS_API_SCHEMA.curie('mobile_phases'),
                   model_uri=ANALYSIS_API_SCHEMA.mobile_phases, domain=None, range=Optional[Union[Union[str, MobilePhaseSegmentId], list[Union[str, MobilePhaseSegmentId]]]])

slots.modification_method = Slot(uri=ANALYSIS_API_SCHEMA.modification_method, name="modification_method", curie=ANALYSIS_API_SCHEMA.curie('modification_method'),
                   model_uri=ANALYSIS_API_SCHEMA.modification_method, domain=None, range=Optional[Union[str, "ModificationMethodEnum"]])

slots.ms_raw_file_type = Slot(uri=ANALYSIS_API_SCHEMA.ms_raw_file_type, name="ms_raw_file_type", curie=ANALYSIS_API_SCHEMA.curie('ms_raw_file_type'),
                   model_uri=ANALYSIS_API_SCHEMA.ms_raw_file_type, domain=None, range=Optional[Union[str, "MassSpecRawFileTypeEnum"]])

slots.n_alkanes = Slot(uri=ANALYSIS_API_SCHEMA.n_alkanes, name="n_alkanes", curie=ANALYSIS_API_SCHEMA.curie('n_alkanes'),
                   model_uri=ANALYSIS_API_SCHEMA.n_alkanes, domain=None, range=Optional[str])

slots.name = Slot(uri=ANALYSIS_API_SCHEMA.name, name="name", curie=ANALYSIS_API_SCHEMA.curie('name'),
                   model_uri=ANALYSIS_API_SCHEMA.name, domain=None, range=str)

slots.neon_domain = Slot(uri=ANALYSIS_API_SCHEMA.neon_domain, name="neon_domain", curie=ANALYSIS_API_SCHEMA.curie('neon_domain'),
                   model_uri=ANALYSIS_API_SCHEMA.neon_domain, domain=None, range=Optional[Union[str, "NEONDomainEnum"]])

slots.neon_plot_id = Slot(uri=ANALYSIS_API_SCHEMA.neon_plot_id, name="neon_plot_id", curie=ANALYSIS_API_SCHEMA.curie('neon_plot_id'),
                   model_uri=ANALYSIS_API_SCHEMA.neon_plot_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Z]{4}_\d{3}$'))

slots.neon_site_code = Slot(uri=ANALYSIS_API_SCHEMA.neon_site_code, name="neon_site_code", curie=ANALYSIS_API_SCHEMA.curie('neon_site_code'),
                   model_uri=ANALYSIS_API_SCHEMA.neon_site_code, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Z]{4}$'))

slots.nitrate = Slot(uri=ANALYSIS_API_SCHEMA.nitrate, name="nitrate", curie=ANALYSIS_API_SCHEMA.curie('nitrate'),
                   model_uri=ANALYSIS_API_SCHEMA.nitrate, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(umol/L|mg/L|ppm)$'))

slots.nitrite = Slot(uri=ANALYSIS_API_SCHEMA.nitrite, name="nitrite", curie=ANALYSIS_API_SCHEMA.curie('nitrite'),
                   model_uri=ANALYSIS_API_SCHEMA.nitrite, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(umol/L|mg/L|ppm)$'))

slots.nitro = Slot(uri=ANALYSIS_API_SCHEMA.nitro, name="nitro", curie=ANALYSIS_API_SCHEMA.curie('nitro'),
                   model_uri=ANALYSIS_API_SCHEMA.nitro, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*umol/L$'))

slots.non_microb_biomass = Slot(uri=ANALYSIS_API_SCHEMA.non_microb_biomass, name="non_microb_biomass", curie=ANALYSIS_API_SCHEMA.curie('non_microb_biomass'),
                   model_uri=ANALYSIS_API_SCHEMA.non_microb_biomass, domain=None, range=Optional[str])

slots.non_microb_biomass_method = Slot(uri=ANALYSIS_API_SCHEMA.non_microb_biomass_method, name="non_microb_biomass_method", curie=ANALYSIS_API_SCHEMA.curie('non_microb_biomass_method'),
                   model_uri=ANALYSIS_API_SCHEMA.non_microb_biomass_method, domain=None, range=Optional[str])

slots.non_min_nutr_regm = Slot(uri=ANALYSIS_API_SCHEMA.non_min_nutr_regm, name="non_min_nutr_regm", curie=ANALYSIS_API_SCHEMA.curie('non_min_nutr_regm'),
                   model_uri=ANALYSIS_API_SCHEMA.non_min_nutr_regm, domain=None, range=Optional[str])

slots.nucleotide_sequencing_category = Slot(uri=ANALYSIS_API_SCHEMA.nucleotide_sequencing_category, name="nucleotide_sequencing_category", curie=ANALYSIS_API_SCHEMA.curie('nucleotide_sequencing_category'),
                   model_uri=ANALYSIS_API_SCHEMA.nucleotide_sequencing_category, domain=None, range=Optional[Union[str, "NucleotideSequencingEnum"]])

slots.org_carb = Slot(uri=ANALYSIS_API_SCHEMA.org_carb, name="org_carb", curie=ANALYSIS_API_SCHEMA.curie('org_carb'),
                   model_uri=ANALYSIS_API_SCHEMA.org_carb, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.org_matter = Slot(uri=ANALYSIS_API_SCHEMA.org_matter, name="org_matter", curie=ANALYSIS_API_SCHEMA.curie('org_matter'),
                   model_uri=ANALYSIS_API_SCHEMA.org_matter, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*mg/L$'))

slots.org_nitro = Slot(uri=ANALYSIS_API_SCHEMA.org_nitro, name="org_nitro", curie=ANALYSIS_API_SCHEMA.curie('org_nitro'),
                   model_uri=ANALYSIS_API_SCHEMA.org_nitro, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.org_nitro_method = Slot(uri=ANALYSIS_API_SCHEMA.org_nitro_method, name="org_nitro_method", curie=ANALYSIS_API_SCHEMA.curie('org_nitro_method'),
                   model_uri=ANALYSIS_API_SCHEMA.org_nitro_method, domain=None, range=Optional[str])

slots.org_particles = Slot(uri=ANALYSIS_API_SCHEMA.org_particles, name="org_particles", curie=ANALYSIS_API_SCHEMA.curie('org_particles'),
                   model_uri=ANALYSIS_API_SCHEMA.org_particles, domain=None, range=Optional[str])

slots.organism_count = Slot(uri=ANALYSIS_API_SCHEMA.organism_count, name="organism_count", curie=ANALYSIS_API_SCHEMA.curie('organism_count'),
                   model_uri=ANALYSIS_API_SCHEMA.organism_count, domain=None, range=Optional[str])

slots.organism_name = Slot(uri=ANALYSIS_API_SCHEMA.organism_name, name="organism_name", curie=ANALYSIS_API_SCHEMA.curie('organism_name'),
                   model_uri=ANALYSIS_API_SCHEMA.organism_name, domain=None, range=Optional[str])

slots.other = Slot(uri=ANALYSIS_API_SCHEMA.other, name="other", curie=ANALYSIS_API_SCHEMA.curie('other'),
                   model_uri=ANALYSIS_API_SCHEMA.other, domain=None, range=Optional[str])

slots.other_growth_facil = Slot(uri=ANALYSIS_API_SCHEMA.other_growth_facil, name="other_growth_facil", curie=ANALYSIS_API_SCHEMA.curie('other_growth_facil'),
                   model_uri=ANALYSIS_API_SCHEMA.other_growth_facil, domain=None, range=Optional[str])

slots.other_guid_source = Slot(uri=ANALYSIS_API_SCHEMA.other_guid_source, name="other_guid_source", curie=ANALYSIS_API_SCHEMA.curie('other_guid_source'),
                   model_uri=ANALYSIS_API_SCHEMA.other_guid_source, domain=None, range=Optional[str])

slots.other_samp_store_temp = Slot(uri=ANALYSIS_API_SCHEMA.other_samp_store_temp, name="other_samp_store_temp", curie=ANALYSIS_API_SCHEMA.curie('other_samp_store_temp'),
                   model_uri=ANALYSIS_API_SCHEMA.other_samp_store_temp, domain=None, range=Optional[str])

slots.other_storage_condt = Slot(uri=ANALYSIS_API_SCHEMA.other_storage_condt, name="other_storage_condt", curie=ANALYSIS_API_SCHEMA.curie('other_storage_condt'),
                   model_uri=ANALYSIS_API_SCHEMA.other_storage_condt, domain=None, range=Optional[str])

slots.other_treatment = Slot(uri=ANALYSIS_API_SCHEMA.other_treatment, name="other_treatment", curie=ANALYSIS_API_SCHEMA.curie('other_treatment'),
                   model_uri=ANALYSIS_API_SCHEMA.other_treatment, domain=None, range=Optional[str])

slots.oxygen = Slot(uri=ANALYSIS_API_SCHEMA.oxygen, name="oxygen", curie=ANALYSIS_API_SCHEMA.curie('oxygen'),
                   model_uri=ANALYSIS_API_SCHEMA.oxygen, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(mg/L|ppm)$'))

slots.oxygen_relationship = Slot(uri=ANALYSIS_API_SCHEMA.oxygen_status, name="oxygen_relationship", curie=ANALYSIS_API_SCHEMA.curie('oxygen_status'),
                   model_uri=ANALYSIS_API_SCHEMA.oxygen_relationship, domain=None, range=Optional[Union[str, "OxygenStatusEnum"]])

slots.parent_workflow_id = Slot(uri=ANALYSIS_API_SCHEMA.parent_workflow_id, name="parent_workflow_id", curie=ANALYSIS_API_SCHEMA.curie('parent_workflow_id'),
                   model_uri=ANALYSIS_API_SCHEMA.parent_workflow_id, domain=None, range=Optional[Union[str, DataProcessingActivityId]])

slots.part_org_carb = Slot(uri=ANALYSIS_API_SCHEMA.part_org_carb, name="part_org_carb", curie=ANALYSIS_API_SCHEMA.curie('part_org_carb'),
                   model_uri=ANALYSIS_API_SCHEMA.part_org_carb, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.part_org_nitro = Slot(uri=ANALYSIS_API_SCHEMA.part_org_nitro, name="part_org_nitro", curie=ANALYSIS_API_SCHEMA.curie('part_org_nitro'),
                   model_uri=ANALYSIS_API_SCHEMA.part_org_nitro, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(umol/L|ug/L)$'))

slots.particle_class = Slot(uri=ANALYSIS_API_SCHEMA.particle_class, name="particle_class", curie=ANALYSIS_API_SCHEMA.curie('particle_class'),
                   model_uri=ANALYSIS_API_SCHEMA.particle_class, domain=None, range=Optional[str])

slots.pathogenicity = Slot(uri=ANALYSIS_API_SCHEMA.pathogenicity, name="pathogenicity", curie=ANALYSIS_API_SCHEMA.curie('pathogenicity'),
                   model_uri=ANALYSIS_API_SCHEMA.pathogenicity, domain=None, range=Optional[str])

slots.perturbation = Slot(uri=ANALYSIS_API_SCHEMA.perturbation, name="perturbation", curie=ANALYSIS_API_SCHEMA.curie('perturbation'),
                   model_uri=ANALYSIS_API_SCHEMA.perturbation, domain=None, range=Optional[str])

slots.pesticide_regm = Slot(uri=ANALYSIS_API_SCHEMA.pesticide_regm, name="pesticide_regm", curie=ANALYSIS_API_SCHEMA.curie('pesticide_regm'),
                   model_uri=ANALYSIS_API_SCHEMA.pesticide_regm, domain=None, range=Optional[str])

slots.petroleum_hydrocarb = Slot(uri=ANALYSIS_API_SCHEMA.petroleum_hydrocarb, name="petroleum_hydrocarb", curie=ANALYSIS_API_SCHEMA.curie('petroleum_hydrocarb'),
                   model_uri=ANALYSIS_API_SCHEMA.petroleum_hydrocarb, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*umol/L$'))

slots.ph = Slot(uri=ANALYSIS_API_SCHEMA.ph, name="ph", curie=ANALYSIS_API_SCHEMA.curie('ph'),
                   model_uri=ANALYSIS_API_SCHEMA.ph, domain=None, range=Optional[float])

slots.ph_adjustment = Slot(uri=ANALYSIS_API_SCHEMA.ph_adjustment, name="ph_adjustment", curie=ANALYSIS_API_SCHEMA.curie('ph_adjustment'),
                   model_uri=ANALYSIS_API_SCHEMA.ph_adjustment, domain=None, range=Optional[Union[bool, Bool]])

slots.ph_meth = Slot(uri=ANALYSIS_API_SCHEMA.ph_meth, name="ph_meth", curie=ANALYSIS_API_SCHEMA.curie('ph_meth'),
                   model_uri=ANALYSIS_API_SCHEMA.ph_meth, domain=None, range=Optional[str])

slots.ph_regm = Slot(uri=ANALYSIS_API_SCHEMA.ph_regm, name="ph_regm", curie=ANALYSIS_API_SCHEMA.curie('ph_regm'),
                   model_uri=ANALYSIS_API_SCHEMA.ph_regm, domain=None, range=Optional[str])

slots.ph_target = Slot(uri=ANALYSIS_API_SCHEMA.ph_target, name="ph_target", curie=ANALYSIS_API_SCHEMA.curie('ph_target'),
                   model_uri=ANALYSIS_API_SCHEMA.ph_target, domain=None, range=Optional[float])

slots.phaeopigments = Slot(uri=ANALYSIS_API_SCHEMA.phaeopigments, name="phaeopigments", curie=ANALYSIS_API_SCHEMA.curie('phaeopigments'),
                   model_uri=ANALYSIS_API_SCHEMA.phaeopigments, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*mg/cm3(;\s*\d+(\.\d+)?\s*mg/cm3)*$'))

slots.phenotype = Slot(uri=ANALYSIS_API_SCHEMA.phenotype, name="phenotype", curie=ANALYSIS_API_SCHEMA.curie('phenotype'),
                   model_uri=ANALYSIS_API_SCHEMA.phenotype, domain=None, range=Optional[str])

slots.phosphate = Slot(uri=ANALYSIS_API_SCHEMA.phosphate, name="phosphate", curie=ANALYSIS_API_SCHEMA.curie('phosphate'),
                   model_uri=ANALYSIS_API_SCHEMA.phosphate, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*umol/L$'))

slots.phosplipid_fatt_acid = Slot(uri=ANALYSIS_API_SCHEMA.phosplipid_fatt_acid, name="phosplipid_fatt_acid", curie=ANALYSIS_API_SCHEMA.curie('phosplipid_fatt_acid'),
                   model_uri=ANALYSIS_API_SCHEMA.phosplipid_fatt_acid, domain=None, range=Optional[str])

slots.photochemical_exposure = Slot(uri=ANALYSIS_API_SCHEMA.photochemical_exposure, name="photochemical_exposure", curie=ANALYSIS_API_SCHEMA.curie('photochemical_exposure'),
                   model_uri=ANALYSIS_API_SCHEMA.photochemical_exposure, domain=None, range=Optional[Union[str, "PhotochemicalExposureEnum"]])

slots.photon_flux = Slot(uri=ANALYSIS_API_SCHEMA.photon_flux, name="photon_flux", curie=ANALYSIS_API_SCHEMA.curie('photon_flux'),
                   model_uri=ANALYSIS_API_SCHEMA.photon_flux, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.plant_age = Slot(uri=ANALYSIS_API_SCHEMA.plant_age, name="plant_age", curie=ANALYSIS_API_SCHEMA.curie('plant_age'),
                   model_uri=ANALYSIS_API_SCHEMA.plant_age, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*\w+$'))

slots.plant_common_name = Slot(uri=ANALYSIS_API_SCHEMA.plant_common_name, name="plant_common_name", curie=ANALYSIS_API_SCHEMA.curie('plant_common_name'),
                   model_uri=ANALYSIS_API_SCHEMA.plant_common_name, domain=None, range=Optional[str])

slots.plant_disease_stat = Slot(uri=ANALYSIS_API_SCHEMA.plant_disease_stat, name="plant_disease_stat", curie=ANALYSIS_API_SCHEMA.curie('plant_disease_stat'),
                   model_uri=ANALYSIS_API_SCHEMA.plant_disease_stat, domain=None, range=Optional[str])

slots.plant_dry_mass = Slot(uri=ANALYSIS_API_SCHEMA.plant_dry_mass, name="plant_dry_mass", curie=ANALYSIS_API_SCHEMA.curie('plant_dry_mass'),
                   model_uri=ANALYSIS_API_SCHEMA.plant_dry_mass, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(kg|g)$'))

slots.plant_genotype = Slot(uri=ANALYSIS_API_SCHEMA.plant_genotype, name="plant_genotype", curie=ANALYSIS_API_SCHEMA.curie('plant_genotype'),
                   model_uri=ANALYSIS_API_SCHEMA.plant_genotype, domain=None, range=Optional[str])

slots.plant_growth_med = Slot(uri=ANALYSIS_API_SCHEMA.plant_growth_med, name="plant_growth_med", curie=ANALYSIS_API_SCHEMA.curie('plant_growth_med'),
                   model_uri=ANALYSIS_API_SCHEMA.plant_growth_med, domain=None, range=Optional[str],
                   pattern=re.compile(r'^_*\s*[a-zA-Z\s]+\[PECO:\d+\]$'))

slots.plant_product = Slot(uri=ANALYSIS_API_SCHEMA.plant_product, name="plant_product", curie=ANALYSIS_API_SCHEMA.curie('plant_product'),
                   model_uri=ANALYSIS_API_SCHEMA.plant_product, domain=None, range=Optional[str])

slots.plant_sex = Slot(uri=ANALYSIS_API_SCHEMA.plant_sex, name="plant_sex", curie=ANALYSIS_API_SCHEMA.curie('plant_sex'),
                   model_uri=ANALYSIS_API_SCHEMA.plant_sex, domain=None, range=Optional[Union[str, "PlantSexEnum"]])

slots.plant_struc = Slot(uri=ANALYSIS_API_SCHEMA.plant_struc, name="plant_struc", curie=ANALYSIS_API_SCHEMA.curie('plant_struc'),
                   model_uri=ANALYSIS_API_SCHEMA.plant_struc, domain=None, range=Optional[Union[str, "PlantStructureEnum"]])

slots.plant_taxid = Slot(uri=ANALYSIS_API_SCHEMA.plant_taxid, name="plant_taxid", curie=ANALYSIS_API_SCHEMA.curie('plant_taxid'),
                   model_uri=ANALYSIS_API_SCHEMA.plant_taxid, domain=None, range=Optional[str])

slots.plant_wet_mass = Slot(uri=ANALYSIS_API_SCHEMA.plant_wet_mass, name="plant_wet_mass", curie=ANALYSIS_API_SCHEMA.curie('plant_wet_mass'),
                   model_uri=ANALYSIS_API_SCHEMA.plant_wet_mass, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(kg|g)$'))

slots.plate_average = Slot(uri=ANALYSIS_API_SCHEMA.plate_average, name="plate_average", curie=ANALYSIS_API_SCHEMA.curie('plate_average'),
                   model_uri=ANALYSIS_API_SCHEMA.plate_average, domain=None, range=Optional[float])

slots.plate_barcode = Slot(uri=ANALYSIS_API_SCHEMA.plate_barcode, name="plate_barcode", curie=ANALYSIS_API_SCHEMA.curie('plate_barcode'),
                   model_uri=ANALYSIS_API_SCHEMA.plate_barcode, domain=None, range=Optional[str])

slots.plate_lot = Slot(uri=ANALYSIS_API_SCHEMA.plate_lot, name="plate_lot", curie=ANALYSIS_API_SCHEMA.curie('plate_lot'),
                   model_uri=ANALYSIS_API_SCHEMA.plate_lot, domain=None, range=Optional[str])

slots.plate_reader_model = Slot(uri=ANALYSIS_API_SCHEMA.plate_reader_model, name="plate_reader_model", curie=ANALYSIS_API_SCHEMA.curie('plate_reader_model'),
                   model_uri=ANALYSIS_API_SCHEMA.plate_reader_model, domain=None, range=Optional[str])

slots.plate_type = Slot(uri=ANALYSIS_API_SCHEMA.plate_type, name="plate_type", curie=ANALYSIS_API_SCHEMA.curie('plate_type'),
                   model_uri=ANALYSIS_API_SCHEMA.plate_type, domain=None, range=str)

slots.polarity = Slot(uri=ANALYSIS_API_SCHEMA.polarity, name="polarity", curie=ANALYSIS_API_SCHEMA.curie('polarity'),
                   model_uri=ANALYSIS_API_SCHEMA.polarity, domain=None, range=Union[str, "PolarityEnum"])

slots.porosity = Slot(uri=ANALYSIS_API_SCHEMA.porosity, name="porosity", curie=ANALYSIS_API_SCHEMA.curie('porosity'),
                   model_uri=ANALYSIS_API_SCHEMA.porosity, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*percent$'))

slots.potassium = Slot(uri=ANALYSIS_API_SCHEMA.potassium, name="potassium", curie=ANALYSIS_API_SCHEMA.curie('potassium'),
                   model_uri=ANALYSIS_API_SCHEMA.potassium, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(mg/L|ppm)$'))

slots.pre_treatment = Slot(uri=ANALYSIS_API_SCHEMA.pre_treatment, name="pre_treatment", curie=ANALYSIS_API_SCHEMA.curie('pre_treatment'),
                   model_uri=ANALYSIS_API_SCHEMA.pre_treatment, domain=None, range=Optional[str])

slots.preparation_date = Slot(uri=ANALYSIS_API_SCHEMA.preparation_date, name="preparation_date", curie=ANALYSIS_API_SCHEMA.curie('preparation_date'),
                   model_uri=ANALYSIS_API_SCHEMA.preparation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.pressure = Slot(uri=ANALYSIS_API_SCHEMA.pressure, name="pressure", curie=ANALYSIS_API_SCHEMA.curie('pressure'),
                   model_uri=ANALYSIS_API_SCHEMA.pressure, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*atm$'))

slots.pressure_control = Slot(uri=ANALYSIS_API_SCHEMA.pressure_control, name="pressure_control", curie=ANALYSIS_API_SCHEMA.curie('pressure_control'),
                   model_uri=ANALYSIS_API_SCHEMA.pressure_control, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*Pa$'))

slots.previous_land_use = Slot(uri=ANALYSIS_API_SCHEMA.previous_land_use, name="previous_land_use", curie=ANALYSIS_API_SCHEMA.curie('previous_land_use'),
                   model_uri=ANALYSIS_API_SCHEMA.previous_land_use, domain=None, range=Optional[str])

slots.previous_land_use_meth = Slot(uri=ANALYSIS_API_SCHEMA.previous_land_use_meth, name="previous_land_use_meth", curie=ANALYSIS_API_SCHEMA.curie('previous_land_use_meth'),
                   model_uri=ANALYSIS_API_SCHEMA.previous_land_use_meth, domain=None, range=Optional[str])

slots.primary_prod = Slot(uri=ANALYSIS_API_SCHEMA.primary_prod, name="primary_prod", curie=ANALYSIS_API_SCHEMA.curie('primary_prod'),
                   model_uri=ANALYSIS_API_SCHEMA.primary_prod, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.primary_treatment = Slot(uri=ANALYSIS_API_SCHEMA.primary_treatment, name="primary_treatment", curie=ANALYSIS_API_SCHEMA.curie('primary_treatment'),
                   model_uri=ANALYSIS_API_SCHEMA.primary_treatment, domain=None, range=Optional[str])

slots.priority_order = Slot(uri=ANALYSIS_API_SCHEMA.priority_order, name="priority_order", curie=ANALYSIS_API_SCHEMA.curie('priority_order'),
                   model_uri=ANALYSIS_API_SCHEMA.priority_order, domain=None, range=Optional[float])

slots.produced_by_ms_run = Slot(uri=ANALYSIS_API_SCHEMA.produced_by_ms_run, name="produced_by_ms_run", curie=ANALYSIS_API_SCHEMA.curie('produced_by_ms_run'),
                   model_uri=ANALYSIS_API_SCHEMA.produced_by_ms_run, domain=None, range=Optional[Union[str, MassSpectrometryDataGenerationActivityId]])

slots.produced_by_sequencing_activity = Slot(uri=ANALYSIS_API_SCHEMA.produced_by_sequencing_activity, name="produced_by_sequencing_activity", curie=ANALYSIS_API_SCHEMA.curie('produced_by_sequencing_activity'),
                   model_uri=ANALYSIS_API_SCHEMA.produced_by_sequencing_activity, domain=None, range=Optional[Union[str, NucleotideSequencingId]])

slots.product_name = Slot(uri=ANALYSIS_API_SCHEMA.product_name, name="product_name", curie=ANALYSIS_API_SCHEMA.curie('product_name'),
                   model_uri=ANALYSIS_API_SCHEMA.product_name, domain=None, range=Optional[str])

slots.production_method = Slot(uri=ANALYSIS_API_SCHEMA.production_method, name="production_method", curie=ANALYSIS_API_SCHEMA.curie('production_method'),
                   model_uri=ANALYSIS_API_SCHEMA.production_method, domain=None, range=Optional[str])

slots.profile_position = Slot(uri=ANALYSIS_API_SCHEMA.profile_position, name="profile_position", curie=ANALYSIS_API_SCHEMA.curie('profile_position'),
                   model_uri=ANALYSIS_API_SCHEMA.profile_position, domain=None, range=Optional[Union[str, "ProfilePositionEnum"]])

slots.project = Slot(uri=ANALYSIS_API_SCHEMA.project, name="project", curie=ANALYSIS_API_SCHEMA.curie('project'),
                   model_uri=ANALYSIS_API_SCHEMA.project, domain=None, range=Optional[int])

slots.propagation = Slot(uri=ANALYSIS_API_SCHEMA.propagation, name="propagation", curie=ANALYSIS_API_SCHEMA.curie('propagation'),
                   model_uri=ANALYSIS_API_SCHEMA.propagation, domain=None, range=Optional[str])

slots.protocol_url = Slot(uri=ANALYSIS_API_SCHEMA.protocol_url, name="protocol_url", curie=ANALYSIS_API_SCHEMA.curie('protocol_url'),
                   model_uri=ANALYSIS_API_SCHEMA.protocol_url, domain=None, range=Optional[str])

slots.protocol_version = Slot(uri=ANALYSIS_API_SCHEMA.protocol_version, name="protocol_version", curie=ANALYSIS_API_SCHEMA.curie('protocol_version'),
                   model_uri=ANALYSIS_API_SCHEMA.protocol_version, domain=None, range=Optional[str])

slots.provider_name = Slot(uri=ANALYSIS_API_SCHEMA.provider_name, name="provider_name", curie=ANALYSIS_API_SCHEMA.curie('provider_name'),
                   model_uri=ANALYSIS_API_SCHEMA.provider_name, domain=None, range=Optional[Union[str, ControlledTermValueId]])

slots.purchased_material_type = Slot(uri=ANALYSIS_API_SCHEMA.purchased_material_type, name="purchased_material_type", curie=ANALYSIS_API_SCHEMA.curie('purchased_material_type'),
                   model_uri=ANALYSIS_API_SCHEMA.purchased_material_type, domain=None, range=str)

slots.radiation_regm = Slot(uri=ANALYSIS_API_SCHEMA.radiation_regm, name="radiation_regm", curie=ANALYSIS_API_SCHEMA.curie('radiation_regm'),
                   model_uri=ANALYSIS_API_SCHEMA.radiation_regm, domain=None, range=Optional[str])

slots.rainfall_regm = Slot(uri=ANALYSIS_API_SCHEMA.rainfall_regm, name="rainfall_regm", curie=ANALYSIS_API_SCHEMA.curie('rainfall_regm'),
                   model_uri=ANALYSIS_API_SCHEMA.rainfall_regm, domain=None, range=Optional[str])

slots.raw_fasta_url = Slot(uri=ANALYSIS_API_SCHEMA.raw_fasta_url, name="raw_fasta_url", curie=ANALYSIS_API_SCHEMA.curie('raw_fasta_url'),
                   model_uri=ANALYSIS_API_SCHEMA.raw_fasta_url, domain=None, range=Optional[str])

slots.reactor_type = Slot(uri=ANALYSIS_API_SCHEMA.reactor_type, name="reactor_type", curie=ANALYSIS_API_SCHEMA.curie('reactor_type'),
                   model_uri=ANALYSIS_API_SCHEMA.reactor_type, domain=None, range=Optional[str])

slots.redox_potential = Slot(uri=ANALYSIS_API_SCHEMA.redox_potential, name="redox_potential", curie=ANALYSIS_API_SCHEMA.curie('redox_potential'),
                   model_uri=ANALYSIS_API_SCHEMA.redox_potential, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*mV$'))

slots.ref_biomaterial = Slot(uri=ANALYSIS_API_SCHEMA.ref_biomaterial, name="ref_biomaterial", curie=ANALYSIS_API_SCHEMA.curie('ref_biomaterial'),
                   model_uri=ANALYSIS_API_SCHEMA.ref_biomaterial, domain=None, range=Optional[str])

slots.replicate = Slot(uri=ANALYSIS_API_SCHEMA.replicate, name="replicate", curie=ANALYSIS_API_SCHEMA.curie('replicate'),
                   model_uri=ANALYSIS_API_SCHEMA.replicate, domain=None, range=Optional[int])

slots.replicate_bio = Slot(uri=ANALYSIS_API_SCHEMA.replicate_bio, name="replicate_bio", curie=ANALYSIS_API_SCHEMA.curie('replicate_bio'),
                   model_uri=ANALYSIS_API_SCHEMA.replicate_bio, domain=None, range=Optional[int])

slots.replicate_number = Slot(uri=ANALYSIS_API_SCHEMA.replicate_number, name="replicate_number", curie=ANALYSIS_API_SCHEMA.curie('replicate_number'),
                   model_uri=ANALYSIS_API_SCHEMA.replicate_number, domain=None, range=Optional[int])

slots.replicate_tech = Slot(uri=ANALYSIS_API_SCHEMA.replicate_tech, name="replicate_tech", curie=ANALYSIS_API_SCHEMA.curie('replicate_tech'),
                   model_uri=ANALYSIS_API_SCHEMA.replicate_tech, domain=None, range=Optional[int])

slots.resolution = Slot(uri=ANALYSIS_API_SCHEMA.resolution, name="resolution", curie=ANALYSIS_API_SCHEMA.curie('resolution'),
                   model_uri=ANALYSIS_API_SCHEMA.resolution, domain=None, range=Union[str, "MassSpecResolutionEnum"])

slots.results_from_ms_processing = Slot(uri=ANALYSIS_API_SCHEMA.results_from_ms_processing, name="results_from_ms_processing", curie=ANALYSIS_API_SCHEMA.curie('results_from_ms_processing'),
                   model_uri=ANALYSIS_API_SCHEMA.results_from_ms_processing, domain=None, range=Optional[Union[str, MassSpectrometryDataProcessingActivityId]])

slots.root_cond = Slot(uri=ANALYSIS_API_SCHEMA.root_cond, name="root_cond", curie=ANALYSIS_API_SCHEMA.curie('root_cond'),
                   model_uri=ANALYSIS_API_SCHEMA.root_cond, domain=None, range=Optional[str])

slots.root_med_carbon = Slot(uri=ANALYSIS_API_SCHEMA.root_med_carbon, name="root_med_carbon", curie=ANALYSIS_API_SCHEMA.curie('root_med_carbon'),
                   model_uri=ANALYSIS_API_SCHEMA.root_med_carbon, domain=None, range=Optional[str])

slots.root_med_macronutr = Slot(uri=ANALYSIS_API_SCHEMA.root_med_macronutr, name="root_med_macronutr", curie=ANALYSIS_API_SCHEMA.curie('root_med_macronutr'),
                   model_uri=ANALYSIS_API_SCHEMA.root_med_macronutr, domain=None, range=Optional[str])

slots.root_med_micronutr = Slot(uri=ANALYSIS_API_SCHEMA.root_med_micronutr, name="root_med_micronutr", curie=ANALYSIS_API_SCHEMA.curie('root_med_micronutr'),
                   model_uri=ANALYSIS_API_SCHEMA.root_med_micronutr, domain=None, range=Optional[str])

slots.root_med_ph = Slot(uri=ANALYSIS_API_SCHEMA.root_med_ph, name="root_med_ph", curie=ANALYSIS_API_SCHEMA.curie('root_med_ph'),
                   model_uri=ANALYSIS_API_SCHEMA.root_med_ph, domain=None, range=Optional[float])

slots.root_med_regl = Slot(uri=ANALYSIS_API_SCHEMA.root_med_regl, name="root_med_regl", curie=ANALYSIS_API_SCHEMA.curie('root_med_regl'),
                   model_uri=ANALYSIS_API_SCHEMA.root_med_regl, domain=None, range=Optional[str])

slots.root_med_solid = Slot(uri=ANALYSIS_API_SCHEMA.root_med_solid, name="root_med_solid", curie=ANALYSIS_API_SCHEMA.curie('root_med_solid'),
                   model_uri=ANALYSIS_API_SCHEMA.root_med_solid, domain=None, range=Optional[str])

slots.root_med_suppl = Slot(uri=ANALYSIS_API_SCHEMA.root_med_suppl, name="root_med_suppl", curie=ANALYSIS_API_SCHEMA.curie('root_med_suppl'),
                   model_uri=ANALYSIS_API_SCHEMA.root_med_suppl, domain=None, range=Optional[str])

slots.s3_base_url = Slot(uri=ANALYSIS_API_SCHEMA.s3_base_url, name="s3_base_url", curie=ANALYSIS_API_SCHEMA.curie('s3_base_url'),
                   model_uri=ANALYSIS_API_SCHEMA.s3_base_url, domain=None, range=Optional[str])

slots.s3_bucket = Slot(uri=ANALYSIS_API_SCHEMA.s3_bucket, name="s3_bucket", curie=ANALYSIS_API_SCHEMA.curie('s3_bucket'),
                   model_uri=ANALYSIS_API_SCHEMA.s3_bucket, domain=None, range=Optional[str])

slots.s3_key = Slot(uri=ANALYSIS_API_SCHEMA.s3_key, name="s3_key", curie=ANALYSIS_API_SCHEMA.curie('s3_key'),
                   model_uri=ANALYSIS_API_SCHEMA.s3_key, domain=None, range=str)

slots.salinity = Slot(uri=ANALYSIS_API_SCHEMA.salinity, name="salinity", curie=ANALYSIS_API_SCHEMA.curie('salinity'),
                   model_uri=ANALYSIS_API_SCHEMA.salinity, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(practical salinity unit|percent)$'))

slots.salinity_method = Slot(uri=ANALYSIS_API_SCHEMA.salinity_method, name="salinity_method", curie=ANALYSIS_API_SCHEMA.curie('salinity_method'),
                   model_uri=ANALYSIS_API_SCHEMA.salinity_method, domain=None, range=Optional[str])

slots.salt_regm = Slot(uri=ANALYSIS_API_SCHEMA.salt_regm, name="salt_regm", curie=ANALYSIS_API_SCHEMA.curie('salt_regm'),
                   model_uri=ANALYSIS_API_SCHEMA.salt_regm, domain=None, range=Optional[str])

slots.samp_capt_status = Slot(uri=ANALYSIS_API_SCHEMA.samp_capt_status, name="samp_capt_status", curie=ANALYSIS_API_SCHEMA.curie('samp_capt_status'),
                   model_uri=ANALYSIS_API_SCHEMA.samp_capt_status, domain=None, range=Optional[str])

slots.samp_dis_stage = Slot(uri=ANALYSIS_API_SCHEMA.samp_dis_stage, name="samp_dis_stage", curie=ANALYSIS_API_SCHEMA.curie('samp_dis_stage'),
                   model_uri=ANALYSIS_API_SCHEMA.samp_dis_stage, domain=None, range=Optional[str])

slots.samp_store_temp = Slot(uri=ANALYSIS_API_SCHEMA.samp_store_temp, name="samp_store_temp", curie=ANALYSIS_API_SCHEMA.curie('samp_store_temp'),
                   model_uri=ANALYSIS_API_SCHEMA.samp_store_temp, domain=None, range=Optional[Union[str, "SampleStoreTempEnum"]])

slots.sample_collected = Slot(uri=ANALYSIS_API_SCHEMA.sample_collected, name="sample_collected", curie=ANALYSIS_API_SCHEMA.curie('sample_collected'),
                   model_uri=ANALYSIS_API_SCHEMA.sample_collected, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.sample_collection_dev = Slot(uri=ANALYSIS_API_SCHEMA.sample_collection_dev, name="sample_collection_dev", curie=ANALYSIS_API_SCHEMA.curie('sample_collection_dev'),
                   model_uri=ANALYSIS_API_SCHEMA.sample_collection_dev, domain=None, range=Optional[str])

slots.sample_collection_method = Slot(uri=ANALYSIS_API_SCHEMA.sample_collection_method, name="sample_collection_method", curie=ANALYSIS_API_SCHEMA.curie('sample_collection_method'),
                   model_uri=ANALYSIS_API_SCHEMA.sample_collection_method, domain=None, range=Optional[str])

slots.sample_end_time = Slot(uri=ANALYSIS_API_SCHEMA.sample_end_time, name="sample_end_time", curie=ANALYSIS_API_SCHEMA.curie('sample_end_time'),
                   model_uri=ANALYSIS_API_SCHEMA.sample_end_time, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$'))

slots.sample_id = Slot(uri=ANALYSIS_API_SCHEMA.sample_id, name="sample_id", curie=ANALYSIS_API_SCHEMA.curie('sample_id'),
                   model_uri=ANALYSIS_API_SCHEMA.sample_id, domain=None, range=Optional[Union[str, SampleId]])

slots.sample_link = Slot(uri=ANALYSIS_API_SCHEMA.sample_link, name="sample_link", curie=ANALYSIS_API_SCHEMA.curie('sample_link'),
                   model_uri=ANALYSIS_API_SCHEMA.sample_link, domain=None, range=Optional[str])

slots.sample_name = Slot(uri=ANALYSIS_API_SCHEMA.sample_name, name="sample_name", curie=ANALYSIS_API_SCHEMA.curie('sample_name'),
                   model_uri=ANALYSIS_API_SCHEMA.sample_name, domain=None, range=Optional[str])

slots.sample_processing = Slot(uri=ANALYSIS_API_SCHEMA.sample_processing, name="sample_processing", curie=ANALYSIS_API_SCHEMA.curie('sample_processing'),
                   model_uri=ANALYSIS_API_SCHEMA.sample_processing, domain=None, range=Optional[str])

slots.sample_start_time = Slot(uri=ANALYSIS_API_SCHEMA.sample_start_time, name="sample_start_time", curie=ANALYSIS_API_SCHEMA.curie('sample_start_time'),
                   model_uri=ANALYSIS_API_SCHEMA.sample_start_time, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])\s*(hh:mm:ss|HH:MM:SS)$'))

slots.sample_type = Slot(uri=ANALYSIS_API_SCHEMA.sample_type, name="sample_type", curie=ANALYSIS_API_SCHEMA.curie('sample_type'),
                   model_uri=ANALYSIS_API_SCHEMA.sample_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'^_*\s*[a-zA-Z\-]+\s\[[a-zA-Z]+:\d+\]$'))

slots.sampled_at_site = Slot(uri=ANALYSIS_API_SCHEMA.sampled_at_site, name="sampled_at_site", curie=ANALYSIS_API_SCHEMA.curie('sampled_at_site'),
                   model_uri=ANALYSIS_API_SCHEMA.sampled_at_site, domain=None, range=Optional[Union[str, SiteId]])

slots.sampled_during = Slot(uri=ANALYSIS_API_SCHEMA.sampled_during, name="sampled_during", curie=ANALYSIS_API_SCHEMA.curie('sampled_during'),
                   model_uri=ANALYSIS_API_SCHEMA.sampled_during, domain=None, range=Optional[Union[str, SamplingActivityId]])

slots.sampled_portion = Slot(uri=ANALYSIS_API_SCHEMA.sampled_portion, name="sampled_portion", curie=ANALYSIS_API_SCHEMA.curie('sampled_portion'),
                   model_uri=ANALYSIS_API_SCHEMA.sampled_portion, domain=None, range=Optional[Union[str, "SamplePortionEnum"]])

slots.sampling_duration = Slot(uri=ANALYSIS_API_SCHEMA.sampling_duration, name="sampling_duration", curie=ANALYSIS_API_SCHEMA.curie('sampling_duration'),
                   model_uri=ANALYSIS_API_SCHEMA.sampling_duration, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*s$'))

slots.sampling_set = Slot(uri=ANALYSIS_API_SCHEMA.sampling_set, name="sampling_set", curie=ANALYSIS_API_SCHEMA.curie('sampling_set'),
                   model_uri=ANALYSIS_API_SCHEMA.sampling_set, domain=None, range=Optional[int])

slots.sealing_method = Slot(uri=ANALYSIS_API_SCHEMA.sealing_method, name="sealing_method", curie=ANALYSIS_API_SCHEMA.curie('sealing_method'),
                   model_uri=ANALYSIS_API_SCHEMA.sealing_method, domain=None, range=Optional[str])

slots.season_environment = Slot(uri=ANALYSIS_API_SCHEMA.season_environment, name="season_environment", curie=ANALYSIS_API_SCHEMA.curie('season_environment'),
                   model_uri=ANALYSIS_API_SCHEMA.season_environment, domain=None, range=Optional[str])

slots.season_precpt = Slot(uri=ANALYSIS_API_SCHEMA.season_precpt, name="season_precpt", curie=ANALYSIS_API_SCHEMA.curie('season_precpt'),
                   model_uri=ANALYSIS_API_SCHEMA.season_precpt, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*mm$'))

slots.season_temp = Slot(uri=ANALYSIS_API_SCHEMA.season_temp, name="season_temp", curie=ANALYSIS_API_SCHEMA.curie('season_temp'),
                   model_uri=ANALYSIS_API_SCHEMA.season_temp, domain=None, range=Optional[str],
                   pattern=re.compile(r'^-?\d+(\.\d+)?\s*C$'))

slots.second_blh = Slot(uri=ANALYSIS_API_SCHEMA.second_blh, name="second_blh", curie=ANALYSIS_API_SCHEMA.curie('second_blh'),
                   model_uri=ANALYSIS_API_SCHEMA.second_blh, domain=None, range=Optional[float])

slots.second_blh_quality = Slot(uri=ANALYSIS_API_SCHEMA.second_blh_quality, name="second_blh_quality", curie=ANALYSIS_API_SCHEMA.curie('second_blh_quality'),
                   model_uri=ANALYSIS_API_SCHEMA.second_blh_quality, domain=None, range=Optional[str])

slots.second_cbh = Slot(uri=ANALYSIS_API_SCHEMA.second_cbh, name="second_cbh", curie=ANALYSIS_API_SCHEMA.curie('second_cbh'),
                   model_uri=ANALYSIS_API_SCHEMA.second_cbh, domain=None, range=Optional[float])

slots.secondary_treatment = Slot(uri=ANALYSIS_API_SCHEMA.secondary_treatment, name="secondary_treatment", curie=ANALYSIS_API_SCHEMA.curie('secondary_treatment'),
                   model_uri=ANALYSIS_API_SCHEMA.secondary_treatment, domain=None, range=Optional[str])

slots.sediment_type = Slot(uri=ANALYSIS_API_SCHEMA.sediment_type, name="sediment_type", curie=ANALYSIS_API_SCHEMA.curie('sediment_type'),
                   model_uri=ANALYSIS_API_SCHEMA.sediment_type, domain=None, range=Optional[Union[str, "SedimentTypeEnum"]])

slots.sequence_order = Slot(uri=ANALYSIS_API_SCHEMA.sequence_order, name="sequence_order", curie=ANALYSIS_API_SCHEMA.curie('sequence_order'),
                   model_uri=ANALYSIS_API_SCHEMA.sequence_order, domain=None, range=Optional[int])

slots.setup_date = Slot(uri=ANALYSIS_API_SCHEMA.setup_date, name="setup_date", curie=ANALYSIS_API_SCHEMA.curie('setup_date'),
                   model_uri=ANALYSIS_API_SCHEMA.setup_date, domain=None, range=Union[str, XSDDateTime])

slots.setup_instrument = Slot(uri=ANALYSIS_API_SCHEMA.setup_instrument, name="setup_instrument", curie=ANALYSIS_API_SCHEMA.curie('setup_instrument'),
                   model_uri=ANALYSIS_API_SCHEMA.setup_instrument, domain=None, range=Optional[str])

slots.setup_operator_id = Slot(uri=ANALYSIS_API_SCHEMA.setup_operator_id, name="setup_operator_id", curie=ANALYSIS_API_SCHEMA.curie('setup_operator_id'),
                   model_uri=ANALYSIS_API_SCHEMA.setup_operator_id, domain=None, range=Optional[Union[str, PersonValueId]])

slots.sewage_type = Slot(uri=ANALYSIS_API_SCHEMA.sewage_type, name="sewage_type", curie=ANALYSIS_API_SCHEMA.curie('sewage_type'),
                   model_uri=ANALYSIS_API_SCHEMA.sewage_type, domain=None, range=Optional[str])

slots.shipped_sample_size = Slot(uri=ANALYSIS_API_SCHEMA.shipped_sample_size, name="shipped_sample_size", curie=ANALYSIS_API_SCHEMA.curie('shipped_sample_size'),
                   model_uri=ANALYSIS_API_SCHEMA.shipped_sample_size, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.sieving = Slot(uri=ANALYSIS_API_SCHEMA.sieving, name="sieving", curie=ANALYSIS_API_SCHEMA.curie('sieving'),
                   model_uri=ANALYSIS_API_SCHEMA.sieving, domain=None, range=Optional[str])

slots.silicate = Slot(uri=ANALYSIS_API_SCHEMA.silicate, name="silicate", curie=ANALYSIS_API_SCHEMA.curie('silicate'),
                   model_uri=ANALYSIS_API_SCHEMA.silicate, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*umol/L$'))

slots.size_frac_low = Slot(uri=ANALYSIS_API_SCHEMA.size_frac_low, name="size_frac_low", curie=ANALYSIS_API_SCHEMA.curie('size_frac_low'),
                   model_uri=ANALYSIS_API_SCHEMA.size_frac_low, domain=None, range=Optional[str])

slots.size_frac_up = Slot(uri=ANALYSIS_API_SCHEMA.size_frac_up, name="size_frac_up", curie=ANALYSIS_API_SCHEMA.curie('size_frac_up'),
                   model_uri=ANALYSIS_API_SCHEMA.size_frac_up, domain=None, range=Optional[str])

slots.slope_aspect = Slot(uri=ANALYSIS_API_SCHEMA.slope_aspect, name="slope_aspect", curie=ANALYSIS_API_SCHEMA.curie('slope_aspect'),
                   model_uri=ANALYSIS_API_SCHEMA.slope_aspect, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*degrees$'))

slots.slope_gradient = Slot(uri=ANALYSIS_API_SCHEMA.slope_gradient, name="slope_gradient", curie=ANALYSIS_API_SCHEMA.curie('slope_gradient'),
                   model_uri=ANALYSIS_API_SCHEMA.slope_gradient, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*percent$'))

slots.sludge_retent_time = Slot(uri=ANALYSIS_API_SCHEMA.sludge_retent_time, name="sludge_retent_time", curie=ANALYSIS_API_SCHEMA.curie('sludge_retent_time'),
                   model_uri=ANALYSIS_API_SCHEMA.sludge_retent_time, domain=None, range=Optional[str])

slots.sodium = Slot(uri=ANALYSIS_API_SCHEMA.sodium, name="sodium", curie=ANALYSIS_API_SCHEMA.curie('sodium'),
                   model_uri=ANALYSIS_API_SCHEMA.sodium, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*ug/mL$'))

slots.soil_horizon = Slot(uri=ANALYSIS_API_SCHEMA.soil_horizon, name="soil_horizon", curie=ANALYSIS_API_SCHEMA.curie('soil_horizon'),
                   model_uri=ANALYSIS_API_SCHEMA.soil_horizon, domain=None, range=Optional[Union[str, "SoilHorizonEnum"]])

slots.soil_sample_type = Slot(uri=ANALYSIS_API_SCHEMA.soil_sample_type, name="soil_sample_type", curie=ANALYSIS_API_SCHEMA.curie('soil_sample_type'),
                   model_uri=ANALYSIS_API_SCHEMA.soil_sample_type, domain=None, range=Optional[Union[str, "SoilSampleTypeEnum"]])

slots.soil_texture = Slot(uri=ANALYSIS_API_SCHEMA.soil_texture, name="soil_texture", curie=ANALYSIS_API_SCHEMA.curie('soil_texture'),
                   model_uri=ANALYSIS_API_SCHEMA.soil_texture, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(\w+:0\.\d+ )*description:[A-Za-z ]+$'))

slots.soil_type = Slot(uri=ANALYSIS_API_SCHEMA.soil_type, name="soil_type", curie=ANALYSIS_API_SCHEMA.curie('soil_type'),
                   model_uri=ANALYSIS_API_SCHEMA.soil_type, domain=None, range=Optional[Union[str, "SoilTypeEnum"]])

slots.soil_type_meth = Slot(uri=ANALYSIS_API_SCHEMA.soil_type_meth, name="soil_type_meth", curie=ANALYSIS_API_SCHEMA.curie('soil_type_meth'),
                   model_uri=ANALYSIS_API_SCHEMA.soil_type_meth, domain=None, range=Optional[str])

slots.solar_irradiance = Slot(uri=ANALYSIS_API_SCHEMA.solar_irradiance, name="solar_irradiance", curie=ANALYSIS_API_SCHEMA.curie('solar_irradiance'),
                   model_uri=ANALYSIS_API_SCHEMA.solar_irradiance, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(kW/m2/d|erg/cm2/s)$'))

slots.soluble_inorg_mat = Slot(uri=ANALYSIS_API_SCHEMA.soluble_inorg_mat, name="soluble_inorg_mat", curie=ANALYSIS_API_SCHEMA.curie('soluble_inorg_mat'),
                   model_uri=ANALYSIS_API_SCHEMA.soluble_inorg_mat, domain=None, range=Optional[str])

slots.soluble_org_mat = Slot(uri=ANALYSIS_API_SCHEMA.soluble_org_mat, name="soluble_org_mat", curie=ANALYSIS_API_SCHEMA.curie('soluble_org_mat'),
                   model_uri=ANALYSIS_API_SCHEMA.soluble_org_mat, domain=None, range=Optional[str])

slots.soluble_react_phosp = Slot(uri=ANALYSIS_API_SCHEMA.soluble_react_phosp, name="soluble_react_phosp", curie=ANALYSIS_API_SCHEMA.curie('soluble_react_phosp'),
                   model_uri=ANALYSIS_API_SCHEMA.soluble_react_phosp, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(umol/L|mg/L|ppm)$'))

slots.source_mat_id = Slot(uri=ANALYSIS_API_SCHEMA.source_mat_id, name="source_mat_id", curie=ANALYSIS_API_SCHEMA.curie('source_mat_id'),
                   model_uri=ANALYSIS_API_SCHEMA.source_mat_id, domain=None, range=Optional[str])

slots.specific_host = Slot(uri=ANALYSIS_API_SCHEMA.specific_host, name="specific_host", curie=ANALYSIS_API_SCHEMA.curie('specific_host'),
                   model_uri=ANALYSIS_API_SCHEMA.specific_host, domain=None, range=Optional[str])

slots.standing_water_regm = Slot(uri=ANALYSIS_API_SCHEMA.standing_water_regm, name="standing_water_regm", curie=ANALYSIS_API_SCHEMA.curie('standing_water_regm'),
                   model_uri=ANALYSIS_API_SCHEMA.standing_water_regm, domain=None, range=Optional[str])

slots.start_date_inc = Slot(uri=ANALYSIS_API_SCHEMA.start_date_inc, name="start_date_inc", curie=ANALYSIS_API_SCHEMA.curie('start_date_inc'),
                   model_uri=ANALYSIS_API_SCHEMA.start_date_inc, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$'))

slots.stationary_phase = Slot(uri=ANALYSIS_API_SCHEMA.stationary_phase, name="stationary_phase", curie=ANALYSIS_API_SCHEMA.curie('stationary_phase'),
                   model_uri=ANALYSIS_API_SCHEMA.stationary_phase, domain=None, range=Optional[str])

slots.sterilization_method = Slot(uri=ANALYSIS_API_SCHEMA.sterilization_method, name="sterilization_method", curie=ANALYSIS_API_SCHEMA.curie('sterilization_method'),
                   model_uri=ANALYSIS_API_SCHEMA.sterilization_method, domain=None, range=Optional[Union[str, "SterilizationMethodEnum"]])

slots.storage_condition = Slot(uri=ANALYSIS_API_SCHEMA.storage_condition, name="storage_condition", curie=ANALYSIS_API_SCHEMA.curie('storage_condition'),
                   model_uri=ANALYSIS_API_SCHEMA.storage_condition, domain=None, range=Optional[Union[str, "StorageConditionEnum"]])

slots.storage_condition_other = Slot(uri=ANALYSIS_API_SCHEMA.storage_condition_other, name="storage_condition_other", curie=ANALYSIS_API_SCHEMA.curie('storage_condition_other'),
                   model_uri=ANALYSIS_API_SCHEMA.storage_condition_other, domain=None, range=Optional[str])

slots.storage_location = Slot(uri=ANALYSIS_API_SCHEMA.storage_location, name="storage_location", curie=ANALYSIS_API_SCHEMA.curie('storage_location'),
                   model_uri=ANALYSIS_API_SCHEMA.storage_location, domain=None, range=Optional[str])

slots.storage_temperature = Slot(uri=ANALYSIS_API_SCHEMA.storage_temperature, name="storage_temperature", curie=ANALYSIS_API_SCHEMA.curie('storage_temperature'),
                   model_uri=ANALYSIS_API_SCHEMA.storage_temperature, domain=None, range=Optional[str])

slots.strain_description = Slot(uri=ANALYSIS_API_SCHEMA.strain_description, name="strain_description", curie=ANALYSIS_API_SCHEMA.curie('strain_description'),
                   model_uri=ANALYSIS_API_SCHEMA.strain_description, domain=None, range=Optional[str])

slots.strain_identifier = Slot(uri=ANALYSIS_API_SCHEMA.strain_identifier, name="strain_identifier", curie=ANALYSIS_API_SCHEMA.curie('strain_identifier'),
                   model_uri=ANALYSIS_API_SCHEMA.strain_identifier, domain=None, range=str)

slots.strain_mutation = Slot(uri=ANALYSIS_API_SCHEMA.strain_mutation, name="strain_mutation", curie=ANALYSIS_API_SCHEMA.curie('strain_mutation'),
                   model_uri=ANALYSIS_API_SCHEMA.strain_mutation, domain=None, range=Optional[str])

slots.strain_name = Slot(uri=ANALYSIS_API_SCHEMA.strain_name, name="strain_name", curie=ANALYSIS_API_SCHEMA.curie('strain_name'),
                   model_uri=ANALYSIS_API_SCHEMA.strain_name, domain=None, range=Optional[str])

slots.strain_ref = Slot(uri=ANALYSIS_API_SCHEMA.strain_ref, name="strain_ref", curie=ANALYSIS_API_SCHEMA.curie('strain_ref'),
                   model_uri=ANALYSIS_API_SCHEMA.strain_ref, domain=None, range=Optional[Union[str, BiologicalEntityId]])

slots.strain_source = Slot(uri=ANALYSIS_API_SCHEMA.strain_source, name="strain_source", curie=ANALYSIS_API_SCHEMA.curie('strain_source'),
                   model_uri=ANALYSIS_API_SCHEMA.strain_source, domain=None, range=Optional[str])

slots.strain_type = Slot(uri=ANALYSIS_API_SCHEMA.strain_type, name="strain_type", curie=ANALYSIS_API_SCHEMA.curie('strain_type'),
                   model_uri=ANALYSIS_API_SCHEMA.strain_type, domain=None, range=Optional[Union[str, "StrainTypeEnum"]])

slots.subspecf_gen_lin = Slot(uri=ANALYSIS_API_SCHEMA.subspecf_gen_lin, name="subspecf_gen_lin", curie=ANALYSIS_API_SCHEMA.curie('subspecf_gen_lin'),
                   model_uri=ANALYSIS_API_SCHEMA.subspecf_gen_lin, domain=None, range=Optional[str])

slots.sulfate = Slot(uri=ANALYSIS_API_SCHEMA.sulfate, name="sulfate", curie=ANALYSIS_API_SCHEMA.curie('sulfate'),
                   model_uri=ANALYSIS_API_SCHEMA.sulfate, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(umol/L|mg/L|ppm)$'))

slots.sulfide = Slot(uri=ANALYSIS_API_SCHEMA.sulfide, name="sulfide", curie=ANALYSIS_API_SCHEMA.curie('sulfide'),
                   model_uri=ANALYSIS_API_SCHEMA.sulfide, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(umol/L|mg/L|ppm)$'))

slots.summary_metrics = Slot(uri=ANALYSIS_API_SCHEMA.summary_metrics, name="summary_metrics", curie=ANALYSIS_API_SCHEMA.curie('summary_metrics'),
                   model_uri=ANALYSIS_API_SCHEMA.summary_metrics, domain=None, range=Optional[str])

slots.suspend_part_matter = Slot(uri=ANALYSIS_API_SCHEMA.suspend_part_matter, name="suspend_part_matter", curie=ANALYSIS_API_SCHEMA.curie('suspend_part_matter'),
                   model_uri=ANALYSIS_API_SCHEMA.suspend_part_matter, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(mg/L)$'))

slots.suspend_solids = Slot(uri=ANALYSIS_API_SCHEMA.suspend_solids, name="suspend_solids", curie=ANALYSIS_API_SCHEMA.curie('suspend_solids'),
                   model_uri=ANALYSIS_API_SCHEMA.suspend_solids, domain=None, range=Optional[str])

slots.synth_env_assembly = Slot(uri=ANALYSIS_API_SCHEMA.synth_env_assembly, name="synth_env_assembly", curie=ANALYSIS_API_SCHEMA.curie('synth_env_assembly'),
                   model_uri=ANALYSIS_API_SCHEMA.synth_env_assembly, domain=None, range=Optional[str])

slots.synth_env_design = Slot(uri=ANALYSIS_API_SCHEMA.synth_env_design, name="synth_env_design", curie=ANALYSIS_API_SCHEMA.curie('synth_env_design'),
                   model_uri=ANALYSIS_API_SCHEMA.synth_env_design, domain=None, range=Optional[Union[str, "SyntheticEnvironmentEnum"]])

slots.synth_env_design_method = Slot(uri=ANALYSIS_API_SCHEMA.synth_env_design_method, name="synth_env_design_method", curie=ANALYSIS_API_SCHEMA.curie('synth_env_design_method'),
                   model_uri=ANALYSIS_API_SCHEMA.synth_env_design_method, domain=None, range=Optional[str])

slots.synth_env_material = Slot(uri=ANALYSIS_API_SCHEMA.synth_env_material, name="synth_env_material", curie=ANALYSIS_API_SCHEMA.curie('synth_env_material'),
                   model_uri=ANALYSIS_API_SCHEMA.synth_env_material, domain=None, range=Optional[str])

slots.synth_env_treatment = Slot(uri=ANALYSIS_API_SCHEMA.synth_env_treatment, name="synth_env_treatment", curie=ANALYSIS_API_SCHEMA.curie('synth_env_treatment'),
                   model_uri=ANALYSIS_API_SCHEMA.synth_env_treatment, domain=None, range=Optional[str])

slots.synth_instrument = Slot(uri=ANALYSIS_API_SCHEMA.synth_instrument, name="synth_instrument", curie=ANALYSIS_API_SCHEMA.curie('synth_instrument'),
                   model_uri=ANALYSIS_API_SCHEMA.synth_instrument, domain=None, range=Optional[str])

slots.synth_process = Slot(uri=ANALYSIS_API_SCHEMA.synth_process, name="synth_process", curie=ANALYSIS_API_SCHEMA.curie('synth_process'),
                   model_uri=ANALYSIS_API_SCHEMA.synth_process, domain=None, range=Optional[str])

slots.synth_reagents = Slot(uri=ANALYSIS_API_SCHEMA.synth_reagents, name="synth_reagents", curie=ANALYSIS_API_SCHEMA.curie('synth_reagents'),
                   model_uri=ANALYSIS_API_SCHEMA.synth_reagents, domain=None, range=Optional[str])

slots.synth_start_date = Slot(uri=ANALYSIS_API_SCHEMA.synth_start_date, name="synth_start_date", curie=ANALYSIS_API_SCHEMA.curie('synth_start_date'),
                   model_uri=ANALYSIS_API_SCHEMA.synth_start_date, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$'))

slots.target_strain = Slot(uri=ANALYSIS_API_SCHEMA.target_strain, name="target_strain", curie=ANALYSIS_API_SCHEMA.curie('target_strain'),
                   model_uri=ANALYSIS_API_SCHEMA.target_strain, domain=None, range=Optional[str])

slots.taxonomy_id = Slot(uri=ANALYSIS_API_SCHEMA.taxonomy_id, name="taxonomy_id", curie=ANALYSIS_API_SCHEMA.curie('taxonomy_id'),
                   model_uri=ANALYSIS_API_SCHEMA.taxonomy_id, domain=None, range=Optional[str])

slots.technical_reps = Slot(uri=ANALYSIS_API_SCHEMA.technical_reps, name="technical_reps", curie=ANALYSIS_API_SCHEMA.curie('technical_reps'),
                   model_uri=ANALYSIS_API_SCHEMA.technical_reps, domain=None, range=Optional[int])

slots.temp = Slot(uri=ANALYSIS_API_SCHEMA.temp, name="temp", curie=ANALYSIS_API_SCHEMA.curie('temp'),
                   model_uri=ANALYSIS_API_SCHEMA.temp, domain=None, range=Optional[str],
                   pattern=re.compile(r'^-?\d+(\.\d+)?\s*C$'))

slots.temperature_celsius = Slot(uri=ANALYSIS_API_SCHEMA.temperature_celsius, name="temperature_celsius", curie=ANALYSIS_API_SCHEMA.curie('temperature_celsius'),
                   model_uri=ANALYSIS_API_SCHEMA.temperature_celsius, domain=None, range=Optional[float])

slots.temperature_exposure = Slot(uri=ANALYSIS_API_SCHEMA.temperature_exposure, name="temperature_exposure", curie=ANALYSIS_API_SCHEMA.curie('temperature_exposure'),
                   model_uri=ANALYSIS_API_SCHEMA.temperature_exposure, domain=None, range=Optional[str])

slots.tertiary_treatment = Slot(uri=ANALYSIS_API_SCHEMA.tertiary_treatment, name="tertiary_treatment", curie=ANALYSIS_API_SCHEMA.curie('tertiary_treatment'),
                   model_uri=ANALYSIS_API_SCHEMA.tertiary_treatment, domain=None, range=Optional[str])

slots.texture_meth = Slot(uri=ANALYSIS_API_SCHEMA.texture_meth, name="texture_meth", curie=ANALYSIS_API_SCHEMA.curie('texture_meth'),
                   model_uri=ANALYSIS_API_SCHEMA.texture_meth, domain=None, range=Optional[str])

slots.third_blh = Slot(uri=ANALYSIS_API_SCHEMA.third_blh, name="third_blh", curie=ANALYSIS_API_SCHEMA.curie('third_blh'),
                   model_uri=ANALYSIS_API_SCHEMA.third_blh, domain=None, range=Optional[float])

slots.third_blh_quality = Slot(uri=ANALYSIS_API_SCHEMA.third_blh_quality, name="third_blh_quality", curie=ANALYSIS_API_SCHEMA.curie('third_blh_quality'),
                   model_uri=ANALYSIS_API_SCHEMA.third_blh_quality, domain=None, range=Optional[str])

slots.tidal_stage = Slot(uri=ANALYSIS_API_SCHEMA.tidal_stage, name="tidal_stage", curie=ANALYSIS_API_SCHEMA.curie('tidal_stage'),
                   model_uri=ANALYSIS_API_SCHEMA.tidal_stage, domain=None, range=Optional[Union[str, "TidalStageEnum"]])

slots.tillage = Slot(uri=ANALYSIS_API_SCHEMA.tillage, name="tillage", curie=ANALYSIS_API_SCHEMA.curie('tillage'),
                   model_uri=ANALYSIS_API_SCHEMA.tillage, domain=None, range=Optional[Union[str, "TillageEnum"]])

slots.timepoint_label = Slot(uri=ANALYSIS_API_SCHEMA.timepoint_label, name="timepoint_label", curie=ANALYSIS_API_SCHEMA.curie('timepoint_label'),
                   model_uri=ANALYSIS_API_SCHEMA.timepoint_label, domain=None, range=str)

slots.tiss_cult_growth_med = Slot(uri=ANALYSIS_API_SCHEMA.tiss_cult_growth_med, name="tiss_cult_growth_med", curie=ANALYSIS_API_SCHEMA.curie('tiss_cult_growth_med'),
                   model_uri=ANALYSIS_API_SCHEMA.tiss_cult_growth_med, domain=None, range=Optional[str])

slots.tot_carb = Slot(uri=ANALYSIS_API_SCHEMA.tot_carb, name="tot_carb", curie=ANALYSIS_API_SCHEMA.curie('tot_carb'),
                   model_uri=ANALYSIS_API_SCHEMA.tot_carb, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.tot_depth_water_col = Slot(uri=ANALYSIS_API_SCHEMA.tot_depth_water_col, name="tot_depth_water_col", curie=ANALYSIS_API_SCHEMA.curie('tot_depth_water_col'),
                   model_uri=ANALYSIS_API_SCHEMA.tot_depth_water_col, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*m$'))

slots.tot_diss_nitro = Slot(uri=ANALYSIS_API_SCHEMA.tot_diss_nitro, name="tot_diss_nitro", curie=ANALYSIS_API_SCHEMA.curie('tot_diss_nitro'),
                   model_uri=ANALYSIS_API_SCHEMA.tot_diss_nitro, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(ug/L)$'))

slots.tot_inorg_nitro = Slot(uri=ANALYSIS_API_SCHEMA.tot_inorg_nitro, name="tot_inorg_nitro", curie=ANALYSIS_API_SCHEMA.curie('tot_inorg_nitro'),
                   model_uri=ANALYSIS_API_SCHEMA.tot_inorg_nitro, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(ug/L)$'))

slots.tot_nitro = Slot(uri=ANALYSIS_API_SCHEMA.tot_nitro, name="tot_nitro", curie=ANALYSIS_API_SCHEMA.curie('tot_nitro'),
                   model_uri=ANALYSIS_API_SCHEMA.tot_nitro, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(ug/L|umol/L|mg/L)$'))

slots.tot_nitro_cont_meth = Slot(uri=ANALYSIS_API_SCHEMA.tot_nitro_cont_meth, name="tot_nitro_cont_meth", curie=ANALYSIS_API_SCHEMA.curie('tot_nitro_cont_meth'),
                   model_uri=ANALYSIS_API_SCHEMA.tot_nitro_cont_meth, domain=None, range=Optional[str])

slots.tot_nitro_content = Slot(uri=ANALYSIS_API_SCHEMA.tot_nitro_content, name="tot_nitro_content", curie=ANALYSIS_API_SCHEMA.curie('tot_nitro_content'),
                   model_uri=ANALYSIS_API_SCHEMA.tot_nitro_content, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.tot_org_c_meth = Slot(uri=ANALYSIS_API_SCHEMA.tot_org_c_meth, name="tot_org_c_meth", curie=ANALYSIS_API_SCHEMA.curie('tot_org_c_meth'),
                   model_uri=ANALYSIS_API_SCHEMA.tot_org_c_meth, domain=None, range=Optional[str])

slots.tot_org_carb = Slot(uri=ANALYSIS_API_SCHEMA.tot_org_carb, name="tot_org_carb", curie=ANALYSIS_API_SCHEMA.curie('tot_org_carb'),
                   model_uri=ANALYSIS_API_SCHEMA.tot_org_carb, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*g C/kg$'))

slots.tot_part_carb = Slot(uri=ANALYSIS_API_SCHEMA.tot_part_carb, name="tot_part_carb", curie=ANALYSIS_API_SCHEMA.curie('tot_part_carb'),
                   model_uri=ANALYSIS_API_SCHEMA.tot_part_carb, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(ug/L|umol/L)$'))

slots.tot_phosp = Slot(uri=ANALYSIS_API_SCHEMA.tot_phosp, name="tot_phosp", curie=ANALYSIS_API_SCHEMA.curie('tot_phosp'),
                   model_uri=ANALYSIS_API_SCHEMA.tot_phosp, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(ug/L|umol/L)$'))

slots.tot_phosphate = Slot(uri=ANALYSIS_API_SCHEMA.tot_phosphate, name="tot_phosphate", curie=ANALYSIS_API_SCHEMA.curie('tot_phosphate'),
                   model_uri=ANALYSIS_API_SCHEMA.tot_phosphate, domain=None, range=Optional[str])

slots.total_amount_ug = Slot(uri=ANALYSIS_API_SCHEMA.total_amount_ug, name="total_amount_ug", curie=ANALYSIS_API_SCHEMA.curie('total_amount_ug'),
                   model_uri=ANALYSIS_API_SCHEMA.total_amount_ug, domain=None, range=Optional[float])

slots.trait = Slot(uri=ANALYSIS_API_SCHEMA.trait, name="trait", curie=ANALYSIS_API_SCHEMA.curie('trait'),
                   model_uri=ANALYSIS_API_SCHEMA.trait, domain=None, range=Optional[Union[str, "IntendedTraitEnum"]])

slots.treatment_type = Slot(uri=ANALYSIS_API_SCHEMA.treatment_type, name="treatment_type", curie=ANALYSIS_API_SCHEMA.curie('treatment_type'),
                   model_uri=ANALYSIS_API_SCHEMA.treatment_type, domain=None, range=Optional[str])

slots.trophic_level = Slot(uri=ANALYSIS_API_SCHEMA.trophic_level, name="trophic_level", curie=ANALYSIS_API_SCHEMA.curie('trophic_level'),
                   model_uri=ANALYSIS_API_SCHEMA.trophic_level, domain=None, range=Optional[Union[str, "TrophicLevelEnum"]])

slots.turbidity = Slot(uri=ANALYSIS_API_SCHEMA.turbidity, name="turbidity", curie=ANALYSIS_API_SCHEMA.curie('turbidity'),
                   model_uri=ANALYSIS_API_SCHEMA.turbidity, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.uninoculated_mean = Slot(uri=ANALYSIS_API_SCHEMA.uninoculated_mean, name="uninoculated_mean", curie=ANALYSIS_API_SCHEMA.curie('uninoculated_mean'),
                   model_uri=ANALYSIS_API_SCHEMA.uninoculated_mean, domain=None, range=Optional[float])

slots.uses_calibration = Slot(uri=ANALYSIS_API_SCHEMA.uses_calibration, name="uses_calibration", curie=ANALYSIS_API_SCHEMA.curie('uses_calibration'),
                   model_uri=ANALYSIS_API_SCHEMA.uses_calibration, domain=None, range=Optional[Union[str, MassSpectrometryStandardRunId]])

slots.uses_chromatography = Slot(uri=ANALYSIS_API_SCHEMA.uses_chromatography, name="uses_chromatography", curie=ANALYSIS_API_SCHEMA.curie('uses_chromatography'),
                   model_uri=ANALYSIS_API_SCHEMA.uses_chromatography, domain=None, range=Optional[Union[dict, ChromatographyConfiguration]])

slots.uses_ms_configuration = Slot(uri=ANALYSIS_API_SCHEMA.uses_ms_configuration, name="uses_ms_configuration", curie=ANALYSIS_API_SCHEMA.curie('uses_ms_configuration'),
                   model_uri=ANALYSIS_API_SCHEMA.uses_ms_configuration, domain=None, range=Union[dict, MassSpectrometryConfiguration])

slots.uses_raw_ms_data = Slot(uri=ANALYSIS_API_SCHEMA.uses_raw_ms_data, name="uses_raw_ms_data", curie=ANALYSIS_API_SCHEMA.curie('uses_raw_ms_data'),
                   model_uri=ANALYSIS_API_SCHEMA.uses_raw_ms_data, domain=None, range=Optional[Union[str, MassSpectrometryInstrumentDataId]])

slots.version = Slot(uri=ANALYSIS_API_SCHEMA.version, name="version", curie=ANALYSIS_API_SCHEMA.curie('version'),
                   model_uri=ANALYSIS_API_SCHEMA.version, domain=None, range=str)

slots.volatile_org_comp = Slot(uri=ANALYSIS_API_SCHEMA.volatile_org_comp, name="volatile_org_comp", curie=ANALYSIS_API_SCHEMA.curie('volatile_org_comp'),
                   model_uri=ANALYSIS_API_SCHEMA.volatile_org_comp, domain=None, range=Optional[str])

slots.volume_ml = Slot(uri=ANALYSIS_API_SCHEMA.volume_ml, name="volume_ml", curie=ANALYSIS_API_SCHEMA.curie('volume_ml'),
                   model_uri=ANALYSIS_API_SCHEMA.volume_ml, domain=None, range=Optional[float])

slots.volume_uL = Slot(uri=ANALYSIS_API_SCHEMA.volume_uL, name="volume_uL", curie=ANALYSIS_API_SCHEMA.curie('volume_uL'),
                   model_uri=ANALYSIS_API_SCHEMA.volume_uL, domain=None, range=Optional[float])

slots.wastewater_type = Slot(uri=ANALYSIS_API_SCHEMA.wastewater_type, name="wastewater_type", curie=ANALYSIS_API_SCHEMA.curie('wastewater_type'),
                   model_uri=ANALYSIS_API_SCHEMA.wastewater_type, domain=None, range=Optional[str])

slots.water_content = Slot(uri=ANALYSIS_API_SCHEMA.water_content, name="water_content", curie=ANALYSIS_API_SCHEMA.curie('water_content'),
                   model_uri=ANALYSIS_API_SCHEMA.water_content, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.water_content_meth = Slot(uri=ANALYSIS_API_SCHEMA.water_content_meth, name="water_content_meth", curie=ANALYSIS_API_SCHEMA.curie('water_content_meth'),
                   model_uri=ANALYSIS_API_SCHEMA.water_content_meth, domain=None, range=Optional[str])

slots.water_current = Slot(uri=ANALYSIS_API_SCHEMA.water_current, name="water_current", curie=ANALYSIS_API_SCHEMA.curie('water_current'),
                   model_uri=ANALYSIS_API_SCHEMA.water_current, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.water_temp_regm = Slot(uri=ANALYSIS_API_SCHEMA.water_temp_regm, name="water_temp_regm", curie=ANALYSIS_API_SCHEMA.curie('water_temp_regm'),
                   model_uri=ANALYSIS_API_SCHEMA.water_temp_regm, domain=None, range=Optional[str])

slots.watering_regm = Slot(uri=ANALYSIS_API_SCHEMA.watering_regm, name="watering_regm", curie=ANALYSIS_API_SCHEMA.curie('watering_regm'),
                   model_uri=ANALYSIS_API_SCHEMA.watering_regm, domain=None, range=Optional[str])

slots.wavelength_nm = Slot(uri=ANALYSIS_API_SCHEMA.wavelength_nm, name="wavelength_nm", curie=ANALYSIS_API_SCHEMA.curie('wavelength_nm'),
                   model_uri=ANALYSIS_API_SCHEMA.wavelength_nm, domain=None, range=int)

slots.weather = Slot(uri=ANALYSIS_API_SCHEMA.weather, name="weather", curie=ANALYSIS_API_SCHEMA.curie('weather'),
                   model_uri=ANALYSIS_API_SCHEMA.weather, domain=None, range=Optional[str])

slots.well_metadata = Slot(uri=ANALYSIS_API_SCHEMA.well_metadata, name="well_metadata", curie=ANALYSIS_API_SCHEMA.curie('well_metadata'),
                   model_uri=ANALYSIS_API_SCHEMA.well_metadata, domain=None, range=Optional[Union[Union[dict, WellMetadata], list[Union[dict, WellMetadata]]]])

slots.well_readings = Slot(uri=ANALYSIS_API_SCHEMA.well_readings, name="well_readings", curie=ANALYSIS_API_SCHEMA.curie('well_readings'),
                   model_uri=ANALYSIS_API_SCHEMA.well_readings, domain=None, range=Optional[Union[Union[dict, WellReading], list[Union[dict, WellReading]]]])

slots.wind_direction = Slot(uri=ANALYSIS_API_SCHEMA.wind_direction, name="wind_direction", curie=ANALYSIS_API_SCHEMA.curie('wind_direction'),
                   model_uri=ANALYSIS_API_SCHEMA.wind_direction, domain=None, range=Optional[Union[str, "CardinalDirectionEnum"]])

slots.wind_speed = Slot(uri=ANALYSIS_API_SCHEMA.wind_speed, name="wind_speed", curie=ANALYSIS_API_SCHEMA.curie('wind_speed'),
                   model_uri=ANALYSIS_API_SCHEMA.wind_speed, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.within_17_oz = Slot(uri=ANALYSIS_API_SCHEMA.within_17_oz, name="within_17_oz", curie=ANALYSIS_API_SCHEMA.curie('within_17_oz'),
                   model_uri=ANALYSIS_API_SCHEMA.within_17_oz, domain=None, range=Optional[str])

slots.workflow_steps = Slot(uri=ANALYSIS_API_SCHEMA.workflow_steps, name="workflow_steps", curie=ANALYSIS_API_SCHEMA.curie('workflow_steps'),
                   model_uri=ANALYSIS_API_SCHEMA.workflow_steps, domain=None, range=Optional[str])

slots.activity__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="activity__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.activity__id, domain=None, range=URIRef)

slots.activity__ended_at_time = Slot(uri=ANALYSIS_API_SCHEMA.ended_at_time, name="activity__ended_at_time", curie=ANALYSIS_API_SCHEMA.curie('ended_at_time'),
                   model_uri=ANALYSIS_API_SCHEMA.activity__ended_at_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.activity__processing_institution = Slot(uri=ANALYSIS_API_SCHEMA.processing_institution, name="activity__processing_institution", curie=ANALYSIS_API_SCHEMA.curie('processing_institution'),
                   model_uri=ANALYSIS_API_SCHEMA.activity__processing_institution, domain=None, range=Optional[Union[str, "InstitutionEnum"]])

slots.activity__protocol_link = Slot(uri=ANALYSIS_API_SCHEMA.protocol_link, name="activity__protocol_link", curie=ANALYSIS_API_SCHEMA.curie('protocol_link'),
                   model_uri=ANALYSIS_API_SCHEMA.activity__protocol_link, domain=None, range=Optional[str])

slots.activity__started_at_time = Slot(uri=ANALYSIS_API_SCHEMA.started_at_time, name="activity__started_at_time", curie=ANALYSIS_API_SCHEMA.curie('started_at_time'),
                   model_uri=ANALYSIS_API_SCHEMA.activity__started_at_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.entity__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="entity__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.entity__id, domain=None, range=URIRef)

slots.dataProduct__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="dataProduct__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.dataProduct__id, domain=None, range=URIRef)

slots.instrumentData__alternative_identifiers = Slot(uri=ANALYSIS_API_SCHEMA.alternative_identifiers, name="instrumentData__alternative_identifiers", curie=ANALYSIS_API_SCHEMA.curie('alternative_identifiers'),
                   model_uri=ANALYSIS_API_SCHEMA.instrumentData__alternative_identifiers, domain=None, range=Optional[str])

slots.instrumentData__compression_type = Slot(uri=ANALYSIS_API_SCHEMA.compression_type, name="instrumentData__compression_type", curie=ANALYSIS_API_SCHEMA.curie('compression_type'),
                   model_uri=ANALYSIS_API_SCHEMA.instrumentData__compression_type, domain=None, range=Optional[str])

slots.instrumentData__file_type = Slot(uri=ANALYSIS_API_SCHEMA.file_type, name="instrumentData__file_type", curie=ANALYSIS_API_SCHEMA.curie('file_type'),
                   model_uri=ANALYSIS_API_SCHEMA.instrumentData__file_type, domain=None, range=Optional[Union[str, "FileTypeEnum"]])

slots.instrumentData__software_version = Slot(uri=ANALYSIS_API_SCHEMA.software_version, name="instrumentData__software_version", curie=ANALYSIS_API_SCHEMA.curie('software_version'),
                   model_uri=ANALYSIS_API_SCHEMA.instrumentData__software_version, domain=None, range=Optional[str])

slots.sitePhoto__site_photo_type = Slot(uri=ANALYSIS_API_SCHEMA.site_photo_type, name="sitePhoto__site_photo_type", curie=ANALYSIS_API_SCHEMA.curie('site_photo_type'),
                   model_uri=ANALYSIS_API_SCHEMA.sitePhoto__site_photo_type, domain=None, range=Optional[Union[str, "SitePhotoCategoryEnum"]])

slots.sitePhoto__photo_taken_during = Slot(uri=ANALYSIS_API_SCHEMA.photo_taken_during, name="sitePhoto__photo_taken_during", curie=ANALYSIS_API_SCHEMA.curie('photo_taken_during'),
                   model_uri=ANALYSIS_API_SCHEMA.sitePhoto__photo_taken_during, domain=None, range=Optional[Union[str, SamplingActivityId]])

slots.dataGenerationActivity__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="dataGenerationActivity__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.dataGenerationActivity__id, domain=None, range=URIRef)

slots.dataGenerationActivity__analyte_id = Slot(uri=ANALYSIS_API_SCHEMA.analyte_id, name="dataGenerationActivity__analyte_id", curie=ANALYSIS_API_SCHEMA.curie('analyte_id'),
                   model_uri=ANALYSIS_API_SCHEMA.dataGenerationActivity__analyte_id, domain=None, range=Optional[Union[str, ProcessedSampleId]])

slots.dataGenerationActivity__acquisition_start_time = Slot(uri=ANALYSIS_API_SCHEMA.acquisition_start_time, name="dataGenerationActivity__acquisition_start_time", curie=ANALYSIS_API_SCHEMA.curie('acquisition_start_time'),
                   model_uri=ANALYSIS_API_SCHEMA.dataGenerationActivity__acquisition_start_time, domain=None, range=Union[str, XSDDateTime])

slots.dataGenerationActivity__acquisition_end_time = Slot(uri=ANALYSIS_API_SCHEMA.acquisition_end_time, name="dataGenerationActivity__acquisition_end_time", curie=ANALYSIS_API_SCHEMA.curie('acquisition_end_time'),
                   model_uri=ANALYSIS_API_SCHEMA.dataGenerationActivity__acquisition_end_time, domain=None, range=Union[str, XSDDateTime])

slots.dataGenerationActivity__instrument_used = Slot(uri=ANALYSIS_API_SCHEMA.instrument_used, name="dataGenerationActivity__instrument_used", curie=ANALYSIS_API_SCHEMA.curie('instrument_used'),
                   model_uri=ANALYSIS_API_SCHEMA.dataGenerationActivity__instrument_used, domain=None, range=Optional[Union[str, InstrumentId]])

slots.dataGenerationActivity__instrument_operator_id = Slot(uri=ANALYSIS_API_SCHEMA.instrument_operator_id, name="dataGenerationActivity__instrument_operator_id", curie=ANALYSIS_API_SCHEMA.curie('instrument_operator_id'),
                   model_uri=ANALYSIS_API_SCHEMA.dataGenerationActivity__instrument_operator_id, domain=None, range=Optional[Union[str, PersonValueId]])

slots.respirationDataGenerationActivity__method_id = Slot(uri=ANALYSIS_API_SCHEMA.method_id, name="respirationDataGenerationActivity__method_id", curie=ANALYSIS_API_SCHEMA.curie('method_id'),
                   model_uri=ANALYSIS_API_SCHEMA.respirationDataGenerationActivity__method_id, domain=None, range=Optional[Union[dict, RespirationMethod]])

slots.dataProcessingActivity__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="dataProcessingActivity__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.dataProcessingActivity__id, domain=None, range=URIRef)

slots.dataProcessingActivity__started_at_time = Slot(uri=ANALYSIS_API_SCHEMA.started_at_time, name="dataProcessingActivity__started_at_time", curie=ANALYSIS_API_SCHEMA.curie('started_at_time'),
                   model_uri=ANALYSIS_API_SCHEMA.dataProcessingActivity__started_at_time, domain=None, range=Union[str, XSDDateTime])

slots.dataProcessingActivity__ended_at_time = Slot(uri=ANALYSIS_API_SCHEMA.ended_at_time, name="dataProcessingActivity__ended_at_time", curie=ANALYSIS_API_SCHEMA.curie('ended_at_time'),
                   model_uri=ANALYSIS_API_SCHEMA.dataProcessingActivity__ended_at_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.dataProcessingActivity__software_url = Slot(uri=ANALYSIS_API_SCHEMA.software_url, name="dataProcessingActivity__software_url", curie=ANALYSIS_API_SCHEMA.curie('software_url'),
                   model_uri=ANALYSIS_API_SCHEMA.dataProcessingActivity__software_url, domain=None, range=Optional[str])

slots.dataProcessingActivity__software_version = Slot(uri=ANALYSIS_API_SCHEMA.software_version, name="dataProcessingActivity__software_version", curie=ANALYSIS_API_SCHEMA.curie('software_version'),
                   model_uri=ANALYSIS_API_SCHEMA.dataProcessingActivity__software_version, domain=None, range=Optional[str])

slots.dataProcessingActivity__software_poc = Slot(uri=ANALYSIS_API_SCHEMA.software_poc, name="dataProcessingActivity__software_poc", curie=ANALYSIS_API_SCHEMA.curie('software_poc'),
                   model_uri=ANALYSIS_API_SCHEMA.dataProcessingActivity__software_poc, domain=None, range=Optional[str])

slots.dataProcessingActivity__execution_resource = Slot(uri=ANALYSIS_API_SCHEMA.execution_resource, name="dataProcessingActivity__execution_resource", curie=ANALYSIS_API_SCHEMA.curie('execution_resource'),
                   model_uri=ANALYSIS_API_SCHEMA.dataProcessingActivity__execution_resource, domain=None, range=Optional[Union[str, "ExecutionResourceEnum"]])

slots.alternativeIdentifier__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="alternativeIdentifier__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.alternativeIdentifier__id, domain=None, range=URIRef)

slots.alternativeIdentifier__alternate_id = Slot(uri=ANALYSIS_API_SCHEMA.alternate_id, name="alternativeIdentifier__alternate_id", curie=ANALYSIS_API_SCHEMA.curie('alternate_id'),
                   model_uri=ANALYSIS_API_SCHEMA.alternativeIdentifier__alternate_id, domain=None, range=str)

slots.alternativeIdentifier__alternate_identifier_type = Slot(uri=ANALYSIS_API_SCHEMA.alternate_identifier_type, name="alternativeIdentifier__alternate_identifier_type", curie=ANALYSIS_API_SCHEMA.curie('alternate_identifier_type'),
                   model_uri=ANALYSIS_API_SCHEMA.alternativeIdentifier__alternate_identifier_type, domain=None, range=Union[str, "AlternateIdentifierType"])

slots.functionalAnnotationIdentifier__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="functionalAnnotationIdentifier__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.functionalAnnotationIdentifier__id, domain=None, range=URIRef)

slots.functionalAnnotationIdentifier__functional_identifier = Slot(uri=ANALYSIS_API_SCHEMA.functional_identifier, name="functionalAnnotationIdentifier__functional_identifier", curie=ANALYSIS_API_SCHEMA.curie('functional_identifier'),
                   model_uri=ANALYSIS_API_SCHEMA.functionalAnnotationIdentifier__functional_identifier, domain=None, range=str)

slots.functionalAnnotationIdentifier__database = Slot(uri=ANALYSIS_API_SCHEMA.database, name="functionalAnnotationIdentifier__database", curie=ANALYSIS_API_SCHEMA.curie('database'),
                   model_uri=ANALYSIS_API_SCHEMA.functionalAnnotationIdentifier__database, domain=None, range=Union[str, "AnnotationDatabaseEnum"])

slots.instrument__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="instrument__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.instrument__id, domain=None, range=URIRef)

slots.instrument__name = Slot(uri=ANALYSIS_API_SCHEMA.name, name="instrument__name", curie=ANALYSIS_API_SCHEMA.curie('name'),
                   model_uri=ANALYSIS_API_SCHEMA.instrument__name, domain=None, range=str)

slots.instrument__vendor = Slot(uri=ANALYSIS_API_SCHEMA.vendor, name="instrument__vendor", curie=ANALYSIS_API_SCHEMA.curie('vendor'),
                   model_uri=ANALYSIS_API_SCHEMA.instrument__vendor, domain=None, range=Optional[Union[str, "VendorEnum"]])

slots.instrument__model = Slot(uri=ANALYSIS_API_SCHEMA.model, name="instrument__model", curie=ANALYSIS_API_SCHEMA.curie('model'),
                   model_uri=ANALYSIS_API_SCHEMA.instrument__model, domain=None, range=Optional[Union[str, "ModelEnum"]])

slots.instrument__serial_number = Slot(uri=ANALYSIS_API_SCHEMA.serial_number, name="instrument__serial_number", curie=ANALYSIS_API_SCHEMA.curie('serial_number'),
                   model_uri=ANALYSIS_API_SCHEMA.instrument__serial_number, domain=None, range=Optional[str])

slots.instrument__lims_resource_id = Slot(uri=ANALYSIS_API_SCHEMA.lims_resource_id, name="instrument__lims_resource_id", curie=ANALYSIS_API_SCHEMA.curie('lims_resource_id'),
                   model_uri=ANALYSIS_API_SCHEMA.instrument__lims_resource_id, domain=None, range=Optional[int])

slots.instrument__location = Slot(uri=ANALYSIS_API_SCHEMA.location, name="instrument__location", curie=ANALYSIS_API_SCHEMA.curie('location'),
                   model_uri=ANALYSIS_API_SCHEMA.instrument__location, domain=None, range=Optional[str])

slots.instrument__maintenance = Slot(uri=ANALYSIS_API_SCHEMA.maintenance, name="instrument__maintenance", curie=ANALYSIS_API_SCHEMA.curie('maintenance'),
                   model_uri=ANALYSIS_API_SCHEMA.instrument__maintenance, domain=None, range=Optional[str])

slots.instrument__alternative_names = Slot(uri=ANALYSIS_API_SCHEMA.alternative_names, name="instrument__alternative_names", curie=ANALYSIS_API_SCHEMA.curie('alternative_names'),
                   model_uri=ANALYSIS_API_SCHEMA.instrument__alternative_names, domain=None, range=Optional[str])

slots.instrument__instrument_parameters = Slot(uri=ANALYSIS_API_SCHEMA.instrument_parameters, name="instrument__instrument_parameters", curie=ANALYSIS_API_SCHEMA.curie('instrument_parameters'),
                   model_uri=ANALYSIS_API_SCHEMA.instrument__instrument_parameters, domain=None, range=Optional[str])

slots.instrument__mass_analyzer_type = Slot(uri=ANALYSIS_API_SCHEMA.mass_analyzer_type, name="instrument__mass_analyzer_type", curie=ANALYSIS_API_SCHEMA.curie('mass_analyzer_type'),
                   model_uri=ANALYSIS_API_SCHEMA.instrument__mass_analyzer_type, domain=None, range=Optional[Union[str, "MassAnalyzerEnum"]])

slots.instrument__other_properties = Slot(uri=ANALYSIS_API_SCHEMA.other_properties, name="instrument__other_properties", curie=ANALYSIS_API_SCHEMA.curie('other_properties'),
                   model_uri=ANALYSIS_API_SCHEMA.instrument__other_properties, domain=None, range=Optional[str])

slots.ontologyClass__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="ontologyClass__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.ontologyClass__id, domain=None, range=URIRef)

slots.ontologyClass__description = Slot(uri=ANALYSIS_API_SCHEMA.description, name="ontologyClass__description", curie=ANALYSIS_API_SCHEMA.curie('description'),
                   model_uri=ANALYSIS_API_SCHEMA.ontologyClass__description, domain=None, range=Optional[str])

slots.ontologyClass__alternative_identifiers = Slot(uri=ANALYSIS_API_SCHEMA.alternative_identifiers, name="ontologyClass__alternative_identifiers", curie=ANALYSIS_API_SCHEMA.curie('alternative_identifiers'),
                   model_uri=ANALYSIS_API_SCHEMA.ontologyClass__alternative_identifiers, domain=None, range=Optional[str])

slots.ontologyClass__name = Slot(uri=ANALYSIS_API_SCHEMA.name, name="ontologyClass__name", curie=ANALYSIS_API_SCHEMA.curie('name'),
                   model_uri=ANALYSIS_API_SCHEMA.ontologyClass__name, domain=None, range=Optional[str])

slots.containerType__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="containerType__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.containerType__id, domain=None, range=URIRef)

slots.containerType__description = Slot(uri=ANALYSIS_API_SCHEMA.description, name="containerType__description", curie=ANALYSIS_API_SCHEMA.curie('description'),
                   model_uri=ANALYSIS_API_SCHEMA.containerType__description, domain=None, range=Optional[str])

slots.containerType__container_type = Slot(uri=ANALYSIS_API_SCHEMA.container_type, name="containerType__container_type", curie=ANALYSIS_API_SCHEMA.curie('container_type'),
                   model_uri=ANALYSIS_API_SCHEMA.containerType__container_type, domain=None, range=Optional[Union[str, "ContainerTypeEnum"]])

slots.containerType__container_size_id = Slot(uri=ANALYSIS_API_SCHEMA.container_size_id, name="containerType__container_size_id", curie=ANALYSIS_API_SCHEMA.curie('container_size_id'),
                   model_uri=ANALYSIS_API_SCHEMA.containerType__container_size_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.containerType__axes = Slot(uri=ANALYSIS_API_SCHEMA.axes, name="containerType__axes", curie=ANALYSIS_API_SCHEMA.curie('axes'),
                   model_uri=ANALYSIS_API_SCHEMA.containerType__axes, domain=None, range=Optional[Union[Union[dict, ContainerAxis], list[Union[dict, ContainerAxis]]]])

slots.containerType__contains = Slot(uri=ANALYSIS_API_SCHEMA.contains, name="containerType__contains", curie=ANALYSIS_API_SCHEMA.curie('contains'),
                   model_uri=ANALYSIS_API_SCHEMA.containerType__contains, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.containerType__label_format = Slot(uri=ANALYSIS_API_SCHEMA.label_format, name="containerType__label_format", curie=ANALYSIS_API_SCHEMA.curie('label_format'),
                   model_uri=ANALYSIS_API_SCHEMA.containerType__label_format, domain=None, range=Optional[str])

slots.containerType__renderer = Slot(uri=ANALYSIS_API_SCHEMA.renderer, name="containerType__renderer", curie=ANALYSIS_API_SCHEMA.curie('renderer'),
                   model_uri=ANALYSIS_API_SCHEMA.containerType__renderer, domain=None, range=Optional[str])

slots.containerType__slot_capacity = Slot(uri=ANALYSIS_API_SCHEMA.slot_capacity, name="containerType__slot_capacity", curie=ANALYSIS_API_SCHEMA.curie('slot_capacity'),
                   model_uri=ANALYSIS_API_SCHEMA.containerType__slot_capacity, domain=None, range=Optional[str])

slots.containerAxis__name = Slot(uri=ANALYSIS_API_SCHEMA.name, name="containerAxis__name", curie=ANALYSIS_API_SCHEMA.curie('name'),
                   model_uri=ANALYSIS_API_SCHEMA.containerAxis__name, domain=None, range=Optional[str])

slots.containerAxis__values = Slot(uri=ANALYSIS_API_SCHEMA.values, name="containerAxis__values", curie=ANALYSIS_API_SCHEMA.curie('values'),
                   model_uri=ANALYSIS_API_SCHEMA.containerAxis__values, domain=None, range=Optional[Union[str, list[str]]])

slots.custodian__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="custodian__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.custodian__id, domain=None, range=URIRef)

slots.custodian__person_id = Slot(uri=ANALYSIS_API_SCHEMA.person_id, name="custodian__person_id", curie=ANALYSIS_API_SCHEMA.curie('person_id'),
                   model_uri=ANALYSIS_API_SCHEMA.custodian__person_id, domain=None, range=Optional[Union[str, PersonValueId]])

slots.instrumentAlternativeIdentifier__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="instrumentAlternativeIdentifier__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.instrumentAlternativeIdentifier__id, domain=None, range=URIRef)

slots.instrumentAlternativeIdentifier__alt_id = Slot(uri=ANALYSIS_API_SCHEMA.alt_id, name="instrumentAlternativeIdentifier__alt_id", curie=ANALYSIS_API_SCHEMA.curie('alt_id'),
                   model_uri=ANALYSIS_API_SCHEMA.instrumentAlternativeIdentifier__alt_id, domain=None, range=Optional[Union[str, AlternativeIdentifierId]])

slots.instrumentAlternativeIdentifier__instrument_alt_id_provider = Slot(uri=ANALYSIS_API_SCHEMA.instrument_alt_id_provider, name="instrumentAlternativeIdentifier__instrument_alt_id_provider", curie=ANALYSIS_API_SCHEMA.curie('instrument_alt_id_provider'),
                   model_uri=ANALYSIS_API_SCHEMA.instrumentAlternativeIdentifier__instrument_alt_id_provider, domain=None, range=Optional[Union[str, "InstrumentAltIdProviderEnum"]])

slots.instrumentAlternativeIdentifier__instrument_id = Slot(uri=ANALYSIS_API_SCHEMA.instrument_id, name="instrumentAlternativeIdentifier__instrument_id", curie=ANALYSIS_API_SCHEMA.curie('instrument_id'),
                   model_uri=ANALYSIS_API_SCHEMA.instrumentAlternativeIdentifier__instrument_id, domain=None, range=Union[str, InstrumentId])

slots.labDevice__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="labDevice__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.labDevice__id, domain=None, range=URIRef)

slots.labDevice__description = Slot(uri=ANALYSIS_API_SCHEMA.description, name="labDevice__description", curie=ANALYSIS_API_SCHEMA.curie('description'),
                   model_uri=ANALYSIS_API_SCHEMA.labDevice__description, domain=None, range=Optional[str])

slots.labDevice__device_type = Slot(uri=ANALYSIS_API_SCHEMA.device_type, name="labDevice__device_type", curie=ANALYSIS_API_SCHEMA.curie('device_type'),
                   model_uri=ANALYSIS_API_SCHEMA.labDevice__device_type, domain=None, range=Optional[Union[str, "DeviceTypeEnum"]])

slots.labDevice__activity_time_id = Slot(uri=ANALYSIS_API_SCHEMA.activity_time_id, name="labDevice__activity_time_id", curie=ANALYSIS_API_SCHEMA.curie('activity_time_id'),
                   model_uri=ANALYSIS_API_SCHEMA.labDevice__activity_time_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.labDevice__activity_speed_id = Slot(uri=ANALYSIS_API_SCHEMA.activity_speed_id, name="labDevice__activity_speed_id", curie=ANALYSIS_API_SCHEMA.curie('activity_speed_id'),
                   model_uri=ANALYSIS_API_SCHEMA.labDevice__activity_speed_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.sampleProcessing__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="sampleProcessing__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.sampleProcessing__id, domain=None, range=URIRef)

slots.sampleProcessing__analysis_type = Slot(uri=ANALYSIS_API_SCHEMA.analysis_type, name="sampleProcessing__analysis_type", curie=ANALYSIS_API_SCHEMA.curie('analysis_type'),
                   model_uri=ANALYSIS_API_SCHEMA.sampleProcessing__analysis_type, domain=None, range=Optional[Union[str, "RouteMethodEnum"]])

slots.sampleProcessing__method_name = Slot(uri=ANALYSIS_API_SCHEMA.method_name, name="sampleProcessing__method_name", curie=ANALYSIS_API_SCHEMA.curie('method_name'),
                   model_uri=ANALYSIS_API_SCHEMA.sampleProcessing__method_name, domain=None, range=Optional[Union[str, "MethodNameEnum"]])

slots.sampleProcessing__processing_steps = Slot(uri=ANALYSIS_API_SCHEMA.processing_steps, name="sampleProcessing__processing_steps", curie=ANALYSIS_API_SCHEMA.curie('processing_steps'),
                   model_uri=ANALYSIS_API_SCHEMA.sampleProcessing__processing_steps, domain=None, range=str)

slots.sampleProcessing__uses_sample = Slot(uri=ANALYSIS_API_SCHEMA.uses_sample, name="sampleProcessing__uses_sample", curie=ANALYSIS_API_SCHEMA.curie('uses_sample'),
                   model_uri=ANALYSIS_API_SCHEMA.sampleProcessing__uses_sample, domain=None, range=Optional[Union[str, SampleId]])

slots.processingSampleLink__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="processingSampleLink__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.processingSampleLink__id, domain=None, range=URIRef)

slots.processingSampleLink__sample_base_id = Slot(uri=ANALYSIS_API_SCHEMA.sample_base_id, name="processingSampleLink__sample_base_id", curie=ANALYSIS_API_SCHEMA.curie('sample_base_id'),
                   model_uri=ANALYSIS_API_SCHEMA.processingSampleLink__sample_base_id, domain=None, range=Union[str, SampleId])

slots.processingSampleLink__processing_id = Slot(uri=ANALYSIS_API_SCHEMA.processing_id, name="processingSampleLink__processing_id", curie=ANALYSIS_API_SCHEMA.curie('processing_id'),
                   model_uri=ANALYSIS_API_SCHEMA.processingSampleLink__processing_id, domain=None, range=Union[str, SampleProcessingId])

slots.processingSampleLink__step_number = Slot(uri=ANALYSIS_API_SCHEMA.step_number, name="processingSampleLink__step_number", curie=ANALYSIS_API_SCHEMA.curie('step_number'),
                   model_uri=ANALYSIS_API_SCHEMA.processingSampleLink__step_number, domain=None, range=int)

slots.processingSampleLink__role = Slot(uri=ANALYSIS_API_SCHEMA.role, name="processingSampleLink__role", curie=ANALYSIS_API_SCHEMA.curie('role'),
                   model_uri=ANALYSIS_API_SCHEMA.processingSampleLink__role, domain=None, range=Union[str, "SampleRole"])

slots.instrumentCustodian__instrument_id = Slot(uri=ANALYSIS_API_SCHEMA.instrument_id, name="instrumentCustodian__instrument_id", curie=ANALYSIS_API_SCHEMA.curie('instrument_id'),
                   model_uri=ANALYSIS_API_SCHEMA.instrumentCustodian__instrument_id, domain=None, range=Union[str, InstrumentId])

slots.instrumentCustodian__custodian_id = Slot(uri=ANALYSIS_API_SCHEMA.custodian_id, name="instrumentCustodian__custodian_id", curie=ANALYSIS_API_SCHEMA.curie('custodian_id'),
                   model_uri=ANALYSIS_API_SCHEMA.instrumentCustodian__custodian_id, domain=None, range=Union[str, CustodianId])

slots.workflowExecutionFunctionalAnnotation__workflow_id = Slot(uri=ANALYSIS_API_SCHEMA.workflow_id, name="workflowExecutionFunctionalAnnotation__workflow_id", curie=ANALYSIS_API_SCHEMA.curie('workflow_id'),
                   model_uri=ANALYSIS_API_SCHEMA.workflowExecutionFunctionalAnnotation__workflow_id, domain=None, range=Union[str, DataProcessingActivityId])

slots.workflowExecutionFunctionalAnnotation__functional_annotation_id = Slot(uri=ANALYSIS_API_SCHEMA.functional_annotation_id, name="workflowExecutionFunctionalAnnotation__functional_annotation_id", curie=ANALYSIS_API_SCHEMA.curie('functional_annotation_id'),
                   model_uri=ANALYSIS_API_SCHEMA.workflowExecutionFunctionalAnnotation__functional_annotation_id, domain=None, range=Union[str, FunctionalAnnotationIdentifierId])

slots.workflowExecutionFunctionalAnnotation__count = Slot(uri=ANALYSIS_API_SCHEMA.count, name="workflowExecutionFunctionalAnnotation__count", curie=ANALYSIS_API_SCHEMA.curie('count'),
                   model_uri=ANALYSIS_API_SCHEMA.workflowExecutionFunctionalAnnotation__count, domain=None, range=Optional[float])

slots.changelog__version = Slot(uri=ANALYSIS_API_SCHEMA.version, name="changelog__version", curie=ANALYSIS_API_SCHEMA.curie('version'),
                   model_uri=ANALYSIS_API_SCHEMA.changelog__version, domain=None, range=URIRef)

slots.changelog__changelog = Slot(uri=ANALYSIS_API_SCHEMA.changelog, name="changelog__changelog", curie=ANALYSIS_API_SCHEMA.curie('changelog'),
                   model_uri=ANALYSIS_API_SCHEMA.changelog__changelog, domain=None, range=str)

slots.configuration__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="configuration__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.configuration__id, domain=None, range=Union[str, Uuid])

slots.mobilePhaseSegment__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="mobilePhaseSegment__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.mobilePhaseSegment__id, domain=None, range=URIRef)

slots.mobilePhaseSegment__segment_order = Slot(uri=ANALYSIS_API_SCHEMA.segment_order, name="mobilePhaseSegment__segment_order", curie=ANALYSIS_API_SCHEMA.curie('segment_order'),
                   model_uri=ANALYSIS_API_SCHEMA.mobilePhaseSegment__segment_order, domain=None, range=Optional[int])

slots.mobilePhaseSegment__substance = Slot(uri=ANALYSIS_API_SCHEMA.substance, name="mobilePhaseSegment__substance", curie=ANALYSIS_API_SCHEMA.curie('substance'),
                   model_uri=ANALYSIS_API_SCHEMA.mobilePhaseSegment__substance, domain=None, range=Optional[str])

slots.massSpectrometryStandardRun__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="massSpectrometryStandardRun__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.massSpectrometryStandardRun__id, domain=None, range=URIRef)

slots.purchasedMaterial__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="purchasedMaterial__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.purchasedMaterial__id, domain=None, range=URIRef)

slots.labProcessingActivity__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="labProcessingActivity__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.labProcessingActivity__id, domain=None, range=URIRef)

slots.labProcessingActivity__name = Slot(uri=ANALYSIS_API_SCHEMA.name, name="labProcessingActivity__name", curie=ANALYSIS_API_SCHEMA.curie('name'),
                   model_uri=ANALYSIS_API_SCHEMA.labProcessingActivity__name, domain=None, range=Optional[str])

slots.labProcessingActivity__description = Slot(uri=ANALYSIS_API_SCHEMA.description, name="labProcessingActivity__description", curie=ANALYSIS_API_SCHEMA.curie('description'),
                   model_uri=ANALYSIS_API_SCHEMA.labProcessingActivity__description, domain=None, range=Optional[str])

slots.wellMetadata__position = Slot(uri=ANALYSIS_API_SCHEMA.position, name="wellMetadata__position", curie=ANALYSIS_API_SCHEMA.curie('position'),
                   model_uri=ANALYSIS_API_SCHEMA.wellMetadata__position, domain=None, range=str)

slots.wellMetadata__well_type = Slot(uri=ANALYSIS_API_SCHEMA.well_type, name="wellMetadata__well_type", curie=ANALYSIS_API_SCHEMA.curie('well_type'),
                   model_uri=ANALYSIS_API_SCHEMA.wellMetadata__well_type, domain=None, range=Optional[str])

slots.wellMetadata__replicate_group = Slot(uri=ANALYSIS_API_SCHEMA.replicate_group, name="wellMetadata__replicate_group", curie=ANALYSIS_API_SCHEMA.curie('replicate_group'),
                   model_uri=ANALYSIS_API_SCHEMA.wellMetadata__replicate_group, domain=None, range=Optional[str])

slots.aMP2WellMetadata__media_ref = Slot(uri=ANALYSIS_API_SCHEMA.media_ref, name="aMP2WellMetadata__media_ref", curie=ANALYSIS_API_SCHEMA.curie('media_ref'),
                   model_uri=ANALYSIS_API_SCHEMA.aMP2WellMetadata__media_ref, domain=None, range=Optional[Union[str, ProcessedSampleId]])

slots.aMP2WellMetadata__media_volume_ul = Slot(uri=ANALYSIS_API_SCHEMA.media_volume_ul, name="aMP2WellMetadata__media_volume_ul", curie=ANALYSIS_API_SCHEMA.curie('media_volume_ul'),
                   model_uri=ANALYSIS_API_SCHEMA.aMP2WellMetadata__media_volume_ul, domain=None, range=float)

slots.aMP2WellMetadata__inoculum_volume_ul = Slot(uri=ANALYSIS_API_SCHEMA.inoculum_volume_ul, name="aMP2WellMetadata__inoculum_volume_ul", curie=ANALYSIS_API_SCHEMA.curie('inoculum_volume_ul'),
                   model_uri=ANALYSIS_API_SCHEMA.aMP2WellMetadata__inoculum_volume_ul, domain=None, range=float)

slots.aMP2WellMetadata__sample_id = Slot(uri=ANALYSIS_API_SCHEMA.sample_id, name="aMP2WellMetadata__sample_id", curie=ANALYSIS_API_SCHEMA.curie('sample_id'),
                   model_uri=ANALYSIS_API_SCHEMA.aMP2WellMetadata__sample_id, domain=None, range=Optional[str])

slots.aMP2WellMetadata__treatments = Slot(uri=ANALYSIS_API_SCHEMA.treatments, name="aMP2WellMetadata__treatments", curie=ANALYSIS_API_SCHEMA.curie('treatments'),
                   model_uri=ANALYSIS_API_SCHEMA.aMP2WellMetadata__treatments, domain=None, range=Optional[Union[str, list[str]]])

slots.ecoplateWellMetadata__media_volume_ul = Slot(uri=ANALYSIS_API_SCHEMA.media_volume_ul, name="ecoplateWellMetadata__media_volume_ul", curie=ANALYSIS_API_SCHEMA.curie('media_volume_ul'),
                   model_uri=ANALYSIS_API_SCHEMA.ecoplateWellMetadata__media_volume_ul, domain=None, range=float)

slots.ecoplateWellMetadata__carbon_source = Slot(uri=ANALYSIS_API_SCHEMA.carbon_source, name="ecoplateWellMetadata__carbon_source", curie=ANALYSIS_API_SCHEMA.curie('carbon_source'),
                   model_uri=ANALYSIS_API_SCHEMA.ecoplateWellMetadata__carbon_source, domain=None, range=str)

slots.ecoplateWellMetadata__treatment = Slot(uri=ANALYSIS_API_SCHEMA.treatment, name="ecoplateWellMetadata__treatment", curie=ANALYSIS_API_SCHEMA.curie('treatment'),
                   model_uri=ANALYSIS_API_SCHEMA.ecoplateWellMetadata__treatment, domain=None, range=Optional[str])

slots.ecoplateWellMetadata__treatment_concentration = Slot(uri=ANALYSIS_API_SCHEMA.treatment_concentration, name="ecoplateWellMetadata__treatment_concentration", curie=ANALYSIS_API_SCHEMA.curie('treatment_concentration'),
                   model_uri=ANALYSIS_API_SCHEMA.ecoplateWellMetadata__treatment_concentration, domain=None, range=Optional[str])

slots.wellReading__position = Slot(uri=ANALYSIS_API_SCHEMA.position, name="wellReading__position", curie=ANALYSIS_API_SCHEMA.curie('position'),
                   model_uri=ANALYSIS_API_SCHEMA.wellReading__position, domain=None, range=str)

slots.wellReading__value = Slot(uri=ANALYSIS_API_SCHEMA.value, name="wellReading__value", curie=ANALYSIS_API_SCHEMA.curie('value'),
                   model_uri=ANALYSIS_API_SCHEMA.wellReading__value, domain=None, range=float)

slots.wellReading__flag = Slot(uri=ANALYSIS_API_SCHEMA.flag, name="wellReading__flag", curie=ANALYSIS_API_SCHEMA.curie('flag'),
                   model_uri=ANALYSIS_API_SCHEMA.wellReading__flag, domain=None, range=Optional[str])

slots.enzymeActivityMethod__incubation_temp_c = Slot(uri=ANALYSIS_API_SCHEMA.incubation_temp_c, name="enzymeActivityMethod__incubation_temp_c", curie=ANALYSIS_API_SCHEMA.curie('incubation_temp_c'),
                   model_uri=ANALYSIS_API_SCHEMA.enzymeActivityMethod__incubation_temp_c, domain=None, range=Optional[float])

slots.enzymeActivityMethod__incubation_time = Slot(uri=ANALYSIS_API_SCHEMA.incubation_time, name="enzymeActivityMethod__incubation_time", curie=ANALYSIS_API_SCHEMA.curie('incubation_time'),
                   model_uri=ANALYSIS_API_SCHEMA.enzymeActivityMethod__incubation_time, domain=None, range=Optional[str])

slots.enzymeActivityMethod__wavelength = Slot(uri=ANALYSIS_API_SCHEMA.wavelength, name="enzymeActivityMethod__wavelength", curie=ANALYSIS_API_SCHEMA.curie('wavelength'),
                   model_uri=ANALYSIS_API_SCHEMA.enzymeActivityMethod__wavelength, domain=None, range=Optional[float])

slots.hydraulicPropertiesMethod__fitting_model = Slot(uri=ANALYSIS_API_SCHEMA.fitting_model, name="hydraulicPropertiesMethod__fitting_model", curie=ANALYSIS_API_SCHEMA.curie('fitting_model'),
                   model_uri=ANALYSIS_API_SCHEMA.hydraulicPropertiesMethod__fitting_model, domain=None, range=str)

slots.kuoMethod__detection_limit = Slot(uri=ANALYSIS_API_SCHEMA.detection_limit, name="kuoMethod__detection_limit", curie=ANALYSIS_API_SCHEMA.curie('detection_limit'),
                   model_uri=ANALYSIS_API_SCHEMA.kuoMethod__detection_limit, domain=None, range=str)

slots.kuoMethod__wavelength = Slot(uri=ANALYSIS_API_SCHEMA.wavelength, name="kuoMethod__wavelength", curie=ANALYSIS_API_SCHEMA.curie('wavelength'),
                   model_uri=ANALYSIS_API_SCHEMA.kuoMethod__wavelength, domain=None, range=Optional[str])

slots.microbialBiomassMethod__detector = Slot(uri=ANALYSIS_API_SCHEMA.detector, name="microbialBiomassMethod__detector", curie=ANALYSIS_API_SCHEMA.curie('detector'),
                   model_uri=ANALYSIS_API_SCHEMA.microbialBiomassMethod__detector, domain=None, range=str)

slots.microbialBiomassMethod__mode = Slot(uri=ANALYSIS_API_SCHEMA.mode, name="microbialBiomassMethod__mode", curie=ANALYSIS_API_SCHEMA.curie('mode'),
                   model_uri=ANALYSIS_API_SCHEMA.microbialBiomassMethod__mode, domain=None, range=Optional[str])

slots.microbialBiomassMethod__injection_volume = Slot(uri=ANALYSIS_API_SCHEMA.injection_volume, name="microbialBiomassMethod__injection_volume", curie=ANALYSIS_API_SCHEMA.curie('injection_volume'),
                   model_uri=ANALYSIS_API_SCHEMA.microbialBiomassMethod__injection_volume, domain=None, range=str)

slots.microbialBiomassMethod__sample_volume = Slot(uri=ANALYSIS_API_SCHEMA.sample_volume, name="microbialBiomassMethod__sample_volume", curie=ANALYSIS_API_SCHEMA.curie('sample_volume'),
                   model_uri=ANALYSIS_API_SCHEMA.microbialBiomassMethod__sample_volume, domain=None, range=str)

slots.microbialBiomassMethod__number_of_injections = Slot(uri=ANALYSIS_API_SCHEMA.number_of_injections, name="microbialBiomassMethod__number_of_injections", curie=ANALYSIS_API_SCHEMA.curie('number_of_injections'),
                   model_uri=ANALYSIS_API_SCHEMA.microbialBiomassMethod__number_of_injections, domain=None, range=float)

slots.microbialBiomassMethod__check_standard_spacing = Slot(uri=ANALYSIS_API_SCHEMA.check_standard_spacing, name="microbialBiomassMethod__check_standard_spacing", curie=ANALYSIS_API_SCHEMA.curie('check_standard_spacing'),
                   model_uri=ANALYSIS_API_SCHEMA.microbialBiomassMethod__check_standard_spacing, domain=None, range=str)

slots.pHMethod__calibration = Slot(uri=ANALYSIS_API_SCHEMA.calibration, name="pHMethod__calibration", curie=ANALYSIS_API_SCHEMA.curie('calibration'),
                   model_uri=ANALYSIS_API_SCHEMA.pHMethod__calibration, domain=None, range=str)

slots.tOCTNMethod__column = Slot(uri=ANALYSIS_API_SCHEMA.column, name="tOCTNMethod__column", curie=ANALYSIS_API_SCHEMA.curie('column'),
                   model_uri=ANALYSIS_API_SCHEMA.tOCTNMethod__column, domain=None, range=Optional[str])

slots.tOCTNMethod__mode = Slot(uri=ANALYSIS_API_SCHEMA.mode, name="tOCTNMethod__mode", curie=ANALYSIS_API_SCHEMA.curie('mode'),
                   model_uri=ANALYSIS_API_SCHEMA.tOCTNMethod__mode, domain=None, range=Optional[str])

slots.tOCTNMethod__detector = Slot(uri=ANALYSIS_API_SCHEMA.detector, name="tOCTNMethod__detector", curie=ANALYSIS_API_SCHEMA.curie('detector'),
                   model_uri=ANALYSIS_API_SCHEMA.tOCTNMethod__detector, domain=None, range=str)

slots.tOCTNMethod__injection_volume = Slot(uri=ANALYSIS_API_SCHEMA.injection_volume, name="tOCTNMethod__injection_volume", curie=ANALYSIS_API_SCHEMA.curie('injection_volume'),
                   model_uri=ANALYSIS_API_SCHEMA.tOCTNMethod__injection_volume, domain=None, range=str)

slots.tOCTNMethod__sample_volume = Slot(uri=ANALYSIS_API_SCHEMA.sample_volume, name="tOCTNMethod__sample_volume", curie=ANALYSIS_API_SCHEMA.curie('sample_volume'),
                   model_uri=ANALYSIS_API_SCHEMA.tOCTNMethod__sample_volume, domain=None, range=str)

slots.tOCTNMethod__number_of_injections = Slot(uri=ANALYSIS_API_SCHEMA.number_of_injections, name="tOCTNMethod__number_of_injections", curie=ANALYSIS_API_SCHEMA.curie('number_of_injections'),
                   model_uri=ANALYSIS_API_SCHEMA.tOCTNMethod__number_of_injections, domain=None, range=float)

slots.tOCTNMethod__check_standard_spacing = Slot(uri=ANALYSIS_API_SCHEMA.check_standard_spacing, name="tOCTNMethod__check_standard_spacing", curie=ANALYSIS_API_SCHEMA.curie('check_standard_spacing'),
                   model_uri=ANALYSIS_API_SCHEMA.tOCTNMethod__check_standard_spacing, domain=None, range=Optional[str])

slots.xrayComputedTomographyMethod__x_ray_power = Slot(uri=ANALYSIS_API_SCHEMA.x_ray_power, name="xrayComputedTomographyMethod__x_ray_power", curie=ANALYSIS_API_SCHEMA.curie('x_ray_power'),
                   model_uri=ANALYSIS_API_SCHEMA.xrayComputedTomographyMethod__x_ray_power, domain=None, range=str)

slots.xrayComputedTomographyMethod__cu_filter = Slot(uri=ANALYSIS_API_SCHEMA.cu_filter, name="xrayComputedTomographyMethod__cu_filter", curie=ANALYSIS_API_SCHEMA.curie('cu_filter'),
                   model_uri=ANALYSIS_API_SCHEMA.xrayComputedTomographyMethod__cu_filter, domain=None, range=str)

slots.xrayComputedTomographyMethod__total_projections_collected = Slot(uri=ANALYSIS_API_SCHEMA.total_projections_collected, name="xrayComputedTomographyMethod__total_projections_collected", curie=ANALYSIS_API_SCHEMA.curie('total_projections_collected'),
                   model_uri=ANALYSIS_API_SCHEMA.xrayComputedTomographyMethod__total_projections_collected, domain=None, range=float)

slots.xrayComputedTomographyMethod__rotation = Slot(uri=ANALYSIS_API_SCHEMA.rotation, name="xrayComputedTomographyMethod__rotation", curie=ANALYSIS_API_SCHEMA.curie('rotation'),
                   model_uri=ANALYSIS_API_SCHEMA.xrayComputedTomographyMethod__rotation, domain=None, range=str)

slots.xrayComputedTomographyMethod__frames_recording_per_projection = Slot(uri=ANALYSIS_API_SCHEMA.frames_recording_per_projection, name="xrayComputedTomographyMethod__frames_recording_per_projection", curie=ANALYSIS_API_SCHEMA.curie('frames_recording_per_projection'),
                   model_uri=ANALYSIS_API_SCHEMA.xrayComputedTomographyMethod__frames_recording_per_projection, domain=None, range=float)

slots.xrayComputedTomographyMethod__exposure_time_per_frame = Slot(uri=ANALYSIS_API_SCHEMA.exposure_time_per_frame, name="xrayComputedTomographyMethod__exposure_time_per_frame", curie=ANALYSIS_API_SCHEMA.curie('exposure_time_per_frame'),
                   model_uri=ANALYSIS_API_SCHEMA.xrayComputedTomographyMethod__exposure_time_per_frame, domain=None, range=str)

slots.xrayComputedTomographyMethod__image_voxel_size_is = Slot(uri=ANALYSIS_API_SCHEMA.image_voxel_size_is, name="xrayComputedTomographyMethod__image_voxel_size_is", curie=ANALYSIS_API_SCHEMA.curie('image_voxel_size_is'),
                   model_uri=ANALYSIS_API_SCHEMA.xrayComputedTomographyMethod__image_voxel_size_is, domain=None, range=str)

slots.bulkDensityProduct__bulk_density_id = Slot(uri=ANALYSIS_API_SCHEMA.bulk_density_id, name="bulkDensityProduct__bulk_density_id", curie=ANALYSIS_API_SCHEMA.curie('bulk_density_id'),
                   model_uri=ANALYSIS_API_SCHEMA.bulkDensityProduct__bulk_density_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.bulkDensityProduct__flag = Slot(uri=ANALYSIS_API_SCHEMA.flag, name="bulkDensityProduct__flag", curie=ANALYSIS_API_SCHEMA.curie('flag'),
                   model_uri=ANALYSIS_API_SCHEMA.bulkDensityProduct__flag, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.elementalAnalysisProduct__total_carbon_id = Slot(uri=ANALYSIS_API_SCHEMA.total_carbon_id, name="elementalAnalysisProduct__total_carbon_id", curie=ANALYSIS_API_SCHEMA.curie('total_carbon_id'),
                   model_uri=ANALYSIS_API_SCHEMA.elementalAnalysisProduct__total_carbon_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.elementalAnalysisProduct__total_nitrogen_id = Slot(uri=ANALYSIS_API_SCHEMA.total_nitrogen_id, name="elementalAnalysisProduct__total_nitrogen_id", curie=ANALYSIS_API_SCHEMA.curie('total_nitrogen_id'),
                   model_uri=ANALYSIS_API_SCHEMA.elementalAnalysisProduct__total_nitrogen_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.elementalAnalysisProduct__total_kjeldahl_nitrogen_id = Slot(uri=ANALYSIS_API_SCHEMA.total_kjeldahl_nitrogen_id, name="elementalAnalysisProduct__total_kjeldahl_nitrogen_id", curie=ANALYSIS_API_SCHEMA.curie('total_kjeldahl_nitrogen_id'),
                   model_uri=ANALYSIS_API_SCHEMA.elementalAnalysisProduct__total_kjeldahl_nitrogen_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.elementalAnalysisProduct__total_sulfur_id = Slot(uri=ANALYSIS_API_SCHEMA.total_sulfur_id, name="elementalAnalysisProduct__total_sulfur_id", curie=ANALYSIS_API_SCHEMA.curie('total_sulfur_id'),
                   model_uri=ANALYSIS_API_SCHEMA.elementalAnalysisProduct__total_sulfur_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.elementalAnalysisProduct__flag_total_carbon = Slot(uri=ANALYSIS_API_SCHEMA.flag_total_carbon, name="elementalAnalysisProduct__flag_total_carbon", curie=ANALYSIS_API_SCHEMA.curie('flag_total_carbon'),
                   model_uri=ANALYSIS_API_SCHEMA.elementalAnalysisProduct__flag_total_carbon, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.elementalAnalysisProduct__flag_total_nitrogen = Slot(uri=ANALYSIS_API_SCHEMA.flag_total_nitrogen, name="elementalAnalysisProduct__flag_total_nitrogen", curie=ANALYSIS_API_SCHEMA.curie('flag_total_nitrogen'),
                   model_uri=ANALYSIS_API_SCHEMA.elementalAnalysisProduct__flag_total_nitrogen, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.elementalAnalysisProduct__flag_tkn = Slot(uri=ANALYSIS_API_SCHEMA.flag_tkn, name="elementalAnalysisProduct__flag_tkn", curie=ANALYSIS_API_SCHEMA.curie('flag_tkn'),
                   model_uri=ANALYSIS_API_SCHEMA.elementalAnalysisProduct__flag_tkn, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.elementalAnalysisProduct__flag_total_sulfur = Slot(uri=ANALYSIS_API_SCHEMA.flag_total_sulfur, name="elementalAnalysisProduct__flag_total_sulfur", curie=ANALYSIS_API_SCHEMA.curie('flag_total_sulfur'),
                   model_uri=ANALYSIS_API_SCHEMA.elementalAnalysisProduct__flag_total_sulfur, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.enzymeProduct__beta_glucosidase_ug_pnp_per_g_per_h_id = Slot(uri=ANALYSIS_API_SCHEMA.beta_glucosidase_ug_pnp_per_g_per_h_id, name="enzymeProduct__beta_glucosidase_ug_pnp_per_g_per_h_id", curie=ANALYSIS_API_SCHEMA.curie('beta_glucosidase_ug_pnp_per_g_per_h_id'),
                   model_uri=ANALYSIS_API_SCHEMA.enzymeProduct__beta_glucosidase_ug_pnp_per_g_per_h_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.enzymeProduct__flag = Slot(uri=ANALYSIS_API_SCHEMA.flag, name="enzymeProduct__flag", curie=ANALYSIS_API_SCHEMA.curie('flag'),
                   model_uri=ANALYSIS_API_SCHEMA.enzymeProduct__flag, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.gWCMoistureProduct__gwc_percent_id = Slot(uri=ANALYSIS_API_SCHEMA.gwc_percent_id, name="gWCMoistureProduct__gwc_percent_id", curie=ANALYSIS_API_SCHEMA.curie('gwc_percent_id'),
                   model_uri=ANALYSIS_API_SCHEMA.gWCMoistureProduct__gwc_percent_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.gWCMoistureProduct__flag = Slot(uri=ANALYSIS_API_SCHEMA.flag, name="gWCMoistureProduct__flag", curie=ANALYSIS_API_SCHEMA.curie('flag'),
                   model_uri=ANALYSIS_API_SCHEMA.gWCMoistureProduct__flag, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.hydraulicPropertiesProduct__alpha = Slot(uri=ANALYSIS_API_SCHEMA.alpha, name="hydraulicPropertiesProduct__alpha", curie=ANALYSIS_API_SCHEMA.curie('alpha'),
                   model_uri=ANALYSIS_API_SCHEMA.hydraulicPropertiesProduct__alpha, domain=None, range=Optional[float])

slots.hydraulicPropertiesProduct__n = Slot(uri=ANALYSIS_API_SCHEMA.n, name="hydraulicPropertiesProduct__n", curie=ANALYSIS_API_SCHEMA.curie('n'),
                   model_uri=ANALYSIS_API_SCHEMA.hydraulicPropertiesProduct__n, domain=None, range=Optional[float])

slots.hydraulicPropertiesProduct__theta_r = Slot(uri=ANALYSIS_API_SCHEMA.theta_r, name="hydraulicPropertiesProduct__theta_r", curie=ANALYSIS_API_SCHEMA.curie('theta_r'),
                   model_uri=ANALYSIS_API_SCHEMA.hydraulicPropertiesProduct__theta_r, domain=None, range=Optional[float])

slots.hydraulicPropertiesProduct__theta_s = Slot(uri=ANALYSIS_API_SCHEMA.theta_s, name="hydraulicPropertiesProduct__theta_s", curie=ANALYSIS_API_SCHEMA.curie('theta_s'),
                   model_uri=ANALYSIS_API_SCHEMA.hydraulicPropertiesProduct__theta_s, domain=None, range=Optional[float])

slots.hydraulicPropertiesProduct__flag = Slot(uri=ANALYSIS_API_SCHEMA.flag, name="hydraulicPropertiesProduct__flag", curie=ANALYSIS_API_SCHEMA.curie('flag'),
                   model_uri=ANALYSIS_API_SCHEMA.hydraulicPropertiesProduct__flag, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.ionsAnalysisProduct__sulfate_id = Slot(uri=ANALYSIS_API_SCHEMA.sulfate_id, name="ionsAnalysisProduct__sulfate_id", curie=ANALYSIS_API_SCHEMA.curie('sulfate_id'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__sulfate_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.ionsAnalysisProduct__boron_id = Slot(uri=ANALYSIS_API_SCHEMA.boron_id, name="ionsAnalysisProduct__boron_id", curie=ANALYSIS_API_SCHEMA.curie('boron_id'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__boron_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.ionsAnalysisProduct__zinc_id = Slot(uri=ANALYSIS_API_SCHEMA.zinc_id, name="ionsAnalysisProduct__zinc_id", curie=ANALYSIS_API_SCHEMA.curie('zinc_id'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__zinc_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.ionsAnalysisProduct__manganate_id = Slot(uri=ANALYSIS_API_SCHEMA.manganate_id, name="ionsAnalysisProduct__manganate_id", curie=ANALYSIS_API_SCHEMA.curie('manganate_id'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__manganate_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.ionsAnalysisProduct__copper_id = Slot(uri=ANALYSIS_API_SCHEMA.copper_id, name="ionsAnalysisProduct__copper_id", curie=ANALYSIS_API_SCHEMA.curie('copper_id'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__copper_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.ionsAnalysisProduct__iron_id = Slot(uri=ANALYSIS_API_SCHEMA.iron_id, name="ionsAnalysisProduct__iron_id", curie=ANALYSIS_API_SCHEMA.curie('iron_id'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__iron_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.ionsAnalysisProduct__calcium_id = Slot(uri=ANALYSIS_API_SCHEMA.calcium_id, name="ionsAnalysisProduct__calcium_id", curie=ANALYSIS_API_SCHEMA.curie('calcium_id'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__calcium_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.ionsAnalysisProduct__magnesium_id = Slot(uri=ANALYSIS_API_SCHEMA.magnesium_id, name="ionsAnalysisProduct__magnesium_id", curie=ANALYSIS_API_SCHEMA.curie('magnesium_id'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__magnesium_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.ionsAnalysisProduct__sodium_id = Slot(uri=ANALYSIS_API_SCHEMA.sodium_id, name="ionsAnalysisProduct__sodium_id", curie=ANALYSIS_API_SCHEMA.curie('sodium_id'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__sodium_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.ionsAnalysisProduct__potassium_id = Slot(uri=ANALYSIS_API_SCHEMA.potassium_id, name="ionsAnalysisProduct__potassium_id", curie=ANALYSIS_API_SCHEMA.curie('potassium_id'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__potassium_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.ionsAnalysisProduct__total_bases_id = Slot(uri=ANALYSIS_API_SCHEMA.total_bases_id, name="ionsAnalysisProduct__total_bases_id", curie=ANALYSIS_API_SCHEMA.curie('total_bases_id'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__total_bases_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.ionsAnalysisProduct__cation_exchange_capacity_id = Slot(uri=ANALYSIS_API_SCHEMA.cation_exchange_capacity_id, name="ionsAnalysisProduct__cation_exchange_capacity_id", curie=ANALYSIS_API_SCHEMA.curie('cation_exchange_capacity_id'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__cation_exchange_capacity_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.ionsAnalysisProduct__flag_sulfate = Slot(uri=ANALYSIS_API_SCHEMA.flag_sulfate, name="ionsAnalysisProduct__flag_sulfate", curie=ANALYSIS_API_SCHEMA.curie('flag_sulfate'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__flag_sulfate, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.ionsAnalysisProduct__flag_boron = Slot(uri=ANALYSIS_API_SCHEMA.flag_boron, name="ionsAnalysisProduct__flag_boron", curie=ANALYSIS_API_SCHEMA.curie('flag_boron'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__flag_boron, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.ionsAnalysisProduct__flag_zinc = Slot(uri=ANALYSIS_API_SCHEMA.flag_zinc, name="ionsAnalysisProduct__flag_zinc", curie=ANALYSIS_API_SCHEMA.curie('flag_zinc'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__flag_zinc, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.ionsAnalysisProduct__flag_manganate = Slot(uri=ANALYSIS_API_SCHEMA.flag_manganate, name="ionsAnalysisProduct__flag_manganate", curie=ANALYSIS_API_SCHEMA.curie('flag_manganate'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__flag_manganate, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.ionsAnalysisProduct__flag_copper = Slot(uri=ANALYSIS_API_SCHEMA.flag_copper, name="ionsAnalysisProduct__flag_copper", curie=ANALYSIS_API_SCHEMA.curie('flag_copper'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__flag_copper, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.ionsAnalysisProduct__flag_iron = Slot(uri=ANALYSIS_API_SCHEMA.flag_iron, name="ionsAnalysisProduct__flag_iron", curie=ANALYSIS_API_SCHEMA.curie('flag_iron'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__flag_iron, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.ionsAnalysisProduct__flag_calcium = Slot(uri=ANALYSIS_API_SCHEMA.flag_calcium, name="ionsAnalysisProduct__flag_calcium", curie=ANALYSIS_API_SCHEMA.curie('flag_calcium'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__flag_calcium, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.ionsAnalysisProduct__flag_magnesium = Slot(uri=ANALYSIS_API_SCHEMA.flag_magnesium, name="ionsAnalysisProduct__flag_magnesium", curie=ANALYSIS_API_SCHEMA.curie('flag_magnesium'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__flag_magnesium, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.ionsAnalysisProduct__flag_sodium = Slot(uri=ANALYSIS_API_SCHEMA.flag_sodium, name="ionsAnalysisProduct__flag_sodium", curie=ANALYSIS_API_SCHEMA.curie('flag_sodium'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__flag_sodium, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.ionsAnalysisProduct__flag_potassium = Slot(uri=ANALYSIS_API_SCHEMA.flag_potassium, name="ionsAnalysisProduct__flag_potassium", curie=ANALYSIS_API_SCHEMA.curie('flag_potassium'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__flag_potassium, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.ionsAnalysisProduct__flag_total_bases = Slot(uri=ANALYSIS_API_SCHEMA.flag_total_bases, name="ionsAnalysisProduct__flag_total_bases", curie=ANALYSIS_API_SCHEMA.curie('flag_total_bases'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__flag_total_bases, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.ionsAnalysisProduct__flag_cec = Slot(uri=ANALYSIS_API_SCHEMA.flag_cec, name="ionsAnalysisProduct__flag_cec", curie=ANALYSIS_API_SCHEMA.curie('flag_cec'),
                   model_uri=ANALYSIS_API_SCHEMA.ionsAnalysisProduct__flag_cec, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.mAOMProduct__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="mAOMProduct__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.mAOMProduct__id, domain=None, range=URIRef)

slots.mAOMProduct__total_organic_carbon_id = Slot(uri=ANALYSIS_API_SCHEMA.total_organic_carbon_id, name="mAOMProduct__total_organic_carbon_id", curie=ANALYSIS_API_SCHEMA.curie('total_organic_carbon_id'),
                   model_uri=ANALYSIS_API_SCHEMA.mAOMProduct__total_organic_carbon_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.mAOMProduct__total_organic_carbon_avg = Slot(uri=ANALYSIS_API_SCHEMA.total_organic_carbon_avg, name="mAOMProduct__total_organic_carbon_avg", curie=ANALYSIS_API_SCHEMA.curie('total_organic_carbon_avg'),
                   model_uri=ANALYSIS_API_SCHEMA.mAOMProduct__total_organic_carbon_avg, domain=None, range=Optional[float])

slots.mAOMProduct__total_nitrogen_id = Slot(uri=ANALYSIS_API_SCHEMA.total_nitrogen_id, name="mAOMProduct__total_nitrogen_id", curie=ANALYSIS_API_SCHEMA.curie('total_nitrogen_id'),
                   model_uri=ANALYSIS_API_SCHEMA.mAOMProduct__total_nitrogen_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.mAOMProduct__total_nitrogen_avg = Slot(uri=ANALYSIS_API_SCHEMA.total_nitrogen_avg, name="mAOMProduct__total_nitrogen_avg", curie=ANALYSIS_API_SCHEMA.curie('total_nitrogen_avg'),
                   model_uri=ANALYSIS_API_SCHEMA.mAOMProduct__total_nitrogen_avg, domain=None, range=Optional[float])

slots.mAOMProduct__flag_toc = Slot(uri=ANALYSIS_API_SCHEMA.flag_toc, name="mAOMProduct__flag_toc", curie=ANALYSIS_API_SCHEMA.curie('flag_toc'),
                   model_uri=ANALYSIS_API_SCHEMA.mAOMProduct__flag_toc, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.mAOMProduct__flag_tn = Slot(uri=ANALYSIS_API_SCHEMA.flag_tn, name="mAOMProduct__flag_tn", curie=ANALYSIS_API_SCHEMA.curie('flag_tn'),
                   model_uri=ANALYSIS_API_SCHEMA.mAOMProduct__flag_tn, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.mAOMProduct__flag_toc_avg = Slot(uri=ANALYSIS_API_SCHEMA.flag_toc_avg, name="mAOMProduct__flag_toc_avg", curie=ANALYSIS_API_SCHEMA.curie('flag_toc_avg'),
                   model_uri=ANALYSIS_API_SCHEMA.mAOMProduct__flag_toc_avg, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.mAOMProduct__flag_tn_avg = Slot(uri=ANALYSIS_API_SCHEMA.flag_tn_avg, name="mAOMProduct__flag_tn_avg", curie=ANALYSIS_API_SCHEMA.curie('flag_tn_avg'),
                   model_uri=ANALYSIS_API_SCHEMA.mAOMProduct__flag_tn_avg, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.microbialBiomassProduct__mbc_id = Slot(uri=ANALYSIS_API_SCHEMA.mbc_id, name="microbialBiomassProduct__mbc_id", curie=ANALYSIS_API_SCHEMA.curie('mbc_id'),
                   model_uri=ANALYSIS_API_SCHEMA.microbialBiomassProduct__mbc_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.microbialBiomassProduct__mbc_avg = Slot(uri=ANALYSIS_API_SCHEMA.mbc_avg, name="microbialBiomassProduct__mbc_avg", curie=ANALYSIS_API_SCHEMA.curie('mbc_avg'),
                   model_uri=ANALYSIS_API_SCHEMA.microbialBiomassProduct__mbc_avg, domain=None, range=Optional[float])

slots.microbialBiomassProduct__mbn_id = Slot(uri=ANALYSIS_API_SCHEMA.mbn_id, name="microbialBiomassProduct__mbn_id", curie=ANALYSIS_API_SCHEMA.curie('mbn_id'),
                   model_uri=ANALYSIS_API_SCHEMA.microbialBiomassProduct__mbn_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.microbialBiomassProduct__mbn_avg = Slot(uri=ANALYSIS_API_SCHEMA.mbn_avg, name="microbialBiomassProduct__mbn_avg", curie=ANALYSIS_API_SCHEMA.curie('mbn_avg'),
                   model_uri=ANALYSIS_API_SCHEMA.microbialBiomassProduct__mbn_avg, domain=None, range=Optional[float])

slots.microbialBiomassProduct__flag_mbc = Slot(uri=ANALYSIS_API_SCHEMA.flag_mbc, name="microbialBiomassProduct__flag_mbc", curie=ANALYSIS_API_SCHEMA.curie('flag_mbc'),
                   model_uri=ANALYSIS_API_SCHEMA.microbialBiomassProduct__flag_mbc, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.microbialBiomassProduct__flag_mbn = Slot(uri=ANALYSIS_API_SCHEMA.flag_mbn, name="microbialBiomassProduct__flag_mbn", curie=ANALYSIS_API_SCHEMA.curie('flag_mbn'),
                   model_uri=ANALYSIS_API_SCHEMA.microbialBiomassProduct__flag_mbn, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.microbialBiomassProduct__flag_mbc_avg = Slot(uri=ANALYSIS_API_SCHEMA.flag_mbc_avg, name="microbialBiomassProduct__flag_mbc_avg", curie=ANALYSIS_API_SCHEMA.curie('flag_mbc_avg'),
                   model_uri=ANALYSIS_API_SCHEMA.microbialBiomassProduct__flag_mbc_avg, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.microbialBiomassProduct__flag_mbn_avg = Slot(uri=ANALYSIS_API_SCHEMA.flag_mbn_avg, name="microbialBiomassProduct__flag_mbn_avg", curie=ANALYSIS_API_SCHEMA.curie('flag_mbn_avg'),
                   model_uri=ANALYSIS_API_SCHEMA.microbialBiomassProduct__flag_mbn_avg, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.nitrogenAnalysisProduct__no3_n_id = Slot(uri=ANALYSIS_API_SCHEMA.no3_n_id, name="nitrogenAnalysisProduct__no3_n_id", curie=ANALYSIS_API_SCHEMA.curie('no3_n_id'),
                   model_uri=ANALYSIS_API_SCHEMA.nitrogenAnalysisProduct__no3_n_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.nitrogenAnalysisProduct__no3_n_avg = Slot(uri=ANALYSIS_API_SCHEMA.no3_n_avg, name="nitrogenAnalysisProduct__no3_n_avg", curie=ANALYSIS_API_SCHEMA.curie('no3_n_avg'),
                   model_uri=ANALYSIS_API_SCHEMA.nitrogenAnalysisProduct__no3_n_avg, domain=None, range=Optional[float])

slots.nitrogenAnalysisProduct__nh4_n_id = Slot(uri=ANALYSIS_API_SCHEMA.nh4_n_id, name="nitrogenAnalysisProduct__nh4_n_id", curie=ANALYSIS_API_SCHEMA.curie('nh4_n_id'),
                   model_uri=ANALYSIS_API_SCHEMA.nitrogenAnalysisProduct__nh4_n_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.nitrogenAnalysisProduct__nh4_n_avg = Slot(uri=ANALYSIS_API_SCHEMA.nh4_n_avg, name="nitrogenAnalysisProduct__nh4_n_avg", curie=ANALYSIS_API_SCHEMA.curie('nh4_n_avg'),
                   model_uri=ANALYSIS_API_SCHEMA.nitrogenAnalysisProduct__nh4_n_avg, domain=None, range=Optional[float])

slots.nitrogenAnalysisProduct__flag_no3n = Slot(uri=ANALYSIS_API_SCHEMA.flag_no3n, name="nitrogenAnalysisProduct__flag_no3n", curie=ANALYSIS_API_SCHEMA.curie('flag_no3n'),
                   model_uri=ANALYSIS_API_SCHEMA.nitrogenAnalysisProduct__flag_no3n, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.nitrogenAnalysisProduct__flag_nh4n = Slot(uri=ANALYSIS_API_SCHEMA.flag_nh4n, name="nitrogenAnalysisProduct__flag_nh4n", curie=ANALYSIS_API_SCHEMA.curie('flag_nh4n'),
                   model_uri=ANALYSIS_API_SCHEMA.nitrogenAnalysisProduct__flag_nh4n, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.nitrogenAnalysisProduct__flag_no3n_avg = Slot(uri=ANALYSIS_API_SCHEMA.flag_no3n_avg, name="nitrogenAnalysisProduct__flag_no3n_avg", curie=ANALYSIS_API_SCHEMA.curie('flag_no3n_avg'),
                   model_uri=ANALYSIS_API_SCHEMA.nitrogenAnalysisProduct__flag_no3n_avg, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.nitrogenAnalysisProduct__flag_nh4n_avg = Slot(uri=ANALYSIS_API_SCHEMA.flag_nh4n_avg, name="nitrogenAnalysisProduct__flag_nh4n_avg", curie=ANALYSIS_API_SCHEMA.curie('flag_nh4n_avg'),
                   model_uri=ANALYSIS_API_SCHEMA.nitrogenAnalysisProduct__flag_nh4n_avg, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.phosphorusAnalysisProduct__extraction_method = Slot(uri=ANALYSIS_API_SCHEMA.extraction_method, name="phosphorusAnalysisProduct__extraction_method", curie=ANALYSIS_API_SCHEMA.curie('extraction_method'),
                   model_uri=ANALYSIS_API_SCHEMA.phosphorusAnalysisProduct__extraction_method, domain=None, range=Optional[str])

slots.phosphorusAnalysisProduct__phosphorus_id = Slot(uri=ANALYSIS_API_SCHEMA.phosphorus_id, name="phosphorusAnalysisProduct__phosphorus_id", curie=ANALYSIS_API_SCHEMA.curie('phosphorus_id'),
                   model_uri=ANALYSIS_API_SCHEMA.phosphorusAnalysisProduct__phosphorus_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.phosphorusAnalysisProduct__phosphorus_avg = Slot(uri=ANALYSIS_API_SCHEMA.phosphorus_avg, name="phosphorusAnalysisProduct__phosphorus_avg", curie=ANALYSIS_API_SCHEMA.curie('phosphorus_avg'),
                   model_uri=ANALYSIS_API_SCHEMA.phosphorusAnalysisProduct__phosphorus_avg, domain=None, range=Optional[float])

slots.phosphorusAnalysisProduct__flag = Slot(uri=ANALYSIS_API_SCHEMA.flag, name="phosphorusAnalysisProduct__flag", curie=ANALYSIS_API_SCHEMA.curie('flag'),
                   model_uri=ANALYSIS_API_SCHEMA.phosphorusAnalysisProduct__flag, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.phosphorusAnalysisProduct__flag_avg = Slot(uri=ANALYSIS_API_SCHEMA.flag_avg, name="phosphorusAnalysisProduct__flag_avg", curie=ANALYSIS_API_SCHEMA.curie('flag_avg'),
                   model_uri=ANALYSIS_API_SCHEMA.phosphorusAnalysisProduct__flag_avg, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.respirationProduct__respiration_co2_c_ug_per_g = Slot(uri=ANALYSIS_API_SCHEMA.respiration_co2_c_ug_per_g, name="respirationProduct__respiration_co2_c_ug_per_g", curie=ANALYSIS_API_SCHEMA.curie('respiration_co2_c_ug_per_g'),
                   model_uri=ANALYSIS_API_SCHEMA.respirationProduct__respiration_co2_c_ug_per_g, domain=None, range=Optional[float])

slots.respirationProduct__flag = Slot(uri=ANALYSIS_API_SCHEMA.flag, name="respirationProduct__flag", curie=ANALYSIS_API_SCHEMA.curie('flag'),
                   model_uri=ANALYSIS_API_SCHEMA.respirationProduct__flag, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.textureProduct__sand_pct_id = Slot(uri=ANALYSIS_API_SCHEMA.sand_pct_id, name="textureProduct__sand_pct_id", curie=ANALYSIS_API_SCHEMA.curie('sand_pct_id'),
                   model_uri=ANALYSIS_API_SCHEMA.textureProduct__sand_pct_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.textureProduct__silt_pct_id = Slot(uri=ANALYSIS_API_SCHEMA.silt_pct_id, name="textureProduct__silt_pct_id", curie=ANALYSIS_API_SCHEMA.curie('silt_pct_id'),
                   model_uri=ANALYSIS_API_SCHEMA.textureProduct__silt_pct_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.textureProduct__clay_pct_id = Slot(uri=ANALYSIS_API_SCHEMA.clay_pct_id, name="textureProduct__clay_pct_id", curie=ANALYSIS_API_SCHEMA.curie('clay_pct_id'),
                   model_uri=ANALYSIS_API_SCHEMA.textureProduct__clay_pct_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.textureProduct__flag = Slot(uri=ANALYSIS_API_SCHEMA.flag, name="textureProduct__flag", curie=ANALYSIS_API_SCHEMA.curie('flag'),
                   model_uri=ANALYSIS_API_SCHEMA.textureProduct__flag, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.tomographyProduct__roi_volume_voxel = Slot(uri=ANALYSIS_API_SCHEMA.roi_volume_voxel, name="tomographyProduct__roi_volume_voxel", curie=ANALYSIS_API_SCHEMA.curie('roi_volume_voxel'),
                   model_uri=ANALYSIS_API_SCHEMA.tomographyProduct__roi_volume_voxel, domain=None, range=Optional[float])

slots.tomographyProduct__voxel_size = Slot(uri=ANALYSIS_API_SCHEMA.voxel_size, name="tomographyProduct__voxel_size", curie=ANALYSIS_API_SCHEMA.curie('voxel_size'),
                   model_uri=ANALYSIS_API_SCHEMA.tomographyProduct__voxel_size, domain=None, range=Optional[float])

slots.tomographyProduct__connected_pores = Slot(uri=ANALYSIS_API_SCHEMA.connected_pores, name="tomographyProduct__connected_pores", curie=ANALYSIS_API_SCHEMA.curie('connected_pores'),
                   model_uri=ANALYSIS_API_SCHEMA.tomographyProduct__connected_pores, domain=None, range=Optional[float])

slots.tomographyProduct__pore_diameter_min = Slot(uri=ANALYSIS_API_SCHEMA.pore_diameter_min, name="tomographyProduct__pore_diameter_min", curie=ANALYSIS_API_SCHEMA.curie('pore_diameter_min'),
                   model_uri=ANALYSIS_API_SCHEMA.tomographyProduct__pore_diameter_min, domain=None, range=Optional[float])

slots.tomographyProduct__pore_diameter_max = Slot(uri=ANALYSIS_API_SCHEMA.pore_diameter_max, name="tomographyProduct__pore_diameter_max", curie=ANALYSIS_API_SCHEMA.curie('pore_diameter_max'),
                   model_uri=ANALYSIS_API_SCHEMA.tomographyProduct__pore_diameter_max, domain=None, range=Optional[float])

slots.tomographyProduct__pore_diameter_mean = Slot(uri=ANALYSIS_API_SCHEMA.pore_diameter_mean, name="tomographyProduct__pore_diameter_mean", curie=ANALYSIS_API_SCHEMA.curie('pore_diameter_mean'),
                   model_uri=ANALYSIS_API_SCHEMA.tomographyProduct__pore_diameter_mean, domain=None, range=Optional[float])

slots.tomographyProduct__pore_diameter_median = Slot(uri=ANALYSIS_API_SCHEMA.pore_diameter_median, name="tomographyProduct__pore_diameter_median", curie=ANALYSIS_API_SCHEMA.curie('pore_diameter_median'),
                   model_uri=ANALYSIS_API_SCHEMA.tomographyProduct__pore_diameter_median, domain=None, range=Optional[float])

slots.tomographyProduct__pore_diameter_variance = Slot(uri=ANALYSIS_API_SCHEMA.pore_diameter_variance, name="tomographyProduct__pore_diameter_variance", curie=ANALYSIS_API_SCHEMA.curie('pore_diameter_variance'),
                   model_uri=ANALYSIS_API_SCHEMA.tomographyProduct__pore_diameter_variance, domain=None, range=Optional[float])

slots.tomographyProduct__pore_volume_mean = Slot(uri=ANALYSIS_API_SCHEMA.pore_volume_mean, name="tomographyProduct__pore_volume_mean", curie=ANALYSIS_API_SCHEMA.curie('pore_volume_mean'),
                   model_uri=ANALYSIS_API_SCHEMA.tomographyProduct__pore_volume_mean, domain=None, range=Optional[float])

slots.tomographyProduct__total_pore_volume = Slot(uri=ANALYSIS_API_SCHEMA.total_pore_volume, name="tomographyProduct__total_pore_volume", curie=ANALYSIS_API_SCHEMA.curie('total_pore_volume'),
                   model_uri=ANALYSIS_API_SCHEMA.tomographyProduct__total_pore_volume, domain=None, range=Optional[float])

slots.tomographyProduct__permeability_x = Slot(uri=ANALYSIS_API_SCHEMA.permeability_x, name="tomographyProduct__permeability_x", curie=ANALYSIS_API_SCHEMA.curie('permeability_x'),
                   model_uri=ANALYSIS_API_SCHEMA.tomographyProduct__permeability_x, domain=None, range=Optional[float])

slots.tomographyProduct__flow_rate_x = Slot(uri=ANALYSIS_API_SCHEMA.flow_rate_x, name="tomographyProduct__flow_rate_x", curie=ANALYSIS_API_SCHEMA.curie('flow_rate_x'),
                   model_uri=ANALYSIS_API_SCHEMA.tomographyProduct__flow_rate_x, domain=None, range=Optional[float])

slots.tomographyProduct__tortuosity_x = Slot(uri=ANALYSIS_API_SCHEMA.tortuosity_x, name="tomographyProduct__tortuosity_x", curie=ANALYSIS_API_SCHEMA.curie('tortuosity_x'),
                   model_uri=ANALYSIS_API_SCHEMA.tomographyProduct__tortuosity_x, domain=None, range=Optional[float])

slots.tomographyProduct__permeability_y = Slot(uri=ANALYSIS_API_SCHEMA.permeability_y, name="tomographyProduct__permeability_y", curie=ANALYSIS_API_SCHEMA.curie('permeability_y'),
                   model_uri=ANALYSIS_API_SCHEMA.tomographyProduct__permeability_y, domain=None, range=Optional[float])

slots.tomographyProduct__flow_rate_y = Slot(uri=ANALYSIS_API_SCHEMA.flow_rate_y, name="tomographyProduct__flow_rate_y", curie=ANALYSIS_API_SCHEMA.curie('flow_rate_y'),
                   model_uri=ANALYSIS_API_SCHEMA.tomographyProduct__flow_rate_y, domain=None, range=Optional[float])

slots.tomographyProduct__tortuosity_y = Slot(uri=ANALYSIS_API_SCHEMA.tortuosity_y, name="tomographyProduct__tortuosity_y", curie=ANALYSIS_API_SCHEMA.curie('tortuosity_y'),
                   model_uri=ANALYSIS_API_SCHEMA.tomographyProduct__tortuosity_y, domain=None, range=Optional[float])

slots.tomographyProduct__permeability_z = Slot(uri=ANALYSIS_API_SCHEMA.permeability_z, name="tomographyProduct__permeability_z", curie=ANALYSIS_API_SCHEMA.curie('permeability_z'),
                   model_uri=ANALYSIS_API_SCHEMA.tomographyProduct__permeability_z, domain=None, range=Optional[float])

slots.tomographyProduct__flow_rate_z = Slot(uri=ANALYSIS_API_SCHEMA.flow_rate_z, name="tomographyProduct__flow_rate_z", curie=ANALYSIS_API_SCHEMA.curie('flow_rate_z'),
                   model_uri=ANALYSIS_API_SCHEMA.tomographyProduct__flow_rate_z, domain=None, range=Optional[float])

slots.tomographyProduct__tortuosity_z = Slot(uri=ANALYSIS_API_SCHEMA.tortuosity_z, name="tomographyProduct__tortuosity_z", curie=ANALYSIS_API_SCHEMA.curie('tortuosity_z'),
                   model_uri=ANALYSIS_API_SCHEMA.tomographyProduct__tortuosity_z, domain=None, range=Optional[float])

slots.tomographyProduct__flag_xct = Slot(uri=ANALYSIS_API_SCHEMA.flag_xct, name="tomographyProduct__flag_xct", curie=ANALYSIS_API_SCHEMA.curie('flag_xct'),
                   model_uri=ANALYSIS_API_SCHEMA.tomographyProduct__flag_xct, domain=None, range=Optional[str])

slots.wEOMProduct__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="wEOMProduct__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.wEOMProduct__id, domain=None, range=URIRef)

slots.wEOMProduct__total_organic_carbon_id = Slot(uri=ANALYSIS_API_SCHEMA.total_organic_carbon_id, name="wEOMProduct__total_organic_carbon_id", curie=ANALYSIS_API_SCHEMA.curie('total_organic_carbon_id'),
                   model_uri=ANALYSIS_API_SCHEMA.wEOMProduct__total_organic_carbon_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.wEOMProduct__total_organic_carbon_avg = Slot(uri=ANALYSIS_API_SCHEMA.total_organic_carbon_avg, name="wEOMProduct__total_organic_carbon_avg", curie=ANALYSIS_API_SCHEMA.curie('total_organic_carbon_avg'),
                   model_uri=ANALYSIS_API_SCHEMA.wEOMProduct__total_organic_carbon_avg, domain=None, range=Optional[float])

slots.wEOMProduct__total_nitrogen_id = Slot(uri=ANALYSIS_API_SCHEMA.total_nitrogen_id, name="wEOMProduct__total_nitrogen_id", curie=ANALYSIS_API_SCHEMA.curie('total_nitrogen_id'),
                   model_uri=ANALYSIS_API_SCHEMA.wEOMProduct__total_nitrogen_id, domain=None, range=Optional[Union[str, QuantityValueId]])

slots.wEOMProduct__total_nitrogen_avg = Slot(uri=ANALYSIS_API_SCHEMA.total_nitrogen_avg, name="wEOMProduct__total_nitrogen_avg", curie=ANALYSIS_API_SCHEMA.curie('total_nitrogen_avg'),
                   model_uri=ANALYSIS_API_SCHEMA.wEOMProduct__total_nitrogen_avg, domain=None, range=Optional[float])

slots.wEOMProduct__flag_toc = Slot(uri=ANALYSIS_API_SCHEMA.flag_toc, name="wEOMProduct__flag_toc", curie=ANALYSIS_API_SCHEMA.curie('flag_toc'),
                   model_uri=ANALYSIS_API_SCHEMA.wEOMProduct__flag_toc, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.wEOMProduct__flag_tn = Slot(uri=ANALYSIS_API_SCHEMA.flag_tn, name="wEOMProduct__flag_tn", curie=ANALYSIS_API_SCHEMA.curie('flag_tn'),
                   model_uri=ANALYSIS_API_SCHEMA.wEOMProduct__flag_tn, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.wEOMProduct__flag_toc_avg = Slot(uri=ANALYSIS_API_SCHEMA.flag_toc_avg, name="wEOMProduct__flag_toc_avg", curie=ANALYSIS_API_SCHEMA.curie('flag_toc_avg'),
                   model_uri=ANALYSIS_API_SCHEMA.wEOMProduct__flag_toc_avg, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.wEOMProduct__flag_tn_avg = Slot(uri=ANALYSIS_API_SCHEMA.flag_tn_avg, name="wEOMProduct__flag_tn_avg", curie=ANALYSIS_API_SCHEMA.curie('flag_tn_avg'),
                   model_uri=ANALYSIS_API_SCHEMA.wEOMProduct__flag_tn_avg, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.pHProduct__ph = Slot(uri=ANALYSIS_API_SCHEMA.ph, name="pHProduct__ph", curie=ANALYSIS_API_SCHEMA.curie('ph'),
                   model_uri=ANALYSIS_API_SCHEMA.pHProduct__ph, domain=None, range=Optional[float])

slots.pHProduct__flag = Slot(uri=ANALYSIS_API_SCHEMA.flag, name="pHProduct__flag", curie=ANALYSIS_API_SCHEMA.curie('flag'),
                   model_uri=ANALYSIS_API_SCHEMA.pHProduct__flag, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__cl_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.cl_mg_per_kg, name="xRFElementalProduct__cl_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('cl_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__cl_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__v_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.v_mg_per_kg, name="xRFElementalProduct__v_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('v_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__v_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__cr_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.cr_mg_per_kg, name="xRFElementalProduct__cr_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('cr_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__cr_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__ni_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.ni_mg_per_kg, name="xRFElementalProduct__ni_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('ni_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__ni_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__cu_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.cu_mg_per_kg, name="xRFElementalProduct__cu_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('cu_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__cu_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__zn_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.zn_mg_per_kg, name="xRFElementalProduct__zn_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('zn_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__zn_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__ga_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.ga_mg_per_kg, name="xRFElementalProduct__ga_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('ga_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__ga_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__as_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.as_mg_per_kg, name="xRFElementalProduct__as_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('as_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__as_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__se_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.se_mg_per_kg, name="xRFElementalProduct__se_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('se_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__se_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__br_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.br_mg_per_kg, name="xRFElementalProduct__br_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('br_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__br_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__rb_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.rb_mg_per_kg, name="xRFElementalProduct__rb_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('rb_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__rb_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__sr_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.sr_mg_per_kg, name="xRFElementalProduct__sr_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('sr_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__sr_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__y_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.y_mg_per_kg, name="xRFElementalProduct__y_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('y_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__y_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__nb_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.nb_mg_per_kg, name="xRFElementalProduct__nb_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('nb_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__nb_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__mo_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.mo_mg_per_kg, name="xRFElementalProduct__mo_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('mo_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__mo_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__ag_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.ag_mg_per_kg, name="xRFElementalProduct__ag_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('ag_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__ag_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__cd_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.cd_mg_per_kg, name="xRFElementalProduct__cd_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('cd_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__cd_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__in_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.in_mg_per_kg, name="xRFElementalProduct__in_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('in_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__in_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__sn_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.sn_mg_per_kg, name="xRFElementalProduct__sn_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('sn_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__sn_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__sb_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.sb_mg_per_kg, name="xRFElementalProduct__sb_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('sb_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__sb_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__cs_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.cs_mg_per_kg, name="xRFElementalProduct__cs_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('cs_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__cs_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__ba_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.ba_mg_per_kg, name="xRFElementalProduct__ba_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('ba_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__ba_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__la_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.la_mg_per_kg, name="xRFElementalProduct__la_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('la_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__la_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__ce_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.ce_mg_per_kg, name="xRFElementalProduct__ce_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('ce_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__ce_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__pb_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.pb_mg_per_kg, name="xRFElementalProduct__pb_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('pb_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__pb_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__th_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.th_mg_per_kg, name="xRFElementalProduct__th_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('th_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__th_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__u_mg_per_kg = Slot(uri=ANALYSIS_API_SCHEMA.u_mg_per_kg, name="xRFElementalProduct__u_mg_per_kg", curie=ANALYSIS_API_SCHEMA.curie('u_mg_per_kg'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__u_mg_per_kg, domain=None, range=Optional[float])

slots.xRFElementalProduct__flag_cl = Slot(uri=ANALYSIS_API_SCHEMA.flag_cl, name="xRFElementalProduct__flag_cl", curie=ANALYSIS_API_SCHEMA.curie('flag_cl'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_cl, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_v = Slot(uri=ANALYSIS_API_SCHEMA.flag_v, name="xRFElementalProduct__flag_v", curie=ANALYSIS_API_SCHEMA.curie('flag_v'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_v, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_cr = Slot(uri=ANALYSIS_API_SCHEMA.flag_cr, name="xRFElementalProduct__flag_cr", curie=ANALYSIS_API_SCHEMA.curie('flag_cr'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_cr, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_ni = Slot(uri=ANALYSIS_API_SCHEMA.flag_ni, name="xRFElementalProduct__flag_ni", curie=ANALYSIS_API_SCHEMA.curie('flag_ni'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_ni, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_cu = Slot(uri=ANALYSIS_API_SCHEMA.flag_cu, name="xRFElementalProduct__flag_cu", curie=ANALYSIS_API_SCHEMA.curie('flag_cu'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_cu, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_zn = Slot(uri=ANALYSIS_API_SCHEMA.flag_zn, name="xRFElementalProduct__flag_zn", curie=ANALYSIS_API_SCHEMA.curie('flag_zn'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_zn, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_ga = Slot(uri=ANALYSIS_API_SCHEMA.flag_ga, name="xRFElementalProduct__flag_ga", curie=ANALYSIS_API_SCHEMA.curie('flag_ga'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_ga, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_as = Slot(uri=ANALYSIS_API_SCHEMA.flag_as, name="xRFElementalProduct__flag_as", curie=ANALYSIS_API_SCHEMA.curie('flag_as'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_as, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_se = Slot(uri=ANALYSIS_API_SCHEMA.flag_se, name="xRFElementalProduct__flag_se", curie=ANALYSIS_API_SCHEMA.curie('flag_se'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_se, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_br = Slot(uri=ANALYSIS_API_SCHEMA.flag_br, name="xRFElementalProduct__flag_br", curie=ANALYSIS_API_SCHEMA.curie('flag_br'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_br, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_rb = Slot(uri=ANALYSIS_API_SCHEMA.flag_rb, name="xRFElementalProduct__flag_rb", curie=ANALYSIS_API_SCHEMA.curie('flag_rb'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_rb, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_sr = Slot(uri=ANALYSIS_API_SCHEMA.flag_sr, name="xRFElementalProduct__flag_sr", curie=ANALYSIS_API_SCHEMA.curie('flag_sr'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_sr, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_y = Slot(uri=ANALYSIS_API_SCHEMA.flag_y, name="xRFElementalProduct__flag_y", curie=ANALYSIS_API_SCHEMA.curie('flag_y'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_y, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_nb = Slot(uri=ANALYSIS_API_SCHEMA.flag_nb, name="xRFElementalProduct__flag_nb", curie=ANALYSIS_API_SCHEMA.curie('flag_nb'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_nb, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_mo = Slot(uri=ANALYSIS_API_SCHEMA.flag_mo, name="xRFElementalProduct__flag_mo", curie=ANALYSIS_API_SCHEMA.curie('flag_mo'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_mo, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_ag = Slot(uri=ANALYSIS_API_SCHEMA.flag_ag, name="xRFElementalProduct__flag_ag", curie=ANALYSIS_API_SCHEMA.curie('flag_ag'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_ag, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_cd = Slot(uri=ANALYSIS_API_SCHEMA.flag_cd, name="xRFElementalProduct__flag_cd", curie=ANALYSIS_API_SCHEMA.curie('flag_cd'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_cd, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_in = Slot(uri=ANALYSIS_API_SCHEMA.flag_in, name="xRFElementalProduct__flag_in", curie=ANALYSIS_API_SCHEMA.curie('flag_in'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_in, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_sn = Slot(uri=ANALYSIS_API_SCHEMA.flag_sn, name="xRFElementalProduct__flag_sn", curie=ANALYSIS_API_SCHEMA.curie('flag_sn'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_sn, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_sb = Slot(uri=ANALYSIS_API_SCHEMA.flag_sb, name="xRFElementalProduct__flag_sb", curie=ANALYSIS_API_SCHEMA.curie('flag_sb'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_sb, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_cs = Slot(uri=ANALYSIS_API_SCHEMA.flag_cs, name="xRFElementalProduct__flag_cs", curie=ANALYSIS_API_SCHEMA.curie('flag_cs'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_cs, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_ba = Slot(uri=ANALYSIS_API_SCHEMA.flag_ba, name="xRFElementalProduct__flag_ba", curie=ANALYSIS_API_SCHEMA.curie('flag_ba'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_ba, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_la = Slot(uri=ANALYSIS_API_SCHEMA.flag_la, name="xRFElementalProduct__flag_la", curie=ANALYSIS_API_SCHEMA.curie('flag_la'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_la, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_ce = Slot(uri=ANALYSIS_API_SCHEMA.flag_ce, name="xRFElementalProduct__flag_ce", curie=ANALYSIS_API_SCHEMA.curie('flag_ce'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_ce, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_pb = Slot(uri=ANALYSIS_API_SCHEMA.flag_pb, name="xRFElementalProduct__flag_pb", curie=ANALYSIS_API_SCHEMA.curie('flag_pb'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_pb, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_th = Slot(uri=ANALYSIS_API_SCHEMA.flag_th, name="xRFElementalProduct__flag_th", curie=ANALYSIS_API_SCHEMA.curie('flag_th'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_th, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRFElementalProduct__flag_u = Slot(uri=ANALYSIS_API_SCHEMA.flag_u, name="xRFElementalProduct__flag_u", curie=ANALYSIS_API_SCHEMA.curie('flag_u'),
                   model_uri=ANALYSIS_API_SCHEMA.xRFElementalProduct__flag_u, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRDPhaseProduct__quartz_percent = Slot(uri=ANALYSIS_API_SCHEMA.quartz_percent, name="xRDPhaseProduct__quartz_percent", curie=ANALYSIS_API_SCHEMA.curie('quartz_percent'),
                   model_uri=ANALYSIS_API_SCHEMA.xRDPhaseProduct__quartz_percent, domain=None, range=Optional[float])

slots.xRDPhaseProduct__albite_percent = Slot(uri=ANALYSIS_API_SCHEMA.albite_percent, name="xRDPhaseProduct__albite_percent", curie=ANALYSIS_API_SCHEMA.curie('albite_percent'),
                   model_uri=ANALYSIS_API_SCHEMA.xRDPhaseProduct__albite_percent, domain=None, range=Optional[float])

slots.xRDPhaseProduct__microcline_percent = Slot(uri=ANALYSIS_API_SCHEMA.microcline_percent, name="xRDPhaseProduct__microcline_percent", curie=ANALYSIS_API_SCHEMA.curie('microcline_percent'),
                   model_uri=ANALYSIS_API_SCHEMA.xRDPhaseProduct__microcline_percent, domain=None, range=Optional[float])

slots.xRDPhaseProduct__muscovite_percent = Slot(uri=ANALYSIS_API_SCHEMA.muscovite_percent, name="xRDPhaseProduct__muscovite_percent", curie=ANALYSIS_API_SCHEMA.curie('muscovite_percent'),
                   model_uri=ANALYSIS_API_SCHEMA.xRDPhaseProduct__muscovite_percent, domain=None, range=Optional[float])

slots.xRDPhaseProduct__kaolinite_percent = Slot(uri=ANALYSIS_API_SCHEMA.kaolinite_percent, name="xRDPhaseProduct__kaolinite_percent", curie=ANALYSIS_API_SCHEMA.curie('kaolinite_percent'),
                   model_uri=ANALYSIS_API_SCHEMA.xRDPhaseProduct__kaolinite_percent, domain=None, range=Optional[float])

slots.xRDPhaseProduct__chlorite_percent = Slot(uri=ANALYSIS_API_SCHEMA.chlorite_percent, name="xRDPhaseProduct__chlorite_percent", curie=ANALYSIS_API_SCHEMA.curie('chlorite_percent'),
                   model_uri=ANALYSIS_API_SCHEMA.xRDPhaseProduct__chlorite_percent, domain=None, range=Optional[float])

slots.xRDPhaseProduct__hornblende_percent = Slot(uri=ANALYSIS_API_SCHEMA.hornblende_percent, name="xRDPhaseProduct__hornblende_percent", curie=ANALYSIS_API_SCHEMA.curie('hornblende_percent'),
                   model_uri=ANALYSIS_API_SCHEMA.xRDPhaseProduct__hornblende_percent, domain=None, range=Optional[float])

slots.xRDPhaseProduct__pyrite_percent = Slot(uri=ANALYSIS_API_SCHEMA.pyrite_percent, name="xRDPhaseProduct__pyrite_percent", curie=ANALYSIS_API_SCHEMA.curie('pyrite_percent'),
                   model_uri=ANALYSIS_API_SCHEMA.xRDPhaseProduct__pyrite_percent, domain=None, range=Optional[float])

slots.xRDPhaseProduct__halite_percent = Slot(uri=ANALYSIS_API_SCHEMA.halite_percent, name="xRDPhaseProduct__halite_percent", curie=ANALYSIS_API_SCHEMA.curie('halite_percent'),
                   model_uri=ANALYSIS_API_SCHEMA.xRDPhaseProduct__halite_percent, domain=None, range=Optional[float])

slots.xRDPhaseProduct__gypsum_percent = Slot(uri=ANALYSIS_API_SCHEMA.gypsum_percent, name="xRDPhaseProduct__gypsum_percent", curie=ANALYSIS_API_SCHEMA.curie('gypsum_percent'),
                   model_uri=ANALYSIS_API_SCHEMA.xRDPhaseProduct__gypsum_percent, domain=None, range=Optional[float])

slots.xRDPhaseProduct__flag_quartz = Slot(uri=ANALYSIS_API_SCHEMA.flag_quartz, name="xRDPhaseProduct__flag_quartz", curie=ANALYSIS_API_SCHEMA.curie('flag_quartz'),
                   model_uri=ANALYSIS_API_SCHEMA.xRDPhaseProduct__flag_quartz, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRDPhaseProduct__flag_albite = Slot(uri=ANALYSIS_API_SCHEMA.flag_albite, name="xRDPhaseProduct__flag_albite", curie=ANALYSIS_API_SCHEMA.curie('flag_albite'),
                   model_uri=ANALYSIS_API_SCHEMA.xRDPhaseProduct__flag_albite, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRDPhaseProduct__flag_microcline = Slot(uri=ANALYSIS_API_SCHEMA.flag_microcline, name="xRDPhaseProduct__flag_microcline", curie=ANALYSIS_API_SCHEMA.curie('flag_microcline'),
                   model_uri=ANALYSIS_API_SCHEMA.xRDPhaseProduct__flag_microcline, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRDPhaseProduct__flag_muscovite = Slot(uri=ANALYSIS_API_SCHEMA.flag_muscovite, name="xRDPhaseProduct__flag_muscovite", curie=ANALYSIS_API_SCHEMA.curie('flag_muscovite'),
                   model_uri=ANALYSIS_API_SCHEMA.xRDPhaseProduct__flag_muscovite, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRDPhaseProduct__flag_kaolinite = Slot(uri=ANALYSIS_API_SCHEMA.flag_kaolinite, name="xRDPhaseProduct__flag_kaolinite", curie=ANALYSIS_API_SCHEMA.curie('flag_kaolinite'),
                   model_uri=ANALYSIS_API_SCHEMA.xRDPhaseProduct__flag_kaolinite, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRDPhaseProduct__flag_chlorite = Slot(uri=ANALYSIS_API_SCHEMA.flag_chlorite, name="xRDPhaseProduct__flag_chlorite", curie=ANALYSIS_API_SCHEMA.curie('flag_chlorite'),
                   model_uri=ANALYSIS_API_SCHEMA.xRDPhaseProduct__flag_chlorite, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRDPhaseProduct__flag_hornblende = Slot(uri=ANALYSIS_API_SCHEMA.flag_hornblende, name="xRDPhaseProduct__flag_hornblende", curie=ANALYSIS_API_SCHEMA.curie('flag_hornblende'),
                   model_uri=ANALYSIS_API_SCHEMA.xRDPhaseProduct__flag_hornblende, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRDPhaseProduct__flag_pyrite = Slot(uri=ANALYSIS_API_SCHEMA.flag_pyrite, name="xRDPhaseProduct__flag_pyrite", curie=ANALYSIS_API_SCHEMA.curie('flag_pyrite'),
                   model_uri=ANALYSIS_API_SCHEMA.xRDPhaseProduct__flag_pyrite, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRDPhaseProduct__flag_halite = Slot(uri=ANALYSIS_API_SCHEMA.flag_halite, name="xRDPhaseProduct__flag_halite", curie=ANALYSIS_API_SCHEMA.curie('flag_halite'),
                   model_uri=ANALYSIS_API_SCHEMA.xRDPhaseProduct__flag_halite, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.xRDPhaseProduct__flag_gypsum = Slot(uri=ANALYSIS_API_SCHEMA.flag_gypsum, name="xRDPhaseProduct__flag_gypsum", curie=ANALYSIS_API_SCHEMA.curie('flag_gypsum'),
                   model_uri=ANALYSIS_API_SCHEMA.xRDPhaseProduct__flag_gypsum, domain=None, range=Optional[Union[str, "ProcessedDataFlag"]])

slots.site__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="site__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.site__id, domain=None, range=URIRef)

slots.sample__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="sample__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.sample__id, domain=None, range=URIRef)

slots.aerosolArmSample__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="aerosolArmSample__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.aerosolArmSample__id, domain=None, range=URIRef)

slots.aerosolSample__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="aerosolSample__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.aerosolSample__id, domain=None, range=URIRef)

slots.aMP2UserSample__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="aMP2UserSample__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.aMP2UserSample__id, domain=None, range=URIRef)

slots.commerciallyPurchasedSample__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="commerciallyPurchasedSample__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.commerciallyPurchasedSample__id, domain=None, range=URIRef)

slots.cultureEnvironmentalSample__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="cultureEnvironmentalSample__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.cultureEnvironmentalSample__id, domain=None, range=URIRef)

slots.engineeredStrainSample__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="engineeredStrainSample__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.engineeredStrainSample__id, domain=None, range=URIRef)

slots.engineeredStrainSample__cbi = Slot(uri=ANALYSIS_API_SCHEMA.cbi, name="engineeredStrainSample__cbi", curie=ANALYSIS_API_SCHEMA.curie('cbi'),
                   model_uri=ANALYSIS_API_SCHEMA.engineeredStrainSample__cbi, domain=None, range=str)

slots.engineeredStrainSample__storage_condition = Slot(uri=ANALYSIS_API_SCHEMA.storage_condition, name="engineeredStrainSample__storage_condition", curie=ANALYSIS_API_SCHEMA.curie('storage_condition'),
                   model_uri=ANALYSIS_API_SCHEMA.engineeredStrainSample__storage_condition, domain=None, range=str)

slots.engineeredStrainSample__storage_temperature = Slot(uri=ANALYSIS_API_SCHEMA.storage_temperature, name="engineeredStrainSample__storage_temperature", curie=ANALYSIS_API_SCHEMA.curie('storage_temperature'),
                   model_uri=ANALYSIS_API_SCHEMA.engineeredStrainSample__storage_temperature, domain=None, range=Optional[str])

slots.fieldDeployedTerraformSample__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="fieldDeployedTerraformSample__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.fieldDeployedTerraformSample__id, domain=None, range=URIRef)

slots.mixedCultureSample__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="mixedCultureSample__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.mixedCultureSample__id, domain=None, range=URIRef)

slots.monetSoilSample__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="monetSoilSample__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.monetSoilSample__id, domain=None, range=URIRef)

slots.otherUndescribedSample__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="otherUndescribedSample__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.otherUndescribedSample__id, domain=None, range=URIRef)

slots.plantSample__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="plantSample__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.plantSample__id, domain=None, range=URIRef)

slots.pureCultureSample__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="pureCultureSample__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.pureCultureSample__id, domain=None, range=URIRef)

slots.sedimentSample__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="sedimentSample__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.sedimentSample__id, domain=None, range=URIRef)

slots.soilSample__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="soilSample__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.soilSample__id, domain=None, range=URIRef)

slots.synthesizedMaterialSample__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="synthesizedMaterialSample__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.synthesizedMaterialSample__id, domain=None, range=URIRef)

slots.terraformSample__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="terraformSample__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.terraformSample__id, domain=None, range=URIRef)

slots.waterSample__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="waterSample__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.waterSample__id, domain=None, range=URIRef)

slots.processedSample__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="processedSample__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.processedSample__id, domain=None, range=URIRef)

slots.coreSection__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="coreSection__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.coreSection__id, domain=None, range=URIRef)

slots.samplingActivity__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="samplingActivity__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.samplingActivity__id, domain=None, range=URIRef)

slots.aerosolArmSamplingActivity__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="aerosolArmSamplingActivity__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.aerosolArmSamplingActivity__id, domain=None, range=URIRef)

slots.aerosolSamplingActivity__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="aerosolSamplingActivity__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.aerosolSamplingActivity__id, domain=None, range=URIRef)

slots.commerciallyPurchasedSamplingActivity__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="commerciallyPurchasedSamplingActivity__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.commerciallyPurchasedSamplingActivity__id, domain=None, range=URIRef)

slots.cultureEnvironmentalSamplingActivity__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="cultureEnvironmentalSamplingActivity__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.cultureEnvironmentalSamplingActivity__id, domain=None, range=URIRef)

slots.engineeredStrainSamplingActivity__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="engineeredStrainSamplingActivity__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.engineeredStrainSamplingActivity__id, domain=None, range=URIRef)

slots.fieldDeployedTerraformSamplingActivity__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="fieldDeployedTerraformSamplingActivity__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.fieldDeployedTerraformSamplingActivity__id, domain=None, range=URIRef)

slots.mixedCultureSamplingActivity__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="mixedCultureSamplingActivity__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.mixedCultureSamplingActivity__id, domain=None, range=URIRef)

slots.monetSoilSamplingActivity__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="monetSoilSamplingActivity__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.monetSoilSamplingActivity__id, domain=None, range=URIRef)

slots.otherUndescribedSamplingActivity__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="otherUndescribedSamplingActivity__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.otherUndescribedSamplingActivity__id, domain=None, range=URIRef)

slots.plantSamplingActivity__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="plantSamplingActivity__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.plantSamplingActivity__id, domain=None, range=URIRef)

slots.pureCultureSamplingActivity__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="pureCultureSamplingActivity__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.pureCultureSamplingActivity__id, domain=None, range=URIRef)

slots.sedimentSamplingActivity__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="sedimentSamplingActivity__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.sedimentSamplingActivity__id, domain=None, range=URIRef)

slots.soilSamplingActivity__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="soilSamplingActivity__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.soilSamplingActivity__id, domain=None, range=URIRef)

slots.synthesizedMaterialSamplingActivity__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="synthesizedMaterialSamplingActivity__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.synthesizedMaterialSamplingActivity__id, domain=None, range=URIRef)

slots.terraformSamplingActivity__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="terraformSamplingActivity__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.terraformSamplingActivity__id, domain=None, range=URIRef)

slots.waterSamplingActivity__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="waterSamplingActivity__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.waterSamplingActivity__id, domain=None, range=URIRef)

slots.biologicalEntity__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="biologicalEntity__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.biologicalEntity__id, domain=None, range=URIRef)

slots.study__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="study__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.study__id, domain=None, range=URIRef)

slots.study__project_id = Slot(uri=ANALYSIS_API_SCHEMA.project_id, name="study__project_id", curie=ANALYSIS_API_SCHEMA.curie('project_id'),
                   model_uri=ANALYSIS_API_SCHEMA.study__project_id, domain=None, range=int)

slots.study__title = Slot(uri=ANALYSIS_API_SCHEMA.title, name="study__title", curie=ANALYSIS_API_SCHEMA.curie('title'),
                   model_uri=ANALYSIS_API_SCHEMA.study__title, domain=None, range=Optional[str])

slots.study__name = Slot(uri=ANALYSIS_API_SCHEMA.name, name="study__name", curie=ANALYSIS_API_SCHEMA.curie('name'),
                   model_uri=ANALYSIS_API_SCHEMA.study__name, domain=None, range=str)

slots.study__proposal_abstract = Slot(uri=ANALYSIS_API_SCHEMA.proposal_abstract, name="study__proposal_abstract", curie=ANALYSIS_API_SCHEMA.curie('proposal_abstract'),
                   model_uri=ANALYSIS_API_SCHEMA.study__proposal_abstract, domain=None, range=Optional[str])

slots.study__description = Slot(uri=ANALYSIS_API_SCHEMA.description, name="study__description", curie=ANALYSIS_API_SCHEMA.curie('description'),
                   model_uri=ANALYSIS_API_SCHEMA.study__description, domain=None, range=Optional[str])

slots.study__has_participants = Slot(uri=ANALYSIS_API_SCHEMA.has_participants, name="study__has_participants", curie=ANALYSIS_API_SCHEMA.curie('has_participants'),
                   model_uri=ANALYSIS_API_SCHEMA.study__has_participants, domain=None, range=Optional[Union[Union[str, ProjectParticipantId], list[Union[str, ProjectParticipantId]]]])

slots.study__principal_investigator = Slot(uri=ANALYSIS_API_SCHEMA.principal_investigator, name="study__principal_investigator", curie=ANALYSIS_API_SCHEMA.curie('principal_investigator'),
                   model_uri=ANALYSIS_API_SCHEMA.study__principal_investigator, domain=None, range=Union[str, PersonValueId])

slots.study__collaborating_institution = Slot(uri=ANALYSIS_API_SCHEMA.collaborating_institution, name="study__collaborating_institution", curie=ANALYSIS_API_SCHEMA.curie('collaborating_institution'),
                   model_uri=ANALYSIS_API_SCHEMA.study__collaborating_institution, domain=None, range=Optional[str])

slots.study__project_status = Slot(uri=ANALYSIS_API_SCHEMA.project_status, name="study__project_status", curie=ANALYSIS_API_SCHEMA.curie('project_status'),
                   model_uri=ANALYSIS_API_SCHEMA.study__project_status, domain=None, range=Optional[Union[str, "ProjectStatusEnum"]])

slots.study__project_start = Slot(uri=ANALYSIS_API_SCHEMA.project_start, name="study__project_start", curie=ANALYSIS_API_SCHEMA.curie('project_start'),
                   model_uri=ANALYSIS_API_SCHEMA.study__project_start, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.study__project_end = Slot(uri=ANALYSIS_API_SCHEMA.project_end, name="study__project_end", curie=ANALYSIS_API_SCHEMA.curie('project_end'),
                   model_uri=ANALYSIS_API_SCHEMA.study__project_end, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.study__associated_dois = Slot(uri=ANALYSIS_API_SCHEMA.associated_dois, name="study__associated_dois", curie=ANALYSIS_API_SCHEMA.curie('associated_dois'),
                   model_uri=ANALYSIS_API_SCHEMA.study__associated_dois, domain=None, range=Optional[Union[Union[dict, DOI], list[Union[dict, DOI]]]])

slots.study__funding_sources = Slot(uri=ANALYSIS_API_SCHEMA.funding_sources, name="study__funding_sources", curie=ANALYSIS_API_SCHEMA.curie('funding_sources'),
                   model_uri=ANALYSIS_API_SCHEMA.study__funding_sources, domain=None, range=Optional[Union[Union[dict, DOI], list[Union[dict, DOI]]]])

slots.projectParticipant__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="projectParticipant__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.projectParticipant__id, domain=None, range=URIRef)

slots.projectParticipant__role = Slot(uri=ANALYSIS_API_SCHEMA.role, name="projectParticipant__role", curie=ANALYSIS_API_SCHEMA.curie('role'),
                   model_uri=ANALYSIS_API_SCHEMA.projectParticipant__role, domain=None, range=Union[str, "NexusRoleEnum"])

slots.projectParticipant__person = Slot(uri=ANALYSIS_API_SCHEMA.person, name="projectParticipant__person", curie=ANALYSIS_API_SCHEMA.curie('person'),
                   model_uri=ANALYSIS_API_SCHEMA.projectParticipant__person, domain=None, range=Union[str, PersonValueId])

slots.dOI__doi_value = Slot(uri=ANALYSIS_API_SCHEMA.doi_value, name="dOI__doi_value", curie=ANALYSIS_API_SCHEMA.curie('doi_value'),
                   model_uri=ANALYSIS_API_SCHEMA.dOI__doi_value, domain=None, range=Union[str, URIorCURIE])

slots.dOI__doi_category = Slot(uri=ANALYSIS_API_SCHEMA.doi_category, name="dOI__doi_category", curie=ANALYSIS_API_SCHEMA.curie('doi_category'),
                   model_uri=ANALYSIS_API_SCHEMA.dOI__doi_category, domain=None, range=Optional[Union[str, "DoiCategoryEnum"]])

slots.dOI__doi_provider = Slot(uri=ANALYSIS_API_SCHEMA.doi_provider, name="dOI__doi_provider", curie=ANALYSIS_API_SCHEMA.curie('doi_provider'),
                   model_uri=ANALYSIS_API_SCHEMA.dOI__doi_provider, domain=None, range=Optional[Union[str, "DoiProviderEnum"]])

slots.timestampValue__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="timestampValue__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.timestampValue__id, domain=None, range=URIRef)

slots.timestampValue__description = Slot(uri=ANALYSIS_API_SCHEMA.description, name="timestampValue__description", curie=ANALYSIS_API_SCHEMA.curie('description'),
                   model_uri=ANALYSIS_API_SCHEMA.timestampValue__description, domain=None, range=Optional[str])

slots.timestampValue__has_raw_value = Slot(uri=ANALYSIS_API_SCHEMA.has_raw_value, name="timestampValue__has_raw_value", curie=ANALYSIS_API_SCHEMA.curie('has_raw_value'),
                   model_uri=ANALYSIS_API_SCHEMA.timestampValue__has_raw_value, domain=None, range=Optional[str])

slots.textValue__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="textValue__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.textValue__id, domain=None, range=URIRef)

slots.textValue__language = Slot(uri=ANALYSIS_API_SCHEMA.language, name="textValue__language", curie=ANALYSIS_API_SCHEMA.curie('language'),
                   model_uri=ANALYSIS_API_SCHEMA.textValue__language, domain=None, range=Optional[str])

slots.textValue__has_raw_value = Slot(uri=ANALYSIS_API_SCHEMA.has_raw_value, name="textValue__has_raw_value", curie=ANALYSIS_API_SCHEMA.curie('has_raw_value'),
                   model_uri=ANALYSIS_API_SCHEMA.textValue__has_raw_value, domain=None, range=Optional[str])

slots.softwareControlledTermValue__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="softwareControlledTermValue__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.softwareControlledTermValue__id, domain=None, range=URIRef)

slots.softwareControlledTermValue__has_raw_value = Slot(uri=ANALYSIS_API_SCHEMA.has_raw_value, name="softwareControlledTermValue__has_raw_value", curie=ANALYSIS_API_SCHEMA.curie('has_raw_value'),
                   model_uri=ANALYSIS_API_SCHEMA.softwareControlledTermValue__has_raw_value, domain=None, range=Optional[str])

slots.controlledTermValue__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="controlledTermValue__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.controlledTermValue__id, domain=None, range=URIRef)

slots.controlledTermValue__has_raw_value = Slot(uri=ANALYSIS_API_SCHEMA.has_raw_value, name="controlledTermValue__has_raw_value", curie=ANALYSIS_API_SCHEMA.curie('has_raw_value'),
                   model_uri=ANALYSIS_API_SCHEMA.controlledTermValue__has_raw_value, domain=None, range=Optional[str])

slots.controlledTermValue__term = Slot(uri=ANALYSIS_API_SCHEMA.term, name="controlledTermValue__term", curie=ANALYSIS_API_SCHEMA.curie('term'),
                   model_uri=ANALYSIS_API_SCHEMA.controlledTermValue__term, domain=None, range=Optional[str])

slots.controlledTermValue__term_id = Slot(uri=ANALYSIS_API_SCHEMA.term_id, name="controlledTermValue__term_id", curie=ANALYSIS_API_SCHEMA.curie('term_id'),
                   model_uri=ANALYSIS_API_SCHEMA.controlledTermValue__term_id, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.controlledTermValue__controlled_term_provider = Slot(uri=ANALYSIS_API_SCHEMA.controlled_term_provider, name="controlledTermValue__controlled_term_provider", curie=ANALYSIS_API_SCHEMA.curie('controlled_term_provider'),
                   model_uri=ANALYSIS_API_SCHEMA.controlledTermValue__controlled_term_provider, domain=None, range=Optional[str])

slots.personValue__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="personValue__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.personValue__id, domain=None, range=URIRef)

slots.personValue__first_name = Slot(uri=ANALYSIS_API_SCHEMA.first_name, name="personValue__first_name", curie=ANALYSIS_API_SCHEMA.curie('first_name'),
                   model_uri=ANALYSIS_API_SCHEMA.personValue__first_name, domain=None, range=str)

slots.personValue__last_name = Slot(uri=ANALYSIS_API_SCHEMA.last_name, name="personValue__last_name", curie=ANALYSIS_API_SCHEMA.curie('last_name'),
                   model_uri=ANALYSIS_API_SCHEMA.personValue__last_name, domain=None, range=str)

slots.personValue__middle_initial = Slot(uri=ANALYSIS_API_SCHEMA.middle_initial, name="personValue__middle_initial", curie=ANALYSIS_API_SCHEMA.curie('middle_initial'),
                   model_uri=ANALYSIS_API_SCHEMA.personValue__middle_initial, domain=None, range=Optional[str])

slots.personValue__orcid = Slot(uri=ANALYSIS_API_SCHEMA.orcid, name="personValue__orcid", curie=ANALYSIS_API_SCHEMA.curie('orcid'),
                   model_uri=ANALYSIS_API_SCHEMA.personValue__orcid, domain=None, range=Optional[str])

slots.personValue__profile_image_url = Slot(uri=ANALYSIS_API_SCHEMA.profile_image_url, name="personValue__profile_image_url", curie=ANALYSIS_API_SCHEMA.curie('profile_image_url'),
                   model_uri=ANALYSIS_API_SCHEMA.personValue__profile_image_url, domain=None, range=Optional[str])

slots.personValue__websites = Slot(uri=ANALYSIS_API_SCHEMA.websites, name="personValue__websites", curie=ANALYSIS_API_SCHEMA.curie('websites'),
                   model_uri=ANALYSIS_API_SCHEMA.personValue__websites, domain=None, range=Optional[str])

slots.quantityValue__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="quantityValue__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.quantityValue__id, domain=None, range=URIRef)

slots.quantityValue__has_value_unit = Slot(uri=ANALYSIS_API_SCHEMA.has_value_unit, name="quantityValue__has_value_unit", curie=ANALYSIS_API_SCHEMA.curie('has_value_unit'),
                   model_uri=ANALYSIS_API_SCHEMA.quantityValue__has_value_unit, domain=None, range=Optional[str])

slots.quantityValue__has_unit = Slot(uri=ANALYSIS_API_SCHEMA.has_unit, name="quantityValue__has_unit", curie=ANALYSIS_API_SCHEMA.curie('has_unit'),
                   model_uri=ANALYSIS_API_SCHEMA.quantityValue__has_unit, domain=None, range=Optional[str])

slots.quantityValue__has_numeric_value = Slot(uri=ANALYSIS_API_SCHEMA.has_numeric_value, name="quantityValue__has_numeric_value", curie=ANALYSIS_API_SCHEMA.curie('has_numeric_value'),
                   model_uri=ANALYSIS_API_SCHEMA.quantityValue__has_numeric_value, domain=None, range=Optional[float])

slots.quantityValue__has_minimum_numeric_value = Slot(uri=ANALYSIS_API_SCHEMA.has_minimum_numeric_value, name="quantityValue__has_minimum_numeric_value", curie=ANALYSIS_API_SCHEMA.curie('has_minimum_numeric_value'),
                   model_uri=ANALYSIS_API_SCHEMA.quantityValue__has_minimum_numeric_value, domain=None, range=Optional[float])

slots.quantityValue__has_maximum_numeric_value = Slot(uri=ANALYSIS_API_SCHEMA.has_maximum_numeric_value, name="quantityValue__has_maximum_numeric_value", curie=ANALYSIS_API_SCHEMA.curie('has_maximum_numeric_value'),
                   model_uri=ANALYSIS_API_SCHEMA.quantityValue__has_maximum_numeric_value, domain=None, range=Optional[float])

slots.quantityValue__has_raw_value = Slot(uri=ANALYSIS_API_SCHEMA.has_raw_value, name="quantityValue__has_raw_value", curie=ANALYSIS_API_SCHEMA.curie('has_raw_value'),
                   model_uri=ANALYSIS_API_SCHEMA.quantityValue__has_raw_value, domain=None, range=Optional[str])

slots.conditioningValue__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="conditioningValue__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.conditioningValue__id, domain=None, range=URIRef)

slots.conditioningValue__source_material = Slot(uri=ANALYSIS_API_SCHEMA.source_material, name="conditioningValue__source_material", curie=ANALYSIS_API_SCHEMA.curie('source_material'),
                   model_uri=ANALYSIS_API_SCHEMA.conditioningValue__source_material, domain=None, range=Optional[str])

slots.conditioningValue__instrument = Slot(uri=ANALYSIS_API_SCHEMA.instrument, name="conditioningValue__instrument", curie=ANALYSIS_API_SCHEMA.curie('instrument'),
                   model_uri=ANALYSIS_API_SCHEMA.conditioningValue__instrument, domain=None, range=Optional[str])

slots.conditioningValue__gas = Slot(uri=ANALYSIS_API_SCHEMA.gas, name="conditioningValue__gas", curie=ANALYSIS_API_SCHEMA.curie('gas'),
                   model_uri=ANALYSIS_API_SCHEMA.conditioningValue__gas, domain=None, range=Optional[str])

slots.conditioningValue__pressure = Slot(uri=ANALYSIS_API_SCHEMA.pressure, name="conditioningValue__pressure", curie=ANALYSIS_API_SCHEMA.curie('pressure'),
                   model_uri=ANALYSIS_API_SCHEMA.conditioningValue__pressure, domain=None, range=Optional[str])

slots.conditioningValue__has_raw_value = Slot(uri=ANALYSIS_API_SCHEMA.has_raw_value, name="conditioningValue__has_raw_value", curie=ANALYSIS_API_SCHEMA.curie('has_raw_value'),
                   model_uri=ANALYSIS_API_SCHEMA.conditioningValue__has_raw_value, domain=None, range=Optional[str])

slots.zipDownload__id = Slot(uri=ANALYSIS_API_SCHEMA.id, name="zipDownload__id", curie=ANALYSIS_API_SCHEMA.curie('id'),
                   model_uri=ANALYSIS_API_SCHEMA.zipDownload__id, domain=None, range=URIRef)

slots.zipDownload__time = Slot(uri=ANALYSIS_API_SCHEMA.time, name="zipDownload__time", curie=ANALYSIS_API_SCHEMA.curie('time'),
                   model_uri=ANALYSIS_API_SCHEMA.zipDownload__time, domain=None, range=Union[str, XSDDateTime])

slots.zipDownload__user = Slot(uri=ANALYSIS_API_SCHEMA.user, name="zipDownload__user", curie=ANALYSIS_API_SCHEMA.curie('user'),
                   model_uri=ANALYSIS_API_SCHEMA.zipDownload__user, domain=None, range=str)

slots.zipDownload__files = Slot(uri=ANALYSIS_API_SCHEMA.files, name="zipDownload__files", curie=ANALYSIS_API_SCHEMA.curie('files'),
                   model_uri=ANALYSIS_API_SCHEMA.zipDownload__files, domain=None, range=int)

slots.zipDownload__packages = Slot(uri=ANALYSIS_API_SCHEMA.packages, name="zipDownload__packages", curie=ANALYSIS_API_SCHEMA.curie('packages'),
                   model_uri=ANALYSIS_API_SCHEMA.zipDownload__packages, domain=None, range=Optional[str])

slots.InstrumentData_description = Slot(uri=ANALYSIS_API_SCHEMA.description, name="InstrumentData_description", curie=ANALYSIS_API_SCHEMA.curie('description'),
                   model_uri=ANALYSIS_API_SCHEMA.InstrumentData_description, domain=InstrumentData, range=str)

slots.DataProcessingActivity_description = Slot(uri=ANALYSIS_API_SCHEMA.description, name="DataProcessingActivity_description", curie=ANALYSIS_API_SCHEMA.curie('description'),
                   model_uri=ANALYSIS_API_SCHEMA.DataProcessingActivity_description, domain=DataProcessingActivity, range=Optional[str])

slots.NucleotideSequencing_external_identifiers = Slot(uri=ANALYSIS_API_SCHEMA.external_identifiers, name="NucleotideSequencing_external_identifiers", curie=ANALYSIS_API_SCHEMA.curie('external_identifiers'),
                   model_uri=ANALYSIS_API_SCHEMA.NucleotideSequencing_external_identifiers, domain=NucleotideSequencing, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.Site_elev = Slot(uri=ANALYSIS_API_SCHEMA.elev, name="Site_elev", curie=ANALYSIS_API_SCHEMA.curie('elev'),
                   model_uri=ANALYSIS_API_SCHEMA.Site_elev, domain=Site, range=str,
                   pattern=re.compile(r'^\d+(\.\d+)?\s*m$'))

slots.Site_geo_loc_name = Slot(uri=ANALYSIS_API_SCHEMA.geo_loc_name, name="Site_geo_loc_name", curie=ANALYSIS_API_SCHEMA.curie('geo_loc_name'),
                   model_uri=ANALYSIS_API_SCHEMA.Site_geo_loc_name, domain=Site, range=str,
                   pattern=re.compile(r'^([^\s-]{12}|[^\s-]+.+[^\s-]+):\s?([^\s-]{12}|[^\s-]+.+[^\s-]+)\s?([^\s-]{12}|[^\s-]+.+[^\s-]+)$'))

slots.Site_growth_facil = Slot(uri=ANALYSIS_API_SCHEMA.growth_facil, name="Site_growth_facil", curie=ANALYSIS_API_SCHEMA.curie('growth_facil'),
                   model_uri=ANALYSIS_API_SCHEMA.Site_growth_facil, domain=Site, range=Union[str, "GrowthFacilityEnum"])

slots.Site_latitude = Slot(uri=ANALYSIS_API_SCHEMA.latitude, name="Site_latitude", curie=ANALYSIS_API_SCHEMA.curie('latitude'),
                   model_uri=ANALYSIS_API_SCHEMA.Site_latitude, domain=Site, range=float)

slots.Site_longitude = Slot(uri=ANALYSIS_API_SCHEMA.longitude, name="Site_longitude", curie=ANALYSIS_API_SCHEMA.curie('longitude'),
                   model_uri=ANALYSIS_API_SCHEMA.Site_longitude, domain=Site, range=float)

slots.AerosolArmSample_analysis_type = Slot(uri=ANALYSIS_API_SCHEMA.analysis_type, name="AerosolArmSample_analysis_type", curie=ANALYSIS_API_SCHEMA.curie('analysis_type'),
                   model_uri=ANALYSIS_API_SCHEMA.AerosolArmSample_analysis_type, domain=AerosolArmSample, range=str)

slots.AerosolArmSample_carb_dioxide = Slot(uri=ANALYSIS_API_SCHEMA.carb_dioxide, name="AerosolArmSample_carb_dioxide", curie=ANALYSIS_API_SCHEMA.curie('carb_dioxide'),
                   model_uri=ANALYSIS_API_SCHEMA.AerosolArmSample_carb_dioxide, domain=AerosolArmSample, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.AerosolArmSample_carb_monoxide = Slot(uri=ANALYSIS_API_SCHEMA.carb_monoxide, name="AerosolArmSample_carb_monoxide", curie=ANALYSIS_API_SCHEMA.curie('carb_monoxide'),
                   model_uri=ANALYSIS_API_SCHEMA.AerosolArmSample_carb_monoxide, domain=AerosolArmSample, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.AerosolArmSample_size_frac_low = Slot(uri=ANALYSIS_API_SCHEMA.size_frac_low, name="AerosolArmSample_size_frac_low", curie=ANALYSIS_API_SCHEMA.curie('size_frac_low'),
                   model_uri=ANALYSIS_API_SCHEMA.AerosolArmSample_size_frac_low, domain=AerosolArmSample, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*um$'))

slots.AerosolArmSample_size_frac_up = Slot(uri=ANALYSIS_API_SCHEMA.size_frac_up, name="AerosolArmSample_size_frac_up", curie=ANALYSIS_API_SCHEMA.curie('size_frac_up'),
                   model_uri=ANALYSIS_API_SCHEMA.AerosolArmSample_size_frac_up, domain=AerosolArmSample, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*um$'))

slots.AerosolSample_analysis_type = Slot(uri=ANALYSIS_API_SCHEMA.analysis_type, name="AerosolSample_analysis_type", curie=ANALYSIS_API_SCHEMA.curie('analysis_type'),
                   model_uri=ANALYSIS_API_SCHEMA.AerosolSample_analysis_type, domain=AerosolSample, range=str)

slots.AerosolSample_size_frac_low = Slot(uri=ANALYSIS_API_SCHEMA.size_frac_low, name="AerosolSample_size_frac_low", curie=ANALYSIS_API_SCHEMA.curie('size_frac_low'),
                   model_uri=ANALYSIS_API_SCHEMA.AerosolSample_size_frac_low, domain=AerosolSample, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*um$'))

slots.AerosolSample_size_frac_up = Slot(uri=ANALYSIS_API_SCHEMA.size_frac_up, name="AerosolSample_size_frac_up", curie=ANALYSIS_API_SCHEMA.curie('size_frac_up'),
                   model_uri=ANALYSIS_API_SCHEMA.AerosolSample_size_frac_up, domain=AerosolSample, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*um$'))

slots.AMP2UserSample_biological_entity_ref = Slot(uri=ANALYSIS_API_SCHEMA.biological_entity_ref, name="AMP2UserSample_biological_entity_ref", curie=ANALYSIS_API_SCHEMA.curie('biological_entity_ref'),
                   model_uri=ANALYSIS_API_SCHEMA.AMP2UserSample_biological_entity_ref, domain=AMP2UserSample, range=Union[str, BiologicalEntityId])

slots.AMP2UserSample_storage_condition = Slot(uri=ANALYSIS_API_SCHEMA.storage_condition, name="AMP2UserSample_storage_condition", curie=ANALYSIS_API_SCHEMA.curie('storage_condition'),
                   model_uri=ANALYSIS_API_SCHEMA.AMP2UserSample_storage_condition, domain=AMP2UserSample, range=Union[str, "StorageConditionEnum"])

slots.AMP2UserSample_storage_temperature = Slot(uri=ANALYSIS_API_SCHEMA.storage_temperature, name="AMP2UserSample_storage_temperature", curie=ANALYSIS_API_SCHEMA.curie('storage_temperature'),
                   model_uri=ANALYSIS_API_SCHEMA.AMP2UserSample_storage_temperature, domain=AMP2UserSample, range=Optional[str])

slots.AMP2UserSample_name = Slot(uri=ANALYSIS_API_SCHEMA.name, name="AMP2UserSample_name", curie=ANALYSIS_API_SCHEMA.curie('name'),
                   model_uri=ANALYSIS_API_SCHEMA.AMP2UserSample_name, domain=AMP2UserSample, range=str)

slots.AMP2UserSample_collection_date = Slot(uri=ANALYSIS_API_SCHEMA.collection_date, name="AMP2UserSample_collection_date", curie=ANALYSIS_API_SCHEMA.curie('collection_date'),
                   model_uri=ANALYSIS_API_SCHEMA.AMP2UserSample_collection_date, domain=AMP2UserSample, range=Optional[Union[str, XSDDate]],
                   pattern=re.compile(r'^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$'))

slots.AMP2UserSample_analysis_type = Slot(uri=ANALYSIS_API_SCHEMA.analysis_type, name="AMP2UserSample_analysis_type", curie=ANALYSIS_API_SCHEMA.curie('analysis_type'),
                   model_uri=ANALYSIS_API_SCHEMA.AMP2UserSample_analysis_type, domain=AMP2UserSample, range=Optional[str])

slots.CommerciallyPurchasedSample_analysis_type = Slot(uri=ANALYSIS_API_SCHEMA.analysis_type, name="CommerciallyPurchasedSample_analysis_type", curie=ANALYSIS_API_SCHEMA.curie('analysis_type'),
                   model_uri=ANALYSIS_API_SCHEMA.CommerciallyPurchasedSample_analysis_type, domain=CommerciallyPurchasedSample, range=str)

slots.CommerciallyPurchasedSample_compound_name = Slot(uri=ANALYSIS_API_SCHEMA.compound_name, name="CommerciallyPurchasedSample_compound_name", curie=ANALYSIS_API_SCHEMA.curie('compound_name'),
                   model_uri=ANALYSIS_API_SCHEMA.CommerciallyPurchasedSample_compound_name, domain=CommerciallyPurchasedSample, range=str)

slots.CultureEnvironmentalSample_analysis_type = Slot(uri=ANALYSIS_API_SCHEMA.analysis_type, name="CultureEnvironmentalSample_analysis_type", curie=ANALYSIS_API_SCHEMA.curie('analysis_type'),
                   model_uri=ANALYSIS_API_SCHEMA.CultureEnvironmentalSample_analysis_type, domain=CultureEnvironmentalSample, range=str)

slots.CultureEnvironmentalSample_growth_medium = Slot(uri=ANALYSIS_API_SCHEMA.growth_medium, name="CultureEnvironmentalSample_growth_medium", curie=ANALYSIS_API_SCHEMA.curie('growth_medium'),
                   model_uri=ANALYSIS_API_SCHEMA.CultureEnvironmentalSample_growth_medium, domain=CultureEnvironmentalSample, range=str)

slots.CultureEnvironmentalSample_host_common_name = Slot(uri=ANALYSIS_API_SCHEMA.host_common_name, name="CultureEnvironmentalSample_host_common_name", curie=ANALYSIS_API_SCHEMA.curie('host_common_name'),
                   model_uri=ANALYSIS_API_SCHEMA.CultureEnvironmentalSample_host_common_name, domain=CultureEnvironmentalSample, range=str)

slots.CultureEnvironmentalSample_host_taxid = Slot(uri=ANALYSIS_API_SCHEMA.host_taxid, name="CultureEnvironmentalSample_host_taxid", curie=ANALYSIS_API_SCHEMA.curie('host_taxid'),
                   model_uri=ANALYSIS_API_SCHEMA.CultureEnvironmentalSample_host_taxid, domain=CultureEnvironmentalSample, range=str,
                   pattern=re.compile(r'NCBITaxon:\d+'))

slots.CultureEnvironmentalSample_isol_growth_condt = Slot(uri=ANALYSIS_API_SCHEMA.isol_growth_condt, name="CultureEnvironmentalSample_isol_growth_condt", curie=ANALYSIS_API_SCHEMA.curie('isol_growth_condt'),
                   model_uri=ANALYSIS_API_SCHEMA.CultureEnvironmentalSample_isol_growth_condt, domain=CultureEnvironmentalSample, range=str)

slots.CultureEnvironmentalSample_non_microb_biomass = Slot(uri=ANALYSIS_API_SCHEMA.non_microb_biomass, name="CultureEnvironmentalSample_non_microb_biomass", curie=ANALYSIS_API_SCHEMA.curie('non_microb_biomass'),
                   model_uri=ANALYSIS_API_SCHEMA.CultureEnvironmentalSample_non_microb_biomass, domain=CultureEnvironmentalSample, range=Optional[str])

slots.CultureEnvironmentalSample_start_date_inc = Slot(uri=ANALYSIS_API_SCHEMA.start_date_inc, name="CultureEnvironmentalSample_start_date_inc", curie=ANALYSIS_API_SCHEMA.curie('start_date_inc'),
                   model_uri=ANALYSIS_API_SCHEMA.CultureEnvironmentalSample_start_date_inc, domain=CultureEnvironmentalSample, range=str,
                   pattern=re.compile(r'^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$'))

slots.FieldDeployedTerraformSample_analysis_type = Slot(uri=ANALYSIS_API_SCHEMA.analysis_type, name="FieldDeployedTerraformSample_analysis_type", curie=ANALYSIS_API_SCHEMA.curie('analysis_type'),
                   model_uri=ANALYSIS_API_SCHEMA.FieldDeployedTerraformSample_analysis_type, domain=FieldDeployedTerraformSample, range=str)

slots.FieldDeployedTerraformSample_initiation_date_inoculation = Slot(uri=ANALYSIS_API_SCHEMA.initiation_date_inoculation, name="FieldDeployedTerraformSample_initiation_date_inoculation", curie=ANALYSIS_API_SCHEMA.curie('initiation_date_inoculation'),
                   model_uri=ANALYSIS_API_SCHEMA.FieldDeployedTerraformSample_initiation_date_inoculation, domain=FieldDeployedTerraformSample, range=str,
                   pattern=re.compile(r'^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$'))

slots.FieldDeployedTerraformSample_initiation_date_plant = Slot(uri=ANALYSIS_API_SCHEMA.initiation_date_plant, name="FieldDeployedTerraformSample_initiation_date_plant", curie=ANALYSIS_API_SCHEMA.curie('initiation_date_plant'),
                   model_uri=ANALYSIS_API_SCHEMA.FieldDeployedTerraformSample_initiation_date_plant, domain=FieldDeployedTerraformSample, range=str,
                   pattern=re.compile(r'^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$'))

slots.FieldDeployedTerraformSample_latitude = Slot(uri=ANALYSIS_API_SCHEMA.latitude, name="FieldDeployedTerraformSample_latitude", curie=ANALYSIS_API_SCHEMA.curie('latitude'),
                   model_uri=ANALYSIS_API_SCHEMA.FieldDeployedTerraformSample_latitude, domain=FieldDeployedTerraformSample, range=float)

slots.FieldDeployedTerraformSample_longitude = Slot(uri=ANALYSIS_API_SCHEMA.longitude, name="FieldDeployedTerraformSample_longitude", curie=ANALYSIS_API_SCHEMA.curie('longitude'),
                   model_uri=ANALYSIS_API_SCHEMA.FieldDeployedTerraformSample_longitude, domain=FieldDeployedTerraformSample, range=float)

slots.FieldDeployedTerraformSample_synth_env_assembly = Slot(uri=ANALYSIS_API_SCHEMA.synth_env_assembly, name="FieldDeployedTerraformSample_synth_env_assembly", curie=ANALYSIS_API_SCHEMA.curie('synth_env_assembly'),
                   model_uri=ANALYSIS_API_SCHEMA.FieldDeployedTerraformSample_synth_env_assembly, domain=FieldDeployedTerraformSample, range=str)

slots.FieldDeployedTerraformSample_synth_env_design = Slot(uri=ANALYSIS_API_SCHEMA.synth_env_design, name="FieldDeployedTerraformSample_synth_env_design", curie=ANALYSIS_API_SCHEMA.curie('synth_env_design'),
                   model_uri=ANALYSIS_API_SCHEMA.FieldDeployedTerraformSample_synth_env_design, domain=FieldDeployedTerraformSample, range=Union[str, "SyntheticEnvironmentEnum"])

slots.FieldDeployedTerraformSample_synth_env_design_method = Slot(uri=ANALYSIS_API_SCHEMA.synth_env_design_method, name="FieldDeployedTerraformSample_synth_env_design_method", curie=ANALYSIS_API_SCHEMA.curie('synth_env_design_method'),
                   model_uri=ANALYSIS_API_SCHEMA.FieldDeployedTerraformSample_synth_env_design_method, domain=FieldDeployedTerraformSample, range=str)

slots.FieldDeployedTerraformSample_synth_env_material = Slot(uri=ANALYSIS_API_SCHEMA.synth_env_material, name="FieldDeployedTerraformSample_synth_env_material", curie=ANALYSIS_API_SCHEMA.curie('synth_env_material'),
                   model_uri=ANALYSIS_API_SCHEMA.FieldDeployedTerraformSample_synth_env_material, domain=FieldDeployedTerraformSample, range=str)

slots.FieldDeployedTerraformSample_synth_env_treatment = Slot(uri=ANALYSIS_API_SCHEMA.synth_env_treatment, name="FieldDeployedTerraformSample_synth_env_treatment", curie=ANALYSIS_API_SCHEMA.curie('synth_env_treatment'),
                   model_uri=ANALYSIS_API_SCHEMA.FieldDeployedTerraformSample_synth_env_treatment, domain=FieldDeployedTerraformSample, range=str)

slots.FieldDeployedTerraformSample_synth_start_date = Slot(uri=ANALYSIS_API_SCHEMA.synth_start_date, name="FieldDeployedTerraformSample_synth_start_date", curie=ANALYSIS_API_SCHEMA.curie('synth_start_date'),
                   model_uri=ANALYSIS_API_SCHEMA.FieldDeployedTerraformSample_synth_start_date, domain=FieldDeployedTerraformSample, range=str,
                   pattern=re.compile(r'^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$'))

slots.MixedCultureSample_analysis_type = Slot(uri=ANALYSIS_API_SCHEMA.analysis_type, name="MixedCultureSample_analysis_type", curie=ANALYSIS_API_SCHEMA.curie('analysis_type'),
                   model_uri=ANALYSIS_API_SCHEMA.MixedCultureSample_analysis_type, domain=MixedCultureSample, range=str)

slots.MixedCultureSample_growth_medium = Slot(uri=ANALYSIS_API_SCHEMA.growth_medium, name="MixedCultureSample_growth_medium", curie=ANALYSIS_API_SCHEMA.curie('growth_medium'),
                   model_uri=ANALYSIS_API_SCHEMA.MixedCultureSample_growth_medium, domain=MixedCultureSample, range=str)

slots.MixedCultureSample_host_common_name = Slot(uri=ANALYSIS_API_SCHEMA.host_common_name, name="MixedCultureSample_host_common_name", curie=ANALYSIS_API_SCHEMA.curie('host_common_name'),
                   model_uri=ANALYSIS_API_SCHEMA.MixedCultureSample_host_common_name, domain=MixedCultureSample, range=str)

slots.MixedCultureSample_host_taxid = Slot(uri=ANALYSIS_API_SCHEMA.host_taxid, name="MixedCultureSample_host_taxid", curie=ANALYSIS_API_SCHEMA.curie('host_taxid'),
                   model_uri=ANALYSIS_API_SCHEMA.MixedCultureSample_host_taxid, domain=MixedCultureSample, range=str,
                   pattern=re.compile(r'NCBITaxon:\d+'))

slots.MixedCultureSample_isol_growth_condt = Slot(uri=ANALYSIS_API_SCHEMA.isol_growth_condt, name="MixedCultureSample_isol_growth_condt", curie=ANALYSIS_API_SCHEMA.curie('isol_growth_condt'),
                   model_uri=ANALYSIS_API_SCHEMA.MixedCultureSample_isol_growth_condt, domain=MixedCultureSample, range=str)

slots.MixedCultureSample_start_date_inc = Slot(uri=ANALYSIS_API_SCHEMA.start_date_inc, name="MixedCultureSample_start_date_inc", curie=ANALYSIS_API_SCHEMA.curie('start_date_inc'),
                   model_uri=ANALYSIS_API_SCHEMA.MixedCultureSample_start_date_inc, domain=MixedCultureSample, range=str,
                   pattern=re.compile(r'^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$'))

slots.MixedCultureSample_subspecf_gen_lin = Slot(uri=ANALYSIS_API_SCHEMA.subspecf_gen_lin, name="MixedCultureSample_subspecf_gen_lin", curie=ANALYSIS_API_SCHEMA.curie('subspecf_gen_lin'),
                   model_uri=ANALYSIS_API_SCHEMA.MixedCultureSample_subspecf_gen_lin, domain=MixedCultureSample, range=Optional[str])

slots.MonetSoilSample_bulk_elect_conductivity = Slot(uri=ANALYSIS_API_SCHEMA.bulk_elect_conductivity, name="MonetSoilSample_bulk_elect_conductivity", curie=ANALYSIS_API_SCHEMA.curie('bulk_elect_conductivity'),
                   model_uri=ANALYSIS_API_SCHEMA.MonetSoilSample_bulk_elect_conductivity, domain=MonetSoilSample, range=str,
                   pattern=re.compile(r'^\d+(\.\d+)?\s*mS/cm|did not collect|failed'))

slots.MonetSoilSample_depth = Slot(uri=ANALYSIS_API_SCHEMA.depth, name="MonetSoilSample_depth", curie=ANALYSIS_API_SCHEMA.curie('depth'),
                   model_uri=ANALYSIS_API_SCHEMA.MonetSoilSample_depth, domain=MonetSoilSample, range=str,
                   pattern=re.compile(r'^\d+(\.\d+)?-\d+(\.\d+)?\s*(m|cm)$'))

slots.MonetSoilSample_latitude = Slot(uri=ANALYSIS_API_SCHEMA.latitude, name="MonetSoilSample_latitude", curie=ANALYSIS_API_SCHEMA.curie('latitude'),
                   model_uri=ANALYSIS_API_SCHEMA.MonetSoilSample_latitude, domain=MonetSoilSample, range=float)

slots.MonetSoilSample_longitude = Slot(uri=ANALYSIS_API_SCHEMA.longitude, name="MonetSoilSample_longitude", curie=ANALYSIS_API_SCHEMA.curie('longitude'),
                   model_uri=ANALYSIS_API_SCHEMA.MonetSoilSample_longitude, domain=MonetSoilSample, range=float)

slots.MonetSoilSample_sampling_set = Slot(uri=ANALYSIS_API_SCHEMA.sampling_set, name="MonetSoilSample_sampling_set", curie=ANALYSIS_API_SCHEMA.curie('sampling_set'),
                   model_uri=ANALYSIS_API_SCHEMA.MonetSoilSample_sampling_set, domain=MonetSoilSample, range=int)

slots.MonetSoilSample_soil_sample_type = Slot(uri=ANALYSIS_API_SCHEMA.soil_sample_type, name="MonetSoilSample_soil_sample_type", curie=ANALYSIS_API_SCHEMA.curie('soil_sample_type'),
                   model_uri=ANALYSIS_API_SCHEMA.MonetSoilSample_soil_sample_type, domain=MonetSoilSample, range=Union[str, "SoilSampleTypeEnum"])

slots.MonetSoilSample_soil_type = Slot(uri=ANALYSIS_API_SCHEMA.soil_type, name="MonetSoilSample_soil_type", curie=ANALYSIS_API_SCHEMA.curie('soil_type'),
                   model_uri=ANALYSIS_API_SCHEMA.MonetSoilSample_soil_type, domain=MonetSoilSample, range=Union[str, "SoilTypeEnum"])

slots.MonetSoilSample_soil_type_meth = Slot(uri=ANALYSIS_API_SCHEMA.soil_type_meth, name="MonetSoilSample_soil_type_meth", curie=ANALYSIS_API_SCHEMA.curie('soil_type_meth'),
                   model_uri=ANALYSIS_API_SCHEMA.MonetSoilSample_soil_type_meth, domain=MonetSoilSample, range=str)

slots.MonetSoilSample_temp = Slot(uri=ANALYSIS_API_SCHEMA.temp, name="MonetSoilSample_temp", curie=ANALYSIS_API_SCHEMA.curie('temp'),
                   model_uri=ANALYSIS_API_SCHEMA.MonetSoilSample_temp, domain=MonetSoilSample, range=str,
                   pattern=re.compile(r'^-?\d+(\.\d+)?\s*C|did not collect|failed'))

slots.MonetSoilSample_water_content = Slot(uri=ANALYSIS_API_SCHEMA.water_content, name="MonetSoilSample_water_content", curie=ANALYSIS_API_SCHEMA.curie('water_content'),
                   model_uri=ANALYSIS_API_SCHEMA.MonetSoilSample_water_content, domain=MonetSoilSample, range=str,
                   pattern=re.compile(r'^\d+(\.\d+)?\s*m3/m3|did not collect|failed'))

slots.OtherUndescribedSample_analysis_type = Slot(uri=ANALYSIS_API_SCHEMA.analysis_type, name="OtherUndescribedSample_analysis_type", curie=ANALYSIS_API_SCHEMA.curie('analysis_type'),
                   model_uri=ANALYSIS_API_SCHEMA.OtherUndescribedSample_analysis_type, domain=OtherUndescribedSample, range=str)

slots.OtherUndescribedSample_carb_dioxide = Slot(uri=ANALYSIS_API_SCHEMA.carb_dioxide, name="OtherUndescribedSample_carb_dioxide", curie=ANALYSIS_API_SCHEMA.curie('carb_dioxide'),
                   model_uri=ANALYSIS_API_SCHEMA.OtherUndescribedSample_carb_dioxide, domain=OtherUndescribedSample, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(umol/L|ppm)$'))

slots.OtherUndescribedSample_carb_monoxide = Slot(uri=ANALYSIS_API_SCHEMA.carb_monoxide, name="OtherUndescribedSample_carb_monoxide", curie=ANALYSIS_API_SCHEMA.curie('carb_monoxide'),
                   model_uri=ANALYSIS_API_SCHEMA.OtherUndescribedSample_carb_monoxide, domain=OtherUndescribedSample, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(umol/L|ppm)$'))

slots.OtherUndescribedSample_latitude = Slot(uri=ANALYSIS_API_SCHEMA.latitude, name="OtherUndescribedSample_latitude", curie=ANALYSIS_API_SCHEMA.curie('latitude'),
                   model_uri=ANALYSIS_API_SCHEMA.OtherUndescribedSample_latitude, domain=OtherUndescribedSample, range=float)

slots.OtherUndescribedSample_longitude = Slot(uri=ANALYSIS_API_SCHEMA.longitude, name="OtherUndescribedSample_longitude", curie=ANALYSIS_API_SCHEMA.curie('longitude'),
                   model_uri=ANALYSIS_API_SCHEMA.OtherUndescribedSample_longitude, domain=OtherUndescribedSample, range=float)

slots.OtherUndescribedSample_oxygen = Slot(uri=ANALYSIS_API_SCHEMA.oxygen, name="OtherUndescribedSample_oxygen", curie=ANALYSIS_API_SCHEMA.curie('oxygen'),
                   model_uri=ANALYSIS_API_SCHEMA.OtherUndescribedSample_oxygen, domain=OtherUndescribedSample, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(mg/L|ppm)$'))

slots.OtherUndescribedSample_sample_type = Slot(uri=ANALYSIS_API_SCHEMA.sample_type, name="OtherUndescribedSample_sample_type", curie=ANALYSIS_API_SCHEMA.curie('sample_type'),
                   model_uri=ANALYSIS_API_SCHEMA.OtherUndescribedSample_sample_type, domain=OtherUndescribedSample, range=str,
                   pattern=re.compile(r'^_*\s*[a-zA-Z\-]+\s\[[a-zA-Z]+:\d+\]$'))

slots.OtherUndescribedSample_subspecf_gen_lin = Slot(uri=ANALYSIS_API_SCHEMA.subspecf_gen_lin, name="OtherUndescribedSample_subspecf_gen_lin", curie=ANALYSIS_API_SCHEMA.curie('subspecf_gen_lin'),
                   model_uri=ANALYSIS_API_SCHEMA.OtherUndescribedSample_subspecf_gen_lin, domain=OtherUndescribedSample, range=Optional[str])

slots.PlantSample_analysis_type = Slot(uri=ANALYSIS_API_SCHEMA.analysis_type, name="PlantSample_analysis_type", curie=ANALYSIS_API_SCHEMA.curie('analysis_type'),
                   model_uri=ANALYSIS_API_SCHEMA.PlantSample_analysis_type, domain=PlantSample, range=str)

slots.PlantSample_host_height = Slot(uri=ANALYSIS_API_SCHEMA.host_height, name="PlantSample_host_height", curie=ANALYSIS_API_SCHEMA.curie('host_height'),
                   model_uri=ANALYSIS_API_SCHEMA.PlantSample_host_height, domain=PlantSample, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(cm|mm|m)$'))

slots.PlantSample_host_length = Slot(uri=ANALYSIS_API_SCHEMA.host_length, name="PlantSample_host_length", curie=ANALYSIS_API_SCHEMA.curie('host_length'),
                   model_uri=ANALYSIS_API_SCHEMA.PlantSample_host_length, domain=PlantSample, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(cm|mm|m)$'))

slots.PlantSample_host_life_stage = Slot(uri=ANALYSIS_API_SCHEMA.host_life_stage, name="PlantSample_host_life_stage", curie=ANALYSIS_API_SCHEMA.curie('host_life_stage'),
                   model_uri=ANALYSIS_API_SCHEMA.PlantSample_host_life_stage, domain=PlantSample, range=Optional[str])

slots.PlantSample_latitude = Slot(uri=ANALYSIS_API_SCHEMA.latitude, name="PlantSample_latitude", curie=ANALYSIS_API_SCHEMA.curie('latitude'),
                   model_uri=ANALYSIS_API_SCHEMA.PlantSample_latitude, domain=PlantSample, range=float)

slots.PlantSample_longitude = Slot(uri=ANALYSIS_API_SCHEMA.longitude, name="PlantSample_longitude", curie=ANALYSIS_API_SCHEMA.curie('longitude'),
                   model_uri=ANALYSIS_API_SCHEMA.PlantSample_longitude, domain=PlantSample, range=float)

slots.PlantSample_non_microb_biomass = Slot(uri=ANALYSIS_API_SCHEMA.non_microb_biomass, name="PlantSample_non_microb_biomass", curie=ANALYSIS_API_SCHEMA.curie('non_microb_biomass'),
                   model_uri=ANALYSIS_API_SCHEMA.PlantSample_non_microb_biomass, domain=PlantSample, range=Optional[str])

slots.PlantSample_plant_common_name = Slot(uri=ANALYSIS_API_SCHEMA.plant_common_name, name="PlantSample_plant_common_name", curie=ANALYSIS_API_SCHEMA.curie('plant_common_name'),
                   model_uri=ANALYSIS_API_SCHEMA.PlantSample_plant_common_name, domain=PlantSample, range=str)

slots.PlantSample_plant_struc = Slot(uri=ANALYSIS_API_SCHEMA.plant_struc, name="PlantSample_plant_struc", curie=ANALYSIS_API_SCHEMA.curie('plant_struc'),
                   model_uri=ANALYSIS_API_SCHEMA.PlantSample_plant_struc, domain=PlantSample, range=Union[str, "PlantStructureEnum"])

slots.PlantSample_plant_taxid = Slot(uri=ANALYSIS_API_SCHEMA.plant_taxid, name="PlantSample_plant_taxid", curie=ANALYSIS_API_SCHEMA.curie('plant_taxid'),
                   model_uri=ANALYSIS_API_SCHEMA.PlantSample_plant_taxid, domain=PlantSample, range=str)

slots.PureCultureSample_analysis_type = Slot(uri=ANALYSIS_API_SCHEMA.analysis_type, name="PureCultureSample_analysis_type", curie=ANALYSIS_API_SCHEMA.curie('analysis_type'),
                   model_uri=ANALYSIS_API_SCHEMA.PureCultureSample_analysis_type, domain=PureCultureSample, range=str)

slots.PureCultureSample_growth_medium = Slot(uri=ANALYSIS_API_SCHEMA.growth_medium, name="PureCultureSample_growth_medium", curie=ANALYSIS_API_SCHEMA.curie('growth_medium'),
                   model_uri=ANALYSIS_API_SCHEMA.PureCultureSample_growth_medium, domain=PureCultureSample, range=str)

slots.PureCultureSample_host_common_name = Slot(uri=ANALYSIS_API_SCHEMA.host_common_name, name="PureCultureSample_host_common_name", curie=ANALYSIS_API_SCHEMA.curie('host_common_name'),
                   model_uri=ANALYSIS_API_SCHEMA.PureCultureSample_host_common_name, domain=PureCultureSample, range=str)

slots.PureCultureSample_host_taxid = Slot(uri=ANALYSIS_API_SCHEMA.host_taxid, name="PureCultureSample_host_taxid", curie=ANALYSIS_API_SCHEMA.curie('host_taxid'),
                   model_uri=ANALYSIS_API_SCHEMA.PureCultureSample_host_taxid, domain=PureCultureSample, range=str,
                   pattern=re.compile(r'NCBITaxon:\d+'))

slots.PureCultureSample_isol_growth_condt = Slot(uri=ANALYSIS_API_SCHEMA.isol_growth_condt, name="PureCultureSample_isol_growth_condt", curie=ANALYSIS_API_SCHEMA.curie('isol_growth_condt'),
                   model_uri=ANALYSIS_API_SCHEMA.PureCultureSample_isol_growth_condt, domain=PureCultureSample, range=str)

slots.PureCultureSample_non_microb_biomass = Slot(uri=ANALYSIS_API_SCHEMA.non_microb_biomass, name="PureCultureSample_non_microb_biomass", curie=ANALYSIS_API_SCHEMA.curie('non_microb_biomass'),
                   model_uri=ANALYSIS_API_SCHEMA.PureCultureSample_non_microb_biomass, domain=PureCultureSample, range=Optional[str])

slots.PureCultureSample_start_date_inc = Slot(uri=ANALYSIS_API_SCHEMA.start_date_inc, name="PureCultureSample_start_date_inc", curie=ANALYSIS_API_SCHEMA.curie('start_date_inc'),
                   model_uri=ANALYSIS_API_SCHEMA.PureCultureSample_start_date_inc, domain=PureCultureSample, range=str,
                   pattern=re.compile(r'^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$'))

slots.SedimentSample_analysis_type = Slot(uri=ANALYSIS_API_SCHEMA.analysis_type, name="SedimentSample_analysis_type", curie=ANALYSIS_API_SCHEMA.curie('analysis_type'),
                   model_uri=ANALYSIS_API_SCHEMA.SedimentSample_analysis_type, domain=SedimentSample, range=str)

slots.SedimentSample_depth = Slot(uri=ANALYSIS_API_SCHEMA.depth, name="SedimentSample_depth", curie=ANALYSIS_API_SCHEMA.curie('depth'),
                   model_uri=ANALYSIS_API_SCHEMA.SedimentSample_depth, domain=SedimentSample, range=str,
                   pattern=re.compile(r'^\d+(\.\d+)?-\d+(\.\d+)?\s*m$'))

slots.SedimentSample_latitude = Slot(uri=ANALYSIS_API_SCHEMA.latitude, name="SedimentSample_latitude", curie=ANALYSIS_API_SCHEMA.curie('latitude'),
                   model_uri=ANALYSIS_API_SCHEMA.SedimentSample_latitude, domain=SedimentSample, range=float)

slots.SedimentSample_longitude = Slot(uri=ANALYSIS_API_SCHEMA.longitude, name="SedimentSample_longitude", curie=ANALYSIS_API_SCHEMA.curie('longitude'),
                   model_uri=ANALYSIS_API_SCHEMA.SedimentSample_longitude, domain=SedimentSample, range=float)

slots.SedimentSample_microbial_biomass = Slot(uri=ANALYSIS_API_SCHEMA.microbial_biomass, name="SedimentSample_microbial_biomass", curie=ANALYSIS_API_SCHEMA.curie('microbial_biomass'),
                   model_uri=ANALYSIS_API_SCHEMA.SedimentSample_microbial_biomass, domain=SedimentSample, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(g/kg sediment|ug/g sediment)$'))

slots.SedimentSample_non_microb_biomass = Slot(uri=ANALYSIS_API_SCHEMA.non_microb_biomass, name="SedimentSample_non_microb_biomass", curie=ANALYSIS_API_SCHEMA.curie('non_microb_biomass'),
                   model_uri=ANALYSIS_API_SCHEMA.SedimentSample_non_microb_biomass, domain=SedimentSample, range=Optional[str],
                   pattern=re.compile(r'^(\S+\s+\d+\s*\S+)(;\s*\S+\s+\d+\s*\S+)*$'))

slots.SedimentSample_biotic_relationship = Slot(uri=ANALYSIS_API_SCHEMA.biotic_relationship, name="SedimentSample_biotic_relationship", curie=ANALYSIS_API_SCHEMA.curie('biotic_relationship'),
                   model_uri=ANALYSIS_API_SCHEMA.SedimentSample_biotic_relationship, domain=SedimentSample, range=Optional[Union[str, "BioticRelationshipEnum"]])

slots.SoilSample_al_sat = Slot(uri=ANALYSIS_API_SCHEMA.al_sat, name="SoilSample_al_sat", curie=ANALYSIS_API_SCHEMA.curie('al_sat'),
                   model_uri=ANALYSIS_API_SCHEMA.SoilSample_al_sat, domain=SoilSample, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*percent$'))

slots.SoilSample_analysis_type = Slot(uri=ANALYSIS_API_SCHEMA.analysis_type, name="SoilSample_analysis_type", curie=ANALYSIS_API_SCHEMA.curie('analysis_type'),
                   model_uri=ANALYSIS_API_SCHEMA.SoilSample_analysis_type, domain=SoilSample, range=str)

slots.SoilSample_depth = Slot(uri=ANALYSIS_API_SCHEMA.depth, name="SoilSample_depth", curie=ANALYSIS_API_SCHEMA.curie('depth'),
                   model_uri=ANALYSIS_API_SCHEMA.SoilSample_depth, domain=SoilSample, range=str,
                   pattern=re.compile(r'^\d+(\.\d+)?-\d+(\.\d+)?\s*m$'))

slots.SoilSample_heavy_metals = Slot(uri=ANALYSIS_API_SCHEMA.heavy_metals, name="SoilSample_heavy_metals", curie=ANALYSIS_API_SCHEMA.curie('heavy_metals'),
                   model_uri=ANALYSIS_API_SCHEMA.SoilSample_heavy_metals, domain=SoilSample, range=Optional[str])

slots.SoilSample_latitude = Slot(uri=ANALYSIS_API_SCHEMA.latitude, name="SoilSample_latitude", curie=ANALYSIS_API_SCHEMA.curie('latitude'),
                   model_uri=ANALYSIS_API_SCHEMA.SoilSample_latitude, domain=SoilSample, range=float)

slots.SoilSample_longitude = Slot(uri=ANALYSIS_API_SCHEMA.longitude, name="SoilSample_longitude", curie=ANALYSIS_API_SCHEMA.curie('longitude'),
                   model_uri=ANALYSIS_API_SCHEMA.SoilSample_longitude, domain=SoilSample, range=float)

slots.SoilSample_microbial_biomass = Slot(uri=ANALYSIS_API_SCHEMA.microbial_biomass, name="SoilSample_microbial_biomass", curie=ANALYSIS_API_SCHEMA.curie('microbial_biomass'),
                   model_uri=ANALYSIS_API_SCHEMA.SoilSample_microbial_biomass, domain=SoilSample, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*(g/kg soil|ug/g dry soil)$'))

slots.SoilSample_non_microb_biomass = Slot(uri=ANALYSIS_API_SCHEMA.non_microb_biomass, name="SoilSample_non_microb_biomass", curie=ANALYSIS_API_SCHEMA.curie('non_microb_biomass'),
                   model_uri=ANALYSIS_API_SCHEMA.SoilSample_non_microb_biomass, domain=SoilSample, range=Optional[str],
                   pattern=re.compile(r'^(\S+\s+\d+\s*\S+)(;\s*\S+\s+\d+\s*\S+)*$'))

slots.SoilSample_size_frac_low = Slot(uri=ANALYSIS_API_SCHEMA.size_frac_low, name="SoilSample_size_frac_low", curie=ANALYSIS_API_SCHEMA.curie('size_frac_low'),
                   model_uri=ANALYSIS_API_SCHEMA.SoilSample_size_frac_low, domain=SoilSample, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*um$'))

slots.SoilSample_size_frac_up = Slot(uri=ANALYSIS_API_SCHEMA.size_frac_up, name="SoilSample_size_frac_up", curie=ANALYSIS_API_SCHEMA.curie('size_frac_up'),
                   model_uri=ANALYSIS_API_SCHEMA.SoilSample_size_frac_up, domain=SoilSample, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*um$'))

slots.SynthesizedMaterialSample_analysis_type = Slot(uri=ANALYSIS_API_SCHEMA.analysis_type, name="SynthesizedMaterialSample_analysis_type", curie=ANALYSIS_API_SCHEMA.curie('analysis_type'),
                   model_uri=ANALYSIS_API_SCHEMA.SynthesizedMaterialSample_analysis_type, domain=SynthesizedMaterialSample, range=str)

slots.SynthesizedMaterialSample_synth_instrument = Slot(uri=ANALYSIS_API_SCHEMA.synth_instrument, name="SynthesizedMaterialSample_synth_instrument", curie=ANALYSIS_API_SCHEMA.curie('synth_instrument'),
                   model_uri=ANALYSIS_API_SCHEMA.SynthesizedMaterialSample_synth_instrument, domain=SynthesizedMaterialSample, range=str)

slots.SynthesizedMaterialSample_synth_reagents = Slot(uri=ANALYSIS_API_SCHEMA.synth_reagents, name="SynthesizedMaterialSample_synth_reagents", curie=ANALYSIS_API_SCHEMA.curie('synth_reagents'),
                   model_uri=ANALYSIS_API_SCHEMA.SynthesizedMaterialSample_synth_reagents, domain=SynthesizedMaterialSample, range=str)

slots.TerraformSample_analysis_type = Slot(uri=ANALYSIS_API_SCHEMA.analysis_type, name="TerraformSample_analysis_type", curie=ANALYSIS_API_SCHEMA.curie('analysis_type'),
                   model_uri=ANALYSIS_API_SCHEMA.TerraformSample_analysis_type, domain=TerraformSample, range=str)

slots.TerraformSample_initiation_date_inoculation = Slot(uri=ANALYSIS_API_SCHEMA.initiation_date_inoculation, name="TerraformSample_initiation_date_inoculation", curie=ANALYSIS_API_SCHEMA.curie('initiation_date_inoculation'),
                   model_uri=ANALYSIS_API_SCHEMA.TerraformSample_initiation_date_inoculation, domain=TerraformSample, range=str,
                   pattern=re.compile(r'^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$'))

slots.TerraformSample_initiation_date_plant = Slot(uri=ANALYSIS_API_SCHEMA.initiation_date_plant, name="TerraformSample_initiation_date_plant", curie=ANALYSIS_API_SCHEMA.curie('initiation_date_plant'),
                   model_uri=ANALYSIS_API_SCHEMA.TerraformSample_initiation_date_plant, domain=TerraformSample, range=str,
                   pattern=re.compile(r'^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$'))

slots.TerraformSample_synth_env_assembly = Slot(uri=ANALYSIS_API_SCHEMA.synth_env_assembly, name="TerraformSample_synth_env_assembly", curie=ANALYSIS_API_SCHEMA.curie('synth_env_assembly'),
                   model_uri=ANALYSIS_API_SCHEMA.TerraformSample_synth_env_assembly, domain=TerraformSample, range=str)

slots.TerraformSample_synth_env_design = Slot(uri=ANALYSIS_API_SCHEMA.synth_env_design, name="TerraformSample_synth_env_design", curie=ANALYSIS_API_SCHEMA.curie('synth_env_design'),
                   model_uri=ANALYSIS_API_SCHEMA.TerraformSample_synth_env_design, domain=TerraformSample, range=Union[str, "SyntheticEnvironmentEnum"])

slots.TerraformSample_synth_env_design_method = Slot(uri=ANALYSIS_API_SCHEMA.synth_env_design_method, name="TerraformSample_synth_env_design_method", curie=ANALYSIS_API_SCHEMA.curie('synth_env_design_method'),
                   model_uri=ANALYSIS_API_SCHEMA.TerraformSample_synth_env_design_method, domain=TerraformSample, range=str)

slots.TerraformSample_synth_env_material = Slot(uri=ANALYSIS_API_SCHEMA.synth_env_material, name="TerraformSample_synth_env_material", curie=ANALYSIS_API_SCHEMA.curie('synth_env_material'),
                   model_uri=ANALYSIS_API_SCHEMA.TerraformSample_synth_env_material, domain=TerraformSample, range=str)

slots.TerraformSample_synth_env_treatment = Slot(uri=ANALYSIS_API_SCHEMA.synth_env_treatment, name="TerraformSample_synth_env_treatment", curie=ANALYSIS_API_SCHEMA.curie('synth_env_treatment'),
                   model_uri=ANALYSIS_API_SCHEMA.TerraformSample_synth_env_treatment, domain=TerraformSample, range=str)

slots.TerraformSample_synth_start_date = Slot(uri=ANALYSIS_API_SCHEMA.synth_start_date, name="TerraformSample_synth_start_date", curie=ANALYSIS_API_SCHEMA.curie('synth_start_date'),
                   model_uri=ANALYSIS_API_SCHEMA.TerraformSample_synth_start_date, domain=TerraformSample, range=str,
                   pattern=re.compile(r'^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$'))

slots.WaterSample_analysis_type = Slot(uri=ANALYSIS_API_SCHEMA.analysis_type, name="WaterSample_analysis_type", curie=ANALYSIS_API_SCHEMA.curie('analysis_type'),
                   model_uri=ANALYSIS_API_SCHEMA.WaterSample_analysis_type, domain=WaterSample, range=str)

slots.WaterSample_depth = Slot(uri=ANALYSIS_API_SCHEMA.depth, name="WaterSample_depth", curie=ANALYSIS_API_SCHEMA.curie('depth'),
                   model_uri=ANALYSIS_API_SCHEMA.WaterSample_depth, domain=WaterSample, range=str,
                   pattern=re.compile(r'^\d+(\.\d+)?(-\d+(\.\d+)?)?\s*m$'))

slots.WaterSample_filter_method = Slot(uri=ANALYSIS_API_SCHEMA.filter_method, name="WaterSample_filter_method", curie=ANALYSIS_API_SCHEMA.curie('filter_method'),
                   model_uri=ANALYSIS_API_SCHEMA.WaterSample_filter_method, domain=WaterSample, range=str)

slots.WaterSample_latitude = Slot(uri=ANALYSIS_API_SCHEMA.latitude, name="WaterSample_latitude", curie=ANALYSIS_API_SCHEMA.curie('latitude'),
                   model_uri=ANALYSIS_API_SCHEMA.WaterSample_latitude, domain=WaterSample, range=float)

slots.WaterSample_longitude = Slot(uri=ANALYSIS_API_SCHEMA.longitude, name="WaterSample_longitude", curie=ANALYSIS_API_SCHEMA.curie('longitude'),
                   model_uri=ANALYSIS_API_SCHEMA.WaterSample_longitude, domain=WaterSample, range=float)

slots.WaterSample_non_microb_biomass = Slot(uri=ANALYSIS_API_SCHEMA.non_microb_biomass, name="WaterSample_non_microb_biomass", curie=ANALYSIS_API_SCHEMA.curie('non_microb_biomass'),
                   model_uri=ANALYSIS_API_SCHEMA.WaterSample_non_microb_biomass, domain=WaterSample, range=Optional[str],
                   pattern=re.compile(r'^(\S+\s+\d+\s*\S+)(;\s*\S+\s+\d+\s*\S+)*$'))

slots.WaterSample_size_frac_low = Slot(uri=ANALYSIS_API_SCHEMA.size_frac_low, name="WaterSample_size_frac_low", curie=ANALYSIS_API_SCHEMA.curie('size_frac_low'),
                   model_uri=ANALYSIS_API_SCHEMA.WaterSample_size_frac_low, domain=WaterSample, range=str,
                   pattern=re.compile(r'^\d+(\.\d+)?\s*um$'))

slots.WaterSample_size_frac_up = Slot(uri=ANALYSIS_API_SCHEMA.size_frac_up, name="WaterSample_size_frac_up", curie=ANALYSIS_API_SCHEMA.curie('size_frac_up'),
                   model_uri=ANALYSIS_API_SCHEMA.WaterSample_size_frac_up, domain=WaterSample, range=str,
                   pattern=re.compile(r'^\d+(\.\d+)?\s*um$'))

slots.ProcessedSample_replicate = Slot(uri=ANALYSIS_API_SCHEMA.replicate, name="ProcessedSample_replicate", curie=ANALYSIS_API_SCHEMA.curie('replicate'),
                   model_uri=ANALYSIS_API_SCHEMA.ProcessedSample_replicate, domain=ProcessedSample, range=Optional[int])

slots.ProcessedSample_sampled_during = Slot(uri=ANALYSIS_API_SCHEMA.sampled_during, name="ProcessedSample_sampled_during", curie=ANALYSIS_API_SCHEMA.curie('sampled_during'),
                   model_uri=ANALYSIS_API_SCHEMA.ProcessedSample_sampled_during, domain=ProcessedSample, range=Optional[Union[str, SampleProcessingId]])

slots.CoreSection_core_section = Slot(uri=ANALYSIS_API_SCHEMA.core_section, name="CoreSection_core_section", curie=ANALYSIS_API_SCHEMA.curie('core_section'),
                   model_uri=ANALYSIS_API_SCHEMA.CoreSection_core_section, domain=CoreSection, range=Union[str, "CoreSectionEnum"])

slots.AerosolArmSamplingActivity_humidity = Slot(uri=ANALYSIS_API_SCHEMA.humidity, name="AerosolArmSamplingActivity_humidity", curie=ANALYSIS_API_SCHEMA.curie('humidity'),
                   model_uri=ANALYSIS_API_SCHEMA.AerosolArmSamplingActivity_humidity, domain=AerosolArmSamplingActivity, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.MonetSoilSamplingActivity_collection_time = Slot(uri=ANALYSIS_API_SCHEMA.collection_time, name="MonetSoilSamplingActivity_collection_time", curie=ANALYSIS_API_SCHEMA.curie('collection_time'),
                   model_uri=ANALYSIS_API_SCHEMA.MonetSoilSamplingActivity_collection_time, domain=MonetSoilSamplingActivity, range=str,
                   pattern=re.compile(r'^(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])\s*(hh:mm:ss|HH:MM:SS)$'))

slots.MonetSoilSamplingActivity_infiltration_1 = Slot(uri=ANALYSIS_API_SCHEMA.infiltration_1, name="MonetSoilSamplingActivity_infiltration_1", curie=ANALYSIS_API_SCHEMA.curie('infiltration_1'),
                   model_uri=ANALYSIS_API_SCHEMA.MonetSoilSamplingActivity_infiltration_1, domain=MonetSoilSamplingActivity, range=str,
                   pattern=re.compile(r'^((0[0-9]|[1-5][0-9]):([0-5][0-9])\smm:ss|did not collect|failed)$'))

slots.MonetSoilSamplingActivity_infiltration_2 = Slot(uri=ANALYSIS_API_SCHEMA.infiltration_2, name="MonetSoilSamplingActivity_infiltration_2", curie=ANALYSIS_API_SCHEMA.curie('infiltration_2'),
                   model_uri=ANALYSIS_API_SCHEMA.MonetSoilSamplingActivity_infiltration_2, domain=MonetSoilSamplingActivity, range=str,
                   pattern=re.compile(r'^((0[0-9]|[1-5][0-9]):([0-5][0-9])\smm:ss|did not collect|failed)'))

slots.MonetSoilSamplingActivity_sample_collection_dev = Slot(uri=ANALYSIS_API_SCHEMA.sample_collection_dev, name="MonetSoilSamplingActivity_sample_collection_dev", curie=ANALYSIS_API_SCHEMA.curie('sample_collection_dev'),
                   model_uri=ANALYSIS_API_SCHEMA.MonetSoilSamplingActivity_sample_collection_dev, domain=MonetSoilSamplingActivity, range=str)

slots.OtherUndescribedSamplingActivity_humidity = Slot(uri=ANALYSIS_API_SCHEMA.humidity, name="OtherUndescribedSamplingActivity_humidity", curie=ANALYSIS_API_SCHEMA.curie('humidity'),
                   model_uri=ANALYSIS_API_SCHEMA.OtherUndescribedSamplingActivity_humidity, domain=OtherUndescribedSamplingActivity, range=Optional[str],
                   pattern=re.compile(r'^\d+(\.\d+)?\s*[\w\s/]+$'))

slots.WaterSamplingActivity_sample_collection_dev = Slot(uri=ANALYSIS_API_SCHEMA.sample_collection_dev, name="WaterSamplingActivity_sample_collection_dev", curie=ANALYSIS_API_SCHEMA.curie('sample_collection_dev'),
                   model_uri=ANALYSIS_API_SCHEMA.WaterSamplingActivity_sample_collection_dev, domain=WaterSamplingActivity, range=str)

slots.WaterSamplingActivity_sample_collection_method = Slot(uri=ANALYSIS_API_SCHEMA.sample_collection_method, name="WaterSamplingActivity_sample_collection_method", curie=ANALYSIS_API_SCHEMA.curie('sample_collection_method'),
                   model_uri=ANALYSIS_API_SCHEMA.WaterSamplingActivity_sample_collection_method, domain=WaterSamplingActivity, range=str)

slots.biological_entity_strain_identifier = Slot(uri=ANALYSIS_API_SCHEMA.strain_identifier, name="biological_entity_strain_identifier", curie=ANALYSIS_API_SCHEMA.curie('strain_identifier'),
                   model_uri=ANALYSIS_API_SCHEMA.biological_entity_strain_identifier, domain=BiologicalEntity, range=str)

slots.biological_entity_name = Slot(uri=ANALYSIS_API_SCHEMA.name, name="biological_entity_name", curie=ANALYSIS_API_SCHEMA.curie('name'),
                   model_uri=ANALYSIS_API_SCHEMA.biological_entity_name, domain=BiologicalEntity, range=str)

slots.biological_entity_organism_name = Slot(uri=ANALYSIS_API_SCHEMA.organism_name, name="biological_entity_organism_name", curie=ANALYSIS_API_SCHEMA.curie('organism_name'),
                   model_uri=ANALYSIS_API_SCHEMA.biological_entity_organism_name, domain=BiologicalEntity, range=Optional[str])

slots.biological_entity_strain_source = Slot(uri=ANALYSIS_API_SCHEMA.strain_source, name="biological_entity_strain_source", curie=ANALYSIS_API_SCHEMA.curie('strain_source'),
                   model_uri=ANALYSIS_API_SCHEMA.biological_entity_strain_source, domain=BiologicalEntity, range=Optional[str])

slots.biological_entity_strain_mutation = Slot(uri=ANALYSIS_API_SCHEMA.strain_mutation, name="biological_entity_strain_mutation", curie=ANALYSIS_API_SCHEMA.curie('strain_mutation'),
                   model_uri=ANALYSIS_API_SCHEMA.biological_entity_strain_mutation, domain=BiologicalEntity, range=Optional[str])

slots.biological_entity_modification_method = Slot(uri=ANALYSIS_API_SCHEMA.modification_method, name="biological_entity_modification_method", curie=ANALYSIS_API_SCHEMA.curie('modification_method'),
                   model_uri=ANALYSIS_API_SCHEMA.biological_entity_modification_method, domain=BiologicalEntity, range=Optional[Union[str, "ModificationMethodEnum"]])

slots.biological_entity_trophic_level = Slot(uri=ANALYSIS_API_SCHEMA.trophic_level, name="biological_entity_trophic_level", curie=ANALYSIS_API_SCHEMA.curie('trophic_level'),
                   model_uri=ANALYSIS_API_SCHEMA.biological_entity_trophic_level, domain=BiologicalEntity, range=Optional[Union[str, "TrophicLevelEnum"]])

slots.Study_external_identifiers = Slot(uri=ANALYSIS_API_SCHEMA.external_identifiers, name="Study_external_identifiers", curie=ANALYSIS_API_SCHEMA.curie('external_identifiers'),
                   model_uri=ANALYSIS_API_SCHEMA.Study_external_identifiers, domain=Study, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])
