

# Slot: dissolved inorganic nitrogen (diss_inorg_nitro) 


_Concentration of dissolved inorganic nitrogen. (Unit: ug/L or umol/L)_





URI: [analysis_api_schema:diss_inorg_nitro](https://w3id.org/MONet/analysis-api-schema/diss_inorg_nitro)
Alias: diss_inorg_nitro

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*(umol/L|ug/L)$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:diss_inorg_nitro |
| native | analysis_api_schema:diss_inorg_nitro |




## LinkML Source

<details>
```yaml
name: diss_inorg_nitro
description: 'Concentration of dissolved inorganic nitrogen. (Unit: ug/L or umol/L)'
title: dissolved inorganic nitrogen
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: diss_inorg_nitro
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(umol/L|ug/L)$

```
</details>