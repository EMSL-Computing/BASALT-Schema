

# Slot: n-alkanes (n_alkanes) 


_Concentration of n-alkanes; can include multiple n-alkanes (Unit: ug/mL)_





URI: [analysis_api_schema:n_alkanes](https://w3id.org/MONet/analysis-api-schema/n_alkanes)
Alias: n_alkanes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:n_alkanes |
| native | analysis_api_schema:n_alkanes |




## LinkML Source

<details>
```yaml
name: n_alkanes
description: 'Concentration of n-alkanes; can include multiple n-alkanes (Unit: ug/mL)'
title: n-alkanes
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: n_alkanes
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string

```
</details>