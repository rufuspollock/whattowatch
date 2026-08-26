# Agent Notes

Quick orientation for coding agents working in this repo.

## Project

"What to Watch" — a film picker. Learn preference via quick pairwise comparisons, then recommend. See `README.md` for the idea/plan.

## Data

Film/TV data sourced from TMDB. See `data.md` for source research and `docs/plans/` for the sync design (once written).

**TMDB API key**: lives at `~/.config/tmdb/` (outside repo, never commit it):
- `~/.config/tmdb/apikey` — v3 API key
- `~/.config/tmdb/apikeyread` — v4 read access token (bearer token, preferred for API calls — simpler auth header, no query param)

Never commit API keys, tokens, or `.env` files with secrets to this repo.

## Docs

- `README.md` — project idea and plan
- `data.md` — data source research
- `docs/plans/` — design docs for specific pieces of work (e.g. TMDB sync)
