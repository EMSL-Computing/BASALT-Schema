

# Slot: bulk electrical conductivity (bulk_elect_conductivity) 


_Electrical conductivity is a measure of the bulk soil ability to carry electric current which is mostly dictated by the chemistry of and amount of soil water. (Unit: mS/cm)_





URI: [basalt_schema:bulk_elect_conductivity](https://emsl-computing.github.io/BASALT-Schema/elements/bulk_elect_conductivity)
Alias: bulk_elect_conductivity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MonetSoilSample](MonetSoilSample.md) | A soil sample that has been collected according to the MONet soil sampling pr... |  yes  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MonetSoilSample](MonetSoilSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [SoilSample](SoilSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*mS/cm$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:bulk_elect_conductivity |
| native | basalt_schema:bulk_elect_conductivity |




## LinkML Source

<details>
```yaml
name: bulk_elect_conductivity
description: 'Electrical conductivity is a measure of the bulk soil ability to carry
  electric current which is mostly dictated by the chemistry of and amount of soil
  water. (Unit: mS/cm)'
title: bulk electrical conductivity
from_schema: https://emsl-computing.github.io/BASALT-Schema
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