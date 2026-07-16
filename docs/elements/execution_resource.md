

# Slot: execution_resource 



URI: [analysis_api_schema:execution_resource](https://w3id.org/MONet/analysis-api-schema/execution_resource)
Alias: execution_resource

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md) | Concrete mass spectrometry workflow run |  no  |
| [MetagenomicsDataProcessingActivity](MetagenomicsDataProcessingActivity.md) | Concrete metagenomics workflow run |  no  |
| [DataProcessingActivity](DataProcessingActivity.md) | Abstract base for any data processing activity (digital to digital) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ExecutionResourceEnum](ExecutionResourceEnum.md) |
| Domain Of | [DataProcessingActivity](DataProcessingActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [DataProcessingActivity](DataProcessingActivity.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:execution_resource |
| native | analysis_api_schema:execution_resource |




## LinkML Source

<details>
```yaml
name: execution_resource
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: execution_resource
owner: DataProcessingActivity
domain_of:
- DataProcessingActivity
range: ExecutionResourceEnum

```
</details>