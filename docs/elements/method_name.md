

# Slot: method_name 



URI: [analysis_api_schema:method_name](https://w3id.org/MONet/analysis-api-schema/method_name)
Alias: method_name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlateSetupActivity](PlateSetupActivity.md) | Abstract base for 96-well plate setup activities |  no  |
| [AMP2PlateSetupActivity](AMP2PlateSetupActivity.md) | AMP2-specific plate setup |  no  |
| [MediaPreparation](MediaPreparation.md) | Activity that prepares a batch of growth media |  no  |
| [PreCultureGrowth](PreCultureGrowth.md) | Growth of a pre-culture to establish viable inoculum before |  no  |
| [CultureGrowth](CultureGrowth.md) | Abstract activity for growing cultures from samples or other cultures |  no  |
| [ExperimentalCulture](ExperimentalCulture.md) | Growth of an experimental culture for downstream analysis |  no  |
| [StockCulturePreparation](StockCulturePreparation.md) | Preparation of a stock culture from user samples for long-term storage |  no  |
| [SampleProcessing](SampleProcessing.md) | Abstract base for any sample processing activity (physical to physical) |  no  |
| [EcoplatePlateSetupActivity](EcoplatePlateSetupActivity.md) | Ecoplate-specific plate setup |  no  |
| [StrainPurity](StrainPurity.md) | Purity check of a strain culture |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MethodNameEnum](MethodNameEnum.md) |
| Domain Of | [SampleProcessing](SampleProcessing.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SampleProcessing](SampleProcessing.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:method_name |
| native | analysis_api_schema:method_name |




## LinkML Source

<details>
```yaml
name: method_name
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: method_name
owner: SampleProcessing
domain_of:
- SampleProcessing
range: MethodNameEnum

```
</details>