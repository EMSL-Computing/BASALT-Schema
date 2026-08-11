

# Slot: methane (methane) 


_Methane (gas) amount or concentration at the time of sampling. (Unit: umol/L or ppb or ppm)_





URI: [basalt_schema:methane](https://w3id.org/MONet/basalt-schema/methane)
Alias: methane

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AerosolArmSample](AerosolArmSample.md), [AerosolSample](AerosolSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*(umol/L|ppm|ppb)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:methane |
| native | basalt_schema:methane |




## LinkML Source

<details>
```yaml
name: methane
description: 'Methane (gas) amount or concentration at the time of sampling. (Unit:
  umol/L or ppb or ppm)'
title: methane
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: methane
domain_of:
- AerosolArmSample
- AerosolSample
- OtherUndescribedSample
- SedimentSample
range: string
pattern: ^\d+(\.\d+)?\s*(umol/L|ppm|ppb)$

```
</details>