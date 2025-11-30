from nltk.corpus import wordnet as wn
import random

# Get lemmas
words = [word for word in list(wn.all_lemma_names())
    if word.isalpha() and word[0].islower() and len(word) >= 3
]

def getWordRandom(n = 1):
    lemmas = random.sample(words, n)
    i = 0
    ret = list()
    for lemma in lemmas:
        word = lemma.replace("_", " ")
        synsets = wn.synsets(lemma)
        if not synsets:
            continue
        defi = [{
            "pos": synset.pos(),
            "content": synset.definition(), 
            "examples": synset.examples(),
            "syn": [l.name() for l in synset.lemmas()]
        } for synset in synsets if synset is not None]
        i += 1
        ret.append(
            {"name": word, "defs": defi}
        )
        if i >= n:
            break
    return ret
