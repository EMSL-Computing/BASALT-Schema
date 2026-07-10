

# Class: TextureMethod 



URI: [analysis_api_schema:TextureMethod](https://w3id.org/MONet/analysis-api-schema/TextureMethod)






```mermaid
 classDiagram
    class TextureMethod
    click TextureMethod href "../TextureMethod"
      Method <|-- TextureMethod
        click Method href "../Method"
      
      TextureMethod : analytic
        
      TextureMethod : location
        
      TextureMethod : method
        
      
```





## Inheritance
* [Method](Method.md)
    * **TextureMethod**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [location](location.md) | 1 <br/> [String](String.md) |  | direct |
| [method](method.md) | 0..1 <br/> [String](String.md) |  | direct |
| [analytic](analytic.md) | 1 <br/> [String](String.md) |  | [Method](Method.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:TextureMethod |
| native | analysis_api_schema:TextureMethod |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TextureMethod
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
is_a: Method
slots:
- location
- method

```
</details>

### Induced

<details>
```yaml
name: TextureMethod
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
is_a: Method
attributes:
  location:
    name: location
    todos:
    - used on many method classes. no description. what was this meant to mean?
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: location
    owner: TextureMethod
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
    owner: TextureMethod
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
    owner: TextureMethod
    domain_of:
    - Method
    range: string
    required: true

```
</details>