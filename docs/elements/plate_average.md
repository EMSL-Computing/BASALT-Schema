

# Slot: plate_average 


_Mean measurement across all sample wells (excludes blanks)_





URI: [analysis_api_schema:plate_average](https://w3id.org/MONet/analysis-api-schema/plate_average)
Alias: plate_average

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EcoplateAbsorbanceProduct](EcoplateAbsorbanceProduct.md) | Ecoplate absorbance measurement product |  no  |
| [PlateProduct](PlateProduct.md) | Abstract base for plate measurement data products |  no  |
| [AMP2ODProduct](AMP2ODProduct.md) | AMP2 optical density measurement product |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [PlateProduct](PlateProduct.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |








## TODOs

* units



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:plate_average |
| native | analysis_api_schema:plate_average |




## LinkML Source

<details>
```yaml
name: plate_average
description: Mean measurement across all sample wells (excludes blanks)
todos:
- units
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: plate_average
domain_of:
- PlateProduct
range: float

```
</details>