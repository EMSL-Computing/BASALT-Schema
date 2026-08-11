

# Slot: dissolved carbon dioxide (diss_carb_dioxide) 


_Concentration of dissolved carbon dioxide in the sample or liquid portion of the sample (Unit: umol/L or mg/L)_





URI: [basalt_schema:diss_carb_dioxide](https://EMSL-Computing.github.io/basalt-schema/diss_carb_dioxide)
Alias: diss_carb_dioxide

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
| Regex Pattern | `^\d+(\.\d+)?\s*(umol|mg)/L$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:diss_carb_dioxide |
| native | basalt_schema:diss_carb_dioxide |




## LinkML Source

<details>
```yaml
name: diss_carb_dioxide
description: 'Concentration of dissolved carbon dioxide in the sample or liquid portion
  of the sample (Unit: umol/L or mg/L)'
title: dissolved carbon dioxide
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: diss_carb_dioxide
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(umol|mg)/L$

```
</details>