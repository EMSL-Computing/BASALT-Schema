

# Slot: alkalinity (alkalinity) 


_The ability of a solution to neutralize acids to the equivalence point of carbonate or bicarbonate (Unit: mg/L or meq/L)_





URI: [analysis_api_schema:alkalinity](https://w3id.org/MONet/analysis-api-schema/alkalinity)
Alias: alkalinity

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
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*(mg|meq)/L$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:alkalinity |
| native | analysis_api_schema:alkalinity |




## LinkML Source

<details>
```yaml
name: alkalinity
description: 'The ability of a solution to neutralize acids to the equivalence point
  of carbonate or bicarbonate (Unit: mg/L or meq/L)'
title: alkalinity
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: alkalinity
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(mg|meq)/L$

```
</details>