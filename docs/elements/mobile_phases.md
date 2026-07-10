

# Slot: mobile_phases 


_Description of the mobile phases used in the chromatography method (e.g., solvents, gradients)_





URI: [analysis_api_schema:mobile_phases](https://w3id.org/MONet/analysis-api-schema/mobile_phases)
Alias: mobile_phases

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChromatographyConfiguration](ChromatographyConfiguration.md) | Configuration and settings for a chromatography run |  no  |







## Properties

* Range: [MobilePhaseSegment](MobilePhaseSegment.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:mobile_phases |
| native | analysis_api_schema:mobile_phases |




## LinkML Source

<details>
```yaml
name: mobile_phases
description: Description of the mobile phases used in the chromatography method (e.g.,
  solvents, gradients)
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: mobile_phases
domain_of:
- ChromatographyConfiguration
range: MobilePhaseSegment
multivalued: true

```
</details>