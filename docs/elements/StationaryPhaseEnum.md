# Enum: StationaryPhaseEnum 




_The stationary phase used in chromatography._



URI: [basalt_schema:StationaryPhaseEnum](https://emsl-computing.github.io/BASALT-Schema/elements/StationaryPhaseEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| BEH-HILIC | None | Hydrophilic Interaction Chromatography (HILIC) employing BEH (Bridged Ethylen... | Is-A: NONE<br>|
| C18 | None | A stationary phase consisting of octadecyl chains (C18) bonded to silica part... ||
| C8 | None | A stationary phase consisting of octyl chains (C8) bonded to silica particles ||
| C4 | None | A stationary phase consisting of butyl chains (C4) bonded to silica particles ||
| C2 | None | A stationary phase consisting of ethyl chains (C2) bonded to silica particles ||
| C1 | None | A stationary phase consisting of methyl chains (C1) bonded to silica particle... ||
| C30 | None | A stationary phase consisting of triacontyl chains (C30) bonded to silica par... ||
| C60 | None | A stationary phase consisting of hexatriacontyl chains (C60) bonded to silica... ||
| CNT | None | Carbon Nanotube stationary phase ||
| CN | None | Cyano (CN) bonded stationary phase ||
| Diol | None | A stationary phase with diol (1,2-diol) functional groups ||
| HILIC | None | Hydrophilic Interaction Chromatography (HILIC) stationary phase ||
| HLB | None | Hydrophilic-Lipophilic-Balance (HLB) stationary phase ||
| NH2 | None | Amino (NH2) bonded stationary phase ||
| Phenyl | None | Phenyl bonded stationary phase ||
| Polysiloxane | None | A stationary phase made of polysiloxane, usually used in gas chromatography ||
| PS-DVB | None | Polystyrene-divinylbenzene stationary phase, often used in solid-phase extrac... ||
| SAX | None | Strong Anion Exchange (SAX) stationary phase ||
| SCX | None | Strong Cation Exchange (SCX) stationary phase ||
| Silica | None | A stationary phase made of silica, commonly used in chromatography ||
| WCX | None | Weak Cation Exchange (WCX) stationary phase ||
| WAX | None | Weak Anion Exchange (WAX) stationary phase ||
| ZIC-HILIC | None | Zwitterionic Hydrophilic Interaction Chromatography (ZIC-HILIC) stationary ph... | Is-A: NONE<br>|
| ZIC-pHILIC | None | Zwitterionic pH-Responsive Hydrophilic Interaction Chromatography (ZIC-pHILIC... | Is-A: NONE<br>|
| ZIC-cHILIC | None | Zwitterionic Charged Hydrophilic Interaction Chromatography (ZIC-cHILIC) stat... | Is-A: NONE<br>|













## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema






## LinkML Source

<details>
```yaml
name: StationaryPhaseEnum
description: The stationary phase used in chromatography.
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
permissible_values:
  BEH-HILIC:
    text: BEH-HILIC
    description: Hydrophilic Interaction Chromatography (HILIC) employing BEH (Bridged
      Ethylene Hybrid) particles as the stationary phase.
    is_a: HILIC
  C18:
    text: C18
    description: A stationary phase consisting of octadecyl chains (C18) bonded to
      silica particles.
  C8:
    text: C8
    description: A stationary phase consisting of octyl chains (C8) bonded to silica
      particles.
  C4:
    text: C4
    description: A stationary phase consisting of butyl chains (C4) bonded to silica
      particles.
  C2:
    text: C2
    description: A stationary phase consisting of ethyl chains (C2) bonded to silica
      particles.
  C1:
    text: C1
    description: A stationary phase consisting of methyl chains (C1) bonded to silica
      particles.
  C30:
    text: C30
    description: A stationary phase consisting of triacontyl chains (C30) bonded to
      silica particles.
  C60:
    text: C60
    description: A stationary phase consisting of hexatriacontyl chains (C60) bonded
      to silica particles.
  CNT:
    text: CNT
    description: Carbon Nanotube stationary phase.
  CN:
    text: CN
    description: Cyano (CN) bonded stationary phase.
  Diol:
    text: Diol
    description: A stationary phase with diol (1,2-diol) functional groups.
  HILIC:
    text: HILIC
    description: Hydrophilic Interaction Chromatography (HILIC) stationary phase.
  HLB:
    text: HLB
    description: Hydrophilic-Lipophilic-Balance (HLB) stationary phase.
  NH2:
    text: NH2
    description: Amino (NH2) bonded stationary phase.
  Phenyl:
    text: Phenyl
    description: Phenyl bonded stationary phase.
  Polysiloxane:
    text: Polysiloxane
    description: A stationary phase made of polysiloxane, usually used in gas chromatography.
  PS-DVB:
    text: PS-DVB
    description: Polystyrene-divinylbenzene stationary phase, often used in solid-phase
      extraction, including proprietary Priority PolLutant (PPL).
  SAX:
    text: SAX
    description: Strong Anion Exchange (SAX) stationary phase.
  SCX:
    text: SCX
    description: Strong Cation Exchange (SCX) stationary phase.
  Silica:
    text: Silica
    description: A stationary phase made of silica, commonly used in chromatography.
  WCX:
    text: WCX
    description: Weak Cation Exchange (WCX) stationary phase.
  WAX:
    text: WAX
    description: Weak Anion Exchange (WAX) stationary phase.
  ZIC-HILIC:
    text: ZIC-HILIC
    description: Zwitterionic Hydrophilic Interaction Chromatography (ZIC-HILIC) stationary
      phase.
    is_a: HILIC
  ZIC-pHILIC:
    text: ZIC-pHILIC
    description: Zwitterionic pH-Responsive Hydrophilic Interaction Chromatography
      (ZIC-pHILIC) stationary phase.
    is_a: ZIC-HILIC
  ZIC-cHILIC:
    text: ZIC-cHILIC
    description: Zwitterionic Charged Hydrophilic Interaction Chromatography (ZIC-cHILIC)
      stationary phase.
    is_a: ZIC-HILIC

```
</details>