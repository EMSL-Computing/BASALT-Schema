

# Slot: petroleum hydrocarbon (petroleum_hydrocarb) 


_Concentration of petroleum hydrocarbon (Unit: umol/L)_





URI: [basalt_schema:petroleum_hydrocarb](https://EMSL-Computing.github.io/BASALT-Schema/petroleum_hydrocarb)
Alias: petroleum_hydrocarb

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |






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
| Regex Pattern | `^\d+(\.\d+)?\s*umol/L$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:petroleum_hydrocarb |
| native | basalt_schema:petroleum_hydrocarb |




## LinkML Source

<details>
```yaml
name: petroleum_hydrocarb
description: 'Concentration of petroleum hydrocarbon (Unit: umol/L)'
title: petroleum hydrocarbon
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: petroleum_hydrocarb
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*umol/L$

```
</details>