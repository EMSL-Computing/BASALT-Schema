

# Class: ContainerAxis 



URI: [analysis_api_schema:ContainerAxis](https://w3id.org/MONet/analysis-api-schema/ContainerAxis)





```mermaid
 classDiagram
    class ContainerAxis
    click ContainerAxis href "../ContainerAxis/"
      ContainerAxis : name
        
      ContainerAxis : values
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 0..1 <br/> [String](String.md) |  | direct |
| [values](values.md) | * <br/> [String](String.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ContainerType](ContainerType.md) | [axes](axes.md) | range | [ContainerAxis](ContainerAxis.md) |










## TODOs

* I'm only including this in case we need it to sync up with L7 in some way



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:ContainerAxis |
| native | analysis_api_schema:ContainerAxis |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ContainerAxis
todos:
- I'm only including this in case we need it to sync up with L7 in some way
from_schema: https://w3id.org/MONet/analysis-api-schema
attributes:
  name:
    name: name
    from_schema: https://w3id.org/MONet/analysis-api-schema
    domain_of:
    - Activity
    - Entity
    - DataProduct
    - DataGenerationActivity
    - Instrument
    - OntologyClass
    - ContainerAxis
    - Configuration
    - MobilePhaseSegment
    - MassSpectrometryStandardRun
    - PurchasedMaterial
    - LabProcessingActivity
    - organism
    - Site
    - Sample
    - SamplingActivity
    - SoilSamplingActivity
    - Study
    - SoftwareControlledTermValue
    range: string
  values:
    name: values
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    domain_of:
    - ContainerAxis
    range: string
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: ContainerAxis
todos:
- I'm only including this in case we need it to sync up with L7 in some way
from_schema: https://w3id.org/MONet/analysis-api-schema
attributes:
  name:
    name: name
    from_schema: https://w3id.org/MONet/analysis-api-schema
    alias: name
    owner: ContainerAxis
    domain_of:
    - Activity
    - Entity
    - DataProduct
    - DataGenerationActivity
    - Instrument
    - OntologyClass
    - ContainerAxis
    - Configuration
    - MobilePhaseSegment
    - MassSpectrometryStandardRun
    - PurchasedMaterial
    - LabProcessingActivity
    - organism
    - Site
    - Sample
    - SamplingActivity
    - SoilSamplingActivity
    - Study
    - SoftwareControlledTermValue
    range: string
  values:
    name: values
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: values
    owner: ContainerAxis
    domain_of:
    - ContainerAxis
    range: string
    multivalued: true

```
</details>