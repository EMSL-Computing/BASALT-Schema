

# Slot: mean annual temperature (annual_temp) 


_Mean annual temperature (Unit: C)_





URI: [analysis_api_schema:annual_temp](https://w3id.org/MONet/analysis-api-schema/annual_temp)
Alias: annual_temp

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Site](Site.md) | Site-level metadata for a specific location from which a set of samples are c... |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^-?\d+(\.\d+)?\s*C$`



## Aliases


* average annual temperature



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:annual_temp |
| native | analysis_api_schema:annual_temp |




## LinkML Source

<details>
```yaml
name: annual_temp
description: 'Mean annual temperature (Unit: C)'
title: mean annual temperature
from_schema: https://w3id.org/MONet/analysis-api-schema
aliases:
- average annual temperature
rank: 1000
alias: annual_temp
domain_of:
- Site
range: string
pattern: ^-?\d+(\.\d+)?\s*C$

```
</details>