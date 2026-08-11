

# Slot: link to soil classification (link_class_info) 


_Link to digitized soil maps or other soil classification information_





URI: [basalt_schema:link_class_info](https://EMSL-Computing.github.io/basalt-schema/link_class_info)
Alias: link_class_info

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










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:link_class_info |
| native | basalt_schema:link_class_info |




## LinkML Source

<details>
```yaml
name: link_class_info
description: Link to digitized soil maps or other soil classification information
title: link to soil classification
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: link_class_info
domain_of:
- Site
range: string

```
</details>