

# Slot: host age (host_age) 


_Age of host at the time of sampling; relevant scale depends on species and study, e.g. Could be seconds for amoebae or centuries for trees. (Unit: a (year) or d (day) or h (hour). Do not include the additional information in ().)_





URI: [analysis_api_schema:host_age](https://w3id.org/MONet/analysis-api-schema/host_age)
Alias: host_age

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |






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
| Regex Pattern | `^\d+(\.\d+)?\s*(a|d|h)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:host_age |
| native | analysis_api_schema:host_age |




## LinkML Source

<details>
```yaml
name: host_age
description: 'Age of host at the time of sampling; relevant scale depends on species
  and study, e.g. Could be seconds for amoebae or centuries for trees. (Unit: a (year)
  or d (day) or h (hour). Do not include the additional information in ().)'
title: host age
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: host_age
domain_of:
- FieldDeployedTerraformSample
- OtherUndescribedSample
- TerraformSample
range: string
pattern: ^\d+(\.\d+)?\s*(a|d|h)$

```
</details>