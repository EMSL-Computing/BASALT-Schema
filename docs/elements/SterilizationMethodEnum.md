# Enum: SterilizationMethodEnum 




_Method used to sterilize media or other entities._



URI: [analysis_api_schema:SterilizationMethodEnum](https://w3id.org/MONet/analysis-api-schema/SterilizationMethodEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| autoclave | None | Autoclaved |
| filter | None | Filter-sterilised (typically 0 |
| uv | None | UV-sterilised |
| none | None | Not sterilised (used as-is) |




## Slots

| Name | Description |
| ---  | --- |
| [sterilization_method](sterilization_method.md) | Method used to sterilize the entity (autoclave, filter, UV, etc |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema






## LinkML Source

<details>
```yaml
name: SterilizationMethodEnum
description: Method used to sterilize media or other entities.
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
permissible_values:
  autoclave:
    text: autoclave
    description: Autoclaved
  filter:
    text: filter
    description: Filter-sterilised (typically 0.22 μm)
  uv:
    text: uv
    description: UV-sterilised
  none:
    text: none
    description: Not sterilised (used as-is)

```
</details>