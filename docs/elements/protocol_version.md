

# Slot: protocol_version 


_Version of the protocol used in the activity, if applicable._





URI: [basalt_schema:protocol_version](https://emsl-computing.github.io/BASALT-Schema/elements/protocol_version)
Alias: protocol_version

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryDataGenerationActivity](MassSpectrometryDataGenerationActivity.md) | A record of the mass spectrometry run that generates a raw data product |  no  |
| [NucleotideSequencing](NucleotideSequencing.md) | A lab activity in which DNA or RNA that was extracted from a sample is sequen... |  no  |
| [XRDDataGenerationActivity](XRDDataGenerationActivity.md) | X-ray Diffraction (XRD) mineralogical analysis activity |  no  |
| [PlateDataGenerationActivity](PlateDataGenerationActivity.md) | Abstract base for plate measurement activities |  no  |
| [XRayDataGenerationActivity](XRayDataGenerationActivity.md) | Abstract base class for X-ray analytical methods including XRF (elemental), |  no  |
| [SampleProcessingProtocol](SampleProcessingProtocol.md) | A sample processing protocol: the recipe, not an execution of it |  no  |
| [XRFDataGenerationActivity](XRFDataGenerationActivity.md) | X-ray Fluorescence (XRF) elemental analysis activity |  no  |
| [XASDataGenerationActivity](XASDataGenerationActivity.md) | X-ray Absorption Spectroscopy (XAS) acquisition activity |  no  |
| [AMP2DataGenerationActivity](AMP2DataGenerationActivity.md) | AMP2 plate measurement (OD, fluorescence, flow cytometry) |  no  |
| [EcoplateDataGenerationActivity](EcoplateDataGenerationActivity.md) | Ecoplate absorbance measurement at a single timepoint |  no  |
| [DataGenerationActivity](DataGenerationActivity.md) | Abstract base for any data generation activity (physical to digital) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [DataGenerationActivity](DataGenerationActivity.md), [SampleProcessingProtocol](SampleProcessingProtocol.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:protocol_version |
| native | basalt_schema:protocol_version |




## LinkML Source

<details>
```yaml
name: protocol_version
description: Version of the protocol used in the activity, if applicable.
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: protocol_version
domain_of:
- DataGenerationActivity
- SampleProcessingProtocol
range: string

```
</details>