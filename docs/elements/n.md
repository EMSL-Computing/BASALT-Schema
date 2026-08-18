

# Slot: n 


_Van Genuchten pore-size distribution index n (dimensionless, n > 1). Controls the slope of the water-retention curve._





URI: [basalt_schema:n](https://EMSL-Computing.github.io/BASALT-Schema/n)
Alias: n

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HydraulicPropertiesProduct](HydraulicPropertiesProduct.md) | Soil hydraulic parameters derived from HYPROP evaporation-experiment data |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Double](Double.md) |
| Domain Of | [HydraulicPropertiesProduct](HydraulicPropertiesProduct.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [HydraulicPropertiesProduct](HydraulicPropertiesProduct.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:n |
| native | basalt_schema:n |




## LinkML Source

<details>
```yaml
name: n
description: Van Genuchten pore-size distribution index n (dimensionless, n > 1).
  Controls the slope of the water-retention curve.
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: n
owner: HydraulicPropertiesProduct
domain_of:
- HydraulicPropertiesProduct
range: double

```
</details>