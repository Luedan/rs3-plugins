import re

def norm_tokens(s):
    s = s.lower()
    s = re.sub(r'[\.\,\!\?\;\:\'\"…\-\–\—]', ' ', s)
    tokens = s.split()
    stemmed = []
    for t in tokens:
        if len(t) > 4 and t.endswith('es'):
            stemmed.append(t[:-2])
        elif len(t) > 4 and t.endswith('s'):
            stemmed.append(t[:-1])
        else:
            stemmed.append(t)
    return ' '.join(stemmed)

game_text = "Great! I buy and sell pickaxes and hatchets. There are plenty to choose from, and I've some free samples too. Take your pick...or hatchet."
wiki_key = "Great! I buy and sell pickaxes and hatchet. There are plenty to choose from, and I've some free samples too. Take your pick...or hatchet."

print("Game norm: ", norm_tokens(game_text))
print("Wiki norm: ", norm_tokens(wiki_key))
print("Exact Match? ", norm_tokens(game_text) == norm_tokens(wiki_key))
