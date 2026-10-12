"""Rebuild CATALOG.md and STATUS.md from catalog.json and the course folders.

Usage (from the repository root, Python 3.9+, standard library only):
    python tools/build_indexes.py
"""
import io
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load():
    with io.open(os.path.join(ROOT, 'catalog.json'), encoding='utf-8') as fh:
        return json.load(fh)


def exists(rel):
    return os.path.exists(os.path.join(ROOT, rel))


def chapters(rel):
    d = os.path.join(ROOT, rel, 'chapters')
    return len([f for f in os.listdir(d) if f.endswith('.md')]) if os.path.isdir(d) else 0


def link(c):
    return f"[{c['code']}]({c['path']}/README.md)" if exists(c['path'] + '/README.md') else c['code']


def row(c):
    pre = ', '.join(c['prerequisites']) or 'none'
    if c.get('corequisites'):
        pre += ' (with ' + ', '.join(c['corequisites']) + ' alongside)'
    return f"| {link(c)} | {c['title']} | {c['year']} · {c['semester']} | {c['credits']} | {pre} |"


HEAD = '| Code | Course | Year · Semester | Credits | Prerequisites |\n|---|---|---|---|---|'


def build_catalog(cat):
    by = {}
    for c in cat['courses']:
        by.setdefault(c['major'], []).append(c)
    out = ['# Course catalog', '',
           f"{len(cat['courses'])} courses: the common core (Years 1–2), {len(cat['majors'])} majors (Years 3–5), "
           f"{len(cat['overlaps'])} overlap specializations, and the shared upper-year courses. "
           'Generated from `catalog.json` by `tools/build_indexes.py`.', '']
    core = by.get(None, [])
    sections = [('Year 1 · Foundations (every major)', [c for c in core if c['year'] == 1]),
                ('Year 2 · Core computer science (every major)', [c for c in core if c['year'] == 2]),
                ('Shared courses in Years 3–5 (every major)', [c for c in core if c['year'] >= 3])]
    for title, rows in sections:
        out += [f'## {title}', '', HEAD] + [row(c) for c in rows] + ['']
    out += ['## Majors', '']
    for m in cat['majors']:
        rows = by.get(m['code'], [])
        readme = m['path'] + '/README.md'
        name = f"[{m['name']}]({readme})" if exists(readme) else m['name']
        out += [f"### {name} ({m['code']})", '', f"Entry requirements: {', '.join(m['entry_requirements'])}", '', HEAD]
        out += [row(c) for c in rows] + ['']
    out += ['## Overlap specializations', '']
    for o in cat['overlaps']:
        readme = o['path'] + '/README.md'
        name = f"[{o['name']}]({readme})" if exists(readme) else o['name']
        out += [f"### {name} ({o['code']})", '', f"Built on: {', '.join(o['composed_of'])}", '', HEAD]
        out += [row(c) for c in by.get(o['code'], [])] + ['']
    return '\n'.join(out)


def build_status(cat):
    total = len(cat['courses'])
    syl = sum(exists(c['path'] + '/README.md') for c in cat['courses'])
    prj = sum(exists(c['path'] + '/projects.md') for c in cat['courses'])
    chp = sum(chapters(c['path']) > 0 for c in cat['courses'])
    out = ['# Build status', '',
           'What is written so far. Syllabus = the course README; Projects = labs and projects; '
           'Chapters = full lesson notes.', '',
           f'- Syllabi: **{syl} / {total}**', f'- Labs and projects: **{prj} / {total}**',
           f'- Courses with full chapter notes: **{chp} / {total}**', '',
           '| Code | Course | Syllabus | Projects | Chapters |', '|---|---|---|---|---|']
    for c in cat['courses']:
        out.append(f"| {link(c)} | {c['title']} | {'✓' if exists(c['path'] + '/README.md') else '·'} | "
                   f"{'✓' if exists(c['path'] + '/projects.md') else '·'} | {chapters(c['path']) or '·'} |")
    return '\n'.join(out) + '\n'


def main():
    cat = load()
    for name, text in (('CATALOG.md', build_catalog(cat)), ('STATUS.md', build_status(cat))):
        with io.open(os.path.join(ROOT, name), 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(text if text.endswith('\n') else text + '\n')
    print('CATALOG.md and STATUS.md rebuilt')


if __name__ == '__main__':
    main()
