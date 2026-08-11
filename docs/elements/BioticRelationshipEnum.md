# Enum: BioticRelationshipEnum 




_Sample biotic relationships_



URI: [basalt_schema:BioticRelationshipEnum](https://EMSL-Computing.github.io/basalt-schema/BioticRelationshipEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| free_living | None | Free-living organism |
| parasite | None | Parasitic organism |
| commensal | None | Commensal organism |
| symbiont | None | Symbiotic organism |




## Slots

| Name | Description |
| ---  | --- |
| [biotic_relationship](biotic_relationship.md) | Description of relationship(s) between the subject organism and other organis... |







## Aliases


* sampbioticenum




## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema






## LinkML Source

<details>
```yaml
name: BioticRelationshipEnum
description: Sample biotic relationships
from_schema: https://EMSL-Computing.github.io/basalt-schema
aliases:
- sampbioticenum
rank: 1000
permissible_values:
  free_living:
    text: free_living
    description: Free-living organism
  parasite:
    text: parasite
    description: Parasitic organism
  commensal:
    text: commensal
    description: Commensal organism
  symbiont:
    text: symbiont
    description: Symbiotic organism

```
</details>