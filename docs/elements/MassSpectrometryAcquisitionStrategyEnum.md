# Enum: MassSpectrometryAcquisitionStrategyEnum 



URI: [basalt_schema:MassSpectrometryAcquisitionStrategyEnum](https://w3id.org/MONet/basalt-schema/MassSpectrometryAcquisitionStrategyEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| data_independent_acquisition | None | Data independent mass spectrometer acquisition method wherein the full mass r... |
| data_dependent_acquisition | None | Mass spectrometer data acquisition method wherein MSn spectra are triggered b... |
| full_scan_only | None | Mass spectrometer data acquisition method wherein only MS1 data are acquired |




## Slots

| Name | Description |
| ---  | --- |
| [acquisition_strategy](acquisition_strategy.md) | The acquisition strategy used in the mass spectrometry run |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema






## LinkML Source

<details>
```yaml
name: MassSpectrometryAcquisitionStrategyEnum
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
permissible_values:
  data_independent_acquisition:
    text: data_independent_acquisition
    description: Data independent mass spectrometer acquisition method wherein the
      full mass range is fragmented. Examples of such an approach include MS^E, AIF,
      and bbCID.
    aliases:
    - DIA
    - data independent acquisition from dissociation of full mass range
    exact_mappings:
    - MS:1003227
  data_dependent_acquisition:
    text: data_dependent_acquisition
    description: Mass spectrometer data acquisition method wherein MSn spectra are
      triggered based on the m/z of precursor ions detected in the same run.
    aliases:
    - DDA
    exact_mappings:
    - MS:1003221
  full_scan_only:
    text: full_scan_only
    description: Mass spectrometer data acquisition method wherein only MS1 data are
      acquired.
    aliases:
    - MS

```
</details>