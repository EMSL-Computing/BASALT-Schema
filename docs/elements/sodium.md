

# Slot: sodium (sodium) 


_Sodium concentration in the sample (Unit: ug/mL)_





URI: [basalt_schema:sodium](https://EMSL-Computing.github.io/BASALT-Schema/sodium)
Alias: sodium

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
| Regex Pattern | `^\d+(\.\d+)?\s*ug/mL$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:sodium |
| native | basalt_schema:sodium |




## LinkML Source

<details>
```yaml
name: sodium
description: 'Sodium concentration in the sample (Unit: ug/mL)'
title: sodium
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: sodium
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*ug/mL$

```
</details>