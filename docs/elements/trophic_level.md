

# Slot: trophic level (trophic_level) 


_Trophic levels are the feeding position in a food chain. Microbes can_

_be a range of producers._





URI: [analysis_api_schema:trophic_level](https://w3id.org/MONet/analysis-api-schema/trophic_level)
Alias: trophic_level

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organism](Organism.md) | Reference data representing a biological identity (strain, isolate, |  yes  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |






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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:trophic_level |
| native | analysis_api_schema:trophic_level |




## LinkML Source

<details>
```yaml
name: trophic_level
description: 'Trophic levels are the feeding position in a food chain. Microbes can

  be a range of producers.'
title: trophic level
from_schema: https://w3id.org/MONet/analysis-api-schema
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