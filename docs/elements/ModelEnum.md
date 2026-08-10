# Enum: ModelEnum 



URI: [basalt_schema:ModelEnum](https://w3id.org/MONet/basalt-schema/ModelEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| exploris_21T | None |  |
| exploris_240 | None |  |
| exploris_480 | None |  |
| ltq_orbitrap_velos | None |  |
| orbitrap_fusion_lumos | None |  |
| orbitrap_eclipse_tribid | None |  |
| orbitrap_q_exactive | None |  |
| orbitrap_iqx_tribrid | None |  |
| orbitrap_exploris_120 | None |  |
| solarix_7T | None |  |
| solarix_12T | None |  |
| solarix_15T | None |  |
| agilent_8890A | None |  |
| agilent_7980A | None |  |
| vortex_genie_2 | None |  |
| novaseq | None |  |
| novaseq_6000 | OBI:0002630 |  |
| novaseq_x | None |  |
| hiseq | None |  |
| hiseq_1000 | OBI:0002022 |  |
| hiseq_1500 | OBI:0003386 |  |
| hiseq_2000 | OBI:0002001 |  |
| hiseq_2500 | OBI:0002002 |  |
| hiseq_3000 | OBI:0002048 |  |
| hiseq_4000 | OBI:0002049 |  |
| hiseq_x_ten | OBI:0002129 |  |
| miniseq | OBI:0003114 |  |
| miseq | OBI:0002003 |  |
| nextseq_1000 | OBI:0003606 |  |
| nextseq | None |  |
| nextseq_500 | OBI:0002021 |  |
| nextseq_550 | OBI:0003387 |  |
| gridion | OBI:0002751 |  |
| minion | OBI:0002750 |  |
| promethion | OBI:0002752 |  |
| rs_II | OBI:0002012 |  |
| sequel | OBI:0002632 |  |
| sequel_II | OBI:0002633 |  |
| revio | None |  |
| scimax | None |  |
| ed_400_with_rs_422 | None |  |
| mettler_toledo_30029066 | None |  |
| mettler_toledo_30266628 | None |  |
| ums_hyprop2_020210 | None |  |
| fialyzer_1000 | None |  |
| fialyzer_1001 | None |  |
| fialyzer_1002 | None |  |
| orbitrap_q_exactive_plus | None |  |
| toc_5000A | None |  |
| toc_lcsh | None |  |
| sr_1 | None |  |
| xth320 | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [model](model.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema






## LinkML Source

<details>
```yaml
name: ModelEnum
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
permissible_values:
  exploris_21T:
    text: exploris_21T
    aliases:
    - Exploris 21T
  exploris_240:
    text: exploris_240
    aliases:
    - Orbitrap Exploris 240
  exploris_480:
    text: exploris_480
    aliases:
    - Orbitrap Exploris 480
  ltq_orbitrap_velos:
    text: ltq_orbitrap_velos
    aliases:
    - LTQ Orbitrap Velos
    - LTQ Orbitrap Velos ETD
    - Velos
  orbitrap_fusion_lumos:
    text: orbitrap_fusion_lumos
    aliases:
    - Orbitrap Fusion Lumos
    - Fusion
  orbitrap_eclipse_tribid:
    text: orbitrap_eclipse_tribid
    aliases:
    - Orbitrap Eclipse Tribid
    - Eclipse
  orbitrap_q_exactive:
    text: orbitrap_q_exactive
    aliases:
    - Orbitrap Q-Exactive HF
    - Orbitrap Q-Exactive HF-X
  orbitrap_iqx_tribrid:
    text: orbitrap_iqx_tribrid
    aliases:
    - Orbitrap IQ-X Tribrid
    - Thermo Orbitrap IQ-X Tribrid
  orbitrap_exploris_120:
    text: orbitrap_exploris_120
    aliases:
    - Orbitrap Exploris 120
    - Thermo Orbitrap Exploris 120
  solarix_7T:
    text: solarix_7T
    aliases:
    - 7T Solarix
    - 7T FT-ICR MS
    - 7T MRMS
  solarix_12T:
    text: solarix_12T
    aliases:
    - 12T Solarix
    - 12T FT-ICR MS
    - 12T MRMS
  solarix_15T:
    text: solarix_15T
    aliases:
    - 15T Solarix
    - 15T FT-ICR MS
    - 15T MRMS
  agilent_8890A:
    text: agilent_8890A
    aliases:
    - 8890A GC-MS
    - Agilent GC MS
  agilent_7980A:
    text: agilent_7980A
    aliases:
    - 7980A GC-MS
    - Agilent GC MS
  vortex_genie_2:
    text: vortex_genie_2
    aliases:
    - VortexGenie2
  novaseq:
    text: novaseq
    aliases:
    - NovaSeq
    - Illumina NovaSeq
  novaseq_6000:
    text: novaseq_6000
    meaning: OBI:0002630
    comments:
    - Possible flowcell versions are SP, S1, S2, S4.
    see_also:
    - https://www.illumina.com/systems/sequencing-platforms/novaseq/specifications.html
    aliases:
    - NovaSeq 6000
    - Illumina NovaSeq 6000
    structured_aliases:
      Illumina NovaSeq S2:
        literal_form: Illumina NovaSeq S2
        predicate: NARROW_SYNONYM
        contexts:
        - https://gold.jgi.doe.gov/
      Illumina NovaSeq S4:
        literal_form: Illumina NovaSeq S4
        predicate: NARROW_SYNONYM
        contexts:
        - https://gold.jgi.doe.gov/
      Illumina NovaSeq SP:
        literal_form: Illumina NovaSeq SP
        predicate: NARROW_SYNONYM
        contexts:
        - https://gold.jgi.doe.gov/
  novaseq_x:
    text: novaseq_x
    comments:
    - Possible flowcell versions are 1.5B, 10B, 25B. Only difference between X and
      X Plus is 2 flowcells for X Plus versus 1 flowcell for X.
    see_also:
    - https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus/specifications.html
    aliases:
    - Illumina NovaSeq X
    - Illumina NovaSeq X Plus
    exact_mappings:
    - OBI:0003663
    narrow_mappings:
    - OBI:0003664
  hiseq:
    text: hiseq
    aliases:
    - Illumina HiSeq
  hiseq_1000:
    text: hiseq_1000
    meaning: OBI:0002022
    aliases:
    - Illumina HiSeq 1000
  hiseq_1500:
    text: hiseq_1500
    meaning: OBI:0003386
    aliases:
    - Illumina HiSeq 1500
  hiseq_2000:
    text: hiseq_2000
    meaning: OBI:0002001
    aliases:
    - Illumina HiSeq 2000
  hiseq_2500:
    text: hiseq_2500
    meaning: OBI:0002002
    aliases:
    - Illumina HiSeq 2500
    structured_aliases:
      Illumina HiSeq 2500-1TB:
        literal_form: Illumina HiSeq 2500-1TB
        predicate: NARROW_SYNONYM
        contexts:
        - https://gold.jgi.doe.gov/
      Illumina HiSeq 2500-Rapid:
        literal_form: Illumina HiSeq 2500-Rapid
        predicate: NARROW_SYNONYM
        contexts:
        - https://gold.jgi.doe.gov/
  hiseq_3000:
    text: hiseq_3000
    meaning: OBI:0002048
    aliases:
    - Illumina HiSeq 3000
  hiseq_4000:
    text: hiseq_4000
    meaning: OBI:0002049
    aliases:
    - Illumina HiSeq 4000
  hiseq_x_ten:
    text: hiseq_x_ten
    meaning: OBI:0002129
    aliases:
    - Illumina HiSeq X Ten
  miniseq:
    text: miniseq
    meaning: OBI:0003114
    aliases:
    - Illumina MiniSeq
  miseq:
    text: miseq
    meaning: OBI:0002003
    aliases:
    - MiSeq
    - Illumina MiSeq
    structured_aliases:
      Illumina MiSeq:
        literal_form: Illumina MiSeq
        predicate: EXACT_SYNONYM
        contexts:
        - https://gold.jgi.doe.gov/
  nextseq_1000:
    text: nextseq_1000
    meaning: OBI:0003606
    aliases:
    - Illumina NextSeq 1000
  nextseq:
    text: nextseq
    aliases:
    - NextSeq
    - Illumina NextSeq
    structured_aliases:
      Illumina NextSeq-HO:
        literal_form: Illumina NextSeq-HO
        predicate: NARROW_SYNONYM
        contexts:
        - https://gold.jgi.doe.gov/
      Illumina NextSeq-MO:
        literal_form: Illumina NextSeq-MO
        predicate: NARROW_SYNONYM
        contexts:
        - https://gold.jgi.doe.gov/
  nextseq_500:
    text: nextseq_500
    meaning: OBI:0002021
    aliases:
    - NextSeq 500
    - Illumina NextSeq 500
  nextseq_550:
    text: nextseq_550
    meaning: OBI:0003387
    aliases:
    - NextSeq 550
    - Illumina NextSeq 550
  gridion:
    text: gridion
    meaning: OBI:0002751
    aliases:
    - Oxford Nanopore GridION Mk1
  minion:
    text: minion
    meaning: OBI:0002750
    aliases:
    - Oxford Nanopore MinION
  promethion:
    text: promethion
    meaning: OBI:0002752
    aliases:
    - Oxford Nanopore PromethION
  rs_II:
    text: rs_II
    meaning: OBI:0002012
    aliases:
    - PacBio RS II
  sequel:
    text: sequel
    meaning: OBI:0002632
    aliases:
    - PacBio Sequel
  sequel_II:
    text: sequel_II
    meaning: OBI:0002633
    aliases:
    - PacBio Sequel II
  revio:
    text: revio
    aliases:
    - PacBio Revio
    - Revio
  scimax:
    text: scimax
  ed_400_with_rs_422:
    text: ed_400_with_rs_422
  mettler_toledo_30029066:
    text: mettler_toledo_30029066
  mettler_toledo_30266628:
    text: mettler_toledo_30266628
  ums_hyprop2_020210:
    text: ums_hyprop2_020210
  fialyzer_1000:
    text: fialyzer_1000
  fialyzer_1001:
    text: fialyzer_1001
  fialyzer_1002:
    text: fialyzer_1002
  orbitrap_q_exactive_plus:
    text: orbitrap_q_exactive_plus
  toc_5000A:
    text: toc_5000A
  toc_lcsh:
    text: toc_lcsh
  sr_1:
    text: sr_1
  xth320:
    text: xth320

```
</details>