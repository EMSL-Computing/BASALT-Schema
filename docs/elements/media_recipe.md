

# Slot: media_recipe 


_Reference or description of recipe used to prepare media._

_Examples: "M9 media with 1% Glucose", "rich media with 10% LB and 90% glycerol"_





URI: [analysis_api_schema:media_recipe](https://w3id.org/MONet/analysis-api-schema/media_recipe)
Alias: media_recipe

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
| self | analysis_api_schema:media_recipe |
| native | analysis_api_schema:media_recipe |




## LinkML Source

<details>
```yaml
name: media_recipe
description: 'Reference or description of recipe used to prepare media.

  Examples: "M9 media with 1% Glucose", "rich media with 10% LB and 90% glycerol"'
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: media_recipe
domain_of:
- MediaPreparation
range: string

```
</details>