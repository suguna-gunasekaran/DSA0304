def analyze_word(word):
    rules = {
        "connected":  {"root": "connect", "suffix": "ed",  "type": "Inflectional"},
        "connecting": {"root": "connect", "suffix": "ing", "type": "Inflectional"},
        "connection": {"root": "connect", "suffix": "ion", "type": "Derivational"},
    }
    info = rules[word]
    normalized = info["root"]
    return info["root"], info["suffix"], info["type"], normalized
 
words = ["connected", "connecting", "connection"]
 
print(f"{'Word':<12}{'Root':<10}{'Suffix':<8}{'Type':<14}{'Normalized':<12}")
print("-" * 56)
for w in words:
    root, suffix, wtype, norm = analyze_word(w)
    print(f"{w:<12}{root:<10}{suffix:<8}{wtype:<14}{norm:<12}")
