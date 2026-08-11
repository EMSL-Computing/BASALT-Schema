

# Slot: maintenance 


_Maintenance notes or directions to a maintenance log._





URI: [basalt_schema:maintenance](https://EMSL-Computing.github.io/basalt-schema/maintenance)
Alias: maintenance

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Instrument](Instrument.md) | A material entity that is designed to perform a function in a scientific  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:maintenance |
| native | basalt_schema:maintenance |




## LinkML Source

<details>
```yaml
name: maintenance
description: Maintenance notes or directions to a maintenance log.
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: maintenance
owner: Instrument
domain_of:
- Instrument
range: string

```
</details>