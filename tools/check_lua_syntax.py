import os, re

files = [
    'plugins/rs-translator/main.lua',
    'plugins/rs-translator/src/dialogue_hook.lua',
    'plugins/rs-translator/src/dialogue_loader.lua',
    'plugins/rs-translator/src/translator.lua',
    'plugins/rs-translator/src/dictionary.lua',
    'plugins/rs-translator/src/quest_highlighter.lua',
    'plugins/rs-translator/src/quest_helper_hook.lua',
    'plugins/rs-translator/src/minimenu_hook.lua',
    'plugins/rs-translator/src/entity_guard.lua',
    'plugins/rs-translator/src/ui.lua',
    'plugins/rs-translator/src/data/quest_dialogue_steps.lua',
]

for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"Checking {fp} ({len(content)} chars)...")
    # Check open/close braces
    open_c = content.count('{')
    close_c = content.count('}')
    if open_c != close_c:
        print(f"  WARNING: Brace mismatch in {fp}: {open_c} vs {close_c}")
    # Check open/close parens
    open_p = content.count('(')
    close_p = content.count(')')
    if open_p != close_p:
        print(f"  WARNING: Paren mismatch in {fp}: {open_p} vs {close_p}")

print("Check finished.")
