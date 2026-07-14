

# Slot: host dry mass (host_dry_mass) 


_Measurement of dry mass. (Unit: kg or g)_





URI: [analysis_api_schema:host_dry_mass](https://w3id.org/MONet/analysis-api-schema/host_dry_mass)
Alias: host_dry_mass

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*(kg|g)$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:host_dry_mass |
| native | analysis_api_schema:host_dry_mass |




## LinkML Source

<details>
```yaml
name: host_dry_mass
description: 'Measurement of dry mass. (Unit: kg or g)'
title: host dry mass
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: host_dry_mass
domain_of:
- FieldDeployedTerraformSample
- OtherUndescribedSample
- TerraformSample
range: string
pattern: ^\d+(\.\d+)?\s*(kg|g)$

```
</details>