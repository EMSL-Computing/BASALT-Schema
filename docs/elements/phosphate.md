

# Slot: phosphate (phosphate) 


_Concentration of phosphate (Unit: umol/L)_





URI: [analysis_api_schema:phosphate](https://w3id.org/MONet/analysis-api-schema/phosphate)
Alias: phosphate

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*umol/L$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:phosphate |
| native | analysis_api_schema:phosphate |




## LinkML Source

<details>
```yaml
name: phosphate
description: 'Concentration of phosphate (Unit: umol/L)'
title: phosphate
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: phosphate
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*umol/L$

```
</details>