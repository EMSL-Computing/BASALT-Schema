

# Class: MicrobialBiomassMethod 



URI: [basalt_schema:MicrobialBiomassMethod](https://EMSL-Computing.github.io/basalt-schema/MicrobialBiomassMethod)





```mermaid
 classDiagram
    class MicrobialBiomassMethod
    click MicrobialBiomassMethod href "../MicrobialBiomassMethod/"
      Method <|-- MicrobialBiomassMethod
        click Method href "../Method/"
      
      MicrobialBiomassMethod : analytic
        
      MicrobialBiomassMethod : check_standard_spacing
        
      MicrobialBiomassMethod : detector
        
      MicrobialBiomassMethod : injection_volume
        
      MicrobialBiomassMethod : location
        
      MicrobialBiomassMethod : mode
        
      MicrobialBiomassMethod : number_of_injections
        
      MicrobialBiomassMethod : sample_volume
        
      
```





## Inheritance
* [Method](Method.md)
    * **MicrobialBiomassMethod**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [location](location.md) | 1 <br/> [String](String.md) |  | direct |
| [detector](detector.md) | 1 <br/> [String](String.md) |  | direct |
| [mode](mode.md) | 0..1 <br/> [String](String.md) |  | direct |
| [injection_volume](injection_volume.md) | 1 <br/> [String](String.md) |  | direct |
| [sample_volume](sample_volume.md) | 1 <br/> [String](String.md) |  | direct |
| [number_of_injections](number_of_injections.md) | 1 <br/> [Double](Double.md) |  | direct |
| [check_standard_spacing](check_standard_spacing.md) | 1 <br/> [String](String.md) |  | direct |
| [analytic](analytic.md) | 1 <br/> [String](String.md) |  | [Method](Method.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:MicrobialBiomassMethod |
| native | basalt_schema:MicrobialBiomassMethod |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MicrobialBiomassMethod
from_schema: https://EMSL-Computing.github.io/basalt-schema
is_a: Method
slots:
- location
attributes:
  detector:
    name: detector
    from_schema: https://EMSL-Computing.github.io/basalt-schema/methods
    rank: 1000
    domain_of:
    - MicrobialBiomassMethod
    - TOC_TN_Method
    range: string
    required: true
  mode:
    name: mode
    from_schema: https://EMSL-Computing.github.io/basalt-schema/methods
    rank: 1000
    domain_of:
    - MicrobialBiomassMethod
    - TOC_TN_Method
    range: string
  injection_volume:
    name: injection_volume
    from_schema: https://EMSL-Computing.github.io/basalt-schema/methods
    rank: 1000
    domain_of:
    - MicrobialBiomassMethod
    - TOC_TN_Method
    range: string
    required: true
  sample_volume:
    name: sample_volume
    from_schema: https://EMSL-Computing.github.io/basalt-schema/methods
    rank: 1000
    domain_of:
    - MicrobialBiomassMethod
    - TOC_TN_Method
    range: string
    required: true
  number_of_injections:
    name: number_of_injections
    from_schema: https://EMSL-Computing.github.io/basalt-schema/methods
    rank: 1000
    domain_of:
    - MicrobialBiomassMethod
    - TOC_TN_Method
    range: double
    required: true
  check_standard_spacing:
    name: check_standard_spacing
    from_schema: https://EMSL-Computing.github.io/basalt-schema/methods
    rank: 1000
    domain_of:
    - MicrobialBiomassMethod
    - TOC_TN_Method
    range: string
    required: true

```
</details>

### Induced

<details>
```yaml
name: MicrobialBiomassMethod
from_schema: https://EMSL-Computing.github.io/basalt-schema
is_a: Method
attributes:
  detector:
    name: detector
    from_schema: https://EMSL-Computing.github.io/basalt-schema/methods
    rank: 1000
    alias: detector
    owner: MicrobialBiomassMethod
    domain_of:
    - MicrobialBiomassMethod
    - TOC_TN_Method
    range: string
    required: true
  mode:
    name: mode
    from_schema: https://EMSL-Computing.github.io/basalt-schema/methods
    rank: 1000
    alias: mode
    owner: MicrobialBiomassMethod
    domain_of:
    - MicrobialBiomassMethod
    - TOC_TN_Method
    range: string
  injection_volume:
    name: injection_volume
    from_schema: https://EMSL-Computing.github.io/basalt-schema/methods
    rank: 1000
    alias: injection_volume
    owner: MicrobialBiomassMethod
    domain_of:
    - MicrobialBiomassMethod
    - TOC_TN_Method
    range: string
    required: true
  sample_volume:
    name: sample_volume
    from_schema: https://EMSL-Computing.github.io/basalt-schema/methods
    rank: 1000
    alias: sample_volume
    owner: MicrobialBiomassMethod
    domain_of:
    - MicrobialBiomassMethod
    - TOC_TN_Method
    range: string
    required: true
  number_of_injections:
    name: number_of_injections
    from_schema: https://EMSL-Computing.github.io/basalt-schema/methods
    rank: 1000
    alias: number_of_injections
    owner: MicrobialBiomassMethod
    domain_of:
    - MicrobialBiomassMethod
    - TOC_TN_Method
    range: double
    required: true
  check_standard_spacing:
    name: check_standard_spacing
    from_schema: https://EMSL-Computing.github.io/basalt-schema/methods
    rank: 1000
    alias: check_standard_spacing
    owner: MicrobialBiomassMethod
    domain_of:
    - MicrobialBiomassMethod
    - TOC_TN_Method
    range: string
    required: true
  location:
    name: location
    todos:
    - used on many method classes. no description. what was this meant to mean?
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: location
    owner: MicrobialBiomassMethod
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
    owner: MicrobialBiomassMethod
    domain_of:
    - Method
    range: string
    required: true

```
</details>