

# Slot: method_id 


_Reference to the RespirationMethod used for this run_





URI: [basalt_schema:method_id](https://EMSL-Computing.github.io/basalt-schema/method_id)
Alias: method_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RespirationDataGenerationActivity](RespirationDataGenerationActivity.md) | Data generation activity for soil respiration analysis |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RespirationMethod](RespirationMethod.md) |
| Domain Of | [RespirationDataGenerationActivity](RespirationDataGenerationActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [RespirationDataGenerationActivity](RespirationDataGenerationActivity.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:method_id |
| native | basalt_schema:method_id |




## LinkML Source

<details>
```yaml
name: method_id
description: Reference to the RespirationMethod used for this run
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: method_id
owner: RespirationDataGenerationActivity
domain_of:
- RespirationDataGenerationActivity
range: RespirationMethod

```
</details>