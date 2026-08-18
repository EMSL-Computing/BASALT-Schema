

# Slot: site_photo_type 



URI: [basalt_schema:site_photo_type](https://EMSL-Computing.github.io/BASALT-Schema/site_photo_type)
Alias: site_photo_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SitePhoto](SitePhoto.md) | A data product representing a photo of a site, typically taken during samplin... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SitePhotoCategoryEnum](SitePhotoCategoryEnum.md) |
| Domain Of | [SitePhoto](SitePhoto.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SitePhoto](SitePhoto.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:site_photo_type |
| native | basalt_schema:site_photo_type |




## LinkML Source

<details>
```yaml
name: site_photo_type
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: site_photo_type
owner: SitePhoto
domain_of:
- SitePhoto
range: SitePhotoCategoryEnum

```
</details>