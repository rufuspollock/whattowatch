---
name: watch-tonight
description: Use when the user asks what to watch tonight, wants a film/series pick, or says they just watched/finished something. Two modes — pick a film via context questions + pairwise comparison, or log a rating/notes after watching. Reads and writes ratings.md and notes/ in this project.
---

# Watch Tonight

Picks a film for tonight from taste + context, or logs a rating after watching. No external DB yet — reasons over this project's own files plus the model's film knowledge.

## Files this skill uses

- `ratings.md` — watch log (Title/Year/Type/Rating/Watched/Notes table) + "Picked / to watch" list. Read for seen-list + taste signal. Write new rows/entries here.
- `notes/*.md` — verbatim taste-discussion logs (e.g. `notes/2026-08-04-kieslowski-filmmakers.md`: Tarkovsky = peer of Kieślowski, prioritize; Haneke = too dark, reject; Villeneuve = elegant but lacks humanism, deprioritize). Read all of these for taste signal before picking.
- `data.md` — status of external data sources (TMDB etc.). Context only, not queried live in v0.

Mode is decided from how the user opens the conversation — don't ask which mode, infer it. "what should I watch" / "pick me something" → Pick mode. "I watched X" / "just finished Y" / "we saw Z last night" → Log mode.

## Pick mode

1. Read `ratings.md` and every file in `notes/` before asking anything. Build:
   - Seen-list (title + watched-date if present)
   - Taste snapshot: liked/disliked filmmakers, genres, patterns from ratings and notes commentary
2. Ask context questions **one at a time**, multiple-choice where sensible, skip any the user has already answered unprompted:
   - Mood/genre pull tonight, or "surprise me"
   - Energy: demanding/arthouse vs light/easy
   - Alone or with company (affects tone, subtitles, darkness tolerance)
   - Time available (length ceiling)
3. Generate a shortlist of ~5-6 candidates from your own film knowledge:
   - Drop anything on the seen-list watched within the last ~2 years, unless the user asked for a rewatch — otherwise a prior watch is fine to resurface, just flag it as a rewatch option, not a default pick
   - Weight toward taste signal — e.g. peer-of-Kieślowski calibre for arthouse asks, exclude Haneke-style bleakness unless explicitly asked for
4. Run pairwise comparisons ("A or B?") narrowing the shortlist to one pick, 2-3 rounds.
5. Confirm the pick with the user, then append it to `ratings.md` under "## Picked / to watch" with today's date and a short context tag (mood/energy/company), e.g.:
   `- Title (Year, type) — picked YYYY-MM-DD, [context tags], unseen/rewatch.`
6. If new taste info surfaced in the conversation that isn't just about tonight's pick (a strong like/dislike, a filmmaker comparison, a rule like "never rate Haneke") — offer to log it as a new verbatim note in `notes/YYYY-MM-DD-<topic>.md`, following the structure of the existing Kieślowski note (question, assistant answer summary, user commentary tidied, user commentary raw verbatim, takeaways for future picks). Only write it if the user confirms.

## Log mode

1. Ask for whatever's missing: rating (out of 10, ranges like "7–7.5" are fine), watched date (default: today), and any notes worth keeping.
2. Update `ratings.md`:
   - If the title is already a row (e.g. was in "Picked / to watch"), fill in Rating + Watched date, move/remove it from the "Picked / to watch" list.
   - Otherwise add a new row to the table.
3. If the user gives substantive taste commentary (not just a number), offer to capture it verbatim as a new note in `notes/`, same as step 6 above. Only write it if confirmed.

## Principles

- Never invent a rating or watched-date — always ask.
- Keep taste commentary verbatim when logged as notes; don't paraphrase away nuance (see existing notes for the raw-vs-tidied pattern).
- v0 has no external ratings data (Rotten Tomatoes etc.) or full film DB — candidates come from the model's own knowledge. `data.md` tracks the plan to swap in a real dataset; this skill doesn't need to change shape when that happens, just where the candidate list comes from.
