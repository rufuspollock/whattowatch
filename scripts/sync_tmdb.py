#!/usr/bin/env python3
"""Sync a filtered slice of TMDB movies into data/films.jsonl.

See docs/plans/2026-08-26-tmdb-sync-design.md for the design.
"""
import argparse
import datetime
import json
import pathlib
import sys
import time
import urllib.error
import urllib.request

API_BASE = "https://api.themoviedb.org/3"
TOKEN_PATH = pathlib.Path.home() / ".config" / "tmdb" / "apikeyread"
DATA_DIR = pathlib.Path(__file__).resolve().parent.parent / "data"

VOTE_COUNT_MIN = 300
RUNTIME_MIN = 40
YEARS_BACK = 5


def load_token():
    if not TOKEN_PATH.exists():
        sys.exit(f"Missing TMDB token at {TOKEN_PATH}")
    return TOKEN_PATH.read_text().strip()


def api_get(path, token, params=None, retries=5):
    query = "&".join(f"{k}={v}" for k, v in (params or {}).items())
    url = f"{API_BASE}{path}"
    if query:
        url += f"?{query}"
    req = urllib.request.Request(
        url,
        headers={"Authorization": f"Bearer {token}", "accept": "application/json"},
    )
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code == 401:
                sys.exit("TMDB auth failed (401) — check ~/.config/tmdb/apikeyread")
            if e.code == 429 or e.code >= 500:
                wait = 2 ** attempt
                print(f"  HTTP {e.code} on {path}, retrying in {wait}s...", file=sys.stderr)
                time.sleep(wait)
                continue
            raise
    sys.exit(f"Gave up on {path} after {retries} retries")


def discover_movie_ids(token, limit):
    today = datetime.date.today()
    start = today.replace(year=today.year - YEARS_BACK)
    ids = []
    page = 1
    total_pages = 1
    while page <= total_pages:
        data = api_get(
            "/discover/movie",
            token,
            {
                "include_adult": "false",
                "include_video": "false",
                "language": "en-US",
                "primary_release_date.gte": start.isoformat(),
                "primary_release_date.lte": today.isoformat(),
                "with_original_language": "en",
                "with_runtime.gte": RUNTIME_MIN,
                "vote_count.gte": VOTE_COUNT_MIN,
                "sort_by": "popularity.desc",
                "page": page,
            },
        )
        total_pages = data["total_pages"]
        ids.extend(r["id"] for r in data["results"])
        print(f"  page {page}/{total_pages}, {len(ids)} ids so far", file=sys.stderr)
        page += 1
        if limit and len(ids) >= limit:
            return ids[:limit]
    return ids


def fetch_movie_details(token, movie_id):
    return api_get(f"/movie/{movie_id}", token, {"language": "en-US"})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--limit", type=int, default=50,
        help="Max number of films to fetch (default 50, for fast iteration). Use --limit 0 for no limit (full sync).",
    )
    args = parser.parse_args()
    limit = None if args.limit == 0 else args.limit

    token = load_token()
    DATA_DIR.mkdir(exist_ok=True)

    print("Fetching genre list...", file=sys.stderr)
    genres = api_get("/genre/movie/list", token, {"language": "en-US"})
    (DATA_DIR / "genres.json").write_text(json.dumps(genres, indent=2))

    print(f"Discovering movie ids (limit={limit})...", file=sys.stderr)
    ids = discover_movie_ids(token, limit)
    print(f"Found {len(ids)} movies matching filters. Fetching details...", file=sys.stderr)

    films = []
    for i, movie_id in enumerate(ids, 1):
        details = fetch_movie_details(token, movie_id)
        if details is None:
            print(f"  skip {movie_id}: not found (404)", file=sys.stderr)
            continue
        films.append(details)
        if i % 25 == 0 or i == len(ids):
            print(f"  {i}/{len(ids)} details fetched", file=sys.stderr)

    films.sort(key=lambda f: f["id"])
    out_path = DATA_DIR / "films.jsonl"
    with out_path.open("w") as f:
        for film in films:
            f.write(json.dumps(film, ensure_ascii=False) + "\n")

    print(f"Wrote {len(films)} films to {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
