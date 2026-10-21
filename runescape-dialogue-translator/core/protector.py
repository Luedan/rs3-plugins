import re
from .dictionaries import (
    MULTI_ENTITIES,
    SINGLE_RS_SPECIFIC,
    RS_CAPITALIZED_SKILLS,
    SINGLE_PROPER_NAMES
)

def standardize_and_clean_line(line):
    # Convert dialogue menu/choice/condition/action templates to standard markdown
    line = re.sub(r'\{\{tselect\|([^}]+)\}\}', r'[Menu]: \1', line)
    line = re.sub(r'\{\{topt\|cond=([^|]+)\|([^}]+)\}\}', r'[Choice]: cond=\1|\2', line)
    line = re.sub(r'\{\{topt\|([^}]+)\}\}', r'[Choice]: \1', line)
    line = re.sub(r'\{\{tcond\|([^}]+)\}\}', r'(Condition: \1)', line)
    def clean_tact(m):
        arg = m.group(1).strip()
        if arg in {'continue', 'initial', 'end', 'previous'}:
            return f"({arg})"
        if arg.startswith('removes=') or arg.startswith('receives='):
            return f"({arg})"
        return f"(Action: {arg})"
    line = re.sub(r'\{\{tact\|([^}]+)\}\}', clean_tact, line)
    line = re.sub(r'\{\{Qact\|([^}]+)\}\}', r'(Action: \1)', line)
    line = re.sub(r'\{\{qact\|([^}]+)\}\}', r'(Action: \1)', line)
    line = re.sub(r'\{\{Pop-up\|([^}]+)\}\}', r'(Pop-up: \1)', line)
    line = re.sub(r'\{\{(?:incomplete|cleanup|wip|ToC|DEFAULTSORT:[^}]+)\}\}', '', line)
    return line

def mask_entities(text):
    placeholders = {}
    masked = text

    # =========================================================================
    # 0. STRICT CODE, WIKI TEMPLATES, AUDIO, COMMANDS & FILENAMES PROTECTION
    # =========================================================================

    # 0a. Protect all {{Audio button|...}} completely (never touch audio filename or template)
    for m in re.findall(r'\{\{Audio button\|[^\}]+\}\}', masked, re.IGNORECASE):
        tok = f"ZZCMD{len(placeholders)}ZZ"
        placeholders[tok] = m
        masked = masked.replace(m, tok, 1)

    # 0b. Protect any #var / #vardefineecho / parser functions: {{#...}}
    for m in re.findall(r'\{\{#[^\}]+\}\}', masked):
        tok = f"ZZCMD{len(placeholders)}ZZ"
        placeholders[tok] = m
        masked = masked.replace(m, tok, 1)

    # 0c. Protect hex colour prefix: {{Colour|#99FF99|
    for m in re.findall(r'\{\{Colou?r\|#[0-9a-fA-F]{3,6}\|', masked, re.IGNORECASE):
        tok = f"ZZCMD{len(placeholders)}ZZ"
        placeholders[tok] = m
        masked = masked.replace(m, tok, 1)

    # 0d. Protect ALL remaining {{...}} completely (wiki syntax, variables, tags)
    for m in re.findall(r'\{\{[^}]+\}\}', masked):
        if not any(m.startswith(x) for x in ['{{tselect', '{{topt', '{{tcond', '{{tact']):
            tok = f"ZZCMD{len(placeholders)}ZZ"
            placeholders[tok] = m
            masked = masked.replace(m, tok, 1)

    # 0e. Protect audio/image filenames: e.g. name.ogg, name.png, etc.
    for f in re.findall(r'\b[A-Za-z0-9_\'-]+\.(?:ogg|png|jpg|gif|wav|mp3)\b', masked, re.IGNORECASE):
        tok = f"ZZCMD{len(placeholders)}ZZ"
        placeholders[tok] = f
        masked = masked.replace(f, tok, 1)

    # 0f. Protect client script action tokens: (removes=...), (receives=...), (opens=...), etc.
    for tok_match in re.findall(r'\((?:removes|receives|opens|gives|takes|teleports|requires|below\||above\|)[^)]*\)', masked):
        tok = f"ZZTOK{len(placeholders)}ZZ"
        placeholders[tok] = tok_match
        masked = masked.replace(tok_match, tok, 1)

    # 0g. Protect HTML tags: <br>, <span>, etc.
    for html in re.findall(r'<[^>]+>', masked):
        tok = f"ZZHTML{len(placeholders)}ZZ"
        placeholders[tok] = html
        masked = masked.replace(html, tok, 1)

    # =========================================================================
    # 1. BRACKETS & PLAYER PROTECTION
    # =========================================================================
    bracket_matches = re.findall(r'\[[^\]]+\]', masked)
    for bm in bracket_matches:
        if any(marker in bm for marker in ['Menu', 'Choice', 'Transcript', 'http']):
            continue
        tok = f"ZZBRA{len(placeholders)}ZZ"
        val = bm
        if val.lower() == '[number]':
            val = '[número]'
        placeholders[tok] = val
        masked = masked.replace(bm, tok, 1)

    masked = re.sub(r'\bthe player\b', 'ZZPLY0ZZ', masked, flags=re.IGNORECASE)
    placeholders['ZZPLY0ZZ'] = 'el player'
    masked = re.sub(r'\bPlayer\b', 'ZZPLY1ZZ', masked)
    placeholders['ZZPLY1ZZ'] = 'Player'

    # =========================================================================
    # 2. RSLORE / GAME ENTITIES PROTECTION
    # =========================================================================
    for ent in MULTI_ENTITIES:
        pattern = re.compile(rf'\b{re.escape(ent)}\b', re.IGNORECASE)
        if pattern.search(masked):
            def repl(m):
                tok = f"ZZENT{len(placeholders)}ZZ"
                placeholders[tok] = m.group(0)
                return tok
            masked = pattern.sub(repl, masked)

    for term in SINGLE_RS_SPECIFIC:
        pattern = re.compile(rf'\b{re.escape(term)}\b', re.IGNORECASE)
        if pattern.search(masked):
            def repl(m):
                tok = f"ZZENT{len(placeholders)}ZZ"
                placeholders[tok] = m.group(0)
                return tok
            masked = pattern.sub(repl, masked)

    for skill in RS_CAPITALIZED_SKILLS:
        pattern = re.compile(rf'\b{re.escape(skill)}\b')
        if pattern.search(masked):
            def repl(m):
                tok = f"ZZENT{len(placeholders)}ZZ"
                placeholders[tok] = m.group(0)
                return tok
            masked = pattern.sub(repl, masked)

    for name in SINGLE_PROPER_NAMES:
        pattern = re.compile(rf'\b{re.escape(name)}\b')
        if pattern.search(masked):
            def repl(m):
                tok = f"ZZENT{len(placeholders)}ZZ"
                placeholders[tok] = m.group(0)
                return tok
            masked = pattern.sub(repl, masked)

    return masked, placeholders

def unmask_entities(trans, placeholders):
    for tok, orig in placeholders.items():
        trans = re.sub(re.escape(tok), orig, trans, flags=re.IGNORECASE)
        num_match = re.search(r'\d+', tok)
        if num_match:
            num = num_match.group(0)
            prefix = tok[2:5]
            loose = rf'ZZ\s*{prefix}\s*{num}\s*ZZ'
            trans = re.sub(loose, orig, trans, flags=re.IGNORECASE)
    return trans
