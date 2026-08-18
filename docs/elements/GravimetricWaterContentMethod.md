

# Class: GravimetricWaterContentMethod 



URI: [basalt_schema:GravimetricWaterContentMethod](https://emsl-computing.github.io/BASALT-Schema/elements/GravimetricWaterContentMethod)





```mermaid
 classDiagram
    class GravimetricWaterContentMethod
    click GravimetricWaterContentMethod href "../GravimetricWaterContentMethod/"
      Method <|-- GravimetricWaterContentMethod
        click Method href "../Method/"
      
      GravimetricWaterContentMethod : analytic
        
      GravimetricWaterContentMethod : location
        
      
```





## Inheritance
* [Method](Method.md)
    * **GravimetricWaterContentMethod**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [location](location.md) | 1 <br/> [String](String.md) |  | direct |
| [analytic](analytic.md) | 1 <br/> [String](String.md) |  | [Method](Method.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:GravimetricWaterContentMethod |
| native | basalt_schema:GravimetricWaterContentMethod |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GravimetricWaterContentMethod
from_schema: https://emsl-computing.github.io/BASALT-Schema
is_a: Method
slots:
- location

```
</details>

### Induced

<details>
```yaml
name: GravimetricWaterContentMethod
from_schema: https://emsl-computing.github.io/BASALT-Schema
is_a: Method
attributes:
  location:
    name: location
    todos:
    - used on many method classes. no description. what was this meant to mean?
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: location
    owner: GravimetricWaterContentMethod
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
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: analytic
    owner: GravimetricWaterContentMethod
    domain_of:
    - Method
    range: string
    required: true

```
</details>