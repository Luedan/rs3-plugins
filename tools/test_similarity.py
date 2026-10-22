def word_similarity(s1, s2):
    import re
    w1 = set(re.findall(r'\b[a-z]{3,}\b', s1.lower()))
    w2 = set(re.findall(r'\b[a-z]{3,}\b', s2.lower()))
    if not w1 or not w2:
        return 0.0
    inter = len(w1 & w2)
    union = len(w1 | w2)
    return inter / union

t1 = "Great! I buy and sell pickaxes and hatchets. There are plenty to choose from, and I've some free samples too. Take your pick...or hatchet."
t2 = "Great! I buy and sell pickaxes and hatchet. There are plenty to choose from, and I've some free samples too. Take your pick...or hatchet."

sim = word_similarity(t1, t2)
print("Word similarity:", sim)
