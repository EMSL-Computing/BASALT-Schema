

# Slot: compound name (compound_name) 


_The name of the purchased material. A substance formed by chemical union of two or more elements or ingredients in definite proportion by weight._





URI: [basalt_schema:compound_name](https://w3id.org/MONet/basalt-schema/compound_name)
Alias: compound_name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md) | A sample containing commercially purchased material |  yes  |
| [SynthesizedMaterialSample](SynthesizedMaterialSample.md) | A sample containing synthetically generated material |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






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


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:compound_name |
| native | basalt_schema:compound_name |




## LinkML Source

<details>
```yaml
name: compound_name
description: The name of the purchased material. A substance formed by chemical union
  of two or more elements or ingredients in definite proportion by weight.
title: compound name
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: compound_name
domain_of:
- CommerciallyPurchasedSample
- OtherUndescribedSample
- SynthesizedMaterialSample
range: string

```
</details>