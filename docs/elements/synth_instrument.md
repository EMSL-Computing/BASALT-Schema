

# Slot: synthesizing instrument (synth_instrument) 


_The instrumentation used to synthesize the material sample._





URI: [basalt_schema:synth_instrument](https://EMSL-Computing.github.io/basalt-schema/synth_instrument)
Alias: synth_instrument

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SynthesizedMaterialSample](SynthesizedMaterialSample.md) | A sample containing synthetically generated material |  yes  |
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


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:synth_instrument |
| native | basalt_schema:synth_instrument |




## LinkML Source

<details>
```yaml
name: synth_instrument
description: The instrumentation used to synthesize the material sample.
title: synthesizing instrument
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: synth_instrument
domain_of:
- OtherUndescribedSample
- SynthesizedMaterialSample
range: string

```
</details>