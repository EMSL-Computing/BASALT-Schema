

# Slot: cv_percent 


_Coefficient of variation across technical replicates_





URI: [basalt_schema:cv_percent](https://emsl-computing.github.io/BASALT-Schema/elements/cv_percent)
Alias: cv_percent

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










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:cv_percent |
| native | basalt_schema:cv_percent |




## LinkML Source

<details>
```yaml
name: cv_percent
description: Coefficient of variation across technical replicates
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: cv_percent
domain_of:
- PlateProduct
range: float

```
</details>