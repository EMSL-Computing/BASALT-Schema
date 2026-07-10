

# Slot: herbicide regimen (herbicide_regm) 


_Information about treatment involving use of herbicides; information about treatment involving use of growth hormones; should include the name of herbicide, amount administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple regimens_





URI: [analysis_api_schema:herbicide_regm](https://w3id.org/MONet/analysis-api-schema/herbicide_regm)
Alias: herbicide_regm

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:herbicide_regm |
| native | analysis_api_schema:herbicide_regm |




## LinkML Source

<details>
```yaml
name: herbicide_regm
description: Information about treatment involving use of herbicides; information
  about treatment involving use of growth hormones; should include the name of herbicide,
  amount administered, treatment regimen including how many times the treatment was
  repeated, how long each treatment lasted, and the start and end time of the entire
  treatment; can include multiple regimens
title: herbicide regimen
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: herbicide_regm
domain_of:
- OtherUndescribedSample
- PlantSample
range: string

```
</details>