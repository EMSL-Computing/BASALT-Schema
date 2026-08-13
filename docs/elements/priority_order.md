

# Slot: priority order (priority_order) 


_Indicate the run order priority of your samples_





URI: [basalt_schema:priority_order](https://EMSL-Computing.github.io/basalt-schema/priority_order)
Alias: priority_order

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [AerosolArmSample](AerosolArmSample.md), [AerosolSample](AerosolSample.md), [OtherUndescribedSample](OtherUndescribedSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:priority_order |
| native | basalt_schema:priority_order |




## LinkML Source

<details>
```yaml
name: priority_order
description: Indicate the run order priority of your samples
title: priority order
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: priority_order
domain_of:
- AerosolArmSample
- AerosolSample
- OtherUndescribedSample
range: float

```
</details>