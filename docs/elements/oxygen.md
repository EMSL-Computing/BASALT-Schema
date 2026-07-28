

# Slot: oxygen (oxygen) 


_Amount of oxygen measured in the air the day of sampling. (Unit: mg/L or ppm)_





URI: [analysis_api_schema:oxygen](https://w3id.org/MONet/analysis-api-schema/oxygen)
Alias: oxygen

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AerosolSample](AerosolSample.md), [OtherUndescribedSample](OtherUndescribedSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*(mg/L|ppm)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:oxygen |
| native | analysis_api_schema:oxygen |




## LinkML Source

<details>
```yaml
name: oxygen
description: 'Amount of oxygen measured in the air the day of sampling. (Unit: mg/L
  or ppm)'
title: oxygen
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: oxygen
domain_of:
- AerosolSample
- OtherUndescribedSample
range: string
pattern: ^\d+(\.\d+)?\s*(mg/L|ppm)$

```
</details>