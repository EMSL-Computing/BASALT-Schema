

# Slot: contaminant_strains 


_Known or detected contaminant strains (if any)_





URI: [basalt_schema:contaminant_strains](https://EMSL-Computing.github.io/basalt-schema/contaminant_strains)
Alias: contaminant_strains

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


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:contaminant_strains |
| native | basalt_schema:contaminant_strains |




## LinkML Source

<details>
```yaml
name: contaminant_strains
description: Known or detected contaminant strains (if any)
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: contaminant_strains
domain_of:
- StrainPurity
range: string

```
</details>