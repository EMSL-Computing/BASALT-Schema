

# Slot: device_type 



URI: [basalt_schema:device_type](https://EMSL-Computing.github.io/BASALT-Schema/device_type)
Alias: device_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LabDevice](LabDevice.md) | A lab device is a physical instrument or equipment used in a laboratory setti... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DeviceTypeEnum](DeviceTypeEnum.md) |
| Domain Of | [LabDevice](LabDevice.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [LabDevice](LabDevice.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:device_type |
| native | basalt_schema:device_type |




## LinkML Source

<details>
```yaml
name: device_type
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: device_type
owner: LabDevice
domain_of:
- LabDevice
range: DeviceTypeEnum

```
</details>