

# Slot: production method (production_method) 


_A DOI or description of how the compound was produced, if the commercially purchased material was altered_





URI: [basalt_schema:production_method](https://emsl-computing.github.io/BASALT-Schema/elements/production_method)
Alias: production_method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SynthesizedMaterialSample](SynthesizedMaterialSample.md) | A sample containing synthetically generated material |  no  |
| [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md) | A sample containing commercially purchased material |  no  |
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


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:production_method |
| native | basalt_schema:production_method |




## LinkML Source

<details>
```yaml
name: production_method
description: A DOI or description of how the compound was produced, if the commercially
  purchased material was altered
title: production method
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: production_method
domain_of:
- CommerciallyPurchasedSample
- OtherUndescribedSample
- SynthesizedMaterialSample
range: string

```
</details>