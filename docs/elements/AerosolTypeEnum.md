# Enum: AerosolTypeEnum 




_Types of aerosol samples_



URI: [basalt_schema:AerosolTypeEnum](https://emsl-computing.github.io/BASALT-Schema/elements/AerosolTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| sea_salt | None | Sea salt aerosol |
| dust | None | Dust aerosol |
| volcanic_ash | None | Volcanic ash aerosol |




## Slots

| Name | Description |
| ---  | --- |
| [aerosol_type](aerosol_type.md) | The type or method of aerosol collection |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema






## LinkML Source

<details>
```yaml
name: AerosolTypeEnum
description: Types of aerosol samples
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
permissible_values:
  sea_salt:
    text: sea_salt
    description: Sea salt aerosol
  dust:
    text: dust
    description: Dust aerosol
  volcanic_ash:
    text: volcanic_ash
    description: Volcanic ash aerosol

```
</details>