

# Slot: acquisition_end_time 



URI: [basalt_schema:acquisition_end_time](https://w3id.org/MONet/basalt-schema/acquisition_end_time)
Alias: acquisition_end_time

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [XRFDataGenerationActivity](XRFDataGenerationActivity.md) | X-ray Fluorescence (XRF) elemental analysis activity |  no  |
| [MassSpectrometryDataGenerationActivity](MassSpectrometryDataGenerationActivity.md) | A record of the mass spectrometry run that generates a raw data product |  no  |
| [AMP2DataGenerationActivity](AMP2DataGenerationActivity.md) | AMP2 plate measurement (OD, fluorescence, flow cytometry) |  no  |
| [EcoplateDataGenerationActivity](EcoplateDataGenerationActivity.md) | Ecoplate absorbance measurement at a single timepoint |  no  |
| [PlateDataGenerationActivity](PlateDataGenerationActivity.md) | Abstract base for plate measurement activities |  no  |
| [RespirationDataGenerationActivity](RespirationDataGenerationActivity.md) | Data generation activity for soil respiration analysis |  no  |
| [XRayDataGenerationActivity](XRayDataGenerationActivity.md) | Abstract base class for X-ray analytical methods including XRF (elemental) |  no  |
| [NucleotideSequencing](NucleotideSequencing.md) | A lab activity in which DNA or RNA that was extracted from a sample is sequen... |  no  |
| [XRDDataGenerationActivity](XRDDataGenerationActivity.md) | X-ray Diffraction (XRD) mineralogical analysis activity |  no  |
| [DataGenerationActivity](DataGenerationActivity.md) | Abstract base for any data generation activity (physical to digital) |  no  |






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


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:acquisition_end_time |
| native | basalt_schema:acquisition_end_time |




## LinkML Source

<details>
```yaml
name: acquisition_end_time
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: acquisition_end_time
owner: DataGenerationActivity
domain_of:
- DataGenerationActivity
range: datetime
required: true

```
</details>