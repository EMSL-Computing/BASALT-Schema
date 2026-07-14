

# Slot: aminopeptidase activity (aminopept_act) 


_Measurement of aminopeptidase activity (Unit: mol/L/h)_





URI: [analysis_api_schema:aminopept_act](https://w3id.org/MONet/analysis-api-schema/aminopept_act)
Alias: aminopept_act

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*mol/L/h$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:aminopept_act |
| native | analysis_api_schema:aminopept_act |




## LinkML Source

<details>
```yaml
name: aminopept_act
description: 'Measurement of aminopeptidase activity (Unit: mol/L/h)'
title: aminopeptidase activity
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: aminopept_act
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*mol/L/h$

```
</details>