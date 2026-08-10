

# Slot: media_additions 


_Additional components added to the media (antibiotics, inducers, etc.)._

_Examples: "100 ug/mL ampicillin", "1 mM IPTG"_





URI: [basalt_schema:media_additions](https://w3id.org/MONet/basalt-schema/media_additions)
Alias: media_additions

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaPreparation](MediaPreparation.md) | Activity that prepares a batch of growth media |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MediaPreparation](MediaPreparation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:media_additions |
| native | basalt_schema:media_additions |




## LinkML Source

<details>
```yaml
name: media_additions
description: 'Additional components added to the media (antibiotics, inducers, etc.).

  Examples: "100 ug/mL ampicillin", "1 mM IPTG"'
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: media_additions
domain_of:
- MediaPreparation
range: string
multivalued: true

```
</details>