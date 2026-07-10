

# Slot: second infiltration time (infiltration_2) 


_Amount of time it takes to accomplish the second infiltration activity. If infiltration time was started and unsuccessful enter 'failed' if infiltration time was not attempted enter 'did not collect'. Units and format of mm:ss required. (Example: 15:20 mm:ss)_





URI: [analysis_api_schema:infiltration_2](https://w3id.org/MONet/analysis-api-schema/infiltration_2)
Alias: infiltration_2

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilSamplingActivity](SoilSamplingActivity.md) | Collection of soil samples from the environment |  no  |
| [MonetSoilSamplingActivity](MonetSoilSamplingActivity.md) | Collection of soil cores according to the MONet soil sampling protocol |  yes  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^((0[0-9]|[1-5][0-9]):([0-5][0-9])\smm:ss|did not collect|failed)`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:infiltration_2 |
| native | analysis_api_schema:infiltration_2 |




## LinkML Source

<details>
```yaml
name: infiltration_2
description: 'Amount of time it takes to accomplish the second infiltration activity.
  If infiltration time was started and unsuccessful enter ''failed'' if infiltration
  time was not attempted enter ''did not collect''. Units and format of mm:ss required.
  (Example: 15:20 mm:ss)'
title: second infiltration time
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: infiltration_2
domain_of:
- MonetSoilSamplingActivity
- SoilSamplingActivity
range: string
pattern: ^((0[0-9]|[1-5][0-9]):([0-5][0-9])\smm:ss|did not collect|failed)

```
</details>