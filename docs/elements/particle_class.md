

# Slot: particle class (particle_class) 


_Particles are classified based on their size into six general categories: clay, silt, sand, gravel, cobbles, and boulders. Include amount of particle with units preceded by the name of the particle type; can include multiple values separated by ';'._





URI: [analysis_api_schema:particle_class](https://w3id.org/MONet/analysis-api-schema/particle_class)
Alias: particle_class

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:particle_class |
| native | analysis_api_schema:particle_class |




## LinkML Source

<details>
```yaml
name: particle_class
description: 'Particles are classified based on their size into six general categories:
  clay, silt, sand, gravel, cobbles, and boulders. Include amount of particle with
  units preceded by the name of the particle type; can include multiple values separated
  by '';''.'
title: particle class
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: particle_class
domain_of:
- OtherUndescribedSample
- SedimentSample
range: string

```
</details>