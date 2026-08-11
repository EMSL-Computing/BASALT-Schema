

# Slot: pressure control (pressure_control) 


_Measurment of pressure applied to the sample during experimentation (Unit: Pa)_





URI: [basalt_schema:pressure_control](https://w3id.org/MONet/basalt-schema/pressure_control)
Alias: pressure_control

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






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
| Regex Pattern | `^\d+(\.\d+)?\s*Pa$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:pressure_control |
| native | basalt_schema:pressure_control |




## LinkML Source

<details>
```yaml
name: pressure_control
description: 'Measurment of pressure applied to the sample during experimentation
  (Unit: Pa)'
title: pressure control
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: pressure_control
domain_of:
- AerosolArmSample
- AerosolSample
- OtherUndescribedSample
range: string
pattern: ^\d+(\.\d+)?\s*Pa$

```
</details>