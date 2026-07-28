

# Slot: treatments 


_Per-well treatments if applicable (e.g. different mineral concentrations)._

_NULL for uniform-treatment plates._





URI: [analysis_api_schema:treatments](https://w3id.org/MONet/analysis-api-schema/treatments)
Alias: treatments

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AMP2WellMetadata](AMP2WellMetadata.md) | AMP2-specific per-well metadata |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AMP2WellMetadata](AMP2WellMetadata.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AMP2WellMetadata](AMP2WellMetadata.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:treatments |
| native | analysis_api_schema:treatments |




## LinkML Source

<details>
```yaml
name: treatments
description: 'Per-well treatments if applicable (e.g. different mineral concentrations).

  NULL for uniform-treatment plates.'
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: treatments
owner: AMP2WellMetadata
domain_of:
- AMP2WellMetadata
range: string
multivalued: true

```
</details>