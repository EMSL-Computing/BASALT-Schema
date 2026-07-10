

# Slot: annotation_database 


_Primary annotation database used (e.g., IMG, KEGG)_





URI: [analysis_api_schema:annotation_database](https://w3id.org/MONet/analysis-api-schema/annotation_database)
Alias: annotation_database

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MetagenomicsAnnotationProduct](MetagenomicsAnnotationProduct.md) | Top-level archive for functional annotation outputs (zip/tar stored in MinIO) |  no  |







## Properties

* Range: [AnnotationDatabaseEnum](AnnotationDatabaseEnum.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:annotation_database |
| native | analysis_api_schema:annotation_database |




## LinkML Source

<details>
```yaml
name: annotation_database
description: Primary annotation database used (e.g., IMG, KEGG)
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: annotation_database
domain_of:
- Metagenomics_AnnotationProduct
range: AnnotationDatabaseEnum
required: false

```
</details>