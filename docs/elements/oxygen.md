

# Slot: oxygen (oxygen) 


_Amount of oxygen measured in the air the day of sampling. (Unit: mg/L or ppm)_





URI: [basalt_schema:oxygen](https://EMSL-Computing.github.io/BASALT-Schema/oxygen)
Alias: oxygen

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  yes  |
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
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*(mg/L|ppm)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:oxygen |
| native | basalt_schema:oxygen |




## LinkML Source

<details>
```yaml
name: oxygen
description: 'Amount of oxygen measured in the air the day of sampling. (Unit: mg/L
  or ppm)'
title: oxygen
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: oxygen
domain_of:
- AerosolSample
- OtherUndescribedSample
range: string
pattern: ^\d+(\.\d+)?\s*(mg/L|ppm)$

```
</details>