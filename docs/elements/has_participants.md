

# Slot: has_participants 


_Links to a record of a person and their roles for this study._





URI: [analysis_api_schema:has_participants](https://w3id.org/MONet/analysis-api-schema/has_participants)
Alias: has_participants

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](Study.md) |  |  no  |






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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:has_participants |
| native | analysis_api_schema:has_participants |




## LinkML Source

<details>
```yaml
name: has_participants
description: Links to a record of a person and their roles for this study.
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: has_participants
owner: Study
domain_of:
- Study
range: ProjectParticipant
multivalued: true

```
</details>