

# Slot: plant taxonomy identifier (plant_taxid) 


_NCBI taxon ID of the plant from https://www.ncbi.nlm.nih.gov/taxonomy_





URI: [basalt_schema:plant_taxid](https://EMSL-Computing.github.io/BASALT-Schema/plant_taxid)
Alias: plant_taxid

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSample](PlantSample.md) | A sample containing plant material |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PlantSample](PlantSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:plant_taxid |
| native | basalt_schema:plant_taxid |




## LinkML Source

<details>
```yaml
name: plant_taxid
description: NCBI taxon ID of the plant from https://www.ncbi.nlm.nih.gov/taxonomy
title: plant taxonomy identifier
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: plant_taxid
domain_of:
- PlantSample
range: string

```
</details>