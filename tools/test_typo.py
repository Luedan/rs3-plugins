# -*- coding: utf-8 -*-
from test_bob_translation import bob_table, lookup_npc_fuzzy

typo_text = "Great! I buy and sell pickaxes and hatchets. There is plenty to choose from, and I have some free samples too. Take your pick...or hatchet."
match = lookup_npc_fuzzy(bob_table, typo_text)
print("Fuzzy match with 2 altered words ('is' instead of 'are', 'have' instead of \"'ve\"):")
print("->", match)
assert match is not None
print("PASS: Fuzzy match handles slight wording changes!")
