

# Slot: version 


_String indicating the version of the software or protocol_





URI: [basalt_schema:version](https://w3id.org/MONet/basalt-schema/version)
Alias: version

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Changelog](Changelog.md) |  |  no  |
| [SoftwareControlledTermValue](SoftwareControlledTermValue.md) |  |  no  |






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


* from schema: https://w3id.org/MONet/basalt-schema




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
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: version
domain_of:
- Changelog
- SoftwareControlledTermValue
range: string
required: true

```
</details>