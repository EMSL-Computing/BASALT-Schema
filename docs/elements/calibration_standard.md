

# Slot: calibration_standard 


_The reference standard used for calibration_





URI: [basalt_schema:calibration_standard](https://EMSL-Computing.github.io/BASALT-Schema/calibration_standard)
Alias: calibration_standard

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryStandardRun](MassSpectrometryStandardRun.md) | A record of a mass spectrometry standard run with a batch of samples, which i... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PurchasedMaterial](PurchasedMaterial.md) |
| Domain Of | [MassSpectrometryStandardRun](MassSpectrometryStandardRun.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:calibration_standard |
| native | basalt_schema:calibration_standard |




## LinkML Source

<details>
```yaml
name: calibration_standard
description: The reference standard used for calibration
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: calibration_standard
domain_of:
- MassSpectrometryStandardRun
range: PurchasedMaterial

```
</details>