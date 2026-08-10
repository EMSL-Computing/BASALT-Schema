# Enum: CalibrationTargetEnum 



URI: [basalt_schema:CalibrationTargetEnum](https://w3id.org/MONet/basalt-schema/CalibrationTargetEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| mass_charge_ratio | None |  | Title: m/z<br>|
| retention_time | None |  ||
| retention_index | None |  ||




## Slots

| Name | Description |
| ---  | --- |
| [calibration_target](calibration_target.md) | The measurement being calibrated |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema






## LinkML Source

<details>
```yaml
name: CalibrationTargetEnum
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
permissible_values:
  mass_charge_ratio:
    text: mass_charge_ratio
    title: m/z
    aliases:
    - Mass
    - m/z
  retention_time:
    text: retention_time
    aliases:
    - RT
  retention_index:
    text: retention_index
    aliases:
    - RI

```
</details>