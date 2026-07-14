

# Slot: subspecific genetic lineage (subspecf_gen_lin) 


_Information about the genetic distinctness of the sequenced organism below the subspecies level, e.g. serovar, serotype, biotype, ecotype, or any relevant genetic typing schemes like Group I plasmid. Supply both the lineage name and the lineage rank separated by a colon, e.g. biovar:abc123_





URI: [analysis_api_schema:subspecf_gen_lin](https://w3id.org/MONet/analysis-api-schema/subspecf_gen_lin)
Alias: subspecf_gen_lin

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  yes  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  yes  |







## Properties

* Range: [String](String.md)





## TODOs

* make this inlined/multivalued?

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:subspecf_gen_lin |
| native | analysis_api_schema:subspecf_gen_lin |




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
from_schema: https://w3id.org/MONet/analysis-api-schema
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