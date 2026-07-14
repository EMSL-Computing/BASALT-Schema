

# Slot: started_at_time 



URI: [analysis_api_schema:started_at_time](https://w3id.org/MONet/analysis-api-schema/started_at_time)
Alias: started_at_time

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataProcessingActivity](DataProcessingActivity.md) | Abstract base for any data processing activity |  no  |
| [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md) | Concrete mass spectrometry workflow run |  no  |
| [MetagenomicsDataProcessingActivity](MetagenomicsDataProcessingActivity.md) | Concrete metagenomics workflow run |  no  |
| [Activity](Activity.md) | Something that happens over time and can use equipment |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information








## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:started_at_time |
| native | analysis_api_schema:started_at_time |




## LinkML Source

<details>
```yaml
name: started_at_time
alias: started_at_time
domain_of:
- Activity
- DataProcessingActivity
range: string

```
</details>