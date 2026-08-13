

# Slot: link to additional analysis (link_addit_analys) 


_Link to additional analysis results performed on the sample_





URI: [basalt_schema:link_addit_analys](https://EMSL-Computing.github.io/basalt-schema/link_addit_analys)
Alias: link_addit_analys

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [SoilSample](SoilSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:link_addit_analys |
| native | basalt_schema:link_addit_analys |




## LinkML Source

<details>
```yaml
name: link_addit_analys
description: Link to additional analysis results performed on the sample
title: link to additional analysis
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: link_addit_analys
domain_of:
- OtherUndescribedSample
- SoilSample
range: string

```
</details>