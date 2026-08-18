

# Slot: sampled_portion 


_The portion of the original sample used in creating this processed sample (e.g., "interlayer", "supernatant", "pellet")._





URI: [basalt_schema:sampled_portion](https://emsl-computing.github.io/BASALT-Schema/elements/sampled_portion)
Alias: sampled_portion

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CoreSection](CoreSection.md) | A section of a core sample (TOP, MID, BTM) |  no  |
| [ProcessedSample](ProcessedSample.md) | A sample that has undergone processing or analysis |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SamplePortionEnum](SamplePortionEnum.md) |
| Domain Of | [ProcessedSample](ProcessedSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:sampled_portion |
| native | basalt_schema:sampled_portion |




## LinkML Source

<details>
```yaml
name: sampled_portion
description: The portion of the original sample used in creating this processed sample
  (e.g., "interlayer", "supernatant", "pellet").
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: sampled_portion
domain_of:
- ProcessedSample
range: SamplePortionEnum

```
</details>