

# Slot: elevation (elev) 


_Elevation of the sampling site is its height above a fixed reference point, most commonly the mean sea level. Elevation is mainly used when referring to points on the earth's surface. (Unit: m)._





URI: [basalt_schema:elev](https://EMSL-Computing.github.io/basalt-schema/elev)
Alias: elev

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Site](Site.md) | Site-level metadata for a specific location from which a set of samples are c... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Site](Site.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*m$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:elev |
| native | basalt_schema:elev |




## LinkML Source

<details>
```yaml
name: elev
description: 'Elevation of the sampling site is its height above a fixed reference
  point, most commonly the mean sea level. Elevation is mainly used when referring
  to points on the earth''s surface. (Unit: m).'
title: elevation
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: elev
domain_of:
- Site
range: string
pattern: ^\d+(\.\d+)?\s*m$

```
</details>