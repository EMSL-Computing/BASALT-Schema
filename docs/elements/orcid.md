

# Slot: orcid 


_ORCID identifier of the person_





URI: [basalt_schema:orcid](https://emsl-computing.github.io/BASALT-Schema/elements/orcid)
Alias: orcid

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
| self | basalt_schema:orcid |
| native | basalt_schema:orcid |




## LinkML Source

<details>
```yaml
name: orcid
description: ORCID identifier of the person
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: orcid
owner: PersonValue
domain_of:
- PersonValue
range: string

```
</details>