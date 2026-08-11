

# Slot: well_readings 


_Structured per-well measurement data array._

_Lightweight summary for SQL queries without full file download._

_Raw data still accessible via processedData.s3_key in MinIO._

_typed via LinkML inlined class._





URI: [basalt_schema:well_readings](https://w3id.org/MONet/basalt-schema/well_readings)
Alias: well_readings

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlateProduct](PlateProduct.md) | Abstract base for plate measurement data products |  no  |
| [AMP2ODProduct](AMP2ODProduct.md) | AMP2 optical density measurement product |  no  |
| [EcoplateAbsorbanceProduct](EcoplateAbsorbanceProduct.md) | Ecoplate absorbance measurement product |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [WellReading](WellReading.md) |
| Domain Of | [PlateProduct](PlateProduct.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |








## TODOs

* decide how to represent in backend (normalized child table with FK to PlateSetupActivity, array column, or other)



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:well_readings |
| native | basalt_schema:well_readings |




## LinkML Source

<details>
```yaml
name: well_readings
description: 'Structured per-well measurement data array.

  Lightweight summary for SQL queries without full file download.

  Raw data still accessible via processedData.s3_key in MinIO.

  typed via LinkML inlined class.'
todos:
- decide how to represent in backend (normalized child table with FK to PlateSetupActivity,
  array column, or other)
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: well_readings
domain_of:
- PlateProduct
range: WellReading
multivalued: true
inlined: true
inlined_as_list: true

```
</details>