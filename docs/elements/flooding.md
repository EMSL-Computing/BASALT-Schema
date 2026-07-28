

# Slot: flooding (flooding) 


_Historical and/or physical evidence of flooding. Format: YYYY-MM-DD_





URI: [analysis_api_schema:flooding](https://w3id.org/MONet/analysis-api-schema/flooding)
Alias: flooding

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
| Regex Pattern | `^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:flooding |
| native | analysis_api_schema:flooding |




## LinkML Source

<details>
```yaml
name: flooding
description: 'Historical and/or physical evidence of flooding. Format: YYYY-MM-DD'
title: flooding
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: flooding
domain_of:
- Site
range: string
pattern: ^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$

```
</details>