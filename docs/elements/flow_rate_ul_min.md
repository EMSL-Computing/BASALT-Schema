

# Slot: flow rate (uL/min) (flow_rate_ul_min) 


_Flow rate of the mobile phase, in microliters per minute._





URI: [basalt_schema:flow_rate_ul_min](https://EMSL-Computing.github.io/BASALT-Schema/flow_rate_ul_min)
Alias: flow_rate_ul_min

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChromatographyConfiguration](ChromatographyConfiguration.md) | Configuration and settings for a chromatography run |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [ChromatographyConfiguration](ChromatographyConfiguration.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:flow_rate_ul_min |
| native | basalt_schema:flow_rate_ul_min |




## LinkML Source

<details>
```yaml
name: flow_rate_ul_min
description: Flow rate of the mobile phase, in microliters per minute.
title: flow rate (uL/min)
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: flow_rate_ul_min
domain_of:
- ChromatographyConfiguration
range: float

```
</details>