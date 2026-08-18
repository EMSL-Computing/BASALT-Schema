

# Slot: column_manufacturer 


_Name of the institution that manufactured the chromatography column._





URI: [basalt_schema:column_manufacturer](https://EMSL-Computing.github.io/BASALT-Schema/column_manufacturer)
Alias: column_manufacturer

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
| self | basalt_schema:column_manufacturer |
| native | basalt_schema:column_manufacturer |




## LinkML Source

<details>
```yaml
name: column_manufacturer
description: Name of the institution that manufactured the chromatography column.
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: column_manufacturer
domain_of:
- ChromatographyConfiguration
range: string

```
</details>