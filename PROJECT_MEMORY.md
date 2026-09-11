# wordpress-bet: project memory

## What this is
A one-page site memorialising a bet between Dan Wood (MD, Nettl of Fareham) and Chris, struck on
11 September 2026: will WordPress's share of the web fall faster? Live at
https://the-wordpress-bet.netlify.app. Companion to the Bubble Bet (Karim vs Chris).

## Current state (11 September 2026)
- Page live, fetching HTTP Archive data in the browser; snapshot committed (80 months, Jan 2020 to
  Aug 2026, latest figure 31.56%).
- Terms agreed by both on 11 September 2026: baseline the August 2026 crawl (31.56%); Dan wins if the
  August 2027 figure has fallen under 1 point, draw between 1 and 2, Chris over 2. Dan's first
  proposal used the April figure (33.2%); Chris re-based it to August with the same band widths and
  Dan accepted. The 12 months before the baseline fell 2.67 points, so the line is set below the
  prior year's pace; both knew that when they agreed.

## Now / next
- [ ] Monthly refresh runs on the Mini on the 20th at 09:00 (launchd
      `com.chrisrimmer.wordpress-bet-refresh`). First real run: 20 October 2026. Check its log
      (`~/Library/Logs/wordpress-bet-refresh.log`) after that date.
- [ ] Decision: read the August 2027 crawl on 11 September 2027 and update the status line.

## Files
- `index.html`: the page; terms in the `BET` object at the top of the script.
- `data/snapshot.json`: monthly series from the HTTP Archive API, the durable record.
- `scripts/snapshot.py`: refreshes the snapshot (exit 0 changed, 3 unchanged).
- `scripts/refresh.sh`: snapshot, commit, push, deploy; run by launchd.
- `automation/com.chrisrimmer.wordpress-bet-refresh.plist`: the launchd job (installed copy in
  `~/Library/LaunchAgents/` on the Mini).
- `docs/HISTORY.md`: dated events, newest first.

## Sources
- HTTP Archive Technology Report API: `https://cdn.httparchive.org/v1/adoption?technology=WordPress&geo=ALL&rank=ALL&start=latest`
  (and `technology=ALL` for the denominator). CORS open, cached 1 hour. New month lands a few weeks
  into the following month.
- W3Techs figures on the page (40.3% all sites, 58.8% known CMS, 11 September 2026) are hand-entered;
  W3Techs has no API. Update them by hand at the anniversary.
- Background on Dan and the bet: about-me, `okf/people/daniel-wood.md`.
