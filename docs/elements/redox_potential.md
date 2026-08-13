

# Slot: redox potential (redox_potential) 


_Redox potential measured relative to a hydrogen cell indicating oxidation or reduction potential (Unit: mV)_





URI: [basalt_schema:redox_potential](https://EMSL-Computing.github.io/BASALT-Schema/redox_potential)
Alias: redox_potential

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md), [TerraformSample](TerraformSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*mV$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:redox_potential |
| native | basalt_schema:redox_potential |




## LinkML Source

<details>
```yaml
name: redox_potential
description: 'Redox potential measured relative to a hydrogen cell indicating oxidation
  or reduction potential (Unit: mV)'
title: redox potential
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: redox_potential
domain_of:
- FieldDeployedTerraformSample
- OtherUndescribedSample
- SedimentSample
- TerraformSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*mV$

```
</details>