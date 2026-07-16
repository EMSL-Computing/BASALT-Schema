

# Slot: porosity (porosity) 


_Porosity of deposited sediment is volume of voids divided by the total volume of sample. (Unit: percent)_





URI: [analysis_api_schema:porosity](https://w3id.org/MONet/analysis-api-schema/porosity)
Alias: porosity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*percent$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:porosity |
| native | analysis_api_schema:porosity |




## LinkML Source

<details>
```yaml
name: porosity
description: 'Porosity of deposited sediment is volume of voids divided by the total
  volume of sample. (Unit: percent)'
title: porosity
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: porosity
domain_of:
- OtherUndescribedSample
- SedimentSample
range: string
pattern: ^\d+(\.\d+)?\s*percent$

```
</details>