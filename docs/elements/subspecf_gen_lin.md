

# Slot: subspecific genetic lineage (subspecf_gen_lin) 


_Information about the genetic distinctness of the sequenced organism below the subspecies level, e.g. serovar, serotype, biotype, ecotype, or any relevant genetic typing schemes like Group I plasmid. Supply both the lineage name and the lineage rank separated by a colon, e.g. biovar:abc123_





URI: [basalt_schema:subspecf_gen_lin](https://EMSL-Computing.github.io/basalt-schema/subspecf_gen_lin)
Alias: subspecf_gen_lin

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  yes  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  yes  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [CultureEnvironmentalSample](CultureEnvironmentalSample.md), [MixedCultureSample](MixedCultureSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [PureCultureSample](PureCultureSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |








## TODOs

* make this inlined/multivalued?



## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:subspecf_gen_lin |
| native | basalt_schema:subspecf_gen_lin |




## LinkML Source

<details>
```yaml
name: subspecf_gen_lin
description: Information about the genetic distinctness of the sequenced organism
  below the subspecies level, e.g. serovar, serotype, biotype, ecotype, or any relevant
  genetic typing schemes like Group I plasmid. Supply both the lineage name and the
  lineage rank separated by a colon, e.g. biovar:abc123
title: subspecific genetic lineage
todos:
- make this inlined/multivalued?
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: subspecf_gen_lin
domain_of:
- CultureEnvironmentalSample
- MixedCultureSample
- OtherUndescribedSample
- PureCultureSample
range: string

```
</details>