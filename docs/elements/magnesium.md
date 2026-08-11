

# Slot: magnesium (magnesium) 


_Concentration of magnesium in the sample (Unit: umol/kg or mol/L or mg/L or ppm)_





URI: [basalt_schema:magnesium](https://w3id.org/MONet/basalt-schema/magnesium)
Alias: magnesium

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
| Regex Pattern | `^\d+(\.\d+)?\s*(umol/kg|mol/L|mg/L|ppm)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:magnesium |
| native | basalt_schema:magnesium |




## LinkML Source

<details>
```yaml
name: magnesium
description: 'Concentration of magnesium in the sample (Unit: umol/kg or mol/L or
  mg/L or ppm)'
title: magnesium
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: magnesium
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(umol/kg|mol/L|mg/L|ppm)$

```
</details>