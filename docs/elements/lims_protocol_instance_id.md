

# Slot: lims_protocol_instance_id 


_Reference to the L7 protocol_instance that corresponds to this sample processing step, if applicable._





URI: [analysis_api_schema:lims_protocol_instance_id](https://w3id.org/MONet/analysis-api-schema/lims_protocol_instance_id)
Alias: lims_protocol_instance_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryConfiguration](MassSpectrometryConfiguration.md) | Instrument configuration and setup for a mass spectrometry run |  no  |







## Properties

* Range: [Integer](Integer.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:lims_protocol_instance_id |
| native | analysis_api_schema:lims_protocol_instance_id |




## LinkML Source

<details>
```yaml
name: lims_protocol_instance_id
description: Reference to the L7 protocol_instance that corresponds to this sample
  processing step, if applicable.
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: lims_protocol_instance_id
domain_of:
- MassSpectrometryConfiguration
range: integer

```
</details>