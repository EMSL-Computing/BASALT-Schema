# Enum: CoreSectionEnum 




_Sections of a core sample_



URI: [basalt_schema:CoreSectionEnum](https://EMSL-Computing.github.io/BASALT-Schema/CoreSectionEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| TOP | None | Top section of core |
| BTM | None | Bottom section of core |
| MID | None | Middle section of core |




## Slots

| Name | Description |
| ---  | --- |
| [core_section](core_section.md) | The section of the core |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema






## LinkML Source

<details>
```yaml
name: CoreSectionEnum
description: Sections of a core sample
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
permissible_values:
  TOP:
    text: TOP
    description: Top section of core
  BTM:
    text: BTM
    description: Bottom section of core
  MID:
    text: MID
    description: Middle section of core

```
</details>