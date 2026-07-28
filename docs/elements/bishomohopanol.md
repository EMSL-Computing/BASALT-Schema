

# Slot: bishomohopanol (bishomohopanol) 


_Concentration of bishomohopanol. (Unit: ug/L or ug/g)_





URI: [analysis_api_schema:bishomohopanol](https://w3id.org/MONet/analysis-api-schema/bishomohopanol)
Alias: bishomohopanol

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
| Regex Pattern | `^\d+(\.\d+)?\s*(ug/L|ug/g)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:bishomohopanol |
| native | analysis_api_schema:bishomohopanol |




## LinkML Source

<details>
```yaml
name: bishomohopanol
description: 'Concentration of bishomohopanol. (Unit: ug/L or ug/g)'
title: bishomohopanol
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: bishomohopanol
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(ug/L|ug/g)$

```
</details>