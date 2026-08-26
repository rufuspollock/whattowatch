#!/usr/bin/env python3
"""Fetch OMDb ratings (IMDb/Rotten Tomatoes/Metacritic) for films in data/films.jsonl.

Writes to a separate file (data/ratings_omdb.jsonl), keyed by imdb_id — join
with films.jsonl happens separately, not here. See data.md for source notes.

Resumable: skips imdb_ids already present in ratings_omdb.jsonl, and stops
cleanly (saving progress) when OMDb's daily free-tier limit (1,000/day) is
hit — rerun the next day to pick up where it left off.
"""
import json
import pathlib
import sys
import time
import urllib.error
import urllib.request

API_BASE = "http://www.omdbapi.com/"
TOKEN_PATH = pathlib.Path.home() / ".config" / "omdb" / "apikey"
DATA_DIR = pathlib.Path(__file__).resolve().parent.parent / "data"
FILMS_PATH = DATA_DIR / "films.jsonl"
OUT_PATH = DATA_DIR / "ratings_omdb.jsonl"


class QuotaExceeded(Exception):
    pass


def load_key():
    if not TOKEN_PATH.exists():
        sys.exit(f"Missing OMDb key at {TOKEN_PATH}")
    return TOKEN_PATH.read_text().strip()


def load_existing(path):
    if not path.exists():
        return {}
    existing = {}
    with path.open() as f:
        for line in f:
            r = json.loads(line)
            existing[r["imdbID"]] = r
    return existing


def fetch_omdb(imdb_id, key, retries=5):
    url = f"{API_BASE}?i={imdb_id}&apikey={key}"
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            body = json.loads(e.read().decode())
            if e.code == 401:
                if body.get("Error") == "Request limit reached!":
                    raise QuotaExceeded
                sys.exit(f"OMDb auth failed (401): {body.get('Error')} — check ~/.config/omdb/apikey")
            if e.code == 429 or e.code >= 500:
                wait = 2 ** attempt
                print(f"  HTTP {e.code} for {imdb_id}, retrying in {wait}s...", file=sys.stderr)
                time.sleep(wait)
                continue
            raise
    print(f"  gave up on {imdb_id} after {retries} retries", file=sys.stderr)
    return None


def write_results(path, results_by_id):
    ordered = sorted(results_by_id.values(), key=lambda r: r["imdbID"])
    with path.open("w") as f:
        for r in ordered:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def main():
    if not FILMS_PATH.exists():
        sys.exit(f"Missing {FILMS_PATH} — run sync_tmdb.py first")

    key = load_key()
    imdb_ids = []
    with FILMS_PATH.open() as f:
        for line in f:
            film = json.loads(line)
            imdb_id = film.get("imdb_id")
            if imdb_id:
                imdb_ids.append(imdb_id)

    results = load_existing(OUT_PATH)
    todo = [i for i in imdb_ids if i not in results]
    print(f"{len(results)} already fetched, {len(todo)} remaining of {len(imdb_ids)} total", file=sys.stderr)

    quota_hit = False
    fetched_this_run = 0
    for i, imdb_id in enumerate(todo, 1):
        try:
            data = fetch_omdb(imdb_id, key)
        except QuotaExceeded:
            print("  OMDb daily free-tier limit (1,000/day) reached — stopping, rerun tomorrow to resume", file=sys.stderr)
            quota_hit = True
            break
        if data is None or data.get("Response") == "False":
            print(f"  skip {imdb_id}: {data.get('Error') if data else 'no response'}", file=sys.stderr)
            continue
        results[imdb_id] = data
        fetched_this_run += 1
        if i % 25 == 0 or i == len(todo):
            print(f"  {i}/{len(todo)} attempted this run", file=sys.stderr)

    write_results(OUT_PATH, results)
    print(f"Wrote {len(results)} total ratings to {OUT_PATH} ({fetched_this_run} fetched this run)", file=sys.stderr)
    if quota_hit:
        print(f"{len(imdb_ids) - len(results)} films still need ratings — rerun tomorrow", file=sys.stderr)


if __name__ == "__main__":
    main()
