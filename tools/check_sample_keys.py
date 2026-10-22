import re, glob

# Let's see what happens if we normalize <br> and newlines
sample_keys = [
    "That's lucky, I need someone to do a quest for me.",
    "Sadly you are not eligible for the five-year veteran cape.",
    "I'm looking for a quest!",
    "Who's Saradomin?",
    "Nice place you've got here.",
    "Have you been here as long as me?",
]

with open('plugins/rs-translator/src/data/dialogues_H.lua', 'r', encoding='utf-8') as f:
    h_c = f.read()

with open('plugins/rs-translator/src/data/dialogues_F.lua', 'r', encoding='utf-8') as f:
    f_c = f.read()

for k in sample_keys:
    in_h = f'["{k}"]' in h_c
    in_f = f'["{k}"]' in f_c
    print(f"'{k}': H={in_h}, F={in_f}")
