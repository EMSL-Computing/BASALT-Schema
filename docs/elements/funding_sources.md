

# Slot: funding_sources 



URI: [analysis_api_schema:funding_sources](https://w3id.org/MONet/analysis-api-schema/funding_sources)
Alias: funding_sources

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](Study.md) | A study or research project, typically associated with a proposal and a set o... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DOI](DOI.md) |
| Domain Of | [Study](Study.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Study](Study.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:funding_sources |
| native | analysis_api_schema:funding_sources |




## LinkML Source

<details>
```yaml
name: funding_sources
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: funding_sources
owner: Study
domain_of:
- Study
range: DOI
multivalued: true

```
</details>