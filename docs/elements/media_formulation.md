

# Slot: media_formulation 


_Formulation method of the media (manual mix, commercial, etc.)_





URI: [basalt_schema:media_formulation](https://EMSL-Computing.github.io/basalt-schema/media_formulation)
Alias: media_formulation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaPreparation](MediaPreparation.md) | Activity that prepares a batch of growth media |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [FormulationEnum](FormulationEnum.md) |
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
| self | basalt_schema:media_formulation |
| native | basalt_schema:media_formulation |




## LinkML Source

<details>
```yaml
name: media_formulation
description: Formulation method of the media (manual mix, commercial, etc.)
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: media_formulation
domain_of:
- MediaPreparation
range: FormulationEnum

```
</details>