

# Slot: role 



URI: [analysis_api_schema:role](https://w3id.org/MONet/analysis-api-schema/role)
Alias: role

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProjectParticipant](ProjectParticipant.md) | A record of a person and their role on an EMSL project |  no  |
| [ProcessingSampleLink](ProcessingSampleLink.md) |  |  no  |






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
| self | analysis_api_schema:role |
| native | analysis_api_schema:role |




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