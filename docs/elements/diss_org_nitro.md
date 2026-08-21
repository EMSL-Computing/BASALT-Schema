

# Slot: dissolved organic nitrogen (diss_org_nitro) 


_Dissolved organic nitrogen concentration measured as: total dissolved nitrogen - NH4 - NO3 - NO2. Provide value and unit, any unit is valid_





URI: [basalt_schema:diss_org_nitro](https://emsl-computing.github.io/BASALT-Schema/elements/diss_org_nitro)
Alias: diss_org_nitro

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
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
| Regex Pattern | `^\d+(\.\d+)?\s*[\w\s/]+$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:diss_org_nitro |
| native | basalt_schema:diss_org_nitro |




## LinkML Source

<details>
```yaml
name: diss_org_nitro
description: 'Dissolved organic nitrogen concentration measured as: total dissolved
  nitrogen - NH4 - NO3 - NO2. Provide value and unit, any unit is valid'
title: dissolved organic nitrogen
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: diss_org_nitro
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>