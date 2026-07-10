

# Slot: slope gradient (slope_gradient) 


_Commonly called 'slope'. The angle between ground surface and a horizontal line (in percent). This is the direction that overland water would flow. This measure is usually taken with a hand level meter or clinometer. (Unit: percent)_





URI: [analysis_api_schema:slope_gradient](https://w3id.org/MONet/analysis-api-schema/slope_gradient)
Alias: slope_gradient

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Site](Site.md) | Site-level metadata for a specific location from which a set of samples are c... |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*percent$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:slope_gradient |
| native | analysis_api_schema:slope_gradient |




## LinkML Source

<details>
```yaml
name: slope_gradient
description: 'Commonly called ''slope''. The angle between ground surface and a horizontal
  line (in percent). This is the direction that overland water would flow. This measure
  is usually taken with a hand level meter or clinometer. (Unit: percent)'
title: slope gradient
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: slope_gradient
domain_of:
- Site
range: string
pattern: ^\d+(\.\d+)?\s*percent$

```
</details>