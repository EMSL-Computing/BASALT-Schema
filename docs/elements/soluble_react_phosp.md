

# Slot: soluble reactive phosphorus (soluble_react_phosp) 


_Concentration of soluble reactive phosphorus. (Unit: umol/L or mg/L or ppm)_





URI: [analysis_api_schema:soluble_react_phosp](https://w3id.org/MONet/analysis-api-schema/soluble_react_phosp)
Alias: soluble_react_phosp

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*(umol/L|mg/L|ppm)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:soluble_react_phosp |
| native | analysis_api_schema:soluble_react_phosp |




## LinkML Source

<details>
```yaml
name: soluble_react_phosp
description: 'Concentration of soluble reactive phosphorus. (Unit: umol/L or mg/L
  or ppm)'
title: soluble reactive phosphorus
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: soluble_react_phosp
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(umol/L|mg/L|ppm)$

```
</details>