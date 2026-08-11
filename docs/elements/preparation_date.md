

# Slot: preparation_date 


_Date the stock culture or entity was prepared_





URI: [basalt_schema:preparation_date](https://EMSL-Computing.github.io/basalt-schema/preparation_date)
Alias: preparation_date

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StockCulturePreparation](StockCulturePreparation.md) | Preparation of a stock culture from user samples for long-term storage |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [StockCulturePreparation](StockCulturePreparation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:preparation_date |
| native | basalt_schema:preparation_date |




## LinkML Source

<details>
```yaml
name: preparation_date
description: Date the stock culture or entity was prepared
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: preparation_date
domain_of:
- StockCulturePreparation
range: date

```
</details>