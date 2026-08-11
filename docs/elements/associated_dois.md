

# Slot: associated_dois 


_A list of DOIs associated with this study_





URI: [basalt_schema:associated_dois](https://EMSL-Computing.github.io/basalt-schema/associated_dois)
Alias: associated_dois

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](Study.md) | A study or research project, typically associated with a proposal and a set o... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DOI](DOI.md) |
| Domain Of | [Study](Study.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Study](Study.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:associated_dois |
| native | basalt_schema:associated_dois |




## LinkML Source

<details>
```yaml
name: associated_dois
description: A list of DOIs associated with this study
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: associated_dois
owner: Study
domain_of:
- Study
range: DOI
multivalued: true

```
</details>