# 2026-08-26 — watch-tonight skill v0 session feedback

First live run of the `watch-tonight` skill (pick mode). Ran through it end to end per user's request — collect feedback as we go, revise skill after. Feedback quoted as close to verbatim as possible.

## On option descriptions

> "i need a short desrcription of films e.g. Paddington 2 (2018) doesn't tell me much when i'm choosing."

Fix: pairwise/shortlist options must carry a real plot/tone blurb (what happens, tone, runtime), not vibe-adjectives like "warm, shareable."

## On steering / interaction shape

> "other than yes / no answers on otpions i don't have much way to steer Other than to interrupt the flow like I'm doing now and give comments, I'm also here giving meta comments about the overall skill approach."

Fix: the flow should expect and welcome freeform interruptions/comments mid-round, not just A/B/C selection. Multiple-choice narrows too hard.

## On when to capture feedback vs. keep flowing

> "It might be better to go all the way through and just make notes that you're capturing somewhere to on the on this kind of version zero point one of the skill and then improve it at the end once we've completed."

Process used this session: keep going through pick mode live, capture feedback verbatim as it comes up, revise the skill once afterward. Worked fine — do this by default for early versions rather than stopping to edit the skill mid-session.

## On persistent viewer/household context

> "i think we need somewhere to have data like the first thing there should always be like a setup command where people describe their context and their family so that you can kind of tell quite early on of like are you watching on your own that was a good question are you watching as a couple are you watching as a family in that case for whom what age that's very helpful information that should be recorded somewhere permanently that can be drawn on maybe it's also even a different group like it's a group film night."

Fix: add a one-time/occasionally-updated setup step (or file, e.g. `household.md`) recording viewer context — solo / couple / family (+ ages) / group night — so the skill doesn't have to ask "who's watching" fresh, or at least can pre-fill a sensible default and only confirm.

Trigger for this: mid-session confusion where "with company" was ambiguous — turned out to include a throwaway comment about the user's 7-year-old finding Paddington 2 scary, which wasn't about tonight's viewing at all. Had to stop and clarify "adults only tonight" explicitly.

## On feedback capture itself

> "i also note that logging my feedback (as precisely verbatim as possible) is really useful"

Fix: when the user gives commentary/feedback (about films or about the skill), log it close to verbatim, not summarized — matches the existing raw-vs-tidied pattern already used in `notes/2026-08-04-kieslowski-filmmakers.md`.

## Taste signal surfaced this session

- Paddington (at least Paddington 1) — not to this user's taste, and found surprisingly scary for a 7-year-old. Off the list for both adult-solo/couple picks and assumed-safe "family" picks.
- Wes Anderson — strong yes. "he is amazing, most of his movies are amazing." The Grand Budapest Hotel rated 8.5, called "almost arthouse," rewatch-list candidate.
- Knives Out — seen, rated 7, "decent entertainment," explicitly not in the "great film" tier for this user.
- Your Name — started but didn't grab the user immediately; left open as "may come back to it," not abandoned outright.

## Follow-up for skill v0.1

- [ ] Add plot/tone blurbs to every option shown in shortlist/pairwise questions.
- [ ] Design flow to accept freeform mid-round comments as first-class input, not a detour.
- [ ] Add persistent household/viewer-context file, referenced early in pick mode instead of asked fresh each time.
- [ ] Reinforce: log user commentary verbatim by default, both taste and meta/skill feedback.
