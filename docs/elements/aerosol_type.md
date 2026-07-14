

# Slot: aerosol_type 


_The type or method of aerosol collection_





URI: [analysis_api_schema:aerosol_type](https://w3id.org/MONet/analysis-api-schema/aerosol_type)
Alias: aerosol_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |







## Properties

* Range: [AerosolTypeEnum](AerosolTypeEnum.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:aerosol_type |
| native | analysis_api_schema:aerosol_type |




## LinkML Source

<details>
```yaml
name: aerosol_type
description: The type or method of aerosol collection
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: aerosol_type
domain_of:
- AerosolArmSample
- AerosolSample
range: AerosolTypeEnum
required: true

```
</details>