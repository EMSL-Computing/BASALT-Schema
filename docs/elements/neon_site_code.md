

# Slot: neon site code (neon_site_code) 


_When sampling from a NEON site provide the 4 letter site code (Example: DEJU). If you do not have your NEON site use the code SITE_999._





URI: [basalt_schema:neon_site_code](https://EMSL-Computing.github.io/basalt-schema/neon_site_code)
Alias: neon_site_code

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
| Regex Pattern | `^[A-Z]{4}$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:neon_site_code |
| native | basalt_schema:neon_site_code |




## LinkML Source

<details>
```yaml
name: neon_site_code
description: 'When sampling from a NEON site provide the 4 letter site code (Example:
  DEJU). If you do not have your NEON site use the code SITE_999.'
title: neon site code
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: neon_site_code
domain_of:
- Site
range: string
pattern: ^[A-Z]{4}$

```
</details>