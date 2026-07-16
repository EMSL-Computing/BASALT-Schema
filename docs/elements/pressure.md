

# Slot: pressure (pressure) 


_Pressure to which the sample is subject, in atmospheres (Unit: atm)_





URI: [analysis_api_schema:pressure](https://w3id.org/MONet/analysis-api-schema/pressure)
Alias: pressure

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [ConditioningValue](ConditioningValue.md) |  |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md), [TerraformSample](TerraformSample.md), [WaterSample](WaterSample.md), [ConditioningValue](ConditioningValue.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*atm$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:pressure |
| native | analysis_api_schema:pressure |




## LinkML Source

<details>
```yaml
name: pressure
description: 'Pressure to which the sample is subject, in atmospheres (Unit: atm)'
title: pressure
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: pressure
domain_of:
- FieldDeployedTerraformSample
- OtherUndescribedSample
- SedimentSample
- TerraformSample
- WaterSample
- ConditioningValue
range: string
pattern: ^\d+(\.\d+)?\s*atm$

```
</details>