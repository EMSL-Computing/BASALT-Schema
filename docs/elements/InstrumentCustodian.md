

# Class: InstrumentCustodian 


_A link between an instrument and a custodian (person) responsible for it._

_This class captures the relationship between an instrument and the person_

_who is responsible for its maintenance, calibration, and proper use._





URI: [basalt_schema:InstrumentCustodian](https://EMSL-Computing.github.io/basalt-schema/InstrumentCustodian)





```mermaid
 classDiagram
    class InstrumentCustodian
    click InstrumentCustodian href "../InstrumentCustodian/"
      InstrumentCustodian : custodian_id
        
          
    
        
        
        InstrumentCustodian --> "1" Custodian : custodian_id
        click Custodian href "../Custodian/"
    

        
      InstrumentCustodian : instrument_id
        
          
    
        
        
        InstrumentCustodian --> "1" Instrument : instrument_id
        click Instrument href "../Instrument/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [instrument_id](instrument_id.md) | 1 <br/> [Instrument](Instrument.md) |  | direct |
| [custodian_id](custodian_id.md) | 1 <br/> [Custodian](Custodian.md) |  | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:InstrumentCustodian |
| native | basalt_schema:InstrumentCustodian |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InstrumentCustodian
description: 'A link between an instrument and a custodian (person) responsible for
  it.

  This class captures the relationship between an instrument and the person

  who is responsible for its maintenance, calibration, and proper use.'
from_schema: https://EMSL-Computing.github.io/basalt-schema
attributes:
  instrument_id:
    name: instrument_id
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    domain_of:
    - InstrumentAlternativeIdentifier
    - InstrumentCustodian
    range: Instrument
    required: true
  custodian_id:
    name: custodian_id
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    domain_of:
    - InstrumentCustodian
    range: Custodian
    required: true

```
</details>

### Induced

<details>
```yaml
name: InstrumentCustodian
description: 'A link between an instrument and a custodian (person) responsible for
  it.

  This class captures the relationship between an instrument and the person

  who is responsible for its maintenance, calibration, and proper use.'
from_schema: https://EMSL-Computing.github.io/basalt-schema
attributes:
  instrument_id:
    name: instrument_id
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    alias: instrument_id
    owner: InstrumentCustodian
    domain_of:
    - InstrumentAlternativeIdentifier
    - InstrumentCustodian
    range: Instrument
    required: true
  custodian_id:
    name: custodian_id
    from_schema: https://EMSL-Computing.github.io/basalt-schema
    rank: 1000
    alias: custodian_id
    owner: InstrumentCustodian
    domain_of:
    - InstrumentCustodian
    range: Custodian
    required: true

```
</details>