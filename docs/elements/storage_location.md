

# Slot: storage_location 


_The physical or digital location where the processed sample is stored (e.g., freezer location, database ID)._





URI: [basalt_schema:storage_location](https://w3id.org/MONet/basalt-schema/storage_location)
Alias: storage_location

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProcessedSample](ProcessedSample.md) | A sample that has undergone processing or analysis |  no  |
| [CoreSection](CoreSection.md) | A section of a core sample (TOP, MID, BTM) |  no  |






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


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:storage_location |
| native | basalt_schema:storage_location |




## LinkML Source

<details>
```yaml
name: storage_location
description: The physical or digital location where the processed sample is stored
  (e.g., freezer location, database ID).
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: storage_location
domain_of:
- ProcessedSample
range: string

```
</details>