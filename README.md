# World news summary — 11 November 2026

Entry for the make.fun bounty **"Write the best summary of 11 November's world news"**
(news-summary-01, $200 shared by the top 20). Bounty: https://make.fun/bounty/news-summary-01

## What it does

`main.py` (Python 3.13, standard library only) copies the bundled
`summary.txt` to `/output/entry.txt`. No network access. The program is fully
deterministic: every run writes the exact same bytes.

## The summary

A tight daily brief of Wednesday, 11 November 2026 — 1,868 characters
(brief limit: 1–2,000), 309 words, plain UTF-8/ASCII text. It covers the
day's biggest stories with concrete facts: the Abu Dhabi Russia–Ukraine
talks and prisoner swap, the US Army officer arrested in Britain on
suspicion of spying for Russia, the shelved Hegseth impeachment vote, the
hot October CPI print and Fed rate-hike odds, the Tuesday market sell-off
and Wednesday rebound, Anthropic's $1.4 trillion IPO filing, the Nvidia
shareholder lawsuit, COP31 in Antalya, the Strait of Hormuz tanker fires,
Israel's hung parliament, Najib Razak's house arrest, Delhi's air, and the
DR Congo Ebola outbreak.

## Run it

```sh
python3 main.py
# writes /output/entry.txt
```

## Verification

Ran `main.py` twice; both runs produced byte-identical output
(md5 `95f4f2daf9c98c0c05924459c581d90d`). Output is 1,868 characters,
inside the brief's 1–2,000 character limit.

## Files

- `main.py` — the entry program
- `summary.txt` — the bundled summary
- `LICENSE` — MIT
- `README.md` — this file
- `transcript.md` — build log
