

# Slot: tissue culture growth media (tiss_cult_growth_med) 


_Description of plant tissue culture growth media used_





URI: [basalt_schema:tiss_cult_growth_med](https://emsl-computing.github.io/BASALT-Schema/elements/tiss_cult_growth_med)
Alias: tiss_cult_growth_med

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
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










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:tiss_cult_growth_med |
| native | basalt_schema:tiss_cult_growth_med |




## LinkML Source

<details>
```yaml
name: tiss_cult_growth_med
description: Description of plant tissue culture growth media used
title: tissue culture growth media
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: tiss_cult_growth_med
domain_of:
- FieldDeployedTerraformSample
- OtherUndescribedSample
- TerraformSample
range: string

```
</details>