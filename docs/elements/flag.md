

# Slot: flag 



URI: [analysis_api_schema:flag](https://w3id.org/MONet/analysis-api-schema/flag)
Alias: flag

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GWCMoistureProduct](GWCMoistureProduct.md) |  |  no  |
| [BulkDensityProduct](BulkDensityProduct.md) |  |  no  |
| [RespirationProduct](RespirationProduct.md) |  |  no  |
| [EnzymeProduct](EnzymeProduct.md) |  |  no  |
| [PHProduct](PHProduct.md) |  |  no  |
| [WellReading](WellReading.md) | Per-well measurement data |  no  |
| [PhosphorusAnalysisProduct](PhosphorusAnalysisProduct.md) |  |  no  |
| [HydraulicPropertiesProduct](HydraulicPropertiesProduct.md) | Soil hydraulic parameters derived from HYPROP evaporation-experiment data |  no  |
| [TextureProduct](TextureProduct.md) |  |  no  |







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