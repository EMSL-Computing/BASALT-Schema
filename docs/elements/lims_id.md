

# Slot: LIMS ID (lims_id) 


_An EMSL internal LIMS identifier for your sample. This will be provided by the MPOC and should not be edited._





URI: [analysis_api_schema:lims_id](https://w3id.org/MONet/analysis-api-schema/lims_id)
Alias: lims_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MonetSoilSample](MonetSoilSample.md) | A soil sample that has been collected according to the MONet soil sampling pr... |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^INGEST_SAMPLE_\d{9}$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:lims_id |
| native | analysis_api_schema:lims_id |




## LinkML Source

<details>
```yaml
name: lims_id
description: An EMSL internal LIMS identifier for your sample. This will be provided
  by the MPOC and should not be edited.
title: LIMS ID
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: lims_id
domain_of:
- MonetSoilSample
range: string
pattern: ^INGEST_SAMPLE_\d{9}$

```
</details>