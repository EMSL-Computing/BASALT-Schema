

# Slot: pathogenicity (pathogenicity) 


_To what is the entity pathogenic, e.g., humans, animals, plants, or specific tissues._





URI: [basalt_schema:pathogenicity](https://EMSL-Computing.github.io/basalt-schema/pathogenicity)
Alias: pathogenicity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organism](Organism.md) | Reference data representing a biological identity (strain, isolate, |  no  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Organism](Organism.md), [CultureEnvironmentalSample](CultureEnvironmentalSample.md), [MixedCultureSample](MixedCultureSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [PureCultureSample](PureCultureSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:pathogenicity |
| native | basalt_schema:pathogenicity |




## LinkML Source

<details>
```yaml
name: pathogenicity
description: To what is the entity pathogenic, e.g., humans, animals, plants, or specific
  tissues.
title: pathogenicity
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: pathogenicity
domain_of:
- organism
- CultureEnvironmentalSample
- MixedCultureSample
- OtherUndescribedSample
- PureCultureSample
range: string

```
</details>