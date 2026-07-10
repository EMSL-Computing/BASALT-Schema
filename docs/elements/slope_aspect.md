

# Slot: slope aspect (slope_aspect) 


_The direction a slope faces. While looking down a slope use a compass to record the direction you are facing (degrees); e.g. 315 degrees. This measure provides an indication of sun and wind exposure that will influence soil temperature and evapotranspiration. (Unit: degrees)_





URI: [analysis_api_schema:slope_aspect](https://w3id.org/MONet/analysis-api-schema/slope_aspect)
Alias: slope_aspect

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Site](Site.md) | Site-level metadata for a specific location from which a set of samples are c... |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*degrees$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:slope_aspect |
| native | analysis_api_schema:slope_aspect |




## LinkML Source

<details>
```yaml
name: slope_aspect
description: 'The direction a slope faces. While looking down a slope use a compass
  to record the direction you are facing (degrees); e.g. 315 degrees. This measure
  provides an indication of sun and wind exposure that will influence soil temperature
  and evapotranspiration. (Unit: degrees)'
title: slope aspect
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: slope_aspect
domain_of:
- Site
range: string
pattern: ^\d+(\.\d+)?\s*degrees$

```
</details>