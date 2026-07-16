

# Slot: pH (ph) 


_pH measurement of the sample or liquid portion of sample or aqueous phase of the fluid_





URI: [analysis_api_schema:ph](https://w3id.org/MONet/analysis-api-schema/ph)
Alias: ph

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [PHProduct](PHProduct.md) |  |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [PHProduct](PHProduct.md), [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:ph |
| native | analysis_api_schema:ph |




## LinkML Source

<details>
```yaml
name: ph
description: pH measurement of the sample or liquid portion of sample or aqueous phase
  of the fluid
title: pH
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: ph
domain_of:
- pHProduct
- OtherUndescribedSample
- SedimentSample
- SoilSample
- WaterSample
range: float

```
</details>