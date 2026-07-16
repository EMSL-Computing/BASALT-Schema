

# Slot: carbon dioxide (carb_dioxide) 


_Amount of carbon dioxide measured in the air the day of sampling. (Unit: umol/L or ppm)_





URI: [analysis_api_schema:carb_dioxide](https://w3id.org/MONet/analysis-api-schema/carb_dioxide)
Alias: carb_dioxide

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  yes  |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AerosolArmSample](AerosolArmSample.md), [AerosolSample](AerosolSample.md), [OtherUndescribedSample](OtherUndescribedSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*(umol/L|ppm)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:carb_dioxide |
| native | analysis_api_schema:carb_dioxide |




## LinkML Source

<details>
```yaml
name: carb_dioxide
description: 'Amount of carbon dioxide measured in the air the day of sampling. (Unit:
  umol/L or ppm)'
title: carbon dioxide
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: carb_dioxide
domain_of:
- AerosolArmSample
- AerosolSample
- OtherUndescribedSample
range: string
pattern: ^\d+(\.\d+)?\s*(umol/L|ppm)$

```
</details>