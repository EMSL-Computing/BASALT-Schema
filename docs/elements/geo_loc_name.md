

# Slot: geographic location name (geo_loc_name) 


_The geographical origin of the sample as defined by the country or sea name followed by specific region name and site. Formatted as [Country or sea names: region or state, site]_





URI: [basalt_schema:geo_loc_name](https://EMSL-Computing.github.io/basalt-schema/geo_loc_name)
Alias: geo_loc_name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Site](Site.md) | Site-level metadata for a specific location from which a set of samples are c... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Site](Site.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^([^\s-]{12}|[^\s-]+.+[^\s-]+):\s?([^\s-]{12}|[^\s-]+.+[^\s-]+)\s?([^\s-]{12}|[^\s-]+.+[^\s-]+)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:geo_loc_name |
| native | basalt_schema:geo_loc_name |




## LinkML Source

<details>
```yaml
name: geo_loc_name
description: 'The geographical origin of the sample as defined by the country or sea
  name followed by specific region name and site. Formatted as [Country or sea names:
  region or state, site]'
title: geographic location name
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: geo_loc_name
domain_of:
- Site
range: string
pattern: ^([^\s-]{12}|[^\s-]+.+[^\s-]+):\s?([^\s-]{12}|[^\s-]+.+[^\s-]+)\s?([^\s-]{12}|[^\s-]+.+[^\s-]+)$

```
</details>