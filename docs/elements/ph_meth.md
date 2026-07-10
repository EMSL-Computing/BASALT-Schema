

# Slot: pH method (ph_meth) 


_Reference or method used in determining ph of the sample_





URI: [analysis_api_schema:ph_meth](https://w3id.org/MONet/analysis-api-schema/ph_meth)
Alias: ph_meth

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:ph_meth |
| native | analysis_api_schema:ph_meth |




## LinkML Source

<details>
```yaml
name: ph_meth
description: Reference or method used in determining ph of the sample
title: pH method
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: ph_meth
domain_of:
- OtherUndescribedSample
- SedimentSample
- SoilSample
- WaterSample
range: string

```
</details>