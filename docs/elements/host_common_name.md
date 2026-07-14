

# Slot: host common name (host_common_name) 


_Common name for the host organism (e.g., "Pseudomonas putida")._

_For microbes, this may be identical to organism_name._





URI: [analysis_api_schema:host_common_name](https://w3id.org/MONet/analysis-api-schema/host_common_name)
Alias: host_common_name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [BiologicalEntity](BiologicalEntity.md) | Reference data representing a biological identity (strain, isolate, |  no  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  yes  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  yes  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  yes  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |







## Properties

* Range: [String](String.md)



## Aliases


* common_name



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:host_common_name |
| native | analysis_api_schema:host_common_name |




## LinkML Source

<details>
```yaml
name: host_common_name
description: 'Common name for the host organism (e.g., "Pseudomonas putida").

  For microbes, this may be identical to organism_name.'
title: host common name
from_schema: https://w3id.org/MONet/analysis-api-schema
aliases:
- common_name
rank: 1000
alias: host_common_name
domain_of:
- CultureEnvironmentalSample
- FieldDeployedTerraformSample
- MixedCultureSample
- OtherUndescribedSample
- PureCultureSample
- TerraformSample
- biological_entity
range: string

```
</details>