

# Slot: wind speed (wind_speed) 


_Wind speed describes how fast the air is moving past a certain point during sampling time. Collected via anemometer. Provide value and unit, any unit is valid._





URI: [basalt_schema:wind_speed](https://w3id.org/MONet/basalt-schema/wind_speed)
Alias: wind_speed

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AerosolSamplingActivity](AerosolSamplingActivity.md) | A sampling activity where aerosol samples were collected |  no  |
| [OtherUndescribedSamplingActivity](OtherUndescribedSamplingActivity.md) | Collection of samples from source that does not fit into any of the other cat... |  no  |






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


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:wind_speed |
| native | basalt_schema:wind_speed |




## LinkML Source

<details>
```yaml
name: wind_speed
description: Wind speed describes how fast the air is moving past a certain point
  during sampling time. Collected via anemometer. Provide value and unit, any unit
  is valid.
title: wind speed
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: wind_speed
domain_of:
- AerosolSamplingActivity
- OtherUndescribedSamplingActivity
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>