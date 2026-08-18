

# Slot: first_name 



URI: [basalt_schema:first_name](https://EMSL-Computing.github.io/BASALT-Schema/first_name)
Alias: first_name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonValue](PersonValue.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PersonValue](PersonValue.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PersonValue](PersonValue.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:first_name |
| native | basalt_schema:first_name |




## LinkML Source

<details>
```yaml
name: first_name
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: first_name
owner: PersonValue
domain_of:
- PersonValue
range: string
required: true

```
</details>