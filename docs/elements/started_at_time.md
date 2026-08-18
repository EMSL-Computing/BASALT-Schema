

# Slot: started_at_time 



URI: [basalt_schema:started_at_time](https://emsl-computing.github.io/BASALT-Schema/elements/started_at_time)
Alias: started_at_time

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md) | Concrete mass spectrometry workflow run |  no  |
| [DataProcessingActivity](DataProcessingActivity.md) | Abstract base for any data processing activity (digital to digital) |  no  |
| [MetagenomicsDataProcessingActivity](MetagenomicsDataProcessingActivity.md) | Concrete metagenomics workflow run |  no  |
| [Activity](Activity.md) | Something that happens over time and can use equipment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Activity](Activity.md), [DataProcessingActivity](DataProcessingActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:started_at_time |
| native | basalt_schema:started_at_time |




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