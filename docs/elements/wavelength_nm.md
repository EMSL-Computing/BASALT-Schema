

# Slot: wavelength_nm 


_Measurement wavelength in nanometres (e.g. 590 Ecoplate, 610 AMP2 OD)_





URI: [basalt_schema:wavelength_nm](https://w3id.org/MONet/basalt-schema/wavelength_nm)
Alias: wavelength_nm

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlateProduct](PlateProduct.md) | Abstract base for plate measurement data products |  no  |
| [AMP2DataGenerationActivity](AMP2DataGenerationActivity.md) | AMP2 plate measurement (OD, fluorescence, flow cytometry) |  no  |
| [AMP2ODProduct](AMP2ODProduct.md) | AMP2 optical density measurement product |  no  |
| [EcoplateDataGenerationActivity](EcoplateDataGenerationActivity.md) | Ecoplate absorbance measurement at a single timepoint |  no  |
| [EcoplateAbsorbanceProduct](EcoplateAbsorbanceProduct.md) | Ecoplate absorbance measurement product |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [AMP2DataGenerationActivity](AMP2DataGenerationActivity.md), [EcoplateDataGenerationActivity](EcoplateDataGenerationActivity.md), [PlateProduct](PlateProduct.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:wavelength_nm |
| native | basalt_schema:wavelength_nm |




## LinkML Source

<details>
```yaml
name: wavelength_nm
description: Measurement wavelength in nanometres (e.g. 590 Ecoplate, 610 AMP2 OD)
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: wavelength_nm
domain_of:
- AMP2DataGenerationActivity
- EcoplateDataGenerationActivity
- PlateProduct
range: integer
required: true

```
</details>