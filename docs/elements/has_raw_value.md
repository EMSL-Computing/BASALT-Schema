

# Slot: has_raw_value 



URI: [basalt_schema:has_raw_value](https://EMSL-Computing.github.io/BASALT-Schema/has_raw_value)
Alias: has_raw_value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TimestampValue](TimestampValue.md) | A timestamp value with optional description |  no  |
| [TextValue](TextValue.md) | A text value with optional description and language |  no  |
| [SoftwareControlledTermValue](SoftwareControlledTermValue.md) |  |  no  |
| [ConditioningValue](ConditioningValue.md) |  |  no  |
| [QuantityValue](QuantityValue.md) | A quantity value with numeric value and optional unit |  no  |
| [ControlledTermValue](ControlledTermValue.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [TimestampValue](TimestampValue.md), [TextValue](TextValue.md), [SoftwareControlledTermValue](SoftwareControlledTermValue.md), [ControlledTermValue](ControlledTermValue.md), [QuantityValue](QuantityValue.md), [ConditioningValue](ConditioningValue.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:has_raw_value |
| native | basalt_schema:has_raw_value |




## LinkML Source

<details>
```yaml
name: has_raw_value
alias: has_raw_value
domain_of:
- TimestampValue
- TextValue
- SoftwareControlledTermValue
- ControlledTermValue
- QuantityValue
- ConditioningValue
range: string

```
</details>