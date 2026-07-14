

# Slot: sampled_portion 


_The portion of the original sample used in creating this processed sample (e.g., "interlayer", "supernatant", "pellet")._





URI: [analysis_api_schema:sampled_portion](https://w3id.org/MONet/analysis-api-schema/sampled_portion)
Alias: sampled_portion

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CoreSection](CoreSection.md) | A section of a core sample (TOP, MID, BTM) |  no  |
| [ProcessedSample](ProcessedSample.md) | A sample that has undergone processing or analysis |  no  |







## Properties

* Range: [SamplePortionEnum](SamplePortionEnum.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:sampled_portion |
| native | analysis_api_schema:sampled_portion |




## LinkML Source

<details>
```yaml
name: sampled_portion
description: The portion of the original sample used in creating this processed sample
  (e.g., "interlayer", "supernatant", "pellet").
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: sampled_portion
domain_of:
- ProcessedSample
range: SamplePortionEnum

```
</details>