

# Class: RespirationMethod 



URI: [basalt_schema:RespirationMethod](https://emsl-computing.github.io/BASALT-Schema/elements/RespirationMethod)





```mermaid
 classDiagram
    class RespirationMethod
    click RespirationMethod href "../RespirationMethod/"
      Method <|-- RespirationMethod
        click Method href "../Method/"
      
      RespirationMethod : analytic
        
      
```





## Inheritance
* [Method](Method.md)
    * **RespirationMethod**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [analytic](analytic.md) | 1 <br/> [String](String.md) |  | [Method](Method.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [RespirationDataGenerationActivity](RespirationDataGenerationActivity.md) | [method_id](method_id.md) | range | [RespirationMethod](RespirationMethod.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:RespirationMethod |
| native | basalt_schema:RespirationMethod |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RespirationMethod
from_schema: https://emsl-computing.github.io/BASALT-Schema
is_a: Method

```
</details>

### Induced

<details>
```yaml
name: RespirationMethod
from_schema: https://emsl-computing.github.io/BASALT-Schema
is_a: Method
attributes:
  analytic:
    name: analytic
    todos:
    - what does this mean
    from_schema: https://emsl-computing.github.io/BASALT-Schema
    rank: 1000
    alias: analytic
    owner: RespirationMethod
    domain_of:
    - Method
    range: string
    required: true

```
</details>