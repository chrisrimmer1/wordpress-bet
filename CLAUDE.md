# wordpress-bet

First thing every session: read `PROJECT_MEMORY.md` in full. Don't act until you have. The dated
back-story is in `docs/HISTORY.md` (immutable, newest-first): consult, don't bulk-read.

Lockstep: a state change updates `PROJECT_MEMORY.md` in the same action; a dated event is prepended
to `docs/HISTORY.md` in the same action.

## Conventions
- One static page, no build step. The bet's terms live in the `BET` object at the top of the script in
  `index.html`; change them there and redeploy. Never restate the terms elsewhere in the repo.
- Data: `scripts/snapshot.py` (stdlib only) refreshes `data/snapshot.json`. The page fetches live first,
  snapshot second. The snapshot is the record even if the API changes.
- Deploy: `netlify deploy --dir=. --site=e9491dc7-ca73-4455-893c-6268f004c683 --prod`. Never link this
  directory to a site (no `.netlify/state.json`).
- The monthly job (`scripts/refresh.sh`, launchd `com.chrisrimmer.wordpress-bet-refresh`, Mac mini) needs
  the login keychain, so run it on the Mini itself, never through headless SSH.
- Commit and push after every verified change; a redeploy is fine.
