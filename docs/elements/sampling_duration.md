

# Slot: sampling duration (sampling_duration) 


_The difference between sample start and sample end time in seconds. (Unit: s)_





URI: [basalt_schema:sampling_duration](https://emsl-computing.github.io/BASALT-Schema/elements/sampling_duration)
Alias: sampling_duration

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
| Regex Pattern | `^\d+(\.\d+)?\s*s$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:sampling_duration |
| native | basalt_schema:sampling_duration |




## LinkML Source

<details>
```yaml
name: sampling_duration
description: 'The difference between sample start and sample end time in seconds.
  (Unit: s)'
title: sampling duration
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: sampling_duration
domain_of:
- AerosolSamplingActivity
- OtherUndescribedSamplingActivity
range: string
pattern: ^\d+(\.\d+)?\s*s$

```
</details>