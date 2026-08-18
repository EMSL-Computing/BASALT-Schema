

# Slot: plate_average 


_Mean measurement across all sample wells (excludes blanks)_





URI: [basalt_schema:plate_average](https://emsl-computing.github.io/BASALT-Schema/elements/plate_average)
Alias: plate_average

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AMP2ODProduct](AMP2ODProduct.md) | AMP2 optical density measurement product |  no  |
| [EcoplateAbsorbanceProduct](EcoplateAbsorbanceProduct.md) | Ecoplate absorbance measurement product |  no  |
| [PlateProduct](PlateProduct.md) | Abstract base for plate measurement data products |  no  |






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


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:plate_average |
| native | basalt_schema:plate_average |




## LinkML Source

<details>
```yaml
name: plate_average
description: Mean measurement across all sample wells (excludes blanks)
todos:
- units
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: plate_average
domain_of:
- PlateProduct
range: float

```
</details>