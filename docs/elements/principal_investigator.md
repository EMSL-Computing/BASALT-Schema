

# Slot: principal_investigator 



URI: [basalt_schema:principal_investigator](https://EMSL-Computing.github.io/basalt-schema/principal_investigator)
Alias: principal_investigator

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](Study.md) | A study or research project, typically associated with a proposal and a set o... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PersonValue](PersonValue.md) |
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
| self | basalt_schema:principal_investigator |
| native | basalt_schema:principal_investigator |




## LinkML Source

<details>
```yaml
name: principal_investigator
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: principal_investigator
owner: Study
domain_of:
- Study
range: PersonValue
required: true

```
</details>