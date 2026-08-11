

# Slot: ph_target 


_Target pH value (required if ph_adjustment is true)_





URI: [basalt_schema:ph_target](https://EMSL-Computing.github.io/basalt-schema/ph_target)
Alias: ph_target

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaPreparation](MediaPreparation.md) | Activity that prepares a batch of growth media |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
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
| self | basalt_schema:ph_target |
| native | basalt_schema:ph_target |




## LinkML Source

<details>
```yaml
name: ph_target
description: Target pH value (required if ph_adjustment is true)
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: ph_target
domain_of:
- MediaPreparation
range: float
required: false

```
</details>