# Enum: SampleStoreTempEnum 




_Sample storage temperature conditions_



URI: [SampleStoreTempEnum](SampleStoreTempEnum.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| fresh4 | None | Fresh storage at 4°C |
| freshroom | None | Fresh storage at room temperature |
| frozen20 | None | Frozen storage at -20°C |
| frozen80 | None | Frozen storage at -80°C |
| other | None | Other storage temperature |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema






## LinkML Source

<details>
```yaml
name: SampleStoreTempEnum
description: Sample storage temperature conditions
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
permissible_values:
  fresh4:
    text: fresh4
    description: Fresh storage at 4°C
    aliases:
    - 4 C
  freshroom:
    text: freshroom
    description: Fresh storage at room temperature
    aliases:
    - room temperature
  frozen20:
    text: frozen20
    description: Frozen storage at -20°C
    aliases:
    - -20 C
  frozen80:
    text: frozen80
    description: Frozen storage at -80°C
    aliases:
    - -80 C
  other:
    text: other
    description: Other storage temperature

```
</details>
