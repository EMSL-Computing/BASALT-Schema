

# Slot: turbidity (turbidity) 


_Measure of the amount of cloudiness or haziness in water caused by individual particles. Provide value and unit any unit is valid._





URI: [analysis_api_schema:turbidity](https://w3id.org/MONet/analysis-api-schema/turbidity)
Alias: turbidity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*[\w\s/]+$`





## TODOs

* decide how to represent in backend (normalized child table with FK to PlateSetupActivity, array column, or other)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:turbidity |
| native | analysis_api_schema:turbidity |




## LinkML Source

<details>
```yaml
name: turbidity
description: Measure of the amount of cloudiness or haziness in water caused by individual
  particles. Provide value and unit any unit is valid.
title: turbidity
todos:
- decide how to represent in backend (normalized child table with FK to PlateSetupActivity,
  array column, or other)
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: turbidity
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>