

# Slot: doi_value 



URI: [basalt_schema:doi_value](https://emsl-computing.github.io/BASALT-Schema/elements/doi_value)
Alias: doi_value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DOI](DOI.md) | A digital object identifier (DOI) representing a persistent link to a digital... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [DOI](DOI.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [DOI](DOI.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:doi_value |
| native | basalt_schema:doi_value |




## LinkML Source

<details>
```yaml
name: doi_value
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: doi_value
owner: DOI
domain_of:
- DOI
range: uriorcurie
required: true

```
</details>