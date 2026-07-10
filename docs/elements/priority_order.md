

# Slot: priority order (priority_order) 


_Indicate the run order priority of your samples_





URI: [analysis_api_schema:priority_order](https://w3id.org/MONet/analysis-api-schema/priority_order)
Alias: priority_order

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |







## Properties

* Range: [Float](Float.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:priority_order |
| native | analysis_api_schema:priority_order |




## LinkML Source

<details>
```yaml
name: priority_order
description: Indicate the run order priority of your samples
title: priority order
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: priority_order
domain_of:
- AerosolArmSample
- AerosolSample
- OtherUndescribedSample
range: float

```
</details>