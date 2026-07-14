

# Slot: total phosphorus (tot_phosp) 


_Total phosphorus concentration in the sample calculated by: total phosphorus = total dissolved phosphorus + particulate phosphorus. (Unit: ug/L or umol/L)_





URI: [analysis_api_schema:tot_phosp](https://w3id.org/MONet/analysis-api-schema/tot_phosp)
Alias: tot_phosp

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*(ug/L|umol/L)$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:tot_phosp |
| native | analysis_api_schema:tot_phosp |




## LinkML Source

<details>
```yaml
name: tot_phosp
description: 'Total phosphorus concentration in the sample calculated by: total phosphorus
  = total dissolved phosphorus + particulate phosphorus. (Unit: ug/L or umol/L)'
title: total phosphorus
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: tot_phosp
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(ug/L|umol/L)$

```
</details>