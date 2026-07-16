

# Slot: temperature exposure (temperature_exposure) 


_The range of temperatures at which it is safe to store a label that has been applied to a substrate. Provided by iMet_





URI: [analysis_api_schema:temperature_exposure](https://w3id.org/MONet/analysis-api-schema/temperature_exposure)
Alias: temperature_exposure

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AerosolSample](AerosolSample.md), [OtherUndescribedSample](OtherUndescribedSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:temperature_exposure |
| native | analysis_api_schema:temperature_exposure |




## LinkML Source

<details>
```yaml
name: temperature_exposure
description: The range of temperatures at which it is safe to store a label that has
  been applied to a substrate. Provided by iMet
title: temperature exposure
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: temperature_exposure
domain_of:
- AerosolSample
- OtherUndescribedSample
range: string

```
</details>