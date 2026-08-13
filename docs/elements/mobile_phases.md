

# Slot: mobile_phases 


_Description of the mobile phases used in the chromatography method (e.g., solvents, gradients)_





URI: [basalt_schema:mobile_phases](https://EMSL-Computing.github.io/BASALT-Schema/mobile_phases)
Alias: mobile_phases

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChromatographyConfiguration](ChromatographyConfiguration.md) | Configuration and settings for a chromatography run |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MobilePhaseSegment](MobilePhaseSegment.md) |
| Domain Of | [ChromatographyConfiguration](ChromatographyConfiguration.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:mobile_phases |
| native | basalt_schema:mobile_phases |




## LinkML Source

<details>
```yaml
name: mobile_phases
description: Description of the mobile phases used in the chromatography method (e.g.,
  solvents, gradients)
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: mobile_phases
domain_of:
- ChromatographyConfiguration
range: MobilePhaseSegment
multivalued: true

```
</details>