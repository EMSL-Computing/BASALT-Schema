

# Slot: flag 



URI: [basalt_schema:flag](https://EMSL-Computing.github.io/basalt-schema/flag)
Alias: flag

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhosphorusAnalysisProduct](PhosphorusAnalysisProduct.md) | Phosphorus analysis product, typically derived via colorimetric assay of soil... |  no  |
| [PHProduct](PHProduct.md) | Soil pH analysis product, typically derived via pH meter or similar instrumen... |  no  |
| [BulkDensityProduct](BulkDensityProduct.md) | Bulk density analysis product, typically derived via oven-drying and weighing... |  no  |
| [EnzymeProduct](EnzymeProduct.md) | Enzyme activity analysis product, typically derived via colorimetric assay of... |  no  |
| [HydraulicPropertiesProduct](HydraulicPropertiesProduct.md) | Soil hydraulic parameters derived from HYPROP evaporation-experiment data |  no  |
| [RespirationProduct](RespirationProduct.md) | Soil respiration analysis product |  no  |
| [GWCMoistureProduct](GWCMoistureProduct.md) | Gravimetric water content (GWC) analysis product, typically derived via oven-... |  no  |
| [WellReading](WellReading.md) | Per-well measurement data |  no  |
| [TextureProduct](TextureProduct.md) | Soil texture analysis product, typically derived via hydrometer or similar in... |  no  |






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
| self | basalt_schema:flag |
| native | basalt_schema:flag |




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