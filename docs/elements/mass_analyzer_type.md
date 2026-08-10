

# Slot: mass_analyzer_type 


_The type of mass analyzer present in the instrument, if applicable (e.g., Orbitrap, Time-of-Flight, Quadrupole)._





URI: [basalt_schema:mass_analyzer_type](https://w3id.org/MONet/basalt-schema/mass_analyzer_type)
Alias: mass_analyzer_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Instrument](Instrument.md) | A material entity that is designed to perform a function in a scientific  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MassAnalyzerEnum](MassAnalyzerEnum.md) |
| Domain Of | [Instrument](Instrument.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Instrument](Instrument.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:mass_analyzer_type |
| native | basalt_schema:mass_analyzer_type |




## LinkML Source

<details>
```yaml
name: mass_analyzer_type
description: The type of mass analyzer present in the instrument, if applicable (e.g.,
  Orbitrap, Time-of-Flight, Quadrupole).
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: mass_analyzer_type
owner: Instrument
domain_of:
- Instrument
range: MassAnalyzerEnum

```
</details>