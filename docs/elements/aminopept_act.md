

# Slot: aminopeptidase activity (aminopept_act) 


_Measurement of aminopeptidase activity (Unit: mol/L/h)_





URI: [basalt_schema:aminopept_act](https://EMSL-Computing.github.io/basalt-schema/aminopept_act)
Alias: aminopept_act

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






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


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:aminopept_act |
| native | basalt_schema:aminopept_act |




## LinkML Source

<details>
```yaml
name: aminopept_act
description: 'Measurement of aminopeptidase activity (Unit: mol/L/h)'
title: aminopeptidase activity
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: aminopept_act
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*mol/L/h$

```
</details>