

# Slot: stationary_phase 


_Description of the stationary phase used in the chromatography method (e.g., column type)_





URI: [basalt_schema:stationary_phase](https://EMSL-Computing.github.io/BASALT-Schema/stationary_phase)
Alias: stationary_phase

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChromatographyConfiguration](ChromatographyConfiguration.md) | Configuration and settings for a chromatography run |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ChromatographyConfiguration](ChromatographyConfiguration.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:stationary_phase |
| native | basalt_schema:stationary_phase |




## LinkML Source

<details>
```yaml
name: stationary_phase
description: Description of the stationary phase used in the chromatography method
  (e.g., column type)
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: stationary_phase
domain_of:
- ChromatographyConfiguration
range: string

```
</details>