#!/usr/bin/env python3
import argparse
import sys
import lxml.html
import requests

parser = argparse.ArgumentParser(description="Scrape wikisource")
parser.add_argument('url', default='')
parser.add_argument('--vname', default='')
parser.add_argument('--vid', default=1)
args = parser.parse_args()

text = requests.get(args.url).text
doc = lxml.html.document_fromstring(text)
iterator = list(doc.cssselect("#toc ~ p"))

print(f''':{args.vid} a sch:Volume ;
sch:name "{args.vname}" ;
sch:paragraphs ( {" ".join([f":{args.vid}-{i}" for i in range(len(iterator))])} ) .\n''')

for i, p in enumerate(iterator):
    print(f':{args.vid}-{i} a sch:Paragraph ; sch:content "{p.text_content().strip()}" .')
