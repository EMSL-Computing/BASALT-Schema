# Enum: FormulationEnum 




_Method used to formulate media._



URI: [analysis_api_schema:FormulationEnum](https://w3id.org/MONet/analysis-api-schema/FormulationEnum)

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


* from schema: https://w3id.org/MONet/analysis-api-schema






## LinkML Source

<details>
```yaml
name: FormulationEnum
description: Method used to formulate media.
todos:
- could be made generic for mixing more than just media.
from_schema: https://w3id.org/MONet/analysis-api-schema
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