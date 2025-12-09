# analysis-api-schema

linkML transition for analysis-api schemae

## Website

[https://MONet.github.io/analysis-api-schema](https://MONet.github.io/analysis-api-schema)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [analysis_api_schema](src/analysis_api_schema)
    * [schema](src/analysis_api_schema/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/analysis_api_schema/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

Windows and Powershell users:

```bash
poetry install
.venv/Scripts/activate

just gen
just gen-pydantic
```

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
