

# Slot: sample end time (sample_end_time) 


_Time of when the sample collection ends. Required format: HH:MM:SS in 24-hour time format. Don't forget the seconds! (Unit: hh:mm:ss or HH:MM:SS)_





URI: [basalt_schema:sample_end_time](https://EMSL-Computing.github.io/basalt-schema/sample_end_time)
Alias: sample_end_time

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
| Regex Pattern | `^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:sample_end_time |
| native | basalt_schema:sample_end_time |




## LinkML Source

<details>
```yaml
name: sample_end_time
description: 'Time of when the sample collection ends. Required format: HH:MM:SS in
  24-hour time format. Don''t forget the seconds! (Unit: hh:mm:ss or HH:MM:SS)'
title: sample end time
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: sample_end_time
range: string
pattern: ^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$

```
</details>