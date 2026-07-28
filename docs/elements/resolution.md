

# Slot: resolution 



URI: [analysis_api_schema:resolution](https://w3id.org/MONet/analysis-api-schema/resolution)
Alias: resolution

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryConfiguration](MassSpectrometryConfiguration.md) | Instrument configuration and setup for a mass spectrometry run |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MassSpecResolutionEnum](MassSpecResolutionEnum.md) |
| Domain Of | [MassSpectrometryConfiguration](MassSpectrometryConfiguration.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:resolution |
| native | analysis_api_schema:resolution |




## LinkML Source

<details>
```yaml
name: resolution
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: resolution
domain_of:
- MassSpectrometryConfiguration
range: MassSpecResolutionEnum
required: true

```
</details>