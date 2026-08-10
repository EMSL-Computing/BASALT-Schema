

# Slot: person 


_The person who contributed to the study._





URI: [basalt_schema:person](https://w3id.org/MONet/basalt-schema/person)
Alias: person

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProjectParticipant](ProjectParticipant.md) | A record of a person and their role on an EMSL project |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PersonValue](PersonValue.md) |
| Domain Of | [ProjectParticipant](ProjectParticipant.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ProjectParticipant](ProjectParticipant.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:person |
| native | basalt_schema:person |




## LinkML Source

<details>
```yaml
name: person
description: The person who contributed to the study.
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: person
owner: ProjectParticipant
domain_of:
- ProjectParticipant
range: PersonValue
required: true

```
</details>