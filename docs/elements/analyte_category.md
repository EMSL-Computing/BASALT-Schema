

# Slot: analyte_category 


_omics type for easier search, optional_





URI: [basalt_schema:analyte_category](https://EMSL-Computing.github.io/basalt-schema/analyte_category)
Alias: analyte_category

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryDataGenerationActivity](MassSpectrometryDataGenerationActivity.md) | A record of the mass spectrometry run that generates a raw data product |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AnalyteCategoryEnum](AnalyteCategoryEnum.md) |
| Domain Of | [MassSpectrometryDataGenerationActivity](MassSpectrometryDataGenerationActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:analyte_category |
| native | basalt_schema:analyte_category |




## LinkML Source

<details>
```yaml
name: analyte_category
description: omics type for easier search, optional
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: analyte_category
domain_of:
- MassSpectrometryDataGenerationActivity
range: AnalyteCategoryEnum

```
</details>