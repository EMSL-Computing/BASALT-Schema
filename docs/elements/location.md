

# Slot: location 



URI: [basalt_schema:location](https://EMSL-Computing.github.io/basalt-schema/location)
Alias: location

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [KuoMethod](KuoMethod.md) |  |  no  |
| [TOCTNMethod](TOCTNMethod.md) |  |  no  |
| [MicrobialBiomassMethod](MicrobialBiomassMethod.md) |  |  no  |
| [EnzymeActivityMethod](EnzymeActivityMethod.md) |  |  no  |
| [XrayComputedTomographyMethod](XrayComputedTomographyMethod.md) |  |  no  |
| [PHMethod](PHMethod.md) |  |  no  |
| [HydraulicPropertiesMethod](HydraulicPropertiesMethod.md) |  |  no  |
| [GravimetricWaterContentMethod](GravimetricWaterContentMethod.md) |  |  no  |
| [Instrument](Instrument.md) | A material entity that is designed to perform a function in a scientific  |  no  |
| [TextureMethod](TextureMethod.md) |  |  no  |






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


* from schema: https://EMSL-Computing.github.io/basalt-schema




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
from_schema: https://EMSL-Computing.github.io/basalt-schema
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