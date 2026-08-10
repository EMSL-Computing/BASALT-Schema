

# Slot: organic nitrogen (org_nitro) 


_Concentration of organic nitrogen. Provide value and unit any unit is valid_





URI: [basalt_schema:org_nitro](https://w3id.org/MONet/basalt-schema/org_nitro)
Alias: org_nitro

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
| Regex Pattern | `^\d+(\.\d+)?\s*[\w\s/]+$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:org_nitro |
| native | basalt_schema:org_nitro |




## LinkML Source

<details>
```yaml
name: org_nitro
description: Concentration of organic nitrogen. Provide value and unit any unit is
  valid
title: organic nitrogen
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: org_nitro
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>