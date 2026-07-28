# Enum: SamplePortionEnum 



URI: [analysis_api_schema:SamplePortionEnum](https://w3id.org/MONet/analysis-api-schema/SamplePortionEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| supernatant | None |  ||
| pellet | None |  ||
| organic_layer | None | The portion of a mixture containing dissolved organic material | Title: Organic layer<br>|
| aqueous_layer | None | The portion of a mixture containing molecules dissolved in water | Title: Aqueous layer<br>|
| interlayer | None | The layer of material between liquid layers of a separated mixture | Title: Interlayer<br>|
| chloroform_layer | None | The portion of a mixture containing molecules dissolved in chloroform | Title: Chloroform layer<br> Is-A: NONE<br>|
| methanol_layer | None | The portion of a mixture containing molecules dissolved in methanol | Title: Methanol layer<br> Is-A: NONE<br>|




## Slots

| Name | Description |
| ---  | --- |
| [sampled_portion](sampled_portion.md) | The portion of the original sample used in creating this processed sample (e |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema






## LinkML Source

<details>
```yaml
name: SamplePortionEnum
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
permissible_values:
  supernatant:
    text: supernatant
    aliases:
    - top_layer
  pellet:
    text: pellet
    aliases:
    - bottom_layer
  organic_layer:
    text: organic_layer
    description: The portion of a mixture containing dissolved organic material
    title: Organic layer
  aqueous_layer:
    text: aqueous_layer
    description: The portion of a mixture containing molecules dissolved in water
    title: Aqueous layer
    aliases:
    - water layer
  interlayer:
    text: interlayer
    description: The layer of material between liquid layers of a separated mixture
    title: Interlayer
  chloroform_layer:
    text: chloroform_layer
    description: The portion of a mixture containing molecules dissolved in chloroform
    is_a: organic_layer
    title: Chloroform layer
  methanol_layer:
    text: methanol_layer
    description: The portion of a mixture containing molecules dissolved in methanol
    is_a: organic_layer
    title: Methanol layer

```
</details>