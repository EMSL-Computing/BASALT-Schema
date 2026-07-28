

# Slot: mean seasonal temperature (season_temp) 


_Mean seasonal temperature (Unit: C)_





URI: [analysis_api_schema:season_temp](https://w3id.org/MONet/analysis-api-schema/season_temp)
Alias: season_temp

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Site](Site.md) | Site-level metadata for a specific location from which a set of samples are c... |  no  |






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
| Regex Pattern | `^-?\d+(\.\d+)?\s*C$` |









## Aliases


* average seasonal precipitation




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:season_temp |
| native | analysis_api_schema:season_temp |




## LinkML Source

<details>
```yaml
name: season_temp
description: 'Mean seasonal temperature (Unit: C)'
title: mean seasonal temperature
from_schema: https://w3id.org/MONet/analysis-api-schema
aliases:
- average seasonal precipitation
rank: 1000
alias: season_temp
domain_of:
- Site
range: string
pattern: ^-?\d+(\.\d+)?\s*C$

```
</details>