

# Slot: volatile organic compounds (volatile_org_comp) 


_Volatile organic compounds are organic chemicals that have a high vapour pressure at room temperature._





URI: [analysis_api_schema:volatile_org_comp](https://w3id.org/MONet/analysis-api-schema/volatile_org_comp)
Alias: volatile_org_comp

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:volatile_org_comp |
| native | analysis_api_schema:volatile_org_comp |




## LinkML Source

<details>
```yaml
name: volatile_org_comp
description: Volatile organic compounds are organic chemicals that have a high vapour
  pressure at room temperature.
title: volatile organic compounds
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: volatile_org_comp
domain_of:
- AerosolArmSample
- AerosolSample
- OtherUndescribedSample
range: string

```
</details>