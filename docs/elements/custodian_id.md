

# Slot: custodian_id 



URI: [basalt_schema:custodian_id](https://EMSL-Computing.github.io/BASALT-Schema/custodian_id)
Alias: custodian_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InstrumentCustodian](InstrumentCustodian.md) | A link between an instrument and a custodian (person) responsible for it |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Custodian](Custodian.md) |
| Domain Of | [InstrumentCustodian](InstrumentCustodian.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [InstrumentCustodian](InstrumentCustodian.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:custodian_id |
| native | basalt_schema:custodian_id |




## LinkML Source

<details>
```yaml
name: custodian_id
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: custodian_id
owner: InstrumentCustodian
domain_of:
- InstrumentCustodian
range: Custodian
required: true

```
</details>