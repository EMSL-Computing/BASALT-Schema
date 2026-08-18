

# Slot: last_name 



URI: [basalt_schema:last_name](https://emsl-computing.github.io/BASALT-Schema/elements/last_name)
Alias: last_name

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


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:last_name |
| native | basalt_schema:last_name |




## LinkML Source

<details>
```yaml
name: last_name
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: last_name
owner: PersonValue
domain_of:
- PersonValue
range: string
required: true

```
</details>