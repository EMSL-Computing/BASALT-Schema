

# Slot: tidal stage (tidal_stage) 


_Stage of tide_





URI: [analysis_api_schema:tidal_stage](https://w3id.org/MONet/analysis-api-schema/tidal_stage)
Alias: tidal_stage

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |







## Properties

* Range: [TidalStageEnum](TidalStageEnum.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:tidal_stage |
| native | analysis_api_schema:tidal_stage |




## LinkML Source

<details>
```yaml
name: tidal_stage
description: Stage of tide
title: tidal stage
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: tidal_stage
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: TidalStageEnum

```
</details>