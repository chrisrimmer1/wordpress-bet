#!/bin/zsh
# Monthly refresh: pull the latest HTTP Archive figures, commit if they changed, redeploy.
# Runs on the Mac mini (launchd com.chrisrimmer.wordpress-bet-refresh); needs the login keychain
# for netlify and the ssh-agent for git, so it is not for headless SSH.
set -euo pipefail
export PATH=/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin
cd "$(dirname "$0")/.."
git pull -q --ff-only || true
if python3 scripts/snapshot.py; then
  git add data/snapshot.json
  git commit -q -m "data: HTTP Archive snapshot $(date '+%Y-%m-%d')"
  git push -q
  netlify deploy --dir=. --site="${NETLIFY_SITE_ID:?}" --prod --message "snapshot $(date '+%Y-%m-%d')" >/dev/null
  echo "$(date '+%F %T') deployed"
else
  echo "$(date '+%F %T') no new month"
fi
