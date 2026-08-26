# Letterboxd

**What it is:** A social film-cataloguing/reviewing platform (launched 2011) — think Goodreads for films. Its value here would be its own user rating/review data, which reflects a distinctly cinephile audience (skews arthouse/enthusiast rather than general-audience like IMDb or TMDB voters). Letterboxd does **not** maintain its own film metadata database — it sources that from TMDB (see `tmdb.md`), so it offers nothing new on the metadata side, only on the ratings/review side.

**Coverage:** Strong for anything with a cinephile following — arthouse, festival, classic, and cult titles are often better-represented in review depth (if not raw vote count) than on IMDb.

**Access:**
- **No public self-serve API** as of 2026. Letterboxd offers an API but access is by request only — email `api@letterboxd.com` describing your intended use, OAuth2-based, no guaranteed approval or timeline.
- **Unofficial scrapers exist** (e.g. third-party tools on Apify and elsewhere) but scraping Letterboxd violates its Terms of Service — a real licensing/ToS risk, not a viable long-term plan for anything beyond one-off personal curiosity.
- **CSV export** — individual users can export their own list/diary data from their own account, but that's personal-list export, not a route to the platform's aggregate ratings.

**Licensing:** Unclear/restrictive for the ratings data specifically, precisely because there's no open API — everything beyond personal export goes through their gated request process or carries ToS risk.

**Relevance to non-English filtering:** Because Letterboxd's audience skews toward serious/arthouse viewers, its rating and "popularity" signals could in principle be a better proxy for "major foreign film for a western audience" than TMDB's raw vote_count (see the gap noted in `data.md`) — but that's blocked on the same API-access problem above.

**Status here:** Not integrated. Worth revisiting if/when API access is granted, or if a legitimate bulk data-sharing arrangement becomes available.

**Links:** https://letterboxd.com/about/film-data/ (their own note confirming TMDB as their metadata source)
