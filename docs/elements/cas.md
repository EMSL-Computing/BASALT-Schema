

# Slot: CAS number (cas) 


_A unique numerical identifier assigned by the Chemical Abstract Service (CAS), a division of the American Chemical Society, to chemical compounds, polymers, biological sequences, mixtures, and alloys._





URI: [basalt_schema:cas](https://EMSL-Computing.github.io/BASALT-Schema/cas)
Alias: cas

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SynthesizedMaterialSample](SynthesizedMaterialSample.md) | A sample containing synthetically generated material |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
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







## Aliases


* CAS




## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:cas |
| native | basalt_schema:cas |




## LinkML Source

<details>
```yaml
name: cas
description: A unique numerical identifier assigned by the Chemical Abstract Service
  (CAS), a division of the American Chemical Society, to chemical compounds, polymers,
  biological sequences, mixtures, and alloys.
title: CAS number
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
aliases:
- CAS
rank: 1000
alias: cas
domain_of:
- CommerciallyPurchasedSample
- OtherUndescribedSample
- SynthesizedMaterialSample
range: string

```
</details>