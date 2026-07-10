

# Slot: results_from_ms_processing 


_a reference to the mass spec data processing activity that produced this data product_





URI: [analysis_api_schema:results_from_ms_processing](https://w3id.org/MONet/analysis-api-schema/results_from_ms_processing)
Alias: results_from_ms_processing

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MolecularIdentificationProduct](MolecularIdentificationProduct.md) | a file containing molecular formula identifications that was output from a ma... |  no  |
| [MetaproteomicsProduct](MetaproteomicsProduct.md) | Abstract parent class for processed metaproteomics data |  no  |
| [MassSpectrometryDataProduct](MassSpectrometryDataProduct.md) | Abstract base for all mass spectrometry data products |  no  |
| [MSImageProduct](MSImageProduct.md) | one or more image(s) output from a mass spec data processing workflow (eg |  no  |







## Properties

* Range: [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:results_from_ms_processing |
| native | analysis_api_schema:results_from_ms_processing |




## LinkML Source

<details>
```yaml
name: results_from_ms_processing
description: a reference to the mass spec data processing activity that produced this
  data product
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: results_from_ms_processing
domain_of:
- MassSpectrometryDataProduct
range: MassSpectrometryDataProcessingActivity

```
</details>