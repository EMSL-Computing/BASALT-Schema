

# Slot: ionization 


_Type of ionization used in the mass spectrometry method_





URI: [analysis_api_schema:ionization](https://w3id.org/MONet/analysis-api-schema/ionization)
Alias: ionization

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryConfiguration](MassSpectrometryConfiguration.md) | Instrument configuration and setup for a mass spectrometry run |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IonizationSourceEnum](IonizationSourceEnum.md) |
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
| self | analysis_api_schema:ionization |
| native | analysis_api_schema:ionization |




## LinkML Source

<details>
```yaml
name: ionization
description: Type of ionization used in the mass spectrometry method
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: ionization
domain_of:
- MassSpectrometryConfiguration
range: IonizationSourceEnum
required: true

```
</details>