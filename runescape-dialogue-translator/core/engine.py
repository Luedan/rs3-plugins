import urllib.request
import urllib.parse
import json
import time
import re
from .protector import (
    standardize_and_clean_line,
    mask_entities,
    unmask_entities
)

proxy_support = urllib.request.ProxyHandler({})
opener = urllib.request.build_opener(proxy_support)

def translate_raw(text):
    if not text or not text.strip():
        return text
    url = 'https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=en&tl=es&q=' + urllib.parse.quote(text)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    for attempt in range(3):
        try:
            resp = opener.open(req, timeout=10)
            data = json.loads(resp.read().decode('utf-8'))
            return ''.join(data) if isinstance(data, list) else str(data)
        except Exception:
            if attempt == 2:
                return text
            time.sleep(1)

def translate_batch(texts):
    if not texts:
        return []
    if len(texts) == 1:
        return [translate_raw(texts[0])]
    
    delim = " \n__SEP__\n "
    combined = delim.join(texts)
    if len(urllib.parse.quote(combined)) > 3500:
        mid = len(texts) // 2
        return translate_batch(texts[:mid]) + translate_batch(texts[mid:])
    
    url = 'https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=en&tl=es&q=' + urllib.parse.quote(combined)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    for attempt in range(3):
        try:
            resp = opener.open(req, timeout=15)
            data = json.loads(resp.read().decode('utf-8'))
            res_str = ''.join(data) if isinstance(data, list) else str(data)
            parts = res_str.split('__SEP__')
            if len(parts) == len(texts):
                return [p.strip() for p in parts]
            break
        except Exception:
            if attempt == 2:
                break
            time.sleep(1)
            
    return [translate_raw(t) for t in texts]

def translate_file_content(content):
    lines = content.split('\n')
    cleaned_lines = [standardize_and_clean_line(l) for l in lines]
    out_lines = list(cleaned_lines)
    translate_jobs = []

    for i, line in enumerate(cleaned_lines):
        raw_strip = line.strip()
        if not raw_strip:
            continue
            
        if line.startswith('# ') or line.startswith('## ') or line.startswith('### '):
            continue
        if line.startswith('- **Original Wiki Page**') or line.startswith('- **Letter**'):
            continue
            
        indent_match = re.match(r'^(\s*(?:-\s*)?)', line)
        indent = indent_match.group(1) if indent_match else ''
        content_after = line[len(indent):]
        
        # 1. Speaker line: **Speaker:** text
        sp_match = re.match(r'^(\*\*[^*]+\*\*:\s*)(.*)$', content_after)
        if sp_match:
            speaker_tag = sp_match.group(1)
            text_to_trans = sp_match.group(2).strip()
            if '**player:**' in speaker_tag.lower():
                speaker_tag = '**Player:** '
            prefix = indent + speaker_tag
            if text_to_trans:
                m_text, ph = mask_entities(text_to_trans)
                words_left = re.sub(r'ZZ[A-Z0-9]+ZZ', '', m_text)
                words_left = re.sub(r'[^a-zA-Z]', '', words_left)
                if len(words_left) >= 2:
                    translate_jobs.append((i, prefix, m_text, '', ph))
            continue
            
        # 2. Menu line
        menu_match = re.match(r'^(\[Menu\]:\s*)(.*)$', content_after)
        if menu_match:
            m_text = menu_match.group(2).strip()
            if m_text.lower() in {'select an option', 'select an option:'}:
                out_lines[i] = indent + '[Menu]: Selecciona una opción'
            elif m_text.lower() in {'choose an option:', 'choose an option'}:
                out_lines[i] = indent + '[Menu]: Elige una opción:'
            else:
                masked_m, ph = mask_entities(m_text)
                words_left = re.sub(r'ZZ[A-Z0-9]+ZZ', '', masked_m)
                words_left = re.sub(r'[^a-zA-Z]', '', words_left)
                if len(words_left) >= 2:
                    translate_jobs.append((i, indent + '[Menu]: ', masked_m, '', ph))
            continue
            
        # 3. Choice line
        choice_match = re.match(r'^(\[Choice\]:\s*)(.*)$', content_after)
        if choice_match:
            ch_content = choice_match.group(2).strip()
            if '|' in ch_content and 'cond=' in ch_content:
                cond_part, choice_text = ch_content.split('|', 1)
                m_text, ph = mask_entities(choice_text.strip())
                words_left = re.sub(r'ZZ[A-Z0-9]+ZZ', '', m_text)
                words_left = re.sub(r'[^a-zA-Z]', '', words_left)
                if len(words_left) >= 2:
                    translate_jobs.append((i, indent + f'[Choice]: {cond_part}|', m_text, '', ph))
            else:
                m_text, ph = mask_entities(ch_content)
                words_left = re.sub(r'ZZ[A-Z0-9]+ZZ', '', m_text)
                words_left = re.sub(r'[^a-zA-Z]', '', words_left)
                if len(words_left) >= 2:
                    translate_jobs.append((i, indent + '[Choice]: ', m_text, '', ph))
            continue
            
        # 4. Conditions
        if content_after.startswith('((Otherwise:))') or content_after.startswith('((otherwise:))'):
            out_lines[i] = indent + '((De lo contrario:))'
            continue
        cond_dp_match = re.match(r'^\(\((.*)\)\)$', content_after)
        if cond_dp_match:
            m_text, ph = mask_entities(cond_dp_match.group(1).strip())
            words_left = re.sub(r'ZZ[A-Z0-9]+ZZ', '', m_text)
            words_left = re.sub(r'[^a-zA-Z]', '', words_left)
            if len(words_left) >= 2:
                translate_jobs.append((i, indent + '((', m_text, '))', ph))
            continue
            
        cond_match = re.match(r'^\(Condition:\s*(.*)\)$', content_after)
        if cond_match:
            m_text, ph = mask_entities(cond_match.group(1).strip())
            words_left = re.sub(r'ZZ[A-Z0-9]+ZZ', '', m_text)
            words_left = re.sub(r'[^a-zA-Z]', '', words_left)
            if len(words_left) >= 2:
                translate_jobs.append((i, indent + '(Condition: ', m_text, ')', ph))
            continue
            
        # 5. Action
        act_match = re.match(r'^\(Action:\s*(.*)\)$', content_after)
        if act_match:
            m_text, ph = mask_entities(act_match.group(1).strip())
            words_left = re.sub(r'ZZ[A-Z0-9]+ZZ', '', m_text)
            words_left = re.sub(r'[^a-zA-Z]', '', words_left)
            if len(words_left) >= 2:
                translate_jobs.append((i, indent + '(Action: ', m_text, ')', ph))
            continue

        # 6. Bracketed narration [Le entregas las berries...]
        if content_after.startswith('[') and content_after.endswith(']'):
            inside = content_after[1:-1].strip()
            if not inside.startswith('Choice') and not inside.startswith('Menu'):
                m_text, ph = mask_entities(inside)
                words_left = re.sub(r'ZZ[A-Z0-9]+ZZ', '', m_text)
                words_left = re.sub(r'[^a-zA-Z]', '', words_left)
                if len(words_left) >= 2:
                    translate_jobs.append((i, indent + '[', m_text, ']', ph))
                continue
                
        # 7. Preserved game control tokens
        if re.match(r'^\((?:continue|initial|end|previous|opens=|removes=|receives=|below\||above\|)[^)]*\)$', content_after):
            continue
            
        if len(content_after) > 2 and not content_after.startswith('---'):
            m_text, ph = mask_entities(content_after)
            words_left = re.sub(r'ZZ[A-Z0-9]+ZZ', '', m_text)
            words_left = re.sub(r'[^a-zA-Z]', '', words_left)
            if len(words_left) >= 2:
                translate_jobs.append((i, indent, m_text, '', ph))

    # Perform batch translations
    if translate_jobs:
        texts_to_send = [job[2] for job in translate_jobs]
        translated_results = translate_batch(texts_to_send)
        
        for job, trans_text in zip(translate_jobs, translated_results):
            idx, prefix, _, suffix, ph = job
            unmasked = unmask_entities(trans_text, ph)
            out_lines[idx] = prefix + unmasked + suffix

    res_content = '\n'.join(out_lines)
    # Update language tag in header
    letter_match = re.search(r'- \*\*Letter\*\*: `([A-Za-z#])`', res_content)
    cur_letter = letter_match.group(1) if letter_match else '?'
    if '- **Language**:' not in res_content and letter_match:
        res_content = res_content.replace(
            f"- **Letter**: `{cur_letter}`",
            f"- **Letter**: `{cur_letter}`\n- **Language**: Español (Entidades, ítems y ubicaciones preservados en inglés)"
        )
    return res_content
