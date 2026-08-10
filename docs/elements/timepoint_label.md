

# Slot: timepoint_label 


_Human-readable timepoint label for repeated-measurement series._

_Examples: "t=0", "t=24h", "t=48h"._

_Lives on concrete analysis/product subclasses, NOT on base DataGenerationActivity_





URI: [basalt_schema:timepoint_label](https://w3id.org/MONet/basalt-schema/timepoint_label)
Alias: timepoint_label

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AMP2ODProduct](AMP2ODProduct.md) | AMP2 optical density measurement product |  no  |
| [AMP2DataGenerationActivity](AMP2DataGenerationActivity.md) | AMP2 plate measurement (OD, fluorescence, flow cytometry) |  no  |
| [EcoplateDataGenerationActivity](EcoplateDataGenerationActivity.md) | Ecoplate absorbance measurement at a single timepoint |  no  |
| [PlateDataGenerationActivity](PlateDataGenerationActivity.md) | Abstract base for plate measurement activities |  no  |
| [EcoplateAbsorbanceProduct](EcoplateAbsorbanceProduct.md) | Ecoplate absorbance measurement product |  no  |
| [PlateProduct](PlateProduct.md) | Abstract base for plate measurement data products |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PlateDataGenerationActivity](PlateDataGenerationActivity.md), [PlateProduct](PlateProduct.md) |

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
| self | basalt_schema:timepoint_label |
| native | basalt_schema:timepoint_label |




## LinkML Source

<details>
```yaml
name: timepoint_label
description: 'Human-readable timepoint label for repeated-measurement series.

  Examples: "t=0", "t=24h", "t=48h".

  Lives on concrete analysis/product subclasses, NOT on base DataGenerationActivity'
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: timepoint_label
domain_of:
- PlateDataGenerationActivity
- PlateProduct
range: string
required: true

```
</details>