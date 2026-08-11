

# Slot: calibration_target 


_The measurement being calibrated_





URI: [basalt_schema:calibration_target](https://EMSL-Computing.github.io/basalt-schema/calibration_target)
Alias: calibration_target

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryStandardRun](MassSpectrometryStandardRun.md) | A record of a mass spectrometry standard run with a batch of samples, which i... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CalibrationTargetEnum](CalibrationTargetEnum.md) |
| Domain Of | [MassSpectrometryStandardRun](MassSpectrometryStandardRun.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:calibration_target |
| native | basalt_schema:calibration_target |




## LinkML Source

<details>
```yaml
name: calibration_target
description: The measurement being calibrated
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: calibration_target
domain_of:
- MassSpectrometryStandardRun
range: CalibrationTargetEnum

```
</details>