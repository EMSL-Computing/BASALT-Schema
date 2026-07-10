

# Slot: experimental factor (experimental_factor) 


_Experimental factors are essentially the variable aspects of an experiment design which can be used to describe an experiment or set of experiments in an increasingly detailed manner. This field accepts ontology terms from Experimental Factor Ontology (EFO) and/or Ontology for Biomedical Investigations (OBI). For a browser of EFO (v 2.95) terms please see http://purl.bioontology.org/ontology/EFO; for a browser of OBI (v 2018-02-12) terms please see http://purl.bioontology.org/ontology/OBI_





URI: [analysis_api_schema:experimental_factor](https://w3id.org/MONet/analysis-api-schema/experimental_factor)
Alias: experimental_factor

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |
| [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md) | A sample containing commercially purchased material |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |
| [SynthesizedMaterialSample](SynthesizedMaterialSample.md) | A sample containing synthetically generated material |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:experimental_factor |
| native | analysis_api_schema:experimental_factor |




## LinkML Source

<details>
```yaml
name: experimental_factor
description: Experimental factors are essentially the variable aspects of an experiment
  design which can be used to describe an experiment or set of experiments in an increasingly
  detailed manner. This field accepts ontology terms from Experimental Factor Ontology
  (EFO) and/or Ontology for Biomedical Investigations (OBI). For a browser of EFO
  (v 2.95) terms please see http://purl.bioontology.org/ontology/EFO; for a browser
  of OBI (v 2018-02-12) terms please see http://purl.bioontology.org/ontology/OBI
title: experimental factor
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: experimental_factor
domain_of:
- AerosolArmSample
- AerosolSample
- CommerciallyPurchasedSample
- CultureEnvironmentalSample
- MixedCultureSample
- OtherUndescribedSample
- PlantSample
- PureCultureSample
- SedimentSample
- SoilSample
- SynthesizedMaterialSample
- WaterSample
range: string

```
</details>