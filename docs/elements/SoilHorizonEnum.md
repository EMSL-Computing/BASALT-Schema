# Enum: SoilHorizonEnum 




_Soil horizon classifications_



URI: [SoilHorizonEnum](SoilHorizonEnum.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| a_horizon | None | The surface horizon, also called topsoil |
| b_horizon | None | Also known as the subsoil |
| c_horizon | None | Also known as the substratum is unconsolidated material deepest in the pit an... |
| e_horizon | None | Used to refer to subsurface horizons that have undergone a significant loss o... |
| o_horizon | None | The organic horizon |
| permafrost | None | Soil that continuously remains below 0 °C (32 °F) for two years or more |
| r_layer | None | Hard bedrock, which is usually the lowest layer |
| m_horizon | None | Mineral horizon |




## Slots

| Name | Description |
| ---  | --- |
| [soil_horizon](soil_horizon.md) | Specific layer in the land area which measures parallel to the soil surface a... |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema






## LinkML Source

<details>
```yaml
name: SoilHorizonEnum
description: Soil horizon classifications
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
permissible_values:
  a_horizon:
    text: a_horizon
    description: The surface horizon, also called topsoil. It has a defined soil structure,
      and is mostly made up of humus (decayed organic matter).
    aliases:
    - A_Horizon
  b_horizon:
    text: b_horizon
    description: Also known as the subsoil. It is greatly composed of material illuviated
      (washed in from) layers above it. It is typically denser than the A horizon
      and has a clayey texture.
    aliases:
    - B_Horizon
  c_horizon:
    text: c_horizon
    description: Also known as the substratum is unconsolidated material deepest in
      the pit and closest to the bedrock.
    aliases:
    - C_Horizon
  e_horizon:
    text: e_horizon
    description: Used to refer to subsurface horizons that have undergone a significant
      loss of minerals, also known as Eluviation (or leaching).
    aliases:
    - E_Horizon
  o_horizon:
    text: o_horizon
    description: The organic horizon. Typically at the top of the soil structure and
      is made up of mostly organic matter.
    aliases:
    - O_Horizon
  permafrost:
    text: permafrost
    description: Soil that continuously remains below 0 °C (32 °F) for two years or
      more.
    aliases:
    - Permafrost
  r_layer:
    text: r_layer
    description: Hard bedrock, which is usually the lowest layer. It is characterized
      by tightly bound and unbreakable materials.
    aliases:
    - R_Layer
  m_horizon:
    text: m_horizon
    description: Mineral horizon
    aliases:
    - M_Horizon

```
</details>
