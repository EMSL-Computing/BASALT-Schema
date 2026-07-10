

# Slot: modification method (modification_method) 


_Select the method used to insert your construct into the genome of_

_your modified organism. Examples: "Electroporation", "Conjugation", "CRISPR", "Transduction"_





URI: [analysis_api_schema:modification_method](https://w3id.org/MONet/analysis-api-schema/modification_method)
Alias: modification_method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiologicalEntity](BiologicalEntity.md) | Reference data representing a biological identity (strain, isolate, |  yes  |







## Properties

* Range: [ModificationMethodEnum](ModificationMethodEnum.md)



## Aliases


* genetic_modification_method
* transformation_method



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:modification_method |
| native | analysis_api_schema:modification_method |




## LinkML Source

<details>
```yaml
name: modification_method
description: 'Select the method used to insert your construct into the genome of

  your modified organism. Examples: "Electroporation", "Conjugation", "CRISPR", "Transduction"'
title: modification method
from_schema: https://w3id.org/MONet/analysis-api-schema
aliases:
- genetic_modification_method
- transformation_method
rank: 1000
alias: modification_method
domain_of:
- biological_entity
range: ModificationMethodEnum

```
</details>