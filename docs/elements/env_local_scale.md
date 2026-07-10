

# Slot: local environmental context (env_local_scale) 


_'Report the entity which are in your sample or specimens local vicinity and which you believe have significant causal influences on your sample or specimen. Please use terms that are present in ENVO and which are of smaller spatial grain than your entry for env_broad_scale.If needed, request new terms on the ENVO tracker identified here: http://www.obofoundry.org/ontology/envo.html'_





URI: [analysis_api_schema:env_local_scale](https://w3id.org/MONet/analysis-api-schema/env_local_scale)
Alias: env_local_scale

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
| self | analysis_api_schema:env_local_scale |
| native | analysis_api_schema:env_local_scale |




## LinkML Source

<details>
```yaml
name: env_local_scale
description: '''Report the entity which are in your sample or specimens local vicinity
  and which you believe have significant causal influences on your sample or specimen.
  Please use terms that are present in ENVO and which are of smaller spatial grain
  than your entry for env_broad_scale.If needed, request new terms on the ENVO tracker
  identified here: http://www.obofoundry.org/ontology/envo.html'''
title: local environmental context
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: env_local_scale
domain_of:
- Site
range: string
pattern: ^_*\s*[a-zA-Z\s]+\[ENVO:\d+\]$

```
</details>