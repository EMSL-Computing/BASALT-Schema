

# Slot: label_text 


_The label on the stored processed sample, if applicable (e.g., "f01")._





URI: [analysis_api_schema:label_text](https://w3id.org/MONet/analysis-api-schema/label_text)
Alias: label_text

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProcessedSample](ProcessedSample.md) | A sample that has undergone processing or analysis |  no  |
| [CoreSection](CoreSection.md) | A section of a core sample (TOP, MID, BTM) |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:label_text |
| native | analysis_api_schema:label_text |




## LinkML Source

<details>
```yaml
name: label_text
description: The label on the stored processed sample, if applicable (e.g., "f01").
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: label_text
domain_of:
- ProcessedSample
range: string

```
</details>