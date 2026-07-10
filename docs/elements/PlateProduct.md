

# Class: PlateProduct 


_Abstract base for plate measurement data products._

_Common summary slots shared across AMP2 and Ecoplate products._

__

_v1 origin: plate-general.yaml PlateProduct_

_v2 change: follows existing satellite-table pattern (id: range: processedData)_

_           instead of v1's is_a: dataProduct._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [analysis_api_schema:PlateProduct](https://w3id.org/MONet/analysis-api-schema/PlateProduct)






```mermaid
 classDiagram
    class PlateProduct
    click PlateProduct href "../PlateProduct"
      PlateProduct <|-- AMP2ODProduct
        click AMP2ODProduct href "../AMP2ODProduct"
      PlateProduct <|-- EcoplateAbsorbanceProduct
        click EcoplateAbsorbanceProduct href "../EcoplateAbsorbanceProduct"
      
      PlateProduct : blank_mean
        
      PlateProduct : cv_percent
        
      PlateProduct : plate_average
        
      PlateProduct : timepoint_label
        
      PlateProduct : wavelength_nm
        
      PlateProduct : well_readings
        
          
    
    
    
    
    PlateProduct --> "*" WellReading : well_readings
    click WellReading href "../WellReading"
    

        
      
```





## Inheritance
* **PlateProduct**
    * [AMP2ODProduct](AMP2ODProduct.md)
    * [EcoplateAbsorbanceProduct](EcoplateAbsorbanceProduct.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [wavelength_nm](wavelength_nm.md) | 1 <br/> [Integer](Integer.md) | Measurement wavelength in nanometres (e | direct |
| [timepoint_label](timepoint_label.md) | 1 <br/> [String](String.md) | Human-readable timepoint label for repeated-measurement series | direct |
| [plate_average](plate_average.md) | 0..1 <br/> [Float](Float.md) | Mean measurement across all sample wells (excludes blanks) | direct |
| [blank_mean](blank_mean.md) | 0..1 <br/> [Float](Float.md) | Mean measurement of uninoculated control wells | direct |
| [cv_percent](cv_percent.md) | 0..1 <br/> [Float](Float.md) | Coefficient of variation across technical replicates | direct |
| [well_readings](well_readings.md) | * <br/> [WellReading](WellReading.md) | Structured per-well measurement data array | direct |









## TODOs

* add plate_range (12 well, 96 well, etc.)?

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:PlateProduct |
| native | analysis_api_schema:PlateProduct |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PlateProduct
description: "Abstract base for plate measurement data products.\nCommon summary slots\
  \ shared across AMP2 and Ecoplate products.\n\nv1 origin: plate-general.yaml PlateProduct\n\
  v2 change: follows existing satellite-table pattern (id: range: processedData)\n\
  \           instead of v1's is_a: dataProduct."
todos:
- add plate_range (12 well, 96 well, etc.)?
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
abstract: true
slots:
- wavelength_nm
- timepoint_label
- plate_average
- blank_mean
- cv_percent
- well_readings

```
</details>

### Induced

<details>
```yaml
name: PlateProduct
description: "Abstract base for plate measurement data products.\nCommon summary slots\
  \ shared across AMP2 and Ecoplate products.\n\nv1 origin: plate-general.yaml PlateProduct\n\
  v2 change: follows existing satellite-table pattern (id: range: processedData)\n\
  \           instead of v1's is_a: dataProduct."
todos:
- add plate_range (12 well, 96 well, etc.)?
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
abstract: true
attributes:
  wavelength_nm:
    name: wavelength_nm
    description: Measurement wavelength in nanometres (e.g. 590 Ecoplate, 610 AMP2
      OD)
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: wavelength_nm
    owner: PlateProduct
    domain_of:
    - AMP2DataGenerationActivity
    - EcoplateDataGenerationActivity
    - PlateProduct
    range: integer
    required: true
  timepoint_label:
    name: timepoint_label
    description: 'Human-readable timepoint label for repeated-measurement series.

      Examples: "t=0", "t=24h", "t=48h".

      Lives on concrete analysis/product subclasses, NOT on base DataGenerationActivity'
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: timepoint_label
    owner: PlateProduct
    domain_of:
    - PlateDataGenerationActivity
    - PlateProduct
    range: string
    required: true
  plate_average:
    name: plate_average
    description: Mean measurement across all sample wells (excludes blanks)
    todos:
    - units
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: plate_average
    owner: PlateProduct
    domain_of:
    - PlateProduct
    range: float
  blank_mean:
    name: blank_mean
    description: Mean measurement of uninoculated control wells
    todos:
    - units
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: blank_mean
    owner: PlateProduct
    domain_of:
    - PlateProduct
    range: float
  cv_percent:
    name: cv_percent
    description: Coefficient of variation across technical replicates
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: cv_percent
    owner: PlateProduct
    domain_of:
    - PlateProduct
    range: float
  well_readings:
    name: well_readings
    description: 'Structured per-well measurement data array.

      Lightweight summary for SQL queries without full file download.

      Raw data still accessible via processedData.s3_key in MinIO.

      typed via LinkML inlined class.'
    todos:
    - decide how to represent in backend (normalized child table with FK to PlateSetupActivity,
      array column, or other)
    from_schema: https://w3id.org/MONet/analysis-api-schema
    rank: 1000
    alias: well_readings
    owner: PlateProduct
    domain_of:
    - PlateProduct
    range: WellReading
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>