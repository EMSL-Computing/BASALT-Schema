

# Slot: segment_order 


_The order of this segment in the overall chromatography protocol._





URI: [analysis_api_schema:segment_order](https://w3id.org/MONet/analysis-api-schema/segment_order)
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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:segment_order |
| native | analysis_api_schema:segment_order |




## LinkML Source

<details>
```yaml
name: segment_order
description: The order of this segment in the overall chromatography protocol.
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: segment_order
owner: MobilePhaseSegment
domain_of:
- MobilePhaseSegment
range: integer

```
</details>