

# Slot: host specificity or range (host_spec_range) 


_The range and diversity of host species that an organism is capable of infecting, defined by NCBI taxonomy identifier. Format with prefix NCBITaxon:####_





URI: [analysis_api_schema:host_spec_range](https://w3id.org/MONet/analysis-api-schema/host_spec_range)
Alias: host_spec_range

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  no  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [BiologicalEntity](BiologicalEntity.md) | Reference data representing a biological identity (strain, isolate, |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `NCBITaxon:\d+`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:host_spec_range |
| native | analysis_api_schema:host_spec_range |




## LinkML Source

<details>
```yaml
name: host_spec_range
description: The range and diversity of host species that an organism is capable of
  infecting, defined by NCBI taxonomy identifier. Format with prefix NCBITaxon:####
title: host specificity or range
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: host_spec_range
domain_of:
- CultureEnvironmentalSample
- FieldDeployedTerraformSample
- MixedCultureSample
- OtherUndescribedSample
- PureCultureSample
- TerraformSample
- biological_entity
range: string
pattern: NCBITaxon:\d+

```
</details>