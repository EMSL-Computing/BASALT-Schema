# Enum: SampleStoreTempEnum 




_Sample storage temperature conditions_



URI: [basalt_schema:SampleStoreTempEnum](https://emsl-computing.github.io/BASALT-Schema/elements/SampleStoreTempEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| fresh4 | None | Fresh storage at 4°C |
| freshroom | None | Fresh storage at room temperature |
| frozen20 | None | Frozen storage at -20°C |
| frozen80 | None | Frozen storage at -80°C |
| other | None | Other storage temperature |




## Slots

| Name | Description |
| ---  | --- |
| [samp_store_temp](samp_store_temp.md) | The temperature at which your samples should be stored upon arrival |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema






## LinkML Source

<details>
```yaml
name: SampleStoreTempEnum
description: Sample storage temperature conditions
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
permissible_values:
  fresh4:
    text: fresh4
    description: Fresh storage at 4°C
    aliases:
    - 4 C
  freshroom:
    text: freshroom
    description: Fresh storage at room temperature
    aliases:
    - room temperature
  frozen20:
    text: frozen20
    description: Frozen storage at -20°C
    aliases:
    - -20 C
  frozen80:
    text: frozen80
    description: Frozen storage at -80°C
    aliases:
    - -80 C
  other:
    text: other
    description: Other storage temperature

```
</details>