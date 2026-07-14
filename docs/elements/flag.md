

# Slot: flag 



URI: [analysis_api_schema:flag](https://w3id.org/MONet/analysis-api-schema/flag)
Alias: flag

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PHProduct](PHProduct.md) |  |  no  |
| [TextureProduct](TextureProduct.md) |  |  no  |
| [RespirationProduct](RespirationProduct.md) |  |  no  |
| [BulkDensityProduct](BulkDensityProduct.md) |  |  no  |
| [WellReading](WellReading.md) | Per-well measurement data |  no  |
| [GWCMoistureProduct](GWCMoistureProduct.md) |  |  no  |
| [HydraulicPropertiesProduct](HydraulicPropertiesProduct.md) | Soil hydraulic parameters derived from HYPROP evaporation-experiment data |  no  |
| [PhosphorusAnalysisProduct](PhosphorusAnalysisProduct.md) |  |  no  |
| [EnzymeProduct](EnzymeProduct.md) |  |  no  |







## Properties

* Range: [String](String.md)





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