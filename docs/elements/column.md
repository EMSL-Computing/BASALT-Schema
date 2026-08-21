

# Slot: column 


_The name or identifier of the chromatography column used._





URI: [basalt_schema:column](https://emsl-computing.github.io/BASALT-Schema/elements/column)
Alias: column

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChromatographyConfiguration](ChromatographyConfiguration.md) | Configuration and settings for a chromatography run |  no  |
| [TOCTNMethod](TOCTNMethod.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ChromatographyConfiguration](ChromatographyConfiguration.md), [TOCTNMethod](TOCTNMethod.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:column |
| native | basalt_schema:column |




## LinkML Source

<details>
```yaml
name: column
description: The name or identifier of the chromatography column used.
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: column
domain_of:
- ChromatographyConfiguration
- TOC_TN_Method
range: string

```
</details>