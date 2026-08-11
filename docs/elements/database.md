

# Slot: database 



URI: [basalt_schema:database](https://EMSL-Computing.github.io/basalt-schema/database)
Alias: database

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FunctionalAnnotationIdentifier](FunctionalAnnotationIdentifier.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AnnotationDatabaseEnum](AnnotationDatabaseEnum.md) |
| Domain Of | [FunctionalAnnotationIdentifier](FunctionalAnnotationIdentifier.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [FunctionalAnnotationIdentifier](FunctionalAnnotationIdentifier.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:database |
| native | basalt_schema:database |




## LinkML Source

<details>
```yaml
name: database
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: database
owner: FunctionalAnnotationIdentifier
domain_of:
- FunctionalAnnotationIdentifier
range: AnnotationDatabaseEnum
required: true

```
</details>