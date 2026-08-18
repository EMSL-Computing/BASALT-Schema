

# Slot: setup_instrument 


_Automated liquid handler (e.g. "Hamilton_STAR") or "manual"_





URI: [basalt_schema:setup_instrument](https://emsl-computing.github.io/BASALT-Schema/elements/setup_instrument)
Alias: setup_instrument

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AMP2PlateSetupActivity](AMP2PlateSetupActivity.md) | AMP2-specific plate setup |  no  |
| [PlateSetupActivity](PlateSetupActivity.md) | Abstract base for 96-well plate setup activities |  no  |
| [EcoplatePlateSetupActivity](EcoplatePlateSetupActivity.md) | Ecoplate-specific plate setup |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PlateSetupActivity](PlateSetupActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:setup_instrument |
| native | basalt_schema:setup_instrument |




## LinkML Source

<details>
```yaml
name: setup_instrument
description: Automated liquid handler (e.g. "Hamilton_STAR") or "manual"
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: setup_instrument
domain_of:
- PlateSetupActivity
range: string

```
</details>