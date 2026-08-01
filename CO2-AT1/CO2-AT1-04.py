def fst_parse(word):
    rules = {
        "writes":  {"root": "write", "path": "q0 -> write -> q1 -> +s -> q2",  "type": "Regular"},
        "writing": {"root": "write", "path": "q0 -> write -> q1 -> +ing -> q2","type": "Regular"},
        "written": {"root": "write", "path": "q0 -> writ -> q1 -> +ten -> q2", "type": "Irregular"},
    }
    return rules[word]

words = ["writes", "writing", "written"]

print(f"{'Word':<10}{'Root':<8}{'Type':<12}{'State Transition Path'}")
print("-" * 65)
for w in words:
    info = fst_parse(w)
    print(f"{w:<10}{info['root']:<8}{info['type']:<12}{info['path']}")
