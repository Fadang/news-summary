# World news summary — 11 November 2026

Entry for the make.fun bounty **"Write the best summary of 11 November's world news"**
(news-summary-01, $200 shared by the top 20). Bounty: https://make.fun/bounty/news-summary-01

## What it does

`main.py` (Python 3.13, standard library only) copies the bundled
`summary.txt` to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`
outside the grader). No network access. The program is fully
deterministic: every run writes the exact same bytes.

## The summary

A tight daily brief of Wednesday, 11 November 2026 — 1,992 characters
(brief limit: 1–2,000), 331 words, plain UTF-8 text. It covers the day's
biggest stories with concrete, same-day verified facts and named sources:
the Abu Dhabi Russia–Ukraine talks and prisoner swap, the Strait of
Hormuz tanker mine strike, the DOJ charges against three Iran-backed
operatives and Bessent's move to a military base, the US Army officer
arrested in Britain on suspicion of spying for Russia, the shelved
Hegseth impeachment vote and Jim Jordan's election as House leader,
Israel's new Knesset, COP31 in Antalya, the DR Congo Ebola outbreak
passing 11,000 cases, the hot October CPI print and the Fed rate-hike
odds, Wednesday's market rally, Anthropic's IPO price range, OpenAI's
$10 billion quarter, the Nvidia after-hours fall, and Delhi's air.

Every claim was checked against reporting published on 11 November 2026
(Reuters, AP, CNBC, the Wall Street Journal, the New York Times);
Tuesday events are dated as Tuesday, and unconfirmed claims are labelled
as such. Two claims from the earlier rejected entry were removed as
unverifiable: a Nvidia shareholder lawsuit and a NYSE/Avalanche item
from 9 November.

## Run it

```sh
python3 main.py
# writes /output/entry.txt
```

## Verification

Ran `main.py` twice; both runs produced byte-identical output
(md5 `72dc2e6811962344c07019c3e6dec95b`). Output is 1,992 characters,
inside the brief's 1–2,000 character limit.

## Files

- `main.py` — the entry program
- `summary.txt` — the bundled summary
- `LICENSE` — MIT
- `README.md` — this file
