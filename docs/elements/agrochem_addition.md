

# Slot: agrochemical additions (agrochem_addition) 



URI: [analysis_api_schema:agrochem_addition](https://w3id.org/MONet/analysis-api-schema/agrochem_addition)
Alias: agrochem_addition

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [MonetSoilSample](MonetSoilSample.md) | A soil sample that has been collected according to the MONet soil sampling pr... |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:agrochem_addition |
| native | analysis_api_schema:agrochem_addition |




## LinkML Source

<details>
```yaml
name: agrochem_addition
title: agrochemical additions
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: agrochem_addition
domain_of:
- MonetSoilSample
- OtherUndescribedSample
- SoilSample
range: string

```
</details>