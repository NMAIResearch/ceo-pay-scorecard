# CEO Pay-vs-Delivery Scorecard: interactive (S&P 500)

An interactive front-end to *The CEO Pay-vs-Delivery Scorecard*: a reproducible, primary-sourced, descriptive audit of what the S&P 500's highest-paid CEOs took versus what they delivered.

**Live tool:** _(enable GitHub Pages, then paste the URL here)_
**Canonical record (frozen, citable):** [DOI 10.5281/zenodo.21445815](https://doi.org/10.5281/zenodo.21445815)
**Author:** NM AI Research · ORCID [0009-0003-4213-7769](https://orcid.org/0009-0003-4213-7769) · Licence CC BY 4.0

## What it does

Two views, switched at the top:

- **League table (494).** Toggle between granted pay (the Summary Compensation Table figure the press quotes) and realized pay (Compensation Actually Paid, the SEC measure that re-marks equity to the share price). The table reorders completely, and that reordering is the central finding (F1).
- **Board targets (29).** For 29 hand-curated companies, the board's *own* payout-versus-target beside peer-relative delivery (F4), with a column declaring what each payout measures so a cash-bonus % and a PSU-vesting % are never conflated.

Sort any column, filter by company or CEO, and read pay beside peer-relative shareholder return.

The page embeds the frozen `scorecard_sp500.csv` and `curated_targets.csv` verbatim, so it never goes stale and is not "live": the canonical, citable version is the Zenodo DOI above.

## Files

- `index.html`: the interactive tool, self-contained (no dependencies, no server needed).
- `scorecard_sp500.csv`: the frozen 494-company S&P 500 league-table dataset.
- `curated_targets.csv`: the 29-company board-target layer (the hand-read S&P-100 curated names; this layer does not scale to 500 and is unchanged in v2).
- `build.py`: regenerates `index.html` by embedding the two CSVs (pure standard library). Edit a CSV, run `python3 build.py`, commit.

The full reproducibility bundle, the EDGAR pull pipeline (`reproduce.py`, `assemble_sp500.py`), the 2,741-company-year spine (`pvp_pulled.csv`), and the findings, lives in the [Zenodo record](https://doi.org/10.5281/zenodo.21445815).

## Method (brief)

Built free from SEC EDGAR DEF 14A Pay-versus-Performance disclosures (Item 402(v)); 494 of the S&P 500 expose machine-readable XBRL (2,741 company-years). It is descriptive: it issues no "overpaid" verdict, sets the documented figures side by side, and leaves the conclusion to the reader.

## Guardrails

- **Attribution:** shareholder return is not caused by the CEO (macro, sector, luck, predecessor). The tool shows a co-incidence of pay and peer-relative return, not causation.
- **CAP caveat:** Compensation Actually Paid swings with the share price; it is an accounting fair value, not cash received.
- **Peer-group choice is the company's own** and drives the gap; a lag can mean the benchmark rose sharply.

## Disclosure

The author holds no direct position in any company named. A workplace defined-contribution pension may hold some indirectly through pooled funds, not directed by the author. No third party reviewed, funded, or directed this work.

## Licence

Creative Commons Attribution 4.0 International (CC BY 4.0).
