

# Slot: salinity method (salinity_method) 


_Method used to determine sample salinity_





URI: [basalt_schema:salinity_method](https://w3id.org/MONet/basalt-schema/salinity_method)
Alias: salinity_method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [PlantSample](PlantSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:salinity_method |
| native | basalt_schema:salinity_method |




## LinkML Source

<details>
```yaml
name: salinity_method
description: Method used to determine sample salinity
title: salinity method
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: salinity_method
domain_of:
- OtherUndescribedSample
- PlantSample
- SedimentSample
- SoilSample
- WaterSample
range: string

```
</details>