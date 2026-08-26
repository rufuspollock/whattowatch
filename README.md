# What to Watch

Simple tool for answering "what should I watch tonight?" — a film (later maybe series) picker.

## Idea

Instead of a long questionnaire, learn what kind of film you want through quick pairwise comparisons ("this or that?"), then make a selection. Skip/continue if you've already seen a suggestion.

Backed by an open, structured database of films (open dataset or scraped from Wikipedia — TBD).

Source idea: `~/src/me/planning/ideas/tonights-film-picker.md`. Earlier root idea (2016, neural-net movie matrix): `~/src/me/notebook/ideas/README.md`.

See [`data.md`](data.md) for research on open movie/TV data sources.

## Plan

1. **v0 (now):** Interactive CLI session, no persistence, small hardcoded/manual film list — just pick via pairwise comparison, mark "seen" to skip.
2. Research open movie databases (coverage, licensing, query options).
3. Swap manual list for real dataset.
4. Decide what preference state (if any) persists between sessions.
5. Extend to series.

## Status

Just started. Building v0 CLI picker first.
