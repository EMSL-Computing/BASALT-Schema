

# Slot: organism count (organism_count) 


_Total cell count of any organism (or group of organisms) per gram volume or area of sample, should include name of organism followed by count. The method that was used for the enumeration (e.g. qPCR atp mpn etc.) should also be provided. (example: total prokaryotes; 3.5e7 cells per ml; qpcr)_





URI: [basalt_schema:organism_count](https://EMSL-Computing.github.io/basalt-schema/organism_count)
Alias: organism_count

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


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:organism_count |
| native | basalt_schema:organism_count |




## LinkML Source

<details>
```yaml
name: organism_count
description: 'Total cell count of any organism (or group of organisms) per gram volume
  or area of sample, should include name of organism followed by count. The method
  that was used for the enumeration (e.g. qPCR atp mpn etc.) should also be provided.
  (example: total prokaryotes; 3.5e7 cells per ml; qpcr)'
title: organism count
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: organism_count
domain_of:
- OtherUndescribedSample
range: string

```
</details>