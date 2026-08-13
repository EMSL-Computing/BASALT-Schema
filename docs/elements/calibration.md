

# Slot: calibration 



URI: [basalt_schema:calibration](https://EMSL-Computing.github.io/BASALT-Schema/calibration)
Alias: calibration

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PHMethod](PHMethod.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PHMethod](PHMethod.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PHMethod](PHMethod.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:calibration |
| native | basalt_schema:calibration |




## LinkML Source

<details>
```yaml
name: calibration
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: calibration
owner: PH_Method
domain_of:
- PH_Method
range: string
required: true

```
</details>