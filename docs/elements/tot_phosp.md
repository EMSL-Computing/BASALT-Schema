

# Slot: total phosphorus (tot_phosp) 


_Total phosphorus concentration in the sample calculated by: total phosphorus = total dissolved phosphorus + particulate phosphorus. (Unit: ug/L or umol/L)_





URI: [basalt_schema:tot_phosp](https://EMSL-Computing.github.io/basalt-schema/tot_phosp)
Alias: tot_phosp

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*(ug/L|umol/L)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:tot_phosp |
| native | basalt_schema:tot_phosp |




## LinkML Source

<details>
```yaml
name: tot_phosp
description: 'Total phosphorus concentration in the sample calculated by: total phosphorus
  = total dissolved phosphorus + particulate phosphorus. (Unit: ug/L or umol/L)'
title: total phosphorus
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: tot_phosp
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(ug/L|umol/L)$

```
</details>