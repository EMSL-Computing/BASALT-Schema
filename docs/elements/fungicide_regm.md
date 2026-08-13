

# Slot: fungicide regimen (fungicide_regm) 


_Information about treatment involving use of fungicides; should include the name of fungicide, amount administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple fungicide regimens_





URI: [basalt_schema:fungicide_regm](https://EMSL-Computing.github.io/basalt-schema/fungicide_regm)
Alias: fungicide_regm

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |






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
| self | basalt_schema:fungicide_regm |
| native | basalt_schema:fungicide_regm |




## LinkML Source

<details>
```yaml
name: fungicide_regm
description: Information about treatment involving use of fungicides; should include
  the name of fungicide, amount administered, treatment regimen including how many
  times the treatment was repeated, how long each treatment lasted, and the start
  and end time of the entire treatment; can include multiple fungicide regimens
title: fungicide regimen
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: fungicide_regm
domain_of:
- OtherUndescribedSample
- PlantSample
range: string

```
</details>