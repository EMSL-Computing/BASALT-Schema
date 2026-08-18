

# Slot: carbon dioxide (carb_dioxide) 


_Amount of carbon dioxide measured in the air the day of sampling. (Unit: umol/L or ppm)_





URI: [basalt_schema:carb_dioxide](https://emsl-computing.github.io/BASALT-Schema/elements/carb_dioxide)
Alias: carb_dioxide

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  yes  |
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


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:carb_dioxide |
| native | basalt_schema:carb_dioxide |




## LinkML Source

<details>
```yaml
name: carb_dioxide
description: 'Amount of carbon dioxide measured in the air the day of sampling. (Unit:
  umol/L or ppm)'
title: carbon dioxide
from_schema: https://emsl-computing.github.io/BASALT-Schema
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