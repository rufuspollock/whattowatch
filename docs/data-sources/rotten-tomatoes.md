# Rotten Tomatoes

**What it is:** Aggregates individual critic reviews into a "Tomatometer" (% of reviews positive) plus a separate audience score. Probably the single most culturally recognizable "is this film good" signal, and the one people usually mean when they ask "what's it rated."

**Coverage:** Strong for anything with theatrical/mainstream critical coverage; weaker or absent for straight-to-streaming or very small releases that critics didn't review in volume.

**Access:**
- **No open/free API.** Official access is via Fandango's **RT Developer Network**, which requires an application and approval process (reportedly up to ~60 days), and carries a **license fee starting around $60,000/year** for full scores plus review snippets. This is enterprise/commercial-scale pricing, not remotely viable for a personal project.
- **Via OMDb** (see `omdb.md`) — the practical route. OMDb surfaces the RT Tomatometer score (not review snippets/critic quotes) as one field in its aggregated response, for free at low volume. This is unofficial/unaffiliated with RT but is how most small projects get *a* RT number at all.
- **Scraping** — technically possible, but scraping RT violates its Terms of Service. Not recommended as a real plan; noted here only because it's the "other" option people reach for.

**Licensing:** Effectively closed for a personal/hobby project at the direct-access level. Only the OMDb-proxied score is realistically available.

**How we'd use it:** Rotten Tomatoes % via OMDb (`Ratings` array, `Source: "Rotten Tomatoes"`), joined against our TMDB film set by `imdb_id`. See `omdb.md` and `data/ratings_omdb.jsonl`.

**Links:** https://www.rottentomatoes.com (RT Developer Network access is not self-serve/publicly documented with pricing; the ~$60k/yr figure and 60-day approval window are commonly reported by developers who've gone through the process, not published on an RT pricing page)
