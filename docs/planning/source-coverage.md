# Source-to-requirement coverage

All **23 slides** are accounted for: **90 visible target diagram panels**, plus explicitly identified context. There are **23 PDF checklist/figure items**. Panel IDs are based on visual position, not the number of embedded images.

## Panel notation and previews

`TL/TR/BL/BR` mean top-left/top-right/bottom-left/bottom-right. On slides 5-8, `L1-L3` run down the left column; `C1-C2` and `R1-R2` run down the center/right columns. Slide 11 has four panels in each row (`T1-T4`, `B1-B4`). Other location names are literal. Slot names use the package convention: 1 upper-left, 2 lower-left, 3 upper-right, 4 lower-right.

[Slides 1-8](previews/deck-contact-1.png) | [Slides 9-16](previews/deck-contact-2.png) | [Slides 17-23](previews/deck-contact-3.png)

The originals in `sources/` are authoritative for species and arrow details; previews support navigation. “Repeated graph” means the same structural target, not byte-identical artwork or equal physical amplitudes.

## PDF checklist

| Item | Page | Request / figure | Requirement |
| --- | --- | --- | --- |
| P1-01 | 1 | Square box defaults | [R01](requirements.md) |
| P1-02 | 1 | Complementary internal crossing | [R02](requirements.md) |
| P1-03 | 1 | First crossed-box image: upper external pair | [R03](requirements.md) |
| P1-04 | 1 | Second crossed-box image: right external pair | [R04](requirements.md) |
| P1-05 | 1 | Four-legged bubble request | [R05](requirements.md) |
| P1-06 | 1 | Independent label positions and outside defaults | [R06](requirements.md) |
| P1-07 | 1 | Independent momentum sizing on unequal edges | [R06](requirements.md) |
| P2-01 | 2 | Pink triangle-contact image and label placement | [R06](requirements.md) |
| P2-02 | 2 | All four triangle-contact orientations | [R07](requirements.md) |
| P2-03 | 2 | Regular triangle correction, four tree placements | [R08](requirements.md) |
| P2-04 | 2 | t-tree self-energy on all external legs | [R09](requirements.md) |
| P2-05 | 2 | t-tree seagull on all external legs | [R11](requirements.md) |
| P2-06 | 2 | Swordfish, all legs in t and s; one insertion at a time | [R12](requirements.md) |
| P3-01 | 3 | Swordfish shared-vertex geometry, t example | [R12](requirements.md) |
| P3-02 | 3 | s-tree self-energy on all external legs | [R10](requirements.md) |
| P3-03 | 3 | s-tree seagull on all external legs | [R11](requirements.md) |
| P3-04 | 3 | s-tree swordfish example | [R12](requirements.md) |
| P3-05 | 3 | Diagonal Z connection q1-q4 / q3-q2 | [R14](requirements.md) |
| P3-06 | 3 | Prefer square-shaped vertex-correction layout | [R14](requirements.md) |
| P4-01 | 4 | Contact external self-energy example | [R13](requirements.md) |
| P4-02 | 4 | Vertex-correction labeling heading | [R06](requirements.md) |
| P4-03 | 4 | Proca arrows reach vertices in every topology | [R15](requirements.md) |
| P4-04 | 4 | Reference, landing page, and visuals refresh | [R16](requirements.md) |

## Slide 01

Cover, title, author names; no diagram requirement.


## Slide 02

| Panel | Visible diagram / placement | Requirement | Relation |
| --- | --- | --- | --- |
| S02-left | Triangle-contact, quartic vertex at top | R07 | Target |
| S02-center | Box with crossed upper external pair | R03 | Target |
| S02-right | Ordinary box, side Z / horizontal W styling | R01 | Target |

## Slide 03

| Panel | Visible diagram / placement | Requirement | Relation |
| --- | --- | --- | --- |
| S03-left | Ordinary box, side W / horizontal Z styling | R01 | Styling variant of S02-right |
| S03-center | Box with crossed right external pair | R04 | Target |
| S03-right | Triangle-contact, quartic vertex at right | R07 | Target |

## Slide 04

| Panel | Visible diagram / placement | Requirement | Relation |
| --- | --- | --- | --- |
| S04-TL | Triangle-contact, quartic vertex at bottom | R07 | Target |
| S04-TR | Four-legged s-channel bubble | R05 | Target |
| S04-BL | Triangle-contact, quartic vertex at left | R07 | Target |
| S04-BR | Four-legged t-channel bubble | R05 | Target |

## Slide 05

| Panel | Visible diagram / placement | Requirement | Relation |
| --- | --- | --- | --- |
| S05-L1 | Lower-left t-tree swordfish | R12 | Target |
| S05-L2 | Bottom t-tree regular triangle | R08 | Target |
| S05-L3 | Lower-right t-tree swordfish | R12 | Target |
| S05-C1 | Lower-right t-tree seagull | R11 | Target |
| S05-C2 | Lower-right t-tree self-energy | R09 | Target |
| S05-R1 | Lower-left t-tree seagull | R11 | Target |
| S05-R2 | Lower-left t-tree self-energy | R09 | Target |

## Slide 06

| Panel | Visible diagram / placement | Requirement | Relation |
| --- | --- | --- | --- |
| S06-L1 | Left s-tree shared inner-vertex bubble | R19 | Target |
| S06-L2 | Left s-tree regular triangle | R08 | Target |
| S06-L3 | Left s-tree shared inner-vertex bubble, alternate species | R19 | Styling variant of S06-L1 |
| S06-C1 | Upper-left s-tree seagull | R11 | Target |
| S06-C2 | Lower-left s-tree seagull | R11 | Target |
| S06-R1 | Upper-left s-tree self-energy | R10 | Target |
| S06-R2 | Lower-left s-tree self-energy | R10 | Target |

## Slide 07

| Panel | Visible diagram / placement | Requirement | Relation |
| --- | --- | --- | --- |
| S07-L1 | Right s-tree shared inner-vertex bubble | R19 | Target |
| S07-L2 | Right s-tree regular triangle | R08 | Target |
| S07-L3 | Right s-tree shared inner-vertex bubble, alternate species | R19 | Styling variant of S07-L1 |
| S07-C1 | Lower-right s-tree seagull | R11 | Target |
| S07-C2 | Upper-right s-tree seagull | R11 | Target |
| S07-R1 | Lower-right s-tree self-energy | R10 | Target |
| S07-R2 | Upper-right s-tree self-energy | R10 | Target |

## Slide 08

| Panel | Visible diagram / placement | Requirement | Relation |
| --- | --- | --- | --- |
| S08-L1 | Upper-left t-tree swordfish | R12 | Target |
| S08-L2 | Top t-tree regular triangle | R08 | Target |
| S08-L3 | Upper-right t-tree swordfish | R12 | Target |
| S08-C1 | Upper-right t-tree seagull | R11 | Target |
| S08-C2 | Upper-right t-tree self-energy | R09 | Target |
| S08-R1 | Upper-left t-tree seagull | R11 | Target |
| S08-R2 | Upper-left t-tree self-energy; current prototype subset | R09 | Target |

Context: the screenshot and commentary are recorded separately below.

## Slide 09

Photographed handwritten swordfish/momentum notes: context for R12 and its annotation review. No independent additional supported topology is inferred.


## Slide 10

| Panel | Visible diagram / placement | Requirement | Relation |
| --- | --- | --- | --- |
| S10-TL | Contact self-energy on upper-left leg | R13 | Target |
| S10-TR | Contact self-energy on upper-right leg | R13 | Target |
| S10-BL | Contact self-energy on lower-left leg | R13 | Target |
| S10-BR | Contact self-energy on lower-right leg | R13 | Target |

## Slide 11

| Panel | Visible diagram / placement | Requirement | Relation |
| --- | --- | --- | --- |
| S11-T1 | Contact seagull on lower-right leg | R21 | Target |
| S11-T2 | Contact seagull on lower-right leg | R21 | Species/flow variant of S11-T1 |
| S11-T3 | Contact seagull on upper-right leg | R21 | Target |
| S11-T4 | Contact seagull on upper-right leg | R21 | Species/flow variant of S11-T3 |
| S11-B1 | Contact seagull on lower-left leg | R21 | Target |
| S11-B2 | Contact seagull on lower-left leg | R21 | Species/flow variant of S11-B1 |
| S11-B3 | Contact seagull on upper-left leg | R21 | Target |
| S11-B4 | Contact seagull on upper-left leg | R21 | Species/flow variant of S11-B3 |

Eight diagrams are visible although the slide contains fewer image objects; the composite images have been split into panel references.

## Slide 12

| Panel | Visible diagram / placement | Requirement | Relation |
| --- | --- | --- | --- |
| S12-left | Four-legged s-channel bubble | R05 | Repeated graph: S04-TR |
| S12-right | Triangle-contact, quartic vertex at right | R07 | Repeated graph: S03-right |

## Slide 13

| Panel | Visible diagram / placement | Requirement | Relation |
| --- | --- | --- | --- |
| S13-left | Triangle contact; quartic pair 1/4; Z between q2/q3 cubic vertices | R22 | M07c resolved; same missing external-routing extension as R14 |
| S13-right | Triangle contact; quartic pair 2/3; Z between q1/q4 cubic vertices | R22 | M07c resolved; same missing external-routing extension as R14 |

## Slide 14

| Panel | Visible diagram / placement | Requirement | Relation |
| --- | --- | --- | --- |
| S14-left | Four-legged t-channel bubble | R05 | Species/flow variant of S04-BR |
| S14-right | Four-legged bubble with crossed right external pair | R05 | u-channel layout: compare I16; species/flow variant |

## Slide 15

| Panel | Visible diagram / placement | Requirement | Relation |
| --- | --- | --- | --- |
| S15-left | Four-legged s-channel bubble | R05 | Species/flow variant of S04-TR |
| S15-right | Triangle-contact, quartic vertex at right | R07 | Repeated graph: S03-right |

## Slide 16

| Panel | Visible diagram / placement | Requirement | Relation |
| --- | --- | --- | --- |
| S16-TL | Stemmed loop on upper t-tree vertex | R20 | Target |
| S16-TR | Stemmed loop on left s-tree vertex | R20 | Target |
| S16-BL | Stemmed loop on lower t-tree vertex | R20 | Target |
| S16-BR | Stemmed loop on right s-tree vertex | R20 | Target |

## Slide 17

| Panel | Visible diagram / placement | Requirement | Relation |
| --- | --- | --- | --- |
| S17-TL | Stemmed loop on contact upper-right leg | R20 | Target |
| S17-TR | Stemmed loop on contact upper-left leg | R20 | Target |
| S17-BL | Stemmed loop on contact lower-right leg | R20 | Target |
| S17-BR | Stemmed loop on contact lower-left leg | R20 | Target |

## Slide 18

| Panel | Visible diagram / placement | Requirement | Relation |
| --- | --- | --- | --- |
| S18-TL | Stemmed loop on s-tree upper-right leg | R20 | Target |
| S18-TR | Stemmed loop on s-tree upper-left leg | R20 | Target |
| S18-BL | Stemmed loop on s-tree lower-right leg | R20 | Target |
| S18-BR | Stemmed loop on s-tree lower-left leg | R20 | Target |

## Slide 19

| Panel | Visible diagram / placement | Requirement | Relation |
| --- | --- | --- | --- |
| S19-TL | Stemmed loop on t-tree upper-left leg | R20 | Target |
| S19-TR | Stemmed loop on t-tree upper-right leg | R20 | Target |
| S19-BL | Stemmed loop on t-tree lower-left leg | R20 | Target |
| S19-BR | Stemmed loop on t-tree lower-right leg | R20 | Target |

## Slide 20

| Panel | Visible diagram / placement | Requirement | Relation |
| --- | --- | --- | --- |
| S20-TL | s-tree seagull on lower-right leg | R11 | Repeated graph / species variant: S07-C1 |
| S20-TR | s-tree seagull on upper-right leg | R11 | Repeated graph / species variant: S07-C2 |
| S20-BL | s-tree seagull on upper-left leg | R11 | Repeated graph / species variant: S06-C1 |
| S20-BR | s-tree seagull on lower-left leg | R11 | Repeated graph / species variant: S06-C2 |

## Slide 21

| Panel | Visible diagram / placement | Requirement | Relation |
| --- | --- | --- | --- |
| S21-TL | t-tree seagull on upper-right leg | R11 | Repeated graph / species variant: S08-C1 |
| S21-TR | t-tree seagull on upper-left leg | R11 | Repeated graph / species variant: S08-R1 |
| S21-BL | t-tree seagull on lower-right leg | R11 | Repeated graph / species variant: S05-C1 |
| S21-BR | t-tree seagull on lower-left leg | R11 | Repeated graph / species variant: S05-R1 |

## Slide 22

| Panel | Visible diagram / placement | Requirement | Relation |
| --- | --- | --- | --- |
| S22-TL | Left s-tree shared inner-vertex bubble | R19 | Repeated graph: S06-L1 |
| S22-TR | Top t-tree shared inner-vertex bubble | R19 | Target |
| S22-BL | Right s-tree shared inner-vertex bubble | R19 | Repeated graph: S07-L1 |
| S22-BR | Bottom t-tree shared inner-vertex bubble | R19 | Target |

## Slide 23

| Panel | Visible diagram / placement | Requirement | Relation |
| --- | --- | --- | --- |
| S23-TL | t-tree internal exchange self-energy | R17 | Target |
| S23-TR | s-tree internal exchange self-energy | R17 | Target |
| S23-BL | t-tree internal exchange seagull | R18 | Target |
| S23-BR | s-tree internal exchange seagull | R18 | Target |

## Context and non-target material

| Source | Treatment |
| --- | --- |
| S01 | Cover, title, author names; no diagram requirement. |
| S08-context | ResearchGate screenshot and swordfish commentary: terminology context for R12, not an instruction or a new graph. The seven actual diagram panels are listed separately. |
| S09 | Photographed handwritten swordfish/momentum notes: context for R12 and its annotation review. No independent additional supported topology is inferred. |
| S11-context | Editing tooltip and composite-image boundaries: UI/context, not diagram requirements. |
| PDF-P3-context | The unfinished “We also need” / trailing bullet has no accompanying distinct target; no extra capability is inferred. |

## Cross-cutting requirements

R06 (independent annotations), R15 (Proca endpoint contact), and R16 (documentation) apply to every relevant diagram, including repeats. R02 is requested in the PDF even though no isolated PowerPoint panel explicitly specifies the complementary internal crossing. M07c now records the full endpoint map for R14 and infers its correspondence to S13 from the established spatial slot numbering. R22 preserves the two slide-panel records for that same routing gap.

The cross-shaped contact hosts on slides 10, 11, and 17 are actual interactions. The crossovers on the box examples are routing crossings and must not acquire extra interaction vertices. The S13 panels are now traced: each has one quartic and two cubic interactions; its external crossover has no interaction. See the [M07c audit](m07c/routing-audit.pdf).
