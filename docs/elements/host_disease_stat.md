

# Slot: host disease status (host_disease_stat) 


_List of diseases with which the host has been diagnosed; can include multiple diagnoses. The value of the field depends on host; for humans the terms should be chosen from the DO (Human Disease Ontology) at https://www.disease-ontology.org non-human host diseases are free text_





URI: [analysis_api_schema:host_disease_stat](https://w3id.org/MONet/analysis-api-schema/host_disease_stat)
Alias: host_disease_stat

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:host_disease_stat |
| native | analysis_api_schema:host_disease_stat |




## LinkML Source

<details>
```yaml
name: host_disease_stat
description: List of diseases with which the host has been diagnosed; can include
  multiple diagnoses. The value of the field depends on host; for humans the terms
  should be chosen from the DO (Human Disease Ontology) at https://www.disease-ontology.org
  non-human host diseases are free text
title: host disease status
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: host_disease_stat
domain_of:
- OtherUndescribedSample
range: string

```
</details>