

# Slot: agrochemical additions (agrochem_addition) 


_Addition of fertilizers, pesticides, etc. - amount and time of applications_





URI: [basalt_schema:agrochem_addition](https://EMSL-Computing.github.io/BASALT-Schema/agrochem_addition)
Alias: agrochem_addition

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [MonetSoilSample](MonetSoilSample.md) | A soil sample that has been collected according to the MONet soil sampling pr... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MonetSoilSample](MonetSoilSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [SoilSample](SoilSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:agrochem_addition |
| native | basalt_schema:agrochem_addition |




## LinkML Source

<details>
```yaml
name: agrochem_addition
description: Addition of fertilizers, pesticides, etc. - amount and time of applications
title: agrochemical additions
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: agrochem_addition
domain_of:
- MonetSoilSample
- OtherUndescribedSample
- SoilSample
range: string

```
</details>