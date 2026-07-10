

# Slot: total nitrogen content (tot_nitro_content) 


_Total nitrogen content of the sample. Provide value and unit any unit is valid_





URI: [analysis_api_schema:tot_nitro_content](https://w3id.org/MONet/analysis-api-schema/tot_nitro_content)
Alias: tot_nitro_content

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*[\w\s/]+$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:tot_nitro_content |
| native | analysis_api_schema:tot_nitro_content |




## LinkML Source

<details>
```yaml
name: tot_nitro_content
description: Total nitrogen content of the sample. Provide value and unit any unit
  is valid
title: total nitrogen content
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: tot_nitro_content
domain_of:
- OtherUndescribedSample
- SedimentSample
- SoilSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>