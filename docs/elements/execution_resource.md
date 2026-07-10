

# Slot: execution_resource 



URI: [analysis_api_schema:execution_resource](https://w3id.org/MONet/analysis-api-schema/execution_resource)
Alias: execution_resource

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataProcessingActivity](DataProcessingActivity.md) | Abstract base for any data processing activity |  no  |
| [MetagenomicsDataProcessingActivity](MetagenomicsDataProcessingActivity.md) | Concrete metagenomics workflow run |  no  |
| [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md) | Concrete mass spectrometry workflow run |  no  |







## Properties

* Range: [ExecutionResourceEnum](ExecutionResourceEnum.md)





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