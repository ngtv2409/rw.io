from nltk.corpus import wordnet as wn
import random

# Get lemmas
words = [word for word in list(wn.all_lemma_names())
    if word.isalpha() and word[0].islower() and len(word) >= 3
]

posaltname = {
    wn.NOUN: "n",
    wn.VERB: "v",
    wn.ADJ: "adj",
    wn.ADJ_SAT: "adj",
    wn.ADV: "adv"
}

def getWordRandom(n = 1):
    lemmas = random.sample(words, n)
    i = 0
    ret = list()
    for lemma in lemmas:
        word = lemma.replace("_", " ")
        synsets = [s for s in wn.synsets(lemma) if s is not None]
        if not synsets:
            continue
        defs = list()
        for synset in synsets:
            defi = dict()
            defi["pos"] = posaltname[synset.pos()]
            defi["content"] = synset.definition()
            defi["examples"] = synset.examples()[0] if synset.examples() else None
            defi["syn"] = [l.name().replace("_"," ") for l in synset.lemmas()]
            defs.append(defi)

        i += 1
        ret.append(
            {"name": word, "defs": defs}
        )
        if i >= n:
            break
    return ret
