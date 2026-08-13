

# Slot: drainage class (drainage_class) 


_Drainage classification from a standard system such as the USDA system_





URI: [basalt_schema:drainage_class](https://EMSL-Computing.github.io/BASALT-Schema/drainage_class)
Alias: drainage_class

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Site](Site.md) | Site-level metadata for a specific location from which a set of samples are c... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DrainageClassEnum](DrainageClassEnum.md) |
| Domain Of | [Site](Site.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:drainage_class |
| native | basalt_schema:drainage_class |




## LinkML Source

<details>
```yaml
name: drainage_class
description: Drainage classification from a standard system such as the USDA system
title: drainage class
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: drainage_class
domain_of:
- Site
range: DrainageClassEnum

```
</details>