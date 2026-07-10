

# Slot: photochemical exposure (photochemical_exposure) 


_This term is used to describe a chemical reaction caused by absorption of ultraviolet (wavelength from 100 to 400 nm), visible light (400-750 nm), or infrared radiation (750-2500 nm)_





URI: [analysis_api_schema:photochemical_exposure](https://w3id.org/MONet/analysis-api-schema/photochemical_exposure)
Alias: photochemical_exposure

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |







## Properties

* Range: [PhotochemicalExposureEnum](PhotochemicalExposureEnum.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:photochemical_exposure |
| native | analysis_api_schema:photochemical_exposure |




## LinkML Source

<details>
```yaml
name: photochemical_exposure
description: This term is used to describe a chemical reaction caused by absorption
  of ultraviolet (wavelength from 100 to 400 nm), visible light (400-750 nm), or infrared
  radiation (750-2500 nm)
title: photochemical exposure
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: photochemical_exposure
domain_of:
- AerosolArmSample
- AerosolSample
- OtherUndescribedSample
range: PhotochemicalExposureEnum

```
</details>