

# Slot: fertilizer regimen (fertilizer_regm) 


_Information about treatment involving the use of fertilizers; should include the name of fertilizer, amount administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple fertilizer regimens_





URI: [basalt_schema:fertilizer_regm](https://EMSL-Computing.github.io/basalt-schema/fertilizer_regm)
Alias: fertilizer_regm

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [PlantSample](PlantSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:fertilizer_regm |
| native | basalt_schema:fertilizer_regm |




## LinkML Source

<details>
```yaml
name: fertilizer_regm
description: Information about treatment involving the use of fertilizers; should
  include the name of fertilizer, amount administered, treatment regimen including
  how many times the treatment was repeated, how long each treatment lasted, and the
  start and end time of the entire treatment; can include multiple fertilizer regimens
title: fertilizer regimen
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: fertilizer_regm
domain_of:
- OtherUndescribedSample
- PlantSample
range: string

```
</details>