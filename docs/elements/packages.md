

# Slot: packages 



URI: [basalt_schema:packages](https://EMSL-Computing.github.io/basalt-schema/packages)
Alias: packages

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
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ZipDownload](ZipDownload.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:packages |
| native | basalt_schema:packages |




## LinkML Source

<details>
```yaml
name: packages
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: packages
owner: zipDownload
domain_of:
- zipDownload
range: string

```
</details>