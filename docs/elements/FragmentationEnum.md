# Enum: FragmentationEnum 




_The fragmentation techniques used in mass spectrometry._



URI: [basalt_schema:FragmentationEnum](https://EMSL-Computing.github.io/basalt-schema/FragmentationEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| HCD | None | Higher-energy Collisional Dissociation |
| CID | None | Collision-Induced Dissociation |
| ETD | None | Electron Transfer Dissociation |




## Slots

| Name | Description |
| ---  | --- |
| [fragmentation](fragmentation.md) | fragmentation technique used in the mass spectrometry run |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema






## LinkML Source

<details>
```yaml
name: FragmentationEnum
description: The fragmentation techniques used in mass spectrometry.
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
permissible_values:
  HCD:
    text: HCD
    description: Higher-energy Collisional Dissociation
  CID:
    text: CID
    description: Collision-Induced Dissociation
  ETD:
    text: ETD
    description: Electron Transfer Dissociation

```
</details>