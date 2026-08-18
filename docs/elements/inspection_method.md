

# Slot: inspection_method 


_Method used to inspect or verify purity (visual, sequencing, etc.)_





URI: [basalt_schema:inspection_method](https://EMSL-Computing.github.io/BASALT-Schema/inspection_method)
Alias: inspection_method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StrainPurity](StrainPurity.md) | Purity check of a strain culture |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [StrainPurity](StrainPurity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:inspection_method |
| native | basalt_schema:inspection_method |




## LinkML Source

<details>
```yaml
name: inspection_method
description: Method used to inspect or verify purity (visual, sequencing, etc.)
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: inspection_method
domain_of:
- StrainPurity
range: string

```
</details>