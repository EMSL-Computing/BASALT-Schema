

# Slot: guid_source 


_Source system for the sample GUID (e.g., "LIMS")._





URI: [analysis_api_schema:guid_source](https://w3id.org/MONet/analysis-api-schema/guid_source)
Alias: guid_source

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AMP2UserSample](AMP2UserSample.md) | A user-submitted microbial sample for AMP2 workflows |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AMP2UserSample](AMP2UserSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:guid_source |
| native | analysis_api_schema:guid_source |




## LinkML Source

<details>
```yaml
name: guid_source
description: Source system for the sample GUID (e.g., "LIMS").
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: guid_source
domain_of:
- AMP2UserSample
range: string

```
</details>