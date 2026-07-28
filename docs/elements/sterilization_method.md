

# Slot: sterilization_method 


_Method used to sterilize the entity (autoclave, filter, UV, etc.)_





URI: [analysis_api_schema:sterilization_method](https://w3id.org/MONet/analysis-api-schema/sterilization_method)
Alias: sterilization_method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaPreparation](MediaPreparation.md) | Activity that prepares a batch of growth media |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SterilizationMethodEnum](SterilizationMethodEnum.md) |
| Domain Of | [MediaPreparation](MediaPreparation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:sterilization_method |
| native | analysis_api_schema:sterilization_method |




## LinkML Source

<details>
```yaml
name: sterilization_method
description: Method used to sterilize the entity (autoclave, filter, UV, etc.)
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: sterilization_method
domain_of:
- MediaPreparation
range: SterilizationMethodEnum
required: false

```
</details>