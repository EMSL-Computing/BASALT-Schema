

# Slot: segment_order 


_The order of this segment in the overall chromatography protocol._





URI: [basalt_schema:segment_order](https://EMSL-Computing.github.io/basalt-schema/segment_order)
Alias: segment_order

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MobilePhaseSegment](MobilePhaseSegment.md) | A segment of the mobile phase used in chromatography during mass spectrometry |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
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
| self | basalt_schema:segment_order |
| native | basalt_schema:segment_order |




## LinkML Source

<details>
```yaml
name: segment_order
description: The order of this segment in the overall chromatography protocol.
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: segment_order
owner: MobilePhaseSegment
domain_of:
- MobilePhaseSegment
range: integer

```
</details>