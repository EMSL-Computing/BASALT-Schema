

# Slot: heavy metals (heavy_metals) 


_Heavy metals present and concentrations; can include multiple heavy metals and concentrations_





URI: [analysis_api_schema:heavy_metals](https://w3id.org/MONet/analysis-api-schema/heavy_metals)
Alias: heavy_metals

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  yes  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:heavy_metals |
| native | analysis_api_schema:heavy_metals |




## LinkML Source

<details>
```yaml
name: heavy_metals
description: Heavy metals present and concentrations; can include multiple heavy metals
  and concentrations
title: heavy metals
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: heavy_metals
domain_of:
- OtherUndescribedSample
- SoilSample
range: string

```
</details>