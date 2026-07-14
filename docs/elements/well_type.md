

# Slot: well_type 


_Role of this well   "sample", "blank", "uninoculated_control", "standard"_





URI: [analysis_api_schema:well_type](https://w3id.org/MONet/analysis-api-schema/well_type)
Alias: well_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EcoplateWellMetadata](EcoplateWellMetadata.md) | Ecoplate-specific per-well metadata |  no  |
| [AMP2WellMetadata](AMP2WellMetadata.md) | AMP2-specific per-well metadata |  no  |
| [WellMetadata](WellMetadata.md) | Base structure for per-well metadata in plate setup |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:well_type |
| native | analysis_api_schema:well_type |




## LinkML Source

<details>
```yaml
name: well_type
description: Role of this well   "sample", "blank", "uninoculated_control", "standard"
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: well_type
owner: WellMetadata
domain_of:
- WellMetadata
range: string

```
</details>