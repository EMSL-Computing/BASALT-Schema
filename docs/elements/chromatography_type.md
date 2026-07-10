

# Slot: chromatography_type 


_Type of chromatography used in the method (e.g., GC, LC)_





URI: [analysis_api_schema:chromatography_type](https://w3id.org/MONet/analysis-api-schema/chromatography_type)
Alias: chromatography_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChromatographyConfiguration](ChromatographyConfiguration.md) | Configuration and settings for a chromatography run |  no  |







## Properties

* Range: [ChromatographyCategoryEnum](ChromatographyCategoryEnum.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:chromatography_type |
| native | analysis_api_schema:chromatography_type |




## LinkML Source

<details>
```yaml
name: chromatography_type
description: Type of chromatography used in the method (e.g., GC, LC)
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: chromatography_type
domain_of:
- ChromatographyConfiguration
range: ChromatographyCategoryEnum
required: true

```
</details>