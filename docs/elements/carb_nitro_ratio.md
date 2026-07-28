

# Slot: carbon nitrogen ratio (carb_nitro_ratio) 


_Ratio of amount or concentrations of carbon to nitrogen._





URI: [analysis_api_schema:carb_nitro_ratio](https://w3id.org/MONet/analysis-api-schema/carb_nitro_ratio)
Alias: carb_nitro_ratio

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:carb_nitro_ratio |
| native | analysis_api_schema:carb_nitro_ratio |




## LinkML Source

<details>
```yaml
name: carb_nitro_ratio
description: Ratio of amount or concentrations of carbon to nitrogen.
title: carbon nitrogen ratio
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: carb_nitro_ratio
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string

```
</details>