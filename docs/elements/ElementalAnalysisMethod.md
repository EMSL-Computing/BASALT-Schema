

# Class: ElementalAnalysisMethod 



URI: [analysis_api_schema:ElementalAnalysisMethod](https://w3id.org/MONet/analysis-api-schema/ElementalAnalysisMethod)





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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:ElementalAnalysisMethod |
| native | analysis_api_schema:ElementalAnalysisMethod |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ElementalAnalysisMethod
from_schema: https://w3id.org/MONet/analysis-api-schema
is_a: Method

```
</details>

### Induced

<details>
```yaml
name: ElementalAnalysisMethod
from_schema: https://w3id.org/MONet/analysis-api-schema
is_a: Method
attributes:
  analytic:
    name: analytic
    todos:
    - what does this mean
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: analytic
    owner: ElementalAnalysisMethod
    domain_of:
    - Method
    range: string
    required: true

```
</details>