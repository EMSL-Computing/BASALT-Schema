# Enum: EluentIntroductionEnum 




_The method used to introduce the eluent into the mass spectrometer._



URI: [basalt_schema:EluentIntroductionEnum](https://emsl-computing.github.io/BASALT-Schema/elements/EluentIntroductionEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| direct_infusion_syringe | None | Direct infusion of the sample into the mass spectrometer |
| liquid_chromatography | None | Introduction via liquid chromatography |
| gas_chromatography | None | Introduction via gas chromatography |
| direct_infusion_autosampler | None | Direct infusion using an autosampler |













## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema






## LinkML Source

<details>
```yaml
name: EluentIntroductionEnum
description: The method used to introduce the eluent into the mass spectrometer.
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
permissible_values:
  direct_infusion_syringe:
    text: direct_infusion_syringe
    description: Direct infusion of the sample into the mass spectrometer
  liquid_chromatography:
    text: liquid_chromatography
    description: Introduction via liquid chromatography
  gas_chromatography:
    text: gas_chromatography
    description: Introduction via gas chromatography
  direct_infusion_autosampler:
    text: direct_infusion_autosampler
    description: Direct infusion using an autosampler

```
</details>