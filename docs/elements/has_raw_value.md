

# Slot: has_raw_value 



URI: [analysis_api_schema:has_raw_value](https://w3id.org/MONet/analysis-api-schema/has_raw_value)
Alias: has_raw_value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuantityValue](QuantityValue.md) | A quantity value with numeric value and optional unit |  no  |
| [ControlledTermValue](ControlledTermValue.md) |  |  no  |
| [ConditioningValue](ConditioningValue.md) |  |  no  |
| [SoftwareControlledTermValue](SoftwareControlledTermValue.md) |  |  no  |
| [TimestampValue](TimestampValue.md) |  |  no  |
| [TextValue](TextValue.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information








## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:has_raw_value |
| native | analysis_api_schema:has_raw_value |




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