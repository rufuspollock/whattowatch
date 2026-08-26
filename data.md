# Data Sources

Research on open, structured film/TV/ratings data to back the picker. Moved in from a separate planning project (`2026-film-tv-data-collection`, workspace `~/datasets/film-tv-data` — nothing built there yet, so folded the research in here). Detailed write-up per source lives in `docs/data-sources/`; this file is the index plus current status/decisions.

## Film metadata sources

- **[TMDB](docs/data-sources/tmdb.md)** — chosen source. Broad coverage, free API, filterable via `/discover/movie`. This is what `scripts/sync_tmdb.py` uses.
- **[IMDb](docs/data-sources/imdb.md)** — no free API, but free non-commercial bulk datasets (including ratings — see below). Restrictive license (no redistribution).
- **[Wikidata / Wikipedia](docs/data-sources/wikidata.md)** — not yet used. Most promising lead for the non-English curation gap below (permissively licensed, notability-gated).

### Non-English film filtering (known gap)

TMDB's `vote_count` doesn't reliably distinguish "major foreign films for a western audience" from Bollywood/anime/etc — checked live: more non-English films clear `vote_count≥800` than English films clear `vote_count≥300`, i.e. globally popular genre content outweighs the arthouse/prestige titles we'd actually want. A better approach would need real curation (e.g. seed from Oscar Best International Feature submissions, then expand via director/crew — Wikidata may help here, see above). Non-English films are excluded from the sync for now (English-only, see `docs/plans/2026-08-26-tmdb-sync-design.md`) pending this.

## Ratings / reviewer scores (separate from TMDB's own vote_average)

TMDB's `vote_average`/`vote_count` are TMDB-user ratings, not proper critic scores. Sources for those:

- **[Rotten Tomatoes](docs/data-sources/rotten-tomatoes.md)** — no free API (~$60k/yr direct license). Score available for free via OMDb.
- **[Metacritic](docs/data-sources/metacritic.md)** — no free API (paid-only). Score available for free via OMDb.
- **[Letterboxd](docs/data-sources/letterboxd.md)** — no public API (request-only, ungated timeline). Not currently accessible.
- **[IMDb](docs/data-sources/imdb.md)** — free bulk `title.ratings.tsv.gz`, not yet used as a cross-check.
- **[OMDb API](docs/data-sources/omdb.md)** — chosen source. Free aggregator surfacing IMDb/RT/Metacritic scores in one call. This is what `scripts/sync_omdb.py` uses.

## Open questions

- [ ] Evaluate Wikidata/Wikipedia as a source for non-English curation (see gap above)
- [ ] Add IMDb bulk `title.ratings.tsv.gz` as a free cross-check/complement to OMDb
- [ ] Design better non-English curation approach (award-submission based) per gap noted above
- [ ] Design schema for joining `films.jsonl` + `ratings_omdb.jsonl` (deliberately kept separate for now — join happens later)

## Status

- `data/films.jsonl` — 1,024 English films (last 5 years, runtime≥40min, vote_count≥300) via `scripts/sync_tmdb.py`.
- `data/ratings_omdb.jsonl` — in progress via `scripts/sync_omdb.py`. OMDb's free tier caps at 1,000 requests/day; script is resumable (skips already-fetched IDs, stops cleanly on quota) — rerun daily until complete.
