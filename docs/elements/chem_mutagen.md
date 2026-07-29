

# Slot: chemical mutagen (chem_mutagen) 


_Treatment involving use of mutagens; should include the name of mutagen, amount administered, treatment regimen, including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple mutagen regimens_





URI: [analysis_api_schema:chem_mutagen](https://w3id.org/MONet/analysis-api-schema/chem_mutagen)
Alias: chem_mutagen

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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:chem_mutagen |
| native | analysis_api_schema:chem_mutagen |




## LinkML Source

<details>
```yaml
name: chem_mutagen
description: Treatment involving use of mutagens; should include the name of mutagen,
  amount administered, treatment regimen, including how many times the treatment was
  repeated, how long each treatment lasted, and the start and end time of the entire
  treatment; can include multiple mutagen regimens
title: chemical mutagen
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: chem_mutagen
domain_of:
- OtherUndescribedSample
- PlantSample
range: string

```
</details>