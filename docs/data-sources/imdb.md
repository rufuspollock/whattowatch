# IMDb

**What it is:** The oldest and largest film/TV database on the web (started 1990 as a Usenet posting, now owned by Amazon). The de facto reference for cast/crew and the most widely recognized rating number in the industry (the "IMDb rating" is a weighted average of user votes, not a critic score).

**Coverage:** Enormous — essentially everything with a Wikipedia-level or better public record, going back to the silent era, plus contemporary festival/direct-to-streaming titles the moment they're listed.

**Access:**
- **Non-commercial datasets** (`datasets.imdbws.com`) — the practical option. Plain tab-separated `.tsv.gz` files, refreshed daily, no signup or key required. Key files: `title.basics.tsv.gz` (title/type/year/runtime/genres), `title.ratings.tsv.gz` (average rating + vote count per title), `title.crew.tsv.gz`, `name.basics.tsv.gz`, etc. This is the same rating IMDb shows on its own site.
- **No free/open REST API.** IMDb does not offer a public API for querying by title search etc. — you either use the bulk TSVs above, go through a commercial data licensing deal, or use a third-party aggregator like OMDb (see `omdb.md`) which itself is unofficial and not affiliated with IMDb.
- **Commercial licensing** exists (IMDb Pro / enterprise data licensing) but is a sales-contact process, not self-serve.

**Licensing:** The non-commercial datasets are governed by IMDb's Non-Commercial Licensing terms: free to download and use for personal/non-commercial purposes, but **no redistribution** and no commercial use without a separate paid license. Fine for this project's internal use; would block e.g. republishing an IMDb-derived dataset on datahub.io as open data.

**How we might use it:** As a free bulk cross-check/complement to OMDb's per-title ratings — join on `imdb_id` (which TMDB already gives us per film) against `title.ratings.tsv.gz` without spending any OMDb API quota. Not yet implemented.

**Links:** https://developer.imdb.com/non-commercial-datasets/
