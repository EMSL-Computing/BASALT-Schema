

# Slot: geographic location name (geo_loc_name) 


_The geographical origin of the sample as defined by the country or sea name followed by specific region name and site. Formatted as [Country or sea names: region or state, site]_





URI: [analysis_api_schema:geo_loc_name](https://w3id.org/MONet/analysis-api-schema/geo_loc_name)
Alias: geo_loc_name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Site](Site.md) | Site-level metadata for a specific location from which a set of samples are c... |  yes  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^([^\s-]{12}|[^\s-]+.+[^\s-]+):\s?([^\s-]{12}|[^\s-]+.+[^\s-]+)\s?([^\s-]{12}|[^\s-]+.+[^\s-]+)$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:geo_loc_name |
| native | analysis_api_schema:geo_loc_name |




## LinkML Source

<details>
```yaml
name: geo_loc_name
description: 'The geographical origin of the sample as defined by the country or sea
  name followed by specific region name and site. Formatted as [Country or sea names:
  region or state, site]'
title: geographic location name
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: geo_loc_name
domain_of:
- Site
range: string
pattern: ^([^\s-]{12}|[^\s-]+.+[^\s-]+):\s?([^\s-]{12}|[^\s-]+.+[^\s-]+)\s?([^\s-]{12}|[^\s-]+.+[^\s-]+)$

```
</details>