

# Slot: humidity (humidity) 


_Amount of water vapor measured in the air the day of sampling. Provide value and unit, any unit is valid_





URI: [basalt_schema:humidity](https://emsl-computing.github.io/BASALT-Schema/elements/humidity)
Alias: humidity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AerosolSamplingActivity](AerosolSamplingActivity.md) | A sampling activity where aerosol samples were collected |  no  |
| [OtherUndescribedSamplingActivity](OtherUndescribedSamplingActivity.md) | Collection of samples from source that does not fit into any of the other cat... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AerosolSamplingActivity](AerosolSamplingActivity.md), [OtherUndescribedSamplingActivity](OtherUndescribedSamplingActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*[\w\s/]+$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:humidity |
| native | basalt_schema:humidity |




## LinkML Source

<details>
```yaml
name: humidity
description: Amount of water vapor measured in the air the day of sampling. Provide
  value and unit, any unit is valid
title: humidity
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: humidity
domain_of:
- AerosolSamplingActivity
- OtherUndescribedSamplingActivity
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>