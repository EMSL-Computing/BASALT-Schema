

# Slot: crop rotation (crop_rotation) 


_Whether or not crop is rotated, and if yes, rotation schedule_





URI: [basalt_schema:crop_rotation](https://EMSL-Computing.github.io/basalt-schema/crop_rotation)
Alias: crop_rotation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Site](Site.md) | Site-level metadata for a specific location from which a set of samples are c... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Site](Site.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:crop_rotation |
| native | basalt_schema:crop_rotation |




## LinkML Source

<details>
```yaml
name: crop_rotation
description: Whether or not crop is rotated, and if yes, rotation schedule
title: crop rotation
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: crop_rotation
domain_of:
- Site
range: string

```
</details>