

# Slot: pH method (ph_meth) 


_Reference or method used in determining ph of the sample_





URI: [basalt_schema:ph_meth](https://emsl-computing.github.io/BASALT-Schema/elements/ph_meth)
Alias: ph_meth

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:ph_meth |
| native | basalt_schema:ph_meth |




## LinkML Source

<details>
```yaml
name: ph_meth
description: Reference or method used in determining ph of the sample
title: pH method
from_schema: https://emsl-computing.github.io/BASALT-Schema
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