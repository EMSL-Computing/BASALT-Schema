

# Slot: roi_volume_voxel 



URI: [basalt_schema:roi_volume_voxel](https://EMSL-Computing.github.io/BASALT-Schema/roi_volume_voxel)
Alias: roi_volume_voxel

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TomographyProduct](TomographyProduct.md) | Soil tomography analysis product, typically derived via X-ray computed tomogr... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Double](Double.md) |
| Domain Of | [TomographyProduct](TomographyProduct.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TomographyProduct](TomographyProduct.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:roi_volume_voxel |
| native | basalt_schema:roi_volume_voxel |




## LinkML Source

<details>
```yaml
name: roi_volume_voxel
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: roi_volume_voxel
owner: TomographyProduct
domain_of:
- TomographyProduct
range: double

```
</details>