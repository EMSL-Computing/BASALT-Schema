

# Slot: magnesium (magnesium) 


_Concentration of magnesium in the sample (Unit: umol/kg or mol/L or mg/L or ppm)_





URI: [analysis_api_schema:magnesium](https://w3id.org/MONet/analysis-api-schema/magnesium)
Alias: magnesium

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*(umol/kg|mol/L|mg/L|ppm)$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:magnesium |
| native | analysis_api_schema:magnesium |




## LinkML Source

<details>
```yaml
name: magnesium
description: 'Concentration of magnesium in the sample (Unit: umol/kg or mol/L or
  mg/L or ppm)'
title: magnesium
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: magnesium
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(umol/kg|mol/L|mg/L|ppm)$

```
</details>