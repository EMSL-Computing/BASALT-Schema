

# Slot: calcium (calcium) 


_Concentration of calcium in the sample (Unit: mg/L or umol/L or ppm)_





URI: [analysis_api_schema:calcium](https://w3id.org/MONet/analysis-api-schema/calcium)
Alias: calcium

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
| Regex Pattern | `^\d+(\.\d+)?\s*(mg/L|umol/L|ppm)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:calcium |
| native | analysis_api_schema:calcium |




## LinkML Source

<details>
```yaml
name: calcium
description: 'Concentration of calcium in the sample (Unit: mg/L or umol/L or ppm)'
title: calcium
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: calcium
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(mg/L|umol/L|ppm)$

```
</details>