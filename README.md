# The WordPress Bet

One page that tracks a bet between Dan Wood and Chris Rimmer, struck 11 September 2026: does
WordPress's share of the web (WordPress origins as a share of all CrUX origins, mobile, from the
HTTP Archive Technology Report) fall by more than 2 points in a year (Chris), less than 1 point
(Dan), or in between (draw)?

- `index.html`: the page. Fetches the live series from `cdn.httparchive.org/v1/adoption` on load and
  falls back to `data/snapshot.json`. The terms are the `BET` object at the top of the script.
- `scripts/snapshot.py`: refreshes `data/snapshot.json` (exit 0 = changed, 3 = unchanged).
- `scripts/refresh.sh`: snapshot, commit, push, deploy to Netlify. Run monthly by launchd on the Mac mini.

Live: https://the-wordpress-bet.netlify.app
