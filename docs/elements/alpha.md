

# Slot: alpha 


_Van Genuchten shape parameter alpha (1/cm). Controls the inverse of the air-entry suction; typically fitted by HYPROP-FIT or similar software._





URI: [basalt_schema:alpha](https://EMSL-Computing.github.io/basalt-schema/alpha)
Alias: alpha

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


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:alpha |
| native | basalt_schema:alpha |




## LinkML Source

<details>
```yaml
name: alpha
description: Van Genuchten shape parameter alpha (1/cm). Controls the inverse of the
  air-entry suction; typically fitted by HYPROP-FIT or similar software.
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: alpha
owner: HydraulicPropertiesProduct
domain_of:
- HydraulicPropertiesProduct
range: double

```
</details>