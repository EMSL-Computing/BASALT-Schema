

# Slot: volatile organic compounds (volatile_org_comp) 


_Volatile organic compounds are organic chemicals that have a high vapour pressure at room temperature._





URI: [basalt_schema:volatile_org_comp](https://w3id.org/MONet/basalt-schema/volatile_org_comp)
Alias: volatile_org_comp

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AerosolArmSample](AerosolArmSample.md), [AerosolSample](AerosolSample.md), [OtherUndescribedSample](OtherUndescribedSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:volatile_org_comp |
| native | basalt_schema:volatile_org_comp |




## LinkML Source

<details>
```yaml
name: volatile_org_comp
description: Volatile organic compounds are organic chemicals that have a high vapour
  pressure at room temperature.
title: volatile organic compounds
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: volatile_org_comp
domain_of:
- AerosolArmSample
- AerosolSample
- OtherUndescribedSample
range: string

```
</details>