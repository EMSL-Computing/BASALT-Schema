

# Slot: solar irradiance (solar_irradiance) 


_Solar irradiance is the power per unit area (surface power density) received from the Sun in the form of electromagnetic radiation in the wavelength range of the measuring instrument. (Unit: kW/m2/d or erg/cm2/s_





URI: [analysis_api_schema:solar_irradiance](https://w3id.org/MONet/analysis-api-schema/solar_irradiance)
Alias: solar_irradiance

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*(kW/m2/d|erg/cm2/s)$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:solar_irradiance |
| native | analysis_api_schema:solar_irradiance |




## LinkML Source

<details>
```yaml
name: solar_irradiance
description: 'Solar irradiance is the power per unit area (surface power density)
  received from the Sun in the form of electromagnetic radiation in the wavelength
  range of the measuring instrument. (Unit: kW/m2/d or erg/cm2/s'
title: solar irradiance
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: solar_irradiance
domain_of:
- AerosolArmSample
- AerosolSample
- OtherUndescribedSample
range: string
pattern: ^\d+(\.\d+)?\s*(kW/m2/d|erg/cm2/s)$

```
</details>