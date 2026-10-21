import os
import json

# Paths relative to this file
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..', 'data'))
INDEX_PATH = os.path.join(DATA_DIR, 'npc_dialogue_index.json')

# Common English words that must NOT be masked as standalone entities
COMMON_WORDS_BLACKLIST = {
    'may', 'will', 'see', 'can', 'do', 'did', 'done', 'go', 'went', 'gone', 'get', 'got', 'say',
    'said', 'tell', 'told', 'know', 'knew', 'take', 'took', 'make', 'made', 'come', 'came', 'give',
    'gave', 'look', 'find', 'think', 'use', 'used', 'help', 'need', 'want', 'like', 'feel', 'try',
    'ask', 'work', 'call', 'keep', 'put', 'let', 'begin', 'start', 'show', 'hear', 'run', 'set',
    'move', 'play', 'pay', 'meet', 'bring', 'live', 'stand', 'lose', 'fall', 'talk', 'walk', 'win',
    'buy', 'sell', 'leave', 'stop', 'pass', 'hope', 'wish', 'wait', 'send', 'stay', 'cut', 'kill',
    'die', 'open', 'close', 'read', 'write', 'grow', 'draw', 'eat', 'drink', 'sing', 'fly', 'burn',
    'cook', 'fish', 'mine', 'craft', 'smith', 'fletch', 'farm', 'hunt', 'slay', 'steal', 'pray',
    'cast', 'teleport', 'equip', 'wear', 'wield', 'attack', 'defend', 'hit', 'miss', 'heal', 'cure',
    'rest', 'sleep', 'wake', 'trade', 'bank', 'drop', 'pick', 'check', 'view', 'search', 'examine',
    'inspect', 'touch', 'climb', 'jump', 'enter', 'exit', 'board', 'cross', 'pull', 'push', 'turn',
    'press', 'light', 'feed', 'lead', 'follow', 'join', 'free', 'hold', 'carry', 'bear', 'pour',
    'fill', 'empty', 'mix', 'clean', 'wash', 'rub', 'wipe', 'crush', 'grind', 'chop', 'slice',
    'carve', 'bake', 'roast', 'boil', 'brew', 'sew', 'knit', 'weave', 'spin', 'smelt', 'forge',
    'shape', 'bend', 'tool', 'item', 'items', 'object', 'thing', 'person', 'people', 'man', 'men',
    'woman', 'women', 'child', 'children', 'boy', 'girl', 'friend', 'enemy', 'guard', 'soldier',
    'officer', 'master', 'apprentice', 'student', 'teacher', 'doctor', 'nurse', 'priest', 'monk',
    'king', 'queen', 'prince', 'princess', 'lord', 'lady', 'sir', 'madam', 'brother', 'sister',
    'father', 'mother', 'son', 'daughter', 'uncle', 'aunt', 'nephew', 'niece', 'cousin', 'husband',
    'wife', 'stranger', 'fellow', 'anyone', 'someone', 'everyone', 'no one', 'nothing', 'something',
    'everything', 'day', 'night', 'morning', 'afternoon', 'evening', 'year', 'month', 'week', 'hour',
    'minute', 'second', 'time', 'times', 'way', 'place', 'room', 'house', 'home', 'shop', 'store',
    'city', 'town', 'village', 'country', 'world', 'land', 'sea', 'ocean', 'river', 'lake',
    'mountain', 'hill', 'forest', 'wood', 'tree', 'field', 'road', 'path', 'street', 'door',
    'gate', 'wall', 'floor', 'roof', 'window', 'table', 'chair', 'bed', 'box', 'chest', 'bag',
    'sack', 'pack', 'pocket', 'hand', 'foot', 'head', 'eye', 'ear', 'mouth', 'nose', 'face',
    'hair', 'body', 'heart', 'mind', 'soul', 'life', 'death', 'blood', 'bone', 'water', 'fire',
    'air', 'earth', 'wind', 'light', 'dark', 'sun', 'moon', 'star', 'sky', 'good', 'bad', 'new',
    'old', 'great', 'small', 'big', 'little', 'young', 'long', 'short', 'high', 'low', 'early',
    'late', 'hard', 'easy', 'right', 'wrong', 'true', 'false', 'first', 'last', 'next', 'other',
    'another', 'same', 'different', 'only', 'own', 'real', 'sure', 'ready', 'able', 'best',
    'better', 'worse', 'worst', 'more', 'most', 'less', 'least', 'few', 'many', 'much', 'several',
    'all', 'both', 'half', 'some', 'any', 'each', 'every', 'no', 'none', 'one', 'two', 'three',
    'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'invention', 'construction', 'prayer',
    'magic', 'defence', 'strength', 'attack', 'cooking', 'woodcutting', 'fishing', 'mining',
    'smithing', 'crafting', 'thieving', 'agility', 'herblore', 'fletching', 'slayer', 'farming',
    'hunter', 'summoning', 'dungeoneering', 'divination', 'archaeology', 'necromancy'
}

RS_LOCATIONS = [
    "Warriors' Guild", "Champions' Guild", "Heroes' Guild", "Legends' Guild", "Wizards' Tower",
    "Draynor Village", "Draynor Manor", "Tutorial Island", "Edgeville", "Al Kharid", "Burthorpe",
    "Taverley", "Lumbridge", "Varrock", "Falador", "Port Sarim", "Rimmington", "Catherby",
    "Seers' Village", "East Ardougne", "West Ardougne", "Ardougne", "Yanille", "Grand Exchange",
    "Tree Gnome Stronghold", "Gnome Stronghold", "Keldagrim", "Dorgesh-Kaan", "Mort'ton",
    "Canifis", "Morytania", "Burgh de Rott", "Meiyerditch", "Prifddinas", "Tirannwn", "Lletya",
    "Sophanem", "Pollnivneach", "Nardah", "Menaphos", "Kharidian Desert", "Zanaris", "Wilderness",
    "Karamja", "Brimhaven", "Shilo Village", "Tai Bwo Wannai", "Fremennik Province", "Rellekka",
    "Jatizso", "Neitiznot", "Miscellania", "Etceteria", "Lunar Isle", "Ape Atoll", "Entrana",
    "Daemonheim", "Kharid-et", "Everlight", "Infernal Source", "Stormguard Citadel", "Senntisten",
    "Fort Forinthry", "City of Um", "Gielinor", "Dummy Room", "Dummy room", "dummy room"
]

RS_QUESTS = [
    "Monkey Madness", "Vampyre Slayer", "Dragon Slayer", "Cook's Assistant", "Desert Treasure",
    "Temple at Senntisten", "Plague City", "Biohazard", "Underground Pass", "Regicide",
    "Roving Elves", "Mourning's End", "Within the Light", "Prifddinas", "Recipe for Disaster",
    "Eclipse of the Heart", "Heart of Stone", "Sliske's Endgame", "The Feud", "Rogue Trader"
]

RS_CAPITALIZED_SKILLS = [
    "Attack", "Strength", "Defence", "Ranged", "Prayer", "Magic", "Runecrafting", "Construction",
    "Constitution", "Hitpoints", "Agility", "Herblore", "Thieving", "Crafting", "Fletching",
    "Slayer", "Hunter", "Mining", "Smithing", "Fishing", "Cooking", "Firemaking", "Woodcutting",
    "Farming", "Summoning", "Dungeoneering", "Divination", "Invention", "Archaeology", "Necromancy"
]

RS_TERMS = [
    "Slayer Master", "Slayer Masters", "Combat Instructor", "combat instructor", "swordsman",
    "training officer", "trainer", "combat academy", "combat triangle", "action bar", "backpack",
    "lodestone", "general store", "adrenaline", "construction contract", "construction contracts",
    "contracts", "pieces of furniture", "furniture", "skill levels", "skill level",
    "skillcape", "skillcapes", "Capes of Accomplishment", "Cape of Accomplishment",
    "Skillcape of Attack", "Attack cape", "Attack hood", "Attack master cape", "master cape", "master capes",
    "inverted cape", "inverted capes", "inverted skillcape", "inverted skillcapes",
    "Quest Cape", "quest cape", "bronze dagger", "iron dagger", "steel dagger", "mithril dagger",
    "adamant dagger", "rune dagger", "dragon dagger", "dagger", "daggers", "dragon scimitar",
    "rune scimitar", "adamant scimitar", "mithril scimitar", "scimitar", "scimitars",
    "armadyl battlestaff", "armadyl battle staff", "battlestaff", "staff", "oak tree", "willow tree",
    "maple tree", "yew tree", "magic tree", "oak logs", "willow logs", "maple logs", "yew logs",
    "magic logs", "logs", "redberries", "cadava berries", "white berries", "berries", "planks",
    "steel nails", "nails", "red dye", "yellow dye", "blue dye", "dyes", "dye", "coins", "gold coins",
    "butter knife", "fremennik sea boots", "ardougne cloak", "ring of charos", "ring of charos (a)",
    "Black Knight", "Black Knights", "dummies", "piercing attack", "slashing attack", "crushing attack",
    "talking chicken", "flying fish", "Count Draynor", "vampyre", "vampyres"
]

SINGLE_RS_SPECIFIC = {
    'skillcape', 'skillcapes', 'scimitar', 'scimitars', 'battlestaff', 'lodestone',
    'redberries', 'vampyre', 'vampyres', 'planks', 'dyes', 'backpack'
}

def load_npc_names():
    npc_names = set()
    if os.path.exists(INDEX_PATH):
        with open(INDEX_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for letter, npcs in data.items():
                for item in npcs:
                    if isinstance(item, list) and len(item) > 1:
                        npc_names.add(item[1])
                    elif isinstance(item, str):
                        npc_names.add(item)
    return npc_names

NPC_NAMES = load_npc_names()

filtered_npc = set()
for n in NPC_NAMES:
    clean_n = n.strip()
    if ' ' in clean_n:
        filtered_npc.add(clean_n)
    elif clean_n.lower() not in COMMON_WORDS_BLACKLIST and len(clean_n) >= 3:
        filtered_npc.add(clean_n)

MULTI_ENTITIES = sorted(list(set(RS_LOCATIONS + RS_QUESTS + RS_TERMS + [n for n in filtered_npc if ' ' in n])), key=len, reverse=True)
MULTI_ENTITIES = [e for e in MULTI_ENTITIES if len(e) >= 3]

SINGLE_PROPER_NAMES = {n for n in filtered_npc if ' ' not in n and n.lower() not in COMMON_WORDS_BLACKLIST}
