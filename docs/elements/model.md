

# Slot: model 



URI: [basalt_schema:model](https://emsl-computing.github.io/BASALT-Schema/elements/model)
Alias: model

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Instrument](Instrument.md) | A material entity that is designed to perform a function in a scientific  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ModelEnum](ModelEnum.md) |
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


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:model |
| native | basalt_schema:model |




## LinkML Source

<details>
```yaml
name: model
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: model
owner: Instrument
domain_of:
- Instrument
range: ModelEnum

```
</details>