

# Slot: commercial_media_catalog 


_Reference to commercial media catalog entry if applicable._

_Required if media_formulation is 'commercial', otherwise null._





URI: [analysis_api_schema:commercial_media_catalog](https://w3id.org/MONet/analysis-api-schema/commercial_media_catalog)
Alias: commercial_media_catalog

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaPreparation](MediaPreparation.md) | Activity that prepares a batch of growth media |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MediaPreparation](MediaPreparation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:commercial_media_catalog |
| native | analysis_api_schema:commercial_media_catalog |




## LinkML Source

<details>
```yaml
name: commercial_media_catalog
description: 'Reference to commercial media catalog entry if applicable.

  Required if media_formulation is ''commercial'', otherwise null.'
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: commercial_media_catalog
domain_of:
- MediaPreparation
range: string

```
</details>