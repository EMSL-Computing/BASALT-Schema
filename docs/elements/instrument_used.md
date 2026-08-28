

# Slot: instrument_used 


_Instrument used for the measurement_





URI: [basalt_schema:instrument_used](https://emsl-computing.github.io/BASALT-Schema/elements/instrument_used)
Alias: instrument_used

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryDataGenerationActivity](MassSpectrometryDataGenerationActivity.md) | A record of the mass spectrometry run that generates a raw data product |  no  |
| [NucleotideSequencing](NucleotideSequencing.md) | A lab activity in which DNA or RNA that was extracted from a sample is sequen... |  no  |
| [XRDDataGenerationActivity](XRDDataGenerationActivity.md) | X-ray Diffraction (XRD) mineralogical analysis activity |  no  |
| [PlateDataGenerationActivity](PlateDataGenerationActivity.md) | Abstract base for plate measurement activities |  no  |
| [XRayDataGenerationActivity](XRayDataGenerationActivity.md) | Abstract base class for X-ray analytical methods including XRF (elemental), |  no  |
| [XRFDataGenerationActivity](XRFDataGenerationActivity.md) | X-ray Fluorescence (XRF) elemental analysis activity |  no  |
| [XASDataGenerationActivity](XASDataGenerationActivity.md) | X-ray Absorption Spectroscopy (XAS) acquisition activity |  no  |
| [AMP2DataGenerationActivity](AMP2DataGenerationActivity.md) | AMP2 plate measurement (OD, fluorescence, flow cytometry) |  no  |
| [EcoplateDataGenerationActivity](EcoplateDataGenerationActivity.md) | Ecoplate absorbance measurement at a single timepoint |  no  |
| [DataGenerationActivity](DataGenerationActivity.md) | Abstract base for any data generation activity (physical to digital) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Instrument](Instrument.md) |
| Domain Of | [DataGenerationActivity](DataGenerationActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:instrument_used |
| native | basalt_schema:instrument_used |




## LinkML Source

<details>
```yaml
name: instrument_used
description: Instrument used for the measurement
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: instrument_used
domain_of:
- DataGenerationActivity
range: Instrument

```
</details>