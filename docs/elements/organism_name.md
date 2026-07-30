

# Slot: organism name (organism_name) 


_Provide the scientific name (genus and species) of the host organism._





URI: [analysis_api_schema:organism_name](https://w3id.org/MONet/analysis-api-schema/organism_name)
Alias: organism_name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organism](Organism.md) | Reference data representing a biological identity (strain, isolate, |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Organism](Organism.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |







## Aliases


* scientific_name
* species_name




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:organism_name |
| native | analysis_api_schema:organism_name |




## LinkML Source

<details>
```yaml
name: organism_name
description: Provide the scientific name (genus and species) of the host organism.
title: organism name
from_schema: https://w3id.org/MONet/analysis-api-schema
aliases:
- scientific_name
- species_name
rank: 1000
alias: organism_name
domain_of:
- organism
range: string

```
</details>