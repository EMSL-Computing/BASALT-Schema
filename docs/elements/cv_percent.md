

# Slot: cv_percent 


_Coefficient of variation across technical replicates_





URI: [basalt_schema:cv_percent](https://EMSL-Computing.github.io/basalt-schema/cv_percent)
Alias: cv_percent

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EcoplateAbsorbanceProduct](EcoplateAbsorbanceProduct.md) | Ecoplate absorbance measurement product |  no  |
| [AMP2ODProduct](AMP2ODProduct.md) | AMP2 optical density measurement product |  no  |
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


* from schema: https://EMSL-Computing.github.io/basalt-schema




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
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: cv_percent
domain_of:
- PlateProduct
range: float

```
</details>