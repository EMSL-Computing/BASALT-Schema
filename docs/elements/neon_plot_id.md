

# Slot: neon plot identifier (neon_plot_id) 


_When sampling from a NEON site provide the plot ID from which you sampled. This includes the 4 letter site code followed by the 3 digit ID (Example: DEJU_048). If you do not have your NEON site use the code SITE_999._





URI: [basalt_schema:neon_plot_id](https://emsl-computing.github.io/BASALT-Schema/elements/neon_plot_id)
Alias: neon_plot_id

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
| Regex Pattern | `^[A-Z]{4}_\d{3}$` |










## TODOs

* subport mapping - this is submitted as ABCD_123 but we want to store it as neon_site_code and neon_plot_id separately



## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:neon_plot_id |
| native | basalt_schema:neon_plot_id |




## LinkML Source

<details>
```yaml
name: neon_plot_id
description: 'When sampling from a NEON site provide the plot ID from which you sampled.
  This includes the 4 letter site code followed by the 3 digit ID (Example: DEJU_048).
  If you do not have your NEON site use the code SITE_999.'
title: neon plot identifier
todos:
- subport mapping - this is submitted as ABCD_123 but we want to store it as neon_site_code
  and neon_plot_id separately
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: neon_plot_id
domain_of:
- Site
range: string
pattern: ^[A-Z]{4}_\d{3}$

```
</details>