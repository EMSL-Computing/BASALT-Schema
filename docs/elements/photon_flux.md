

# Slot: photon flux (photon_flux) 


_Measurement of photon flux. Provide value and unit, any unit is valid._





URI: [analysis_api_schema:photon_flux](https://w3id.org/MONet/analysis-api-schema/photon_flux)
Alias: photon_flux

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*[\w\s/]+$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:photon_flux |
| native | analysis_api_schema:photon_flux |




## LinkML Source

<details>
```yaml
name: photon_flux
description: Measurement of photon flux. Provide value and unit, any unit is valid.
title: photon flux
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: photon_flux
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>