#!/usr/bin/env python
"""Build _data/toc.yml by inspecting content directory."""

from pathlib import Path

import yaml

def parse_path(path):
    return str(path).replace('content/', '')

contents = [{'url': 'welcome'}]

root = Path(__file__).parents[1] / 'content' / 'chapters'

for cpath in sorted([p for p in root.iterdir() if p.is_dir()]):
    sections = [p for p in sorted(list(cpath.iterdir()))
                if p.suffix == '.md' and '00' not in str(p)]
    chapter = {
        "url": parse_path(cpath / '00_overview'),
        "expand_sections": True,
        "sections": [{"url": parse_path(s.with_suffix(''))} for s in sections]
    }
    contents.append(chapter )

with open(Path(__file__).parents[1] / '_data' / 'toc.yml', 'w') as file_:
    yaml.dump(contents, file_)
