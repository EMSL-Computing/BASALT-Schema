

# Slot: extreme event (extreme_event) 


_Unusual physical events that may have affected microbial populations. Format: YYYY-MM-DD_





URI: [analysis_api_schema:extreme_event](https://w3id.org/MONet/analysis-api-schema/extreme_event)
Alias: extreme_event

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
| self | analysis_api_schema:extreme_event |
| native | analysis_api_schema:extreme_event |




## LinkML Source

<details>
```yaml
name: extreme_event
description: 'Unusual physical events that may have affected microbial populations.
  Format: YYYY-MM-DD'
title: extreme event
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: extreme_event
domain_of:
- Site
range: string
pattern: ^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$

```
</details>