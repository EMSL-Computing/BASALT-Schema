

# Slot: porosity (porosity) 


_Porosity of deposited sediment is volume of voids divided by the total volume of sample. (Unit: percent)_





URI: [basalt_schema:porosity](https://EMSL-Computing.github.io/BASALT-Schema/porosity)
Alias: porosity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*percent$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:porosity |
| native | basalt_schema:porosity |




## LinkML Source

<details>
```yaml
name: porosity
description: 'Porosity of deposited sediment is volume of voids divided by the total
  volume of sample. (Unit: percent)'
title: porosity
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: porosity
domain_of:
- OtherUndescribedSample
- SedimentSample
range: string
pattern: ^\d+(\.\d+)?\s*percent$

```
</details>