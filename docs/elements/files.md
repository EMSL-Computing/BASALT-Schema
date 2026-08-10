

# Slot: files 



URI: [basalt_schema:files](https://w3id.org/MONet/basalt-schema/files)
Alias: files

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ZipDownload](ZipDownload.md) | A zip download record, capturing the details of a zip file download event |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
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
| self | basalt_schema:files |
| native | basalt_schema:files |




## LinkML Source

<details>
```yaml
name: files
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: files
owner: zipDownload
domain_of:
- zipDownload
range: integer
required: true

```
</details>