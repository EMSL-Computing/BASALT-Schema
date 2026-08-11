

# Slot: biological status (biol_stat) 


_The level of genome modification._





URI: [basalt_schema:biol_stat](https://w3id.org/MONet/basalt-schema/biol_stat)
Alias: biol_stat

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
| Range | [BiolStatEnum](BiolStatEnum.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [PlantSample](PlantSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:biol_stat |
| native | basalt_schema:biol_stat |




## LinkML Source

<details>
```yaml
name: biol_stat
description: The level of genome modification.
title: biological status
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: biol_stat
domain_of:
- OtherUndescribedSample
- PlantSample
range: BiolStatEnum

```
</details>