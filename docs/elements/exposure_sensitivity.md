

# Slot: exposure_sensitivity 


_Sensitivity the entity has if exposed (e.g. light-sensitive, oxygen-sensitive)_





URI: [basalt_schema:exposure_sensitivity](https://EMSL-Computing.github.io/BASALT-Schema/exposure_sensitivity)
Alias: exposure_sensitivity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaPreparation](MediaPreparation.md) | Activity that prepares a batch of growth media |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MediaPreparation](MediaPreparation.md) |

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
| self | basalt_schema:exposure_sensitivity |
| native | basalt_schema:exposure_sensitivity |




## LinkML Source

<details>
```yaml
name: exposure_sensitivity
description: Sensitivity the entity has if exposed (e.g. light-sensitive, oxygen-sensitive)
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: exposure_sensitivity
domain_of:
- MediaPreparation
range: string
multivalued: true

```
</details>