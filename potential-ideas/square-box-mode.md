# Square Box Topology Mode

Idea: create a new branch for a box diagram option mode where the rendered
box is exactly square-shaped.

Desired public interface:

- Add a topology mode or style option for `\BoxLoopCorr[...]` that applies the
  square geometry settings.
- Add a convenience macro named `\SquareBox` that defaults to those square-box
  settings.

Intent:

- Keep ordinary `\BoxLoopCorr` behavior available.
- Make it easy to request a compact, symmetric box without repeatedly tuning
  `box-xspan`, `box-yspan`, `box-external-xspan`, and `box-external-yspan`.
- Treat this as a future feature branch, not part of the current merged box
  endcap/cross-box/triangle-contact work.
