

# Slot: workflow_id 



URI: [basalt_schema:workflow_id](https://w3id.org/MONet/basalt-schema/workflow_id)
Alias: workflow_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WorkflowExecutionFunctionalAnnotation](WorkflowExecutionFunctionalAnnotation.md) | A link between a workflow execution and a functional annotation identifier |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DataProcessingActivity](DataProcessingActivity.md) |
| Domain Of | [WorkflowExecutionFunctionalAnnotation](WorkflowExecutionFunctionalAnnotation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [WorkflowExecutionFunctionalAnnotation](WorkflowExecutionFunctionalAnnotation.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:workflow_id |
| native | basalt_schema:workflow_id |




## LinkML Source

<details>
```yaml
name: workflow_id
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: workflow_id
owner: WorkflowExecutionFunctionalAnnotation
domain_of:
- WorkflowExecutionFunctionalAnnotation
range: DataProcessingActivity
required: true

```
</details>