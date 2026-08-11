

# Slot: ph_adjustment 


_Whether the entity was pH-adjusted_





URI: [basalt_schema:ph_adjustment](https://EMSL-Computing.github.io/basalt-schema/ph_adjustment)
Alias: ph_adjustment

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaPreparation](MediaPreparation.md) | Activity that prepares a batch of growth media |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [MediaPreparation](MediaPreparation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:ph_adjustment |
| native | basalt_schema:ph_adjustment |




## LinkML Source

<details>
```yaml
name: ph_adjustment
description: Whether the entity was pH-adjusted
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: ph_adjustment
domain_of:
- MediaPreparation
range: boolean
required: false

```
</details>