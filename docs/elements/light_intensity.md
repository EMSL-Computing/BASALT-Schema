

# Slot: light intensity (light_intensity) 


_Measurement of light intensity. Provide value and unit, any unit is valid._





URI: [analysis_api_schema:light_intensity](https://w3id.org/MONet/analysis-api-schema/light_intensity)
Alias: light_intensity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*[\w\s/]+$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:light_intensity |
| native | analysis_api_schema:light_intensity |




## LinkML Source

<details>
```yaml
name: light_intensity
description: Measurement of light intensity. Provide value and unit, any unit is valid.
title: light intensity
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: light_intensity
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>