# Enum: StorageConditionEnum 




_Sample storage conditions_



URI: [basalt_schema:StorageConditionEnum](https://emsl-computing.github.io/BASALT-Schema/elements/StorageConditionEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| fresh | None | Fresh sample |
| frozen | None | Frozen sample |
| lyophilized | None | Lyophilized (freeze-dried) sample |
| other | None | Other storage condition |




## Slots

| Name | Description |
| ---  | --- |
| [storage_condition](storage_condition.md) | The storage condition of the sample |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema






## LinkML Source

<details>
```yaml
name: StorageConditionEnum
description: Sample storage conditions
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
permissible_values:
  fresh:
    text: fresh
    description: Fresh sample
  frozen:
    text: frozen
    description: Frozen sample
  lyophilized:
    text: lyophilized
    description: Lyophilized (freeze-dried) sample
  other:
    text: other
    description: Other storage condition

```
</details>