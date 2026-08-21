

# Slot: processing_steps 



URI: [basalt_schema:processing_steps](https://emsl-computing.github.io/BASALT-Schema/elements/processing_steps)
Alias: processing_steps

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlateSetupActivity](PlateSetupActivity.md) | Abstract base for 96-well plate setup activities |  no  |
| [SampleProcessing](SampleProcessing.md) | Abstract base for any sample processing activity (physical to physical) |  no  |
| [MediaPreparation](MediaPreparation.md) | Activity that prepares a batch of growth media |  no  |
| [CultureGrowth](CultureGrowth.md) | Abstract activity for growing cultures from samples or other cultures |  no  |
| [ExperimentalCulture](ExperimentalCulture.md) | Growth of an experimental culture for downstream analysis |  no  |
| [PreCultureGrowth](PreCultureGrowth.md) | Growth of a pre-culture to establish viable inoculum before |  no  |
| [StrainPurity](StrainPurity.md) | Purity check of a strain culture |  no  |
| [AMP2PlateSetupActivity](AMP2PlateSetupActivity.md) | AMP2-specific plate setup |  no  |
| [StockCulturePreparation](StockCulturePreparation.md) | Preparation of a stock culture from user samples for long-term storage |  no  |
| [EcoplatePlateSetupActivity](EcoplatePlateSetupActivity.md) | Ecoplate-specific plate setup |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [SampleProcessing](SampleProcessing.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SampleProcessing](SampleProcessing.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:processing_steps |
| native | basalt_schema:processing_steps |




## LinkML Source

<details>
```yaml
name: processing_steps
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: processing_steps
owner: SampleProcessing
domain_of:
- SampleProcessing
range: string
required: true

```
</details>