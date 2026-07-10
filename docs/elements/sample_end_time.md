

# Slot: sample end time (sample_end_time) 


_Time of when the sample collection ends. Required format: HH:MM:SS in 24-hour time format. Don't forget the seconds! (Unit: hh:mm:ss or HH:MM:SS)_





URI: [analysis_api_schema:sample_end_time](https://w3id.org/MONet/analysis-api-schema/sample_end_time)
Alias: sample_end_time

<!-- no inheritance hierarchy -->








## Properties

* Range: [String](String.md)

* Regex pattern: `^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:sample_end_time |
| native | analysis_api_schema:sample_end_time |




## LinkML Source

<details>
```yaml
name: sample_end_time
description: 'Time of when the sample collection ends. Required format: HH:MM:SS in
  24-hour time format. Don''t forget the seconds! (Unit: hh:mm:ss or HH:MM:SS)'
title: sample end time
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: sample_end_time
range: string
pattern: ^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$

```
</details>