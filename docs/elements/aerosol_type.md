

# Slot: aerosol_type 


_The type or method of aerosol collection_





URI: [basalt_schema:aerosol_type](https://EMSL-Computing.github.io/basalt-schema/aerosol_type)
Alias: aerosol_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AerosolTypeEnum](AerosolTypeEnum.md) |
| Domain Of | [AerosolArmSample](AerosolArmSample.md), [AerosolSample](AerosolSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:aerosol_type |
| native | basalt_schema:aerosol_type |




## LinkML Source

<details>
```yaml
name: aerosol_type
description: The type or method of aerosol collection
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: aerosol_type
domain_of:
- AerosolArmSample
- AerosolSample
range: AerosolTypeEnum
required: true

```
</details>