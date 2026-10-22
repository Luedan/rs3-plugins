import re

def translate_sentence_by_sentence(text, dict_exact, patterns):
    # Try whole text first
    if text in dict_exact:
        return dict_exact[text]
    for pat, rep in patterns:
        if re.search(pat, text):
            return re.sub(pat, rep, text)
            
    # Try splitting into sentences
    # Match sentences ending in . ! ?
    sentences = re.split(r'([.!?]+\s+)', text)
    if len(sentences) <= 1:
        return text
        
    translated_parts = []
    any_translated = False
    
    for part in sentences:
        if not part.strip():
            translated_parts.append(part)
            continue
        # Is it a delimiter like ". "?
        if re.match(r'^[.!?]+\s+$', part):
            translated_parts.append(part)
            continue
            
        clean_part = part.strip()
        trans = dict_exact.get(clean_part)
        if not trans:
            for pat, rep in patterns:
                if re.search(pat, clean_part):
                    trans = re.sub(pat, rep, clean_part)
                    break
        if trans and trans != clean_part:
            translated_parts.append(trans)
            any_translated = True
        else:
            translated_parts.append(part)
            
    if any_translated:
        return ''.join(translated_parts)
    return text

test_dict = {
    "Offering bones or ashes at an altar will give an extra 50% XP compared to burying them.": "Ofrecer huesos o cenizas en un altar otorgará un 50% de XP adicional en comparación con enterrarlos.",
    "You pray at the altar.": "Rezas en el altar."
}

test_patterns = [
    (r"^Offering (.*) at an altar will give an extra (.*)% XP compared to (.*)\.$", r"Ofrecer \1 en un altar otorgará un \2% de XP adicional en comparación con \3.")
]

t1 = "Offering bones or ashes at an altar will give an extra 50% XP compared to burying them."
print("Single sentence:", translate_sentence_by_sentence(t1, test_dict, test_patterns))

t2 = "You pray at the altar. Offering bones or ashes at an altar will give an extra 50% XP compared to burying them."
print("Combined sentences:", translate_sentence_by_sentence(t2, test_dict, test_patterns))
