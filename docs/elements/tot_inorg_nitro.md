

# Slot: total inorganic nitrogen (tot_inorg_nitro) 


_Total inorganic nitrogen content. (Unit: ug/L)_





URI: [analysis_api_schema:tot_inorg_nitro](https://w3id.org/MONet/analysis-api-schema/tot_inorg_nitro)
Alias: tot_inorg_nitro

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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:tot_inorg_nitro |
| native | analysis_api_schema:tot_inorg_nitro |




## LinkML Source

<details>
```yaml
name: tot_inorg_nitro
description: 'Total inorganic nitrogen content. (Unit: ug/L)'
title: total inorganic nitrogen
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: tot_inorg_nitro
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(ug/L)$

```
</details>