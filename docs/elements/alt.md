

# Slot: altitude (alt) 


_Heights of objects such as airplanes, space shuttles, rockets, atmospheric balloons and heights of places such as atmospheric layers and clouds. It is used to measure the height of an object which is above the earth's surface. In this context, the altitude measurement is the vertical distance between the earth's surface above sea level and the sampled position in the air. For ARM this can be a range. (Unit: m)_





URI: [analysis_api_schema:alt](https://w3id.org/MONet/analysis-api-schema/alt)
Alias: alt

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Site](Site.md) | Site-level metadata for a specific location from which a set of samples are c... |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?m(?:-\d+(\.\d+)?m)?$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:alt |
| native | analysis_api_schema:alt |




## LinkML Source

<details>
```yaml
name: alt
description: 'Heights of objects such as airplanes, space shuttles, rockets, atmospheric
  balloons and heights of places such as atmospheric layers and clouds. It is used
  to measure the height of an object which is above the earth''s surface. In this
  context, the altitude measurement is the vertical distance between the earth''s
  surface above sea level and the sampled position in the air. For ARM this can be
  a range. (Unit: m)'
title: altitude
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: alt
domain_of:
- Site
range: string
pattern: ^\d+(\.\d+)?m(?:-\d+(\.\d+)?m)?$

```
</details>