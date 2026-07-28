

# Slot: fungicide regimen (fungicide_regm) 


_Information about treatment involving use of fungicides; should include the name of fungicide, amount administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple fungicide regimens_





URI: [analysis_api_schema:fungicide_regm](https://w3id.org/MONet/analysis-api-schema/fungicide_regm)
Alias: fungicide_regm

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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:fungicide_regm |
| native | analysis_api_schema:fungicide_regm |




## LinkML Source

<details>
```yaml
name: fungicide_regm
description: Information about treatment involving use of fungicides; should include
  the name of fungicide, amount administered, treatment regimen including how many
  times the treatment was repeated, how long each treatment lasted, and the start
  and end time of the entire treatment; can include multiple fungicide regimens
title: fungicide regimen
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: fungicide_regm
domain_of:
- OtherUndescribedSample
- PlantSample
range: string

```
</details>