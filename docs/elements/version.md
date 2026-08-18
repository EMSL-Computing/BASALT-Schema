

# Slot: version 


_String indicating the version of the software or protocol_





URI: [basalt_schema:version](https://emsl-computing.github.io/BASALT-Schema/elements/version)
Alias: version

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoftwareControlledTermValue](SoftwareControlledTermValue.md) |  |  no  |
| [Changelog](Changelog.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Changelog](Changelog.md), [SoftwareControlledTermValue](SoftwareControlledTermValue.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:version |
| native | basalt_schema:version |




## LinkML Source

<details>
```yaml
name: version
description: String indicating the version of the software or protocol
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: version
domain_of:
- Changelog
- SoftwareControlledTermValue
range: string
required: true

```
</details>