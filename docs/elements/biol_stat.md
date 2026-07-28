

# Slot: biological status (biol_stat) 


_The level of genome modification._





URI: [analysis_api_schema:biol_stat](https://w3id.org/MONet/analysis-api-schema/biol_stat)
Alias: biol_stat

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |






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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:biol_stat |
| native | analysis_api_schema:biol_stat |




## LinkML Source

<details>
```yaml
name: biol_stat
description: The level of genome modification.
title: biological status
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: biol_stat
domain_of:
- OtherUndescribedSample
- PlantSample
range: BiolStatEnum

```
</details>