

# Slot: strain_identifier 


_External human-readable strain identifier (e.g. "KT2440_pTE314")._

_NOT the database UUID   that is the Strain.id attribute._





URI: [analysis_api_schema:strain_identifier](https://w3id.org/MONet/analysis-api-schema/strain_identifier)
Alias: strain_identifier

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiologicalEntity](BiologicalEntity.md) | Reference data representing a biological identity (strain, isolate, |  yes  |







## Properties

* Range: [String](String.md)

* Required: True



## Aliases


* strain_id
* strain_name



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:strain_identifier |
| native | analysis_api_schema:strain_identifier |




## LinkML Source

<details>
```yaml
name: strain_identifier
description: 'External human-readable strain identifier (e.g. "KT2440_pTE314").

  NOT the database UUID   that is the Strain.id attribute.'
from_schema: https://w3id.org/MONet/analysis-api-schema
aliases:
- strain_id
- strain_name
rank: 1000
alias: strain_identifier
domain_of:
- biological_entity
range: string
required: true

```
</details>