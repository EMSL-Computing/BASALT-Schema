

# Slot: doi_provider 


_The authority, or organization, the DOI is associated with._





URI: [basalt_schema:doi_provider](https://EMSL-Computing.github.io/basalt-schema/doi_provider)
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


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:doi_provider |
| native | basalt_schema:doi_provider |




## LinkML Source

<details>
```yaml
name: doi_provider
description: The authority, or organization, the DOI is associated with.
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: doi_provider
owner: DOI
domain_of:
- DOI
range: DoiProviderEnum

```
</details>