# CEO Pay-vs-Delivery Scorecard: interactive S&P 500 edition

A frozen interactive front-end to *The CEO Pay-vs-Delivery Scorecard*, a reproducible descriptive audit of granted compensation, Compensation Actually Paid and shareholder return across a dated S&P 500 universe.

- **Live tool:** https://nmairesearch.github.io/ceo-pay-scorecard/
- **Canonical concept DOI:** https://doi.org/10.5281/zenodo.20680108
- **Current v2.2 record:** https://doi.org/10.5281/zenodo.21863369
- **Author:** NM AI Research, ORCID [0009-0003-4213-7769](https://orcid.org/0009-0003-4213-7769)
- **Licence:** CC BY 4.0

Parts of the text were artificially generated with AI assistance and reviewed by the author. Anthropic Opus 4.8 assisted with retrieval and drafting. OpenAI GPT-5.6 Sol checked and revised v2.2. The conflict is described below.

## Coverage

The dated universe contains 503 constituent securities. SEC Pay Versus Performance data are populated for 498 securities, with five explicit placeholders. Dual share classes are collapsed by SEC CIK to produce 495 issuer rows. Of those issuers, 493 contain both company and peer total shareholder return.

The audited board-target layer contains 47 cases: 29 original S&P 100 cases and 18 S&P 500 findings extensions. Every case carries primary filing metadata.

## What the tool does

- Toggle granted compensation against Compensation Actually Paid.
- Switch between the latest fiscal year and each issuer's available reporting window.
- Sort and filter the 495-issuer view.
- Read peer-relative shareholder return, reporting-window bounds and board-target annotations beside each issuer.

The page is self-contained. Its frozen issuer data are embedded directly from `scorecard_sp500.csv`.

## Files

- `index.html`: the self-contained interactive tool archived with v2.2.
- `scorecard_sp500.csv`: the 495-issuer frozen view with reporting windows and SEC accessions.
- `board_targets.csv`: 47 primary-verified board-target cases.
- `build.py`: validates the two CSV files and re-embeds `scorecard_sp500.csv` into `index.html`.
- `LICENSE`: Creative Commons Attribution 4.0 International.

## Rebuild

Run in your terminal from this repository:

```sh
python3 build.py
```

The script uses only the Python standard library. A successful rebuild reports 495 issuer rows and 47 primary-verified board-target rows.

The full reproduction bundle, including the 2,768 populated company-year SEC spine, CEO-name backfills, universe list and `assemble_sp500.py`, is preserved in the [v2.2 Zenodo record](https://doi.org/10.5281/zenodo.21863369).

## Guardrails and conflict

- Shareholder return is not caused by the CEO. Macro conditions, sector exposure, predecessor decisions and luck also affect it.
- Compensation Actually Paid is an accounting fair-value remeasurement, not cash received.
- The peer benchmark is selected or disclosed by the issuer. Its composition affects the gap.
- The board-target cases mix different cash and equity measures and are not a common cross-company metric.
- The analysis is descriptive and does not issue an overpaid verdict.

The author holds no direct position in any company named. A workplace defined-contribution pension may hold some names indirectly through pooled funds not directed by the author. No third party funded or directed the work. Anthropic and OpenAI are model providers and compete with some companies discussed or their products. Neither model provider is an issuer in this dataset. This is a potential conflict, not evidence that any result is wrong.
