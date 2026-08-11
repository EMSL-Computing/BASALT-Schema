

# Slot: total nitrogen content (tot_nitro_content) 


_Total nitrogen content of the sample. Provide value and unit any unit is valid_





URI: [basalt_schema:tot_nitro_content](https://EMSL-Computing.github.io/basalt-schema/tot_nitro_content)
Alias: tot_nitro_content

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md) |

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
| self | basalt_schema:tot_nitro_content |
| native | basalt_schema:tot_nitro_content |




## LinkML Source

<details>
```yaml
name: tot_nitro_content
description: Total nitrogen content of the sample. Provide value and unit any unit
  is valid
title: total nitrogen content
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: tot_nitro_content
domain_of:
- OtherUndescribedSample
- SedimentSample
- SoilSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>