

# Slot: redox potential (redox_potential) 


_Redox potential measured relative to a hydrogen cell indicating oxidation or reduction potential (Unit: mV)_





URI: [analysis_api_schema:redox_potential](https://w3id.org/MONet/analysis-api-schema/redox_potential)
Alias: redox_potential

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*mV$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:redox_potential |
| native | analysis_api_schema:redox_potential |




## LinkML Source

<details>
```yaml
name: redox_potential
description: 'Redox potential measured relative to a hydrogen cell indicating oxidation
  or reduction potential (Unit: mV)'
title: redox potential
from_schema: https://w3id.org/MONet/analysis-api-schema
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