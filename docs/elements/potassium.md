

# Slot: potassium (potassium) 


_Concentration of potassium in the sample (Unit: mg/L)_





URI: [analysis_api_schema:potassium](https://w3id.org/MONet/analysis-api-schema/potassium)
Alias: potassium

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*(mg/L|ppm)$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:potassium |
| native | analysis_api_schema:potassium |




## LinkML Source

<details>
```yaml
name: potassium
description: 'Concentration of potassium in the sample (Unit: mg/L)'
title: potassium
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: potassium
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(mg/L|ppm)$

```
</details>