

# Slot: host specific name (specific_host) 


_If there is a host involved please provide its taxid (or environmental if not actually isolated from the dead or alive host - i.e. a pathogen could be isolated from a swipe of a bench etc) and report whether it is a laboratory or natural host_





URI: [basalt_schema:specific_host](https://w3id.org/MONet/basalt-schema/specific_host)
Alias: specific_host

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MixedCultureSample](MixedCultureSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:specific_host |
| native | basalt_schema:specific_host |




## LinkML Source

<details>
```yaml
name: specific_host
description: If there is a host involved please provide its taxid (or environmental
  if not actually isolated from the dead or alive host - i.e. a pathogen could be
  isolated from a swipe of a bench etc) and report whether it is a laboratory or natural
  host
title: host specific name
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: specific_host
domain_of:
- MixedCultureSample
range: string

```
</details>