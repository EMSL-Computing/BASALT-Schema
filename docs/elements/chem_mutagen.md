

# Slot: chemical mutagen (chem_mutagen) 


_Treatment involving use of mutagens; should include the name of mutagen, amount administered, treatment regimen, including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple mutagen regimens_





URI: [basalt_schema:chem_mutagen](https://emsl-computing.github.io/BASALT-Schema/elements/chem_mutagen)
Alias: chem_mutagen

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


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:chem_mutagen |
| native | basalt_schema:chem_mutagen |




## LinkML Source

<details>
```yaml
name: chem_mutagen
description: Treatment involving use of mutagens; should include the name of mutagen,
  amount administered, treatment regimen, including how many times the treatment was
  repeated, how long each treatment lasted, and the start and end time of the entire
  treatment; can include multiple mutagen regimens
title: chemical mutagen
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: chem_mutagen
domain_of:
- OtherUndescribedSample
- PlantSample
range: string

```
</details>