

# Slot: construct component description (component_description) 


_Provide a short statement describing the function of the construct_

_component. You may provide an optional literature reference for lesser-known components._

_Example: "d-Cfp1 to block gene expression", "recognition sequence for guide RNA processing"_





URI: [analysis_api_schema:component_description](https://w3id.org/MONet/analysis-api-schema/component_description)
Alias: component_description

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










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:component_description |
| native | analysis_api_schema:component_description |




## LinkML Source

<details>
```yaml
name: component_description
description: 'Provide a short statement describing the function of the construct

  component. You may provide an optional literature reference for lesser-known components.

  Example: "d-Cfp1 to block gene expression", "recognition sequence for guide RNA
  processing"'
title: construct component description
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: component_description
domain_of:
- biological_entity
range: string

```
</details>