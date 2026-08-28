

# Slot: total dissolved nitrogen (tot_diss_nitro) 


_Total dissolved nitrogen concentration reported as nitrogen measured by: total dissolved nitrogen = NH4 + NO3NO2 + dissolved organic nitrogen. (Unit: ug/L)_





URI: [basalt_schema:tot_diss_nitro](https://emsl-computing.github.io/BASALT-Schema/elements/tot_diss_nitro)
Alias: tot_diss_nitro

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |






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
| Regex Pattern | `^\d+(\.\d+)?\s*(ug/L)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:tot_diss_nitro |
| native | basalt_schema:tot_diss_nitro |




## LinkML Source

<details>
```yaml
name: tot_diss_nitro
description: 'Total dissolved nitrogen concentration reported as nitrogen measured
  by: total dissolved nitrogen = NH4 + NO3NO2 + dissolved organic nitrogen. (Unit:
  ug/L)'
title: total dissolved nitrogen
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: tot_diss_nitro
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(ug/L)$

```
</details>