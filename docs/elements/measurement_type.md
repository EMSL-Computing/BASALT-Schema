

# Slot: measurement_type 


_Type of plate measurement (optical_density, fluorescence, flow_cytometry)_





URI: [basalt_schema:measurement_type](https://EMSL-Computing.github.io/BASALT-Schema/measurement_type)
Alias: measurement_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AMP2DataGenerationActivity](AMP2DataGenerationActivity.md) | AMP2 plate measurement (OD, fluorescence, flow cytometry) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AMP2DataGenerationActivity](AMP2DataGenerationActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:measurement_type |
| native | basalt_schema:measurement_type |




## LinkML Source

<details>
```yaml
name: measurement_type
description: Type of plate measurement (optical_density, fluorescence, flow_cytometry)
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: measurement_type
domain_of:
- AMP2DataGenerationActivity
range: string

```
</details>