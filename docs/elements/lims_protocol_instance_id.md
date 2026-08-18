

# Slot: lims_protocol_instance_id 


_Reference to the L7 protocol_instance that corresponds to this sample processing step, if applicable._





URI: [basalt_schema:lims_protocol_instance_id](https://emsl-computing.github.io/BASALT-Schema/elements/lims_protocol_instance_id)
Alias: lims_protocol_instance_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryConfiguration](MassSpectrometryConfiguration.md) | Instrument configuration and setup for a mass spectrometry run |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [MassSpectrometryConfiguration](MassSpectrometryConfiguration.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:lims_protocol_instance_id |
| native | basalt_schema:lims_protocol_instance_id |




## LinkML Source

<details>
```yaml
name: lims_protocol_instance_id
description: Reference to the L7 protocol_instance that corresponds to this sample
  processing step, if applicable.
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: lims_protocol_instance_id
domain_of:
- MassSpectrometryConfiguration
range: integer

```
</details>