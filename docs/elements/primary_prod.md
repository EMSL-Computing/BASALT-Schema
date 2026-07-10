

# Slot: primary production (primary_prod) 


_Measurement of primary production generally measured as isotope uptake. Provide value and unit, any unit is valid._





URI: [analysis_api_schema:primary_prod](https://w3id.org/MONet/analysis-api-schema/primary_prod)
Alias: primary_prod

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
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
| self | analysis_api_schema:primary_prod |
| native | analysis_api_schema:primary_prod |




## LinkML Source

<details>
```yaml
name: primary_prod
description: Measurement of primary production generally measured as isotope uptake.
  Provide value and unit, any unit is valid.
title: primary production
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: primary_prod
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>