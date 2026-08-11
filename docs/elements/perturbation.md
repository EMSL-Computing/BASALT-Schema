

# Slot: perturbation (perturbation) 


_Type of perturbation, e.g. chemical administration, physical disturbance, etc.; coupled with perturbation regimen, including how many times the perturbation was repeated, how long each perturbation lasted, and the start and end time of the entire perturbation period; can include multiple perturbation types_





URI: [basalt_schema:perturbation](https://EMSL-Computing.github.io/basalt-schema/perturbation)
Alias: perturbation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:perturbation |
| native | basalt_schema:perturbation |




## LinkML Source

<details>
```yaml
name: perturbation
description: Type of perturbation, e.g. chemical administration, physical disturbance,
  etc.; coupled with perturbation regimen, including how many times the perturbation
  was repeated, how long each perturbation lasted, and the start and end time of the
  entire perturbation period; can include multiple perturbation types
title: perturbation
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: perturbation
domain_of:
- OtherUndescribedSample
- SedimentSample
- SoilSample
- WaterSample
range: string

```
</details>