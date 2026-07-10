

# Slot: salinity (salinity) 


_Salinity is the total concentration of all dissolved salts in a sample. While salinity can be measured by a complete chemical analysis, this method is difficult and time consuming. More often it is instead derived from the conductivity measurement. This is known as practical salinity. These derivations compare the specific conductance of the sample to a salinity standard such as seawater (Unit: practical salinity unit or percent)_





URI: [analysis_api_schema:salinity](https://w3id.org/MONet/analysis-api-schema/salinity)
Alias: salinity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*(practical salinity unit|percent)$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:salinity |
| native | analysis_api_schema:salinity |




## LinkML Source

<details>
```yaml
name: salinity
description: 'Salinity is the total concentration of all dissolved salts in a sample.
  While salinity can be measured by a complete chemical analysis, this method is difficult
  and time consuming. More often it is instead derived from the conductivity measurement.
  This is known as practical salinity. These derivations compare the specific conductance
  of the sample to a salinity standard such as seawater (Unit: practical salinity
  unit or percent)'
title: salinity
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: salinity
domain_of:
- OtherUndescribedSample
- PlantSample
- SedimentSample
- SoilSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(practical salinity unit|percent)$

```
</details>