

# Slot: second cloud base height (second_cbh) 


_Second cloud base (meters) or highest received signal in vertical visibility (meters) (-999 if no cloud base or vertical visibility) (Unit: m)_





URI: [analysis_api_schema:second_cbh](https://w3id.org/MONet/analysis-api-schema/second_cbh)
Alias: second_cbh

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |







## Properties

* Range: [Float](Float.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:second_cbh |
| native | analysis_api_schema:second_cbh |




## LinkML Source

<details>
```yaml
name: second_cbh
description: 'Second cloud base (meters) or highest received signal in vertical visibility
  (meters) (-999 if no cloud base or vertical visibility) (Unit: m)'
title: second cloud base height
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: second_cbh
domain_of:
- AerosolArmSample
range: float

```
</details>