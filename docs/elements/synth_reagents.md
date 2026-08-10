

# Slot: synthesis reagents (synth_reagents) 


_The reagents used in the material synthesis_





URI: [basalt_schema:synth_reagents](https://w3id.org/MONet/basalt-schema/synth_reagents)
Alias: synth_reagents

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SynthesizedMaterialSample](SynthesizedMaterialSample.md) | A sample containing synthetically generated material |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [SynthesizedMaterialSample](SynthesizedMaterialSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:synth_reagents |
| native | basalt_schema:synth_reagents |




## LinkML Source

<details>
```yaml
name: synth_reagents
description: The reagents used in the material synthesis
title: synthesis reagents
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: synth_reagents
domain_of:
- OtherUndescribedSample
- SynthesizedMaterialSample
range: string

```
</details>