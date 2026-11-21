# AlachRunning

Source of https://www.alach.pl/running/ – a map of every run since 2013 and the progress toward running the Earth's circumference.

- `index.html` – the page
- `runs.js` – all run data (one run per line), updated daily
- `sat/`, `avatar.jpg` – live only on the server, not in this repository

Every push to `main` that changes `index.html` or `runs.js` is uploaded to the server over FTP with TLS by `.github/workflows/deploy.yml`. (`sync.sh` is a fallback: a cron job on the server can pull from this repository instead.)
