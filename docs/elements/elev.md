

# Slot: elevation (elev) 


_Elevation of the sampling site is its height above a fixed reference point, most commonly the mean sea level. Elevation is mainly used when referring to points on the earth's surface. (Unit: m)._





URI: [analysis_api_schema:elev](https://w3id.org/MONet/analysis-api-schema/elev)
Alias: elev

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Site](Site.md) | Site-level metadata for a specific location from which a set of samples are c... |  yes  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*m$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:elev |
| native | analysis_api_schema:elev |




## LinkML Source

<details>
```yaml
name: elev
description: 'Elevation of the sampling site is its height above a fixed reference
  point, most commonly the mean sea level. Elevation is mainly used when referring
  to points on the earth''s surface. (Unit: m).'
title: elevation
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: elev
domain_of:
- Site
range: string
pattern: ^\d+(\.\d+)?\s*m$

```
</details>