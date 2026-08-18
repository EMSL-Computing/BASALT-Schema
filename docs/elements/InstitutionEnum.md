# Enum: InstitutionEnum 




_The organization that processed the sample / ran the pipeline / participated in the project._



URI: [basalt_schema:InstitutionEnum](https://EMSL-Computing.github.io/BASALT-Schema/InstitutionEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| nmdc | None |  | Title: National Microbiome Data Collaborative<br>|
| ucsd | None |  | Title: University of California, San Diego<br>|
| jgi | None |  | Title: Joint Genome Institute<br>|
| emsl | None |  | Title: Environmental Molecular Sciences Laboratory<br>|
| battelle | None |  | Title: Battelle Memorial Institute<br>|
| anl | None |  | Title: Argonne National Laboratory<br>|
| ucd_genome_center | None |  | Title: University of California, Davis Genome Center<br>|
| azenta | None |  | Title: Azenta Life Sciences<br>|




## Slots

| Name | Description |
| ---  | --- |
| [processing_institution](processing_institution.md) | The institution where the activity took place |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema






## LinkML Source

<details>
```yaml
name: InstitutionEnum
description: The organization that processed the sample / ran the pipeline / participated
  in the project.
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
permissible_values:
  nmdc:
    text: nmdc
    title: National Microbiome Data Collaborative
  ucsd:
    text: ucsd
    title: University of California, San Diego
  jgi:
    text: jgi
    title: Joint Genome Institute
  emsl:
    text: emsl
    title: Environmental Molecular Sciences Laboratory
  battelle:
    text: battelle
    title: Battelle Memorial Institute
  anl:
    text: anl
    title: Argonne National Laboratory
  ucd_genome_center:
    text: ucd_genome_center
    title: University of California, Davis Genome Center
  azenta:
    text: azenta
    title: Azenta Life Sciences

```
</details>