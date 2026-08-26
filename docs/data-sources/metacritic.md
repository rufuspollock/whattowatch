# Metacritic

**What it is:** Similar idea to Rotten Tomatoes — aggregates critic reviews — but produces a weighted average score out of 100 (the "Metascore") rather than a binary positive/negative percentage, which in principle captures more nuance (a score of 55 reads very differently from RT's binary-derived 55%).

**Coverage:** Overlaps heavily with Rotten Tomatoes' critical coverage (same pool of professional critics, different aggregation method); similarly weaker for small/streaming-only releases.

**Access:**
- **No free/open API.** Access is via **Fabric Origin's developer portal** (Metacritic's parent company's data platform), and requires a **paid subscription tier** — Metacritic data is explicitly excluded from Fabric's free trial tier. No self-serve free option was found.
- **Via OMDb** (see `omdb.md`) — same story as Rotten Tomatoes: OMDb surfaces the Metascore as one field in its aggregated response, for free at low volume, unofficial/unaffiliated with Metacritic.
- **Scraping** — same ToS caveat as Rotten Tomatoes; not recommended.

**Licensing:** Closed at the direct-access level for a personal project (paid-only, no published self-serve pricing found). Only the OMDb-proxied score is realistically available.

**How we'd use it:** Metascore via OMDb (`Ratings` array, `Source: "Metacritic"`, also duplicated as the top-level `Metascore` field), joined against our TMDB film set by `imdb_id`. See `omdb.md` and `data/ratings_omdb.jsonl`.

**Links:** https://www.metacritic.com
