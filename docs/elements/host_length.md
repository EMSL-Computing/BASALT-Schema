

# Slot: host length (host_length) 


_The length of subject_





URI: [analysis_api_schema:host_length](https://w3id.org/MONet/analysis-api-schema/host_length)
Alias: host_length

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSample](PlantSample.md) | A sample containing plant material |  yes  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [PlantSample](PlantSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:host_length |
| native | analysis_api_schema:host_length |




## LinkML Source

<details>
```yaml
name: host_length
description: The length of subject
title: host length
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: host_length
domain_of:
- OtherUndescribedSample
- PlantSample
range: string

```
</details>