# Enum: MediaTypeEnum 




_Purpose/context of the media preparation._



URI: [basalt_schema:MediaTypeEnum](https://emsl-computing.github.io/BASALT-Schema/elements/MediaTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| strain_purity | None | Media used in strain purity checks |
| stock_culture | None | Media used in stock culture preparation |
| pre_culture | None | Media used in pre-culture growth |
| rich_media | None | Rich media for experimental culture growth |
| minimal_media | None | Minimal/defined media for experimental culture growth |




## Slots

| Name | Description |
| ---  | --- |
| [media_type](media_type.md) | Purpose/context of the media preparation |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema






## LinkML Source

<details>
```yaml
name: MediaTypeEnum
description: Purpose/context of the media preparation.
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
permissible_values:
  strain_purity:
    text: strain_purity
    description: Media used in strain purity checks
  stock_culture:
    text: stock_culture
    description: Media used in stock culture preparation
  pre_culture:
    text: pre_culture
    description: Media used in pre-culture growth
  rich_media:
    text: rich_media
    description: Rich media for experimental culture growth
  minimal_media:
    text: minimal_media
    description: Minimal/defined media for experimental culture growth

```
</details>