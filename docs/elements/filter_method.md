

# Slot: filter method (filter_method) 


_Type of filter used or how the sample was filtered_





URI: [basalt_schema:filter_method](https://EMSL-Computing.github.io/BASALT-Schema/filter_method)
Alias: filter_method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [CultureEnvironmentalSample](CultureEnvironmentalSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [PureCultureSample](PureCultureSample.md), [SoilSample](SoilSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:filter_method |
| native | basalt_schema:filter_method |




## LinkML Source

<details>
```yaml
name: filter_method
description: Type of filter used or how the sample was filtered
title: filter method
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: filter_method
domain_of:
- CultureEnvironmentalSample
- OtherUndescribedSample
- PureCultureSample
- SoilSample
- WaterSample
range: string

```
</details>