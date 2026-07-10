

# Slot: sampling duration (sampling_duration) 


_The difference between sample start and sample end time in seconds. (Unit: s)_





URI: [analysis_api_schema:sampling_duration](https://w3id.org/MONet/analysis-api-schema/sampling_duration)
Alias: sampling_duration

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AerosolSamplingActivity](AerosolSamplingActivity.md) | A sampling activity where aerosol samples were collected |  no  |
| [OtherUndescribedSamplingActivity](OtherUndescribedSamplingActivity.md) | Collection of samples from source that does not fit into any of the other cat... |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*s$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:sampling_duration |
| native | analysis_api_schema:sampling_duration |




## LinkML Source

<details>
```yaml
name: sampling_duration
description: 'The difference between sample start and sample end time in seconds.
  (Unit: s)'
title: sampling duration
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: sampling_duration
domain_of:
- AerosolSamplingActivity
- OtherUndescribedSamplingActivity
range: string
pattern: ^\d+(\.\d+)?\s*s$

```
</details>