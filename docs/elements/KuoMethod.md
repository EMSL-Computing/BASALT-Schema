

# Class: KuoMethod 



URI: [analysis_api_schema:KuoMethod](https://w3id.org/MONet/analysis-api-schema/KuoMethod)





```mermaid
 classDiagram
    class KuoMethod
    click KuoMethod href "../KuoMethod/"
      Method <|-- KuoMethod
        click Method href "../Method/"
      
      KuoMethod : analytic
        
      KuoMethod : detection_limit
        
      KuoMethod : location
        
      KuoMethod : method
        
      KuoMethod : wavelength
        
      
```





## Inheritance
* [Method](Method.md)
    * **KuoMethod**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [location](location.md) | 1 <br/> [String](String.md) |  | direct |
| [method](method.md) | 0..1 <br/> [String](String.md) |  | direct |
| [detection_limit](detection_limit.md) | 1 <br/> [String](String.md) |  | direct |
| [wavelength](wavelength.md) | 0..1 <br/> [String](String.md) |  | direct |
| [analytic](analytic.md) | 1 <br/> [String](String.md) |  | [Method](Method.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:KuoMethod |
| native | analysis_api_schema:KuoMethod |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: KuoMethod
from_schema: https://w3id.org/MONet/analysis-api-schema
is_a: Method
slots:
- location
- method
attributes:
  detection_limit:
    name: detection_limit
    from_schema: https://w3id.org/MONet/analysis-api-schema/methods
    rank: 1000
    domain_of:
    - KuoMethod
    range: string
    required: true
  wavelength:
    name: wavelength
    from_schema: https://w3id.org/MONet/analysis-api-schema/methods
    domain_of:
    - EnzymeActivityMethod
    - KuoMethod
    range: string

```
</details>

### Induced

<details>
```yaml
name: KuoMethod
from_schema: https://w3id.org/MONet/analysis-api-schema
is_a: Method
attributes:
  detection_limit:
    name: detection_limit
    from_schema: https://w3id.org/MONet/analysis-api-schema/methods
    rank: 1000
    alias: detection_limit
    owner: KuoMethod
    domain_of:
    - KuoMethod
    range: string
    required: true
  wavelength:
    name: wavelength
    from_schema: https://w3id.org/MONet/analysis-api-schema/methods
    alias: wavelength
    owner: KuoMethod
    domain_of:
    - EnzymeActivityMethod
    - KuoMethod
    range: string
  location:
    name: location
    todos:
    - used on many method classes. no description. what was this meant to mean?
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: location
    owner: KuoMethod
    domain_of:
    - Instrument
    - EnzymeActivityMethod
    - GravimetricWaterContentMethod
    - HydraulicPropertiesMethod
    - KuoMethod
    - MicrobialBiomassMethod
    - PH_Method
    - TOC_TN_Method
    - TextureMethod
    - XrayComputedTomographyMethod
    range: string
    required: true
  method:
    name: method
    todos:
    - what does this mean
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: method
    owner: KuoMethod
    domain_of:
    - KuoMethod
    - TextureMethod
    range: string
  analytic:
    name: analytic
    todos:
    - what does this mean
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: analytic
    owner: KuoMethod
    domain_of:
    - Method
    range: string
    required: true

```
</details>