

# Slot: local environmental context (env_local_scale) 


_'Report the entity which are in your sample or specimens local vicinity and which you believe have significant causal influences on your sample or specimen. Please use terms that are present in ENVO and which are of smaller spatial grain than your entry for env_broad_scale.If needed, request new terms on the ENVO tracker identified here: http://www.obofoundry.org/ontology/envo.html'_





URI: [analysis_api_schema:env_local_scale](https://w3id.org/MONet/analysis-api-schema/env_local_scale)
Alias: env_local_scale

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |
| [MonetSoilSample](MonetSoilSample.md) | A soil sample that has been collected according to the MONet soil sampling pr... |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^_*\s*[a-zA-Z\s]+\[ENVO:\d+\]$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:env_local_scale |
| native | analysis_api_schema:env_local_scale |




## LinkML Source

<details>
```yaml
name: env_local_scale
description: '''Report the entity which are in your sample or specimens local vicinity
  and which you believe have significant causal influences on your sample or specimen.
  Please use terms that are present in ENVO and which are of smaller spatial grain
  than your entry for env_broad_scale.If needed, request new terms on the ENVO tracker
  identified here: http://www.obofoundry.org/ontology/envo.html'''
title: local environmental context
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: env_local_scale
domain_of:
- AerosolArmSample
- AerosolSample
- CultureEnvironmentalSample
- FieldDeployedTerraformSample
- MonetSoilSample
- OtherUndescribedSample
- PlantSample
- PureCultureSample
- SedimentSample
- SoilSample
- TerraformSample
- WaterSample
range: string
pattern: ^_*\s*[a-zA-Z\s]+\[ENVO:\d+\]$

```
</details>