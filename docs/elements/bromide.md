

# Slot: bromide (bromide) 


_Concentration of bromide (Unit: ppm)_





URI: [analysis_api_schema:bromide](https://w3id.org/MONet/analysis-api-schema/bromide)
Alias: bromide

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*ppm$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:bromide |
| native | analysis_api_schema:bromide |




## LinkML Source

<details>
```yaml
name: bromide
description: 'Concentration of bromide (Unit: ppm)'
title: bromide
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: bromide
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*ppm$

```
</details>