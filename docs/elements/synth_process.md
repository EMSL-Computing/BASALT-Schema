

# Slot: synthesis process (synth_process) 


_Provide the citation or describe the method of synthesis._





URI: [basalt_schema:synth_process](https://emsl-computing.github.io/BASALT-Schema/elements/synth_process)
Alias: synth_process

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SynthesizedMaterialSample](SynthesizedMaterialSample.md) | A sample containing synthetically generated material |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






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


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:synth_process |
| native | basalt_schema:synth_process |




## LinkML Source

<details>
```yaml
name: synth_process
description: Provide the citation or describe the method of synthesis.
title: synthesis process
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: synth_process
domain_of:
- OtherUndescribedSample
- SynthesizedMaterialSample
range: string

```
</details>