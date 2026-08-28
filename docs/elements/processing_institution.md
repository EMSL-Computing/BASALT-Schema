

# Slot: processing_institution 


_The institution where the activity took place._





URI: [basalt_schema:processing_institution](https://emsl-computing.github.io/BASALT-Schema/elements/processing_institution)
Alias: processing_institution

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Activity](Activity.md) | Something that happens over time and can use equipment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [InstitutionEnum](InstitutionEnum.md) |
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


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:processing_institution |
| native | basalt_schema:processing_institution |




## LinkML Source

<details>
```yaml
name: processing_institution
description: The institution where the activity took place.
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: processing_institution
owner: Activity
domain_of:
- Activity
range: InstitutionEnum

```
</details>