# alach.pl

Source of Andrzej Lach's site. One folder per page; each maps to a folder on the server.

| Folder | Live at | Server folder (under `public_html/alach`) |
|---|---|---|
| `home/` | https://www.alach.pl/ | `.` (only the files in this folder; old projects there are left alone) |
| `astro/` | https://www.alach.pl/astro/ | `astro/` |
| `running/` | https://www.alach.pl/running/ | `running/` (`sat/` and `avatar.jpg` live only on the server) |

## Publishing

Every push to `main` uploads the files that changed in that push, over FTP with TLS
(`.github/workflows/deploy.yml`). Each folder's `index.html` goes last, so a page never points at files that
are not there yet. Deleted files are not removed from the server. A commit whose message contains
`[no upload]` is not uploaded.

Secrets (Settings → Secrets and variables → Actions): `FTP_SERVER`, `FTP_USERNAME`, `FTP_PASSWORD`.

## Pages

- **running/** – every run since 2013 on a map. `runs.js` holds all run data, one run per line, and is updated daily
  from MapMyRun. The other `.js`/`.json` files are map, flag and star data.
- **astro/** – astrophotography gallery with a live sky map. Photos in `astro/img/`; originals stay on Andrzej's Mac
  (`Documents/Astrophotgraphy`).
- **home/** – the landing page linking to Astro, Running and Work.
