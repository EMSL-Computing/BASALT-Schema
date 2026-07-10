

# Slot: pesticide regimen (pesticide_regm) 


_Information about treatment involving use of insecticides; should include the name of pesticide, amount administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple pesticide regimens_





URI: [analysis_api_schema:pesticide_regm](https://w3id.org/MONet/analysis-api-schema/pesticide_regm)
Alias: pesticide_regm

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
| self | analysis_api_schema:pesticide_regm |
| native | analysis_api_schema:pesticide_regm |




## LinkML Source

<details>
```yaml
name: pesticide_regm
description: Information about treatment involving use of insecticides; should include
  the name of pesticide, amount administered, treatment regimen including how many
  times the treatment was repeated, how long each treatment lasted, and the start
  and end time of the entire treatment; can include multiple pesticide regimens
title: pesticide regimen
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: pesticide_regm
domain_of:
- OtherUndescribedSample
- PlantSample
range: string

```
</details>