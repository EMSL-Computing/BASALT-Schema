

# Slot: parent_workflow_id 


_Self-referential FK to the preceding DataProcessingActivity in a chain._

_NULL -> first (or standalone) step._

_Non-null -> this execution directly follows parent_workflow_id._

_Enables single-hop chaining queries; full traversal via linkage_cache._

__

_DDL: ALTER TABLE "DataProcessingActivity"_

_       ADD COLUMN parent_workflow_id UUID_

_       REFERENCES "DataProcessingActivity"(id);_





URI: [basalt_schema:parent_workflow_id](https://emsl-computing.github.io/BASALT-Schema/elements/parent_workflow_id)
Alias: parent_workflow_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MetagenomicsDataProcessingActivity](MetagenomicsDataProcessingActivity.md) | Concrete metagenomics workflow run |  no  |
| [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md) | Concrete mass spectrometry workflow run |  no  |
| [DataProcessingActivity](DataProcessingActivity.md) | Abstract base for any data processing activity (digital to digital) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DataProcessingActivity](DataProcessingActivity.md) |
| Domain Of | [DataProcessingActivity](DataProcessingActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:parent_workflow_id |
| native | basalt_schema:parent_workflow_id |




## LinkML Source

<details>
```yaml
name: parent_workflow_id
description: "Self-referential FK to the preceding DataProcessingActivity in a chain.\n\
  NULL -> first (or standalone) step.\nNon-null -> this execution directly follows\
  \ parent_workflow_id.\nEnables single-hop chaining queries; full traversal via linkage_cache.\n\
  \nDDL: ALTER TABLE \"DataProcessingActivity\"\n       ADD COLUMN parent_workflow_id\
  \ UUID\n       REFERENCES \"DataProcessingActivity\"(id);"
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: parent_workflow_id
domain_of:
- DataProcessingActivity
range: DataProcessingActivity
required: false

```
</details>