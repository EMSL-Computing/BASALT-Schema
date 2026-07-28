

# Slot: processing_institution 


_The institution where the activity took place._





URI: [analysis_api_schema:processing_institution](https://w3id.org/MONet/analysis-api-schema/processing_institution)
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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:processing_institution |
| native | analysis_api_schema:processing_institution |




## LinkML Source

<details>
```yaml
name: processing_institution
description: The institution where the activity took place.
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: processing_institution
owner: Activity
domain_of:
- Activity
range: InstitutionEnum

```
</details>