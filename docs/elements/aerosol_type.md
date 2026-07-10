

# Slot: aerosol_type 



URI: [analysis_api_schema:aerosol_type](https://w3id.org/MONet/analysis-api-schema/aerosol_type)
Alias: aerosol_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |







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