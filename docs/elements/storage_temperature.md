

# Slot: storage_temperature 


_Storage temperature for the sample (e.g., "-80 C", "4 C")._





URI: [analysis_api_schema:storage_temperature](https://w3id.org/MONet/analysis-api-schema/storage_temperature)
Alias: storage_temperature

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaPreparation](MediaPreparation.md) | Activity that prepares a batch of growth media |  no  |
| [AMP2UserSample](AMP2UserSample.md) | A user-submitted microbial sample for AMP2 workflows |  yes  |
| [EngineeredStrainSample](EngineeredStrainSample.md) | A sample containing a strain of an organism that has been subjected to geneti... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MediaPreparation](MediaPreparation.md), [AMP2UserSample](AMP2UserSample.md), [EngineeredStrainSample](EngineeredStrainSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:storage_temperature |
| native | analysis_api_schema:storage_temperature |




## LinkML Source

<details>
```yaml
name: storage_temperature
description: Storage temperature for the sample (e.g., "-80 C", "4 C").
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: storage_temperature
domain_of:
- MediaPreparation
- AMP2UserSample
- EngineeredStrainSample
range: string

```
</details>