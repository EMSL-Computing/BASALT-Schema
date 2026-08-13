

# Slot: fire (fire) 


_Historical and/or physical evidence of fire. Format: YYYY-MM-DD_





URI: [basalt_schema:fire](https://EMSL-Computing.github.io/BASALT-Schema/fire)
Alias: fire

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


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:fire |
| native | basalt_schema:fire |




## LinkML Source

<details>
```yaml
name: fire
description: 'Historical and/or physical evidence of fire. Format: YYYY-MM-DD'
title: fire
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: fire
domain_of:
- Site
range: string
pattern: ^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$

```
</details>