# Enum: ExecutionResourceEnum 




_The computing resource or facility where the processing was executed._



URI: [basalt_schema:ExecutionResourceEnum](https://EMSL-Computing.github.io/basalt-schema/ExecutionResourceEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| nersc_cori | None | NERSC Cori supercomputer |
| nersc_perlmutter | None | NERSC Perlmutter supercomputer |
| emsl_rzr | None | Environmental Molecular Sciences Laboratory RZR cluster |
| emsl_tahoma | None | Environmental Molecular Sciences Laboratory Tahoma cluster |




## Slots

| Name | Description |
| ---  | --- |
| [execution_resource](execution_resource.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema






## LinkML Source

<details>
```yaml
name: ExecutionResourceEnum
description: The computing resource or facility where the processing was executed.
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
permissible_values:
  nersc_cori:
    text: nersc_cori
    description: NERSC Cori supercomputer
    aliases:
    - Cori
  nersc_perlmutter:
    text: nersc_perlmutter
    description: NERSC Perlmutter supercomputer
    aliases:
    - Perlmutter
    - Saul
  emsl_rzr:
    text: emsl_rzr
    description: Environmental Molecular Sciences Laboratory RZR cluster
    aliases:
    - RZR
  emsl_tahoma:
    text: emsl_tahoma
    description: Environmental Molecular Sciences Laboratory Tahoma cluster
    aliases:
    - Tahoma

```
</details>