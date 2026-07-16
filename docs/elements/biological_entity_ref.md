

# Slot: biological_entity_ref 


_FK reference to a biological_entity representing the biological identity_

_strain, isolate, engineered construct) that this sample or activity_

_is associated with._





URI: [analysis_api_schema:biological_entity_ref](https://w3id.org/MONet/analysis-api-schema/biological_entity_ref)
Alias: biological_entity_ref

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StockCulturePreparation](StockCulturePreparation.md) | Preparation of a stock culture from user samples for long-term storage |  no  |
| [AMP2UserSample](AMP2UserSample.md) | A user-submitted microbial sample for AMP2 workflows |  yes  |
| [StrainPurity](StrainPurity.md) | Purity check of a strain culture |  no  |
| [ExperimentalCulture](ExperimentalCulture.md) | Growth of an experimental culture for downstream analysis |  no  |
| [EngineeredStrainSample](EngineeredStrainSample.md) | A sample containing a strain of an organism that has been subjected to geneti... |  no  |
| [CultureGrowth](CultureGrowth.md) | Abstract activity for growing cultures from samples or other cultures |  no  |
| [PreCultureGrowth](PreCultureGrowth.md) | Growth of a pre-culture to establish viable inoculum before |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BiologicalEntity](BiologicalEntity.md) |
| Domain Of | [CultureGrowth](CultureGrowth.md), [AMP2UserSample](AMP2UserSample.md), [EngineeredStrainSample](EngineeredStrainSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |







## Aliases


* strain_ref
* strain_id




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:biological_entity_ref |
| native | analysis_api_schema:biological_entity_ref |




## LinkML Source

<details>
```yaml
name: biological_entity_ref
description: 'FK reference to a biological_entity representing the biological identity

  strain, isolate, engineered construct) that this sample or activity

  is associated with.'
from_schema: https://w3id.org/MONet/analysis-api-schema
aliases:
- strain_ref
- strain_id
rank: 1000
alias: biological_entity_ref
domain_of:
- CultureGrowth
- AMP2UserSample
- EngineeredStrainSample
range: biological_entity
required: false

```
</details>