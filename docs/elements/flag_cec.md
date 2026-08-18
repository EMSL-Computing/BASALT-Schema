

# Slot: flag_cec 



URI: [basalt_schema:flag_cec](https://emsl-computing.github.io/BASALT-Schema/elements/flag_cec)
Alias: flag_cec

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


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:flag_cec |
| native | basalt_schema:flag_cec |




## LinkML Source

<details>
```yaml
name: flag_cec
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: flag_cec
owner: IonsAnalysisProduct
domain_of:
- IonsAnalysisProduct
range: ProcessedDataFlag

```
</details>