# Enum: SampleRole 




_The direction in which a Sample participates in a SampleProcessing activity. Recorded on ProcessingSampleLink, which is the authoritative record of what each processing step consumed and produced._



URI: [basalt_schema:SampleRole](https://emsl-computing.github.io/BASALT-Schema/elements/SampleRole)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| input_sample | None | The sample was consumed by the processing activity |
| output_sample | None | The sample (always a ProcessedSample) was produced by the processing activity |




## Slots

| Name | Description |
| ---  | --- |
| [role](role.md) | Whether sample_id was consumed by (input_sample) or produced by (output_sampl... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema






## LinkML Source

<details>
```yaml
name: SampleRole
description: The direction in which a Sample participates in a SampleProcessing activity.
  Recorded on ProcessingSampleLink, which is the authoritative record of what each
  processing step consumed and produced.
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
permissible_values:
  input_sample:
    text: input_sample
    description: The sample was consumed by the processing activity.
  output_sample:
    text: output_sample
    description: The sample (always a ProcessedSample) was produced by the processing
      activity.

```
</details>