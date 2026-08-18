

# Slot: LIMS ID (lims_id) 


_An EMSL internal LIMS identifier for your sample. This will be provided by the MPOC and should not be edited._





URI: [basalt_schema:lims_id](https://emsl-computing.github.io/BASALT-Schema/elements/lims_id)
Alias: lims_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MonetSoilSample](MonetSoilSample.md) | A soil sample that has been collected according to the MONet soil sampling pr... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MonetSoilSample](MonetSoilSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^INGEST_SAMPLE_\d{9}$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:lims_id |
| native | basalt_schema:lims_id |




## LinkML Source

<details>
```yaml
name: lims_id
description: An EMSL internal LIMS identifier for your sample. This will be provided
  by the MPOC and should not be edited.
title: LIMS ID
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: lims_id
domain_of:
- MonetSoilSample
range: string
pattern: ^INGEST_SAMPLE_\d{9}$

```
</details>