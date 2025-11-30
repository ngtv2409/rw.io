from fetch_word import getWordRandom

# Get 30 words
words = getWordRandom(30)

import os
import datetime
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('template'))

outdir = "output"
os.mkdir("output")

timestr = datetime.datetime.now().strftime("%m - %d - %Y | %H:%M UTC")

with open(os.path.join(outdir, "index.html"), "w", encoding="utf-8") as f:
    f.write(
        env.get_template('index.html').render(
            timestr=timestr,
            words=words
        )
    )
