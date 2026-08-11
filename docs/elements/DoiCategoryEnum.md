# Enum: DoiCategoryEnum 




_The authority, or organization, the DOI is associated with_



URI: [basalt_schema:DoiCategoryEnum](https://EMSL-Computing.github.io/basalt-schema/DoiCategoryEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| award_doi | None | A type of DOI that resolves to a funding authority |
| dataset_doi | None | A type of DOI that resolves to generated data |
| publication_doi | None | A type of DOI that resolves to a publication |
| data_management_plan_doi | None | A type of DOI that resolves to a data management plan |




## Slots

| Name | Description |
| ---  | --- |
| [doi_category](doi_category.md) | The resource type the corresponding doi resolves to |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema






## LinkML Source

<details>
```yaml
name: DoiCategoryEnum
description: The authority, or organization, the DOI is associated with
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
permissible_values:
  award_doi:
    text: award_doi
    description: A type of DOI that resolves to a funding authority.
  dataset_doi:
    text: dataset_doi
    description: A type of DOI that resolves to generated data.
  publication_doi:
    text: publication_doi
    description: A type of DOI that resolves to a publication.
  data_management_plan_doi:
    text: data_management_plan_doi
    description: A type of DOI that resolves to a data management plan.

```
</details>