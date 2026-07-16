

# Slot: software_poc 



URI: [analysis_api_schema:software_poc](https://w3id.org/MONet/analysis-api-schema/software_poc)
Alias: software_poc

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataProcessingActivity](DataProcessingActivity.md) | Abstract base for any data processing activity |  no  |
| [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md) | Concrete mass spectrometry workflow run |  no  |
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
| self | analysis_api_schema:software_poc |
| native | analysis_api_schema:software_poc |




## LinkML Source

<details>
```yaml
name: software_poc
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: software_poc
owner: DataProcessingActivity
domain_of:
- DataProcessingActivity
range: string

```
</details>