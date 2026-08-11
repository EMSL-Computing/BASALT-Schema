

# Slot: sequence_order 


_Integer ordering within a temporal series for the same analyte._

_Lower = earlier in series. Use when acquisition_time alone is insufficient._

__

_DDL: ALTER TABLE "DataGenerationActivity"_

_       ADD COLUMN sequence_order INTEGER;_





URI: [basalt_schema:sequence_order](https://w3id.org/MONet/basalt-schema/sequence_order)
Alias: sequence_order

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [XRayDataGenerationActivity](XRayDataGenerationActivity.md) | Abstract base class for X-ray analytical methods including XRF (elemental) |  no  |
| [AMP2DataGenerationActivity](AMP2DataGenerationActivity.md) | AMP2 plate measurement (OD, fluorescence, flow cytometry) |  no  |
| [DataGenerationActivity](DataGenerationActivity.md) | Abstract base for any data generation activity (physical to digital) |  no  |
| [MassSpectrometryDataGenerationActivity](MassSpectrometryDataGenerationActivity.md) | A record of the mass spectrometry run that generates a raw data product |  no  |
| [PlateDataGenerationActivity](PlateDataGenerationActivity.md) | Abstract base for plate measurement activities |  no  |
| [NucleotideSequencing](NucleotideSequencing.md) | A lab activity in which DNA or RNA that was extracted from a sample is sequen... |  no  |
| [XRFDataGenerationActivity](XRFDataGenerationActivity.md) | X-ray Fluorescence (XRF) elemental analysis activity |  no  |
| [EcoplateDataGenerationActivity](EcoplateDataGenerationActivity.md) | Ecoplate absorbance measurement at a single timepoint |  no  |
| [RespirationDataGenerationActivity](RespirationDataGenerationActivity.md) | Data generation activity for soil respiration analysis |  no  |
| [XRDDataGenerationActivity](XRDDataGenerationActivity.md) | X-ray Diffraction (XRD) mineralogical analysis activity |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [DataGenerationActivity](DataGenerationActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:sequence_order |
| native | basalt_schema:sequence_order |




## LinkML Source

<details>
```yaml
name: sequence_order
description: "Integer ordering within a temporal series for the same analyte.\nLower\
  \ = earlier in series. Use when acquisition_time alone is insufficient.\n\nDDL:\
  \ ALTER TABLE \"DataGenerationActivity\"\n       ADD COLUMN sequence_order INTEGER;"
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: sequence_order
domain_of:
- DataGenerationActivity
range: integer
required: false

```
</details>