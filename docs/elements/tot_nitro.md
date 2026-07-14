

# Slot: total nitrogen (tot_nitro) 


_Total nitrogen concentration of water samples calculated by: total nitrogen = total dissolved nitrogen + particulate nitrogen. Can also be measured without filtering reported as nitrogen. (Unit: ug/L or umol/L or mg/L)_





URI: [analysis_api_schema:tot_nitro](https://w3id.org/MONet/analysis-api-schema/tot_nitro)
Alias: tot_nitro

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*(ug/L|umol/L|mg/L)$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:tot_nitro |
| native | analysis_api_schema:tot_nitro |




## LinkML Source

<details>
```yaml
name: tot_nitro
description: 'Total nitrogen concentration of water samples calculated by: total nitrogen
  = total dissolved nitrogen + particulate nitrogen. Can also be measured without
  filtering reported as nitrogen. (Unit: ug/L or umol/L or mg/L)'
title: total nitrogen
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: tot_nitro
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(ug/L|umol/L|mg/L)$

```
</details>