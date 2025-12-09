# analysis-api-schema

LinkML for the EMSL Science Cental MONet Analysis API schemas

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [analysis_api_schema](src/analysis_api_schema)
    * [schema](src/analysis_api_schema/schema) -- LinkML schema
    * [datamodel](src/analysis_api_schema/datamodel) -- generated
* [tests/](tests/) - Python tests
* [util/](util/) - Adhoc LinkML replacement code

## Developer Documentation

```bash
just --list
just gen-project
```

## Credits

This project was made with `LinkML`