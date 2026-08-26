# Wikidata / Wikipedia

**What it is:** Wikidata is Wikipedia's structured-data sibling project — a free, collaboratively-edited knowledge graph. Films have entries with structured properties (director, cast, genre, release date, country, external IDs linking to IMDb/TMDB/etc.) queryable via SPARQL. Wikipedia itself has film plot summaries and, for well-known films, sometimes lists critical reception/awards in prose.

**Coverage:** Notability-gated — a film needs to clear Wikipedia's notability bar to have an entry at all, so this skews toward films that already have some critical/cultural footprint, which could actually help with the "major foreign film" curation problem (see `../../data.md`) since notability itself is a rough proxy for "this mattered enough to write about," independent of raw popularity/vote counts.

**Access:**
- **Wikidata Query Service** (SPARQL endpoint) — fully open, no key required, can query arbitrarily structured questions like "films with country of origin France, release date in range X, that link to a TMDB ID."
- **Full dumps** — Wikidata and Wikipedia both publish complete database dumps for offline processing.
- **No ratings data** — Wikidata/Wikipedia isn't a ratings source; it's a metadata/identifier source. Any rating info embedded in Wikipedia prose is unstructured and unreliable to parse.

**Licensing:** Wikidata is CC0 (public domain equivalent) — no restrictions at all, the most permissive source in this list. Wikipedia text is CC BY-SA (attribution + share-alike).

**Status here:** Not yet evaluated in practice (no queries run against it yet). Flagged as the most promising lead for the non-English/"major foreign film" curation gap, since it could give us a structured, permissively-licensed signal of notability/awards that TMDB's vote_count doesn't provide — e.g. querying for films tagged as Oscar Best International Feature submissions, which was the original manual-curation idea before we substituted the vote_count heuristic.

**Links:** https://www.wikidata.org · Query service: https://query.wikidata.org
