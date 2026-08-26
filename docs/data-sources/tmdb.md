# TMDB (The Movie Database)

**What it is:** A crowdsourced, community-edited film/TV/person database, founded 2008 as an open alternative to IMDb (which had shut its free API around then). Structurally similar to Wikipedia — volunteer editors maintain entries, moderated by TMDB staff. Free to use for both personal and (with attribution) many commercial purposes, which is unusual among the sources here.

**Coverage:** Very broad — hundreds of thousands of movies, tens of thousands of TV shows, millions of people (cast/crew). Especially strong on mainstream/Western theatrical and streaming releases; community-maintained so very obscure titles vary in completeness. Includes posters, backdrops, trailers (YouTube links), cast/crew, genres, keywords, production companies/countries, budget/revenue, and (crucially for this project) its own user vote_average/vote_count.

**Access:**
- **REST API** (`api.themoviedb.org/3`) — the main way in. `/discover/movie` supports rich server-side filtering (release date range, original language, runtime, vote count, genres, etc.) without needing to page through everything yourself. `/movie/{id}` gives full details per title. Auth via a free API key (v3) or bearer read-access token (v4, JWT — simpler auth header, no query param, preferred).
- **Daily bulk export** (`files.tmdb.org/p/exports/`) — gzip'd JSON-lines files of just IDs + popularity for movies/TV/people, refreshed daily. Good for a complete ID list or existence checks; not useful for filtering since it lacks release status, language, runtime, etc.
- **Third-party dumps** — e.g. a full TMDB movies dataset on Kaggle (~930k movies, snapshot through 2024) if you want an offline dump without hitting the API at all.

**Licensing:** Free for personal use (self-certify on signup). Commercial use requires prior approval from TMDB — see their terms. Attribution required for any images/data displayed (logos provided). Used in production by major platforms — notably Letterboxd sources its film metadata from TMDB rather than maintaining its own.

**How we use it here:** `/discover/movie` for filtering (English, last 5 years, runtime≥40min, vote_count≥300) then `/movie/{id}` for full per-film details. See `scripts/sync_tmdb.py` and `docs/plans/2026-08-26-tmdb-sync-design.md`.

**Gotchas found in practice:**
- `/discover/movie` list results don't include `runtime` even though `with_runtime.gte` filters on it server-side — you only get runtime by fetching each film's full detail.
- Its own `vote_count` doesn't reliably separate "major western-market film" from globally-popular non-English content (anime, Bollywood) — see the non-English filtering note in `data.md`.
- No first-class "status" filter on discover; we approximate "released" via a release-date-in-the-past window plus a vote_count floor (implying it has actually been seen/rated), and cross-checked that returned titles show `status: "Released"`.

**Links:** https://www.themoviedb.org · API docs: https://developer.themoviedb.org · Terms: https://www.themoviedb.org/talk/54f41aafc3a3683455000991 · Letterboxd's note on using TMDB: https://letterboxd.com/about/film-data/
