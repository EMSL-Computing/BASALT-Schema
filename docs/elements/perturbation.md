

# Slot: perturbation (perturbation) 


_Type of perturbation, e.g. chemical administration, physical disturbance, etc.; coupled with perturbation regimen, including how many times the perturbation was repeated, how long each perturbation lasted, and the start and end time of the entire perturbation period; can include multiple perturbation types_





URI: [analysis_api_schema:perturbation](https://w3id.org/MONet/analysis-api-schema/perturbation)
Alias: perturbation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |






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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:perturbation |
| native | analysis_api_schema:perturbation |




## LinkML Source

<details>
```yaml
name: perturbation
description: Type of perturbation, e.g. chemical administration, physical disturbance,
  etc.; coupled with perturbation regimen, including how many times the perturbation
  was repeated, how long each perturbation lasted, and the start and end time of the
  entire perturbation period; can include multiple perturbation types
title: perturbation
from_schema: https://w3id.org/MONet/analysis-api-schema
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