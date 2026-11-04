#!/usr/bin/env python3
"""Measure rendered EW wave density, alias/key order and per-line isolation."""
import argparse
import json
from pathlib import Path

from pypdf import PdfReader
from pypdf.generic import ContentStream


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    reader = PdfReader(args.pdf)
    assert len(reader.pages) == 2, 'Expected the complete two-page wavelength gallery'
    curves, strokes = 0, []
    for operands, operator in ContentStream(reader.pages[1].get_contents(), reader).operations:
        if operator == b'c':
            curves += 1
        elif operator in (b'S', b's', b'f', b'F', b'f*', b'B', b'B*', b'b', b'b*', b'n'):
            if operator in (b'S', b's'):
                strokes.append(curves)
            curves = 0
    # First four stroked paths are equal-length raw lines: default, shortened
    # wavelength, key-before-photon alias, and another unmodified default.
    default, tight, alias, reset = strokes[:4]
    assert default > 0 and tight > 2*default, 'Shorter wavelength did not add visible oscillations'
    assert tight == alias, 'Photon alias or key ordering lost the local wavelength'
    assert reset == default, 'Local wavelength leaked into the following propagator'
    report = {'wave_curve_counts': [default, tight, alias, reset],
              'shorter_to_default_curve_ratio': tight/default,
              'alias_and_key_order_match': True, 'default_restored_next_line': True}
    if args.report:
        args.report.write_text(json.dumps(report, indent=2)+'\n')
    print(f'PASS EW waves: {default}/{tight}/{alias}/{reset} rendered curve segments; '
          'shorter wavelength, alias/key order and per-line reset')


if __name__ == '__main__':
    main()
