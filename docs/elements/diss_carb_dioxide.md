

# Slot: dissolved carbon dioxide (diss_carb_dioxide) 


_Concentration of dissolved carbon dioxide in the sample or liquid portion of the sample (Unit: umol/L or mg/L)_





URI: [analysis_api_schema:diss_carb_dioxide](https://w3id.org/MONet/analysis-api-schema/diss_carb_dioxide)
Alias: diss_carb_dioxide

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*(umol|mg)/L$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:diss_carb_dioxide |
| native | analysis_api_schema:diss_carb_dioxide |




## LinkML Source

<details>
```yaml
name: diss_carb_dioxide
description: 'Concentration of dissolved carbon dioxide in the sample or liquid portion
  of the sample (Unit: umol/L or mg/L)'
title: dissolved carbon dioxide
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: diss_carb_dioxide
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(umol|mg)/L$

```
</details>