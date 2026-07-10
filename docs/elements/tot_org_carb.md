

# Slot: total organic carbon (tot_org_carb) 


_Total organic carbon content. Provided as gram of Carbon per kg of your sample material. (Unit: g C/kg)_





URI: [analysis_api_schema:tot_org_carb](https://w3id.org/MONet/analysis-api-schema/tot_org_carb)
Alias: tot_org_carb

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*g C/kg$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:tot_org_carb |
| native | analysis_api_schema:tot_org_carb |




## LinkML Source

<details>
```yaml
name: tot_org_carb
description: 'Total organic carbon content. Provided as gram of Carbon per kg of your
  sample material. (Unit: g C/kg)'
title: total organic carbon
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: tot_org_carb
domain_of:
- OtherUndescribedSample
- SedimentSample
- SoilSample
range: string
pattern: ^\d+(\.\d+)?\s*g C/kg$

```
</details>