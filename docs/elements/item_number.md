

# Slot: item number (item_number) 


_The item number of the purchased material_





URI: [basalt_schema:item_number](https://EMSL-Computing.github.io/basalt-schema/item_number)
Alias: item_number

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md) | A sample containing commercially purchased material |  no  |
| [SynthesizedMaterialSample](SynthesizedMaterialSample.md) | A sample containing synthetically generated material |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [SynthesizedMaterialSample](SynthesizedMaterialSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:item_number |
| native | basalt_schema:item_number |




## LinkML Source

<details>
```yaml
name: item_number
description: The item number of the purchased material
title: item number
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: item_number
domain_of:
- CommerciallyPurchasedSample
- OtherUndescribedSample
- SynthesizedMaterialSample
range: string

```
</details>