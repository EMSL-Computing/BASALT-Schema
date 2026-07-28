

# Slot: growth facility (growth_facil) 


_Type of facility or location from where the sample was collected or_

_grown. This field is NOT multivalued. If selecting other, add the `other_growth_facil`_

_attribute to provide additional detail._





URI: [analysis_api_schema:growth_facil](https://w3id.org/MONet/analysis-api-schema/growth_facil)
Alias: growth_facil

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AMP2UserSample](AMP2UserSample.md) | A user-submitted microbial sample for AMP2 workflows |  no  |
| [Site](Site.md) | Site-level metadata for a specific location from which a set of samples are c... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GrowthFacilityEnum](GrowthFacilityEnum.md) |
| Domain Of | [Site](Site.md), [AMP2UserSample](AMP2UserSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:growth_facil |
| native | analysis_api_schema:growth_facil |




## LinkML Source

<details>
```yaml
name: growth_facil
description: 'Type of facility or location from where the sample was collected or

  grown. This field is NOT multivalued. If selecting other, add the `other_growth_facil`

  attribute to provide additional detail.'
title: growth facility
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: growth_facil
domain_of:
- Site
- AMP2UserSample
range: GrowthFacilityEnum

```
</details>