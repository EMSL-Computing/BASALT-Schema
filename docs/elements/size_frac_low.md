

# Slot: size fraction lower threshold (size_frac_low) 


_Refers to the mesh/pore size used to pre-filter/pre-sort the sample. Materials larger than the size threshold are excluded from the sample_





URI: [analysis_api_schema:size_frac_low](https://w3id.org/MONet/analysis-api-schema/size_frac_low)
Alias: size_frac_low

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  yes  |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  yes  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  yes  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:size_frac_low |
| native | analysis_api_schema:size_frac_low |




## LinkML Source

<details>
```yaml
name: size_frac_low
description: Refers to the mesh/pore size used to pre-filter/pre-sort the sample.
  Materials larger than the size threshold are excluded from the sample
title: size fraction lower threshold
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: size_frac_low
domain_of:
- AerosolArmSample
- AerosolSample
- OtherUndescribedSample
- SoilSample
- WaterSample
range: string

```
</details>