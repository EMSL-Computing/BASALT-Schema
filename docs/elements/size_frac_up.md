

# Slot: size fraction upper threshold (size_frac_up) 


_Refers to the mesh/pore size used to retain the sample. Materials smaller than the size threshold are excluded from the sample_





URI: [analysis_api_schema:size_frac_up](https://w3id.org/MONet/analysis-api-schema/size_frac_up)
Alias: size_frac_up

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  yes  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  yes  |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  yes  |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AerosolArmSample](AerosolArmSample.md), [AerosolSample](AerosolSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [SoilSample](SoilSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:size_frac_up |
| native | analysis_api_schema:size_frac_up |




## LinkML Source

<details>
```yaml
name: size_frac_up
description: Refers to the mesh/pore size used to retain the sample. Materials smaller
  than the size threshold are excluded from the sample
title: size fraction upper threshold
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: size_frac_up
domain_of:
- AerosolArmSample
- AerosolSample
- OtherUndescribedSample
- SoilSample
- WaterSample
range: string

```
</details>