

# Slot: second cloud base height (second_cbh) 


_Second cloud base (meters) or highest received signal in vertical visibility (meters) (-999 if no cloud base or vertical visibility) (Unit: m)_





URI: [basalt_schema:second_cbh](https://w3id.org/MONet/basalt-schema/second_cbh)
Alias: second_cbh

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [AerosolArmSample](AerosolArmSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:second_cbh |
| native | basalt_schema:second_cbh |




## LinkML Source

<details>
```yaml
name: second_cbh
description: 'Second cloud base (meters) or highest received signal in vertical visibility
  (meters) (-999 if no cloud base or vertical visibility) (Unit: m)'
title: second cloud base height
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: second_cbh
domain_of:
- AerosolArmSample
range: float

```
</details>