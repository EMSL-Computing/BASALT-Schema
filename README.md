# BASALT

Broad Analytical Schema for Samples and Laboratory Techniques

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [basalt_schema](src/basalt_schema)
    * [schema](src/basalt_schema/schema) -- LinkML schema
    * [datamodel](src/basalt_schema/datamodel) -- generated
* [tests/](tests/) - Python tests
* [util/](util/) - Adhoc LinkML replacement code

## Developer Documentation

Windows and Powershell users:

```bash
uv sync

just gen-project
```

## Credits

This material is free to use, and attribution is always appreciated.  Attribution may read as follows:
Authored by Yuri E.Corilo, Conrad Mearns, Maia Kapur, Montana Smith, Beata Meluch  (Staff) at the Pacific Northwest National Laboratory, operated by Battelle for the U.S. Department of Energy.
(Optional, if applicable):  Please cite the following in your work: (Place Holder Zenodo)