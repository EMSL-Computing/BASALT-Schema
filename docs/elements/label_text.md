

# Slot: label_text 


_The label on the stored processed sample, if applicable (e.g., "f01")._





URI: [basalt_schema:label_text](https://EMSL-Computing.github.io/basalt-schema/label_text)
Alias: label_text

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CoreSection](CoreSection.md) | A section of a core sample (TOP, MID, BTM) |  no  |
| [ProcessedSample](ProcessedSample.md) | A sample that has undergone processing or analysis |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ProcessedSample](ProcessedSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:label_text |
| native | basalt_schema:label_text |




## LinkML Source

<details>
```yaml
name: label_text
description: The label on the stored processed sample, if applicable (e.g., "f01").
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: label_text
domain_of:
- ProcessedSample
range: string

```
</details>