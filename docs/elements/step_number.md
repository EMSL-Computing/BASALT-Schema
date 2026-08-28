

# Slot: step_number 


_Integer ordering within a multi-step process for the same analyte._

_Lower = earlier in process._





URI: [basalt_schema:step_number](https://emsl-computing.github.io/BASALT-Schema/elements/step_number)
Alias: step_number

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProcessingSampleLink](ProcessingSampleLink.md) | The authoritative record of what a SampleProcessing step consumed and produce... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [ProcessingSampleLink](ProcessingSampleLink.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:step_number |
| native | basalt_schema:step_number |




## LinkML Source

<details>
```yaml
name: step_number
description: 'Integer ordering within a multi-step process for the same analyte.

  Lower = earlier in process.'
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: step_number
domain_of:
- ProcessingSampleLink
range: integer

```
</details>