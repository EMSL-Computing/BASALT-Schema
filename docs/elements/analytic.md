

# Slot: analytic 



URI: [basalt_schema:analytic](https://emsl-computing.github.io/BASALT-Schema/elements/analytic)
Alias: analytic

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TextureMethod](TextureMethod.md) |  |  no  |
| [XrayComputedTomographyMethod](XrayComputedTomographyMethod.md) |  |  no  |
| [MicrobialBiomassMethod](MicrobialBiomassMethod.md) |  |  no  |
| [GravimetricWaterContentMethod](GravimetricWaterContentMethod.md) |  |  no  |
| [PHMethod](PHMethod.md) |  |  no  |
| [RespirationMethod](RespirationMethod.md) |  |  no  |
| [HydraulicPropertiesMethod](HydraulicPropertiesMethod.md) |  |  no  |
| [Method](Method.md) |  |  no  |
| [EnzymeActivityMethod](EnzymeActivityMethod.md) |  |  no  |
| [ElementalAnalysisMethod](ElementalAnalysisMethod.md) |  |  no  |
| [TOCTNMethod](TOCTNMethod.md) |  |  no  |
| [KuoMethod](KuoMethod.md) |  |  no  |
| [BulkDensityMethod](BulkDensityMethod.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Method](Method.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |








## TODOs

* what does this mean



## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:analytic |
| native | basalt_schema:analytic |




## LinkML Source

<details>
```yaml
name: analytic
todos:
- what does this mean
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: analytic
domain_of:
- Method
range: string
required: true

```
</details>