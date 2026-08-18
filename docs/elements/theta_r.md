

# Slot: theta_r 


_Residual volumetric water content theta_r (cm3 cm). The water content at which liquid conductivity approaches zero._





URI: [basalt_schema:theta_r](https://EMSL-Computing.github.io/BASALT-Schema/theta_r)
Alias: theta_r

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
| self | basalt_schema:theta_r |
| native | basalt_schema:theta_r |




## LinkML Source

<details>
```yaml
name: theta_r
description: Residual volumetric water content theta_r (cm3 cm). The water content
  at which liquid conductivity approaches zero.
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: theta_r
owner: HydraulicPropertiesProduct
domain_of:
- HydraulicPropertiesProduct
range: double

```
</details>