

# Slot: organic matter (org_matter) 


_Concentration of organic matter (Unit: mg/L)_





URI: [analysis_api_schema:org_matter](https://w3id.org/MONet/analysis-api-schema/org_matter)
Alias: org_matter

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*mg/L$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:org_matter |
| native | analysis_api_schema:org_matter |




## LinkML Source

<details>
```yaml
name: org_matter
description: 'Concentration of organic matter (Unit: mg/L)'
title: organic matter
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: org_matter
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*mg/L$

```
</details>