

# Slot: sample_base_id 



URI: [basalt_schema:sample_base_id](https://emsl-computing.github.io/BASALT-Schema/elements/sample_base_id)
Alias: sample_base_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProcessingSampleLink](ProcessingSampleLink.md) | A link between a processed sample and the sample processing activity that pro... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Sample](Sample.md) |
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
| self | basalt_schema:sample_base_id |
| native | basalt_schema:sample_base_id |




## LinkML Source

<details>
```yaml
name: sample_base_id
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: sample_base_id
owner: ProcessingSampleLink
domain_of:
- ProcessingSampleLink
range: Sample
required: true

```
</details>