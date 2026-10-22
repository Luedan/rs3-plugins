import json

with open('runescape-dialogue-translator/data/npc_dialogue_index.json', 'r', encoding='utf-8') as f:
    index = json.load(f)

for target in ['Gee', 'Donnie', 'Jacquelyn', 'Lumbridge Sage']:
    matches = [k for k in index if target.lower() in k.lower()]
    print(f"Target '{target}': {matches}")
