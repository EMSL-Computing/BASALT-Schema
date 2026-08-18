

# Slot: heavy metals (heavy_metals) 


_Heavy metals present and concentrations; can include multiple heavy metals and concentrations_





URI: [basalt_schema:heavy_metals](https://emsl-computing.github.io/BASALT-Schema/elements/heavy_metals)
Alias: heavy_metals

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  yes  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






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


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:heavy_metals |
| native | basalt_schema:heavy_metals |




## LinkML Source

<details>
```yaml
name: heavy_metals
description: Heavy metals present and concentrations; can include multiple heavy metals
  and concentrations
title: heavy metals
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: heavy_metals
domain_of:
- OtherUndescribedSample
- SoilSample
range: string

```
</details>