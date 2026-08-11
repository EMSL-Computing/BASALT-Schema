

# Slot: alkalinity method (alkalinity_method) 


_Method used for alkalinity measurement_





URI: [basalt_schema:alkalinity_method](https://w3id.org/MONet/basalt-schema/alkalinity_method)
Alias: alkalinity_method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:alkalinity_method |
| native | basalt_schema:alkalinity_method |




## LinkML Source

<details>
```yaml
name: alkalinity_method
description: Method used for alkalinity measurement
title: alkalinity method
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: alkalinity_method
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string

```
</details>