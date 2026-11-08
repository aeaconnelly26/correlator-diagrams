# M07c existing public recipes

Baseline: M07c branch from `843c2bf`; package code remains at verified checkpoint
`e2521e2`. These recipes compile through the existing public interface. They
show the supported adjacent-pair layouts and Z styling. **None reproduces the
opposite-quartic-pair attachment in S13-left/right with fixed outer slots.**

External slots: 1 UL, 2 LL, 3 UR, 4 LR. `leg-labels` here names the outer
endpoints; momentum annotations are hidden for clarity.

## E01-E04: all supported quartic pairs

Paste the following recipe and select `top`, `bottom`, `left` or `right`.
The quartic pairs are respectively 1/3, 2/4, 1/2 and 3/4. Existing atlas IDs
I23-I26 cover these orientations; these audit recipes add no inventory count.

```tex
\TriangleContactCorr[
  field={}, central={}, show-momenta=false,
  leg-labels={q_1,q_2,q_3,q_4},
  triangle-contact-orientation=top,
  triangle-contact-line=plain,
  triangle-contact-external-line=plain,
  triangle-contact-internal-line=plain,
  triangle-contact-xspan=1.1,
  triangle-contact-yspan=1.1
]
```

The equal spans give a square internal bounding box using existing keys.
Four-point outer endpoints retain the shared +/-2.10 frame. Adjusting spans
changes geometry, not the logical quartic pair.

## E05: top quartic, Z on internal slot 6

The current quartic pair is 1/3; Z joins vertices carrying q2/q4. S13-left
instead needs quartic pair 1/4 and Z between the q2/q3 vertices.

```tex
\TriangleContactCorr[
  field={}, central={}, show-momenta=false,
  leg-labels={q_1,q_2,q_3,q_4},
  triangle-contact-orientation=top,
  triangle-contact-xspan=1.1,
  triangle-contact-yspan=1.1,
  triangle-contact-external-line=ewboson,
  triangle-contact-internal-lines={
    ewboson,{ewboson,circ=Z},ewboson
  }
]
```

## E06: bottom quartic, Z on internal slot 5

The current quartic pair is 2/4; Z joins vertices carrying q1/q3. S13-right
instead needs quartic pair 2/3 and Z between the q1/q4 vertices.

```tex
\TriangleContactCorr[
  field={}, central={}, show-momenta=false,
  leg-labels={q_1,q_2,q_3,q_4},
  triangle-contact-orientation=bottom,
  triangle-contact-xspan=1.1,
  triangle-contact-yspan=1.1,
  triangle-contact-external-line=ewboson,
  triangle-contact-internal-lines={
    {ewboson,circ=Z},ewboson,ewboson
  }
]
```

The circle defaults to scale .8. Global `line=plain` is omitted from these
styled examples so explicit topology line styles retain their intended role.
Target traces on page 1 of `routing-audit.pdf` are specification drawings,
clearly labeled as unimplemented routing; they are not package recipes.
