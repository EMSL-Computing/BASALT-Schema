

# Class: BulkDensityMethod 



URI: [basalt_schema:BulkDensityMethod](https://w3id.org/MONet/basalt-schema/BulkDensityMethod)





```mermaid
 classDiagram
    class BulkDensityMethod
    click BulkDensityMethod href "../BulkDensityMethod/"
      Method <|-- BulkDensityMethod
        click Method href "../Method/"
      
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


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:BulkDensityMethod |
| native | basalt_schema:BulkDensityMethod |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BulkDensityMethod
from_schema: https://w3id.org/MONet/basalt-schema
is_a: Method

```
</details>

### Induced

<details>
```yaml
name: BulkDensityMethod
from_schema: https://w3id.org/MONet/basalt-schema
is_a: Method
attributes:
  analytic:
    name: analytic
    todos:
    - what does this mean
    from_schema: https://w3id.org/MONet/basalt-schema
    rank: 1000
    alias: analytic
    owner: BulkDensityMethod
    domain_of:
    - Method
    range: string
    required: true

```
</details>