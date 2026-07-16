

# Slot: flag 



URI: [analysis_api_schema:flag](https://w3id.org/MONet/analysis-api-schema/flag)
Alias: flag

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HydraulicPropertiesProduct](HydraulicPropertiesProduct.md) | Soil hydraulic parameters derived from HYPROP evaporation-experiment data |  no  |
| [WellReading](WellReading.md) | Per-well measurement data |  no  |
| [EnzymeProduct](EnzymeProduct.md) |  |  no  |
| [PHProduct](PHProduct.md) |  |  no  |
| [PhosphorusAnalysisProduct](PhosphorusAnalysisProduct.md) |  |  no  |
| [TextureProduct](TextureProduct.md) |  |  no  |
| [RespirationProduct](RespirationProduct.md) |  |  no  |
| [GWCMoistureProduct](GWCMoistureProduct.md) |  |  no  |
| [BulkDensityProduct](BulkDensityProduct.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [WellReading](WellReading.md), [BulkDensityProduct](BulkDensityProduct.md), [EnzymeProduct](EnzymeProduct.md), [GWCMoistureProduct](GWCMoistureProduct.md), [HydraulicPropertiesProduct](HydraulicPropertiesProduct.md), [PhosphorusAnalysisProduct](PhosphorusAnalysisProduct.md), [RespirationProduct](RespirationProduct.md), [TextureProduct](TextureProduct.md), [PHProduct](PHProduct.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:flag |
| native | analysis_api_schema:flag |




## LinkML Source

<details>
```yaml
name: flag
alias: flag
domain_of:
- WellReading
- BulkDensityProduct
- EnzymeProduct
- GWCMoistureProduct
- HydraulicPropertiesProduct
- PhosphorusAnalysisProduct
- RespirationProduct
- TextureProduct
- pHProduct
range: string

```
</details>