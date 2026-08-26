# TMDB Sync — Design

Pull a filtered, curated slice of TMDB movies into this repo as the data backbone for the picker.

## Scope (v1)

- Movies only (no TV yet)
- English original language (`with_original_language=en`) — non-English deferred; vote_count alone doesn't reliably exclude Bollywood/anime (checked live: more non-English films clear vote_count≥800 than English films clear vote_count≥300), so a real curation approach (e.g. award-submission based) is needed first. Tracked in `data.md`.
- Last 5 years, rolling window computed at sync time
- `with_runtime.gte=40` (excludes shorts)
- `vote_count.gte=300` — tunable constant, currently yields ~1,170 films (~235/yr)

## Pipeline

1. Page `/discover/movie` with the filters above (sorted by popularity) to collect matching movie IDs.
2. For each ID, fetch `/movie/{id}` for full details (runtime, named genres, overview, production countries, etc.).
3. Write one JSON object per line to `data/films.jsonl`, sorted by TMDB id (stable diffs).
4. Fetch `/genre/movie/list` once → `data/genres.json`.

## Script

`scripts/sync_tmdb.py`. Reads bearer token from `~/.config/tmdb/apikeyread`. `--limit N` flag to cap the number of films fetched, for fast iteration — default small (e.g. 50) so runs stay quick while iterating; full sync passes a high/no limit. Retries on 429/5xx with backoff; logs and skips 404s; fails loudly on auth errors. Idempotent — overwrites `films.jsonl` fresh each run.

## Approach

Ship small, iterate. First pass: small `--limit`, validate the pipeline and field choices actually work for the picker before running the full ~1,170-film sync. Thresholds/fields expected to change as we learn.

## Testing

Manual: run script, check output line count and a few sample entries look right.
