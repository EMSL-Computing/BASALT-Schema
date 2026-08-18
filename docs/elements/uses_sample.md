

# Slot: uses_sample 


_The starting sample that is being processed or analyzed. This slot should only be used on an Activity class._





URI: [basalt_schema:uses_sample](https://emsl-computing.github.io/BASALT-Schema/elements/uses_sample)
Alias: uses_sample

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PoolingProcess](PoolingProcess.md) | A laboratory pooling process that physically mixes multiple input samples int... |  no  |
| [StrainPurity](StrainPurity.md) | Purity check of a strain culture |  no  |
| [ProteinQuantification](ProteinQuantification.md) | A protein quantification assay (e |  no  |
| [MediaPreparation](MediaPreparation.md) | Activity that prepares a batch of growth media |  no  |
| [StockCulturePreparation](StockCulturePreparation.md) | Preparation of a stock culture from user samples for long-term storage |  no  |
| [PreCultureGrowth](PreCultureGrowth.md) | Growth of a pre-culture to establish viable inoculum before |  no  |
| [StandardSampleProcessing](StandardSampleProcessing.md) | A basic non-abstract SampleProcessing subclass that links to a published stan... |  no  |
| [SubSamplingProcess](SubSamplingProcess.md) | A laboratory subsampling process that takes a portion of an existing  sample ... |  no  |
| [FractionationProcess](FractionationProcess.md) | A fractionation process (e |  no  |
| [ChemicalConversionProcess](ChemicalConversionProcess.md) | A chemical conversion process used in sample preparation |  no  |
| [Extraction](Extraction.md) | The removal and isolation of a desired analyte from other material  in a samp... |  no  |
| [EcoplatePlateSetupActivity](EcoplatePlateSetupActivity.md) | Ecoplate-specific plate setup |  no  |
| [AMP2PlateSetupActivity](AMP2PlateSetupActivity.md) | AMP2-specific plate setup |  no  |
| [NormalizationProcess](NormalizationProcess.md) | A process that adjusts sample amounts (e |  no  |
| [ResuspensionProcess](ResuspensionProcess.md) | Resuspension of an analyte (e |  no  |
| [SampleProcessing](SampleProcessing.md) | Abstract base for any sample processing activity (physical to physical) |  no  |
| [CultureGrowth](CultureGrowth.md) | Abstract activity for growing cultures from samples or other cultures |  no  |
| [PlateSetupActivity](PlateSetupActivity.md) | Abstract base for 96-well plate setup activities |  no  |
| [SolidPhaseExtractionProcess](SolidPhaseExtractionProcess.md) | A solid phase extraction (SPE) step (e |  no  |
| [ExperimentalCulture](ExperimentalCulture.md) | Growth of an experimental culture for downstream analysis |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Sample](Sample.md) |
| Domain Of | [SampleProcessing](SampleProcessing.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:uses_sample |
| native | basalt_schema:uses_sample |




## LinkML Source

<details>
```yaml
name: uses_sample
description: The starting sample that is being processed or analyzed. This slot should
  only be used on an Activity class.
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: uses_sample
domain_of:
- SampleProcessing
range: Sample

```
</details>