

# Slot: synthetic environment start date (synth_start_date) 


_Provide the date the sample was transferred to the synthetic environment. Formatted as YYYY-MM-DD_





URI: [basalt_schema:synth_start_date](https://emsl-computing.github.io/BASALT-Schema/elements/synth_start_date)
Alias: synth_start_date

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  yes  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [TerraformSample](TerraformSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:synth_start_date |
| native | basalt_schema:synth_start_date |




## LinkML Source

<details>
```yaml
name: synth_start_date
description: Provide the date the sample was transferred to the synthetic environment.
  Formatted as YYYY-MM-DD
title: synthetic environment start date
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: synth_start_date
domain_of:
- FieldDeployedTerraformSample
- TerraformSample
range: string
pattern: ^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$

```
</details>