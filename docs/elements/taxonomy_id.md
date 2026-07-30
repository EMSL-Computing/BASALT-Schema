

# Slot: taxonomy_id 


_NCBI taxon ID for the organism._





URI: [analysis_api_schema:taxonomy_id](https://w3id.org/MONet/analysis-api-schema/taxonomy_id)
Alias: taxonomy_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organism](Organism.md) | Reference data representing a biological identity (strain, isolate, |  no  |






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


* ncbi_taxon_id
* taxon_id




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:taxonomy_id |
| native | analysis_api_schema:taxonomy_id |




## LinkML Source

<details>
```yaml
name: taxonomy_id
description: NCBI taxon ID for the organism.
from_schema: https://w3id.org/MONet/analysis-api-schema
aliases:
- ncbi_taxon_id
- taxon_id
rank: 1000
alias: taxonomy_id
domain_of:
- organism
range: string

```
</details>