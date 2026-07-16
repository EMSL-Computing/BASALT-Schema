

# Slot: mechanical damage (mechanical_damage) 


_Information about any mechanical damage exerted on the plant; can include multiple damages and sites_





URI: [analysis_api_schema:mechanical_damage](https://w3id.org/MONet/analysis-api-schema/mechanical_damage)
Alias: mechanical_damage

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [PlantSample](PlantSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:mechanical_damage |
| native | analysis_api_schema:mechanical_damage |




## LinkML Source

<details>
```yaml
name: mechanical_damage
description: Information about any mechanical damage exerted on the plant; can include
  multiple damages and sites
title: mechanical damage
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: mechanical_damage
domain_of:
- OtherUndescribedSample
- PlantSample
range: string

```
</details>