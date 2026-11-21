# AlachRunning

Source of https://www.alach.pl/running/ – a map of every run since 2013 and the progress toward running the Earth's circumference.

- `index.html` – the page
- `runs.js` – all run data (one run per line), updated daily
- `sat/`, `avatar.jpg` – live only on the server, not in this repository

Every push to `main` that changes `index.html` or `runs.js` is uploaded to the server by `.github/workflows/deploy.yml`.
Secrets needed (Settings → Secrets and variables → Actions): `FTP_SERVER`, `FTP_USERNAME`, `FTP_PASSWORD`, `FTP_DIR` (folder on the FTP account that holds the page, ending with `/`, e.g. `/` for an account rooted in `running`).
