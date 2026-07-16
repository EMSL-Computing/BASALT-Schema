

# Slot: depth (depth) 


_The vertical distance below local surface. For sediment or soil samples, depth is measured from sediment or soil surface respectively. Depth is required to be reported as an interval for subsurface samples. (Units: m)_





URI: [analysis_api_schema:depth](https://w3id.org/MONet/analysis-api-schema/depth)
Alias: depth

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  yes  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  yes  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  yes  |
| [MonetSoilSample](MonetSoilSample.md) | A soil sample that has been collected according to the MONet soil sampling pr... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [MonetSoilSample](MonetSoilSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?(-\d+(\.\d+)?)?\s*m$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:depth |
| native | analysis_api_schema:depth |




## LinkML Source

<details>
```yaml
name: depth
description: 'The vertical distance below local surface. For sediment or soil samples,
  depth is measured from sediment or soil surface respectively. Depth is required
  to be reported as an interval for subsurface samples. (Units: m)'
title: depth
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: depth
domain_of:
- FieldDeployedTerraformSample
- MonetSoilSample
- OtherUndescribedSample
- SedimentSample
- SoilSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?(-\d+(\.\d+)?)?\s*m$

```
</details>