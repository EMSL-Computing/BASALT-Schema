

# Slot: workflow_steps 


_Per-run workflow parameters. Previously annotated TODO JSONB in schema._

_Direction: structured key-value pairs keyed by workflow type._

_Schema for allowed keys TBD per workflow type before full implementation._





URI: [analysis_api_schema:workflow_steps](https://w3id.org/MONet/analysis-api-schema/workflow_steps)
Alias: workflow_steps

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataProcessingActivity](DataProcessingActivity.md) | Abstract base for any data processing activity |  no  |
| [MetagenomicsDataProcessingActivity](MetagenomicsDataProcessingActivity.md) | Concrete metagenomics workflow run |  no  |
| [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md) | Concrete mass spectrometry workflow run |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:workflow_steps |
| native | analysis_api_schema:workflow_steps |




## LinkML Source

<details>
```yaml
name: workflow_steps
description: 'Per-run workflow parameters. Previously annotated TODO JSONB in schema.

  Direction: structured key-value pairs keyed by workflow type.

  Schema for allowed keys TBD per workflow type before full implementation.'
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: workflow_steps
domain_of:
- DataProcessingActivity
range: string
required: false

```
</details>