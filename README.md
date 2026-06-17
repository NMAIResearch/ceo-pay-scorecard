# CEO Pay-vs-Delivery Scorecard — interactive

An interactive front-end to *The CEO Pay-vs-Delivery Scorecard*: a reproducible, primary-sourced, descriptive audit of what the S&P-100's highest-paid CEOs **took** versus what they **delivered**.

**Live tool:** _(enable GitHub Pages, then paste the URL here)_
**Canonical record (frozen, citable):** [DOI 10.5281/zenodo.20680109](https://doi.org/10.5281/zenodo.20680109)
**Author:** N. Milton · ORCID [0009-0003-4213-7769](https://orcid.org/0009-0003-4213-7769) · Licence CC BY 4.0

## What it does

Toggle between **granted** pay (the Summary Compensation Table figure the press quotes) and **realized** pay (Compensation Actually Paid, the SEC measure that re-marks equity to the share price). The league table reorders completely — that reordering is the central finding. Sort any column, filter by company or CEO, and read each CEO's pay beside their peer-relative shareholder return.

The page reads the frozen `scorecard_v0.csv` verbatim (embedded in the file), so it never goes stale and is not "live" — the canonical, citable version is the Zenodo DOI above.

## Files

- `index.html` — the interactive tool, self-contained (no dependencies, no build step).
- `scorecard_v0.csv` — the frozen 98-company dataset the tool displays.

The full reproducibility bundle — the EDGAR pull pipeline (`reproduce.py`, `assemble.py`), the 539-company-year spine (`pvp_pulled.csv`), and the hand-curated board-target layer — lives in the [Zenodo record](https://doi.org/10.5281/zenodo.20680109).

## Method (brief)

Built free from SEC EDGAR DEF 14A Pay-versus-Performance disclosures (Item 402(v)); 98 of the S&P-100 expose machine-readable XBRL (539 company-years). It is **descriptive**: it issues no "overpaid" verdict, sets the documented figures side by side, and leaves the conclusion to the reader.

## Guardrails

- **Attribution:** shareholder return is not caused by the CEO (macro, sector, luck, predecessor). The tool shows a co-incidence of pay and peer-relative return, not causation.
- **CAP caveat:** Compensation Actually Paid swings with the share price; it is an accounting fair value, not cash received.
- **Peer-group choice is the company's own** and drives the gap — a lag can mean the benchmark ran hot.

## Disclosure

The author holds no direct position in any company named. A workplace defined-contribution pension may hold some indirectly through pooled funds, not directed by the author. No third party reviewed, funded, or directed this work.

## Licence

Creative Commons Attribution 4.0 International (CC BY 4.0).
