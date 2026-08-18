

# Slot: role 



URI: [basalt_schema:role](https://emsl-computing.github.io/BASALT-Schema/elements/role)
Alias: role

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProcessingSampleLink](ProcessingSampleLink.md) | A link between a processed sample and the sample processing activity that pro... |  no  |
| [ProjectParticipant](ProjectParticipant.md) | A record of a person and their role on an EMSL project |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ProcessingSampleLink](ProcessingSampleLink.md), [ProjectParticipant](ProjectParticipant.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:role |
| native | basalt_schema:role |




## LinkML Source

<details>
```yaml
name: role
alias: role
domain_of:
- ProcessingSampleLink
- ProjectParticipant
range: string

```
</details>