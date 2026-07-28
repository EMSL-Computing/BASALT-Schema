

# Slot: construct component name (component_name) 


_Provide a one-to-three word name based on the component. If using an_

_acronym provide the full component name in the component description._





URI: [analysis_api_schema:component_name](https://w3id.org/MONet/analysis-api-schema/component_name)
Alias: component_name

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
| self | analysis_api_schema:component_name |
| native | analysis_api_schema:component_name |




## LinkML Source

<details>
```yaml
name: component_name
description: 'Provide a one-to-three word name based on the component. If using an

  acronym provide the full component name in the component description.'
title: construct component name
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: component_name
domain_of:
- biological_entity
range: string

```
</details>