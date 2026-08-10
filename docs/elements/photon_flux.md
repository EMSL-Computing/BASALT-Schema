

# Slot: photon flux (photon_flux) 


_Measurement of photon flux. Provide value and unit, any unit is valid._





URI: [basalt_schema:photon_flux](https://w3id.org/MONet/basalt-schema/photon_flux)
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


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:photon_flux |
| native | basalt_schema:photon_flux |




## LinkML Source

<details>
```yaml
name: photon_flux
description: Measurement of photon flux. Provide value and unit, any unit is valid.
title: photon flux
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: photon_flux
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>