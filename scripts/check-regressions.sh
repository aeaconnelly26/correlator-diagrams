#!/usr/bin/env sh
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_root=$(CDPATH= cd -- "$script_dir/.." && pwd)
build_root=${TMPDIR:-/tmp}/feynmanfun-regressions-$$

trap 'rm -rf "$build_root"' EXIT HUP INT TERM

cleanup_latex_scratch() {
  find "$repo_root" \( \
    -name '*.aux' -o \
    -name '*.log' -o \
    -name '*.out' -o \
    -name '*.fls' -o \
    -name '*.fdb_latexmk' -o \
    -name 'texput.log' \
  \) -delete
}

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
    return 1
  fi
}

cleanup_latex_scratch

run_tex "example.tex"
run_tex "vertex-example/vertex-example.tex"
run_tex "regressions/compat/correlator-diagrams-wrapper.tex"
run_tex "regressions/topologies/triangle-contact/triangle-contact-regression.tex"
run_tex "regressions/topologies/triangle-contact/triangle-contact-internal-momentum.tex"
run_tex "regressions/topologies/triangle-contact/momentum-directions-demo.tex"
run_tex "regressions/topologies/vertex-identity/vertex-identity-check.tex"
run_tex "regressions/topologies/vertex-identity/half-box-bridge-momentum.tex"
run_tex "regressions/topologies/three-point/three-point-check.tex"
run_tex "regressions/topologies/box/box-topology-regression.tex"

cleanup_latex_scratch
