

# Class: PHMethod 



URI: [basalt_schema:PHMethod](https://EMSL-Computing.github.io/basalt-schema/PHMethod)





```mermaid
 classDiagram
    class PHMethod
    click PHMethod href "../PHMethod/"
      Method <|-- PHMethod
        click Method href "../Method/"
      
      PHMethod : analytic
        
      PHMethod : calibration
        
      PHMethod : location
        
      
```





## Inheritance
* [Method](Method.md)
    * **PHMethod**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [location](location.md) | 1 <br/> [String](String.md) |  | direct |
| [calibration](calibration.md) | 1 <br/> [String](String.md) |  | direct |
| [analytic](analytic.md) | 1 <br/> [String](String.md) |  | [Method](Method.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:PHMethod |
| native | basalt_schema:PHMethod |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PH_Method
from_schema: https://EMSL-Computing.github.io/basalt-schema
is_a: Method
slots:
- location
attributes:
  calibration:
    name: calibration
    from_schema: https://EMSL-Computing.github.io/basalt-schema/methods
    rank: 1000
    domain_of:
    - PH_Method
    range: string
    required: true

```
</details>

### Induced

<details>
```yaml
name: PH_Method
from_schema: https://EMSL-Computing.github.io/basalt-schema
is_a: Method
attributes:
  calibration:
    name: calibration
    from_schema: https://EMSL-Computing.github.io/basalt-schema/methods
    rank: 1000
    alias: calibration
    owner: PH_Method
    domain_of:
    - PH_Method
    range: string
    required: true
  location:
    name: location
    todos:
    - used on many method classes. no description. what was this meant to mean?
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: location
    owner: PH_Method
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
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: analytic
    owner: PH_Method
    domain_of:
    - Method
    range: string
    required: true

```
</details>