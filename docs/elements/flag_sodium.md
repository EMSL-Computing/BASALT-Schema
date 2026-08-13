

# Slot: flag_sodium 



URI: [basalt_schema:flag_sodium](https://EMSL-Computing.github.io/BASALT-Schema/flag_sodium)
Alias: flag_sodium

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
| self | basalt_schema:flag_sodium |
| native | basalt_schema:flag_sodium |




## LinkML Source

<details>
```yaml
name: flag_sodium
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: flag_sodium
owner: IonsAnalysisProduct
domain_of:
- IonsAnalysisProduct
range: ProcessedDataFlag

```
</details>