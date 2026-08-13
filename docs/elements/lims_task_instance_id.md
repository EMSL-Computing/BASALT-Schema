

# Slot: lims_task_instance_id 


_L7 task_instance_id for the activity, if known._





URI: [basalt_schema:lims_task_instance_id](https://EMSL-Computing.github.io/BASALT-Schema/lims_task_instance_id)
Alias: lims_task_instance_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md) | Concrete mass spectrometry workflow run |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:lims_task_instance_id |
| native | basalt_schema:lims_task_instance_id |




## LinkML Source

<details>
```yaml
name: lims_task_instance_id
description: L7 task_instance_id for the activity, if known.
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: lims_task_instance_id
domain_of:
- MassSpectrometryDataProcessingActivity
range: integer

```
</details>