

# Slot: second infiltration time (infiltration_2) 


_Amount of time it takes to accomplish the second infiltration activity. If infiltration time was started and unsuccessful enter 'failed' if infiltration time was not attempted enter 'did not collect'. Units and format of mm:ss required. (Example: 15:20 mm:ss)_





URI: [basalt_schema:infiltration_2](https://EMSL-Computing.github.io/basalt-schema/infiltration_2)
Alias: infiltration_2

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MonetSoilSamplingActivity](MonetSoilSamplingActivity.md) | Collection of soil cores according to the MONet soil sampling protocol |  yes  |
| [SoilSamplingActivity](SoilSamplingActivity.md) | Collection of soil samples from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MonetSoilSamplingActivity](MonetSoilSamplingActivity.md), [SoilSamplingActivity](SoilSamplingActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^((0[0-9]|[1-5][0-9]):([0-5][0-9])\smm:ss|did not collect|failed)` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:infiltration_2 |
| native | basalt_schema:infiltration_2 |




## LinkML Source

<details>
```yaml
name: infiltration_2
description: 'Amount of time it takes to accomplish the second infiltration activity.
  If infiltration time was started and unsuccessful enter ''failed'' if infiltration
  time was not attempted enter ''did not collect''. Units and format of mm:ss required.
  (Example: 15:20 mm:ss)'
title: second infiltration time
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: infiltration_2
domain_of:
- MonetSoilSamplingActivity
- SoilSamplingActivity
range: string
pattern: ^((0[0-9]|[1-5][0-9]):([0-5][0-9])\smm:ss|did not collect|failed)

```
</details>