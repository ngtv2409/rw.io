from nltk.corpus import wordnet as wn
import random

# Get synsets
noun = list(wn.all_synsets(wn.NOUN))
verb = list(wn.all_synsets(wn.VERB))
adj = list(wn.all_synsets(wn.ADJ))
adv = list(wn.all_synsets(wn.ADV))

posmap = {
    "noun": noun,
    "verb": verb,
    "adj": adj,
    "adv": adv
}

def getWordRandom(pos, n = 1):
    synsets = posmap[pos].copy()
    random.shuffle(synsets)
    i = 0
    ret = list()
    for synset in synsets:
        lemmas = synset.lemmas()
        if not lemmas:
            continue
        # use first lemma 
        word = lemmas[0].name().replace("_", " ")
        # filter words that matter
        if word.isalpha() and word[0].islower() and len(word) >= 3:
            defi = synset.definition()
            i += 1
            ret.append(
                (word, defi, pos)
            )
            if i >= n:
                break
    return ret
