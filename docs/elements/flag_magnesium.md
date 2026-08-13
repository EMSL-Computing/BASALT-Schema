

# Slot: flag_magnesium 



URI: [basalt_schema:flag_magnesium](https://EMSL-Computing.github.io/BASALT-Schema/flag_magnesium)
Alias: flag_magnesium

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IonsAnalysisProduct](IonsAnalysisProduct.md) | Ions analysis product, typically derived via ICP-OES or similar instrument |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ProcessedDataFlag](ProcessedDataFlag.md) |
| Domain Of | [IonsAnalysisProduct](IonsAnalysisProduct.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [IonsAnalysisProduct](IonsAnalysisProduct.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:flag_magnesium |
| native | basalt_schema:flag_magnesium |




## LinkML Source

<details>
```yaml
name: flag_magnesium
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: flag_magnesium
owner: IonsAnalysisProduct
domain_of:
- IonsAnalysisProduct
range: ProcessedDataFlag

```
</details>