

# Slot: media_type 


_Purpose/context of the media preparation._

_Examples: strain_purity, stock_culture, pre_culture, rich_media._





URI: [basalt_schema:media_type](https://w3id.org/MONet/basalt-schema/media_type)
Alias: media_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaPreparation](MediaPreparation.md) | Activity that prepares a batch of growth media |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MediaTypeEnum](MediaTypeEnum.md) |
| Domain Of | [MediaPreparation](MediaPreparation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:media_type |
| native | basalt_schema:media_type |




## LinkML Source

<details>
```yaml
name: media_type
description: 'Purpose/context of the media preparation.

  Examples: strain_purity, stock_culture, pre_culture, rich_media.'
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: media_type
domain_of:
- MediaPreparation
range: MediaTypeEnum

```
</details>