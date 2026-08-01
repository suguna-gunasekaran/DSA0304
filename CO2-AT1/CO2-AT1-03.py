def stem_word(word):
    rules = {
        "played":  {"stem": "play", "affix": "ed",  "type": "Inflectional"},
        "player":  {"stem": "play", "affix": "er",  "type": "Derivational"},
        "playing": {"stem": "play", "affix": "ing", "type": "Inflectional"},
    }
    return rules[word]
 
words = ["played", "player", "playing"]
 
print(f"{'Word':<10}{'Stem':<8}{'Affix':<8}{'Type':<14}{'Normalized':<12}")
print("-" * 52)
for w in words:
    info = stem_word(w)
    print(f"{w:<10}{info['stem']:<8}{info['affix']:<8}{info['type']:<14}{info['stem']:<12}")
