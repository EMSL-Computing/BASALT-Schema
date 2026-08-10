

# Slot: purchased_material_type 


_Discriminator for purchasedMaterial subtype (e.g. 'media', 'strain')_





URI: [basalt_schema:purchased_material_type](https://w3id.org/MONet/basalt-schema/purchased_material_type)
Alias: purchased_material_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PurchasedMaterial](PurchasedMaterial.md) | [NEW ABSTRACT CLASS] Lightweight base for non-sample physical lab materials |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PurchasedMaterial](PurchasedMaterial.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:purchased_material_type |
| native | basalt_schema:purchased_material_type |




## LinkML Source

<details>
```yaml
name: purchased_material_type
description: Discriminator for purchasedMaterial subtype (e.g. 'media', 'strain')
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: purchased_material_type
domain_of:
- PurchasedMaterial
range: string
required: true

```
</details>