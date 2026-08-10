

# Slot: water content (water_content) 


_Water content measurement. Provide value and unit any unit is valid_





URI: [basalt_schema:water_content](https://w3id.org/MONet/basalt-schema/water_content)
Alias: water_content

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [MonetSoilSample](MonetSoilSample.md) | A soil sample that has been collected according to the MONet soil sampling pr... |  yes  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [MonetSoilSample](MonetSoilSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md), [TerraformSample](TerraformSample.md) |

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
| self | basalt_schema:water_content |
| native | basalt_schema:water_content |




## LinkML Source

<details>
```yaml
name: water_content
description: Water content measurement. Provide value and unit any unit is valid
title: water content
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: water_content
domain_of:
- FieldDeployedTerraformSample
- MonetSoilSample
- OtherUndescribedSample
- SedimentSample
- SoilSample
- TerraformSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>