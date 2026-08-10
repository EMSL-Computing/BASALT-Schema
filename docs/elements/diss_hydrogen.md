

# Slot: dissolved hydrogen (diss_hydrogen) 


_Concentration of dissolved hydrogens (Unit: umol/L)_





URI: [basalt_schema:diss_hydrogen](https://w3id.org/MONet/basalt-schema/diss_hydrogen)
Alias: diss_hydrogen

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
| Regex Pattern | `^\d+(\.\d+)?\s*umol/L$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:diss_hydrogen |
| native | basalt_schema:diss_hydrogen |




## LinkML Source

<details>
```yaml
name: diss_hydrogen
description: 'Concentration of dissolved hydrogens (Unit: umol/L)'
title: dissolved hydrogen
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: diss_hydrogen
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*umol/L$

```
</details>