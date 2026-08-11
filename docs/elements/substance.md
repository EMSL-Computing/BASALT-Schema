

# Slot: substance 


_The name of the substance used in this mobile phase segment._





URI: [basalt_schema:substance](https://EMSL-Computing.github.io/basalt-schema/substance)
Alias: substance

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MobilePhaseSegment](MobilePhaseSegment.md) | A segment of the mobile phase used in chromatography during mass spectrometry |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MobilePhaseSegment](MobilePhaseSegment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MobilePhaseSegment](MobilePhaseSegment.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:substance |
| native | basalt_schema:substance |




## LinkML Source

<details>
```yaml
name: substance
description: The name of the substance used in this mobile phase segment.
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: substance
owner: MobilePhaseSegment
domain_of:
- MobilePhaseSegment
range: string

```
</details>