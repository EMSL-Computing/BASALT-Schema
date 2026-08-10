

# Slot: external_identifiers 


_List of external identifiers associated with this entity or activity._





URI: [basalt_schema:external_identifiers](https://w3id.org/MONet/basalt-schema/external_identifiers)
Alias: external_identifiers

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [MonetSoilSample](MonetSoilSample.md) | A soil sample that has been collected according to the MONet soil sampling pr... |  no  |
| [EngineeredStrainSample](EngineeredStrainSample.md) | A sample containing a strain of an organism that has been subjected to geneti... |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md) | A sample containing commercially purchased material |  no  |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SynthesizedMaterialSample](SynthesizedMaterialSample.md) | A sample containing synthetically generated material |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [Study](Study.md) | A study or research project, typically associated with a proposal and a set o... |  yes  |
| [NucleotideSequencing](NucleotideSequencing.md) | A lab activity in which DNA or RNA that was extracted from a sample is sequen... |  yes  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [NucleotideSequencing](NucleotideSequencing.md), [AerosolArmSample](AerosolArmSample.md), [AerosolSample](AerosolSample.md), [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md), [CultureEnvironmentalSample](CultureEnvironmentalSample.md), [EngineeredStrainSample](EngineeredStrainSample.md), [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [MixedCultureSample](MixedCultureSample.md), [MonetSoilSample](MonetSoilSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [PlantSample](PlantSample.md), [PureCultureSample](PureCultureSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md), [SynthesizedMaterialSample](SynthesizedMaterialSample.md), [TerraformSample](TerraformSample.md), [WaterSample](WaterSample.md), [Study](Study.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:external_identifiers |
| native | basalt_schema:external_identifiers |




## LinkML Source

<details>
```yaml
name: external_identifiers
description: List of external identifiers associated with this entity or activity.
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: external_identifiers
domain_of:
- NucleotideSequencing
- AerosolArmSample
- AerosolSample
- CommerciallyPurchasedSample
- CultureEnvironmentalSample
- EngineeredStrainSample
- FieldDeployedTerraformSample
- MixedCultureSample
- MonetSoilSample
- OtherUndescribedSample
- PlantSample
- PureCultureSample
- SedimentSample
- SoilSample
- SynthesizedMaterialSample
- TerraformSample
- WaterSample
- Study
range: uriorcurie
multivalued: true

```
</details>