

# Slot: trophic level (trophic_level) 


_Trophic levels are the feeding position in a food chain. Microbes can_

_be a range of producers._





URI: [basalt_schema:trophic_level](https://emsl-computing.github.io/BASALT-Schema/elements/trophic_level)
Alias: trophic_level

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  no  |
| [Organism](Organism.md) | Reference data representing a biological identity (strain, isolate, |  yes  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TrophicLevelEnum](TrophicLevelEnum.md) |
| Domain Of | [Organism](Organism.md), [CultureEnvironmentalSample](CultureEnvironmentalSample.md), [MixedCultureSample](MixedCultureSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [PureCultureSample](PureCultureSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:trophic_level |
| native | basalt_schema:trophic_level |




## LinkML Source

<details>
```yaml
name: trophic_level
description: 'Trophic levels are the feeding position in a food chain. Microbes can

  be a range of producers.'
title: trophic level
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: trophic_level
domain_of:
- organism
- CultureEnvironmentalSample
- MixedCultureSample
- OtherUndescribedSample
- PureCultureSample
range: TrophicLevelEnum

```
</details>