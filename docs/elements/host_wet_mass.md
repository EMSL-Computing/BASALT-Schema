

# Slot: host wet mass (host_wet_mass) 


_Measurement of wet mass. (Unit: kg or g)_





URI: [analysis_api_schema:host_wet_mass](https://w3id.org/MONet/analysis-api-schema/host_wet_mass)
Alias: host_wet_mass

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [TerraformSample](TerraformSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*(kg|g)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:host_wet_mass |
| native | analysis_api_schema:host_wet_mass |




## LinkML Source

<details>
```yaml
name: host_wet_mass
description: 'Measurement of wet mass. (Unit: kg or g)'
title: host wet mass
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: host_wet_mass
domain_of:
- FieldDeployedTerraformSample
- OtherUndescribedSample
- TerraformSample
range: string
pattern: ^\d+(\.\d+)?\s*(kg|g)$

```
</details>