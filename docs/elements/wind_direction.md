

# Slot: wind direction (wind_direction) 


_Direction of the wind on the day of sampling. Collected via anemometer. Provide cardinal direction._





URI: [basalt_schema:wind_direction](https://EMSL-Computing.github.io/basalt-schema/wind_direction)
Alias: wind_direction

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSamplingActivity](OtherUndescribedSamplingActivity.md) | Collection of samples from source that does not fit into any of the other cat... |  no  |
| [SoilSamplingActivity](SoilSamplingActivity.md) | Collection of soil samples from the environment |  no  |
| [AerosolSamplingActivity](AerosolSamplingActivity.md) | A sampling activity where aerosol samples were collected |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CardinalDirectionEnum](CardinalDirectionEnum.md) |
| Domain Of | [AerosolSamplingActivity](AerosolSamplingActivity.md), [OtherUndescribedSamplingActivity](OtherUndescribedSamplingActivity.md), [SoilSamplingActivity](SoilSamplingActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:wind_direction |
| native | basalt_schema:wind_direction |




## LinkML Source

<details>
```yaml
name: wind_direction
description: Direction of the wind on the day of sampling. Collected via anemometer.
  Provide cardinal direction.
title: wind direction
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: wind_direction
domain_of:
- AerosolSamplingActivity
- OtherUndescribedSamplingActivity
- SoilSamplingActivity
range: CardinalDirectionEnum
required: false

```
</details>