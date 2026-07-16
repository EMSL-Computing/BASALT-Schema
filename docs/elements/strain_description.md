

# Slot: strain description (strain_description) 


_A brief description of the modifications that comprise this strain_





URI: [analysis_api_schema:strain_description](https://w3id.org/MONet/analysis-api-schema/strain_description)
Alias: strain_description

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiologicalEntity](BiologicalEntity.md) | Reference data representing a biological identity (strain, isolate, |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [BiologicalEntity](BiologicalEntity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |







## Aliases


* strain_desc
* strain_notes




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:strain_description |
| native | analysis_api_schema:strain_description |




## LinkML Source

<details>
```yaml
name: strain_description
description: A brief description of the modifications that comprise this strain
title: strain description
from_schema: https://w3id.org/MONet/analysis-api-schema
aliases:
- strain_desc
- strain_notes
rank: 1000
alias: strain_description
domain_of:
- biological_entity
range: string

```
</details>