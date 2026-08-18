

# Slot: acquisition_end_time 



URI: [basalt_schema:acquisition_end_time](https://emsl-computing.github.io/BASALT-Schema/elements/acquisition_end_time)
Alias: acquisition_end_time

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [XRDDataGenerationActivity](XRDDataGenerationActivity.md) | X-ray Diffraction (XRD) mineralogical analysis activity |  no  |
| [PlateDataGenerationActivity](PlateDataGenerationActivity.md) | Abstract base for plate measurement activities |  no  |
| [DataGenerationActivity](DataGenerationActivity.md) | Abstract base for any data generation activity (physical to digital) |  no  |
| [XRayDataGenerationActivity](XRayDataGenerationActivity.md) | Abstract base class for X-ray analytical methods including XRF (elemental) |  no  |
| [AMP2DataGenerationActivity](AMP2DataGenerationActivity.md) | AMP2 plate measurement (OD, fluorescence, flow cytometry) |  no  |
| [XRFDataGenerationActivity](XRFDataGenerationActivity.md) | X-ray Fluorescence (XRF) elemental analysis activity |  no  |
| [NucleotideSequencing](NucleotideSequencing.md) | A lab activity in which DNA or RNA that was extracted from a sample is sequen... |  no  |
| [MassSpectrometryDataGenerationActivity](MassSpectrometryDataGenerationActivity.md) | A record of the mass spectrometry run that generates a raw data product |  no  |
| [EcoplateDataGenerationActivity](EcoplateDataGenerationActivity.md) | Ecoplate absorbance measurement at a single timepoint |  no  |
| [RespirationDataGenerationActivity](RespirationDataGenerationActivity.md) | Data generation activity for soil respiration analysis |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [DataGenerationActivity](DataGenerationActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [DataGenerationActivity](DataGenerationActivity.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:acquisition_end_time |
| native | basalt_schema:acquisition_end_time |




## LinkML Source

<details>
```yaml
name: acquisition_end_time
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: acquisition_end_time
owner: DataGenerationActivity
domain_of:
- DataGenerationActivity
range: datetime
required: true

```
</details>