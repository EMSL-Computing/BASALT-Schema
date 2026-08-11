

# Slot: processing_id 



URI: [basalt_schema:processing_id](https://EMSL-Computing.github.io/basalt-schema/processing_id)
Alias: processing_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProcessingSampleLink](ProcessingSampleLink.md) | A link between a processed sample and the sample processing activity that pro... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SampleProcessing](SampleProcessing.md) |
| Domain Of | [ProcessingSampleLink](ProcessingSampleLink.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ProcessingSampleLink](ProcessingSampleLink.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:processing_id |
| native | basalt_schema:processing_id |




## LinkML Source

<details>
```yaml
name: processing_id
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: processing_id
owner: ProcessingSampleLink
domain_of:
- ProcessingSampleLink
range: SampleProcessing
required: true

```
</details>