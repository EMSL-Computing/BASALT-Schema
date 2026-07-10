

# Slot: replicate 


_The replicate number of the sample or measurement, if applicable._





URI: [analysis_api_schema:replicate](https://w3id.org/MONet/analysis-api-schema/replicate)
Alias: replicate

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProcessedSample](ProcessedSample.md) | A sample that has undergone processing or analysis |  yes  |
| [NitrogenAnalysisProduct](NitrogenAnalysisProduct.md) |  |  no  |
| [MAOMProduct](MAOMProduct.md) |  |  no  |
| [WEOMProduct](WEOMProduct.md) |  |  no  |
| [CoreSection](CoreSection.md) | A section of a core sample (TOP, MID, BTM) |  no  |
| [PhosphorusAnalysisProduct](PhosphorusAnalysisProduct.md) |  |  no  |
| [MicrobialBiomassProduct](MicrobialBiomassProduct.md) |  |  no  |







## Properties

* Range: [Integer](Integer.md)





## TODOs

* reconcile replicate modelling

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:replicate |
| native | analysis_api_schema:replicate |




## LinkML Source

<details>
```yaml
name: replicate
description: The replicate number of the sample or measurement, if applicable.
todos:
- reconcile replicate modelling
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: replicate
domain_of:
- MAOMProduct
- MicrobialBiomassProduct
- NitrogenAnalysisProduct
- PhosphorusAnalysisProduct
- WEOMProduct
- ProcessedSample
range: integer

```
</details>