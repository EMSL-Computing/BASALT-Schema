

# Slot: media_ref 


_FK reference to a prepared media processedSample used in the activity._

_Maps to Montana's growth_medium (on CultureGrowth) and media_id_

_(on plate setup).  Points to processedSample(type=prepared_media)_

_produced by an upstream MediaPreparation activity._





URI: [basalt_schema:media_ref](https://EMSL-Computing.github.io/basalt-schema/media_ref)
Alias: media_ref

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AMP2WellMetadata](AMP2WellMetadata.md) | AMP2-specific per-well metadata |  no  |
| [AMP2PlateSetupActivity](AMP2PlateSetupActivity.md) | AMP2-specific plate setup |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ProcessedSample](ProcessedSample.md) |
| Domain Of | [AMP2PlateSetupActivity](AMP2PlateSetupActivity.md), [AMP2WellMetadata](AMP2WellMetadata.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:media_ref |
| native | basalt_schema:media_ref |




## LinkML Source

<details>
```yaml
name: media_ref
description: 'FK reference to a prepared media processedSample used in the activity.

  Maps to Montana''s growth_medium (on CultureGrowth) and media_id

  (on plate setup).  Points to processedSample(type=prepared_media)

  produced by an upstream MediaPreparation activity.'
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: media_ref
domain_of:
- AMP2PlateSetupActivity
- AMP2WellMetadata
range: ProcessedSample
required: false

```
</details>