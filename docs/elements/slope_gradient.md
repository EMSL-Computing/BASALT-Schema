

# Slot: slope gradient (slope_gradient) 


_Commonly called 'slope'. The angle between ground surface and a horizontal line (in percent). This is the direction that overland water would flow. This measure is usually taken with a hand level meter or clinometer. (Unit: percent)_





URI: [basalt_schema:slope_gradient](https://emsl-computing.github.io/BASALT-Schema/elements/slope_gradient)
Alias: slope_gradient

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
| Regex Pattern | `^\d+(\.\d+)?\s*percent$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:slope_gradient |
| native | basalt_schema:slope_gradient |




## LinkML Source

<details>
```yaml
name: slope_gradient
description: 'Commonly called ''slope''. The angle between ground surface and a horizontal
  line (in percent). This is the direction that overland water would flow. This measure
  is usually taken with a hand level meter or clinometer. (Unit: percent)'
title: slope gradient
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: slope_gradient
domain_of:
- Site
range: string
pattern: ^\d+(\.\d+)?\s*percent$

```
</details>