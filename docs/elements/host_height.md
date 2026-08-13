

# Slot: host height (host_height) 


_The height of subject. (Unit: cm or mm or m)_





URI: [basalt_schema:host_height](https://EMSL-Computing.github.io/basalt-schema/host_height)
Alias: host_height

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  yes  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [PlantSample](PlantSample.md), [TerraformSample](TerraformSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*(cm|mm|m)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:host_height |
| native | basalt_schema:host_height |




## LinkML Source

<details>
```yaml
name: host_height
description: 'The height of subject. (Unit: cm or mm or m)'
title: host height
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: host_height
domain_of:
- FieldDeployedTerraformSample
- OtherUndescribedSample
- PlantSample
- TerraformSample
range: string
pattern: ^\d+(\.\d+)?\s*(cm|mm|m)$

```
</details>