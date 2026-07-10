

# Slot: environmental medium (env_medium) 


_'Report the environmental material immediately surrounding the sample or specimen at the time of sampling. We recommend using subclasses of ''environmental material'' (http://purl.obolibrary.org/obo/ENVO_00010483). EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS.'_





URI: [analysis_api_schema:env_medium](https://w3id.org/MONet/analysis-api-schema/env_medium)
Alias: env_medium

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
| self | analysis_api_schema:env_medium |
| native | analysis_api_schema:env_medium |




## LinkML Source

<details>
```yaml
name: env_medium
description: '''Report the environmental material immediately surrounding the sample
  or specimen at the time of sampling. We recommend using subclasses of ''''environmental
  material'''' (http://purl.obolibrary.org/obo/ENVO_00010483). EnvO documentation
  about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS.'''
title: environmental medium
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: env_medium
domain_of:
- Site
range: string
pattern: ^_*\s*[a-zA-Z\s]+\[ENVO:\d+\]$

```
</details>