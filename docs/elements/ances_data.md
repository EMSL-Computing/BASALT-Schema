

# Slot: ancestral data (ances_data) 


_Information about either pedigree or other ancestral information description_





URI: [basalt_schema:ances_data](https://EMSL-Computing.github.io/BASALT-Schema/ances_data)
Alias: ances_data

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
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
| self | basalt_schema:ances_data |
| native | basalt_schema:ances_data |




## LinkML Source

<details>
```yaml
name: ances_data
description: Information about either pedigree or other ancestral information description
title: ancestral data
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: ances_data
domain_of:
- OtherUndescribedSample
- PlantSample
range: string

```
</details>