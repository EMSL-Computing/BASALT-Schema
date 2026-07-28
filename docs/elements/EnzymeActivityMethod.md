

# Class: EnzymeActivityMethod 



URI: [analysis_api_schema:EnzymeActivityMethod](https://w3id.org/MONet/analysis-api-schema/EnzymeActivityMethod)





```mermaid
 classDiagram
    class EnzymeActivityMethod
    click EnzymeActivityMethod href "../EnzymeActivityMethod/"
      Method <|-- EnzymeActivityMethod
        click Method href "../Method/"
      
      EnzymeActivityMethod : analytic
        
      EnzymeActivityMethod : incubation_temp_c
        
      EnzymeActivityMethod : incubation_time
        
      EnzymeActivityMethod : location
        
      EnzymeActivityMethod : wavelength
        
      
```





## Inheritance
* [Method](Method.md)
    * **EnzymeActivityMethod**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [location](location.md) | 1 <br/> [String](String.md) |  | direct |
| [incubation_temp_c](incubation_temp_c.md) | 0..1 <br/> [Double](Double.md) |  | direct |
| [incubation_time](incubation_time.md) | 0..1 <br/> [String](String.md) |  | direct |
| [wavelength](wavelength.md) | 0..1 <br/> [Double](Double.md) |  | direct |
| [analytic](analytic.md) | 1 <br/> [String](String.md) |  | [Method](Method.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:EnzymeActivityMethod |
| native | analysis_api_schema:EnzymeActivityMethod |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EnzymeActivityMethod
from_schema: https://w3id.org/MONet/analysis-api-schema
is_a: Method
slots:
- location
attributes:
  incubation_temp_c:
    name: incubation_temp_c
    from_schema: https://w3id.org/MONet/analysis-api-schema/methods
    rank: 1000
    domain_of:
    - EnzymeActivityMethod
    range: double
  incubation_time:
    name: incubation_time
    from_schema: https://w3id.org/MONet/analysis-api-schema/methods
    rank: 1000
    domain_of:
    - EnzymeActivityMethod
    range: string
  wavelength:
    name: wavelength
    from_schema: https://w3id.org/MONet/analysis-api-schema/methods
    rank: 1000
    domain_of:
    - EnzymeActivityMethod
    - KuoMethod
    range: double

```
</details>

### Induced

<details>
```yaml
name: EnzymeActivityMethod
from_schema: https://w3id.org/MONet/analysis-api-schema
is_a: Method
attributes:
  incubation_temp_c:
    name: incubation_temp_c
    from_schema: https://w3id.org/MONet/analysis-api-schema/methods
    rank: 1000
    alias: incubation_temp_c
    owner: EnzymeActivityMethod
    domain_of:
    - EnzymeActivityMethod
    range: double
  incubation_time:
    name: incubation_time
    from_schema: https://w3id.org/MONet/analysis-api-schema/methods
    rank: 1000
    alias: incubation_time
    owner: EnzymeActivityMethod
    domain_of:
    - EnzymeActivityMethod
    range: string
  wavelength:
    name: wavelength
    from_schema: https://w3id.org/MONet/analysis-api-schema/methods
    rank: 1000
    alias: wavelength
    owner: EnzymeActivityMethod
    domain_of:
    - EnzymeActivityMethod
    - KuoMethod
    range: double
  location:
    name: location
    todos:
    - used on many method classes. no description. what was this meant to mean?
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: location
    owner: EnzymeActivityMethod
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
  analytic:
    name: analytic
    todos:
    - what does this mean
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: analytic
    owner: EnzymeActivityMethod
    domain_of:
    - Method
    range: string
    required: true

```
</details>