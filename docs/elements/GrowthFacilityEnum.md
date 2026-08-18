# Enum: GrowthFacilityEnum 




_Types of growth facilities_



URI: [basalt_schema:GrowthFacilityEnum](https://emsl-computing.github.io/BASALT-Schema/elements/GrowthFacilityEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| field | None | Field conditions |
| commercially_purchased | None | Commercially purchased |
| experimental_garden | None | Experimental garden |
| field_incubation | None | Field incubation |
| greenhouse | None | Greenhouse |
| growth_chamber | None | Growth chamber |
| lab_incubation | None | Laboratory incubation |
| open_top_chamber | None | Open top chamber |
| other | None | Other growth facility type |




## Slots

| Name | Description |
| ---  | --- |
| [growth_facil](growth_facil.md) | Type of facility or location from where the sample was collected or |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema






## LinkML Source

<details>
```yaml
name: GrowthFacilityEnum
description: Types of growth facilities
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
permissible_values:
  field:
    text: field
    description: Field conditions
  commercially_purchased:
    text: commercially_purchased
    description: Commercially purchased
  experimental_garden:
    text: experimental_garden
    description: Experimental garden
  field_incubation:
    text: field_incubation
    description: Field incubation
  greenhouse:
    text: greenhouse
    description: Greenhouse
  growth_chamber:
    text: growth_chamber
    description: Growth chamber
  lab_incubation:
    text: lab_incubation
    description: Laboratory incubation
  open_top_chamber:
    text: open_top_chamber
    description: Open top chamber
  other:
    text: other
    description: Other growth facility type

```
</details>