#!/usr/bin/env python3

from pathlib import Path
import rdflib

# get files to validate
path = Path(__file__).parent.parent
globs = path.glob("**/*.ttl")

# parse (and validate)
g = rdflib.Graph()
for p in globs:
    g.parse(p)
    print(f"validated: {p}")
