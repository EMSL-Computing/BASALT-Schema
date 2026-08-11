

# Slot: vendor 



URI: [basalt_schema:vendor](https://EMSL-Computing.github.io/basalt-schema/vendor)
Alias: vendor

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Instrument](Instrument.md) | A material entity that is designed to perform a function in a scientific  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [VendorEnum](VendorEnum.md) |
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
| self | basalt_schema:vendor |
| native | basalt_schema:vendor |




## LinkML Source

<details>
```yaml
name: vendor
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: vendor
owner: Instrument
domain_of:
- Instrument
range: VendorEnum

```
</details>