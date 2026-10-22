import re

def test_split_lua(text):
    # Simulated Lua pattern: text:gmatch("()([%!%?%.]+)(%s+)()")
    parts = []
    last_pos = 0
    any_translated = False
    
    dict_sim = {
        "Offering bones or ashes at an altar will give an extra 50% XP compared to burying them.": "Ofrecer huesos o cenizas en un altar otorgará un 50% de XP adicional en comparación con enterrarlos.",
        "You already have full Prayer points.": "Ya tienes todos tus Prayer points."
    }
    
    for m in re.finditer(r'([.!?]+)(\s+)', text):
        punct = m.group(1)
        sep = m.group(2)
        end_pos = m.end()
        start_punct = m.start()
        
        sentence = text[last_pos:start_punct] + punct
        trans = dict_sim.get(sentence, sentence)
        if trans != sentence:
            any_translated = True
        parts.append(trans + sep)
        last_pos = end_pos
        
    if last_pos < len(text):
        rest = text[last_pos:]
        trans = dict_sim.get(rest, rest)
        if trans != rest:
            any_translated = True
        parts.append(trans)
        
    if any_translated:
        return ''.join(parts)
    return None

t = "You already have full Prayer points. Offering bones or ashes at an altar will give an extra 50% XP compared to burying them."
print("Result:", test_split_lua(t))
