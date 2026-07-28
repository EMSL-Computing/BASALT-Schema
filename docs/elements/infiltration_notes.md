

# Slot: infiltration notes (infiltration_notes) 


_Provide any details, issues, or context needed to understand the infiltration activity_





URI: [analysis_api_schema:infiltration_notes](https://w3id.org/MONet/analysis-api-schema/infiltration_notes)
Alias: infiltration_notes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilSamplingActivity](SoilSamplingActivity.md) | Collection of soil samples from the environment |  no  |
| [MonetSoilSamplingActivity](MonetSoilSamplingActivity.md) | Collection of soil cores according to the MONet soil sampling protocol |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MonetSoilSamplingActivity](MonetSoilSamplingActivity.md), [SoilSamplingActivity](SoilSamplingActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:infiltration_notes |
| native | analysis_api_schema:infiltration_notes |




## LinkML Source

<details>
```yaml
name: infiltration_notes
description: Provide any details, issues, or context needed to understand the infiltration
  activity
title: infiltration notes
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: infiltration_notes
domain_of:
- MonetSoilSamplingActivity
- SoilSamplingActivity
range: string

```
</details>