

# Slot: broad-scale environmental context (env_broad_scale) 


_'Report the major environmental system the sample or specimen came from. The system identified should have a coarse spatial grain to provide the general environmental context of where the sampling was done (e.g. in the desert or a rainforest). We recommend using subclasses of EnvO''s biome class: http://purl.obolibrary.org/obo/ENVO_00000428. EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS'_





URI: [analysis_api_schema:env_broad_scale](https://w3id.org/MONet/analysis-api-schema/env_broad_scale)
Alias: env_broad_scale

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Site](Site.md) | Site-level metadata for a specific location from which a set of samples are c... |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^_*\s*[a-zA-Z\s]+\[ENVO:\d+\]$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:env_broad_scale |
| native | analysis_api_schema:env_broad_scale |




## LinkML Source

<details>
```yaml
name: env_broad_scale
description: '''Report the major environmental system the sample or specimen came
  from. The system identified should have a coarse spatial grain to provide the general
  environmental context of where the sampling was done (e.g. in the desert or a rainforest).
  We recommend using subclasses of EnvO''''s biome class: http://purl.obolibrary.org/obo/ENVO_00000428.
  EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS'''
title: broad-scale environmental context
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: env_broad_scale
domain_of:
- Site
range: string
pattern: ^_*\s*[a-zA-Z\s]+\[ENVO:\d+\]$

```
</details>