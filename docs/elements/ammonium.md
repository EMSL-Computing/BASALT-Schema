

# Slot: ammonium (ammonium) 


_Concentration of ammonium in the sample. (Units: umol/L or mg/Liter or ppm)_





URI: [analysis_api_schema:ammonium](https://w3id.org/MONet/analysis-api-schema/ammonium)
Alias: ammonium

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
| Regex Pattern | `^\d+(\.\d+)?\s*(umol/L|mg/L|ppm)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:ammonium |
| native | analysis_api_schema:ammonium |




## LinkML Source

<details>
```yaml
name: ammonium
description: 'Concentration of ammonium in the sample. (Units: umol/L or mg/Liter
  or ppm)'
title: ammonium
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: ammonium
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(umol/L|mg/L|ppm)$

```
</details>