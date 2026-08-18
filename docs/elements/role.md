

# Slot: role 


_The role of the contributor in the study (e.g., data analysis, writing)._





URI: [basalt_schema:role](https://emsl-computing.github.io/BASALT-Schema/elements/role)
Alias: role

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProjectParticipant](ProjectParticipant.md) | A record of a person and their role on an EMSL project |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NexusRoleEnum](NexusRoleEnum.md) |
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


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:role |
| native | basalt_schema:role |




## LinkML Source

<details>
```yaml
name: role
description: The role of the contributor in the study (e.g., data analysis, writing).
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: role
owner: ProjectParticipant
domain_of:
- ProjectParticipant
range: NexusRoleEnum
required: true

```
</details>