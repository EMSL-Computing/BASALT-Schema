

# Slot: dissolved inorganic phosphate (diss_inorg_phosp) 


_Concentration of dissolved inorganic phosphorus in the sample. Provide value and unit, any unit is valid._





URI: [analysis_api_schema:diss_inorg_phosp](https://w3id.org/MONet/analysis-api-schema/diss_inorg_phosp)
Alias: diss_inorg_phosp

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*[\w\s/]+$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:diss_inorg_phosp |
| native | analysis_api_schema:diss_inorg_phosp |




## LinkML Source

<details>
```yaml
name: diss_inorg_phosp
description: Concentration of dissolved inorganic phosphorus in the sample. Provide
  value and unit, any unit is valid.
title: dissolved inorganic phosphate
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: diss_inorg_phosp
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>