

# Slot: treatment_concentration 


_Treatment concentration with unit (e.g. "1.0 pct", "10 mM")_





URI: [analysis_api_schema:treatment_concentration](https://w3id.org/MONet/analysis-api-schema/treatment_concentration)
Alias: treatment_concentration

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EcoplateWellMetadata](EcoplateWellMetadata.md) | Ecoplate-specific per-well metadata |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [EcoplateWellMetadata](EcoplateWellMetadata.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EcoplateWellMetadata](EcoplateWellMetadata.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:treatment_concentration |
| native | analysis_api_schema:treatment_concentration |




## LinkML Source

<details>
```yaml
name: treatment_concentration
description: Treatment concentration with unit (e.g. "1.0 pct", "10 mM")
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: treatment_concentration
owner: EcoplateWellMetadata
domain_of:
- EcoplateWellMetadata
range: string

```
</details>