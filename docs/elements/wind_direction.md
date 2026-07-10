

# Slot: wind direction (wind_direction) 


_Direction of the wind on the day of sampling. Collected via anemometer. Provide cardinal direction._





URI: [analysis_api_schema:wind_direction](https://w3id.org/MONet/analysis-api-schema/wind_direction)
Alias: wind_direction

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AerosolSamplingActivity](AerosolSamplingActivity.md) | A sampling activity where aerosol samples were collected |  no  |
| [SoilSamplingActivity](SoilSamplingActivity.md) | Collection of soil samples from the environment |  no  |
| [OtherUndescribedSamplingActivity](OtherUndescribedSamplingActivity.md) | Collection of samples from source that does not fit into any of the other cat... |  no  |







## Properties

* Range: [CardinalDirectionEnum](CardinalDirectionEnum.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:wind_direction |
| native | analysis_api_schema:wind_direction |




## LinkML Source

<details>
```yaml
name: wind_direction
description: Direction of the wind on the day of sampling. Collected via anemometer.
  Provide cardinal direction.
title: wind direction
from_schema: https://w3id.org/MONet/analysis-api-schema
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