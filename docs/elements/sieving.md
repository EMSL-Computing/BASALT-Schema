

# Slot: sieving (sieving) 


_Collection design of pooled samples and/or sieve size and amount of sample sieved_





URI: [analysis_api_schema:sieving](https://w3id.org/MONet/analysis-api-schema/sieving)
Alias: sieving

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:sieving |
| native | analysis_api_schema:sieving |




## LinkML Source

<details>
```yaml
name: sieving
description: Collection design of pooled samples and/or sieve size and amount of sample
  sieved
title: sieving
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: sieving
domain_of:
- OtherUndescribedSample
- SedimentSample
- SoilSample
range: string

```
</details>