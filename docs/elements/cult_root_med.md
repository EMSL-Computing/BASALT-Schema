

# Slot: culture rooting medium (cult_root_med) 


_Name or reference for the hydroponic or in vitro culture rooting medium; can be the name of a commonly used medium or reference to a specific medium, e.g. Murashige and Skoog medium. If the medium has not been formally published use the rooting medium descriptors._





URI: [basalt_schema:cult_root_med](https://emsl-computing.github.io/BASALT-Schema/elements/cult_root_med)
Alias: cult_root_med

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [TerraformSample](TerraformSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:cult_root_med |
| native | basalt_schema:cult_root_med |




## LinkML Source

<details>
```yaml
name: cult_root_med
description: Name or reference for the hydroponic or in vitro culture rooting medium;
  can be the name of a commonly used medium or reference to a specific medium, e.g.
  Murashige and Skoog medium. If the medium has not been formally published use the
  rooting medium descriptors.
title: culture rooting medium
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: cult_root_med
domain_of:
- FieldDeployedTerraformSample
- TerraformSample
range: string

```
</details>