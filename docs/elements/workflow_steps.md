

# Slot: workflow_steps 


_Per-run workflow parameters. Previously annotated TODO JSONB in schema._

_Direction: structured key-value pairs keyed by workflow type._

_Schema for allowed keys TBD per workflow type before full implementation._





URI: [basalt_schema:workflow_steps](https://w3id.org/MONet/basalt-schema/workflow_steps)
Alias: workflow_steps

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md) | Concrete mass spectrometry workflow run |  no  |
| [DataProcessingActivity](DataProcessingActivity.md) | Abstract base for any data processing activity (digital to digital) |  no  |
| [MetagenomicsDataProcessingActivity](MetagenomicsDataProcessingActivity.md) | Concrete metagenomics workflow run |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [DataProcessingActivity](DataProcessingActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:workflow_steps |
| native | basalt_schema:workflow_steps |




## LinkML Source

<details>
```yaml
name: workflow_steps
description: 'Per-run workflow parameters. Previously annotated TODO JSONB in schema.

  Direction: structured key-value pairs keyed by workflow type.

  Schema for allowed keys TBD per workflow type before full implementation.'
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: workflow_steps
domain_of:
- DataProcessingActivity
range: string
required: false

```
</details>