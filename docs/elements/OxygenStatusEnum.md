# Enum: OxygenStatusEnum 




_Oxygen status of samples_



URI: [basalt_schema:OxygenStatusEnum](https://emsl-computing.github.io/BASALT-Schema/elements/OxygenStatusEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| aerobic | None | Aerobic conditions |
| anaerobic | None | Anaerobic conditions |
| anoxic | None | Anoxic conditions |
| facultative | None | Facultative conditions |
| microaerophilic | None | Microaerophilic conditions |
| microanaerobe | None | Microanaerobe conditions |
| obligate_aerobe | None | Obligate aerobe conditions |
| obligate_anaerobe | None | Obligate anaerobe conditions |




## Slots

| Name | Description |
| ---  | --- |
| [oxygen_relationship](oxygen_relationship.md) | The relationship of the sample to oxygen, such as aerobic or anaerobic |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema






## LinkML Source

<details>
```yaml
name: OxygenStatusEnum
description: Oxygen status of samples
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
permissible_values:
  aerobic:
    text: aerobic
    description: Aerobic conditions
  anaerobic:
    text: anaerobic
    description: Anaerobic conditions
  anoxic:
    text: anoxic
    description: Anoxic conditions
  facultative:
    text: facultative
    description: Facultative conditions
  microaerophilic:
    text: microaerophilic
    description: Microaerophilic conditions
  microanaerobe:
    text: microanaerobe
    description: Microanaerobe conditions
  obligate_aerobe:
    text: obligate_aerobe
    description: Obligate aerobe conditions
    aliases:
    - obligate aerobe
  obligate_anaerobe:
    text: obligate_anaerobe
    description: Obligate anaerobe conditions
    aliases:
    - obligate anaerobe

```
</details>