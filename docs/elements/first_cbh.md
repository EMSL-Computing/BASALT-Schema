

# Slot: first cloud base height (first_cbh) 


_First cloud base (meters) or vertical visibility (meters) (-999 if no cloud base or vertical visibility) (Unit: m)_





URI: [basalt_schema:first_cbh](https://emsl-computing.github.io/BASALT-Schema/elements/first_cbh)
Alias: first_cbh

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


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:first_cbh |
| native | basalt_schema:first_cbh |




## LinkML Source

<details>
```yaml
name: first_cbh
description: 'First cloud base (meters) or vertical visibility (meters) (-999 if no
  cloud base or vertical visibility) (Unit: m)'
title: first cloud base height
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: first_cbh
domain_of:
- AerosolArmSample
range: float

```
</details>