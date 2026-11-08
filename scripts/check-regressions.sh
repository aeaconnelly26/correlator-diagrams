#!/usr/bin/env sh
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_root=$(CDPATH= cd -- "$script_dir/.." && pwd)
build_root=$(mktemp -d "${TMPDIR:-/tmp}/feynmanfun-regressions.XXXXXX")

trap 'rm -rf -- "$build_root"' EXIT
trap 'exit 1' HUP INT TERM

check_count=0

run_tex() {
  rel_path=$1
  tex_dir=$(dirname -- "$rel_path")
  tex_file=$(basename -- "$rel_path")
  out_dir="$build_root/$tex_dir"
  mkdir -p "$out_dir"

  printf 'CHECK %s\n' "$rel_path"
  if (
    cd "$repo_root/$tex_dir"
    TEXINPUTS="$repo_root//:" pdflatex -interaction=batchmode -halt-on-error -output-directory="$out_dir" "$tex_file" >/dev/null
  ); then
    printf 'PASS  %s\n' "$rel_path"
  else
    printf 'FAIL  %s\n' "$rel_path" >&2
    if [ -f "$out_dir/${tex_file%.tex}.log" ]; then
      tail -n 80 "$out_dir/${tex_file%.tex}.log" >&2
    fi
    return 1
  fi
  check_count=$((check_count + 1))
}

run_tex "example.tex"
run_tex "vertex-example/vertex-example.tex"
run_tex "compton-example/compton-example.tex"
run_tex "regressions/compat/correlator-diagrams-wrapper.tex"
run_tex "regressions/scale/diagram-scale.tex"
run_tex "regressions/topologies/triangle-contact/triangle-contact-regression.tex"
run_tex "regressions/topologies/triangle-contact/triangle-contact-internal-momentum.tex"
run_tex "regressions/topologies/triangle-contact/momentum-directions-demo.tex"
run_tex "regressions/topologies/triangle-contact/triangle-contact-annotations.tex"
run_tex "regressions/topologies/vertex-identity/vertex-identity-check.tex"
run_tex "regressions/topologies/vertex-identity/half-box-bridge-momentum.tex"
run_tex "regressions/topologies/channel/channel-momentum-label-gap.tex"
run_tex "regressions/momenta/external-momentum-visibility.tex"
run_tex "regressions/labels/mini-index.tex"
run_tex "regressions/propagators/proca/one-sided-loop-markers.tex"
run_tex "regressions/topologies/three-point/three-point-check.tex"
run_tex "regressions/topologies/three-point/three-point-translation-check.tex"
run_tex "regressions/propagators/scalar-polarization/scalar-polarization-check.tex"
run_tex "regressions/topologies/bubble/bubble-regression.tex"
run_tex "regressions/topologies/insertion/insertion-regression.tex"
run_tex "regressions/topologies/insertion/insertion-endcaps.tex"
run_tex "regressions/topologies/insertion/t-tree-bubble-slots.tex"
run_tex "regressions/topologies/insertion/s-tree-bubble-slots.tex"
run_tex "regressions/topologies/insertion/seagull-insertion-regression.tex"
run_tex "regressions/topologies/insertion/seagull-slots.tex"
run_tex "regressions/topologies/insertion/swordfish-slots.tex"
run_tex "regressions/topologies/insertion/tree-triangle-slots.tex"
run_tex "regressions/topologies/insertion/insertion-momentum-review.tex"
run_tex "regressions/topologies/insertion/insertion-species-samples.tex"
run_tex "regressions/topologies/loop-audit/loop-momentum-audit.tex"
run_tex "regressions/topologies/loop-audit/self-energy-bubble-mockups.tex"
run_tex "regressions/topologies/box/box-topology-regression.tex"
run_tex "regressions/topologies/box/box-external-crossing.tex"
run_tex "regressions/propagators/circ/propagator-circ-check.tex"
run_tex "regressions/propagators/endpoint-markers/endpoint-marker-regression.tex"
run_tex "regressions/propagators/ewboson-frequency/ewboson-frequency-check.tex"
run_tex "regressions/propagators/proca/proca-regression.tex"
run_tex "regressions/propagators/w-favorites/w-propagator-favorites.tex"
run_tex "regressions/topologies/channel/channel-topology-regression.tex"
run_tex "regressions/topologies/channel/s-tree-span-regression.tex"
run_tex "regressions/topologies/cross-box/cross-box-regression.tex"
run_tex "regressions/topologies/cross-box/cross-box-layouts.tex"
run_tex "regressions/topologies/internal-indices/internal-index-slots.tex"
run_tex "regressions/topologies/sunset/sunset-example.tex"
run_tex "regressions/topologies/sunset/sunset-index-regression.tex"
run_tex "regressions/topologies/three-point/three-point-feature-gallery.tex"

run_tex "regressions/propagators/proca-endpoints/proca-endpoint-audit.tex"

if [ -n "${FEYNMANFUN_PDF_PYTHON:-}" ]; then
  "$FEYNMANFUN_PDF_PYTHON" \
    "$repo_root/regressions/topologies/box/check-box-external-crossing.py" \
    "$build_root/regressions/topologies/box/box-external-crossing.pdf"
  "$FEYNMANFUN_PDF_PYTHON" \
    "$repo_root/regressions/topologies/cross-box/check-cross-box-layouts.py" \
    "$build_root/regressions/topologies/cross-box/cross-box-layouts.pdf"
  "$FEYNMANFUN_PDF_PYTHON" \
    "$repo_root/regressions/topologies/insertion/check-insertion-endcaps.py" \
    "$build_root/regressions/topologies/insertion/insertion-endcaps.pdf"
  "$FEYNMANFUN_PDF_PYTHON" \
    "$repo_root/regressions/propagators/proca-endpoints/check-endpoint-contact.py" \
    "$build_root/regressions/propagators/proca-endpoints/proca-endpoint-audit.pdf" \
    --baseline "$repo_root/regressions/propagators/proca-endpoints/proca-endpoint-audit-before.pdf"
  "$FEYNMANFUN_PDF_PYTHON" \
    "$repo_root/regressions/topologies/insertion/check-t-tree-bubble-contact.py" \
    "$build_root/regressions/topologies/insertion/t-tree-bubble-slots.pdf"
  "$FEYNMANFUN_PDF_PYTHON" \
    "$repo_root/regressions/topologies/insertion/check-s-tree-bubble-contact.py" \
    "$build_root/regressions/topologies/insertion/s-tree-bubble-slots.pdf"
  "$FEYNMANFUN_PDF_PYTHON" \
    "$repo_root/regressions/topologies/insertion/check-seagull-contact.py" \
    "$build_root/regressions/topologies/insertion/seagull-slots.pdf"
  "$FEYNMANFUN_PDF_PYTHON" \
    "$repo_root/regressions/topologies/insertion/check-species-circles.py" \
    "$build_root/regressions/topologies/insertion/insertion-species-samples.pdf"
  "$FEYNMANFUN_PDF_PYTHON" \
    "$repo_root/regressions/propagators/ewboson-frequency/check-ewboson-wavelength.py" \
    "$build_root/regressions/propagators/ewboson-frequency/ewboson-frequency-check.pdf"
  "$FEYNMANFUN_PDF_PYTHON" \
    "$repo_root/regressions/topologies/insertion/check-swordfish.py" \
    "$build_root/regressions/topologies/insertion/swordfish-slots.pdf"
  "$FEYNMANFUN_PDF_PYTHON" \
    "$repo_root/regressions/topologies/insertion/check-tree-triangle.py" \
    "$build_root/regressions/topologies/insertion/tree-triangle-slots.pdf"
fi

printf 'PASS  all %s regression and example documents\n' "$check_count"
