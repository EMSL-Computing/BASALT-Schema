

# Slot: contaminant_strains 


_Known or detected contaminant strains (if any)_





URI: [analysis_api_schema:contaminant_strains](https://w3id.org/MONet/analysis-api-schema/contaminant_strains)
Alias: contaminant_strains

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StrainPurity](StrainPurity.md) | Purity check of a strain culture |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [StrainPurity](StrainPurity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:contaminant_strains |
| native | analysis_api_schema:contaminant_strains |




## LinkML Source

<details>
```yaml
name: contaminant_strains
description: Known or detected contaminant strains (if any)
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: contaminant_strains
domain_of:
- StrainPurity
range: string

```
</details>