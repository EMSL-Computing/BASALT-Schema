

# Slot: bulk electrical conductivity (bulk_elect_conductivity) 


_Electrical conductivity is a measure of the bulk soil ability to carry electric current which is mostly dictated by the chemistry of and amount of soil water. (Unit: mS/cm)_





URI: [analysis_api_schema:bulk_elect_conductivity](https://w3id.org/MONet/analysis-api-schema/bulk_elect_conductivity)
Alias: bulk_elect_conductivity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MonetSoilSample](MonetSoilSample.md) | A soil sample that has been collected according to the MONet soil sampling pr... |  yes  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*mS/cm$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:bulk_elect_conductivity |
| native | analysis_api_schema:bulk_elect_conductivity |




## LinkML Source

<details>
```yaml
name: bulk_elect_conductivity
description: 'Electrical conductivity is a measure of the bulk soil ability to carry
  electric current which is mostly dictated by the chemistry of and amount of soil
  water. (Unit: mS/cm)'
title: bulk electrical conductivity
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: bulk_elect_conductivity
domain_of:
- MonetSoilSample
- OtherUndescribedSample
- SoilSample
range: string
pattern: ^\d+(\.\d+)?\s*mS/cm$

```
</details>