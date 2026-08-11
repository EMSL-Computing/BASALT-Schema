

# Slot: organic nitrogen method (org_nitro_method) 


_Method used for obtaining organic nitrogen_





URI: [basalt_schema:org_nitro_method](https://EMSL-Computing.github.io/basalt-schema/org_nitro_method)
Alias: org_nitro_method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:org_nitro_method |
| native | basalt_schema:org_nitro_method |




## LinkML Source

<details>
```yaml
name: org_nitro_method
description: Method used for obtaining organic nitrogen
title: organic nitrogen method
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: org_nitro_method
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string

```
</details>