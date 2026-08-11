

# Slot: funding_sources 



URI: [basalt_schema:funding_sources](https://EMSL-Computing.github.io/basalt-schema/funding_sources)
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


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:funding_sources |
| native | basalt_schema:funding_sources |




## LinkML Source

<details>
```yaml
name: funding_sources
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: funding_sources
owner: Study
domain_of:
- Study
range: DOI
multivalued: true

```
</details>