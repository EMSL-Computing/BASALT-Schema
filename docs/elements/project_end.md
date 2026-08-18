

# Slot: project_end 



URI: [basalt_schema:project_end](https://EMSL-Computing.github.io/BASALT-Schema/project_end)
Alias: project_end

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


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:project_end |
| native | basalt_schema:project_end |




## LinkML Source

<details>
```yaml
name: project_end
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: project_end
owner: Study
domain_of:
- Study
range: datetime

```
</details>