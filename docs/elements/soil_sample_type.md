

# Slot: soil type (soil_sample_type) 


_The specific type of soil sample (e.g. soil core, surface layer)._





URI: [basalt_schema:soil_sample_type](https://EMSL-Computing.github.io/basalt-schema/soil_sample_type)
Alias: soil_sample_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [MonetSoilSample](MonetSoilSample.md) | A soil sample that has been collected according to the MONet soil sampling pr... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SoilSampleTypeEnum](SoilSampleTypeEnum.md) |
| Domain Of | [MonetSoilSample](MonetSoilSample.md), [SoilSample](SoilSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |








## TODOs

* this is a GSC slot but it's not constrined by an enum, it's a string. where did this come from?
* BJM 060626 - clarified this slot and enum name from 'soil_type' but I'm still not sure we need it. it is populated in the current database though.



## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:soil_sample_type |
| native | basalt_schema:soil_sample_type |




## LinkML Source

<details>
```yaml
name: soil_sample_type
description: The specific type of soil sample (e.g. soil core, surface layer).
title: soil type
todos:
- this is a GSC slot but it's not constrined by an enum, it's a string. where did
  this come from?
- BJM 060626 - clarified this slot and enum name from 'soil_type' but I'm still not
  sure we need it. it is populated in the current database though.
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: soil_sample_type
domain_of:
- MonetSoilSample
- SoilSample
range: SoilSampleTypeEnum

```
</details>