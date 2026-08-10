

# Slot: glucosidase activity (glucosidase_act) 


_Measurement of glucosidase activity (Unit: mol/L/h)_





URI: [basalt_schema:glucosidase_act](https://w3id.org/MONet/basalt-schema/glucosidase_act)
Alias: glucosidase_act

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*mol/L/h$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:glucosidase_act |
| native | basalt_schema:glucosidase_act |




## LinkML Source

<details>
```yaml
name: glucosidase_act
description: 'Measurement of glucosidase activity (Unit: mol/L/h)'
title: glucosidase activity
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: glucosidase_act
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*mol/L/h$

```
</details>