

# Slot: organic matter (org_matter) 


_Concentration of organic matter (Unit: mg/L)_





URI: [basalt_schema:org_matter](https://w3id.org/MONet/basalt-schema/org_matter)
Alias: org_matter

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
| Regex Pattern | `^\d+(\.\d+)?\s*mg/L$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:org_matter |
| native | basalt_schema:org_matter |




## LinkML Source

<details>
```yaml
name: org_matter
description: 'Concentration of organic matter (Unit: mg/L)'
title: organic matter
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: org_matter
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*mg/L$

```
</details>