

# Slot: software_url 



URI: [basalt_schema:software_url](https://EMSL-Computing.github.io/basalt-schema/software_url)
Alias: software_url

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MetagenomicsDataProcessingActivity](MetagenomicsDataProcessingActivity.md) | Concrete metagenomics workflow run |  no  |
| [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md) | Concrete mass spectrometry workflow run |  no  |
| [DataProcessingActivity](DataProcessingActivity.md) | Abstract base for any data processing activity (digital to digital) |  no  |






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


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:software_url |
| native | basalt_schema:software_url |




## LinkML Source

<details>
```yaml
name: software_url
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: software_url
owner: DataProcessingActivity
domain_of:
- DataProcessingActivity
range: string

```
</details>