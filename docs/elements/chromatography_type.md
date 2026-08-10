

# Slot: chromatography_type 


_Type of chromatography used in the method (e.g., GC, LC)_





URI: [basalt_schema:chromatography_type](https://w3id.org/MONet/basalt-schema/chromatography_type)
Alias: chromatography_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChromatographyConfiguration](ChromatographyConfiguration.md) | Configuration and settings for a chromatography run |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ChromatographyCategoryEnum](ChromatographyCategoryEnum.md) |
| Domain Of | [ChromatographyConfiguration](ChromatographyConfiguration.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:chromatography_type |
| native | basalt_schema:chromatography_type |




## LinkML Source

<details>
```yaml
name: chromatography_type
description: Type of chromatography used in the method (e.g., GC, LC)
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: chromatography_type
domain_of:
- ChromatographyConfiguration
range: ChromatographyCategoryEnum
required: true

```
</details>