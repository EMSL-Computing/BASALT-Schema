

# Slot: project_id 



URI: [basalt_schema:project_id](https://EMSL-Computing.github.io/basalt-schema/project_id)
Alias: project_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](Study.md) | A study or research project, typically associated with a proposal and a set o... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Study](Study.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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
| self | basalt_schema:project_id |
| native | basalt_schema:project_id |




## LinkML Source

<details>
```yaml
name: project_id
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: project_id
owner: Study
domain_of:
- Study
range: integer
required: true

```
</details>