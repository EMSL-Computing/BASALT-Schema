

# Slot: total_nitrogen_id 



URI: [basalt_schema:total_nitrogen_id](https://emsl-computing.github.io/BASALT-Schema/elements/total_nitrogen_id)
Alias: total_nitrogen_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ElementalAnalysisProduct](ElementalAnalysisProduct.md) | Elemental analysis product, typically derived via combustion or similar instr... |  no  |
| [WEOMProduct](WEOMProduct.md) | Water Extractable Organic Matter (WEOM) analysis product, typically derived v... |  no  |
| [MAOMProduct](MAOMProduct.md) | Mineral-Associated Organic Matter (MAOM) analysis product, typically derived ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ElementalAnalysisProduct](ElementalAnalysisProduct.md), [MAOMProduct](MAOMProduct.md), [WEOMProduct](WEOMProduct.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:total_nitrogen_id |
| native | basalt_schema:total_nitrogen_id |




## LinkML Source

<details>
```yaml
name: total_nitrogen_id
alias: total_nitrogen_id
domain_of:
- ElementalAnalysisProduct
- MAOMProduct
- WEOMProduct
range: string

```
</details>