#!/usr/bin/env python3
"""Validate the frozen v2.2 data and embed the issuer view in index.html.

Inputs:
  scorecard_sp500.csv: 495 issuer rows
  board_targets.csv: 47 primary-verified cases
Output:
  index.html

The page carries the issuer CSV inline so it works without a server. Board-target
fields are already joined to the issuer view; board_targets.csv supplies the
primary-source audit trail.
"""
import csv
import pathlib
import re
import sys


HERE = pathlib.Path(__file__).resolve().parent
HTML = HERE / "index.html"
SCORECARD = HERE / "scorecard_sp500.csv"
TARGETS = HERE / "board_targets.csv"

REQUIRED_SCORECARD_FIELDS = {
    "ticker",
    "issuer_cik",
    "window_start_fy",
    "window_end_fy",
    "window_year_count",
    "latest_fy",
    "latest_granted_usd",
    "latest_cap_usd",
    "tsr_vs_peer",
    "board_target_in_scope",
    "board_target_verification",
    "source_accessions",
}


def read_rows(path):
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main():
    missing = [path.name for path in (HTML, SCORECARD, TARGETS) if not path.is_file()]
    if missing:
        sys.exit("missing required files: " + ", ".join(missing))

    scorecard = read_rows(SCORECARD)
    targets = read_rows(TARGETS)
    scorecard_fields = set(scorecard[0]) if scorecard else set()
    absent_fields = sorted(REQUIRED_SCORECARD_FIELDS - scorecard_fields)
    if absent_fields:
        sys.exit("scorecard fields missing: " + ", ".join(absent_fields))
    if len(scorecard) != 495:
        sys.exit(f"expected 495 issuer rows, found {len(scorecard)}")
    if len(targets) != 47:
        sys.exit(f"expected 47 board-target rows, found {len(targets)}")
    unverified = [row.get("ticker", "") for row in targets if row.get("verification_status") != "PRIMARY_VERIFIED"]
    if unverified:
        sys.exit("board-target rows are not primary-verified: " + ", ".join(unverified))

    joined = [row for row in scorecard if row.get("board_target_in_scope") == "True"]
    if len(joined) != 47:
        sys.exit(f"expected 47 joined board-target cases, found {len(joined)}")
    if any(row.get("board_target_verification") != "PRIMARY_VERIFIED" for row in joined):
        sys.exit("joined board-target verification is incomplete")

    csv_text = SCORECARD.read_text(encoding="utf-8").rstrip("\n")
    if "`" in csv_text:
        sys.exit("scorecard_sp500.csv contains a backtick")
    html = HTML.read_text(encoding="utf-8")
    pattern = re.compile(r"(const CSV = `)(.*?)(`;)", re.DOTALL)
    if len(pattern.findall(html)) != 1:
        sys.exit("expected one const CSV block in index.html")
    html = pattern.sub(lambda match: match.group(1) + csv_text + match.group(3), html)
    HTML.write_text(html, encoding="utf-8")

    print(f"embedded {len(scorecard)} issuer rows")
    print(f"validated {len(targets)} primary-verified board-target rows")
    print("wrote index.html")


if __name__ == "__main__":
    main()
