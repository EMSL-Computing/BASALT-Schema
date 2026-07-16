

# Slot: phospholipid fatty acid (phosplipid_fatt_acid) 


_Concentration of phospholipid fatty acids; can include multiple values separated by `;`. Provide the phospholipid fatty acids followed by the measurement value ({phospholipid fatty acid name}{value} {unit})_





URI: [analysis_api_schema:phosplipid_fatt_acid](https://w3id.org/MONet/analysis-api-schema/phosplipid_fatt_acid)
Alias: phosplipid_fatt_acid

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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:phosplipid_fatt_acid |
| native | analysis_api_schema:phosplipid_fatt_acid |




## LinkML Source

<details>
```yaml
name: phosplipid_fatt_acid
description: Concentration of phospholipid fatty acids; can include multiple values
  separated by `;`. Provide the phospholipid fatty acids followed by the measurement
  value ({phospholipid fatty acid name}{value} {unit})
title: phospholipid fatty acid
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: phosplipid_fatt_acid
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string

```
</details>