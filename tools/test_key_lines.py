import re

# Simulate the exact Lua lookup for Lumbridge Sage
with open('plugins/rs-translator/src/data/dialogues_L.lua', 'r', encoding='utf-8') as f:
    cL = f.read()

with open('plugins/rs-translator/src/dictionary.lua', 'r', encoding='utf-8') as f:
    cDict = f.read()

test_lines = [
    "Jacquelyn, the Slayer master in Lumbridge courtyard, can suggest monsters for you to fight.",
    "Jacquelyn, the Slayer master in Lumbridge courtyard, can suggest monsters for you to fight. Remember, you will do better if you have better armour and weapons and it's always worth carrying a bit of food to heal yourself.",
    "Offering bones or ashes at an altar will give an extra 50% XP compared to burying them.",
    "Great! I buy and sell pickaxes and hatchets. There are plenty to choose from, and I've some free samples too. Take your pick...or hatchet.",
    "Hello there, can I help you?",
    "What is this place?",
    "This is the town of Lumbridge, adventurer. The town is famous for its castle and river.",
]

print("--- Testing Lookups ---")
for t in test_lines:
    found_in_L = f'["{t}"]' in cL
    found_in_dict = f'["{t}"]' in cDict
    print(f"Line: {t[:60]}...")
    print(f"  -> In dialogues_L: {found_in_L}")
    print(f"  -> In dictionary:  {found_in_dict}")
    assert found_in_L or found_in_dict, f"Failed for {t}"
print("\nAll 7 test lines FOUND in dictionaries!")
