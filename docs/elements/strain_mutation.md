

# Slot: strain_mutation 


_Primary genetic modification or plasmid carried (e.g., "pTE314")._

_For complex constructs, use genotype_segment_* and component_* slots._





URI: [analysis_api_schema:strain_mutation](https://w3id.org/MONet/analysis-api-schema/strain_mutation)
Alias: strain_mutation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiologicalEntity](BiologicalEntity.md) | Reference data representing a biological identity (strain, isolate, |  yes  |






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
| self | analysis_api_schema:strain_mutation |
| native | analysis_api_schema:strain_mutation |




## LinkML Source

<details>
```yaml
name: strain_mutation
description: 'Primary genetic modification or plasmid carried (e.g., "pTE314").

  For complex constructs, use genotype_segment_* and component_* slots.'
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: strain_mutation
domain_of:
- biological_entity
range: string

```
</details>