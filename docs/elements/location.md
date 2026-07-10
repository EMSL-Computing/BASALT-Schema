

# Slot: location 



URI: [analysis_api_schema:location](https://w3id.org/MONet/analysis-api-schema/location)
Alias: location

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EnzymeActivityMethod](EnzymeActivityMethod.md) |  |  no  |
| [MicrobialBiomassMethod](MicrobialBiomassMethod.md) |  |  no  |
| [PHMethod](PHMethod.md) |  |  no  |
| [TOCTNMethod](TOCTNMethod.md) |  |  no  |
| [HydraulicPropertiesMethod](HydraulicPropertiesMethod.md) |  |  no  |
| [Instrument](Instrument.md) | A material entity that is designed to perform a function in a scientific  |  no  |
| [XrayComputedTomographyMethod](XrayComputedTomographyMethod.md) |  |  no  |
| [KuoMethod](KuoMethod.md) |  |  no  |
| [GravimetricWaterContentMethod](GravimetricWaterContentMethod.md) |  |  no  |
| [TextureMethod](TextureMethod.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## TODOs

* used on many method classes. no description. what was this meant to mean?

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:location |
| native | analysis_api_schema:location |




## LinkML Source

<details>
```yaml
name: location
todos:
- used on many method classes. no description. what was this meant to mean?
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: location
domain_of:
- Instrument
- EnzymeActivityMethod
- GravimetricWaterContentMethod
- HydraulicPropertiesMethod
- KuoMethod
- MicrobialBiomassMethod
- PH_Method
- TOC_TN_Method
- TextureMethod
- XrayComputedTomographyMethod
range: string
required: true

```
</details>