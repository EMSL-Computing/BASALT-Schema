

# Slot: blank_mean 


_Mean measurement of uninoculated control wells_





URI: [basalt_schema:blank_mean](https://w3id.org/MONet/basalt-schema/blank_mean)
Alias: blank_mean

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


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:blank_mean |
| native | basalt_schema:blank_mean |




## LinkML Source

<details>
```yaml
name: blank_mean
description: Mean measurement of uninoculated control wells
todos:
- units
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: blank_mean
domain_of:
- PlateProduct
range: float

```
</details>