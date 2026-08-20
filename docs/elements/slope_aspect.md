

# Slot: slope aspect (slope_aspect) 


_The direction a slope faces. While looking down a slope use a compass to record the direction you are facing (degrees); e.g. 315 degrees. This measure provides an indication of sun and wind exposure that will influence soil temperature and evapotranspiration. (Unit: degrees)_





URI: [basalt_schema:slope_aspect](https://emsl-computing.github.io/BASALT-Schema/elements/slope_aspect)
Alias: slope_aspect

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
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*degrees$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:slope_aspect |
| native | basalt_schema:slope_aspect |




## LinkML Source

<details>
```yaml
name: slope_aspect
description: 'The direction a slope faces. While looking down a slope use a compass
  to record the direction you are facing (degrees); e.g. 315 degrees. This measure
  provides an indication of sun and wind exposure that will influence soil temperature
  and evapotranspiration. (Unit: degrees)'
title: slope aspect
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: slope_aspect
domain_of:
- Site
range: string
pattern: ^\d+(\.\d+)?\s*degrees$

```
</details>