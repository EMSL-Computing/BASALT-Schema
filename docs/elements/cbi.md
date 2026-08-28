

# Slot: cbi 


_Confidential Business Information flag (yes/no)._

_Indicates if the sample is subject to CBI restrictions._





URI: [basalt_schema:cbi](https://emsl-computing.github.io/BASALT-Schema/elements/cbi)
Alias: cbi

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EngineeredStrainSample](EngineeredStrainSample.md) | A sample containing a strain of an organism that has been subjected to geneti... |  no  |
| [AMP2UserSample](AMP2UserSample.md) | A user-submitted microbial sample for AMP2 workflows |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [AMP2UserSample](AMP2UserSample.md), [EngineeredStrainSample](EngineeredStrainSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |







## Aliases


* CBI




## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:cbi |
| native | basalt_schema:cbi |




## LinkML Source

<details>
```yaml
name: cbi
description: 'Confidential Business Information flag (yes/no).

  Indicates if the sample is subject to CBI restrictions.'
from_schema: https://emsl-computing.github.io/BASALT-Schema
aliases:
- CBI
rank: 1000
alias: cbi
domain_of:
- AMP2UserSample
- EngineeredStrainSample
range: boolean

```
</details>