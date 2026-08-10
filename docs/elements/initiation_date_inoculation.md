

# Slot: initiation date of inoculation (initiation_date_inoculation) 


_The date the sample was inoculated. This can be the date of inoculation, isolation, etc. If providing a sequential initiation, the sample should be linked to the sample it originated from. Formatted as YYYY-MM-DD_





URI: [basalt_schema:initiation_date_inoculation](https://w3id.org/MONet/basalt-schema/initiation_date_inoculation)
Alias: initiation_date_inoculation

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


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:initiation_date_inoculation |
| native | basalt_schema:initiation_date_inoculation |




## LinkML Source

<details>
```yaml
name: initiation_date_inoculation
description: The date the sample was inoculated. This can be the date of inoculation,
  isolation, etc. If providing a sequential initiation, the sample should be linked
  to the sample it originated from. Formatted as YYYY-MM-DD
title: initiation date of inoculation
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: initiation_date_inoculation
domain_of:
- FieldDeployedTerraformSample
- TerraformSample
range: string
pattern: ^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$

```
</details>