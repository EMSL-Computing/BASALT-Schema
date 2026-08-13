

# Slot: dissolved inorganic carbon (diss_inorg_carb) 


_Dissolved inorganic carbon concentration in the sample, typically measured after filtering the sample using a 0.45 micrometer filter (Unit:  ug/L or mg/L or ppm)_





URI: [basalt_schema:diss_inorg_carb](https://EMSL-Computing.github.io/BASALT-Schema/diss_inorg_carb)
Alias: diss_inorg_carb

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |






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
| Regex Pattern | `^\d+(\.\d+)?\s*(ug/L|mg/L|ppm)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:diss_inorg_carb |
| native | basalt_schema:diss_inorg_carb |




## LinkML Source

<details>
```yaml
name: diss_inorg_carb
description: 'Dissolved inorganic carbon concentration in the sample, typically measured
  after filtering the sample using a 0.45 micrometer filter (Unit:  ug/L or mg/L or
  ppm)'
title: dissolved inorganic carbon
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: diss_inorg_carb
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(ug/L|mg/L|ppm)$

```
</details>