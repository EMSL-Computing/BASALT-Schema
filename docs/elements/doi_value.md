

# Slot: doi_value 



URI: [analysis_api_schema:doi_value](https://w3id.org/MONet/analysis-api-schema/doi_value)
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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:doi_value |
| native | analysis_api_schema:doi_value |




## LinkML Source

<details>
```yaml
name: doi_value
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: doi_value
owner: DOI
domain_of:
- DOI
range: uriorcurie
required: true

```
</details>