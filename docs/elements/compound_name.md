

# Slot: compound name (compound_name) 


_The name of the purchased material. A substance formed by chemical union of two or more elements or ingredients in definite proportion by weight._





URI: [analysis_api_schema:compound_name](https://w3id.org/MONet/analysis-api-schema/compound_name)
Alias: compound_name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SynthesizedMaterialSample](SynthesizedMaterialSample.md) | A sample containing synthetically generated material |  no  |
| [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md) | A sample containing commercially purchased material |  yes  |






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
| self | analysis_api_schema:compound_name |
| native | analysis_api_schema:compound_name |




## LinkML Source

<details>
```yaml
name: compound_name
description: The name of the purchased material. A substance formed by chemical union
  of two or more elements or ingredients in definite proportion by weight.
title: compound name
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: compound_name
domain_of:
- CommerciallyPurchasedSample
- OtherUndescribedSample
- SynthesizedMaterialSample
range: string

```
</details>