

# Slot: location 



URI: [basalt_schema:location](https://emsl-computing.github.io/BASALT-Schema/elements/location)
Alias: location

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TextureMethod](TextureMethod.md) |  |  no  |
| [XrayComputedTomographyMethod](XrayComputedTomographyMethod.md) |  |  no  |
| [GravimetricWaterContentMethod](GravimetricWaterContentMethod.md) |  |  no  |
| [PHMethod](PHMethod.md) |  |  no  |
| [HydraulicPropertiesMethod](HydraulicPropertiesMethod.md) |  |  no  |
| [MicrobialBiomassMethod](MicrobialBiomassMethod.md) |  |  no  |
| [EnzymeActivityMethod](EnzymeActivityMethod.md) |  |  no  |
| [TOCTNMethod](TOCTNMethod.md) |  |  no  |
| [KuoMethod](KuoMethod.md) |  |  no  |
| [Instrument](Instrument.md) | A material entity that is designed to perform a function in a scientific  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Instrument](Instrument.md), [EnzymeActivityMethod](EnzymeActivityMethod.md), [GravimetricWaterContentMethod](GravimetricWaterContentMethod.md), [HydraulicPropertiesMethod](HydraulicPropertiesMethod.md), [KuoMethod](KuoMethod.md), [MicrobialBiomassMethod](MicrobialBiomassMethod.md), [PHMethod](PHMethod.md), [TOCTNMethod](TOCTNMethod.md), [TextureMethod](TextureMethod.md), [XrayComputedTomographyMethod](XrayComputedTomographyMethod.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |








## TODOs

* used on many method classes. no description. what was this meant to mean?



## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:location |
| native | basalt_schema:location |




## LinkML Source

<details>
```yaml
name: location
todos:
- used on many method classes. no description. what was this meant to mean?
from_schema: https://emsl-computing.github.io/BASALT-Schema
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