

# Slot: project_start 



URI: [basalt_schema:project_start](https://EMSL-Computing.github.io/basalt-schema/project_start)
Alias: project_start

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](Study.md) | A study or research project, typically associated with a proposal and a set o... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [Study](Study.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | basalt_schema:project_start |
| native | basalt_schema:project_start |




## LinkML Source

<details>
```yaml
name: project_start
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: project_start
owner: Study
domain_of:
- Study
range: datetime

```
</details>