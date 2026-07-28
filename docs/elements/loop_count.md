

# Slot: loop_count 


_Number of MS2 scans to be acquired between each full MS scan._





URI: [analysis_api_schema:loop_count](https://w3id.org/MONet/analysis-api-schema/loop_count)
Alias: loop_count

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryConfiguration](MassSpectrometryConfiguration.md) | Instrument configuration and setup for a mass spectrometry run |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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
| self | analysis_api_schema:loop_count |
| native | analysis_api_schema:loop_count |




## LinkML Source

<details>
```yaml
name: loop_count
description: Number of MS2 scans to be acquired between each full MS scan.
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: loop_count
domain_of:
- MassSpectrometryConfiguration
range: string
required: true

```
</details>