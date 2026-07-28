

# Slot: setup_date 


_When the plate was physically set up_





URI: [analysis_api_schema:setup_date](https://w3id.org/MONet/analysis-api-schema/setup_date)
Alias: setup_date

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlateSetupActivity](PlateSetupActivity.md) | Abstract base for 96-well plate setup activities |  no  |
| [AMP2PlateSetupActivity](AMP2PlateSetupActivity.md) | AMP2-specific plate setup |  no  |
| [EcoplatePlateSetupActivity](EcoplatePlateSetupActivity.md) | Ecoplate-specific plate setup |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [PlateSetupActivity](PlateSetupActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:setup_date |
| native | analysis_api_schema:setup_date |




## LinkML Source

<details>
```yaml
name: setup_date
description: When the plate was physically set up
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: setup_date
domain_of:
- PlateSetupActivity
range: datetime
required: true

```
</details>