#!/usr/bin/env python3
"""
Rebuild index.html by embedding the current CSV data into it.

The interactive page carries its data inline (so it renders standalone, including
the copy archived on Zenodo). This script keeps those inline copies in sync with
the source CSVs: edit a CSV, run `python3 build.py`, commit the new index.html.

  scorecard_sp500.csv -> const CSV     (the 494-company S&P 500 league table)
  curated_targets.csv -> const CURATED (the 29-company board-target layer)

Pure standard library, no dependencies.
"""
import re
import sys
import pathlib

HERE = pathlib.Path(__file__).parent
HTML = HERE / "index.html"

# (variable name in the page, source CSV file)
BLOCKS = [
    ("CSV", HERE / "scorecard_sp500.csv"),
    ("CURATED", HERE / "curated_targets.csv"),
]


def main() -> int:
    if not HTML.exists():
        print("error: run this from the folder containing index.html")
        return 1

    html = HTML.read_text(encoding="utf-8")

    for var, csv_path in BLOCKS:
        if not csv_path.exists():
            print(f"error: missing {csv_path.name}")
            return 1
        csv_text = csv_path.read_text(encoding="utf-8").strip()
        if "`" in csv_text:
            print(f"error: {csv_path.name} contains a backtick, which would break the embedded string")
            return 1
        pattern = re.compile(r"(const " + var + r" = `)(.*?)(`;)", re.DOTALL)
        if not pattern.search(html):
            print(f"error: could not find the `const {var} = ` ... `;` block in index.html")
            return 1
        html = pattern.sub(lambda m: m.group(1) + csv_text + m.group(3), html)
        rows = csv_text.count("\n")  # data rows (header line has no preceding newline)
        print(f"embedded {rows} data rows from {csv_path.name} into const {var}")

    HTML.write_text(html, encoding="utf-8")
    print("done. next: commit index.html (and the CSVs) and push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
