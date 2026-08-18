

# Slot: value 


_Measured value (absorbance, OD, fluorescence)_





URI: [basalt_schema:value](https://EMSL-Computing.github.io/BASALT-Schema/value)
Alias: value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WellReading](WellReading.md) | Per-well measurement data |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [WellReading](WellReading.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [WellReading](WellReading.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:value |
| native | basalt_schema:value |




## LinkML Source

<details>
```yaml
name: value
description: Measured value (absorbance, OD, fluorescence)
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: value
owner: WellReading
domain_of:
- WellReading
range: float
required: true

```
</details>