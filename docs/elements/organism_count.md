

# Slot: organism count (organism_count) 


_Total cell count of any organism (or group of organisms) per gram volume or area of sample, should include name of organism followed by count. The method that was used for the enumeration (e.g. qPCR atp mpn etc.) should also be provided. (example: total prokaryotes; 3.5e7 cells per ml; qpcr)_





URI: [analysis_api_schema:organism_count](https://w3id.org/MONet/analysis-api-schema/organism_count)
Alias: organism_count

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:organism_count |
| native | analysis_api_schema:organism_count |




## LinkML Source

<details>
```yaml
name: organism_count
description: 'Total cell count of any organism (or group of organisms) per gram volume
  or area of sample, should include name of organism followed by count. The method
  that was used for the enumeration (e.g. qPCR atp mpn etc.) should also be provided.
  (example: total prokaryotes; 3.5e7 cells per ml; qpcr)'
title: organism count
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: organism_count
domain_of:
- OtherUndescribedSample
range: string

```
</details>