

# Slot: CAS number (cas) 


_A unique numerical identifier assigned by the Chemical Abstract Service (CAS), a division of the American Chemical Society, to chemical compounds, polymers, biological sequences, mixtures, and alloys._





URI: [analysis_api_schema:cas](https://w3id.org/MONet/analysis-api-schema/cas)
Alias: cas

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SynthesizedMaterialSample](SynthesizedMaterialSample.md) | A sample containing synthetically generated material |  no  |
| [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md) | A sample containing commercially purchased material |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |







## Properties

* Range: [String](String.md)



## Aliases


* CAS



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:cas |
| native | analysis_api_schema:cas |




## LinkML Source

<details>
```yaml
name: cas
description: A unique numerical identifier assigned by the Chemical Abstract Service
  (CAS), a division of the American Chemical Society, to chemical compounds, polymers,
  biological sequences, mixtures, and alloys.
title: CAS number
from_schema: https://w3id.org/MONet/analysis-api-schema
aliases:
- CAS
rank: 1000
alias: cas
domain_of:
- CommerciallyPurchasedSample
- OtherUndescribedSample
- SynthesizedMaterialSample
range: string

```
</details>