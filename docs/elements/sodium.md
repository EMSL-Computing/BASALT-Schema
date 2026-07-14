

# Slot: sodium (sodium) 


_Sodium concentration in the sample (Unit: ug/mL)_





URI: [analysis_api_schema:sodium](https://w3id.org/MONet/analysis-api-schema/sodium)
Alias: sodium

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*ug/mL$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:sodium |
| native | analysis_api_schema:sodium |




## LinkML Source

<details>
```yaml
name: sodium
description: 'Sodium concentration in the sample (Unit: ug/mL)'
title: sodium
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: sodium
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*ug/mL$

```
</details>