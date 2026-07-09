# Endcap And Triple-Vertex Styling Ideas

This branch is a planning anchor for putting more design energy into the
triple-vertex topology and endpoint cap styling.

## Endcap Goals

- Revisit the current endcap feature with more care. The existing cap scales
  strangely in some diagrams, can feel too short, and sometimes has awkward
  spacing relative to the leg it terminates.
- Add a double-endcap feature, likely named `endcapp`, for physically
  polarized endpoint styling that needs a stronger visual signal than the
  current single bar.
- Try multiple double-endcap designs before locking in the public shape. One
  candidate is a pair of terminal bars where the second-to-last bar is longer
  than the final bar.
- Fix current endcap bugs where composed leg add-ons behave differently
  depending on ordering. In particular, some combinations can lose the intended
  color, create a wonky gap between the cap and propagator leg, or otherwise
  render oddly.

## Triple-Vertex Goals

- Expand the rotation controls for the three-point vertex topology so the
  external leg can point left, right, up, or down.
- Treat this as redirecting the whole vertex object in space across four
  cardinal orientations, rather than only tweaking individual coordinates.
- Add line-length controls so the external leg can be shortened independently
  when needed.
- Design a special `epspol` leg for the three-point vertex. This should be a
  shorter external leg than the other two directions and should use the new
  double-endcap styling.

## Notes

- The endcap implementation should ideally become more general and predictable
  instead of relying on fragile ordering between propagator style add-ons.
- The visual goal is a cleaner triple vertex with more intentional endpoint
  language, especially for physically polarized external legs.
