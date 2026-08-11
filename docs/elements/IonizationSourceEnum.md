# Enum: IonizationSourceEnum 



URI: [basalt_schema:IonizationSourceEnum](https://EMSL-Computing.github.io/basalt-schema/IonizationSourceEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| electrospray_ionization | None |  |
| matrix_assisted_laser_desorption_ionization | None |  |
| atmospheric_pressure_photo_ionization | None |  |
| atmospheric_pressure_chemical_ionization | None |  |
| electron_ionization | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [ionization](ionization.md) | Type of ionization used in the mass spectrometry method |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema






## LinkML Source

<details>
```yaml
name: IonizationSourceEnum
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
permissible_values:
  electrospray_ionization:
    text: electrospray_ionization
    aliases:
    - ESI
  matrix_assisted_laser_desorption_ionization:
    text: matrix_assisted_laser_desorption_ionization
    aliases:
    - MALDI
  atmospheric_pressure_photo_ionization:
    text: atmospheric_pressure_photo_ionization
    aliases:
    - APPI
  atmospheric_pressure_chemical_ionization:
    text: atmospheric_pressure_chemical_ionization
    aliases:
    - APCI
  electron_ionization:
    text: electron_ionization
    aliases:
    - EI

```
</details>