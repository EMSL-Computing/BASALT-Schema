

# Slot: setup_operator_id 


_Person who set up the plate_





URI: [analysis_api_schema:setup_operator_id](https://w3id.org/MONet/analysis-api-schema/setup_operator_id)
Alias: setup_operator_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EcoplatePlateSetupActivity](EcoplatePlateSetupActivity.md) | Ecoplate-specific plate setup |  no  |
| [AMP2PlateSetupActivity](AMP2PlateSetupActivity.md) | AMP2-specific plate setup |  no  |
| [PlateSetupActivity](PlateSetupActivity.md) | Abstract base for 96-well plate setup activities |  no  |







## Properties

* Range: [PersonValue](PersonValue.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:setup_operator_id |
| native | analysis_api_schema:setup_operator_id |




## LinkML Source

<details>
```yaml
name: setup_operator_id
description: Person who set up the plate
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: setup_operator_id
domain_of:
- PlateSetupActivity
range: PersonValue

```
</details>