

# Slot: ph_target 


_Target pH value (required if ph_adjustment is true)_





URI: [analysis_api_schema:ph_target](https://w3id.org/MONet/analysis-api-schema/ph_target)
Alias: ph_target

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaPreparation](MediaPreparation.md) | Activity that prepares a batch of growth media |  no  |







## Properties

* Range: [Float](Float.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:ph_target |
| native | analysis_api_schema:ph_target |




## LinkML Source

<details>
```yaml
name: ph_target
description: Target pH value (required if ph_adjustment is true)
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: ph_target
domain_of:
- MediaPreparation
range: float
required: false

```
</details>