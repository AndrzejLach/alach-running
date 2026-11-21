# AlachRunning

Source of https://www.alach.pl/running/ – a map of every run since 2013 and the progress toward running the Earth's circumference.

- `index.html` – the page
- `runs.js` – all run data (one run per line), updated daily
- `sat/`, `avatar.jpg` – live only on the server, not in this repository

The server pulls from this repository every 10 minutes (cron on cyber_Folks runs `alach-running-sync.sh`, which does `git pull` and copies `index.html` and `runs.js` into `public_html/alach/running/`). Pushing to `main` is all it takes to publish.
