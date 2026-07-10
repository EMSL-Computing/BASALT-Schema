

# Slot: injection 


_Type of injection used in the mass spectrometry method_





URI: [analysis_api_schema:injection](https://w3id.org/MONet/analysis-api-schema/injection)
Alias: injection

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryConfiguration](MassSpectrometryConfiguration.md) | Instrument configuration and setup for a mass spectrometry run |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:injection |
| native | analysis_api_schema:injection |




## LinkML Source

<details>
```yaml
name: injection
description: Type of injection used in the mass spectrometry method
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: injection
domain_of:
- MassSpectrometryConfiguration
range: string
required: true

```
</details>