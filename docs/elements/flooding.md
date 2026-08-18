

# Slot: flooding (flooding) 


_Historical and/or physical evidence of flooding. Format: YYYY-MM-DD_





URI: [basalt_schema:flooding](https://emsl-computing.github.io/BASALT-Schema/elements/flooding)
Alias: flooding

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
| Regex Pattern | `^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:flooding |
| native | basalt_schema:flooding |




## LinkML Source

<details>
```yaml
name: flooding
description: 'Historical and/or physical evidence of flooding. Format: YYYY-MM-DD'
title: flooding
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: flooding
domain_of:
- Site
range: string
pattern: ^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$

```
</details>