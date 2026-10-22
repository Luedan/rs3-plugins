import time

# Verify performance of translator simulation
print("Benchmarking performance...")

test_texts = [
    "Jacquelyn, the Slayer master in Lumbridge courtyard, can suggest monsters for you to fight.",
    "Offering bones or ashes at an altar will give an extra 50% XP compared to burying them.",
    "Great! I buy and sell pickaxes and hatchets. There are plenty to choose from, and I've some free samples too. Take your pick...or hatchet.",
    "This is completely unknown gibberish text 123456789.",
    "WHAT WOULD YOU LIKE TO SAY?",
    "Where can I find a quest?",
    "Select an Option",
    "Yes.",
    "No, thanks.",
]

# Simulate table lookups in Python (identical to Lua hash table lookup)
memory_cache = {}
failed_cache = {}

start = time.perf_counter()
for _ in range(10000):
    for t in test_texts:
        if t in memory_cache:
            res = memory_cache[t]
        elif t in failed_cache:
            res = t
        else:
            # First time
            memory_cache[t] = "Traduccion de " + t

elapsed = time.perf_counter() - start
print(f"10,000 iterations over 9 strings took: {elapsed*1000:.2f} ms")
print(f"Average per lookup: {(elapsed / (10000 * 9)) * 1000000:.4f} microseconds")
