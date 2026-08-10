

# Slot: target_strain 


_Target strain identifier for purity checks_





URI: [basalt_schema:target_strain](https://w3id.org/MONet/basalt-schema/target_strain)
Alias: target_strain

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








## TODOs

* should this point to the Strain class?



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:target_strain |
| native | basalt_schema:target_strain |




## LinkML Source

<details>
```yaml
name: target_strain
description: Target strain identifier for purity checks
todos:
- should this point to the Strain class?
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: target_strain
domain_of:
- StrainPurity
range: string

```
</details>