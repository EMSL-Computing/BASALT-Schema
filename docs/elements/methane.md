

# Slot: methane (methane) 


_Methane (gas) amount or concentration at the time of sampling. (Unit: umol/L or ppb or ppm)_





URI: [analysis_api_schema:methane](https://w3id.org/MONet/analysis-api-schema/methane)
Alias: methane

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*(umol/L|ppm|ppb)$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:methane |
| native | analysis_api_schema:methane |




## LinkML Source

<details>
```yaml
name: methane
description: 'Methane (gas) amount or concentration at the time of sampling. (Unit:
  umol/L or ppb or ppm)'
title: methane
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: methane
domain_of:
- AerosolArmSample
- AerosolSample
- OtherUndescribedSample
- SedimentSample
range: string
pattern: ^\d+(\.\d+)?\s*(umol/L|ppm|ppb)$

```
</details>