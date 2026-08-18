

# Slot: sieving (sieving) 


_Collection design of pooled samples and/or sieve size and amount of sample sieved_





URI: [basalt_schema:sieving](https://emsl-computing.github.io/BASALT-Schema/elements/sieving)
Alias: sieving

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






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


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:sieving |
| native | basalt_schema:sieving |




## LinkML Source

<details>
```yaml
name: sieving
description: Collection design of pooled samples and/or sieve size and amount of sample
  sieved
title: sieving
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: sieving
domain_of:
- OtherUndescribedSample
- SedimentSample
- SoilSample
range: string

```
</details>