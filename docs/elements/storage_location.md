

# Slot: storage_location 


_The physical or digital location where the processed sample is stored (e.g., freezer location, database ID)._





URI: [analysis_api_schema:storage_location](https://w3id.org/MONet/analysis-api-schema/storage_location)
Alias: storage_location

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CoreSection](CoreSection.md) | A section of a core sample (TOP, MID, BTM) |  no  |
| [ProcessedSample](ProcessedSample.md) | A sample that has undergone processing or analysis |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ProcessedSample](ProcessedSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:storage_location |
| native | analysis_api_schema:storage_location |




## LinkML Source

<details>
```yaml
name: storage_location
description: The physical or digital location where the processed sample is stored
  (e.g., freezer location, database ID).
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: storage_location
domain_of:
- ProcessedSample
range: string

```
</details>