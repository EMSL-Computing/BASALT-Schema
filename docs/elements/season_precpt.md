

# Slot: mean seasonal precipitation (season_precpt) 


_The average of all seasonal precipitation values known or an estimated equivalent value derived by such methods as regional indexes or Isohyetal maps. (Unit: mm)_





URI: [analysis_api_schema:season_precpt](https://w3id.org/MONet/analysis-api-schema/season_precpt)
Alias: season_precpt

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Site](Site.md) | Site-level metadata for a specific location from which a set of samples are c... |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*mm$`



## Aliases


* average seasonal precipitation



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:season_precpt |
| native | analysis_api_schema:season_precpt |




## LinkML Source

<details>
```yaml
name: season_precpt
description: 'The average of all seasonal precipitation values known or an estimated
  equivalent value derived by such methods as regional indexes or Isohyetal maps.
  (Unit: mm)'
title: mean seasonal precipitation
from_schema: https://w3id.org/MONet/analysis-api-schema
aliases:
- average seasonal precipitation
rank: 1000
alias: season_precpt
domain_of:
- Site
range: string
pattern: ^\d+(\.\d+)?\s*mm$

```
</details>