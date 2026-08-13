

# Slot: phospholipid fatty acid (phosplipid_fatt_acid) 


_Concentration of phospholipid fatty acids; can include multiple values separated by `;`. Provide the phospholipid fatty acids followed by the measurement value ({phospholipid fatty acid name}{value} {unit})_





URI: [basalt_schema:phosplipid_fatt_acid](https://EMSL-Computing.github.io/BASALT-Schema/phosplipid_fatt_acid)
Alias: phosplipid_fatt_acid

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |






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


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:phosplipid_fatt_acid |
| native | basalt_schema:phosplipid_fatt_acid |




## LinkML Source

<details>
```yaml
name: phosplipid_fatt_acid
description: Concentration of phospholipid fatty acids; can include multiple values
  separated by `;`. Provide the phospholipid fatty acids followed by the measurement
  value ({phospholipid fatty acid name}{value} {unit})
title: phospholipid fatty acid
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: phosplipid_fatt_acid
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string

```
</details>