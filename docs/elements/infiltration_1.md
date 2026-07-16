

# Slot: first infiltration time (infiltration_1) 


_Amount of time it takes to accomplish the first infiltration activity. If infiltration time was started and unsuccessful enter 'failed' if infiltration time was not attempted enter 'did not collect'. Units and format of mm:ss required. (Example: 15:20 mm:ss)_





URI: [analysis_api_schema:infiltration_1](https://w3id.org/MONet/analysis-api-schema/infiltration_1)
Alias: infiltration_1

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilSamplingActivity](SoilSamplingActivity.md) | Collection of soil samples from the environment |  no  |
| [MonetSoilSamplingActivity](MonetSoilSamplingActivity.md) | Collection of soil cores according to the MONet soil sampling protocol |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MonetSoilSamplingActivity](MonetSoilSamplingActivity.md), [SoilSamplingActivity](SoilSamplingActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^((0[0-9]|[1-5][0-9]):([0-5][0-9])\smm:ss|did not collect|failed)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:infiltration_1 |
| native | analysis_api_schema:infiltration_1 |




## LinkML Source

<details>
```yaml
name: infiltration_1
description: 'Amount of time it takes to accomplish the first infiltration activity.
  If infiltration time was started and unsuccessful enter ''failed'' if infiltration
  time was not attempted enter ''did not collect''. Units and format of mm:ss required.
  (Example: 15:20 mm:ss)'
title: first infiltration time
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: infiltration_1
domain_of:
- MonetSoilSamplingActivity
- SoilSamplingActivity
range: string
pattern: ^((0[0-9]|[1-5][0-9]):([0-5][0-9])\smm:ss|did not collect|failed)$

```
</details>