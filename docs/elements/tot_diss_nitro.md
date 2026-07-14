

# Slot: total dissolved nitrogen (tot_diss_nitro) 


_Total dissolved nitrogen concentration reported as nitrogen measured by: total dissolved nitrogen = NH4 + NO3NO2 + dissolved organic nitrogen. (Unit: ug/L)_





URI: [analysis_api_schema:tot_diss_nitro](https://w3id.org/MONet/analysis-api-schema/tot_diss_nitro)
Alias: tot_diss_nitro

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*(ug/L)$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:tot_diss_nitro |
| native | analysis_api_schema:tot_diss_nitro |




## LinkML Source

<details>
```yaml
name: tot_diss_nitro
description: 'Total dissolved nitrogen concentration reported as nitrogen measured
  by: total dissolved nitrogen = NH4 + NO3NO2 + dissolved organic nitrogen. (Unit:
  ug/L)'
title: total dissolved nitrogen
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: tot_diss_nitro
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(ug/L)$

```
</details>