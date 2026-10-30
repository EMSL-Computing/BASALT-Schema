# Units and Quantities

BASALT records measurement units in two ways. Which one a slot uses depends on
who controls the unit.

## Fixed units: `double` + `unit.ucum_code` (default)

Lab-produced data products (MONet biogeochemistry, XCT, HYPROP, FTICR, ICP-MS)
report each column in a single unit fixed by the analytical protocol. These
slots store a plain number and declare the unit once, on the slot definition,
using the LinkML [`unit`](https://w3id.org/linkml/unit) metaslot:

```yaml
bulk_density:
  description: Bulk density of the soil core, in g/cm3.
  range: double
  unit:
    ucum_code: g/cm3
```

Rules:

- `unit.ucum_code` is a [UCUM](https://ucum.org/ucum) code.
- When a value is reported "as" an element other than the measured species,
  name it in a UCUM annotation: `mg{N}/kg` for nitrate-N, `mg{C}/kg` for
  organic carbon, `ug{CO2-C}/g` for respiration, `ug{pNP}/g/h` for enzyme
  activity. Plain element concentrations use `mg/kg` (mg Fe per kg soil).
- Exchangeable cations and CEC use `meq/(100.g)`.
- Dimensionless values use `1` (ratios, fractions), `%` (percent), or
  `[pH]`.
- The description also states the unit in plain text, so it is visible in
  generated docs and CSV templates.
- If a slot name already contains a unit (`gwc_percent`,
  `Al_ug_per_g`), the name, `unit.ucum_code`, and description must agree.
  Slot names are not changed to remove units, to avoid breaking ingest and
  database columns.
- Units are schema metadata. Adding or correcting them does not change
  generated SQL and needs no database migration.

Partners whose data arrive with other units (e.g. NMDC-style
`QuantityValue` objects) are converted to the declared unit at ingest.

## Provider-specified units: `QuantityValue`

Use `range: QuantityValue` only when the unit can legitimately differ from
record to record, typically values supplied by external providers or users
(e.g. size thresholds provided by ARM, container sizes, device settings).
Each value then carries its own unit:

```yaml
has_numeric_value: 2.0
has_unit: mm
has_raw_value: 2 mm
```

Rules:

- `has_unit` is a UCUM code.
- The slot description names the expected or default unit, e.g. "Size
  threshold, typically in um. Providers may give another unit in the
  QuantityValue."
- In the relational database each `QuantityValue` slot is a foreign key into
  a shared `QuantityValue` table, so it is not used for wide tabular products.

Moving a slot between `double` and `QuantityValue` changes database columns
and needs a migration.
