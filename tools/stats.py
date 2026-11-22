#!/usr/bin/env python3
"""Write the small summary files the home page cards read.

    python3 tools/stats.py            # both
    python3 tools/stats.py running    # running/stats.json only (daily update)
    python3 tools/stats.py astro      # astro/stats.json only (after an Astro change)

running/stats.json: total km and runs (type "Run" only, like the Running page), % of the equator, latest run.
astro/stats.json:   latest photo (target, title, date), photo and night counts.
"""
import json, re, sys, os, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EQUATOR_KM = 40075.017


def running():
    runs = []
    with open(os.path.join(ROOT, 'running', 'runs.js'), encoding='utf-8') as f:
        for line in f:
            line = line.strip().rstrip(',')
            if not line.startswith('{"id"'):
                continue
            r = json.loads(line)
            if r.get('type') == 'Run' and r.get('km'):
                runs.append(r)
    km = sum(r['km'] for r in runs)
    last = max(runs, key=lambda r: (r['d'], r['id']))
    out = {
        'km': round(km),
        'runs': len(runs),
        'pct': round(km / EQUATOR_KM * 100, 1),
        'last': {'d': last['d'], 'km': last['km'], 'place': last.get('place') or ''},
        'updated': datetime.date.today().isoformat(),
    }
    write(os.path.join(ROOT, 'running', 'stats.json'), out)


def astro():
    h = open(os.path.join(ROOT, 'astro', 'index.html'), encoding='utf-8').read()
    items = []
    for m in re.finditer(r'\{\s*"id":\s*"([^"]+)",\s*"date":\s*"(\d{4}-\d{2}-\d{2})",\s*"t":\s*"([^"]*)",\s*"target":\s*"([^"]*)"', h):
        items.append({'id': m[1], 'd': m[2], 't': m[3], 'target': m[4]})
    if not items:
        sys.exit('no gallery items found in astro/index.html')
    last = max(items, key=lambda i: (i['d'], i['id']))
    out = {
        'last': last,
        'photos': len(items),
        'nights': len({i['d'] for i in items}),
        'updated': datetime.date.today().isoformat(),
    }
    write(os.path.join(ROOT, 'astro', 'stats.json'), out)


def write(path, data):
    s = json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '\n'
    old = open(path, encoding='utf-8').read() if os.path.exists(path) else ''
    # ignore the date when deciding whether anything changed, so an unchanged summary is not re-uploaded
    strip = lambda t: re.sub(r'"updated":"[^"]*"', '', t)
    if strip(old) != strip(s):
        open(path, 'w', encoding='utf-8').write(s)
        print('wrote', os.path.relpath(path, ROOT), s.strip())
    else:
        print('unchanged', os.path.relpath(path, ROOT))


if __name__ == '__main__':
    which = sys.argv[1:] or ['running', 'astro']
    if 'running' in which:
        running()
    if 'astro' in which:
        astro()
