

# Slot: sulfate (sulfate) 


_Concentration of sulfate in the sample. (Unit: umol/L or mg/L or ppm)_





URI: [basalt_schema:sulfate](https://EMSL-Computing.github.io/BASALT-Schema/sulfate)
Alias: sulfate

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
| Regex Pattern | `^\d+(\.\d+)?\s*(umol/L|mg/L|ppm)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:sulfate |
| native | basalt_schema:sulfate |




## LinkML Source

<details>
```yaml
name: sulfate
description: 'Concentration of sulfate in the sample. (Unit: umol/L or mg/L or ppm)'
title: sulfate
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: sulfate
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(umol/L|mg/L|ppm)$

```
</details>