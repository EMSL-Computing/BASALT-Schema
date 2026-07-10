

# Class: BulkDensityMethod 



URI: [analysis_api_schema:BulkDensityMethod](https://w3id.org/MONet/analysis-api-schema/BulkDensityMethod)






```mermaid
 classDiagram
    class BulkDensityMethod
    click BulkDensityMethod href "../BulkDensityMethod"
      Method <|-- BulkDensityMethod
        click Method href "../Method"
      
      BulkDensityMethod : analytic
        
      
```





## Inheritance
* [Method](Method.md)
    * **BulkDensityMethod**



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
| self | analysis_api_schema:BulkDensityMethod |
| native | analysis_api_schema:BulkDensityMethod |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BulkDensityMethod
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
is_a: Method

```
</details>

### Induced

<details>
```yaml
name: BulkDensityMethod
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
is_a: Method
attributes:
  analytic:
    name: analytic
    todos:
    - what does this mean
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: analytic
    owner: BulkDensityMethod
    domain_of:
    - Method
    range: string
    required: true

```
</details>