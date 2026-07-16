

# Slot: downward PAR (down_par) 


_Visible waveband radiance and irradiance measurements in the water column. Provide value and unit, any unit is valid._





URI: [analysis_api_schema:down_par](https://w3id.org/MONet/analysis-api-schema/down_par)
Alias: down_par

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
| Regex Pattern | `^\d+(\.\d+)?\s*[\w\s/]+$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:down_par |
| native | analysis_api_schema:down_par |




## LinkML Source

<details>
```yaml
name: down_par
description: Visible waveband radiance and irradiance measurements in the water column.
  Provide value and unit, any unit is valid.
title: downward PAR
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: down_par
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>