

# Slot: filter method (filter_method) 


_Type of filter used or how the sample was filtered_





URI: [analysis_api_schema:filter_method](https://w3id.org/MONet/analysis-api-schema/filter_method)
Alias: filter_method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  yes  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |






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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:filter_method |
| native | analysis_api_schema:filter_method |




## LinkML Source

<details>
```yaml
name: filter_method
description: Type of filter used or how the sample was filtered
title: filter method
from_schema: https://w3id.org/MONet/analysis-api-schema
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