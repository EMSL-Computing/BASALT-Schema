

# Slot: injection 


_Type of injection used in the mass spectrometry method_





URI: [basalt_schema:injection](https://w3id.org/MONet/basalt-schema/injection)
Alias: injection

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


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:injection |
| native | basalt_schema:injection |




## LinkML Source

<details>
```yaml
name: injection
description: Type of injection used in the mass spectrometry method
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: injection
domain_of:
- MassSpectrometryConfiguration
range: string
required: true

```
</details>