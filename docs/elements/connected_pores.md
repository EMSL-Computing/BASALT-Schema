

# Slot: connected_pores 



URI: [basalt_schema:connected_pores](https://EMSL-Computing.github.io/basalt-schema/connected_pores)
Alias: connected_pores

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


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:connected_pores |
| native | basalt_schema:connected_pores |




## LinkML Source

<details>
```yaml
name: connected_pores
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: connected_pores
owner: TomographyProduct
domain_of:
- TomographyProduct
range: double

```
</details>