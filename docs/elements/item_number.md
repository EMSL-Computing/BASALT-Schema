

# Slot: item number (item_number) 


_The item number of the purchased material_





URI: [analysis_api_schema:item_number](https://w3id.org/MONet/analysis-api-schema/item_number)
Alias: item_number

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SynthesizedMaterialSample](SynthesizedMaterialSample.md) | A sample containing synthetically generated material |  no  |
| [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md) | A sample containing commercially purchased material |  no  |






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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:item_number |
| native | analysis_api_schema:item_number |




## LinkML Source

<details>
```yaml
name: item_number
description: The item number of the purchased material
title: item number
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: item_number
domain_of:
- CommerciallyPurchasedSample
- OtherUndescribedSample
- SynthesizedMaterialSample
range: string

```
</details>