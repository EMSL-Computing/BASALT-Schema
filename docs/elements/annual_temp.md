

# Slot: mean annual temperature (annual_temp) 


_Mean annual temperature (Unit: C)_





URI: [basalt_schema:annual_temp](https://emsl-computing.github.io/BASALT-Schema/elements/annual_temp)
Alias: annual_temp

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
| Regex Pattern | `^-?\d+(\.\d+)?\s*C$` |









## Aliases


* average annual temperature




## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:annual_temp |
| native | basalt_schema:annual_temp |




## LinkML Source

<details>
```yaml
name: annual_temp
description: 'Mean annual temperature (Unit: C)'
title: mean annual temperature
from_schema: https://emsl-computing.github.io/BASALT-Schema
aliases:
- average annual temperature
rank: 1000
alias: annual_temp
domain_of:
- Site
range: string
pattern: ^-?\d+(\.\d+)?\s*C$

```
</details>