

# Slot: plate_reader_model 


_Instrument model used for reading (e.g. "BioTek Epoch2")_





URI: [basalt_schema:plate_reader_model](https://EMSL-Computing.github.io/BASALT-Schema/plate_reader_model)
Alias: plate_reader_model

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AMP2ODProduct](AMP2ODProduct.md) | AMP2 optical density measurement product |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AMP2ODProduct](AMP2ODProduct.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |








## TODOs

* harmonize with existing Instrument modelling



## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:plate_reader_model |
| native | basalt_schema:plate_reader_model |




## LinkML Source

<details>
```yaml
name: plate_reader_model
description: Instrument model used for reading (e.g. "BioTek Epoch2")
todos:
- harmonize with existing Instrument modelling
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: plate_reader_model
domain_of:
- AMP2ODProduct
range: string

```
</details>