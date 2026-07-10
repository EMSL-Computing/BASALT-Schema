

# Slot: particulate organic nitrogen (part_org_nitro) 


_Concentration of particulate organic nitrogen. (Unit: ug/L or umol/L)_





URI: [analysis_api_schema:part_org_nitro](https://w3id.org/MONet/analysis-api-schema/part_org_nitro)
Alias: part_org_nitro

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
| self | analysis_api_schema:part_org_nitro |
| native | analysis_api_schema:part_org_nitro |




## LinkML Source

<details>
```yaml
name: part_org_nitro
description: 'Concentration of particulate organic nitrogen. (Unit: ug/L or umol/L)'
title: particulate organic nitrogen
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: part_org_nitro
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(umol/L|ug/L)$

```
</details>