

# Slot: custodian_id 



URI: [analysis_api_schema:custodian_id](https://w3id.org/MONet/analysis-api-schema/custodian_id)
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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:custodian_id |
| native | analysis_api_schema:custodian_id |




## LinkML Source

<details>
```yaml
name: custodian_id
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: custodian_id
owner: InstrumentCustodian
domain_of:
- InstrumentCustodian
range: Custodian
required: true

```
</details>