#!/bin/sh
# Runs on the cyber_Folks server from cron: fetch the latest page from GitHub and publish it.
# Copies only index.html and runs.js, and only when they changed.
REPO="$HOME/alach-running"
TARGET="$HOME/domains/pleksik.linuxpl.info/public_html/alach/running"
cd "$REPO" || exit 1
git pull -q --ff-only || { echo "$(date '+%F %T') git pull failed"; exit 1; }
for f in index.html runs.js; do
  if ! cmp -s "$f" "$TARGET/$f"; then
    cp "$f" "$TARGET/$f.tmp" && mv "$TARGET/$f.tmp" "$TARGET/$f" && echo "$(date '+%F %T') updated $f ($(git log -1 --format=%h))"
  fi
done
