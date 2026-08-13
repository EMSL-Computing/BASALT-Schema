

# Slot: sample type (sample_type) 


_Requires a standardized ontology term to describe what your sample is. Please search for your sample type via Ontology Lookup Sevice at https://www.ebi.ac.uk/ols4/ _





URI: [basalt_schema:sample_type](https://EMSL-Computing.github.io/BASALT-Schema/sample_type)
Alias: sample_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^_*\s*[a-zA-Z\-]+\s\[[a-zA-Z]+:\d+\]$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:sample_type |
| native | basalt_schema:sample_type |




## LinkML Source

<details>
```yaml
name: sample_type
description: 'Requires a standardized ontology term to describe what your sample is.
  Please search for your sample type via Ontology Lookup Sevice at https://www.ebi.ac.uk/ols4/ '
title: sample type
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: sample_type
domain_of:
- OtherUndescribedSample
range: string
pattern: ^_*\s*[a-zA-Z\-]+\s\[[a-zA-Z]+:\d+\]$

```
</details>