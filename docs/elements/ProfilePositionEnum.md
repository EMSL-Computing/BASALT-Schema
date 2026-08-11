# Enum: ProfilePositionEnum 




_Soil profile positions_



URI: [basalt_schema:ProfilePositionEnum](https://EMSL-Computing.github.io/basalt-schema/ProfilePositionEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| backslope | None | Backslope position |
| footslope | None | Footslope position |
| shoulder | None | Shoulder position |
| summit | None | Summit position |
| toeslope | None | Toeslope position |




## Slots

| Name | Description |
| ---  | --- |
| [profile_position](profile_position.md) | Cross-sectional position in the hillslope where sample was collected |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema






## LinkML Source

<details>
```yaml
name: ProfilePositionEnum
description: Soil profile positions
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
permissible_values:
  backslope:
    text: backslope
    description: Backslope position
    aliases:
    - Backslope
  footslope:
    text: footslope
    description: Footslope position
    aliases:
    - Footslope
  shoulder:
    text: shoulder
    description: Shoulder position
    aliases:
    - Shoulder
  summit:
    text: summit
    description: Summit position
    aliases:
    - Summit
  toeslope:
    text: toeslope
    description: Toeslope position
    aliases:
    - Toeslope

```
</details>