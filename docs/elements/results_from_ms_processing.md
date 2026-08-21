

# Slot: results_from_ms_processing 


_a reference to the mass spec data processing activity that produced this data product_





URI: [basalt_schema:results_from_ms_processing](https://emsl-computing.github.io/BASALT-Schema/elements/results_from_ms_processing)
Alias: results_from_ms_processing

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryDataProduct](MassSpectrometryDataProduct.md) | Abstract base for all mass spectrometry data products |  no  |
| [MSImageProduct](MSImageProduct.md) | one or more image(s) output from a mass spec data processing workflow (eg |  no  |
| [MetaproteomicsProduct](MetaproteomicsProduct.md) | Abstract parent class for processed metaproteomics data |  no  |
| [MolecularIdentificationProduct](MolecularIdentificationProduct.md) | a file containing molecular formula identifications that was output from a ma... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md) |
| Domain Of | [MassSpectrometryDataProduct](MassSpectrometryDataProduct.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:results_from_ms_processing |
| native | basalt_schema:results_from_ms_processing |




## LinkML Source

<details>
```yaml
name: results_from_ms_processing
description: a reference to the mass spec data processing activity that produced this
  data product
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: results_from_ms_processing
domain_of:
- MassSpectrometryDataProduct
range: MassSpectrometryDataProcessingActivity

```
</details>