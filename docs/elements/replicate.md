

# Slot: replicate 


_The replicate number of the sample or measurement, if applicable._





URI: [analysis_api_schema:replicate](https://w3id.org/MONet/analysis-api-schema/replicate)
Alias: replicate

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NitrogenAnalysisProduct](NitrogenAnalysisProduct.md) | Nitrogen analysis product, typically derived via colorimetric assay of soil e... |  no  |
| [MAOMProduct](MAOMProduct.md) | Mineral-Associated Organic Matter (MAOM) analysis product, typically derived ... |  no  |
| [WEOMProduct](WEOMProduct.md) | Water Extractable Organic Matter (WEOM) analysis product, typically derived v... |  no  |
| [CoreSection](CoreSection.md) | A section of a core sample (TOP, MID, BTM) |  no  |
| [ProcessedSample](ProcessedSample.md) | A sample that has undergone processing or analysis |  yes  |
| [PhosphorusAnalysisProduct](PhosphorusAnalysisProduct.md) | Phosphorus analysis product, typically derived via colorimetric assay of soil... |  no  |
| [MicrobialBiomassProduct](MicrobialBiomassProduct.md) | Microbial biomass analysis product, typically derived via chloroform fumigati... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [MAOMProduct](MAOMProduct.md), [MicrobialBiomassProduct](MicrobialBiomassProduct.md), [NitrogenAnalysisProduct](NitrogenAnalysisProduct.md), [PhosphorusAnalysisProduct](PhosphorusAnalysisProduct.md), [WEOMProduct](WEOMProduct.md), [ProcessedSample](ProcessedSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |








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