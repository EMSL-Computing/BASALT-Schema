

# Slot: antibiotic regimen (antibiotic_regm) 


_Information about treatment involving antibiotic administration; should include the name of antibiotic, amount administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple antibiotic regimens_





URI: [basalt_schema:antibiotic_regm](https://EMSL-Computing.github.io/BASALT-Schema/antibiotic_regm)
Alias: antibiotic_regm

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:antibiotic_regm |
| native | basalt_schema:antibiotic_regm |




## LinkML Source

<details>
```yaml
name: antibiotic_regm
description: Information about treatment involving antibiotic administration; should
  include the name of antibiotic, amount administered, treatment regimen including
  how many times the treatment was repeated, how long each treatment lasted, and the
  start and end time of the entire treatment; can include multiple antibiotic regimens
title: antibiotic regimen
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: antibiotic_regm
domain_of:
- OtherUndescribedSample
range: string

```
</details>