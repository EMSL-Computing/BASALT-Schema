# Enum: FormulationEnum 




_Method used to formulate media._



URI: [basalt_schema:FormulationEnum](https://emsl-computing.github.io/BASALT-Schema/elements/FormulationEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| manual_mix | None | Manually mixed from individual components |
| commercial | None | Commercially prepared (see commercial_media_catalog) |
| premixed | None | Pre-mixed from a stock solution |




## Slots

| Name | Description |
| ---  | --- |
| [media_formulation](media_formulation.md) | Formulation method of the media (manual mix, commercial, etc |








## TODOs

* could be made generic for mixing more than just media.



## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema






## LinkML Source

<details>
```yaml
name: FormulationEnum
description: Method used to formulate media.
todos:
- could be made generic for mixing more than just media.
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
permissible_values:
  manual_mix:
    text: manual_mix
    description: Manually mixed from individual components
  commercial:
    text: commercial
    description: Commercially prepared (see commercial_media_catalog)
  premixed:
    text: premixed
    description: Pre-mixed from a stock solution

```
</details>