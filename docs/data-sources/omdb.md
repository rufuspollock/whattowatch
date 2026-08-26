# OMDb API

**What it is:** A free, independent aggregator API (run by developer Brian Fritz since ~2013) that wraps IMDb data and, per-title, surfaces IMDb rating, Rotten Tomatoes score, and Metascore all in one response. **Not affiliated with IMDb** ("This site is not endorsed by or affiliated with IMDb.com" — their own disclaimer). It isn't an independent rating source itself — it's a convenience layer over the others, which is exactly why it's useful: one free API call gets you three otherwise-hard-to-reach numbers.

**Coverage:** Whatever IMDb has an entry for (i.e., essentially everything), though RT/Metacritic fields are only populated when those sites have actually scored the title — smaller/streaming-only films often come back with IMDb rating only.

**Access:**
- **REST API** (`omdbapi.com`), query by IMDb ID (`?i=tt...`) or title (`?t=...`). Response includes a `Ratings` array with `Source`/`Value` pairs (Internet Movie Database, Rotten Tomatoes, Metacritic where available) plus top-level `imdbRating`, `imdbVotes`, `Metascore` fields.
- **Signup**: free, self-serve, email-only (no password/account) at `omdbapi.com/apikey.aspx` — pick "FREE" tier, enter email/name/use description, they email a key + an activation link you must click to enable it.
- **Free tier: 1,000 requests/day.** Hit this limit mid-sync on our ~1,024-film dataset — the API returns **HTTP 401** with body `{"Error":"Request limit reached!"}`, same status code as an actually-invalid key, so code needs to check the error message, not just the status, to tell "wait until tomorrow" apart from "your key is broken."
- **Paid tiers** via Patreon pledge ($1/mo+), flat pledge-based pricing (not metered), raises the daily cap substantially (100k+/day at higher tiers) and unlocks a poster-image API.

**Licensing:** Content is IMDb-derived and licensed CC BY-NC 4.0 by OMDb — non-commercial use, attribution required.

**How we use it here:** `scripts/sync_omdb.py` reads `imdb_id` from each film in `data/films.jsonl` (already present from the TMDB sync) and writes one OMDb response per line to `data/ratings_omdb.jsonl`, keyed by `imdbID`. Script is resumable across the daily quota boundary — it skips IDs already fetched and stops cleanly (rather than crashing) when the limit is hit.

**Links:** https://www.omdbapi.com
