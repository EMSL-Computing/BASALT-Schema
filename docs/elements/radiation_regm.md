

# Slot: radiation regimen (radiation_regm) 


_Information about treatment involving exposure of plant or a plant part to a particular radiation regimen; should include the radiation type, amount or intensity administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple radiation regimens_





URI: [basalt_schema:radiation_regm](https://EMSL-Computing.github.io/basalt-schema/radiation_regm)
Alias: radiation_regm

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:radiation_regm |
| native | basalt_schema:radiation_regm |




## LinkML Source

<details>
```yaml
name: radiation_regm
description: Information about treatment involving exposure of plant or a plant part
  to a particular radiation regimen; should include the radiation type, amount or
  intensity administered, treatment regimen including how many times the treatment
  was repeated, how long each treatment lasted, and the start and end time of the
  entire treatment; can include multiple radiation regimens
title: radiation regimen
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: radiation_regm
domain_of:
- OtherUndescribedSample
range: string

```
</details>