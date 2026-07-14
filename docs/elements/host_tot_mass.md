

# Slot: host total mass (host_tot_mass) 


_Total mass of the host at collection. (Unit: kg or g)_





URI: [analysis_api_schema:host_tot_mass](https://w3id.org/MONet/analysis-api-schema/host_tot_mass)
Alias: host_tot_mass

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
| self | analysis_api_schema:host_tot_mass |
| native | analysis_api_schema:host_tot_mass |




## LinkML Source

<details>
```yaml
name: host_tot_mass
description: 'Total mass of the host at collection. (Unit: kg or g)'
title: host total mass
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: host_tot_mass
domain_of:
- FieldDeployedTerraformSample
- OtherUndescribedSample
- TerraformSample
range: string
pattern: ^\d+(\.\d+)?\s*(kg|g)$

```
</details>