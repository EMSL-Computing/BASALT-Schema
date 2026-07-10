

# Slot: duration_min 


_how long something took, in minutes_





URI: [analysis_api_schema:duration_min](https://w3id.org/MONet/analysis-api-schema/duration_min)
Alias: duration_min

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChromatographyConfiguration](ChromatographyConfiguration.md) | Configuration and settings for a chromatography run |  no  |
| [MobilePhaseSegment](MobilePhaseSegment.md) | A segment of the mobile phase used in chromatography during mass spectrometry |  no  |







## Properties

* Range: [Float](Float.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:duration_min |
| native | analysis_api_schema:duration_min |




## LinkML Source

<details>
```yaml
name: duration_min
description: how long something took, in minutes
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: duration_min
domain_of:
- ChromatographyConfiguration
- MobilePhaseSegment
range: float

```
</details>