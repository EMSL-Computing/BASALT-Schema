# BASALT

**Broad Analytical Schema for Samples and Laboratory Techniques**

[![Schema version](https://img.shields.io/badge/schema-v0.1.0-blue.svg)](src/basalt_schema/schema/basalt_schema.yaml)
[![LinkML](https://img.shields.io/badge/LinkML-schema-blueviolet.svg)](https://linkml.io)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org)
[![License: CC0-1.0](https://img.shields.io/badge/license-CC0%201.0-lightgrey.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-informational.svg)](https://EMSL-Computing.github.io/basalt-schema)

LinkML schema for MONet/EMSL scientific data across **biogeochemical**, **biological**, and **environmental** domains. Canonical source of truth for samples, provenance, laboratory activities, and analytical products used by the Analysis API and database models.

Formerly `analysis-api-schema`.

| | |
| --- | --- |
| **Schema version** | `0.1.0` (see `version` in [`basalt_schema.yaml`](src/basalt_schema/schema/basalt_schema.yaml)) |
| **Package** | `basalt_schema` (Python package version follows git tags via uv-dynamic-versioning) |
| **Docs** | https://EMSL-Computing.github.io/basalt-schema |
| **Repository** | https://github.com/EMSL-Computing/basalt-schema |
| **Canonical URI** | https://EMSL-Computing.github.io/basalt-schema |

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [basalt_schema](src/basalt_schema)
    * [schema](src/basalt_schema/schema) -- LinkML schema
    * [datamodel](src/basalt_schema/datamodel) -- generated
* [tests/](tests/) - Python tests
* [util/](util/) - Adhoc LinkML replacement code

## Versioning

BASALT uses **semantic versioning** (`MAJOR.MINOR.PATCH`) for the schema:

| Change type | Bump | Examples |
| --- | --- | --- |
| **MAJOR** | Breaking model changes | Rename/remove classes or required slots; change identifiers; incompatible range changes |
| **MINOR** | Backward-compatible additions | New optional classes/slots/enums; new modules; expanded permissible values |
| **PATCH** | Non-breaking fixes | Description/docs fixes; typo corrections; generator/tooling-only fixes that do not change the model |

### How versions are recorded

1. **Schema version (authoritative for the data model)**  
   Set in the root schema file:
   ```yaml
   # src/basalt_schema/schema/basalt_schema.yaml
   version: 0.1.0
   ```

2. **Python package version**  
   Derived from **git tags** (`v0.1.0`, `v0.2.0`, …) via [uv-dynamic-versioning](https://github.com/ninoseki/uv-dynamic-versioning).  
   Installable package name: `basalt_schema`.

3. **Release checklist**
   - [ ] Bump `version` in `src/basalt_schema/schema/basalt_schema.yaml`
   - [ ] Update the schema version badge / table in this README
   - [ ] Regenerate project artifacts if needed (`just gen-project`)
   - [ ] Merge to `main`
   - [ ] Tag the release: `git tag -a v0.1.0 -m "basalt-schema 0.1.0"` and push tags
   - [ ] Consumers pin or track the tag / package version

Consumers (API, DB migrations, ingestion) should record which schema version they were built against.

## Developer Documentation

```bash
uv sync
just gen-project
```

Windows and PowerShell users can use the same commands when `uv` and `just` are installed.

## Credits

This material is free to use, and attribution is always appreciated. Attribution may read as follows:

Authored by Conrad Mearns, Maia Kapur, Montana Smith, Beata Meluch, Aramy Truong, and Yuri E. Corilo at the Pacific Northwest National Laboratory, operated by Battelle for the U.S. Department of Energy.

(Optional, if applicable): Please cite the following in your work: (Place Holder Zenodo)
