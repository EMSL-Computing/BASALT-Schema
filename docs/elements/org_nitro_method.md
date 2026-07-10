

# Slot: organic nitrogen method (org_nitro_method) 


_Method used for obtaining organic nitrogen_





URI: [analysis_api_schema:org_nitro_method](https://w3id.org/MONet/analysis-api-schema/org_nitro_method)
Alias: org_nitro_method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:org_nitro_method |
| native | analysis_api_schema:org_nitro_method |




## LinkML Source

<details>
```yaml
name: org_nitro_method
description: Method used for obtaining organic nitrogen
title: organic nitrogen method
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: org_nitro_method
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string

```
</details>