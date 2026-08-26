# Data Sources

Research on open, structured film/TV databases to back the picker. Moved in from a separate planning project (`2026-film-tv-data-collection`, workspace `~/datasets/film-tv-data` — nothing built there yet, so folding the research here for now).

## Candidates

- **TMDB (The Movie Database)** — best candidate so far. Broad coverage, API-friendly license. Used by major platforms like Letterboxd (see https://letterboxd.com/about/film-data/). License terms: https://www.themoviedb.org/talk/54f41aafc3a3683455000991. Full dump available on Kaggle, covers through 2024: https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies
- **IMDB** — large database but restrictive licensing. Non-commercial datasets: https://developer.imdb.com/non-commercial-datasets/. Needs separate documentation of licensing/access before use.
- **Wikidata / Wikipedia dumps** — not yet evaluated.

## Open questions

- [ ] Evaluate TMDB API rate limits, data coverage, license terms for bulk querying
- [ ] Document IMDB licensing and access in more detail
- [ ] Evaluate Wikidata/Wikipedia as source or complement
- [ ] Design schema (fields, format, coverage targets) for whatever gets pulled in
- [ ] Extract/compile initial dataset for v1 (post manual-list v0)

## Status

TMDB is the leading option; nothing pulled in yet. v0 of the picker uses a small hardcoded film list instead.
