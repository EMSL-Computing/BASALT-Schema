

# Slot: plate_lot 


_Manufacturer lot number for Biolog EcoPlate QC_





URI: [basalt_schema:plate_lot](https://EMSL-Computing.github.io/basalt-schema/plate_lot)
Alias: plate_lot

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EcoplateAbsorbanceProduct](EcoplateAbsorbanceProduct.md) | Ecoplate absorbance measurement product |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [EcoplateAbsorbanceProduct](EcoplateAbsorbanceProduct.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:plate_lot |
| native | basalt_schema:plate_lot |




## LinkML Source

<details>
```yaml
name: plate_lot
description: Manufacturer lot number for Biolog EcoPlate QC
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: plate_lot
domain_of:
- EcoplateAbsorbanceProduct
range: string

```
</details>