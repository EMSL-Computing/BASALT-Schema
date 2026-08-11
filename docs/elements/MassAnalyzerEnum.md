# Enum: MassAnalyzerEnum 



URI: [basalt_schema:MassAnalyzerEnum](https://EMSL-Computing.github.io/basalt-schema/MassAnalyzerEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| quadrupole | None |  |
| time_of_flight | None |  |
| orbitrap | None |  |
| ion_trap | None |  |
| ion_cyclotron_resonance | None |  |
| fourier_transform_ion_cyclotron_resonance | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [mass_analyzer_type](mass_analyzer_type.md) | The type of mass analyzer present in the instrument, if applicable (e |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema






## LinkML Source

<details>
```yaml
name: MassAnalyzerEnum
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
permissible_values:
  quadrupole:
    text: quadrupole
    aliases:
    - Q
  time_of_flight:
    text: time_of_flight
    aliases:
    - TOF
  orbitrap:
    text: orbitrap
  ion_trap:
    text: ion_trap
    aliases:
    - IT
  ion_cyclotron_resonance:
    text: ion_cyclotron_resonance
    aliases:
    - ICR
  fourier_transform_ion_cyclotron_resonance:
    text: fourier_transform_ion_cyclotron_resonance
    aliases:
    - FTICR

```
</details>