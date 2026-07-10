

# Slot: production method (production_method) 


_A DOI or description of how the compound was produced, if the commercially purchased material was altered_





URI: [analysis_api_schema:production_method](https://w3id.org/MONet/analysis-api-schema/production_method)
Alias: production_method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SynthesizedMaterialSample](SynthesizedMaterialSample.md) | A sample containing synthetically generated material |  no  |
| [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md) | A sample containing commercially purchased material |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:production_method |
| native | analysis_api_schema:production_method |




## LinkML Source

<details>
```yaml
name: production_method
description: A DOI or description of how the compound was produced, if the commercially
  purchased material was altered
title: production method
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: production_method
domain_of:
- CommerciallyPurchasedSample
- OtherUndescribedSample
- SynthesizedMaterialSample
range: string

```
</details>