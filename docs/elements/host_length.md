

# Slot: host length (host_length) 


_The length of subject_





URI: [basalt_schema:host_length](https://EMSL-Computing.github.io/BASALT-Schema/host_length)
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


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:host_length |
| native | basalt_schema:host_length |




## LinkML Source

<details>
```yaml
name: host_length
description: The length of subject
title: host length
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: host_length
domain_of:
- OtherUndescribedSample
- PlantSample
range: string

```
</details>