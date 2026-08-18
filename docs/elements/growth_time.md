

# Slot: growth_time 


_Total growth time for the culture._

_Required for ExperimentalCulture activities._





URI: [basalt_schema:growth_time](https://EMSL-Computing.github.io/BASALT-Schema/growth_time)
Alias: growth_time

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalCulture](ExperimentalCulture.md) | Growth of an experimental culture for downstream analysis |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ExperimentalCulture](ExperimentalCulture.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:growth_time |
| native | basalt_schema:growth_time |




## LinkML Source

<details>
```yaml
name: growth_time
description: 'Total growth time for the culture.

  Required for ExperimentalCulture activities.'
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: growth_time
domain_of:
- ExperimentalCulture
range: string

```
</details>