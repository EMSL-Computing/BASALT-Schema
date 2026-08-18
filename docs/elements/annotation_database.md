

# Slot: annotation_database 


_Primary annotation database used (e.g., IMG, KEGG)_





URI: [basalt_schema:annotation_database](https://emsl-computing.github.io/BASALT-Schema/elements/annotation_database)
Alias: annotation_database

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MetagenomicsAnnotationProduct](MetagenomicsAnnotationProduct.md) | Top-level archive for functional annotation outputs (zip/tar stored in MinIO) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AnnotationDatabaseEnum](AnnotationDatabaseEnum.md) |
| Domain Of | [MetagenomicsAnnotationProduct](MetagenomicsAnnotationProduct.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:annotation_database |
| native | basalt_schema:annotation_database |




## LinkML Source

<details>
```yaml
name: annotation_database
description: Primary annotation database used (e.g., IMG, KEGG)
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: annotation_database
domain_of:
- Metagenomics_AnnotationProduct
range: AnnotationDatabaseEnum
required: false

```
</details>