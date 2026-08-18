

# Slot: step_number 



URI: [basalt_schema:step_number](https://emsl-computing.github.io/BASALT-Schema/elements/step_number)
Alias: step_number

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProcessingSampleLink](ProcessingSampleLink.md) | A link between a processed sample and the sample processing activity that pro... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [ProcessingSampleLink](ProcessingSampleLink.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ProcessingSampleLink](ProcessingSampleLink.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:step_number |
| native | basalt_schema:step_number |




## LinkML Source

<details>
```yaml
name: step_number
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: step_number
owner: ProcessingSampleLink
domain_of:
- ProcessingSampleLink
range: integer
required: true

```
</details>