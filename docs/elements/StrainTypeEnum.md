# Enum: StrainTypeEnum 




_Types of microbial strains/organisms._



URI: [basalt_schema:StrainTypeEnum](https://w3id.org/MONet/basalt-schema/StrainTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| bacterial | None | Bacterial strain |
| fungal | None | Fungal strain |
| archaeal | None | Archaeal strain |
| viral | None | Viral isolate |
| algal | None | Algal strain |
| protist | None | Protist strain |
| other | None | Other organism type |




## Slots

| Name | Description |
| ---  | --- |
| [strain_type](strain_type.md) | Type of strain/organism (bacterial, fungal, archaeal, etc |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema






## LinkML Source

<details>
```yaml
name: StrainTypeEnum
description: Types of microbial strains/organisms.
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
permissible_values:
  bacterial:
    text: bacterial
    description: Bacterial strain
    aliases:
    - bacteria
  fungal:
    text: fungal
    description: Fungal strain
    aliases:
    - fungi
    - yeast
  archaeal:
    text: archaeal
    description: Archaeal strain
    aliases:
    - archaea
  viral:
    text: viral
    description: Viral isolate
    aliases:
    - virus
    - phage
    - bacteriophage
  algal:
    text: algal
    description: Algal strain
    aliases:
    - algae
  protist:
    text: protist
    description: Protist strain
  other:
    text: other
    description: Other organism type

```
</details>