

# Slot: sample start time (sample_start_time) 


_Time of when the sample collection starts. Required format: HH:MM:SS in 24-hour time format. Don't forget the seconds! (Unit: hh:mm:ss or HH:MM:SS)_





URI: [basalt_schema:sample_start_time](https://EMSL-Computing.github.io/BASALT-Schema/sample_start_time)
Alias: sample_start_time

<!-- no inheritance hierarchy -->







## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])\s*(hh:mm:ss|HH:MM:SS)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:sample_start_time |
| native | basalt_schema:sample_start_time |




## LinkML Source

<details>
```yaml
name: sample_start_time
description: 'Time of when the sample collection starts. Required format: HH:MM:SS
  in 24-hour time format. Don''t forget the seconds! (Unit: hh:mm:ss or HH:MM:SS)'
title: sample start time
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: sample_start_time
range: string
pattern: ^(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])\s*(hh:mm:ss|HH:MM:SS)$

```
</details>