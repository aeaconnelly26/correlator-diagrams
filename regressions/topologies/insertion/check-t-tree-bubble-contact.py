#!/usr/bin/env python3
"""Check the isolated all-slot Proca page using the maintained PDF inspector."""
import argparse
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
source = Path(__file__).resolve().parents[2] / 'propagators/proca-endpoints/check-endpoint-contact.py'
spec = importlib.util.spec_from_file_location('endpoint_contact', source)
contact = importlib.util.module_from_spec(spec)
spec.loader.exec_module(contact)

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('pdf', type=Path)
parser.add_argument('--report', type=Path)
args = parser.parse_args()
pages = contact.inspect(args.pdf)
assert len(pages) == 4, 'Expected complete four-page M03a gallery'
report = pages[3]
assert report['triangles'] == report['dots'] == 16, report
assert all(g >= -0.21 for g in report['gaps_pt']), report
assert all(g <= 0.02 for g in report['visible_gaps_pt']), report
assert all(c[0] > 0.9 and c[1] < 0.1 and c[2] > 0.9 for c in report['colors']), report
if args.report:
    args.report.write_text(json.dumps(report, indent=2) + '\n')
print('PASS M03a: 16 white-filled pink Proca tips contact vertices across all four t-tree placements')
