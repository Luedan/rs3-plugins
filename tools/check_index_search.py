import json

with open('runescape-dialogue-translator/data/npc_dialogue_index.json', 'r', encoding='utf-8') as f:
    index = json.load(f)

for target in ['sage', 'donnie', 'gee', 'jacquelyn']:
    found = []
    for letter, items in index.items():
        for item in items:
            name = item.get('name', '') if isinstance(item, dict) else str(item)
            if target in name.lower():
                found.append(f"{letter}: {name}")
    print(f"Target '{target}': {found}")
