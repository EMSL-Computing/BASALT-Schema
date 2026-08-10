

# Slot: user 



URI: [basalt_schema:user](https://w3id.org/MONet/basalt-schema/user)
Alias: user

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ZipDownload](ZipDownload.md) | A zip download record, capturing the details of a zip file download event |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ZipDownload](ZipDownload.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ZipDownload](ZipDownload.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:user |
| native | basalt_schema:user |




## LinkML Source

<details>
```yaml
name: user
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: user
owner: zipDownload
domain_of:
- zipDownload
range: string
required: true

```
</details>