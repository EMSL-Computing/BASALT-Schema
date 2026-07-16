

# Slot: cv_percent 


_Coefficient of variation across technical replicates_





URI: [analysis_api_schema:cv_percent](https://w3id.org/MONet/analysis-api-schema/cv_percent)
Alias: cv_percent

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AMP2ODProduct](AMP2ODProduct.md) | AMP2 optical density measurement product |  no  |
| [PlateProduct](PlateProduct.md) | Abstract base for plate measurement data products |  no  |
| [EcoplateAbsorbanceProduct](EcoplateAbsorbanceProduct.md) | Ecoplate absorbance measurement product |  no  |






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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:cv_percent |
| native | analysis_api_schema:cv_percent |




## LinkML Source

<details>
```yaml
name: cv_percent
description: Coefficient of variation across technical replicates
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: cv_percent
domain_of:
- PlateProduct
range: float

```
</details>