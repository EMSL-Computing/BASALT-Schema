

# Slot: plate_reader_model 


_Instrument model used for reading (e.g. "BioTek Epoch2")_





URI: [analysis_api_schema:plate_reader_model](https://w3id.org/MONet/analysis-api-schema/plate_reader_model)
Alias: plate_reader_model

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AMP2ODProduct](AMP2ODProduct.md) | AMP2 optical density measurement product |  no  |







## Properties

* Range: [String](String.md)





## TODOs

* harmonize with existing Instrument modelling

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:plate_reader_model |
| native | analysis_api_schema:plate_reader_model |




## LinkML Source

<details>
```yaml
name: plate_reader_model
description: Instrument model used for reading (e.g. "BioTek Epoch2")
todos:
- harmonize with existing Instrument modelling
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: plate_reader_model
domain_of:
- AMP2ODProduct
range: string

```
</details>