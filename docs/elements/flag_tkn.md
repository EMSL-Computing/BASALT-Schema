

# Slot: flag_tkn 



URI: [basalt_schema:flag_tkn](https://EMSL-Computing.github.io/basalt-schema/flag_tkn)
Alias: flag_tkn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ElementalAnalysisProduct](ElementalAnalysisProduct.md) | Elemental analysis product, typically derived via combustion or similar instr... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ProcessedDataFlag](ProcessedDataFlag.md) |
| Domain Of | [ElementalAnalysisProduct](ElementalAnalysisProduct.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ElementalAnalysisProduct](ElementalAnalysisProduct.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:flag_tkn |
| native | basalt_schema:flag_tkn |




## LinkML Source

<details>
```yaml
name: flag_tkn
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: flag_tkn
owner: ElementalAnalysisProduct
domain_of:
- ElementalAnalysisProduct
range: ProcessedDataFlag

```
</details>