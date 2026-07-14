

# Slot: replicate_group 


_Identifier linking technical replicates (e.g. "rep1", "rep2")_





URI: [analysis_api_schema:replicate_group](https://w3id.org/MONet/analysis-api-schema/replicate_group)
Alias: replicate_group

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
| self | analysis_api_schema:replicate_group |
| native | analysis_api_schema:replicate_group |




## LinkML Source

<details>
```yaml
name: replicate_group
description: Identifier linking technical replicates (e.g. "rep1", "rep2")
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: replicate_group
owner: WellMetadata
domain_of:
- WellMetadata
range: string

```
</details>