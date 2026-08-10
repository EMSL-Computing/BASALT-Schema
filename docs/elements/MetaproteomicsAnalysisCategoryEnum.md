# Enum: MetaproteomicsAnalysisCategoryEnum 




_The category of metaproteomics analysis being performed._



URI: [basalt_schema:MetaproteomicsAnalysisCategoryEnum](https://w3id.org/MONet/basalt-schema/MetaproteomicsAnalysisCategoryEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| matched_metagenome | None | A metaproteomics analysis matched to a metagenome from the same biosample |
| in_silico_metagenome | None | A metaproteomics analysis matched to an in silico generated metagenome |
| WITHDRAWN | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [metaproteomics_analysis_category](metaproteomics_analysis_category.md) | The category of metaproteomics analysis being performed, if applicable |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema






## LinkML Source

<details>
```yaml
name: MetaproteomicsAnalysisCategoryEnum
description: The category of metaproteomics analysis being performed.
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
permissible_values:
  matched_metagenome:
    text: matched_metagenome
    description: A metaproteomics analysis matched to a metagenome from the same biosample.
  in_silico_metagenome:
    text: in_silico_metagenome
    description: A metaproteomics analysis matched to an in silico generated metagenome.
  WITHDRAWN:
    text: WITHDRAWN

```
</details>