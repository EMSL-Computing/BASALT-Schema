

# Slot: carbon monoxide (carb_monoxide) 


_Amount of carbon monoxide measured in the air the day of sampling. (Unit: umol/L or ppm)_





URI: [basalt_schema:carb_monoxide](https://w3id.org/MONet/basalt-schema/carb_monoxide)
Alias: carb_monoxide

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


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:carb_monoxide |
| native | basalt_schema:carb_monoxide |




## LinkML Source

<details>
```yaml
name: carb_monoxide
description: 'Amount of carbon monoxide measured in the air the day of sampling. (Unit:
  umol/L or ppm)'
title: carbon monoxide
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: carb_monoxide
domain_of:
- AerosolArmSample
- AerosolSample
- OtherUndescribedSample
range: string
pattern: ^\d+(\.\d+)?\s*(umol/L|ppm)$

```
</details>