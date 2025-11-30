from fetch_word import getWordRandom

# Get 10 of each types
nouns = getWordRandom("noun", 10)
verbs = getWordRandom("verb", 10)
adjs = getWordRandom("adj", 10)
advs = getWordRandom("adv", 10)
words = nouns + verbs + adjs + advs

import os
import datetime

outdir = "output"
os.mkdir("output")

html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Nightly Random Words</title>
<style>
body {{ font-family: Arial, sans-serif; padding: 2rem; }}
li {{ margin-bottom: 0.5rem; }}
.noun {{ color: #3498db; }}
.verb {{ color: #e67e22; }}
.adj  {{ color: #2ecc71; }}
.adv  {{ color: #7e2525; }}
</style>
</head>
<body>
<h1>Random Words</h1>
This page is generated automatically nightly.<br/>
The cron is requested at 17:30 UTC, can have slight delay due to high workloads.<br/>
Last update: {datetime.datetime.now().strftime("%m/%d/%y - %H:%M UTC")}.<br/>
"""

html += "<ul>"
for w,d,p in words:
    html += f'<li class="{p}"><b>{w}</b> ({p}): {d}</li>'
html += "</ul>"

html += "</body></html>"

with open(os.path.join(outdir,"index.html"), "w", encoding="utf-8") as f:
    f.write(html)

