

# Slot: theta_s 


_Saturated volumetric water content theta_s (cm3 cm e-3). Approximates total porosity under saturated conditions._





URI: [analysis_api_schema:theta_s](https://w3id.org/MONet/analysis-api-schema/theta_s)
Alias: theta_s

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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:theta_s |
| native | analysis_api_schema:theta_s |




## LinkML Source

<details>
```yaml
name: theta_s
description: Saturated volumetric water content theta_s (cm3 cm e-3). Approximates
  total porosity under saturated conditions.
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: theta_s
owner: HydraulicPropertiesProduct
domain_of:
- HydraulicPropertiesProduct
range: double

```
</details>