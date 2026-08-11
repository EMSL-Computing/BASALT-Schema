

# Slot: protocol_link 


_A link to a protocol that describes the steps and parameters of the activity._





URI: [basalt_schema:protocol_link](https://EMSL-Computing.github.io/basalt-schema/protocol_link)
Alias: protocol_link

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Activity](Activity.md) | Something that happens over time and can use equipment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Activity](Activity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Activity](Activity.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:protocol_link |
| native | basalt_schema:protocol_link |




## LinkML Source

<details>
```yaml
name: protocol_link
description: A link to a protocol that describes the steps and parameters of the activity.
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: protocol_link
owner: Activity
domain_of:
- Activity
range: string

```
</details>