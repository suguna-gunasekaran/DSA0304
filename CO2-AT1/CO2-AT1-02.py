def parse_word(word):
    rules = {
        "unhappy":   {"prefix": "un",  "suffix": "-",   "root": "happy", "type": "Derivational"},
        "happiness": {"prefix": "-",   "suffix": "ness","root": "happy", "type": "Derivational"},
        "happily":   {"prefix": "-",   "suffix": "ly",  "root": "happy", "type": "Derivational"},
    }
    return rules[word]
 
words = ["unhappy", "happiness", "happily"]
 
print(f"{'Word':<12}{'Prefix':<8}{'Suffix':<8}{'Root':<8}{'Type':<14}")
print("-" * 50)
for w in words:
    info = parse_word(w)
    print(f"{w:<12}{info['prefix']:<8}{info['suffix']:<8}{info['root']:<8}{info['type']:<14}")
