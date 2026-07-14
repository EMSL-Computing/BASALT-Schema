

# Slot: processing_steps 



URI: [analysis_api_schema:processing_steps](https://w3id.org/MONet/analysis-api-schema/processing_steps)
Alias: processing_steps

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PreCultureGrowth](PreCultureGrowth.md) | Growth of a pre-culture to establish viable inoculum before |  no  |
| [CultureGrowth](CultureGrowth.md) | Abstract activity for growing cultures from samples or other cultures |  no  |
| [ExperimentalCulture](ExperimentalCulture.md) | Growth of an experimental culture for downstream analysis |  no  |
| [SampleProcessing](SampleProcessing.md) |  |  no  |
| [PlateSetupActivity](PlateSetupActivity.md) | Abstract base for 96-well plate setup activities |  no  |
| [StrainPurity](StrainPurity.md) | Purity check of a strain culture |  no  |
| [StockCulturePreparation](StockCulturePreparation.md) | Preparation of a stock culture from user samples for long-term storage |  no  |
| [AMP2PlateSetupActivity](AMP2PlateSetupActivity.md) | AMP2-specific plate setup |  no  |
| [MediaPreparation](MediaPreparation.md) | Activity that prepares a batch of growth media |  no  |
| [EcoplatePlateSetupActivity](EcoplatePlateSetupActivity.md) | Ecoplate-specific plate setup |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:processing_steps |
| native | analysis_api_schema:processing_steps |




## LinkML Source

<details>
```yaml
name: processing_steps
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: processing_steps
owner: SampleProcessing
domain_of:
- SampleProcessing
range: string
required: true

```
</details>