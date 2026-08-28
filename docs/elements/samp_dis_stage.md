

# Slot: sample disease stage (samp_dis_stage) 


_Stage of the disease at the time of sample collection e.g. inoculation, penetration, infection, growth and reproduction, dissemination of pathogen._





URI: [basalt_schema:samp_dis_stage](https://emsl-computing.github.io/BASALT-Schema/elements/samp_dis_stage)
Alias: samp_dis_stage

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


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:samp_dis_stage |
| native | basalt_schema:samp_dis_stage |




## LinkML Source

<details>
```yaml
name: samp_dis_stage
description: Stage of the disease at the time of sample collection e.g. inoculation,
  penetration, infection, growth and reproduction, dissemination of pathogen.
title: sample disease stage
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: samp_dis_stage
domain_of:
- OtherUndescribedSample
range: string

```
</details>