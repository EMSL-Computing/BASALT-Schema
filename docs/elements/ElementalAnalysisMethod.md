

# Class: ElementalAnalysisMethod 



URI: [basalt_schema:ElementalAnalysisMethod](https://EMSL-Computing.github.io/BASALT-Schema/ElementalAnalysisMethod)





```mermaid
 classDiagram
    class ElementalAnalysisMethod
    click ElementalAnalysisMethod href "../ElementalAnalysisMethod/"
      Method <|-- ElementalAnalysisMethod
        click Method href "../Method/"
      
      ElementalAnalysisMethod : analytic
        
      
```





## Inheritance
* [Method](Method.md)
    * **ElementalAnalysisMethod**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [analytic](analytic.md) | 1 <br/> [String](String.md) |  | [Method](Method.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:ElementalAnalysisMethod |
| native | basalt_schema:ElementalAnalysisMethod |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ElementalAnalysisMethod
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
is_a: Method

```
</details>

### Induced

<details>
```yaml
name: ElementalAnalysisMethod
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
is_a: Method
attributes:
  analytic:
    name: analytic
    todos:
    - what does this mean
    from_schema: https://EMSL-Computing.github.io/BASALT-Schema
    rank: 1000
    alias: analytic
    owner: ElementalAnalysisMethod
    domain_of:
    - Method
    range: string
    required: true

```
</details>