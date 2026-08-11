

# Slot: total carbon content (tot_carb) 


_Total carbon content. Provide value and unit, any unit is valid_





URI: [basalt_schema:tot_carb](https://EMSL-Computing.github.io/basalt-schema/tot_carb)
Alias: tot_carb

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |






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
| Regex Pattern | `^\d+(\.\d+)?\s*[\w\s/]+$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:tot_carb |
| native | basalt_schema:tot_carb |




## LinkML Source

<details>
```yaml
name: tot_carb
description: Total carbon content. Provide value and unit, any unit is valid
title: total carbon content
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: tot_carb
domain_of:
- OtherUndescribedSample
- SedimentSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>