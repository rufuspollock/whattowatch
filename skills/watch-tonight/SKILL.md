---
name: watch-tonight
description: Use when the user asks what to watch tonight, wants a film/series pick, or says they just watched/finished something. Two modes — pick a film via context questions + pairwise comparison, or log a rating/notes after watching. Reads and writes ratings.md, household.md, and notes/ in this project.
---

# Watch Tonight

Picks a film for tonight from taste + context, or logs a rating after watching. No external DB yet — reasons over this project's own files plus the model's film knowledge.

## Files this skill uses

- `ratings.md` — watch log (Title/Year/Type/Rating/Watched/Notes table) + "Picked / to watch" list. Read for seen-list + taste signal. Write new rows/entries here.
- `household.md` — who might be watching (solo/couple/family+ages/group night) and any per-viewer constraints (e.g. content that reads as kid-safe but isn't). Read before asking who's watching tonight; update it when the session reveals something new or wrong.
- `notes/*.md` — verbatim taste-discussion and session-feedback logs (e.g. `notes/2026-08-04-kieslowski-filmmakers.md`: Tarkovsky = peer of Kieślowski, prioritize; Haneke = too dark, reject; Villeneuve = elegant but lacks humanism, deprioritize). Read all of these for taste signal before picking.
- `data.md` — status of external data sources (TMDB etc.). Context only, not queried live in v0.

Mode is decided from how the user opens the conversation — don't ask which mode, infer it. "what should I watch" / "pick me something" → Pick mode. "I watched X" / "just finished Y" / "we saw Z last night" → Log mode.

## Pick mode

1. Read `ratings.md`, `household.md`, and every file in `notes/` before asking anything. Build:
   - Seen-list (title + watched-date if present)
   - Taste snapshot: liked/disliked filmmakers, genres, patterns from ratings and notes commentary
   - Viewer context defaults from `household.md`
2. Ask context questions **one at a time**, multiple-choice where sensible, skip any the user has already answered or that's unambiguous from `household.md`:
   - Who's watching tonight, if not obvious (solo / adult company / with a specific person from `household.md`) — don't re-ask this from scratch each time, confirm the likely default instead
   - Mood/genre pull tonight, or "surprise me"
   - Energy: demanding/arthouse vs light/easy
   - Time available (length ceiling)
3. Generate a shortlist of ~5-6 candidates from your own film knowledge:
   - Drop anything on the seen-list watched within the last ~2 years, unless the user asked for a rewatch — otherwise a prior watch is fine to resurface, just flag it as a rewatch option, not a default pick
   - Weight toward taste signal — e.g. peer-of-Kieślowski calibre for arthouse asks, exclude Haneke-style bleakness unless explicitly asked for; boost filmmakers with a strong-yes signal (e.g. Wes Anderson) when tone fits
   - If a child from `household.md` is watching, don't trust "family film" marketing at face value — check known exceptions in `household.md` (e.g. Paddington 2 read as scary) and flag any real uncertainty to the user rather than assuming safe
4. Every option shown, in the shortlist or in pairwise rounds, must carry a short **plot/tone blurb** (what actually happens, tone, runtime) — never just vibe-adjectives like "warm" or "shareable" on their own.
5. Run pairwise comparisons ("A or B?") narrowing the shortlist to one pick, 2-3 rounds. Treat any free-text reply as first-class input, not a detour — if the user interrupts with a comment, a "seen it, rate X/10", a correction, or meta-feedback about the process itself, follow that instead of forcing the question back on track. Update `ratings.md`/`notes/` from it immediately, then resume picking.
6. Confirm the pick with the user, then append it to `ratings.md` under "## Picked / to watch" with today's date and a short context tag (mood/energy/company), e.g.:
   `- Title (Year, type) — picked YYYY-MM-DD, [context tags], unseen/rewatch.`
7. If new taste info or process feedback surfaced during the conversation that isn't just about tonight's pick (a strong like/dislike, a filmmaker comparison, a household-context correction, a complaint about how the skill itself is behaving) — capture it. Taste/household info can usually just be written directly (household.md edit, or a new ratings.md row) since it's low-stakes and reversible; a substantive verbatim discussion (like a filmmaker comparison) or explicit process/skill feedback should go in a new note `notes/YYYY-MM-DD-<topic>.md`, quoting the user close to verbatim rather than summarizing (see `notes/2026-08-04-kieslowski-filmmakers.md` and `notes/2026-08-26-watch-tonight-v0-feedback.md` for the pattern). Don't stop the picking flow to do this — capture and keep moving; save the "should the skill itself change" question for after the session, unless the user asks to fix it now.

## Log mode

1. Ask for whatever's missing: rating (out of 10, ranges like "7–7.5" are fine), watched date (default: today), and any notes worth keeping.
2. Update `ratings.md`:
   - If the title is already a row (e.g. was in "Picked / to watch"), fill in Rating + Watched date, move/remove it from the "Picked / to watch" list.
   - Otherwise add a new row to the table.
3. If the user gives substantive taste or household commentary (not just a number), capture it — a quick fact goes straight into `ratings.md`/`household.md`, a fuller discussion becomes a verbatim note in `notes/`, same as pick-mode step 7.

## Principles

- Never invent a rating, watched-date, or household fact — always ask or confirm.
- Keep taste and process-feedback commentary close to verbatim when logged as notes; don't paraphrase away nuance.
- Freeform interruptions mid-flow are expected, not exceptions — a multiple-choice question is a fast path, not the only path.
- v0 has no external ratings data (Rotten Tomatoes etc.) or full film DB — candidates come from the model's own knowledge. `data.md` tracks the plan to swap in a real dataset; this skill doesn't need to change shape when that happens, just where the candidate list comes from.
