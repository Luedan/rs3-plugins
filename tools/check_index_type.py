import json

with open('runescape-dialogue-translator/data/npc_dialogue_index.json', 'r', encoding='utf-8') as f:
    index = json.load(f)

print(f"Index type: {type(index)}, length: {len(index)}")
if isinstance(index, list):
    print("First 10 items:", index[:10])
    matches = [x for x in index if any(t in str(x).lower() for t in ['sage', 'donnie', 'gee', 'jacquelyn'])]
    print("Matches in list:", matches[:10])
elif isinstance(index, dict):
    print("Keys sample:", list(index.keys())[:10])
    matches = [k for k in index.keys() if any(t in k.lower() for t in ['sage', 'donnie', 'gee', 'jacquelyn'])]
    print("Matches in keys:", matches[:10])
