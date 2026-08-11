

# Slot: temperature exposure (temperature_exposure) 


_The range of temperatures at which it is safe to store a label that has been applied to a substrate. Provided by iMet_





URI: [basalt_schema:temperature_exposure](https://w3id.org/MONet/basalt-schema/temperature_exposure)
Alias: temperature_exposure

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AerosolSample](AerosolSample.md), [OtherUndescribedSample](OtherUndescribedSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:temperature_exposure |
| native | basalt_schema:temperature_exposure |




## LinkML Source

<details>
```yaml
name: temperature_exposure
description: The range of temperatures at which it is safe to store a label that has
  been applied to a substrate. Provided by iMet
title: temperature exposure
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: temperature_exposure
domain_of:
- AerosolSample
- OtherUndescribedSample
range: string

```
</details>