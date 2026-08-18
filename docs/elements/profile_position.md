

# Slot: profile position (profile_position) 


_Cross-sectional position in the hillslope where sample was collected. Sample area position in relation to surrounding areas_





URI: [basalt_schema:profile_position](https://emsl-computing.github.io/BASALT-Schema/elements/profile_position)
Alias: profile_position

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Site](Site.md) | Site-level metadata for a specific location from which a set of samples are c... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ProfilePositionEnum](ProfilePositionEnum.md) |
| Domain Of | [Site](Site.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:profile_position |
| native | basalt_schema:profile_position |




## LinkML Source

<details>
```yaml
name: profile_position
description: Cross-sectional position in the hillslope where sample was collected.
  Sample area position in relation to surrounding areas
title: profile position
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: profile_position
domain_of:
- Site
range: ProfilePositionEnum

```
</details>