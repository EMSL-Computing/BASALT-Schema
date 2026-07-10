

# Slot: first cloud base height (first_cbh) 


_First cloud base (meters) or vertical visibility (meters) (-999 if no cloud base or vertical visibility) (Unit: m)_





URI: [analysis_api_schema:first_cbh](https://w3id.org/MONet/analysis-api-schema/first_cbh)
Alias: first_cbh

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
| self | analysis_api_schema:first_cbh |
| native | analysis_api_schema:first_cbh |




## LinkML Source

<details>
```yaml
name: first_cbh
description: 'First cloud base (meters) or vertical visibility (meters) (-999 if no
  cloud base or vertical visibility) (Unit: m)'
title: first cloud base height
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: first_cbh
domain_of:
- AerosolArmSample
range: float

```
</details>