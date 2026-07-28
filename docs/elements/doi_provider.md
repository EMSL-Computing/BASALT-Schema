

# Slot: doi_provider 


_The authority, or organization, the DOI is associated with._





URI: [analysis_api_schema:doi_provider](https://w3id.org/MONet/analysis-api-schema/doi_provider)
Alias: doi_provider

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DOI](DOI.md) | A digital object identifier (DOI) representing a persistent link to a digital... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DoiProviderEnum](DoiProviderEnum.md) |
| Domain Of | [DOI](DOI.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | analysis_api_schema:doi_provider |
| native | analysis_api_schema:doi_provider |




## LinkML Source

<details>
```yaml
name: doi_provider
description: The authority, or organization, the DOI is associated with.
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: doi_provider
owner: DOI
domain_of:
- DOI
range: DoiProviderEnum

```
</details>