

# Slot: has_participants 


_Links to a record of a person and their roles for this study._





URI: [basalt_schema:has_participants](https://emsl-computing.github.io/BASALT-Schema/elements/has_participants)
Alias: has_participants

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](Study.md) | A study or research project, typically associated with a proposal and a set o... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ProjectParticipant](ProjectParticipant.md) |
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


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:has_participants |
| native | basalt_schema:has_participants |




## LinkML Source

<details>
```yaml
name: has_participants
description: Links to a record of a person and their roles for this study.
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: has_participants
owner: Study
domain_of:
- Study
range: ProjectParticipant
multivalued: true

```
</details>