# Data Sources

Research on open, structured film/TV databases to back the picker. Moved in from a separate planning project (`2026-film-tv-data-collection`, workspace `~/datasets/film-tv-data` — nothing built there yet, so folding the research here for now).

## Candidates

- **TMDB (The Movie Database)** — best candidate so far. Broad coverage, API-friendly license. Used by major platforms like Letterboxd (see https://letterboxd.com/about/film-data/). License terms: https://www.themoviedb.org/talk/54f41aafc3a3683455000991. Full dump available on Kaggle, covers through 2024: https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies
  - **Daily bulk export**: `files.tmdb.org/p/exports/` — gzip'd JSON-lines files of movie/tv/person IDs + popularity, updated daily. IDs only, not full metadata — useful for a complete ID list but not for filtering by release status/language/date, so not used for our sync (see `docs/plans/` for the sync design).
  - **API `/discover/movie`**: supports server-side filters (release date range, original language, release status, vote count, etc.) — this is what we use for the filtered sync.
- **IMDB** — large database but restrictive licensing. Non-commercial datasets: https://developer.imdb.com/non-commercial-datasets/. Needs separate documentation of licensing/access before use.
- **Wikidata / Wikipedia dumps** — not yet evaluated.

### Non-English film filtering (known gap)

TMDB's `vote_count` doesn't reliably distinguish "major foreign films for a western audience" from Bollywood/anime/etc — checked live: more non-English films clear `vote_count≥800` than English films clear `vote_count≥300`, i.e. globally popular genre content outweighs the arthouse/prestige titles we'd actually want. A better approach would need real curation (e.g. seed from Oscar Best International Feature submissions, then expand via director/crew). Non-English films are excluded from the sync for now (English-only, see `docs/plans/2026-08-26-tmdb-sync-design.md`) pending this.

## Ratings / reviewer scores (separate from TMDB's own vote_average)

TMDB's `vote_average`/`vote_count` are TMDB-user ratings, not proper critic scores (Rotten Tomatoes, Metacritic) or a dedicated cinephile audience (Letterboxd). Researched where to get those:

- **Rotten Tomatoes** — no open/free API. Official access is via Fandango's RT Developer Network, application/approval required (up to 60 days), license fee starts around $60k/year for full scores + review snippets. Not viable for a personal project. Unofficial scrapers exist but scraping violates RT's ToS — not recommended.
- **Letterboxd** — no public self-serve API (as of 2026). API access is by request only (email api@letterboxd.com), no guaranteed approval. Letterboxd's film metadata is itself TMDB-backed, so the only independent value would be its own user ratings — which is exactly the gated part. Unofficial scrapers exist, same ToS-risk caveat.
- **IMDb** — confirmed real and current: non-commercial datasets at `datasets.imdbws.com`, refreshed daily, includes `title.ratings.tsv.gz` (average rating + vote count per title). Free to download, restricted to personal/non-commercial use under IMDb's licensing terms (no redistribution/commercial use). Most accessible real rating source found.
- **Metacritic** — no free/open API. Access via Fabric Origin's developer portal, requires a paid subscription tier (Metacritic data excluded from free trial). No self-serve free option.
- **OMDb API** (`omdbapi.com`) — best practical option: one call returns IMDb rating, Rotten Tomatoes score, and Metascore together (it's an aggregator sourcing from those, not an independent source). Free tier: 1,000 requests/day, no cost. Paid tiers via Patreon pledge ($1/mo+) raise the cap (up to 100k+/day) and unlock poster API. Flat pledge-based pricing, no metered billing.

**Recommendation for later**: OMDb API for RT/Metacritic/IMDb ratings in one shot (free tier likely sufficient at ~1,000/day for our film count), plus IMDb's bulk `title.ratings.tsv.gz` as a free bulk complement/cross-check. Skip direct RT/Metacritic API deals (cost-prohibitive) and skip scraping RT/Letterboxd (ToS risk). Not yet implemented — this is source identification only.

## Open questions

- [ ] Evaluate TMDB API rate limits, data coverage, license terms for bulk querying
- [ ] Document IMDB licensing and access in more detail
- [ ] Evaluate Wikidata/Wikipedia as source or complement
- [ ] Design schema (fields, format, coverage targets) for whatever gets pulled in
- [ ] Pull in ratings data (OMDb API + IMDb bulk ratings.tsv, per above) once schema settled
- [ ] Design better non-English curation approach (award-submission based) per gap noted above

## Status

TMDB sync live: `data/films.jsonl` has 1,024 English films (last 5 years, runtime≥40min, vote_count≥300) via `scripts/sync_tmdb.py`. Ratings-source research done (above) but not yet integrated.
