

# Slot: execution_resource 



URI: [basalt_schema:execution_resource](https://emsl-computing.github.io/BASALT-Schema/elements/execution_resource)
Alias: execution_resource

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


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:execution_resource |
| native | basalt_schema:execution_resource |




## LinkML Source

<details>
```yaml
name: execution_resource
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: execution_resource
owner: DataProcessingActivity
domain_of:
- DataProcessingActivity
range: ExecutionResourceEnum

```
</details>